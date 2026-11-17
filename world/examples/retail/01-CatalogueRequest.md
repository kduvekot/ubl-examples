# Catalogue Request: Brightmarket Stores to Lumeway Distribution

*Example 1 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Catalogue Request in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CATALOGUE-REQUEST-SCHEMA)*

The store asks the distributor for its spring catalogue.

[The XML file](01-CatalogueRequest.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:catalogue-request:1.0#compliant#urn:ubl-examples:world:community:retail:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Catalogue request"; the community specification "Retail community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:catalogue:1.0**  
  The Trade Accord's process profile the document belongs to: catalogue, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **RETAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BS-DOC-26-0217**  
  The sender's number for this document.
- `UUID` = **5e45c6c8-ba0a-5689-b0f9-f653754fd6b8**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `Name` = **Spring catalogue 2026**  
  The catalogue asked for.
- `IssueDate` = **2026-04-20**  
  The store asks for the spring catalogue. As UBL defines it, the party that sends a catalogue request is its ProviderParty.
- `IssueTime` = **08:42:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **For the garden department.**  
  Who it is for.
- `Description` = **Benches and spare parts.**  
  What the store wants to see.
- `PricingUpdateRequestIndicator` = **true**  
  The store wants price updates during the season.
- `ItemUpdateRequestIndicator` = **true**  
  And changes to the items.
- `LineCountNumeric` = **2**  
  Two lines.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-20**  
  For the season.
- `EndDate` = **2026-07-19**  
  Its end.

### Signature

Inside `Signature`:

- `ID` = **BM-SIG-26-0420**  
  The store's seal.
- `SignatoryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
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
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **sales@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Provider Party

Inside `ProviderParty`:

- `WebsiteURI` = **https://www.brightmarket.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brightmarket Stores (world/parties.json).
- `LogoReferenceID` = **BM-LOGO-2024**  
  The reference of the logo the store prints on its documents; identity of Brightmarket Stores (world/parties.json).
- `IndustryClassificationCode` = **4719** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brightmarket Stores (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4719 = Other retail sale in non-specialized stores.
- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brightmarket Stores (world/parties.json).
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered, with its legal form; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/CompanyLegalFormCode` = **CORP** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: CORP = Corporation (public).
- `PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The name of code CORP in Bayvarra's national company legal form list.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Customer service**  
  The party's customer service desk: the desk for its role in this document (it sells); identity of Brightmarket Stores (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2511 0411**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Contact/ElectronicMail` = **service@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `AdditionalWebSite/Name` = **Online shop**  
  The store's second website, where consumers buy.
- `AdditionalWebSite/URI` = **https://shop.brightmarket.example**  
  Under the reserved .example domain.
- `SocialMediaProfile/ID` = **10442197**  
  The profile's number on the medium.
- `SocialMediaProfile/Name` = **brightmarket**  
  The store's profile name.
- `SocialMediaProfile/SocialMediaTypeCode` = **PHOTO** (listID `urn:ubl-examples:world:codelist:SocialMediaTypeCode`)  
  The kind of social medium. The code is from the Trade Accord's social media type list: PHOTO = Photo sharing.
- `SocialMediaProfile/URI` = **https://social.example/brightmarket**  
  The profile's address, under the reserved .example domain.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Contractor Customer Party

Inside `ContractorCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Requested Catalogue Reference

Inside `RequestedCatalogueReference`:

- `ID` = **LD-CAT-SPRING-26**  
  The catalogue as announced at the fair.

### Referenced Contract

Inside `ReferencedContract`:

- `ID` = **LD-BM-SUPPLY-2026**  
  The supply agreement.

### Trading Terms

Inside `TradingTerms`:

- `Information` = **Delivered duty paid to the store.**  
  The terms the store expects.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BM-RANGE-26**  
  The store's range plan.
- `DocumentType` = **Range plan**  
  The kind of document referred to, the store's range plan, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Applicable Territory Address

Inside `ApplicableTerritoryAddress`:

- `Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  For the store in Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Requested Language

Inside `RequestedLanguage`:

- `ID` = **en** (schemeID `ISO 639`)  
  English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Name` = **English**  
  In words.
- `LocaleCode` = **en** (listID `ISO 639`)  
  The locale, as a lower-case ISO 639 code of the world's language list. The code is from the world's copy of ISO 639 Language: en = English.

### Requested Classification Scheme

Inside `RequestedClassificationScheme`:

- `ID` = **HS**  
  Items classified by the Harmonized System.
- `UUID` = **1afc0bc8-8a3e-5d36-b5be-437211032bac**  
  Its UUID.
- `LastRevisionDate` = **2022-01-01**  
  The edition in force.
- `LastRevisionTime` = **00:00:00**  
  From midnight.
- `Note` = **Six-digit subheadings.**  
  The level wanted.
- `Name` = **Harmonized System**  
  In words.
- `Description` = **The international goods classification.**  
  What it is.
- `AgencyID` = **WCO**  
  The World Customs Organization.
- `AgencyName` = **World Customs Organization**  
  In words.
- `VersionID` = **2022**  
  The edition.
- `URI` = **https://www.wcoomd.org**  
  Where it is published.
- `SchemeURI` = **https://www.wcoomd.org/hs**  
  Where the scheme is.
- `LanguageID` = **en**  
  In English.
- `ClassificationCategory/Name` = **Seats**  
  The heading the benches fall in.
- `ClassificationCategory/CodeValue` = **9401**  
  HS heading 94.01.
- `ClassificationCategory/Description` = **Outdoor furniture and its spare parts.**  
  What the category holds.
- `ClassificationCategory/CategorizesClassificationCategory/Name` = **Spare parts**  
  A subcategory the store wants too.
- `ClassificationCategory/CategorizesClassificationCategory/CodeValue` = **FUR-OUT-SP**  
  Its code.

### Catalogue Request Line

Inside `CatalogueRequestLine`:

- `ID` = **1**  
  Benches.
- `ContractSubdivision` = **Garden**  
  The part of the agreement.
- `Note` = **Pallet prices, please.**  
  What the store asks.
- `LineValidityPeriod/EndDate` = **2026-07-19**  
  For the season.
- `RequiredItemLocationQuantity/MinimumQuantity` = **24** (unitCode `EA`)  
  The store's first order.
- `Item/Name` = **Park bench Serra 180**  
  The item asked for.
- `ID` = **2**  
  Spare frames.
- `Item/Name` = **Bench side frame casting**  
  The item asked for.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CatalogueRequest xmlns="urn:oasis:names:specification:ubl:schema:xsd:CatalogueRequest-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:catalogue-request:1.0#compliant#urn:ubl-examples:world:community:retail:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:catalogue:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>RETAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-DOC-26-0217</cbc:ID>
  <cbc:UUID>5e45c6c8-ba0a-5689-b0f9-f653754fd6b8</cbc:UUID>
  <cbc:Name>Spring catalogue 2026</cbc:Name>
  <cbc:IssueDate>2026-04-20</cbc:IssueDate>
  <cbc:IssueTime>08:42:00</cbc:IssueTime>
  <cbc:Note>For the garden department.</cbc:Note>
  <cbc:Description>Benches and spare parts.</cbc:Description>
  <cbc:PricingUpdateRequestIndicator>true</cbc:PricingUpdateRequestIndicator>
  <cbc:ItemUpdateRequestIndicator>true</cbc:ItemUpdateRequestIndicator>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-20</cbc:StartDate>
    <cbc:EndDate>2026-07-19</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:Signature>
    <cbc:ID>BM-SIG-26-0420</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Sales office</cbc:Name>
      <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
      <cbc:ElectronicMail>sales@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ProviderParty>
    <cbc:WebsiteURI>https://www.brightmarket.example</cbc:WebsiteURI>
    <cbc:LogoReferenceID>BM-LOGO-2024</cbc:LogoReferenceID>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4719</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9522610900002</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:TradePartyName>
      <cbc:Name>Brightmarket</cbc:Name>
    </cac:TradePartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-579130</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:CompanyID>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">CORP</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
      <cac:RegistrationAddress>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FBR</cbc:ID>
        <cbc:Name>Federal business register of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Customer service</cbc:Department>
      <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
      <cbc:ElectronicMail>service@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:AdditionalWebSite>
      <cbc:Name>Online shop</cbc:Name>
      <cbc:URI>https://shop.brightmarket.example</cbc:URI>
    </cac:AdditionalWebSite>
    <cac:SocialMediaProfile>
      <cbc:ID>10442197</cbc:ID>
      <cbc:Name>brightmarket</cbc:Name>
      <cbc:SocialMediaTypeCode listID="urn:ubl-examples:world:codelist:SocialMediaTypeCode">PHOTO</cbc:SocialMediaTypeCode>
      <cbc:URI>https://social.example/brightmarket</cbc:URI>
    </cac:SocialMediaProfile>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ProviderParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ContractorCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:ContractorCustomerParty>
  <cac:RequestedCatalogueReference>
    <cbc:ID>LD-CAT-SPRING-26</cbc:ID>
  </cac:RequestedCatalogueReference>
  <cac:ReferencedContract>
    <cbc:ID>LD-BM-SUPPLY-2026</cbc:ID>
  </cac:ReferencedContract>
  <cac:TradingTerms>
    <cbc:Information>Delivered duty paid to the store.</cbc:Information>
  </cac:TradingTerms>
  <cac:DocumentReference>
    <cbc:ID>BM-RANGE-26</cbc:ID>
    <cbc:DocumentType>Range plan</cbc:DocumentType>
  </cac:DocumentReference>
  <cac:ApplicableTerritoryAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
    </cac:Country>
  </cac:ApplicableTerritoryAddress>
  <cac:RequestedLanguage>
    <cbc:ID schemeID="ISO 639">en</cbc:ID>
    <cbc:Name>English</cbc:Name>
    <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
  </cac:RequestedLanguage>
  <cac:RequestedClassificationScheme>
    <cbc:ID>HS</cbc:ID>
    <cbc:UUID>1afc0bc8-8a3e-5d36-b5be-437211032bac</cbc:UUID>
    <cbc:LastRevisionDate>2022-01-01</cbc:LastRevisionDate>
    <cbc:LastRevisionTime>00:00:00</cbc:LastRevisionTime>
    <cbc:Note>Six-digit subheadings.</cbc:Note>
    <cbc:Name>Harmonized System</cbc:Name>
    <cbc:Description>The international goods classification.</cbc:Description>
    <cbc:AgencyID>WCO</cbc:AgencyID>
    <cbc:AgencyName>World Customs Organization</cbc:AgencyName>
    <cbc:VersionID>2022</cbc:VersionID>
    <cbc:URI>https://www.wcoomd.org</cbc:URI>
    <cbc:SchemeURI>https://www.wcoomd.org/hs</cbc:SchemeURI>
    <cbc:LanguageID>en</cbc:LanguageID>
    <cac:ClassificationCategory>
      <cbc:Name>Seats</cbc:Name>
      <cbc:CodeValue>9401</cbc:CodeValue>
      <cbc:Description>Outdoor furniture and its spare parts.</cbc:Description>
      <cac:CategorizesClassificationCategory>
        <cbc:Name>Spare parts</cbc:Name>
        <cbc:CodeValue>FUR-OUT-SP</cbc:CodeValue>
      </cac:CategorizesClassificationCategory>
    </cac:ClassificationCategory>
  </cac:RequestedClassificationScheme>
  <cac:CatalogueRequestLine>
    <cbc:ID>1</cbc:ID>
    <cbc:ContractSubdivision>Garden</cbc:ContractSubdivision>
    <cbc:Note>Pallet prices, please.</cbc:Note>
    <cac:LineValidityPeriod>
      <cbc:EndDate>2026-07-19</cbc:EndDate>
    </cac:LineValidityPeriod>
    <cac:RequiredItemLocationQuantity>
      <cbc:MinimumQuantity unitCode="EA">24</cbc:MinimumQuantity>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Name>Park bench Serra 180</cbc:Name>
    </cac:Item>
  </cac:CatalogueRequestLine>
  <cac:CatalogueRequestLine>
    <cbc:ID>2</cbc:ID>
    <cac:Item>
      <cbc:Name>Bench side frame casting</cbc:Name>
    </cac:Item>
  </cac:CatalogueRequestLine>
</CatalogueRequest>
```
