"""Turn the UBL 2.5 example documents into CSV tables for the cross-flow consistency review.

usage: python3 -I extract_tables.py [<outdir>]        (default: <repo>/.review/tables/)
       python3 -I extract_tables.py --self-test [<n>] [<outdir>]

Reads nothing but world/examples/*/*.xml of the checkout this script sits in. Writes one CSV per
table (UTF-8, header row, rows in file order and then document order, so two runs on the same commit
give byte-identical files) and a README.md listing every table, its columns, its row count and the
commit it was built from (the commit is only in the README).

Every row carries flow, file and xpath: the absolute XPath of the element the row is about, in the
review skill's citation style (root without prefix, cac:/cbc: prefixes, [n] only where an element
repeats among its siblings), so `<flow>/<file>:<xpath>` can be cited and resolved by check_xpaths.py.

Two kinds of tables:
  generic   identifiers, dates, amounts, measures, codes, texts: one row per leaf element. Together they
            hold every leaf of every example exactly once (a leaf is an element without element
            children), classified by the end of its name: *ID; *Date, *Time; *Amount; *Measure,
            *Quantity, *Numeric, *Percent, *Rate; *Code, *Indicator; everything else is a text.
  thematic  documents, parties, party_ids, contacts, references, periods, locations, transport_means,
            shipment_stages, transport_events, transport_equipment, consignments, handling_units,
            goods_items, hazardous_items, items, item_ids, lines, taxes, exchange_rates, payment_means,
            payment_mandates, financial_accounts, payment_terms, delivery_terms, customs: one row per
            aggregate of that kind. A thematic row's columns are filled from the leaves below the
            aggregate, but not from below a nested aggregate that is itself a row of a thematic table
            (an "entity"; e.g. a party inside a consignment). Leaves that no column takes go to the
            column `other` as `relative/path=value`, so nothing below a row is lost.

Cell conventions: several values in one cell are joined with ' | ' in document order; a value with a
languageID is written `[lang] value`; `*_scheme`/`*_list` columns hold the schemeID/listID of the
values in the column before, in the same order (empty attribute -> '-'); columns marked "with unit"
append the unitCode/currencyID after a space. role_path is the element's own path from the root as
local names without prefixes or positions (e.g. Invoice/AccountingSupplierParty/Party).
Style 'nvl' (payment_terms: settlement_discount, penalty) is 'nv' plus the attributes other than
unitCode/currencyID/languageID in brackets, e.g. `PenaltyInterestRate/TimeBasisCode=ANN [listID=…]`.
"""
import csv
import fnmatch
import hashlib
import io
import random
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from lxml import etree

REPO = Path(__file__).resolve().parents[4]
EXAMPLES = REPO / 'world' / 'examples'
DEFAULT_OUT = REPO / '.review' / 'tables'
CAC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
CBC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
EXT = 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'
PREFIX = {CAC: 'cac', CBC: 'cbc', EXT: 'ext'}
SEP = ' | '
BASE = ['flow', 'file', 'xpath', 'element', 'parent', 'role_path']
CONTEXT = ['party_role', 'party_name', 'line_id', 'entity', 'entity_xpath']


# ---------------------------------------------------------------- basics

def ln(e):
    return etree.QName(e).localname


def kids(e):
    return [c for c in e if isinstance(c.tag, str)]


def is_leaf(e):
    return not kids(e)


def text(e):
    return e.text or ''


def fmt(e):
    lang = e.get('languageID')
    return f'[{lang}] {text(e)}' if lang else text(e)


def unit(e):
    return e.get('unitCode') or e.get('currencyID') or ''


def extra_attrs(e):
    """' [listID=… schemeID=…]' for the attributes that fmt/fmt_unit do not show, else ''."""
    a = ' '.join(f'{k}={v}' for k, v in sorted(e.attrib.items()) if k not in ('unitCode', 'currencyID', 'languageID'))
    return f' [{a}]' if a else ''


def fmt_unit(e):
    u = unit(e)
    return f'{fmt(e)} {u}' if u else fmt(e)


def attrs(e):
    return ' '.join(f'{k}={v}' for k, v in sorted(e.attrib.items()))


def join(values):
    return SEP.join(v for v in values)


class Doc:
    """One example: its tree, XPaths and role paths."""

    def __init__(self, path):
        self.path = path
        self.flow = path.parent.name
        self.file = path.name
        self.tree = etree.parse(str(path))
        self.root = self.tree.getroot()
        self._xp = {}

    def xpath(self, e):
        if e in self._xp:
            return self._xp[e]
        p = e.getparent()
        if p is None:
            s = '/' + ln(e)
        else:
            q = etree.QName(e)
            step = f'{PREFIX.get(q.namespace, "?")}:{q.localname}'
            same = [c for c in p if c.tag == e.tag]
            if len(same) > 1:
                step += f'[{same.index(e) + 1}]'
            s = self.xpath(p) + '/' + step
        self._xp[e] = s
        return s

    @staticmethod
    def role_path(e):
        names = [ln(a) for a in e.iterancestors()][::-1]
        return '/'.join(names + [ln(e)])

    def base(self, e):
        p = e.getparent()
        return {'flow': self.flow, 'file': self.file, 'xpath': self.xpath(e), 'element': ln(e),
                'parent': ln(p) if p is not None else '', 'role_path': self.role_path(e)}


# ---------------------------------------------------------------- what is what

def is_party(e):
    """A PartyType element: cac:Party itself or a role element of PartyType (CarrierParty …).
    Wrappers such as AccountingSupplierParty contain a cac:Party and are not parties themselves."""
    n = ln(e)
    if not n.endswith('Party') or is_leaf(e):
        return False
    return not any(ln(c) == 'Party' for c in kids(e))


def party_role(p):
    return ln(p.getparent()) if ln(p) == 'Party' and p.getparent() is not None else ln(p)


def first(e, *paths):
    """Text of the first leaf found under one of the local-name paths (relative)."""
    for path in paths:
        cur = [e]
        for step in path.split('/'):
            cur = [c for x in cur for c in kids(x) if ln(c) == step]
        for c in cur:
            if text(c):
                return text(c)
    return ''


def party_name(p):
    n = first(p, 'PartyName/Name', 'PartyLegalEntity/RegistrationName', 'TradePartyName/Name')
    if not n:
        person = [c for c in kids(p) if ln(c) == 'Person']
        if person:
            n = ' '.join(x for x in (first(person[0], 'FirstName'), first(person[0], 'FamilyName')) if x)
    return n


def is_line(e):
    n = ln(e)
    return (n.endswith('Line') or n.endswith('LineItem')) and n != 'AddressLine' and not is_leaf(e)


def is_item(e):
    if ln(e) not in ('Item', 'SupplyItem') or is_leaf(e):
        return False
    return True


LOCATION_EXCLUDED = {'JurisdictionRegionAddress', 'RegistrationAddress', 'ElectronicAddress'}


def is_location(e):
    n = ln(e)
    if not (n.endswith('Location') or n.endswith('Address')) or is_leaf(e) or n in LOCATION_EXCLUDED:
        return False
    p = e.getparent()
    if n == 'PostalAddress' and p is not None and is_party(p):
        return False  # the party's own postal address: columns of the parties table
    if p is not None and ln(p) in ('FinancialInstitution', 'FinancialInstitutionBranch'):
        return False  # columns of financial_accounts
    if p is not None and is_location(p):
        return False  # the address of a location: part of the location row
    return True


def is_reference(e):
    return ln(e).endswith('Reference') and not is_leaf(e)


def ends(*suffixes):
    return lambda e: not is_leaf(e) and any(ln(e).endswith(s) for s in suffixes)


def named(*names):
    return lambda e: not is_leaf(e) and ln(e) in names


def is_tax(e):
    n = ln(e)
    if is_leaf(e):
        return False
    if n == 'TaxSubtotal':
        return True
    return n.endswith('TaxCategory') and ln(e.getparent()) != 'TaxSubtotal'


def is_contact(e):
    n = ln(e)
    return not is_leaf(e) and (n.endswith('Contact') or n.endswith('Person') or n == 'Person')


# ---------------------------------------------------------------- column specs
# (column, patterns, style): patterns are fnmatch patterns on the leaf's path relative to the row
# element ('*' also crosses '/'); style: 'v' value, 'u' value with unit, '@attr' attribute of the
# matched leaves, 'nv' 'relpath=value unit'. A callable column gets (doc, element) and returns text.

def c(name, *patterns, style='v'):
    return (name, patterns, style)


