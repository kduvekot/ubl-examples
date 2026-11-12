# The UBL example world

All examples take place in one fictional world. It is built in layers.
Each layer adds one kind of data, is kept in its own file, and is checked
before the next layer builds on it.

| Layer | File | What it holds |
|---|---|---|
| Countries | `world/countries.json` | names, currencies, tax schemes, identifier and address schemes |
| Parties | `world/parties.json` | the organisations: place on the map, role, identity |
| Map | `world/map.json` | routes, towns and localities |
| Documents | `world/documents.json` | the flows of documents between the parties |
| Items | `world/items.json` | what the parties sell: goods and services, with prices |
| UBL model | `world/ubl-model.json` | extracted from the UBL 2.5 semantic model |
| Code lists | `world/codelists/` | the world's code lists, and which code element uses which |
| Specifications | `world/specifications.json` | the transactions, national and community specifications and process profiles the documents claim |
| UBL versions | `world/ubl-versions.json` | the first UBL 2 version of each element, from the published models of UBL 2.0 to 2.5 |

## Countries

The world has three countries: Urvania, Bayvarra and Lisavu, whose
initials spell UBL. Two share a land border on the mainland; the third is
an island overseas. They differ on purpose, so that the
examples show how UBL carries different national arrangements in the same
structure:

- **Urvania (XU)** has a value added tax in the style of the EU VAT:
  charged at every stage, deducted by businesses, not charged on exports.
- **Bayvarra (XB)** is a federal country whose states levy a retail sales
  tax, charged once, on the sale to the final consumer. Sales for resale,
  exports and sales to public bodies are exempt.
- **Lisavu (XL)** has no general sales tax. Customs collects a customs
  duty and an import consumption tax when goods enter the island.

The tax schemes are identified with UN/EDIFACT 5153 codes: `VAT`, `STT`
(state or provincial sales tax), `CUD` (customs duty) and `IMP` (import
tax). Because 5153 has no code for a national sales tax, Bayvarra levies
its sales tax at state level, which also gives the state in its addresses a
purpose. Bayvarra has two states, Upland State inland and Coastal State
around Lumeport, and a federal territory, the Northern Territory, on the
thinly populated north coast, where the gas plant stands. The territory
levies its own rate of the same sales tax: 4 %, against 5 % in Upland State
and 6.5 % in Coastal State. Which state a place is in follows from its place
on the map.

XU, XB and XL are ISO 3166-1 user-assigned codes, which exist for exactly
this purpose; each follows the initial of its country's name. ISO 4217 has
no such range for currencies. The world's currencies follow the ISO 4217
convention of the country code plus the initial of the currency's name:
the ferra of Urvania (`XUF`), the lume of Bayvarra (`XBL`) and the coral of
Lisavu (`XLC`). The convention limits the names: ISO 4217 already uses
`XUA` and `XBA` to `XBD`, so Urvania's currency cannot start with an A and
Bayvarra's not with A to D. Each code is checked against the current
ISO 4217 list, so that none is a real code.

The three currencies also differ in their minor unit, because currencies
do: the ferra has none (amounts are whole ferra, as with the Japanese yen),
the lume has two decimals, and the coral three (as with the Bahraini or
Kuwaiti dinar). An example that only ever shows two decimals hides a case
that software must handle. Neither the countries nor
the currencies are in the UBL default code lists. UBL lets trading partners
use their own code lists in the second phase of validation, so the world
has its own: copies of the UBL 2.5 default lists, unchanged, with the
world's codes added and their own identification.

In the south-west the land border between Urvania and Bayvarra follows
the river: all land south of it is Urvania. The river rises in the
hills west of Ferrano and winds east to the sea, widening into an estuary at
its mouth below Lumeport. The sawmill stands on its north bank in Upland
State, by the water and its forests, as sawmills traditionally do.

