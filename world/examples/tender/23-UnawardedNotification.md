# Unawarded Notification: Lumeport Public Works Department to Brackenmere Furniture

*Example 23 of the flow "A public tender (Bayvarra)" · [Unawarded Notification in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UNAWARDED-NOTIFICATION-SCHEMA)*

The furniture maker is told that the contract went to another tenderer.

[The XML file](23-UnawardedNotification.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:tender**  
  The business process the document belongs to: the flow "A public tender (Bayvarra)".
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0209**  
  The sender's number for this document.
- `UUID` = **e1de7889-b36e-5db6-b38b-dcbd566f2280**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-09**  
  Told on the day of the award decision, as the winner is.
- `IssueTime` = **10:15:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ContractName` = **Park benches for the parks renewal programme**  
  The name of the contract the procedure is for.
- `Note` = **Your tender ranked second. It was lower in price, but the warranty offered scored lower on quality.**  
  Why it lost.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-UNAWD**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Public Works Department (world/parties.json).
- `PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-410548** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Public Works Department (world/parties.json).
- `PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/ID` = **LUM-ADR-000417**  
  The address's number in the city's address register; identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
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
- `PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered for state sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-0900002**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Public Works Department (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/ExemptionReason` = **Public bodies are exempt from the state sales tax**  
  Why purchases by this party carry no sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered, with its legal form; identity of Lumeport Public Works Department (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410548**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Contact/Name` = **Procurement office**  
  The desk that handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Telephone` = **+999 2 3851 0548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.brackenmere.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brackenmere Furniture (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brackenmere Furniture (world/parties.json).
- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered for state sales tax; identity of Brackenmere Furniture (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1237398**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brackenmere Furniture (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered, with its legal form; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412466**  
  Number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Contact/Name` = **Trade sales**  
  The desk that handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Telephone` = **+999 2 7120 2466**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Brackenmere Furniture (world/parties.json).
- `Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Minutes Document Reference

Inside `MinutesDocumentReference`:

- `ID` = **PWD-MIN-AWARD-26**  
  The minutes of the evaluation.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **PWD-EVAL-SCORES-BF**  
  The furniture maker's scores.

### Tender Result

Inside `TenderResult`:

- `AwardID` = **PWD-2026-PARKS-AWARD-1**  
  The award decision.
- `TenderResultCode` = **Awarded**  
  The contract is awarded.
- `Description` = **Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.**  
  Why it won.
- `AwardDate` = **2026-03-09**  
  The day the contract was awarded to another tenderer.
- `AwardTime` = **09:30:00**  
  The time of the decision, before the tenderers are told.
- `Contract/ID` = **PWD-2026-PARKS**  
  The framework contract.
- `Contract/ContractTypeCode` = **Framework**  
  A framework contract.
- `Contract/ValidityPeriod/StartDate` = **2026-03-23**  
  From the first call-off.
- `Contract/ValidityPeriod/DurationMeasure` = **24** (unitCode `MON`)  
  Two years.
- `AwardedTenderedProject/VariantID` = **V0**  
  The main offer.
- `AwardedTenderedProject/ProcurementProjectLot/ID` = **LOT-1**  
  Lot 1 of the procedure.
- `AwardedTenderedProject/ProcurementProjectLot/ID` = **LOT-2**  
  Lot 2 of the procedure.
- `AwardedTenderedProject/LegalMonetaryTotal/PayableAmount` = **124080.00** (currencyID `XBL`)  
  240 benches at 499 lume and their installation at 18 lume each.
- `ContractFormalizationPeriod/StartDate` = **2026-03-19**  
  After the standstill period.
- `ContractFormalizationPeriod/EndDate` = **2026-03-22**  
  Before the first call-off.
- `SubcontractTerms/Rate` = **0**  
  The manufacturer installs with its own staff.
- `SubcontractTerms/UnknownPriceIndicator` = **false**  
  Nothing is subcontracted.
- `SubcontractTerms/Description` = **No subcontracting.**  
  The tender's terms.
- `WinningParty/Rank` = **1**  
  First in the evaluation.
- `WinningParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `WinningParty/Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Appeal Terms

Inside `AppealTerms`:

- `Description` = **An appeal against the decision goes to the review board within ten days.**  
  How to appeal.
- `PresentationPeriod/StartDate` = **2026-03-09**  
  From the decision.
- `PresentationPeriod/EndDate` = **2026-03-19**  
  Ten days later, the end of the standstill period.
- `AppealInformationParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AppealInformationParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.
- `AppealReceiverParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.
- `MediationParty/PartyIdentification/ID` = **20410822** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `MediationParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UnawardedNotification xmlns="urn:oasis:names:specification:ubl:schema:xsd:UnawardedNotification-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:tender</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0209</cbc:ID>
  <cbc:UUID>e1de7889-b36e-5db6-b38b-dcbd566f2280</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-09</cbc:IssueDate>
  <cbc:IssueTime>10:15:00</cbc:IssueTime>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:Note>Your tender ranked second. It was lower in price, but the warranty offered scored lower on quality.</cbc:Note>
  <cac:Signature>
    <cbc:ID>PWD-SIG-UNAWD</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410548</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Public Works Department</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID>LUM-ADR-000417</cbc:ID>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Civic Square</cbc:StreetName>
      <cbc:BuildingNumber>6</cbc:BuildingNumber>
      <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
      <cbc:Department>Procurement office</cbc:Department>
      <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38517</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
      <cbc:CompanyID>CO-0900002</cbc:CompanyID>
      <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
      <cbc:ExemptionReason>Public bodies are exempt from the state sales tax</cbc:ExemptionReason>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
        <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
      <cbc:CompanyID>20410548</cbc:CompanyID>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FBR</cbc:ID>
        <cbc:Name>Federal business register of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Procurement office</cbc:Name>
      <cbc:JobTitle>Procurement officer</cbc:JobTitle>
      <cbc:Department>Procurement</cbc:Department>
      <cbc:Telephone>+999 2 3851 0548</cbc:Telephone>
      <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.brackenmere.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Joiners Row</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71203</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
      <cbc:CompanyID>UL-1237398</cbc:CompanyID>
      <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
        <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20412466</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FBR</cbc:ID>
        <cbc:Name>Federal business register of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Trade sales</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7120 2466</cbc:Telephone>
      <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:MinutesDocumentReference>
    <cbc:ID>PWD-MIN-AWARD-26</cbc:ID>
  </cac:MinutesDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>PWD-EVAL-SCORES-BF</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:TenderResult>
    <cbc:AwardID>PWD-2026-PARKS-AWARD-1</cbc:AwardID>
    <cbc:TenderResultCode>Awarded</cbc:TenderResultCode>
    <cbc:Description>Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.</cbc:Description>
    <cbc:AwardDate>2026-03-09</cbc:AwardDate>
    <cbc:AwardTime>09:30:00</cbc:AwardTime>
    <cac:Contract>
      <cbc:ID>PWD-2026-PARKS</cbc:ID>
      <cbc:ContractTypeCode>Framework</cbc:ContractTypeCode>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-03-23</cbc:StartDate>
        <cbc:DurationMeasure unitCode="MON">24</cbc:DurationMeasure>
      </cac:ValidityPeriod>
    </cac:Contract>
    <cac:AwardedTenderedProject>
      <cbc:VariantID>V0</cbc:VariantID>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-1</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-2</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:LegalMonetaryTotal>
        <cbc:PayableAmount currencyID="XBL">124080.00</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:AwardedTenderedProject>
    <cac:ContractFormalizationPeriod>
      <cbc:StartDate>2026-03-19</cbc:StartDate>
      <cbc:EndDate>2026-03-22</cbc:EndDate>
    </cac:ContractFormalizationPeriod>
    <cac:SubcontractTerms>
      <cbc:Rate>0</cbc:Rate>
      <cbc:UnknownPriceIndicator>false</cbc:UnknownPriceIndicator>
      <cbc:Description>No subcontracting.</cbc:Description>
    </cac:SubcontractTerms>
    <cac:WinningParty>
      <cbc:Rank>1</cbc:Rank>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:WinningParty>
  </cac:TenderResult>
  <cac:AppealTerms>
    <cbc:Description>An appeal against the decision goes to the review board within ten days.</cbc:Description>
    <cac:PresentationPeriod>
      <cbc:StartDate>2026-03-09</cbc:StartDate>
      <cbc:EndDate>2026-03-19</cbc:EndDate>
    </cac:PresentationPeriod>
    <cac:AppealInformationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
      </cac:PartyName>
    </cac:AppealInformationParty>
    <cac:AppealReceiverParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
      </cac:PartyName>
    </cac:AppealReceiverParty>
    <cac:MediationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
      </cac:PartyName>
    </cac:MediationParty>
  </cac:AppealTerms>
</UnawardedNotification>
```