ADDRESS = [
    c('address_id', 'PostalAddress/ID'), c('address_id_scheme', 'PostalAddress/ID', style='@schemeID'),
    c('address_type', 'PostalAddress/AddressTypeCode'), c('address_format', 'PostalAddress/AddressFormatCode'),
    c('street', 'PostalAddress/StreetName'), c('additional_street', 'PostalAddress/AdditionalStreetName'),
    c('building_number', 'PostalAddress/BuildingNumber'), c('block_name', 'PostalAddress/BlockName'),
    c('plot', 'PostalAddress/PlotIdentification'), c('address_line', 'PostalAddress/AddressLine/Line'),
    c('postbox', 'PostalAddress/Postbox'), c('floor', 'PostalAddress/Floor'), c('room', 'PostalAddress/Room'),
    c('address_department', 'PostalAddress/Department'), c('mark_attention', 'PostalAddress/MarkAttention'),
    c('inhouse_mail', 'PostalAddress/InhouseMail'),
    c('city_subdivision', 'PostalAddress/CitySubdivisionName'), c('city', 'PostalAddress/CityName'),
    c('postal_zone', 'PostalAddress/PostalZone'), c('subentity', 'PostalAddress/CountrySubentity'),
    c('subentity_code', 'PostalAddress/CountrySubentityCode'), c('region', 'PostalAddress/Region'),
    c('district', 'PostalAddress/District'), c('timezone', 'PostalAddress/TimezoneOffset'),
    c('country', 'PostalAddress/Country/IdentificationCode'), c('country_name', 'PostalAddress/Country/Name'),
    c('address_coordinates', 'PostalAddress/LocationCoordinate/*', style='nv'),
    c('address_description', 'PostalAddress/Description'),
]


def wrapper_extras(doc, p):
    """Leaves of the role wrapper around a cac:Party (QualifyingParty: EmployeeQuantity …),
    outside the party and outside nested entities."""
    if ln(p) != 'Party' or p.getparent() is None:
        return ''
    w = p.getparent()
    out = []
    for rel, leaf in flatten(w, skip=p):
        out.append(f'{rel}={fmt_unit(leaf)}')
    return join(out)


def contact_names(doc, p):
    return join(f'{ln(x)}={first(x, "Name") or " ".join(filter(None, (first(x, "FirstName"), first(x, "FamilyName"))))}'
                for x in kids(p) if is_contact(x))


def shareholders(doc, p):
    out = []
    for le in kids(p):
        if ln(le) != 'PartyLegalEntity':
            continue
        for sh in kids(le):
            if ln(sh) == 'ShareholderParty':
                inner = [x for x in kids(sh) if ln(x) == 'Party']
                out.append(f'{party_name(inner[0]) if inner else "?"} {first(sh, "ParticipationPercent")}%')
    return join(out)


PARTY_COLS = [
    c('role', style=lambda d, e: party_role(e)),
    c('name', 'PartyName/Name'), c('trade_name', 'TradePartyName/Name'),
    c('party_id', 'PartyIdentification/ID'), c('party_id_scheme', 'PartyIdentification/ID', style='@schemeID'),
    c('additional_party_id', 'AdditionalPartyIdentification/ID'),
    c('additional_party_id_scheme', 'AdditionalPartyIdentification/ID', style='@schemeID'),
    c('endpoint', 'ElectronicAddress/ElectronicAddressID', 'EndpointID'),
    c('endpoint_scheme', 'ElectronicAddress/ElectronicAddressID', 'EndpointID', style='@schemeID'),
    c('exchange_network', 'ElectronicAddress/ExchangeNetworkID'),
    c('website', 'WebsiteURI'), c('additional_website', 'AdditionalWebSite/*', style='nv'),
    c('social_media', 'SocialMediaProfile/*', style='nv'), c('logo', 'LogoReferenceID'),
    c('industry_code', 'IndustryClassificationCode'),
    c('industry_code_list', 'IndustryClassificationCode', style='@listID'),
    c('language_id', 'Language/ID'), c('language_name', 'Language/Name'), c('locale', 'Language/LocaleCode'),
    c('party_type_code', 'PartyTypeCode'), c('party_type', 'PartyType'),
] + ADDRESS + [
    c('legal_name', 'PartyLegalEntity/RegistrationName'),
    c('legal_company_id', 'PartyLegalEntity/CompanyID'),
    c('legal_company_id_scheme', 'PartyLegalEntity/CompanyID', style='@schemeID'),
    c('legal_form_code', 'PartyLegalEntity/CompanyLegalFormCode'),
    c('legal_form', 'PartyLegalEntity/CompanyLegalForm'),
    c('registration_date', 'PartyLegalEntity/RegistrationDate'),
    c('registration_expiration_date', 'PartyLegalEntity/RegistrationExpirationDate'),
    c('size_code', 'PartyLegalEntity/EntitySizeCode'),
    c('liquidation_status', 'PartyLegalEntity/CompanyLiquidationStatusCode'),
    c('stock_amount', 'PartyLegalEntity/CorporateStockAmount', style='u'),
    c('fully_paid_shares', 'PartyLegalEntity/FullyPaidSharesIndicator'),
    c('sole_proprietorship', 'PartyLegalEntity/SoleProprietorshipIndicator'),
    c('legal_registration_city', 'PartyLegalEntity/RegistrationAddress/CityName'),
    c('legal_registration_country', 'PartyLegalEntity/RegistrationAddress/Country/IdentificationCode'),
    c('corporate_scheme_id', 'PartyLegalEntity/CorporateRegistrationScheme/ID'),
    c('corporate_scheme_name', 'PartyLegalEntity/CorporateRegistrationScheme/Name'),
    c('corporate_registration_type', 'PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode'),
    c('corporate_scheme_country',
      'PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode'),
    c('security_listing', 'PartyLegalEntity/SecurityListing/*', style='nv'),
    c('shareholders', style=shareholders),
    c('shareholder_percent', 'PartyLegalEntity/ShareholderParty/ParticipationPercent'),
    c('service_provider', 'ServiceProviderParty/*', style='nv'),
    c('power_of_attorney', 'PowerOfAttorney/*', style='nv'),
    c('tax_registration_name', 'PartyTaxScheme/RegistrationName'),
    c('tax_company_id', 'PartyTaxScheme/CompanyID'),
    c('tax_company_id_scheme', 'PartyTaxScheme/CompanyID', style='@schemeID'),
    c('tax_level', 'PartyTaxScheme/TaxLevelCode'),
    c('tax_scheme', 'PartyTaxScheme/TaxScheme/ID'),
    c('tax_scheme_currency', 'PartyTaxScheme/TaxScheme/CurrencyCode'),
    c('tax_scheme_country', 'PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode'),
    c('tax_scheme_subentity', 'PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity'),
    c('tax_exemption_code', 'PartyTaxScheme/ExemptionReasonCode'),
    c('tax_exemption_reason', 'PartyTaxScheme/ExemptionReason'),
    c('tax_registration_address', 'PartyTaxScheme/RegistrationAddress/*', style='nv'),
    c('authorizations', 'PartyAuthorization/*', style='nv'),
    c('contacts', style=contact_names),
    c('role_extras', style=wrapper_extras),
]

CONTACT_COLS = [
    c('kind', style=lambda d, e: 'person' if ln(e).endswith('Person') else 'contact'),
    c('id', 'ID'), c('name', 'Name'), c('first_name', 'FirstName'), c('middle_name', 'MiddleName'),
    c('family_name', 'FamilyName'), c('other_name', 'OtherName'), c('name_suffix', 'NameSuffix'),
    c('title', 'Title'), c('job_title', 'JobTitle'), c('department', 'Department', 'OrganizationDepartment'),
    c('role_code', 'RoleCode'), c('telephone', 'Telephone'), c('telefax', 'Telefax'),
    c('mail', 'ElectronicMail'), c('other_communication', 'OtherCommunication/*', style='nv'),
    c('note', 'Note'), c('nationality', 'NationalityID', 'NationalityCode', 'CitizenshipCountry/IdentificationCode'),
    c('national_id', 'NationalID'), c('birth_date', 'BirthDate'), c('birthplace', 'BirthplaceName'),
    c('gender', 'GenderCode'),
]

LOC_ADDR = ['', '*Address/', 'Address/']


def la(name, leaf, style='v'):
    return c(name, *[p + leaf for p in LOC_ADDR], style=style)


