# LLM review: 14-CommonTransportationReport.xml

Reviewed file: [14-CommonTransportationReport.xml](14-CommonTransportationReport.xml) · Flow: `cotton` (`COTTON-2026-01`) · Review date: 2026-11-12

**Basis.** The semantic model of UBL 2.5 (`UBL-Entities-2.5.gc` from
<https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/>, SHA-256
`c7df070e…fe988d1`), the meaning of codes in `world/codelists`, and the other
XML documents of the flow where this document refers to them. The fictional
world (countries, currencies, languages, identifier schemes) is accepted as
given; only clashes with real standards are flagged.

**Severity.**
**High**: the value contradicts another value in this document or in a referenced document, or a reference is broken.
**Medium**: the element carries a meaning other than its UBL definition.
**Low**: plausibility, consistency or completeness remark.
**Recurring**: the same pattern occurs in many other examples.

## Summary

| # | Severity | Element(s) | Issue |
|---|---|---|---|
| 1 | High | `/CommonTransportationReport/cac:Shipment/cbc:ID`, `/CommonTransportationReport/cac:TransportMeans` | Shipment, vessel and voyage cannot be linked to any other document of the flow |
| 2 | Medium | `…/cac:ISPSRequirements/cbc:ValidISSCIndicator`, `…/cbc:ISSCAbsenceReason` | An interim ISSC is a valid ISSC; "not valid" contradicts the expiry date and issuer given |
| 3 | Medium | `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage` | A pre-arrival report without arrival time, ports or means for the stage |
| 4 | Low | `…/cac:ShipSanitationControlExemptionDocumentReference/cac:IssuerParty`, `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity` | A private, small port company as the competent health authority |
| 5 | Low | `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Note`, `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` | Office hours for port control; a bookings desk as the reporter's contact |
| 6 | Low | `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation` | Port of registry by name only, while the same port is identified by UN/LOCODE elsewhere in the document |
| 7 | Medium · Recurring | `…/cac:Language/cbc:LocaleCode` | A language code where a locale is defined |

## Findings

### 1. The report cannot be linked to the shipment it is about (High, cross-document)

- **XPaths:**
  - `/CommonTransportationReport/cac:Shipment/cbc:ID` = `TOL-SH-26-0208`
  - `/CommonTransportationReport/cac:TransportMeans/cbc:JourneyID` = `TR-26-09W`
  - `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:VesselName` = `Tidewell Reef` (`VesselID` `XB-S-20231`)
- **UBL definitions:**
  - *Common Transportation Report. Shipment*: "A shipment to which this common transportation report applies."
  - *Shipment. Identifier*: "An identifier for this shipment."
- **Why it does not fit:**
  - The cargo carried by Tidewell Ocean Lines in this flow is the shipment on its own
    [Bill of Lading](13-BillOfLading.xml) `TOL-BL-26-0206`. The
    [Import Customs Declaration](15-ImportCustomsDeclaration.xml) declares the same
    shipment. Both use `Shipment/cbc:ID` = `SCG-SH-26-0200`.
  - `TOL-SH-26-0208` appears in no other document. The vessel, its call sign and the
    voyage `TR-26-09W` do not appear anywhere else either: the Bill of Lading has no
    vessel or voyage at all.
  - An authority receiving this pre-arrival report therefore cannot connect it to the
    cargo manifested and declared for the same arrival. Within the flow, nothing shows
    that the cotton travels on this ship.
- **Suggestion:** Use the shipment ID of the Bill of Lading (`SCG-SH-26-0200`) here, or
  add it as a reference. Give the Bill of Lading the vessel and voyage
  (`ShipmentStage/TransportMeans/MaritimeTransport`, `JourneyID`) so that both documents
  name the same call.

### 2. An interim ISSC reported as "not valid" (Medium)

- **XPaths:**
  - `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ValidISSCIndicator` = `false`
  - `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCAbsenceReason` = `The ship came under Bayvarra's flag on 15 January 2026 and sails with an interim certificate (ISPS Code A/19.4), valid for six months; …`
  - `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCExpiryDate` = `2026-07-14`
  - `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ISSCIssuerParty` = Maritime Administration of Bayvarra
- **UBL definitions:**
  - *ISPS Requirements. Valid ISSC Indicator*: "An indicator of whether the International Ship Security Certificate (ISSC) is valid (true) or not (false)."
  - *ISSC Absence Reason*: "A text describing the reason if not having a International Ship Security Certificate (ISSC)."
- **Why it does not fit:**
  - An interim ISSC issued under ISPS Code part A, section 19.4, is a valid ISSC for its
    period of up to six months. The IMO pre-arrival security information asks whether
    the ship has a valid ISSC and, separately, whether it is full or interim.
  - The same aggregate gives an issuer and a future expiry date (14 July 2026), so the
    ship *has* a valid certificate on the day of the report (3 March 2026). `false`
    contradicts those two values.
  - The text in `ISSCAbsenceReason` explains no absence, since a certificate is present.
- **Suggestion:** `ValidISSCIndicator` = `true`. Move the explanation about the interim
  certificate to `cbc:AdditionalMattersDescription` (or keep only the certificate details)
  and omit `ISSCAbsenceReason`.

### 3. A pre-arrival report that does not say when or where the ship arrives (Medium)