The countries also speak differently. Bayvarra speaks English, the working
language between the three countries. Urvania was an Italian territory and
then under British rule; the British kept the Italian place and street
names, while the people kept their own Urvanian names for the same places.
Independent since 1962, Urvania is bilingual, Urvanian and English, and the
inherited Italian names count as English: Ferrano is also *Ruldraz*, and an
address gives both, as in Brussels. The island is officially bilingual, as
many Pacific islands are, in Lisavan and English, Lisavan having a
Polynesian sound like the island's names. Both languages are invented, and
their codes come from the range ISO 639 reserves for local use, `qaa` to
`qtz`: `qau` for Urvanian and `qal` for Lisavan. A sender from Urvania or the
island gives its notes in its own language and in English, each with its
`languageID`, and a seller there names and describes its items in both
(its name, description, warranty and what comes with it); a seller in
Bayvarra does so in English only. Both countries
name their streets and towns in both official languages, as Brussels and Canada do: UBL 2.5
lets an address repeat its street, city and state names, one per
language. The island's towns keep their Lisavan names as the primary ones,
and each has the English name its English-speaking settlers gave it:
Selanu is also *Port Wrenfield*, a name checked not to be a real place.
The texts in the invented languages are made word by word from a fixed
vocabulary, the English text being the reference. Real Polynesian languages
are deliberately not used, and the invented words are checked against
common words of real languages.

Each country also has an address format (`address` in `world/countries.json`),
which fixes the lines of an address: first the optional lines (attention,
department, in-house mail, post box, building, floor and room), then the
street and number (street first in Urvania, number first in Bayvarra and on
the island), additional street, block and plot, quarter, and last the town
line (postal code before the town in Urvania; the town, state and postal code
in Bayvarra), with the province in Urvania and the district and a
description of the way on the island. A field the address does not have is
left out with its line. A name in two languages is written on its line in
both, the national language first, then ` / `, then English, and the number
once: `<Urvanian street> / <English street> 12` in Urvania, `35 <Lisavan
street> / <English street>` on the island. Every address that has a street, a
building number or a post box carries the code of its country's format in
`AddressFormatCode`, and where a party writes its address in
`AddressLine` elements, one function makes the lines from the structured
fields, so they cannot disagree. The build checks all three. A farm on the
island has no house number: its track is described instead ("at kilometre 4").

Each country also has its own payment practice, which every invoice of a
seller there follows. Urvania gives 2 % discount for payment within ten
days and charges statutory interest on late payment; Bayvarra charges a
surcharge per month late and rounds cash payments to 5 cents, its smallest
coin; the island gives 45 days. A transfer quotes a creditor reference in
the structure of ISO 11649, made from the invoice number, so the payee can
match it, and runs over the domestic clearing or, between the countries,
the trade accord's payment link. Urvania also levies an energy tax per
kilowatt hour, in two tiers, on which value added tax is then charged.
A public body in Bayvarra withholds 10 % of the price of a service from a
business not established there and pays it to the state; such a supplier
names a tax representative in Bayvarra. On the island, a buyer of farm
produce withholds a presumptive tax, 1 % of a delivery's value up to
2,000 coral and 2 % above, and the farm collects a levy of 1 % for the
cotton fund of the chamber of commerce; seed cotton is priced from the
trade accord's lint reference price, published in lume. Coral net, the
island's clearing, settles tokenised deposits on the Bank of Selanu's
ledger. Lumeport's water company also collects the city's sewage levy, as
a line collected on behalf of the city, and runs the city's district
heating.

Urvania's energy market is unbundled, as the EU's is: a gas-fired power
station produces electricity, a grid operator runs the electricity and gas
networks and reads the meters, and a retail company buys the energy and
bills the customers. The gas comes from an offshore field off Bayvarra's
north coast and crosses the border by pipeline. In Bayvarra and on the
island one company still does everything, so the three countries show
three arrangements.

## Code lists