LOCATION_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('name', 'Name'), c('description', 'Description'),
    c('type_code', 'LocationTypeCode'), c('conditions', 'Conditions'), c('information_uri', 'InformationURI'),
    la('address_type', 'AddressTypeCode'), la('address_format', 'AddressFormatCode'), la('timezone', 'TimezoneOffset'),
    la('city_subdivision', 'CitySubdivisionName'),
    c('subentity_location', 'CountrySubentity', 'CountrySubentityCode'),
    c('address_id', '*Address/ID'),
    c('address_id_scheme', '*Address/ID', style='@schemeID'),
    la('street', 'StreetName'), la('additional_street', 'AdditionalStreetName'),
    la('building_number', 'BuildingNumber'), la('building_name', 'BuildingName'), la('city', 'CityName'),
    la('postal_zone', 'PostalZone'), c('subentity', '*Address/CountrySubentity'),
    c('subentity_code', '*Address/CountrySubentityCode'), la('region', 'Region'), la('district', 'District'),
    la('address_line', 'AddressLine/Line'),
    c('country', 'Country/IdentificationCode', '*Address/Country/IdentificationCode'),
    c('country_name', 'Country/Name', '*Address/Country/Name'),
    c('latitude', 'LocationCoordinate/Latitude*', '*Address/LocationCoordinate/Latitude*', style='u'),
    c('longitude', 'LocationCoordinate/Longitude*', '*Address/LocationCoordinate/Longitude*', style='u'),
    c('coordinate_system', '*LocationCoordinate/CoordinateSystemCode'),
    c('altitude', '*LocationCoordinate/AltitudeMeasure', style='u'),
]


def child_entities(doc, e, test, describe):
    return join(f'{ln(x)}={describe(x)}' for x in kids(e) if test(x))


def loc_brief(x):
    parts = [first(x, 'ID'), first(x, 'Name') or first(x, 'Description') or first(x, 'Address/CityName')
             or first(x, 'CityName')]
    return ' '.join(p for p in parts if p) or '?'


def event_brief(x):
    d = first(x, 'OccurrenceDate')
    t = first(x, 'OccurrenceTime')
    per = [p for p in kids(x) if ln(p).endswith('Period')]
    if not d and per:
        d = (first(per[0], 'StartDate') + ' ' + first(per[0], 'StartTime')).strip() + ' – ' + \
            (first(per[0], 'EndDate') + ' ' + first(per[0], 'EndTime')).strip()
    where = [loc for loc in kids(x) if is_location(loc)]
    return ' '.join(s for s in (d, t, f'@{loc_brief(where[0])}' if where else '') if s) or '?'


def means_brief(x):
    for p in ('MaritimeTransport/VesselID', 'MaritimeTransport/VesselName', 'RoadTransport/LicensePlateID',
              'RailTransport/TrainID', 'RailTransport/RailCarID', 'AirTransport/AircraftID', 'JourneyID'):
        v = first(x, p)
        if v:
            return f'{p.split("/")[-1]}={v}'
    return '?'


def parties_of(doc, e):
    out = []
    for x in kids(e):
        if is_party(x):
            out.append(f'{ln(x)}={party_name(x) or "?"}')
        elif ln(x).endswith('Party') and not is_leaf(x):
            for p in kids(x):
                if ln(p) == 'Party':
                    out.append(f'{ln(x)}={party_name(p) or "?"}')
    return join(out)


PLACES = c('places', style=lambda d, e: child_entities(d, e, is_location, loc_brief))
EVENTS = c('events', style=lambda d, e: child_entities(d, e, ends('TransportEvent', 'ArrivalEvent'), event_brief))
MEANS = c('transport_means', style=lambda d, e: child_entities(d, e, ends('TransportMeans'), means_brief))
PARTIES = c('parties', style=parties_of)
MEASUREMENT = c('measurement_dimensions', '*MeasurementDimension/*', '*SpaceMeasurementDimension/*', style='nv')

TRANSPORT_MEANS_COLS = [
    c('journey_id', 'JourneyID'), c('type_code', 'TransportMeansTypeCode'), c('direction', 'DirectionCode'),
    c('trade_service_code', 'TradeServiceCode'),
    c('registration_nationality_id', 'RegistrationNationalityID'),
    c('registration_nationality', 'RegistrationNationality'),
    c('vessel_id', 'MaritimeTransport/VesselID'), c('vessel_id_scheme', 'MaritimeTransport/VesselID', style='@schemeID'),
    c('vessel_name', 'MaritimeTransport/VesselName'), c('call_sign', 'MaritimeTransport/RadioCallSignID'),
    c('mmsi', 'MaritimeTransport/MMSIRegistrationID'),
    c('ship_type', 'MaritimeTransport/ShipTypeCode', 'MaritimeTransport/ShipsRequirements'),
    c('tonnage', 'MaritimeTransport/*TonnageMeasure', style='nv'),
    c('license_plate', 'RoadTransport/LicensePlateID'),
    c('license_plate_scheme', 'RoadTransport/LicensePlateID', style='@schemeID'),
    c('trailer_plate', 'RoadTransport/TrailerLicensePlateID'),
    c('train_id', 'RailTransport/TrainID'), c('rail_car_id', 'RailTransport/RailCarID'),
    c('rail_car_id_scheme', 'RailTransport/RailCarID', style='@schemeID'),
    c('aircraft_id', 'AirTransport/AircraftID'), c('aircraft_id_scheme', 'AirTransport/AircraftID', style='@schemeID'),
    MEASUREMENT, PARTIES, PLACES,
]

STAGE_COLS = [
    c('id', 'ID'), c('mode', 'TransportModeCode'), c('mode_list', 'TransportModeCode', style='@listID'),
    c('means_type', 'TransportMeansTypeCode'), c('direction', 'TransitDirectionCode'),
    c('estimated_delivery', 'EstimatedDeliveryDate', 'EstimatedDeliveryTime'),
    c('required_delivery', 'RequiredDeliveryDate', 'RequiredDeliveryTime'),
    c('loading_sequence', 'LoadingSequenceID'), c('transit_period', 'TransitPeriod/*', style='nv'),
    c('instructions', 'Instructions'), c('quantities', '*Quantity', style='nv'),
    MEANS, PLACES, EVENTS, PARTIES,
]

EVENT_COLS = [
    c('id', 'IdentificationID', 'ID'), c('type_code', 'TransportEventTypeCode'),
    c('occurrence_date', 'OccurrenceDate'), c('occurrence_time', 'OccurrenceTime'),
    c('timestamp', style=lambda d, e: ('T'.join(x for x in (first(e, 'OccurrenceDate'), first(e, 'OccurrenceTime')) if x))),
    c('period', 'Period/*', style='nv'), c('description', 'Description'),
    c('completion', 'CompletionIndicator'), c('status', 'CurrentStatus/*', style='nv'),
    PLACES, PARTIES,
]

EQUIPMENT_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('referenced_consignment', 'ReferencedConsignmentID'),
    c('type_code', 'TransportEquipmentTypeCode'), c('size_type', 'SizeTypeCode'),
    c('provider_type', 'ProviderTypeCode'), c('owner_type', 'OwnerTypeCode'), c('disposition', 'DispositionCode'),
    c('fullness', 'FullnessIndicationCode'), c('stowage_position', 'StowagePositionID'),
    c('seals', 'TransportEquipmentSeal/*', style='nv'),
    c('tare_weight', 'TareWeightMeasure', style='u'), c('gross_weight', 'GrossWeightMeasure', style='u'),
    c('gross_volume', 'GrossVolumeMeasure', style='u'), c('verified_gross_mass', 'VerifiedGrossMass/*', style='nv'),
    c('temperatures', '*Temperature/*', style='nv'), MEASUREMENT,
    c('description', 'Description', 'Characteristics', 'Information', 'DamageRemarks'),
    MEANS, PLACES, EVENTS, PARTIES,
]

CONSIGNMENT_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('assigned_ids', '*AssignedID', 'SequenceID', style='nv'),
    c('weights', '*WeightMeasure', style='nv'), c('volumes', '*VolumeMeasure', style='nv'),
    c('counts', '*Quantity', style='nv'), c('values', '*Amount', style='nv'),
    c('summary', 'SummaryDescription', 'Information', 'Remarks'),
    c('handling', 'HandlingCode', 'HandlingInstructions'),
    c('countries', '*Country/IdentificationCode', style='nv'),
    MEANS, PLACES, EVENTS, PARTIES,
]