- **XPath:** `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage` (has only `ID`, `ReportingPerson`, `ISPSRequirements` and `MaritimeHealthDeclaration`)
- **Related value:** `/CommonTransportationReport/cbc:ReportTypeCode` = `PREARRIVAL` ("Pre-arrival report")
- **UBL definitions:**
  - *Common Transportation Report*: "A common document used for reporting transport related issues to authorities or regulators."
  - *Shipment Stage. Estimated Arrival_ Transport Event*: "Describes an estimated arrival at a location during a transport service."
- **Why it does not fit:**
  - The report type commits the document to a pre-arrival notification. Its essential
    content is the expected arrival (date and time) at the reporting port, together
    with the stage's mode and means, and the last port of call.
  - The stage has none of these. The last port (Selanu) is mentioned only in the free
    text about stowaways. The vessel is given only at document level (`cac:TransportMeans`),
    not as the means of this stage.
- **Suggestion:** Add to the stage `cbc:TransportModeCode` `1`, `cac:TransportMeans`
  (the vessel), `cac:LoadingPortLocation` (Selanu), `cac:UnloadingPortLocation` (`XBLMP`)
  and `cac:EstimatedArrivalTransportEvent` with date and time.

### 4. A private, small port company as the competent health authority (Low)

- **XPaths:**
  - `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:ShipSanitationControlExemptionDocumentReference/cac:IssuerParty` = Port of Lumeport (`20411781`)
  - `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `LTD` ("Limited company (private)")
  - `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- **UBL definitions:**
  - *Common Transportation Report. Authority_ Party*: "The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator."
  - *Document Reference. Issuer_ Party*: "The Party who issues the Referenced Document."
- **Why it does not fit:**
  - Under the International Health Regulations (2005), Art. 39 and Annex 3, ship
    sanitation certificates are issued by the *competent authority* at an authorized
    port. The document's own description cites these regulations. Here the issuer is
    the port company, described as a small, private limited company.
  - That legal form and size also sit uneasily with the party's role as the
    `AuthorityParty` of a container port receiving regulatory pre-arrival reports.
- **Suggestion:** Make the issuer a health authority (e.g. "Port Health Authority of
  Lumeport"). Describe the port as a public port authority, with a fitting legal form
  and size, or make the AuthorityParty the harbour master or port authority rather than
  the port company.

### 5. Contacts that do not fit the reporting situation (Low)

- **XPaths:**
  - `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Name` = `Port control` with `…/cbc:Note` = `Weekdays 08:00–17:00`
  - `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` = `Bookings`
- **UBL definition:** *Contact. Note*: "… in particular, a textual description of the circumstances under which this contact can be used (e.g., "emergency" or "after hours")."
- **Why it does not fit:**
  - Port control handles ship movements around the clock. Office hours on weekdays make
    the contact unusable for arrivals at night or at weekends.
  - The reporter is the shipping line reporting security and health data on behalf of
    the master. The bookings desk is its sales or cargo-booking contact, not the
    operations or ship-agency contact an authority would call about this report.
- **Suggestion:** Port control: `Note` "24/7". Reporter: e.g. "Marine operations" or
  "Ship agency desk".

### 6. Port of registry by name only (Low)

- **XPath:** `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- **UBL definition:** *Maritime Transport. Registry Port_ Location*: "The port in which a vessel is registered or permanently based."
- **Why it does not fit:** The same document identifies Lumeport by UN/LOCODE `XBLMP`
  (`AuthorityParty/cac:PhysicalLocation/cbc:ID`). The registry port is given only as a
  bare city name, so a receiver cannot tell for certain that it is the same port.
- **Suggestion:** Add `cbc:ID` `XBLMP` with `schemeID="UN/LOCODE"`.

### 7. `LocaleCode` holds a language, not a locale (Medium, recurring)

- **XPaths:**
  - `/CommonTransportationReport/cac:ReporterParty/cac:Language/cbc:LocaleCode`
  - `/CommonTransportationReport/cac:AuthorityParty/cac:Language/cbc:LocaleCode`
- **Value:** `en` with `@listID="ISO 639"`
- **UBL definition:** *Language. Locale Code*: "A code signifying the locale in which this language is used."
- **Why it does not fit:** The value repeats `Language/cbc:ID`. A locale is a language
  plus a region (e.g. `en-XB`), and ISO 639 is a list of languages.
- **Recurring:** 728 occurrences in `world/examples`.

## References checked and consistent

- `ReporterParty` = `SenderParty` = Tidewell Ocean Lines (the carrier on the Bill of
  Lading). `AuthorityParty` = `ReceiverParty` = Port of Lumeport.
- `ReportingPerson/RoleCode` `MASTER` matches the master's role in pre-arrival reporting.
- `ISSCExpiryDate` 2026-07-14 is six months after the change of flag on 15 January 2026,
  which matches an interim certificate. `RegistrationNationalityID` `XB` matches the new
  flag.
- `TransportMeansTypeCode` `1511` (full container ship) agrees with `ShipConfigurationCode`
  `FEEDER`. Gross and net tonnage (7480 / 3910) are plausible for a feeder.
- The issue date 2026-03-03 lies between the Bill of Lading (2026-03-02) and the import
  declaration (2026-03-06). The stowaway search before leaving Selanu, after the fence gap
  reported on 1 March, fits that timeline.
- `RadioCallSignID` `QBTR4` (no ITU series starts with Q) belongs to no real station.
  UN/LOCODE `XBLMP` is under a user-assigned country code, so it does not clash.