Every code in the examples comes from a code list, and every code element
names its list in `listID`. The lists are made from one source,
`world/codelists/lists.json`, as genericode files, together with the world's
context/value associations, which say which list each element uses. Where a
standard has a list for a concept, the world uses it; otherwise the Lumeport
Trade Accord, the treaty between the three countries, has a regional list.
A few lists are national, because the countries differ: legal forms, tax
exemption reasons, Bayvarra's states and Urvania's customs tariff.

- **Lists of standards** are used where UBL uses them (its default lists),
  where practice uses them (EN 16931 uses UN/EDIFACT 1001, 5189 and 7161),
  or where a standard is the authority for its domain: the IMO for
  emergency schedules and security levels, the WCO for the Harmonized
  System, the UN for product classification (CPC) and dangerous goods,
  ISO 20022 for payments, EPSG for coordinates, PRONOM for file formats,
  UN/ECE Recommendation 28 for means of transport and, as it refers air
  transport there, IATA's aircraft type codes.
  UBL is not "EDIFACT in XML", so a UN/EDIFACT list is not used just because
  it exists. Each is a world copy of the codes the world uses, with others of
  the same list, made from the copy of the source kept in
  `world/codelists/sources`; its `listID` is in UBL's text style, such as
  `UN/EDIFACT EDED 1001` or `WCO HS 2022`. No code of such a list is invented.
- **Regional and national lists** have short upper-case codes and a name in
  English, Urvanian and Lisavan; their `listID` is a URN such as
  `urn:ubl-examples:world:codelist:AddressTypeCode` or
  `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`.
- **One list per concept.** Elements that only qualify one concept share its
  list, as `PreviousMeterReadingMethodCode` and `LatestMeterReadingMethodCode`
  do. An element used for several things, such as `TypeCode`, gets one list
  per meaning, chosen by its parent element.
- **No filler.** A code says something the receiver needs. Where "none"
  matters, it is a defined code, such as UN/EDIFACT 8339 code 4 "Not
  assigned" for goods without a packing group.

Some choices differ from common practice, on purpose:

- **Allowances and charges.** An allowance takes its reason from
  UN/EDIFACT 5189 and a charge from 7161, as in EN 16931. Where 7161 has no
  code, the world uses 5189 for a charge too, with that list's `listID`
  (96 insurance, 48 interest on arrears), which EN 16931 does not allow.
  UBL's own default list for this element is labelled 5189 but holds the
  codes of UN/EDIFACT 4465, so the world replaces it.
- **Languages.** Language codes are written in lower case, as ISO 639 and
  BCP 47 recommend; UBL's copy of the list is in upper case and merges the
  two alpha-3 codes of a language into one value. The world's list follows
  the ISO 639-2 registration authority and adds `qau` and `qal`. Each
  sender tags its English texts with its own country as the region,
  `en-XU`, `en-XB` or `en-XL`, which BCP 47 allows for private use.
- **Invoice periods.** `InvoicePeriod/DescriptionCode` describes the
  period (a month), as UBL defines it, not the tax point date code that
  EN 16931 puts there.
- **Document distribution.** `DocumentDistribution/DocumentTypeCode`
  gives the type of the distributed document (a bill of lading), and
  `DistributionTypeCode` how the party receives it, original or copy: an
  original by courier, a scanned copy, the electronic document itself.
  UBL 2.5 deprecated the elements that said this before (`CopyIndicator`,
  `MaximumCopiesNumeric`, `MaximumOriginalsNumeric`, `PrintQualifier`),
  and an original is not a type of document.