HANDLING_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('trace_id', 'TraceID'),
    c('trace_id_scheme', 'TraceID', style='@schemeID'),
    c('type_code', 'TransportHandlingUnitTypeCode', 'PackagingTypeCode'),
    c('type_code_list', 'TransportHandlingUnitTypeCode', 'PackagingTypeCode', style='@listID'),
    c('level_code', 'PackageLevelCode'), c('quantities', '*Quantity', style='nv'),
    c('packing_material', 'PackingMaterial', 'PackagingType'), MEASUREMENT,
    c('shipping_marks', 'ShippingMarks'), c('handling', 'HandlingCode', 'HandlingInstructions'),
    c('weights', '*WeightMeasure', style='nv'), PLACES,
]

GOODS_COLS = [
    c('id', 'ID'), c('sequence', 'SequenceNumberID'), c('description', 'Description'),
    c('quantities', '*Quantity', style='nv'), c('weights', '*WeightMeasure', style='nv'),
    c('volumes', '*VolumeMeasure', style='nv'), c('values', '*Amount', style='nv'),
    c('customs', 'Customs*', 'RequiredCustomsID', 'PreferenceCriterionCode', style='nv'),
    c('item_names', style=lambda d, e: join(first(i, 'Name') for i in kids(e) if is_item(i))),
    PLACES,
]

HAZARD_COLS = [
    c('id', 'ID'), c('un_number', 'UNDGCode'), c('un_number_list', 'UNDGCode', style='@listID'),
    c('hazard_class', 'HazardClassID'), c('packing_group', 'UNPackingGroupCode', 'UNPackingGroup'),
    c('proper_shipping_name', 'ProperShippingName'), c('technical_name', 'TechnicalName'),
    c('category', 'HazardousCategoryCode', 'CategoryName'), c('marking', 'MarkingID'),
    c('placard', 'PlacardNotation', 'PlacardEndorsement'), c('emergency', 'EmergencyProceduresCode'),
    c('tunnel', 'TunnelRestrictionCode'), c('weights', '*WeightMeasure', style='nv'),
    c('volumes', '*VolumeMeasure', style='nv'), c('temperatures', '*Temperature/*', style='nv'),
    c('radioactive', 'RadioactiveMaterial/*', style='nv'), c('secondary', 'SecondaryHazard/*', style='nv'),
]


def item_main_id(i):
    for p in ('SellersItemIdentification/ID', 'StandardItemIdentification/ID', 'BuyersItemIdentification/ID',
              'ManufacturersItemIdentification/ID', 'CatalogueItemIdentification/ID'):
        v = first(i, p)
        if v:
            return f'{p.split("/")[0]}={v}'
    return ''


def item_hazard(doc, i):
    return join(f'UN{first(h, "UNDGCode")} class {first(h, "HazardClassID")} PG {first(h, "UNPackingGroupCode")}'
                for h in kids(i) if ln(h).endswith('HazardousItem'))


def line_of(e):
    for a in e.iterancestors():
        if is_line(a):
            return a
    return None


ITEM_COLS = [
    c('main_id', style=lambda d, e: item_main_id(e)),
    c('name', 'Name'), c('description', 'Description'), c('brand', 'BrandName'), c('model', 'ModelName'),
    c('keyword', 'Keyword'), c('additional_information', 'AdditionalInformation'),
    c('warranty', 'WarrantyInformation'), c('pack', 'PackQuantity', 'PackSizeNumeric', style='nv'),
    c('sellers_id', 'SellersItemIdentification/ID'), c('sellers_extended_id', 'SellersItemIdentification/ExtendedID'),
    c('buyers_id', 'BuyersItemIdentification/ID'), c('manufacturers_id', 'ManufacturersItemIdentification/ID'),
    c('standard_id', 'StandardItemIdentification/ID'),
    c('standard_id_scheme', 'StandardItemIdentification/ID', style='@schemeID'),
    c('catalogue_id', 'CatalogueItemIdentification/ID'),
    c('additional_id', 'AdditionalItemIdentification/ID'),
    c('additional_id_scheme', 'AdditionalItemIdentification/ID', style='@schemeID'),
    c('commodity_code', 'CommodityClassification/CommodityCode'),
    c('commodity_code_list', 'CommodityClassification/CommodityCode', style='@listID'),
    c('item_classification', 'CommodityClassification/ItemClassificationCode'),
    c('item_classification_list', 'CommodityClassification/ItemClassificationCode', style='@listID'),
    c('nature_code', 'CommodityClassification/NatureCode'), c('cargo_type', 'CommodityClassification/CargoTypeCode'),
    c('origin_country', 'OriginCountry/IdentificationCode'),
    c('origin_address', style=lambda d, e: child_entities(d, e, is_location, loc_brief)),
    c('dimensions', 'Dimension/*', style='nv'),
    c('physical', 'SellersItemIdentification/PhysicalAttribute/*', 'SellersItemIdentification/MeasurementDimension/*',
      style='nv'),
    c('hazardous', style=item_hazard), c('hazardous_risk', 'HazardousRiskIndicator'),
    c('properties', 'AdditionalItemProperty/*', style='nv'),
    c('emissions', 'EnvironmentalEmission/*', style='nv'), c('circularity', 'CircularityProfile/*', style='nv'),
    c('instances', 'ItemInstance/*', style='nv'), c('certificates', '*Certificate/*', style='nv'),
    c('line_kind', style=lambda d, e: ln(line_of(e)) if line_of(e) is not None else ''),
    c('line_xpath', style=lambda d, e: d.xpath(line_of(e)) if line_of(e) is not None else ''),
]


def line_item(e):
    for x in kids(e):
        if is_item(x):
            return x
    for x in kids(e):  # OrderLine/LineItem/Item
        if is_line(x):
            for y in kids(x):
                if is_item(y):
                    return y
    return None


def line_refs(doc, e):
    out = []
    for x in kids(e):
        if is_reference(x):
            v = first(x, 'LineID') or first(x, 'ID') or first(x, 'DocumentReference/ID')
            doc_id = first(x, 'DocumentReference/ID')
            out.append(f'{ln(x)}={v}' + (f' in {doc_id}' if doc_id and doc_id != v else ''))
    return join(out)


LINE_COLS = [
    c('id', 'ID'), c('uuid', 'UUID'), c('status', 'LineStatusCode'),
    c('quantities', '*Quantity', style='nv'),
    c('line_amount', 'LineExtensionAmount', style='u'), c('amounts', '*Amount', style='nv'),
    c('price', 'Price/PriceAmount', style='u'), c('base_quantity', 'Price/BaseQuantity', style='u'),
    c('references', style=line_refs),
    c('item_main_id', style=lambda d, e: item_main_id(line_item(e)) if line_item(e) is not None else ''),
    c('item_name', style=lambda d, e: first(line_item(e), 'Name') if line_item(e) is not None else ''),
    c('note', 'Note'),
]


def ref_matches(index):
    def f(doc, e):
        rid = first(e, 'ID')
        return join(m['where'] for m in index.get(rid, []) if m['where'] != f'{doc.flow}/{doc.file}')
    return f


REFERENCE_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('uuid', 'UUID'), c('line_id', 'LineID'),
    c('issue_date', 'IssueDate'), c('issue_time', 'IssueTime'),
    c('type_code', 'DocumentTypeCode'), c('type_code_list', 'DocumentTypeCode', style='@listID'),
    c('document_type', 'DocumentType'), c('description', 'DocumentDescription', 'Description'),
    c('status', 'DocumentStatusCode'), c('nested_document_id', 'DocumentReference/ID'),
    c('validity', 'ValidityPeriod/*', style='nv'),
    c('attachment', 'Attachment/ExternalReference/URI', 'Attachment/ExternalReference/*'),
    PARTIES,
]

PERIOD_COLS = [
    c('start_date', 'StartDate'), c('start_time', 'StartTime'), c('end_date', 'EndDate'), c('end_time', 'EndTime'),
    c('start', style=lambda d, e: 'T'.join(x for x in (first(e, 'StartDate'), first(e, 'StartTime')) if x)),
    c('end', style=lambda d, e: 'T'.join(x for x in (first(e, 'EndDate'), first(e, 'EndTime')) if x)),
    c('duration', 'DurationMeasure', style='u'), c('description_code', 'DescriptionCode'),
    c('description', 'Description'),
]

SUPPLIER_ROLES = ('AccountingSupplierParty', 'SellerSupplierParty')
CUSTOMER_ROLES = ('AccountingCustomerParty', 'BuyerCustomerParty', 'CustomerParty', 'ContractingParty')


def top_leaf(doc, name):
    """Text of the document's own (top-level) leaf with this name, else ''."""
    return join(fmt(x) for x in kids(doc.root) if ln(x) == name and is_leaf(x))


