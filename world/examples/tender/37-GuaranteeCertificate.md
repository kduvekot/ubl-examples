# Guarantee Certificate: Bank of Lumeport to Lumeport Public Works Department

*Example 37 of the flow "A public tender (Bayvarra)" · [Guarantee Certificate in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GUARANTEE-CERTIFICATE-SCHEMA)*

The furniture maker's bank certifies the government bonds immobilised in favour of the authority as the guarantee of the furniture maker's tender.

[The XML file](37-GuaranteeCertificate.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:guarantee-certificate:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Guarantee certificate"; the community specification "Public procurement community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **PWD/2026/PARKS**  
  The collaboration this document belongs to: the department's procurement of park benches. Lumeport Public Works Department started it and gave it this identifier, which every document of it repeats.
- `ID` = **3900039354**  
  The bank's number for the certificate.
- `UUID` = **3e922210-3b62-5068-9bc7-523b9c932e1a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD/2026/PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-02-19**  
  Thursday 19 February, the day after the bonds were deposited and immobilised, the day before Brackenmere's tender.
- `IssueTime` = **16:19:00-01:00**  
  Issued in the afternoon, before the bank's desk closes; in the issuer's local time, with its offset from UTC.
- `GuaranteeTypeCode` = **TENDER** (listID `urn:ubl-examples:world:codelist:GuaranteeTypeCode`)  
  A tender guarantee. The code is from the Trade Accord's financial guarantee type list: TENDER = Tender guarantee.
- `Purpose` = **Guarantee of Brackenmere Furniture's tender in the bench procedure, given by pledging Bayvarran government bonds deposited with the bank, immobilized and pledged in favour of the department on 18 February.**  
  Its purpose and how it is given, with the day the bonds were pledged, from which the guarantee runs, the day before the bank's certificate of it.
- `LiabilityAmount` = **2500.00** (currencyID `XBL`)  
  The tender guarantee: the fixed 2,500 lume the procurement documents ask.
- `ConstitutionCode` = **SECURITIES** (listID `urn:ubl-examples:world:codelist:GuaranteeConstitutionCode`)  
  Immobilized securities: public debt securities pledged in favour of the department, which the notices allow. The code is from the Trade Accord's guarantee constitution list: SECURITIES = Immobilised securities.
- `Note` = **Released for every tenderer once the contract is signed, so that each tenderer stays bound to its tender until then.**  
  When it ends.

### Applicable Period

Inside `ApplicablePeriod`:

- `StartDate` = **2026-02-18**  
  From the immobilization.
- `EndDate` = **2026-05-26**  
  Until 90 days after the deadline, the validity of the tenders, at the latest.

### Applicable Regulation

Inside `ApplicableRegulation`:

- `Name` = **Public Procurement Act, article 61**  
  The rule.
- `LegalReference` = **XB-PPA-2019 art. 61**  
  The reference; no ontology URI for an article of the act.

### Immobilized Security

Inside `ImmobilizedSecurity`:

- `ImmobilizationCertificateID` = **1600002271**  
  The bank's certificate of the immobilized bonds.
- `SecurityID` = **XB0000260313** (schemeID `ISO 6166`)  
  Bayvarran federal bonds, the securities of a third issuer. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `IssueDate` = **2023-09-15**  
  The day the federal government issued the bond (option b: the security's issue date, not the immobilization).
- `FaceValueAmount` = **2632.50** (currencyID `XBL`)  
  Their value on 18 February, the day they were immobilized.
- `MarketValueAmount` = **2640.00** (currencyID `XBL`)  
  Their market value on the certificate's day, above the 2,500 guaranteed.
- `SharesNumberQuantity` = **25** (unitCode `C62`)  
  25 bonds of 100 lume nominal.
- `IssuerParty/PartyIdentification/ID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuerParty/PartyName/Name` = **Bank of Lumeport**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **BLUM-SIG-GC-BF**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Bank of Lumeport**  
  A party referred to from another party's details: its identifier and name are enough.

### Guarantor Party

Inside `GuarantorParty`:

- `PartyIdentification/ID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Bank of Lumeport gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bank of Lumeport**  
  The trading name; as Bank of Lumeport gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-190996** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Bank of Lumeport gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/Floor` = **3**  
  The floor of the trade services desk in the bank's building. As Bank of Lumeport gives it.
- `PostalAddress/Room` = **301**  
  The room of the trade services desk. As Bank of Lumeport gives it.
- `PostalAddress/StreetName` = **Exchange Street**  
  Street of the postal address. As Bank of Lumeport gives it.
- `PostalAddress/BuildingName` = **Exchange House**  
  The bank's building, known by its name. As Bank of Lumeport gives it.
- `PostalAddress/BuildingNumber` = **48**  
  Building number of the postal address. As Bank of Lumeport gives it.
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Bank of Lumeport gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bank of Lumeport gives it.
- `PostalAddress/PostalZone` = **38523**  
  Postal code in Bayvarra's format (5 digits). As Bank of Lumeport gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bank of Lumeport gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Bank of Lumeport Corp**  
  The name under which the party is registered, with its legal form; as Bank of Lumeport gives it.
- `PartyLegalEntity/CompanyID` = **20411370** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Bank of Lumeport gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Trade services**  
  The party's main desk, which handles this document; as Bank of Lumeport gives it.
- `Contact/JobTitle` = **Trade services officer**  
  The job of the person who answers at the desk; as Bank of Lumeport gives it.
- `Contact/Department` = **Trade services**  
  The department the desk belongs to; as Bank of Lumeport gives it.
- `Contact/Telephone` = **+999 2 38 5011 8923**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bank of Lumeport gives it.
- `Contact/ElectronicMail` = **trade@bankoflumeport.example**  
  The contact's e-mail address; as Bank of Lumeport gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bank of Lumeport gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Bank of Lumeport gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Interested Party

Inside `InterestedParty`:

- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.

### Beneficiary Party

Inside `BeneficiaryParty`:

- `PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; as Lumeport Public Works Department gives it.
- `PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Public Works Department gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. As Lumeport Public Works Department gives it.
- `PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. As Lumeport Public Works Department gives it.
- `PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. As Lumeport Public Works Department gives it.
- `PostalAddress/Department` = **Procurement office**  
  The department the post is for. As Lumeport Public Works Department gives it.
- `PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. As Lumeport Public Works Department gives it.
- `PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Public Works Department gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Public Works Department gives it.
- `PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Public Works Department gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Public Works Department gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; as Lumeport Public Works Department gives it.
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; as Lumeport Public Works Department gives it.
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; as Lumeport Public Works Department gives it.
- `Contact/Telephone` = **+999 2 38 8235 3927**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeport Public Works Department gives it.
- `Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  The contact's e-mail address; as Lumeport Public Works Department gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Public Works Department gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GuaranteeCertificate xmlns="urn:oasis:names:specification:ubl:schema:xsd:GuaranteeCertificate-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:guarantee-certificate:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PWD/2026/PARKS</cbc:ProfileExecutionID>
  <cbc:ID>3900039354</cbc:ID>
  <cbc:UUID>3e922210-3b62-5068-9bc7-523b9c932e1a</cbc:UUID>
  <cbc:ContractFolderID>PWD/2026/PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-19</cbc:IssueDate>
  <cbc:IssueTime>16:19:00-01:00</cbc:IssueTime>
  <cbc:GuaranteeTypeCode listID="urn:ubl-examples:world:codelist:GuaranteeTypeCode">TENDER</cbc:GuaranteeTypeCode>
  <cbc:Purpose>Guarantee of Brackenmere Furniture's tender in the bench procedure, given by pledging Bayvarran government bonds deposited with the bank, immobilized and pledged in favour of the department on 18 February.</cbc:Purpose>
  <cbc:LiabilityAmount currencyID="XBL">2500.00</cbc:LiabilityAmount>
  <cbc:ConstitutionCode listID="urn:ubl-examples:world:codelist:GuaranteeConstitutionCode">SECURITIES</cbc:ConstitutionCode>
  <cbc:Note>Released for every tenderer once the contract is signed, so that each tenderer stays bound to its tender until then.</cbc:Note>
  <cac:ApplicablePeriod>
    <cbc:StartDate>2026-02-18</cbc:StartDate>
    <cbc:EndDate>2026-05-26</cbc:EndDate>
  </cac:ApplicablePeriod>
  <cac:ApplicableRegulation>
    <cbc:Name>Public Procurement Act, article 61</cbc:Name>
    <cbc:LegalReference>XB-PPA-2019 art. 61</cbc:LegalReference>
  </cac:ApplicableRegulation>
  <cac:ImmobilizedSecurity>
    <cbc:ImmobilizationCertificateID>1600002271</cbc:ImmobilizationCertificateID>
    <cbc:SecurityID schemeID="ISO 6166">XB0000260313</cbc:SecurityID>
    <cbc:IssueDate>2023-09-15</cbc:IssueDate>
    <cbc:FaceValueAmount currencyID="XBL">2632.50</cbc:FaceValueAmount>
    <cbc:MarketValueAmount currencyID="XBL">2640.00</cbc:MarketValueAmount>
    <cbc:SharesNumberQuantity unitCode="C62">25</cbc:SharesNumberQuantity>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bank of Lumeport</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
  </cac:ImmobilizedSecurity>
  <cac:Signature>
    <cbc:ID>BLUM-SIG-GC-BF</cbc:ID>
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
      <cbc:Telephone>+999 2 38 5011 8923</cbc:Telephone>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
  </cac:InterestedParty>
  <cac:BeneficiaryParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
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
      <cbc:Telephone>+999 2 38 8235 3927</cbc:Telephone>
      <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:6250397184</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:BeneficiaryParty>
</GuaranteeCertificate>
```