- **Self-billing.** Where the customer bills itself, as the cotton gin
  does for the farms' seed cotton, the world uses UBL's own
  `SelfBilledInvoice` and `SelfBilledCreditNote`, never an `Invoice` with
  type code 389 as EN 16931 and Peppol BIS do (their syntax binding has
  only Invoice and CreditNote). UBL 2.5 defines Invoice as "A document used
  to request payment" and SelfBilledInvoice as "An Invoice document created
  by the Customer (rather than the Supplier) in a Self Billing
  relationship"; its semantic definitions (§4.7) are what a document must
  conform to (§7.2). The type codes are UN/EDIFACT 1001 389 and 261: they
  repeat the root element, but their definitions are exact ("An invoice the
  invoicee is producing instead of the seller"), while 380 is a document
  "claiming payment". The gin's advance to a farm before the harvest is a
  self-billed prepayment invoice, type 386, which the final self-billed
  invoice deducts as its prepaid amount.
- **Procurement.** The Accord's procurement rules are modelled on the EU's,
  without being EU law: its lists give the matching eForms or ESPD code.
- **Customs.** The Accord is a free trade area, not a customs union: it has
  one customs data model with common procedures and statuses, while tariffs
  stay national. A procedure code is the requested procedure followed by the
  previous one, numbered differently from the EU's, so release for free
  circulation is `1000`.

## Identifiers

An identifier that comes from a scheme names it in `schemeID`; one that only
its sender assigns, such as a document number or a line number, does not.
The world's own schemes have lowercase URNs, as its first ones had
(`urn:ubl-examples:world:XB:register`, `urn:ubl-examples:world:endpoint`),
and a country's scheme carries its code (`urn:ubl-examples:world:XU:tax`,
`urn:ubl-examples:world:XB:vehicle-register`). Real schemes keep the name
their standard gives them, in the text style of UBL's `listID`s: `ISO 11649`
for the creditor references, `ISO 6166` for the securities, `ISO6346` for the
containers. Each scheme has its format in `world/countries.json`, with its
check digit where it has one, and the build checks every identifier against
it, as it checks the telephone numbers. A `schemeID` has no fixed format; the
examples show two.

A code held in an identifier element, such as the tax category in
`TaxCategory/ID`, the language in `Language/ID`, the hazard class or the
Incoterms rule in `DeliveryTerms/ID`, names its code list in `schemeID`, with
the list's `listID` (`UN/EDIFACT EDED 5305`, `ISO 639`), and the world's code
list validation checks it like any code. What a dimension or a temperature is
(`AttributeID`) is a code too, from three lists of the Trade Accord: one for
dimensions (`LENGTH`, `SEATHEIGHT` …), each mapped to the UN/EDIFACT 6313
measured attribute in its description, one for temperatures (`STORAGE`,
`PRODUCT`, `AMBIENT` …) and one for the rest (`COLOUR`, `PALLETPLACES`,
`TEU` …).

Vehicles are registered nationally: plates, aircraft and railway wagons each
have a national scheme. A wagon number follows the UIC's twelve digits with
its check digit. Driving licences and identity numbers carry no `schemeID`:
the element already says what they are, and the person's country says whose.
Values that would look like real ones are made visibly fictional in the right
format: the call signs and aircraft nationality marks use the series `QU`,
`QB` and `QL`, which the ITU has not allocated, the ships' MMSIs the
unallocated maritime identification digits 297, 298 and 299, and the wagons
the UIC country codes 46, 47 and 48, which no railway uses. A container
owner code is one the container register of the Bureau International des
Containers does not hold, looked up on its public site.

Certificates and licences name their issuer in one of two ways. A number
from a national register, such as Urvania's haulage licences and waste
permits, Bayvarra's forestry register or its customs' register of bonded
warehouses, names the register in `schemeID`, and with it the authority that
keeps it, so no issuer party is needed. A certificate whose number is unique
only with its issuer, such as an environmental, medical or sanitation
certificate or the X.509 certificate of an access point, has no `schemeID`
and names its issuer in `IssuerParty`.