def doc_party(doc, roles):
    """(role, party) of the first top-level role in `roles` (in that priority) that the document has,
    else ('', None). The party is the cac:Party inside the role wrapper, or the role element itself."""
    for role in roles:
        for ch in kids(doc.root):
            if ln(ch) == role and not is_leaf(ch):
                inner = [p for p in kids(ch) if ln(p) == 'Party']
                return role, (inner[0] if inner else ch)
    return '', None


def party_country(p):
    return first(p, 'PostalAddress/Country/IdentificationCode') if p is not None else ''


TAX_COLS = [
    c('kind', style=lambda d, e: ln(e)),
    c('taxable_amount', 'TaxableAmount', style='u'), c('tax_amount', 'TaxAmount', style='u'),
    c('transaction_currency_tax', 'TransactionCurrencyTaxAmount', style='u'),
    c('percent', 'Percent', 'TaxCategory/Percent'), c('category', 'ID', 'TaxCategory/ID'),
    c('category_scheme', 'ID', 'TaxCategory/ID', style='@schemeID'), c('category_name', 'Name', 'TaxCategory/Name'),
    c('per_unit', '*PerUnitAmount', style='u'), c('base_unit', '*BaseUnitMeasure', style='u'),
    c('exemption_code', '*TaxExemptionReasonCode'), c('exemption_reason', '*TaxExemptionReason'),
    c('tax_scheme', '*TaxScheme/ID'), c('tax_scheme_name', '*TaxScheme/Name'),
    c('tax_scheme_currency', '*TaxScheme/CurrencyCode'),
    c('jurisdiction', '*TaxScheme/JurisdictionRegionAddress/*', style='nv'),
    c('supply_type', 'SupplyTypeCode'),
    c('total_tax_amount', style=lambda d, e: first(e.getparent(), 'TaxAmount') if ln(e.getparent()).endswith('TaxTotal') else ''),
    c('document_currency', style=lambda d, e: top_leaf(d, 'DocumentCurrencyCode')),
    c('supplier_role', style=lambda d, e: doc_party(d, SUPPLIER_ROLES)[0]),
    c('supplier', style=lambda d, e: party_name(doc_party(d, SUPPLIER_ROLES)[1]) if doc_party(d, SUPPLIER_ROLES)[1] is not None else ''),
    c('supplier_country', style=lambda d, e: party_country(doc_party(d, SUPPLIER_ROLES)[1])),
    c('customer_role', style=lambda d, e: doc_party(d, CUSTOMER_ROLES)[0]),
    c('customer', style=lambda d, e: party_name(doc_party(d, CUSTOMER_ROLES)[1]) if doc_party(d, CUSTOMER_ROLES)[1] is not None else ''),
    c('customer_country', style=lambda d, e: party_country(doc_party(d, CUSTOMER_ROLES)[1])),
]

RATE_COLS = [
    c('source_currency', 'SourceCurrencyCode'), c('source_base_rate', 'SourceCurrencyBaseRate'),
    c('target_currency', 'TargetCurrencyCode'), c('target_base_rate', 'TargetCurrencyBaseRate'),
    c('rate', 'CalculationRate'), c('operator', 'MathematicOperatorCode'), c('date', 'Date'),
    c('market', 'ExchangeMarketID'), c('contract', 'ForeignExchangeContract/*', style='nv'),
    c('document_currency', style=lambda d, e: top_leaf(d, 'DocumentCurrencyCode')),
    c('tax_currency', style=lambda d, e: top_leaf(d, 'TaxCurrencyCode')),
    c('pricing_currency', style=lambda d, e: top_leaf(d, 'PricingCurrencyCode')),
    c('payment_currency', style=lambda d, e: top_leaf(d, 'PaymentCurrencyCode')),
    c('payment_alternative_currency', style=lambda d, e: top_leaf(d, 'PaymentAlternativeCurrencyCode')),
]


def acct_brief(x):
    return ' '.join(s for s in (first(x, 'ID'), first(x, 'Name')) if s) or '?'


PAYMENT_MEANS_COLS = [
    c('id', 'ID'), c('code', 'PaymentMeansCode'), c('code_list', 'PaymentMeansCode', style='@listID'),
    c('due_date', 'PaymentDueDate'), c('channel', 'PaymentChannelCode'), c('channel_list', 'PaymentChannelCode', style='@listID'),
    c('rail_id', 'PaymentRailID'), c('rail_id_scheme', 'PaymentRailID', style='@schemeID'),
    c('platform_id', 'PaymentPlatformID'), c('description', 'PaymentMeansDescription'),
    c('charge_bearer', 'ChargeBearerCode'), c('instruction_id', 'InstructionID'), c('instruction_note', 'InstructionNote'), c('payment_id', 'PaymentID'),
    c('card', 'CardAccount/*', style='nv'), c('credit_account', 'CreditAccount/*', style='nv'),
    c('accounts', style=lambda d, e: child_entities(d, e, ends('FinancialAccount'), acct_brief)),
    c('mandates', style=lambda d, e: child_entities(d, e, named('PaymentMandate'), lambda x: first(x, 'ID'))),
]

MANDATE_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('type', 'MandateTypeCode'),
    c('max_payments', 'MaximumPaymentInstructionsNumeric'), c('max_amount', 'MaximumPaidAmount', style='u'),
    c('signature_id', 'SignatureID'), c('validity', 'ValidityPeriod/*', style='nv'),
    c('payment_reversal', 'PaymentReversalPeriod/*', style='nv'), c('clause', 'Clause/*', style='nv'),
    c('accounts', style=lambda d, e: child_entities(d, e, ends('FinancialAccount'), acct_brief)),
    PARTIES,
]

ACCOUNT_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('name', 'Name'), c('alias', 'AliasName'),
    c('type', 'AccountTypeCode'), c('format', 'AccountFormatCode'), c('currency', 'CurrencyCode'),
    c('payment_note', 'PaymentNote'),
    c('country', 'Country/IdentificationCode'),
    c('branch_id', 'FinancialInstitutionBranch/ID'), c('branch_id_scheme', 'FinancialInstitutionBranch/ID', style='@schemeID'),
    c('branch_name', 'FinancialInstitutionBranch/Name'),
    c('branch_address', 'FinancialInstitutionBranch/Address/*', style='nv'),
    c('institution_id', 'FinancialInstitutionBranch/FinancialInstitution/ID'),
    c('institution_id_scheme', 'FinancialInstitutionBranch/FinancialInstitution/ID', style='@schemeID'),
    c('institution_name', 'FinancialInstitutionBranch/FinancialInstitution/Name'),
    c('institution_address', 'FinancialInstitutionBranch/FinancialInstitution/Address/*', style='nv'),
]

PAYMENT_TERMS_COLS = [
    c('id', 'ID'), c('means_id', 'PaymentMeansID'), c('prepaid_payment_reference', 'PrepaidPaymentReferenceID'),
    c('note', 'Note'), c('reference_event', 'ReferenceEventCode'),
    c('reference_event_list', 'ReferenceEventCode', style='@listID'), c('percent', 'PaymentPercent'),
    c('amount', 'Amount', style='u'),
    c('settlement_discount', 'SettlementDiscount*', 'SettlementPeriod/*', style='nvl'),
    c('penalty', 'Penalty*', style='nvl'), c('due_date', 'PaymentDueDate'), c('installment_due_date', 'InstallmentDueDate'),
    c('invoicing_party_reference', 'InvoicingPartyReference'),
    c('periods', '*Period/*', style='nv'), c('details_uri', 'PaymentTermsDetailsURI'),
]

DELIVERY_TERMS_COLS = [
    c('id', 'ID'), c('id_scheme', 'ID', style='@schemeID'), c('special_terms', 'SpecialTerms'),
    c('loss_risk', 'LossRisk*', style='nv'), c('amount', 'Amount', style='u'),
    PLACES,
]


# ---------------------------------------------------------------- entities and flattening

