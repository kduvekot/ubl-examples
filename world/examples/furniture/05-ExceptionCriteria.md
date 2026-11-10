# Exception Criteria: Brightmarket Stores to Brackenmere Furniture

*Example 5 of the flow "Furniture for the department store and for public offices (Bayvarra)" · [Exception Criteria in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXCEPTION-CRITERIA-SCHEMA)*

Both agree when a deviation is worth a message: thresholds for forecast variance and sales.

[The XML file](05-ExceptionCriteria.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **BS-DOC-26-0571**  
  The sender's number for its exception criteria.
- `IssueDate` = **2026-03-14**  
  Agreed together with the replenishment policy.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-03-16**  
  Valid for the season.
- `EndDate` = **2026-08-29**  
  Its end.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.brightmarket.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brightmarket Stores (world/parties.json).
- `LogoReferenceID` = **BM-LOGO-2024**  
  The reference of the logo the store prints on its documents; identity of Brightmarket Stores (world/parties.json).
- `IndustryClassificationCode` = **4719** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brightmarket Stores (world/parties.json).
- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered for state sales tax; identity of Brightmarket Stores (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brightmarket Stores (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered, with its legal form; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410411**  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1979-02-14**  
  The day the company was entered in the register; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Corp**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **12000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Contact/Name` = **Buying office**  
  The desk that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Contact/Telephone` = **+999 2 3851 0411**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Brightmarket Stores (world/parties.json).
- `Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `AdditionalWebSite/Name` = **Online shop**  
  The store's second website, where consumers buy.
- `AdditionalWebSite/URI` = **https://shop.brightmarket.example**  
  Under the reserved .example domain.
- `SocialMediaProfile/Name` = **brightmarket**  
  The store's profile name.
- `SocialMediaProfile/SocialMediaTypeCode` = **Photo sharing**  
  The kind of social medium.
- `SocialMediaProfile/URI` = **https://social.example/brightmarket**  
  The profile's address, under the reserved .example domain.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brackenmere Furniture**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Exception Criteria Line

Inside `ExceptionCriteriaLine`:

- `ID` = **1**  
  The only criterion.
- `ThresholdValueComparisonCode` = **LessThan**  
  An exception is raised when actual sales fall below the threshold.
- `ThresholdQuantity` = **5** (unitCode `SET`)  
  Fewer than five sets sold in four weeks is worth a message.
- `SupplyItem/Description` = **Garden bench and two chairs in hardwood, made for the department store's own line.**  
  The seller's description; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/Name` = **Garden bench set Marrow**  
  The item's short name; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/BrandName` = **Brackenmere**  
  The brand the maker sells the item under; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/ModelName` = **Marrow**  
  The model; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/SellersItemIdentification/ID` = **BF-GS-01**  
  The seller's own item number; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/StandardItemIdentification/ID` = **772020000079** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/CommodityClassification/ItemClassificationCode` = **9401.69** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item garden-set of Brackenmere Furniture (world/items.json).
- `SupplyItem/Dimension/AttributeID` = **Bench length**  
  Which dimension.
- `SupplyItem/Dimension/Measure` = **1400** (unitCode `MMT`)  
  Its size.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExceptionCriteria xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExceptionCriteria-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>BS-DOC-26-0571</cbc:ID>
  <cbc:IssueDate>2026-03-14</cbc:IssueDate>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-03-16</cbc:StartDate>
    <cbc:EndDate>2026-08-29</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.brightmarket.example</cbc:WebsiteURI>
    <cbc:LogoReferenceID>BM-LOGO-2024</cbc:LogoReferenceID>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4719</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:TradePartyName>
      <cbc:Name>Brightmarket</cbc:Name>
    </cac:TradePartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
      <cbc:CompanyID>CO-1231233</cbc:CompanyID>
      <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
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
      <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
      <cbc:CompanyID>20410411</cbc:CompanyID>
      <cbc:RegistrationDate>1979-02-14</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Corp</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XBL">12000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Buying office</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 3851 0411</cbc:Telephone>
      <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:AdditionalWebSite>
      <cbc:Name>Online shop</cbc:Name>
      <cbc:URI>https://shop.brightmarket.example</cbc:URI>
    </cac:AdditionalWebSite>
    <cac:SocialMediaProfile>
      <cbc:Name>brightmarket</cbc:Name>
      <cbc:SocialMediaTypeCode>Photo sharing</cbc:SocialMediaTypeCode>
      <cbc:URI>https://social.example/brightmarket</cbc:URI>
    </cac:SocialMediaProfile>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
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
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ExceptionCriteriaLine>
    <cbc:ID>1</cbc:ID>
    <cbc:ThresholdValueComparisonCode>LessThan</cbc:ThresholdValueComparisonCode>
    <cbc:ThresholdQuantity unitCode="SET">5</cbc:ThresholdQuantity>
    <cac:SupplyItem>
      <cbc:Description>Garden bench and two chairs in hardwood, made for the department store's own line.</cbc:Description>
      <cbc:Name>Garden bench set Marrow</cbc:Name>
      <cbc:BrandName>Brackenmere</cbc:BrandName>
      <cbc:ModelName>Marrow</cbc:ModelName>
      <cac:SellersItemIdentification>
        <cbc:ID>BF-GS-01</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">772020000079</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">9401.69</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:Dimension>
        <cbc:AttributeID>Bench length</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1400</cbc:Measure>
      </cac:Dimension>
    </cac:SupplyItem>
  </cac:ExceptionCriteriaLine>
</ExceptionCriteria>
```