Payment cards follow ISO/IEC 7812 in a range real cards cannot use: the
major industry identifier 9, which is for national use, followed by the
numeric code of the issuer's country (901, 902 and 903 are user-assigned in
ISO 3166), the issuer's digits and a Luhn check digit. A chip application
starts with its card scheme's application provider identifier from the
national category `D` of ISO/IEC 7816-5 with the same country code. The
Accord has three card schemes: Lumecard, the Bayvarran banks' domestic debit
card, Coralcard on the island, and Tressa, an international credit card of
the banks of all three countries; the names were checked against the real
card networks. A till receipt shows the card number as the merchant's till
prints it, never more than the first six and the last four digits, and never
the card's security code or its dates. The department store's tills print only the last four digits;
the trading company's shop on the island prints the first six and the last
four. A webshop order is different: the card is not at hand, so the order
carries the full number, the card's dates and its security code, and the store
has the payment authorised before it reserves the goods. PCI DSS allows a
merchant to hold the security code until the authorisation, never after.

## Parties

The parties are the organisations of the world, chosen so that every party
role in every UBL document type can be filled (see the party cover
analysis). Each party has:

- a **role**, such as manufacturer, road carrier or contracting authority;
- a **place** on the map, in a town or a locality;
- an **identity**: a name, the identifiers of its country's schemes, a
  postal address in its country's format, an electronic address, a contact,
  and, where it is paid, an account at one of the world's banks;
- for a company, its **headcount and turnover**, from which its size class
  follows by the Trade Accord's limits, modelled on the EU definition of
  small and medium-sized enterprises and given in all three currencies.

Names are invented and checked against real organisations. E-mail
addresses use the reserved domain `.example` (RFC 2606), so that none can
reach a real organisation. Telephone numbers use +999, which the ITU reserves for
a future global service (ITU-T E.164), followed by the country's digit. Each
country has its own numbering plan: Urvania kept the open plan of Italian
times, with area codes of different lengths (9 or 10 digits); Bayvarra has a
British-style plan of always 10 digits; the island has short 7-digit numbers. Account numbers follow the structure of ISO 13616
with its check digits, using the world's country codes, but they are not
called IBANs, because the world's countries are not registered IBAN
countries. Each country writes the bank and the branch into the account
number in its own way: Bayvarra the bank code and a British-style six-digit
sort code, Urvania the Italian-style ABI and CAB codes, the island the bank
code and a three-digit branch number. A bank is identified across the
countries by a code in the structure of ISO 9362, the BIC, with the world's
country codes (`BLUMXBLX`), which the Trade Accord's payment link gives out,
and its branch by the national code; the build checks that every account
number holds the codes of its bank and branch.

An address has a number in its country's address register where it is a
party's postal address or a delivery address: in Urvania one national
register, like the Dutch one, sixteen digits starting with the code of the
municipality; in Bayvarra a register per state, except in Lumeport, which
keeps the city's own register (`LUM-ADR-000417`); on the island the post
office's numbers of its delivery points, as the island has no postal codes.
The build checks that the register is the one of the address's state or
city.

## Items

Every party that sells has items. Goods carry what the documents along
their way need: a seller's item identifier, the maker's standard item
number where the maker has one (see below), its classification in the UN Central Product
Classification (CPC), its Harmonized System subheading and, in Urvania, the
national tariff code below it, the country of origin, dimensions, net and gross weight, and the packaging. Services
have a unit and a price. Units of measure and packaging types are UN/ECE
Recommendation 20 and 21 codes from the UBL default code lists. Prices are
in the seller's currency. A unit price may be finer than the currency, as
an electricity tariff of 27.3 ferra per kilowatt hour is, but every amount
to pay is rounded to the currency's minor unit.

Each party identifies what it makes, ships and runs in one convention, as
real companies do. The distributor, the department store and the furniture
maker work the GS1 way: a GTIN for their items, a GLN for themselves and their
places (the distribution centre's rail siding, the store's goods-in), an SSCC
for every pallet or skid they make up, and a GRAI for the distributor's own
returnable pallets, which go back to it after each delivery to the store. Their company prefixes start with
952, which GS1 reserves for demonstrations and examples. The bench maker,
its warehouse, the packaging maker, the power station and the grid operator
work the ISO way, through the Codana Identification Agency, which is
Urvania's public numbering body: a Codana item number, an organisation
identifier in the structure of ISO/IEC 6523 with the code designator 0990,
which no real scheme has, and licence plates for their transport units in
the structure of ISO/IEC 15459, under the issuing agency code `KXU` (`K` is
the range for national public administrations, and XU is a user-assigned
country code, so no real agency can hold it). The engineering company, the
sawmill, the island's cotton farm and ginnery and the utilities use only
their own numbers. A reseller shows its own item number and the maker's;
where the maker has no GTIN, the GS1 distributor gives the item one of its
own, as GS1 allows a wholesaler or importer to do, and the maker's Codana
number travels with it. Inner packages have local numbers without a scheme.
A logistic unit has the same identifier in every document of its flow,
which the build checks.