ENTITIES = [  # (table, test, columns); the first matching test decides the table of an element
    ('parties', is_party, PARTY_COLS),
    ('contacts', is_contact, CONTACT_COLS),
    ('references', is_reference, REFERENCE_COLS),
    ('locations', is_location, LOCATION_COLS),
    ('transport_means', ends('TransportMeans'), TRANSPORT_MEANS_COLS),
    ('shipment_stages', ends('ShipmentStage'), STAGE_COLS),
    ('transport_events', ends('TransportEvent', 'RequestedArrivalEvent'), EVENT_COLS),
    ('transport_equipment', ends('TransportEquipment'), EQUIPMENT_COLS),
    ('consignments', ends('Consignment', 'Shipment'), CONSIGNMENT_COLS),
    ('handling_units', ends('TransportHandlingUnit', 'Package'), HANDLING_COLS),
    ('goods_items', ends('GoodsItem'), GOODS_COLS),
    ('hazardous_items', ends('HazardousItem'), HAZARD_COLS),
    ('items', is_item, ITEM_COLS),
    ('lines', is_line, LINE_COLS),
    ('taxes', is_tax, TAX_COLS),
    ('exchange_rates', ends('ExchangeRate'), RATE_COLS),
    ('payment_means', named('PaymentMeans'), PAYMENT_MEANS_COLS),
    ('payment_mandates', named('PaymentMandate'), MANDATE_COLS),
    ('financial_accounts', ends('FinancialAccount'), ACCOUNT_COLS),
    ('payment_terms', ends('PaymentTerms'), PAYMENT_TERMS_COLS),
    ('delivery_terms', ends('DeliveryTerms'), DELIVERY_TERMS_COLS),
    ('periods', ends('Period'), PERIOD_COLS),
]


TRANSPARENT = {'periods'}  # rows of their own, but their leaves also count for the row above
_entity_cache = {}


def entity_table(e):
    if e in _entity_cache:
        return _entity_cache[e]
    t = None
    if e.getparent() is not None:
        for name, test, _ in ENTITIES:
            if test(e):
                t = name
                break
    _entity_cache[e] = t
    return t


def flatten(e, skip=None, rel=''):
    """(relative path, leaf) for the leaves below e, not descending into entities (or `skip`)."""
    out = []
    for ch in kids(e):
        if ch is skip:
            continue
        p = rel + ln(ch)
        if is_leaf(ch):
            out.append((p, ch))
        elif entity_table(ch) in (None, *TRANSPARENT):
            out.extend(flatten(ch, skip, p + '/'))
    return out


def cell(doc, e, leaves, used, spec):
    name, patterns, style = spec
    if callable(style):
        return style(doc, e)
    hits = []
    for i, (rel, leaf) in enumerate(leaves):
        if any(fnmatch.fnmatchcase(rel, pat) for pat in patterns):
            hits.append((rel, leaf))
            used.add(i)
    if style == 'v':
        return join(fmt(x) for _, x in hits)
    if style == 'u':
        return join(fmt_unit(x) for _, x in hits)
    if style == 'nv':
        return join(f'{r}={fmt_unit(x)}' for r, x in hits)
    if style == 'nvl':
        return join(f'{r}={fmt_unit(x)}{extra_attrs(x)}' for r, x in hits)
    if style.startswith('@'):
        return join(x.get(style[1:]) or '-' for _, x in hits) if any(x.get(style[1:]) for _, x in hits) else ''
    raise ValueError(style)


def context(doc, e):
    party = None
    line = None
    ent = None
    for a in e.iterancestors():
        if party is None and is_party(a):
            party = a
        if line is None and is_line(a):
            line = a
        if ent is None and entity_table(a):
            ent = a
    return {'party_role': party_role(party) if party is not None else '',
            'party_name': party_name(party) if party is not None else '',
            'line_id': first(line, 'ID') if line is not None else '',
            'entity': f'{entity_table(ent)}:{ln(ent)}' if ent is not None else '',
            'entity_xpath': doc.xpath(ent) if ent is not None else ''}


# ---------------------------------------------------------------- generic leaf tables

def leaf_table(e):
    n = ln(e)
    if n.endswith('ID'):
        return 'identifiers'
    if n.endswith('Date') or n.endswith('Time'):
        return 'dates'
    if n.endswith('Amount'):
        return 'amounts'
    if n.endswith(('Measure', 'Quantity', 'Numeric', 'Percent', 'Rate')):
        return 'measures'
    if n.endswith(('Code', 'Indicator')):
        return 'codes'
    return 'texts'


GENERIC_COLS = {
    'identifiers': ['value', 'scheme_id', 'scheme_name', 'scheme_agency_id', 'attributes'],
    'dates': ['kind', 'value', 'pair_xpath', 'timestamp', 'attributes'],
    'amounts': ['value', 'currency', 'attributes'],
    'measures': ['kind', 'value', 'unit', 'attributes'],
    'codes': ['kind', 'value', 'list_id', 'list_agency_id', 'name_attr', 'attributes'],
    'texts': ['kind', 'value', 'language', 'attributes'],
}

KIND_SUFFIX = ('Measure', 'Quantity', 'Numeric', 'Percent', 'Rate', 'Code', 'Indicator', 'Date', 'Time')


def kind_of(n):
    for s in KIND_SUFFIX:
        if n.endswith(s):
            return s
    for s in ('Name', 'Note', 'Description', 'URI', 'BinaryObject', 'Text'):
        if n.endswith(s):
            return s
    return 'other'


def date_pair(e):
    """The sibling that completes a date with a time or a time with a date (IssueDate/IssueTime …)."""
    n = ln(e)
    want = n[:-4] + ('Time' if n.endswith('Date') else 'Date')
    p = e.getparent()
    for s in kids(p):
        if ln(s) == want:
            return s
    return None


def generic_row(doc, e, table):
    row = doc.base(e)
    a = attrs(e)
    v = text(e)
    if table == 'identifiers':
        row.update(value=v, scheme_id=e.get('schemeID', ''), scheme_name=e.get('schemeName', ''),
                   scheme_agency_id=e.get('schemeAgencyID', ''), attributes=a)
    elif table == 'dates':
        pair = date_pair(e)
        d, t = (v, text(pair) if pair is not None else '') if ln(e).endswith('Date') else \
            (text(pair) if pair is not None else '', v)
        row.update(kind=kind_of(ln(e)), value=v, pair_xpath=doc.xpath(pair) if pair is not None else '',
                   timestamp='T'.join(x for x in (d, t) if x), attributes=a)
    elif table == 'amounts':
        row.update(value=v, currency=e.get('currencyID', ''), attributes=a)
    elif table == 'measures':
        row.update(kind=kind_of(ln(e)), value=v, unit=e.get('unitCode', ''), attributes=a)
    elif table == 'codes':
        row.update(kind=kind_of(ln(e)), value=v, list_id=e.get('listID', ''),
                   list_agency_id=e.get('listAgencyID', ''), name_attr=e.get('name', ''), attributes=a)
    else:
        row.update(kind=kind_of(ln(e)), value=v, language=e.get('languageID', ''), attributes=a)
    row.update(context(doc, e))
    return row


# ---------------------------------------------------------------- special tables

CUSTOMS = re.compile(r'Customs|Procedure|Regime|Tariff|Preference|Declaration|ExportReason|ImportReason|Bonded')


def documents_row(doc, index):
    r = doc.root
    top = {}
    for ch in kids(r):
        if is_leaf(ch):
            top.setdefault(ln(ch), []).append(ch)

    def g(n):
        return join(fmt(x) for x in top.get(n, []))
    roles = []
    for ch in kids(r):
        if is_party(ch):
            roles.append((ln(ch), ch))
        elif ln(ch).endswith('Party') and not is_leaf(ch):
            for p in kids(ch):
                if ln(p) == 'Party':
                    roles.append((ln(ch), p))
    issuer = next(((n, p) for n, p in roles if n == 'SenderParty'), roles[0] if roles else ('', None))
    did = g('ID')
    return {'flow': doc.flow, 'file': doc.file, 'xpath': doc.xpath(r), 'root': ln(r), 'id': did,
            'id_scheme': join(x.get('schemeID', '') for x in top.get('ID', [])), 'uuid': g('UUID'),
            'issue_date': g('IssueDate'), 'issue_time': g('IssueTime'),
            'issue_timestamp': 'T'.join(x for x in (g('IssueDate'), g('IssueTime')) if x),
            'type_codes': join(f'{n}={fmt(x)}' for n, xs in top.items() if n.endswith('TypeCode') for x in xs),
            'customization_id': g('CustomizationID'), 'profile_id': g('ProfileID'),
            'profile_execution_id': g('ProfileExecutionID'), 'version_id': g('VersionID'),
            'copy_indicator': g('CopyIndicator'),
            'currencies': join(f'{n}={fmt(x)}' for n, xs in top.items() if n.endswith('CurrencyCode') for x in xs),
            'parties': join(f'{n}={party_name(p) or "?"}' for n, p in roles),
            'issuer_role': issuer[0], 'issuer': party_name(issuer[1]) if issuer[1] is not None else '',
            'same_id_elsewhere': join(m['where'] for m in index.get(did, []) if m['where'] != f'{doc.flow}/{doc.file}')}


