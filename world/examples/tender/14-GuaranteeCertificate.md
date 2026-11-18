# Guarantee Certificate: Bank of Lumeport to Lumeport Public Works Department

*Example 14 of the flow "A public tender (Bayvarra)" · [Guarantee Certificate in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GUARANTEE-CERTIFICATE-SCHEMA)*

The guarantor notifies the authority of the bid bond deposited for the manufacturer's tender.

[The XML file](14-GuaranteeCertificate.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:guarantee-certificate:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Guarantee certificate"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BL-DOC-26-0200**  
  The guarantee's number.
- `UUID` = **1f0c3218-ba4e-54bc-868e-8554b9039fee**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-02-24**  
  Issued before the tender deadline.
- `IssueTime` = **08:23:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `GuaranteeTypeCode` = **TENDER** (listID `urn:ubl-examples:world:codelist:GuaranteeTypeCode`)  
  A tender guarantee. The code is from the Trade Accord's financial guarantee type list: TENDER = Tender guarantee.
- `Purpose` = **Guarantee of the tender for the bench procedure.**  
  Its purpose.
- `LiabilityAmount` = **2400.00** (currencyID `XBL`)  
  The bid bond: 2 % of the estimated contract value, as the procurement documents ask.
- `ConstitutionCode` = **BANKGUAR** (listID `urn:ubl-examples:world:codelist:GuaranteeConstitutionCode`)  
  A bank guarantee. The code is from the Trade Accord's guarantee constitution list: BANKGUAR = Bank guarantee.
- `Note` = **Released at the award.**  
  When it ends.

### Applicable Period

Inside `ApplicablePeriod`:

- `StartDate` = **2026-02-21**  
  From.
- `EndDate` = **2026-05-27**  
  Until 90 days after the deadline.

### Applicable Regulation

Inside `ApplicableRegulation`:

- `Name` = **Public Procurement Act, article 61**  
  The rule.
- `LegalReference` = **XB-PPA-2019 art. 61**  
  The reference.
- `OntologyURI` = **https://law.bayvarra.example/ppa#art61**  
  Its URI.

### Guarantee Document Reference

Inside `GuaranteeDocumentReference`:

- `ID` = **BLUM-G-26-0221**  
  The bank's guarantee deed.

### Immobilized Security

Inside `ImmobilizedSecurity`:

- `ImmobilizationCertificateID` = **BLUM-IMM-26-0044**  
  The certificate of the pledged securities.
- `SecurityID` = **XU0001042501** (schemeID `ISO 6166`)  
  The manufacturer's own shares, pledged. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `IssueDate` = **2026-02-21**  
  Pledged.
- `FaceValueAmount` = **2500.00** (currencyID `XBL`)  
  Their face value.
- `MarketValueAmount` = **3100.00** (currencyID `XBL`)  
  Their market value.
- `SharesNumberQuantity` = **250** (unitCode `E21`)  
  250 shares (unit: shares).
- `IssuerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **BLUM-SIG-GC**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Bank of Lumeport**  
  A party referred to from another party's details: its identifier and name are enough.

### Guarantor Party

Inside `GuarantorParty`:

- `PartyIdentification/ID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bank of Lumeport (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bank of Lumeport**  
  The trading name; identity of Bank of Lumeport (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-190996** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/Floor` = **3**  
  The floor of the trade services desk in the bank's building. identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/Room` = **301**  
  The room of the trade services desk. identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/StreetName` = **Exchange Street**  
  Street of the postal address. identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/BuildingName` = **Exchange House**  
  The bank's building, known by its name. identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/BuildingNumber` = **48**  
  Building number of the postal address. identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). identity of Bank of Lumeport (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bank of Lumeport (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Bank of Lumeport Corp**  
  The name under which the party is registered, with its legal form; identity of Bank of Lumeport (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Bank of Lumeport (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Trade services**  
  The party's main desk, which handles this document; identity of Bank of Lumeport (world/parties.json).
- `Contact/JobTitle` = **Trade services officer**  
  The job of the person who answers at the desk; identity of Bank of Lumeport (world/parties.json).
- `Contact/Department` = **Trade services**  
  The department the desk belongs to; identity of Bank of Lumeport (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2670 1370**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bank of Lumeport (world/parties.json).
- `Contact/ElectronicMail` = **trade@bankoflumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bank of Lumeport (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bank of Lumeport (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bank of Lumeport (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Interested Party

Inside `InterestedParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).

### Beneficiary Party

Inside `BeneficiaryParty`:

- `PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/Department` = **Procurement office**  
  The department the post is for. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2648 0548**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GuaranteeCertificate xmlns="urn:oasis:names:specification:ubl:schema:xsd:GuaranteeCertificate-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:guarantee-certificate:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BL-DOC-26-0200</cbc:ID>
  <cbc:UUID>1f0c3218-ba4e-54bc-868e-8554b9039fee</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-24</cbc:IssueDate>
  <cbc:IssueTime>08:23:00-01:00</cbc:IssueTime>
  <cbc:GuaranteeTypeCode listID="urn:ubl-examples:world:codelist:GuaranteeTypeCode">TENDER</cbc:GuaranteeTypeCode>
  <cbc:Purpose>Guarantee of the tender for the bench procedure.</cbc:Purpose>
  <cbc:LiabilityAmount currencyID="XBL">2400.00</cbc:LiabilityAmount>
  <cbc:ConstitutionCode listID="urn:ubl-examples:world:codelist:GuaranteeConstitutionCode">BANKGUAR</cbc:ConstitutionCode>
  <cbc:Note>Released at the award.</cbc:Note>
  <cac:ApplicablePeriod>
    <cbc:StartDate>2026-02-21</cbc:StartDate>
    <cbc:EndDate>2026-05-27</cbc:EndDate>
  </cac:ApplicablePeriod>
  <cac:ApplicableRegulation>
    <cbc:Name>Public Procurement Act, article 61</cbc:Name>
    <cbc:LegalReference>XB-PPA-2019 art. 61</cbc:LegalReference>
    <cbc:OntologyURI>https://law.bayvarra.example/ppa#art61</cbc:OntologyURI>
  </cac:ApplicableRegulation>
  <cac:GuaranteeDocumentReference>
    <cbc:ID>BLUM-G-26-0221</cbc:ID>
  </cac:GuaranteeDocumentReference>
  <cac:ImmobilizedSecurity>
    <cbc:ImmobilizationCertificateID>BLUM-IMM-26-0044</cbc:ImmobilizationCertificateID>
    <cbc:SecurityID schemeID="ISO 6166">XU0001042501</cbc:SecurityID>
    <cbc:IssueDate>2026-02-21</cbc:IssueDate>
    <cbc:FaceValueAmount currencyID="XBL">2500.00</cbc:FaceValueAmount>
    <cbc:MarketValueAmount currencyID="XBL">3100.00</cbc:MarketValueAmount>
    <cbc:SharesNumberQuantity unitCode="E21">250</cbc:SharesNumberQuantity>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
  </cac:ImmobilizedSecurity>
  <cac:Signature>
    <cbc:ID>BLUM-SIG-GC</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bank of Lumeport</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:GuarantorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411370</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bank of Lumeport</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-190996</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:Floor>3</cbc:Floor>
      <cbc:Room>301</cbc:Room>
      <cbc:StreetName>Exchange Street</cbc:StreetName>
      <cbc:BuildingName>Exchange House</cbc:BuildingName>
      <cbc:BuildingNumber>48</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38523</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Bank of Lumeport Corp</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411370</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Trade services</cbc:Name>
      <cbc:JobTitle>Trade services officer</cbc:JobTitle>
      <cbc:Department>Trade services</cbc:Department>
      <cbc:Telephone>+999 2 38 2670 1370</cbc:Telephone>
      <cbc:ElectronicMail>trade@bankoflumeport.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411370</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:GuarantorParty>
  <cac:InterestedParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:InterestedParty>
  <cac:BeneficiaryParty>
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
  </cac:BeneficiaryParty>
</GuaranteeCertificate>
```
