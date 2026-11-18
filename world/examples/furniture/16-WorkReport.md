# Work Report: Brackenmere Furniture to Lumeport Public Works Department

*Example 16 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Work Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WORK-REPORT-SCHEMA)*

The installers report the work done; the department approves it.

[The XML file](16-WorkReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); the document type WorkReport first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:work-report:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Work report". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **FURNITURE-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BF-DOC-26-0582**  
  The sender's number for its work report.
- `UUID` = **e84c63f9-b6d1-5eaa-bf75-38181a29b84a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The first version.
- `IssueDate` = **2026-04-09**  
  Reported when the installation was finished.
- `Note` = **Approved by the department's facilities officer.**  
  The approval.
- `AccountingCostCode` = **PWD-OFF-26**  
  The department's cost centre for the job: the planning office's fit-out (furniture/16#F5).
- `AccountingCost` = **Planning office fit-out 2026**  
  The cost centre in words.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-26-WR**  
  The department's approval signature.
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Work Quantity Total

Inside `WorkQuantityTotal`:

- `Quantity` = **14** (unitCode `HUR`)  
  Fourteen hours.
- `WorkTypeCode` = **INSTALL** (listID `urn:ubl-examples:world:codelist:WorkTypeCode`)  
  The kind of work. The code is from the Trade Accord's work type list: INSTALL = Installation.
- `WorkTypeDescription` = **Installing office furniture.**  
  In words.

### Reported Period

Inside `ReportedPeriod`:

- `StartDate` = **2026-04-08**  
  The first day.
- `EndDate` = **2026-04-09**  
  The last.

### Order Reference

Inside `OrderReference`:

- `ID` = **LPWD-PO-26-0581**  
  The department's order.

### Project Reference

Inside `ProjectReference`:

- `ID` = **PWD-PLAN-OFFICE-26**  
  The new planning office.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **PWD-COMMIT-26-0381**  
  The department's budget commitment the work will be billed against, as its order gave it.
- `DocumentType` = **Budget commitment**  
  The kind of document referred to, the department's budget commitment, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brackenmere Furniture (world/parties.json).
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Trade sales**  
  The party's main desk, which handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/JobTitle` = **Trade sales manager**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 266 466**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2648 0548**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Approver Party

Inside `ApproverParty`:

- `PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Lumeport Public Works Department**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **true**  
  A charge.
- `AllowanceChargeReasonCode` = **AEO** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: AEO = Collection and recycling.
- `AllowanceChargeReason` = **Packaging disposal**  
  The installers took the packaging away.
- `Amount` = **24.00** (currencyID `XBL`)  
  A flat charge.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  Exempt: a service to a public body.

### Statement Monetary Total

Inside `StatementMonetaryTotal`:

- `LineExtensionAmount` = **672.00** (currencyID `XBL`)  
  14 hours at 48 lume.
- `ChargeTotalAmount` = **24.00** (currencyID `XBL`)  
  The packaging disposal.
- `PayableAmount` = **696.00** (currencyID `XBL`)  
  What the invoice will charge: the hours and the disposal.

### Work Report Line

Inside `WorkReportLine`:

- `ID` = **1**  
  The installation work.
- `WorkItemID` = **INST**  
  The installation.
- `WorkItemDescription` = **Six desks assembled and placed.**  
  The work.
- `Quantity` = **14** (unitCode `HUR`)  
  Two installers for seven hours, approved by the department.
- `LineExtensionAmount` = **672.00** (currencyID `XBL`)  
  14 hours at the rate.
- `TaxInclusiveLineExtensionAmount` = **672.00** (currencyID `XBL`)  
  Exempt.
- `CompletionPercent` = **100**  
  Finished.
- `ActivityOriginLocation/Name` = **Lumeport Public Works Department, Civic Square**  
  Where.
- `Period/StartDate` = **2026-04-08**  
  From.
- `Period/EndDate` = **2026-04-09**  
  To.
- `PerformingParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PerformingParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `WorkPhaseReference/ID` = **PH-2**  
  The second phase of the move.
- `WorkPhaseReference/WorkPhaseCode` = **FURNISH** (listID `urn:ubl-examples:world:codelist:WorkPhaseCode`)  
  Furnishing. The code is from the Trade Accord's work phase list: FURNISH = Furnishing.
- `WorkPhaseReference/WorkPhase` = **Furnishing: the new office is furnished**  
  The name of code FURNISH in the Trade Accord's work phase list, followed by the detail of this case: the phase of the move it reports.
- `WorkPhaseReference/ProgressPercent` = **100**  
  Done.
- `WorkPhaseReference/StartDate` = **2026-04-08**  
  Started.
- `WorkPhaseReference/EndDate` = **2026-04-09**  
  Ended.
- `WorkPhaseReference/WorkOrderDocumentReference/ID` = **LPWD-PO-26-0581**  
  The order.
- `DocumentReference/ID` = **BF-CHECK-26-0408**  
  The installation checklist.
- `DocumentReference/DocumentType` = **Installation checklist**  
  The kind of document referred to, Brackenmere's checklist of the office installation, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `Price/PriceAmount` = **48** (currencyID `XBL`)  
  Per hour.
- `TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  Exempt.
- `SubWorkReportLine/ID` = **1.1**  
  One installer's part.
- `SubWorkReportLine/WorkItemID` = **INST-1**  
  The installer.
- `SubWorkReportLine/WorkItemDescription` = **Installer 1: seven hours.**  
  The work.
- `SubWorkReportLine/Quantity` = **7** (unitCode `HUR`)  
  Seven hours.
- `SubWorkReportLine/ID` = **1.2**  
  One installer's part.
- `SubWorkReportLine/WorkItemID` = **INST-2**  
  The installer.
- `SubWorkReportLine/WorkItemDescription` = **Installer 2: seven hours.**  
  The work.
- `SubWorkReportLine/Quantity` = **7** (unitCode `HUR`)  
  Seven hours.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<WorkReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:WorkReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:work-report:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>FURNITURE-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BF-DOC-26-0582</cbc:ID>
  <cbc:UUID>e84c63f9-b6d1-5eaa-bf75-38181a29b84a</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:IssueDate>2026-04-09</cbc:IssueDate>
  <cbc:Note>Approved by the department's facilities officer.</cbc:Note>
  <cbc:AccountingCostCode>PWD-OFF-26</cbc:AccountingCostCode>
  <cbc:AccountingCost>Planning office fit-out 2026</cbc:AccountingCost>
  <cac:Signature>
    <cbc:ID>PWD-SIG-26-WR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:WorkQuantityTotal>
    <cbc:Quantity unitCode="HUR">14</cbc:Quantity>
    <cbc:WorkTypeCode listID="urn:ubl-examples:world:codelist:WorkTypeCode">INSTALL</cbc:WorkTypeCode>
    <cbc:WorkTypeDescription>Installing office furniture.</cbc:WorkTypeDescription>
  </cac:WorkQuantityTotal>
  <cac:ReportedPeriod>
    <cbc:StartDate>2026-04-08</cbc:StartDate>
    <cbc:EndDate>2026-04-09</cbc:EndDate>
  </cac:ReportedPeriod>
  <cac:OrderReference>
    <cbc:ID>LPWD-PO-26-0581</cbc:ID>
  </cac:OrderReference>
  <cac:ProjectReference>
    <cbc:ID>PWD-PLAN-OFFICE-26</cbc:ID>
  </cac:ProjectReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>PWD-COMMIT-26-0381</cbc:ID>
    <cbc:DocumentType>Budget commitment</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-821551</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Joiners Row</cbc:StreetName>
        <cbc:BuildingNumber>14</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71203</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Trade sales</cbc:Name>
        <cbc:JobTitle>Trade sales manager</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 266 466</cbc:Telephone>
        <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-000417</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
        <cbc:Department>Procurement office</cbc:Department>
        <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
        <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Procurement office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 38 2648 0548</cbc:Telephone>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410548</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:ApproverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Public Works Department</cbc:Name>
    </cac:PartyName>
  </cac:ApproverParty>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">AEO</cbc:AllowanceChargeReasonCode>
    <cbc:AllowanceChargeReason>Packaging disposal</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XBL">24.00</cbc:Amount>
  </cac:AllowanceCharge>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
  </cac:TaxTotal>
  <cac:StatementMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">672.00</cbc:LineExtensionAmount>
    <cbc:ChargeTotalAmount currencyID="XBL">24.00</cbc:ChargeTotalAmount>
    <cbc:PayableAmount currencyID="XBL">696.00</cbc:PayableAmount>
  </cac:StatementMonetaryTotal>
  <cac:WorkReportLine>
    <cbc:ID>1</cbc:ID>
    <cbc:WorkItemID>INST</cbc:WorkItemID>
    <cbc:WorkItemDescription>Six desks assembled and placed.</cbc:WorkItemDescription>
    <cbc:Quantity unitCode="HUR">14</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XBL">672.00</cbc:LineExtensionAmount>
    <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">672.00</cbc:TaxInclusiveLineExtensionAmount>
    <cbc:CompletionPercent>100</cbc:CompletionPercent>
    <cac:ActivityOriginLocation>
      <cbc:Name>Lumeport Public Works Department, Civic Square</cbc:Name>
    </cac:ActivityOriginLocation>
    <cac:Period>
      <cbc:StartDate>2026-04-08</cbc:StartDate>
      <cbc:EndDate>2026-04-09</cbc:EndDate>
    </cac:Period>
    <cac:PerformingParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
    </cac:PerformingParty>
    <cac:WorkPhaseReference>
      <cbc:ID>PH-2</cbc:ID>
      <cbc:WorkPhaseCode listID="urn:ubl-examples:world:codelist:WorkPhaseCode">FURNISH</cbc:WorkPhaseCode>
      <cbc:WorkPhase>Furnishing: the new office is furnished</cbc:WorkPhase>
      <cbc:ProgressPercent>100</cbc:ProgressPercent>
      <cbc:StartDate>2026-04-08</cbc:StartDate>
      <cbc:EndDate>2026-04-09</cbc:EndDate>
      <cac:WorkOrderDocumentReference>
        <cbc:ID>LPWD-PO-26-0581</cbc:ID>
      </cac:WorkOrderDocumentReference>
    </cac:WorkPhaseReference>
    <cac:DocumentReference>
      <cbc:ID>BF-CHECK-26-0408</cbc:ID>
      <cbc:DocumentType>Installation checklist</cbc:DocumentType>
    </cac:DocumentReference>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">48</cbc:PriceAmount>
    </cac:Price>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:SubWorkReportLine>
      <cbc:ID>1.1</cbc:ID>
      <cbc:WorkItemID>INST-1</cbc:WorkItemID>
      <cbc:WorkItemDescription>Installer 1: seven hours.</cbc:WorkItemDescription>
      <cbc:Quantity unitCode="HUR">7</cbc:Quantity>
    </cac:SubWorkReportLine>
    <cac:SubWorkReportLine>
      <cbc:ID>1.2</cbc:ID>
      <cbc:WorkItemID>INST-2</cbc:WorkItemID>
      <cbc:WorkItemDescription>Installer 2: seven hours.</cbc:WorkItemDescription>
      <cbc:Quantity unitCode="HUR">7</cbc:Quantity>
    </cac:SubWorkReportLine>
  </cac:WorkReportLine>
</WorkReport>
```