DOC_COLS = ['flow', 'file', 'xpath', 'root', 'id', 'id_scheme', 'uuid', 'issue_date', 'issue_time', 'issue_timestamp',
            'type_codes', 'customization_id', 'profile_id', 'profile_execution_id', 'version_id', 'copy_indicator',
            'currencies', 'parties', 'issuer_role', 'issuer', 'same_id_elsewhere']

PARTY_ID_KINDS = [('PartyIdentification/ID', 'party_id'), ('AdditionalPartyIdentification/ID', 'additional_party_id'),
                  ('ElectronicAddress/ElectronicAddressID', 'endpoint'), ('EndpointID', 'endpoint'),
                  ('PartyLegalEntity/CompanyID', 'legal_company_id'), ('PartyTaxScheme/CompanyID', 'tax_company_id'),
                  ('PartyLegalEntity/SecurityListing/ID', 'security_listing_id'),
                  ('PartyAuthorization/Certificate/ID', 'authorization_certificate_id')]
PARTY_ID_COLS = BASE + ['kind', 'value', 'scheme_id', 'party_xpath', 'party_role', 'party_name', 'party_legal_name']

ITEM_ID_KINDS = [('SellersItemIdentification/ID', 'sellers'), ('SellersItemIdentification/ExtendedID', 'sellers_extended'),
                 ('BuyersItemIdentification/ID', 'buyers'), ('ManufacturersItemIdentification/ID', 'manufacturers'),
                 ('StandardItemIdentification/ID', 'standard'), ('CatalogueItemIdentification/ID', 'catalogue'),
                 ('AdditionalItemIdentification/ID', 'additional')]
ITEM_ID_COLS = BASE + ['kind', 'value', 'scheme_id', 'item_xpath', 'item_name', 'item_main_id', 'line_id']

CUSTOMS_COLS = BASE + ['value', 'attributes'] + CONTEXT


def index_documents(docs):
    idx = defaultdict(list)
    for d in docs:
        r = d.root
        did = first(r, 'ID')
        if did:
            idx[did].append({'where': f'{d.flow}/{d.file}', 'root': ln(r), 'uuid': first(r, 'UUID'),
                             'issue_date': first(r, 'IssueDate'), 'issue_time': first(r, 'IssueTime')})
    return idx


def extract(docs):
    index = index_documents(docs)
    for name, _, cols in ENTITIES:
        if name == 'references':
            cols[:] = [x for x in cols if x[0] != 'example_matches'] + [c('example_matches', style=ref_matches(index))]
    entity_cols = {n: cl for n, _, cl in ENTITIES}
    tables = defaultdict(list)
    for d in docs:
        tables['documents'].append(documents_row(d, index))
        for e in d.root.iter():
            if not isinstance(e.tag, str):
                continue
            if is_leaf(e):
                t = leaf_table(e)
                tables[t].append(generic_row(d, e, t))
                if CUSTOMS.search(ln(e)):
                    tables['customs'].append(dict(d.base(e), value=fmt_unit(e), attributes=attrs(e), **context(d, e)))
                continue
            t = entity_table(e)
            if t is None:
                continue
            cols = entity_cols[t]
            leaves = flatten(e)
            used = set()
            row = d.base(e)
            for spec in cols:
                row[spec[0]] = cell(d, e, leaves, used, spec)
            row['other'] = join(f'{rel}={fmt_unit(x)}' for i, (rel, x) in enumerate(leaves) if i not in used)
            row.update(context(d, e))
            tables[t].append(row)
            if t == 'parties':
                for rel, leaf in leaves:
                    for pat, kind in PARTY_ID_KINDS:
                        if rel == pat:
                            tables['party_ids'].append(dict(
                                d.base(leaf), kind=kind, value=text(leaf), scheme_id=leaf.get('schemeID', ''),
                                party_xpath=d.xpath(e), party_role=party_role(e), party_name=party_name(e),
                                party_legal_name=first(e, 'PartyLegalEntity/RegistrationName')))
            if t == 'items':
                for rel, leaf in leaves:
                    for pat, kind in ITEM_ID_KINDS:
                        if rel == pat:
                            ln_ = line_of(e)
                            tables['item_ids'].append(dict(
                                d.base(leaf), kind=kind, value=text(leaf), scheme_id=leaf.get('schemeID', ''),
                                item_xpath=d.xpath(e), item_name=first(e, 'Name'), item_main_id=item_main_id(e),
                                line_id=first(ln_, 'ID') if ln_ is not None else ''))
    columns = {'documents': DOC_COLS, 'party_ids': PARTY_ID_COLS, 'item_ids': ITEM_ID_COLS, 'customs': CUSTOMS_COLS}
    for t, cols in GENERIC_COLS.items():
        columns[t] = BASE + cols + CONTEXT
    for name, _, cols in ENTITIES:
        columns[name] = BASE + [x[0] for x in cols] + ['other'] + CONTEXT
    return tables, columns


ORDER = ['documents', 'parties', 'party_ids', 'contacts', 'identifiers', 'references', 'dates', 'periods', 'locations',
         'transport_means', 'shipment_stages', 'transport_events', 'transport_equipment', 'consignments',
         'handling_units', 'goods_items', 'hazardous_items', 'items', 'item_ids', 'lines', 'amounts', 'taxes',
         'exchange_rates', 'payment_means', 'payment_mandates', 'financial_accounts', 'payment_terms',
         'delivery_terms', 'customs', 'measures', 'codes', 'texts']

DESCRIPTIONS = {
    'documents': 'one row per example: root, ID, UUID, issue date/time, type codes, profile, currencies, top-level '
                 'parties (role=name); issuer = SenderParty if present, else the first top-level party in document '
                 'order (a mechanical rule, not a judgement); same_id_elsewhere = other examples with the same ID',
    'parties': 'one row per PartyType element at any depth (cac:Party in a role wrapper, or a role of PartyType such '
               'as CarrierParty); role = the wrapper or role element; role_extras = leaves of the role wrapper',
    'party_ids': 'one row per identifier of a party (party ID, additional ID, endpoint, legal and tax company IDs, '
                 'security listing ID, authorization certificate ID)',
    'contacts': 'one row per *Contact and *Person aggregate; party_role/party_name = the party it belongs to',
    'identifiers': 'generic: every leaf whose name ends in ID (cbc:ID, UUID, …)',
    'references': 'one row per *Reference aggregate; example_matches = examples whose document ID equals the '
                  'referenced ID (the referencing example itself excluded)',
    'dates': 'generic: every leaf ending in Date or Time; timestamp = date + T + time of the sibling pair '
             '(XDate/XTime) where both exist, on both rows',
    'periods': 'one row per *Period aggregate with start/end (date T time) and duration',
    'locations': 'one row per *Location / *Address aggregate except a party\'s own PostalAddress, '
                 'RegistrationAddress, JurisdictionRegionAddress, ElectronicAddress, financial institution '
                 'addresses and the Address inside a Location (part of the location row)',
    'transport_means': 'one row per *TransportMeans',
    'shipment_stages': 'one row per *ShipmentStage; places/events/transport_means summarise the direct child entities',
    'transport_events': 'one row per *TransportEvent (and RequestedArrivalEvent)',
    'transport_equipment': 'one row per *TransportEquipment; entity/entity_xpath show where it sits',
    'consignments': 'one row per *Consignment and *Shipment',
    'handling_units': 'one row per *TransportHandlingUnit and *Package',
    'goods_items': 'one row per *GoodsItem',
    'hazardous_items': 'one row per *HazardousItem',
    'items': 'one row per cac:Item (and SupplyItem); main_id = first of sellers, standard, buyers, manufacturers, '
             'catalogue ID (Kind=value); line_kind/line_xpath = the line it sits on',
    'item_ids': 'one row per item identification',
    'lines': 'one row per document line (*Line except AddressLine, and *LineItem)',
    'amounts': 'generic: every leaf ending in Amount',
    'taxes': 'one row per TaxSubtotal and per *TaxCategory outside a TaxSubtotal',
    'exchange_rates': 'one row per *ExchangeRate',
    'payment_means': 'one row per PaymentMeans',
    'payment_mandates': 'one row per PaymentMandate',
    'financial_accounts': 'one row per *FinancialAccount with branch and institution',
    'payment_terms': 'one row per *PaymentTerms',
    'delivery_terms': 'one row per *DeliveryTerms',
    'customs': 'every leaf whose name contains Customs, Procedure, Regime, Tariff, Preference, Declaration, '
               'ExportReason, ImportReason or Bonded (also present in the generic tables)',
    'measures': 'generic: every leaf ending in Measure, Quantity, Numeric, Percent or Rate',
    'codes': 'generic: every leaf ending in Code or Indicator',
    'texts': 'generic: every other leaf (names, notes, descriptions, address parts, URIs, binary objects …)',
}