Items connect the chains. The park bench is made with slats from the
sawmill and film from the packaging maker; the distributor resells the
bench, and its own item points to the manufacturer's, so the maker's
identifiers travel along. A component or a resold item is only possible
if the maker or reseller orders it from that seller somewhere in the flows.

The maker's facts travel with the item wherever it appears: brand and
model, properties with their test method and accepted range, certificates,
the carbon footprint and the circularity profile. What belongs to one
delivery is added only where the goods move: a despatch advice names the
production lot, or the serial number of every casting, which stays the same
when a cancelled despatch advice is replaced. A catalogue line adds the
seller's terms (lead time, minimum and maximum quantity, the price list and
its validity), and a till receipt during a promotion shows the discount on
the shelf price.

## Flows of documents

The parties do business in flows. Each country has its own raw material
and industry: Urvania mines ore and makes park benches, recovering its
production waste as recycled plastic; Bayvarra saws timber, makes furniture,
packaging and clothing, and distributes and retails; the island Lisavu grows
and gins cotton, its export. Goods cross the land border by road, rail and
river barge and go overseas by sea and air in both directions; there is a
public tender and a design contest, a temporary export with an ATA carnet, a
utility in each country, and gas by pipeline from Bayvarra's offshore field to Urvania's
power station and grid. Each flow starts from the business: who buys
from whom, on which delivery terms, and therefore who arranges and pays the
transport. A distributor that buys free carrier (FCA) books the truck
itself and names the carrier in its order; a retailer that buys delivered
duty paid (DDP) leaves the transport to its supplier, who then needs an
outgoing waybill.

A document that is revised keeps its number and says which version it
supersedes, with `VersionID` 2 and `PreviousVersionID` 1, and its reasons say
what changed. The design contest shows this: the city of Lumeport relaunches a
contest for its harbour promenade bench, cancelled the year before because no
design met the brief (the new notice gives the reason), offers three prizes and
asks a group of designers to form a limited company before the follow-up
contract. The council raises the prize fund, a corrigendum corrects the site
plan and widens a selection criterion, the design team updates its
declarations, the registry reissues its extract when new accounts are filed,
and the results notice corrects a prize amount.

Every document in a flow records:

- the document type, its sender and its receiver;
- why it is sent, in business terms;
- every party it mentions, at its place in the UBL structure, for example
  the road carrier at `Order/Delivery/Despatch/CarrierParty`.

A flow also lists its transport legs: the mode, from which party to which,
and the carrier. The goods only move where the world allows it. A road leg
needs a road from party to party, so a truck cannot drive to the island; a
rail leg needs a rail line between them, a barge needs the river at both
ends, gas a pipeline from party to party, a ship a sea route from port to
port and an aircraft an air route from airport to airport. The carrier must
have a vehicle, train, vessel, aircraft or pipeline of that mode in its
fleet, and every carrier a document of the
flow names must carry one of its legs. Domestic jobs go to a carrier of
that country: a truck of one country driving within another would be
cabotage, which only happens where a document says so.

