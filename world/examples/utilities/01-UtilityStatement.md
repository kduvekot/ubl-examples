# Utility Statement: Ferrano Energy to Valdara Industries

*Example 1 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The factory's monthly electricity consumption: meter readings and consumption per connection, in the energy and water supply structure.

[The XML file](01-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **FE-DOC-26-0314**  
  The utility's statement number.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `UtilityStatementTypeCode` = **Electricity**  
  The kind of utility the statement is about.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the utility's currency; it has no minor unit.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **FE-INV-26-0313**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.ferranoenergy.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Energy (world/parties.json).
- `IndustryClassificationCode` = **3510** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Energy (world/parties.json).
- `PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Energy**  
  The trading name; identity of Ferrano Energy (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Via della Centrale**  
  Street of the postal address. identity of Ferrano Energy (world/parties.json).
- `PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. identity of Ferrano Energy (world/parties.json).
- `PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Energy (world/parties.json).
- `PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Energy (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Energy (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered for value added tax; identity of Ferrano Energy (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007404785**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Energy (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered, with its legal form; identity of Ferrano Energy (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-105781**  
  Number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1949-01-15**  
  The day the company was entered in the register; identity of Ferrano Energy (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Energy (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **600000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Ferrano Energy (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Ferrano Energy (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Ferrano Energy (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Ferrano Energy (world/parties.json).
- `Contact/Telephone` = **+999 1 4130 5781**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Energy (world/parties.json).
- `Contact/ElectronicMail` = **customer@ferranoenergy.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Energy (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Energy (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Energy (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>FE-DOC-26-0314</cbc:ID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:UtilityStatementTypeCode>Electricity</cbc:UtilityStatementTypeCode>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cac:ParentDocumentReference>
    <cbc:ID>FE-INV-26-0313</cbc:ID>
  </cac:ParentDocumentReference>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.ferranoenergy.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3510</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Energy</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName>Via della Centrale</cbc:StreetName>
      <cbc:BuildingNumber>44</cbc:BuildingNumber>
      <cbc:CityName>Serravona</cbc:CityName>
      <cbc:PostalZone>4130</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU007404785</cbc:CompanyID>
      <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-105781</cbc:CompanyID>
      <cbc:RegistrationDate>1949-01-15</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XUF">600000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Serravona</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XU:CR</cbc:ID>
        <cbc:Name>Commercial register of Urvania</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 4130 5781</cbc:Telephone>
      <cbc:ElectronicMail>customer@ferranoenergy.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105781</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName>Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU007299291</cbc:CompanyID>
      <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
      <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XU:CR</cbc:ID>
        <cbc:Name>Commercial register of Urvania</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 4120 4274</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode>AL</cbc:ChannelCode>
        <cbc:Value>+999 1 7000 4274</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
    <cac:ServiceProviderParty>
      <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Castrano Logistics</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:ServiceProviderParty>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
</UtilityStatement>
```