NOTES = [
    '- `taxes.csv` supplier/customer: `supplier_role`/`customer_role` name the top-level role element of the '
    'document that was used, `supplier`/`customer` its party name and `supplier_country`/`customer_country` the '
    'IdentificationCode of that party\'s PostalAddress/Country. The role is the first one present, in this order: '
    'supplier = AccountingSupplierParty, SellerSupplierParty; customer = AccountingCustomerParty, '
    'BuyerCustomerParty, CustomerParty, ContractingParty. Only direct children of the root count (a party in a '
    'consignment does not); a document without such a role has empty cells (the supplier of a tender notice or a '
    'UtilityStatement, for instance). `document_currency` = the root\'s DocumentCurrencyCode.',
    '- `exchange_rates.csv`: `element` is the kind of rate (PricingExchangeRate, TaxExchangeRate, '
    'PaymentExchangeRate, PaymentAlternativeExchangeRate, or a plain ExchangeRate inside payment terms, a price '
    'or a line); `document_currency`, `tax_currency`, `pricing_currency`, `payment_currency` and '
    '`payment_alternative_currency` are the root\'s own DocumentCurrencyCode, TaxCurrencyCode, PricingCurrencyCode, '
    'PaymentCurrencyCode and PaymentAlternativeCurrencyCode (empty where the document has none).',
    '- `payment_terms.csv`: `settlement_discount` holds SettlementDiscountPercent/Amount and the SettlementPeriod, '
    '`penalty` holds PenaltySurchargePercent, PenaltyAmount, PenaltyPeriod and PenaltyInterestRate, each as '
    '`path=value unit`, followed by `[attribute=value]` for any attribute other than unit/currency/language '
    '(listID of the interest-rate codes). The periods are repeated in `periods`.',
]


def load():
    return [Doc(p) for p in sorted(EXAMPLES.glob('*/*.xml'))]


def csv_text(rows, cols):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator='\n', extrasaction='raise')
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in cols})
    return buf.getvalue()


def git(*args):
    r = subprocess.run(['git', '-C', str(REPO), *args], capture_output=True, text=True)
    return r.stdout.strip()


def write(out):
    docs = load()
    tables, columns = extract(docs)
    out.mkdir(parents=True, exist_ok=True)
    readme = ['# Consistency tables', '',
              f'Built by `.claude/skills/ubl-example-review/scripts/extract_tables.py` from {len(docs)} examples '
              f'(`world/examples/*/*.xml`).', '',
              f'- commit: `{git("rev-parse", "HEAD")}` ({git("log", "-1", "--format=%cI")})',
              f'- branch: `{git("rev-parse", "--abbrev-ref", "HEAD")}`',
              f'- examples changed against the commit: {"yes" if git("status", "--porcelain", "--", "world/examples") else "no"}',
              '', 'Conventions: see the docstring of extract_tables.py (cells with several values are joined with '
              '` | `; `[lang] value` for values with a languageID; role_path = local names from the root; `other` '
              'holds the leaves below a thematic row that no column takes).', '', *NOTES, '',
              '| table | rows | description | columns |', '|---|---:|---|---|']
    for t in ORDER:
        rows = tables.get(t, [])
        (out / f'{t}.csv').write_text(csv_text(rows, columns[t]), encoding='utf-8')
        readme.append(f'| `{t}.csv` | {len(rows)} | {DESCRIPTIONS[t]} | {", ".join(columns[t])} |')
    (out / 'README.md').write_text('\n'.join(readme) + '\n', encoding='utf-8')
    for t in ORDER:
        print(f'{len(tables.get(t, [])):7d}  {t}.csv')
    print(f'written to {out}')


# ---------------------------------------------------------------- self-test

NS = {'cac': CAC, 'cbc': CBC, 'ext': EXT}


def resolve(flow, file, xpath):
    """Resolve the XPath the way the skill's citations.select does (root and unprefixed steps -> default ns)."""
    doc = etree.parse(str(EXAMPLES / flow / file))
    ns = dict(NS, d=doc.getroot().nsmap[None])
    q = re.sub(r'(^|/)([A-Z][A-Za-z]*)(?=/|\[|$)', lambda m: m.group(1) + 'd:' + m.group(2), xpath)
    return doc.xpath(q, namespaces=ns)


def self_test(n, out):
    """Sample n rows across all tables, resolve each xpath and compare the value / element name; also
    check that the generic tables hold every leaf exactly once (independent count with lxml XPath)."""
    rnd = random.Random(20261114)
    files = {t: out / f'{t}.csv' for t in ORDER}
    failures = 0
    checked = 0
    rows_all = []
    for t, f in files.items():
        with open(f, encoding='utf-8', newline='') as fh:
            for r in csv.DictReader(fh):
                rows_all.append((t, r))
    per_table = defaultdict(list)
    for t, r in rows_all:
        per_table[t].append(r)
    sample = []
    for t in ORDER:  # at least one row per non-empty table, the rest at random
        if per_table[t]:
            sample.append((t, rnd.choice(per_table[t])))
    while len(sample) < n:
        sample.append(rnd.choice(rows_all))
    for t, r in sample:
        hits = resolve(r['flow'], r['file'], r['xpath'])
        checked += 1
        ok = len(hits) == 1
        what = ''
        if ok:
            e = hits[0]
            if t == 'documents':
                ok = ln(e) == r['root'] and first(e, 'ID') == r['id']
            else:
                ok = ln(e) == r['element']
            if ok and (t in GENERIC_COLS or t in ('party_ids', 'item_ids')):
                ok = text(e) == r['value']
                what = f' value={r["value"][:40]!r}'
            if ok and t == 'parties':
                ok = r['name'] == join(fmt(x) for x in e.xpath('cac:PartyName/cbc:Name', namespaces=NS))
                what = f' name={r["name"][:40]!r}'
            if ok and t == 'items':
                ok = r['name'] == join(fmt(x) for x in e.xpath('cbc:Name', namespaces=NS))
                what = f' name={r["name"][:40]!r}'
        print(f'{"ok  " if ok else "FAIL"} {t:20s} {r["flow"]}/{r["file"]}:{r["xpath"]}{what}')
        failures += not ok
    # completeness: independent count of leaves per suffix class with a plain XPath
    counts = defaultdict(int)
    for p in sorted(EXAMPLES.glob('*/*.xml')):
        root = etree.parse(str(p)).getroot()
        names = [x.xpath('local-name()') for x in root.xpath('//*[not(*)]')]
        for nm in names:
            counts['all'] += 1
            if nm.endswith('ID'):
                counts['identifiers'] += 1
            elif nm.endswith('Date') or nm.endswith('Time'):
                counts['dates'] += 1
            elif nm.endswith('Amount'):
                counts['amounts'] += 1
            elif re.search(r'(Measure|Quantity|Numeric|Percent|Rate)$', nm):
                counts['measures'] += 1
            elif re.search(r'(Code|Indicator)$', nm):
                counts['codes'] += 1
            else:
                counts['texts'] += 1
    total = 0
    for t in GENERIC_COLS:
        got = len(per_table[t])
        total += got
        ok = got == counts[t]
        failures += not ok
        print(f'{"ok  " if ok else "FAIL"} completeness {t}: table {got}, independent count {counts[t]}')
    ok = total == counts['all']
    failures += not ok
    print(f'{"ok  " if ok else "FAIL"} completeness all leaves: tables {total}, independent count {counts["all"]}')
    print(f'{checked} sampled rows, {failures} failure(s)')
    return failures


def main():
    args = sys.argv[1:]
    if args and args[0] in ('-h', '--help'):
        sys.exit(__doc__)
    if args and args[0] == '--self-test':
        args = args[1:]
        n = int(args.pop(0)) if args and args[0].isdigit() else 60
        out = Path(args[0]) if args else DEFAULT_OUT
        sys.exit(1 if self_test(n, out) else 0)
    out = Path(args[0]) if args else DEFAULT_OUT
    write(out.resolve())


if __name__ == '__main__':
    main()