An air leg also says how the goods are loaded, and the build checks that the
load fits the island airline's ATR 72-600F, as ATR's fact sheet gives it: at
most 9,200 kg, 75 m³ and seven LD3 containers, each within its own maximum
weight, and loose pieces that pass the 2.94 × 1.80 m cargo door into the aft
bulk compartment. The sample benches, at 1.8 m, fly loose. Dangerous goods are
stowed as the IATA Dangerous Goods Regulations ask: the smoke detectors (class
7, an excepted package) may share a container with the corrosive coating
stripper, because class 7 needs no segregation, but the stripper's flammable
subsidiary label keeps it away from the lithium batteries, which must not be
stowed next to a package with a class 3 label. A subsidiary hazard has no
emergency schedule of its own in the IMDG Code, which gives one per UN entry;
the road rules give the crew's actions per hazard label, so the subsidiary
hazard names the Accord's emergency card of its class.

A ship reports to the port before it arrives, with its security and health
certificates. The ocean carrier's second feeder came under Bayvarra's flag in
January: it sails with an interim security certificate and says why, and it
carries a sanitation control exemption certificate, which the port health
office issues when an inspection finds no control measures needed; the first
feeder carries a sanitation control certificate, as its inspection found pests
in the galley stores. The security report lists the ship-to-ship activities of
the last ten port calls, here a bunkering from the port's barge, with the
measure the ship took.

The vehicles on the map are these legs: one truck, train, barge, ship or
aircraft per leg, travelling the way the build found for it, from the
from-party to the to-party, and a leg flown the same way by the same carrier
in several flows is one aircraft. Each makes a round trip: it waits at the
from-party, travels out, waits at the to-party and travels back, and a leg and
its return leg by the same carrier are one vehicle. An aircraft takes off and
lands along the runway: it rolls along it, climbs out straight ahead over the
approach zone, and joins the final approach in line with the runway of the
airport it goes to. A pipeline has no vehicle: the gas is shown
flowing from the field to the consumers. Pipelines follow the rules of real
ones. They are buried, so they cross roads, rail lines and the river
underneath, at right angles and in a straight line, never along them; they
keep out of towns, and nothing is built or planted on their right of way.
They start at the producer, at its offshore platform or as a branch of
another pipeline, end at a customer, and carry exactly the pipeline legs of
the flows, in the direction the gas flows. Where the pipeline crosses the
land border, a border metering station measures the gas, as at the
interconnection points between real gas networks.

## Specifications

Every document says which specification it follows. `CustomizationID` names
a *transaction*: one kind of business message between two roles, with a
purpose, a content and rules, as in CEN BII and Peppol. One or more
document types carry a transaction (billing is the invoice, the credit note
and the debit note), and one document type can carry several (an
application response that answers an invoice is not one that answers a
message). The specification has up to three levels, chained with
`#compliant#` as EN 16931, Peppol and XRechnung chain theirs: the Trade
Accord's transaction (`urn:ubl-examples:world:trns:billing:1.0`), a national
specification built on it, such as Urvania's invoice rules for its value
added tax or Bayvarra's rules for bills to its public bodies, and the
specification of a community that exchanges among itself: the retail
community of the distributor and the store, the port community of
Lumeport, Urvania's energy market and public procurement. `ProfileID` names
one of the Accord's generic process profiles (ordering, billing, transport,
customs …), versioned, and no longer the flow; `ProfileExecutionID` still
names the run of the process. Each specification has a short public page,
and the build checks that every identifier a document uses has one. The
world claims no compliance with real specifications such as EN 16931.

`UBLVersionID` gives the earliest UBL 2 version that defines every element
the document uses, as its definition asks. The build computes it from the
published models of UBL 2.0 to 2.5. For now every example needs 2.5: nearly
all use elements that UBL 2.5 added, such as the electronic address and the
further party identification.

## Who sends and who receives

Who sends and who receives a document type comes from the UBL 2.5 semantic
model first: the elements `SenderParty` and `ReceiverParty`, or a definition
of the document or of one of its party elements, such as "The Party who
submits this Tender". Where the model does not say it, the party role table
of the UBL specification is used. Where neither says it, the choice is
marked as inferred, with the definitions it rests on. Every quote is checked
word for word against its source.
