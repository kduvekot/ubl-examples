# Business Card: Lumeway Distribution to Velumi Trading

*Example 1 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Business Card in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-BUSINESS-CARD-SCHEMA)*

The distributor introduces itself to the new island customer.

[The XML file](01-BusinessCard.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:sea**  
  The business process the document belongs to: the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-DOC-26-0123**  
  The sender's number for this document.
- `UUID` = **da594e74-bfa8-5df5-ab8d-930b60c73ea9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-04**  
  Sent before the first offer to the new customer.
- `IssueTime` = **16:39:00**  
  The time the sender's system issued the document, in the sender's local time.
- `VersionID` = **2**  
  The card as updated this year.
- `PreviousVersionID` = **1**  
  Last year's card.
- `BriefDescription` = **Distributor of street and garden furniture for Bayvarra and the islands.**  
  The business in a sentence.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-BC**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
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
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
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
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 0274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Velumi Trading (world/parties.json).
- `PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
- `Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Business Party

Inside `BusinessParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Lumeway Distribution**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Brochure Document Reference

Inside `BrochureDocumentReference`:

- `ID` = **LD-BROCHURE-2026**  
  The distributor's brochure.
- `Attachment/ExternalReference/URI` = **https://www.lumeway.example/brochure-2026.pdf**  
  Where it is.
- `Attachment/ExternalReference/MimeCode` = **application/pdf**  
  A PDF.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **LD-REG-XB**  
  The distributor's registration extract.

### Business Capability

Inside `BusinessCapability`:

- `ID` = **CAP-STOCK**  
  A capability.
- `CapabilityTypeCode` = **Warehousing**  
  What it can do.
- `Description` = **Stock of 2,000 benches in Marrowdale.**  
  In words.
- `ValueAmount` = **1040000.00** (currencyID `XBL`)  
  The stock's value.
- `ValueQuantity` = **2000** (unitCode `H87`)  
  Benches in stock.
- `SuppliedEvidence/ID` = **LD-AUDIT-2025**  
  The evidence.
- `SuppliedEvidence/EvidenceTypeCode` = **Audit**  
  An audit report.
- `SuppliedEvidence/Name` = **Stock count 2025**  
  Its name.
- `SuppliedEvidence/Description` = **Year-end count by the auditor.**  
  What it is.
- `SuppliedEvidence/CandidateStatement` = **The stock is counted every year.**  
  The company's statement.
- `SuppliedEvidence/ConfidentialityLevelCode` = **Public**  
  May be shared.
- `SuppliedEvidence/EvidenceIssuingParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SuppliedEvidence/EvidenceIssuingParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `SuppliedEvidence/Language/ID` = **en**  
  English.
- `ValidityPeriod/EndDate` = **2026-12-30**  
  Until the next count.
- `WebSite/ID` = **WEB-1**  
  The stock page.
- `WebSite/Name` = **Stock**  
  Its name.
- `WebSite/Description` = **Live stock levels.**  
  What it shows.
- `WebSite/WebSiteTypeCode` = **Extranet**  
  For trade customers.
- `WebSite/URI` = **https://www.lumeway.example/stock**  
  Where.
- `WebSite/WebSiteAccess/URI` = **https://www.lumeway.example/login**  
  The login page.
- `WebSite/WebSiteAccess/Password` = ************  
  Never shown.
- `WebSite/WebSiteAccess/Login` = **velumi**  
  The buyer's login.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<BusinessCard xmlns="urn:oasis:names:specification:ubl:schema:xsd:BusinessCard-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-DOC-26-0123</cbc:ID>
  <cbc:UUID>da594e74-bfa8-5df5-ab8d-930b60c73ea9</cbc:UUID>
  <cbc:IssueDate>2026-05-04</cbc:IssueDate>
  <cbc:IssueTime>16:39:00</cbc:IssueTime>
  <cbc:VersionID>2</cbc:VersionID>
  <cbc:PreviousVersionID>1</cbc:PreviousVersionID>
  <cbc:BriefDescription>Distributor of street and garden furniture for Bayvarra and the islands.</cbc:BriefDescription>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-BC</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID>UL-1230822</cbc:CompanyID>
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
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20410274</cbc:CompanyID>
      <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Medium</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 0274</cbc:Telephone>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.velumi.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
      <cbc:StreetName>Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>16</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
      <cbc:CompanyID>IC41859</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XL:ICR</cbc:ID>
        <cbc:Name>Island companies register</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 3 3000 1859</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:BusinessParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
  </cac:BusinessParty>
  <cac:BrochureDocumentReference>
    <cbc:ID>LD-BROCHURE-2026</cbc:ID>
    <cac:Attachment>
      <cac:ExternalReference>
        <cbc:URI>https://www.lumeway.example/brochure-2026.pdf</cbc:URI>
        <cbc:MimeCode>application/pdf</cbc:MimeCode>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:BrochureDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>LD-REG-XB</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:BusinessCapability>
    <cbc:ID>CAP-STOCK</cbc:ID>
    <cbc:CapabilityTypeCode>Warehousing</cbc:CapabilityTypeCode>
    <cbc:Description>Stock of 2,000 benches in Marrowdale.</cbc:Description>
    <cbc:ValueAmount currencyID="XBL">1040000.00</cbc:ValueAmount>
    <cbc:ValueQuantity unitCode="H87">2000</cbc:ValueQuantity>
    <cac:SuppliedEvidence>
      <cbc:ID>LD-AUDIT-2025</cbc:ID>
      <cbc:EvidenceTypeCode>Audit</cbc:EvidenceTypeCode>
      <cbc:Name>Stock count 2025</cbc:Name>
      <cbc:Description>Year-end count by the auditor.</cbc:Description>
      <cbc:CandidateStatement>The stock is counted every year.</cbc:CandidateStatement>
      <cbc:ConfidentialityLevelCode>Public</cbc:ConfidentialityLevelCode>
      <cac:EvidenceIssuingParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:EvidenceIssuingParty>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
      </cac:Language>
    </cac:SuppliedEvidence>
    <cac:ValidityPeriod>
      <cbc:EndDate>2026-12-30</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:WebSite>
      <cbc:ID>WEB-1</cbc:ID>
      <cbc:Name>Stock</cbc:Name>
      <cbc:Description>Live stock levels.</cbc:Description>
      <cbc:WebSiteTypeCode>Extranet</cbc:WebSiteTypeCode>
      <cbc:URI>https://www.lumeway.example/stock</cbc:URI>
      <cac:WebSiteAccess>
        <cbc:URI>https://www.lumeway.example/login</cbc:URI>
        <cbc:Password>********</cbc:Password>
        <cbc:Login>velumi</cbc:Login>
      </cac:WebSiteAccess>
    </cac:WebSite>
  </cac:BusinessCapability>
</BusinessCard>
```
