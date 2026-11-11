# Despatch Advice: Lumeport Textile Mill to Brightmarket Stores

*Example 6 of the flow "Packaging for the benches, clothing for the store" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The mill announces the delivery with the road carrier it booked.

[The XML file](06-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:packaging**  
  The business process the document belongs to: the flow "Packaging for the benches, clothing for the store".
- `ProfileExecutionID` = **PACKAGING-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LTM-DA-26-0526**  
  The despatching party's number.
- `UUID` = **c1af718a-512a-5aed-8622-6a31ae7211c9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-12**  
  The day the shirts left the mill.
- `IssueTime` = **11:35:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DocumentStatusCode` = **NoStatus** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  A new despatch advice, not a correction. The code is from the world's copy of UBL's Document status list, with a listID: NoStatus = No status on document.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage on the consignment note.**  
  What the receiver should do.
- `LineCountNumeric` = **1**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **BS-PO-26-0525**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/WebsiteURI` = **https://www.lumeporttextile.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeport Textile Mill (world/parties.json).
- `Party/IndustryClassificationCode` = **1312** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Textile Mill (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 1312 = Weaving of textiles.
- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-412603** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Textile Mill (world/parties.json).
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Textile Mill (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeport Textile Mill Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeport Textile Mill (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1237809**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeport Textile Mill (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Textile Mill Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeport Textile Mill (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412603**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Lumeport Textile Mill (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 42 persons and its turnover of 4140000.00 XBL in 2025, by the Trade Accord's limits; identity of Lumeport Textile Mill (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2303 2603**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@lumeporttextile.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Textile Mill (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Textile Mill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/WebsiteURI` = **https://www.brightmarket.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brightmarket Stores (world/parties.json).
- `Party/LogoReferenceID` = **BM-LOGO-2024**  
  The reference of the logo the store prints on its documents; identity of Brightmarket Stores (world/parties.json).
- `Party/IndustryClassificationCode` = **4719** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brightmarket Stores (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4719 = Other retail sale in non-specialized stores.
- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `Party/TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered for state sales tax; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered, with its legal form; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410411**  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1979-02-14**  
  The day the company was entered in the register; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **CORP** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: CORP = Corporation (public).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The name of code CORP in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 2900 persons and its turnover of 671000000.00 XBL in 2025, by the Trade Accord's limits; identity of Brightmarket Stores (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **12000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
- `Party/Contact/Name` = **Buying office**  
  The desk that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2511 0411**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `Party/AdditionalWebSite/Name` = **Online shop**  
  The store's second website, where consumers buy.
- `Party/AdditionalWebSite/URI` = **https://shop.brightmarket.example**  
  Under the reserved .example domain.
- `Party/SocialMediaProfile/ID` = **10442197**  
  The profile's number on the medium.
- `Party/SocialMediaProfile/Name` = **brightmarket**  
  The store's profile name.
- `Party/SocialMediaProfile/SocialMediaTypeCode` = **PHOTO** (listID `urn:ubl-examples:world:codelist:SocialMediaTypeCode`)  
  The kind of social medium. The code is from the Trade Accord's social media type list: PHOTO = Photo sharing.
- `Party/SocialMediaProfile/URI` = **https://social.example/brightmarket**  
  The profile's address, under the reserved .example domain.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **LTM-SH-26-0527**  
  The despatching party's shipment number.
- `GrossWeightMeasure` = **168** (unitCode `KGM`)  
  The gross weight of the cartons.
- `Consignment/ID` = **LTM-CS-26-0528**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/CarrierParty/WebsiteURI` = **https://www.bayforth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/IndustryClassificationCode` = **5229** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Bayforth Forwarding (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5229 = Other transportation support activities.
- `Consignment/CarrierParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/CarrierParty/Language/Name` = **English**  
  The language's name.
- `Consignment/CarrierParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/CarrierParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/PartyTaxScheme/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered for state sales tax; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PartyTaxScheme/CompanyID` = **CO-1234932**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyID` = **20411644**  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Consignment/CarrierParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 40 persons and its turnover of 6660000.00 XBL in 2025, by the Trade Accord's limits; identity of Bayforth Forwarding (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/CarrierParty/Contact/Name` = **Export desk**  
  The desk that handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/Contact/Telephone` = **+999 2 38 2144 1644**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `Consignment/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **The store's spring order of shirts.**  
  The line as the order put it.
- `LineStatusCode` = **NoStatus** (listID `urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode`)  
  Despatched as ordered. The code is from the world's copy of UBL's Line status list, with a listID: NoStatus = Line has no status..
- `DeliveredQuantity` = **600** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Men's shirt, woven cotton from Lisavu, in a garment bag.**  
  The seller's description; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/Name` = **Cotton shirt**  
  The item's short name; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/BrandName` = **Lumeport**  
  The brand the maker sells the item under; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/BuyersItemIdentification/ID` = **BM-778120**  
  The buyer's own item number: it resells this item as its item shirt-r.
- `Item/SellersItemIdentification/ID` = **LT-SH-01**  
  The seller's own item number; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/StandardItemIdentification/ID` = **772030000090** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item shirt of Lumeport Textile Mill (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Item/CommodityClassification/CommodityCode` = **620520** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item shirt of Lumeport Textile Mill (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 620520 = Men's or boys' shirts, of cotton.
- `Item/CommodityClassification/ItemClassificationCode` = **28232** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item shirt of Lumeport Textile Mill (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 28232 = Men's or boys' shirts, singlets, underpants, pyjamas, dressing gowns and similar articles, of textile fabric, not knitted or crocheted.
- `Item/AdditionalItemProperty/Name` = **Material**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **100 % cotton grown on Lisavu**  
  Its value; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Sizes**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **S to XL**  
  Its value; item shirt of Lumeport Textile Mill (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:packaging</cbc:ProfileID>
  <cbc:ProfileExecutionID>PACKAGING-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LTM-DA-26-0526</cbc:ID>
  <cbc:UUID>c1af718a-512a-5aed-8622-6a31ae7211c9</cbc:UUID>
  <cbc:IssueDate>2026-05-12</cbc:IssueDate>
  <cbc:IssueTime>11:35:00</cbc:IssueTime>
  <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">NoStatus</cbc:DocumentStatusCode>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage on the consignment note.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>BS-PO-26-0525</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.lumeporttextile.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">1312</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412603</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Mill Street</cbc:StreetName>
        <cbc:BuildingNumber>21</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38504</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeport Textile Mill Ltd</cbc:RegistrationName>
        <cbc:CompanyID>CO-1237809</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeport Textile Mill Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20412603</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 38 2303 2603</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@lumeporttextile.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
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
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
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
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
        <cbc:CompanyID>CO-1231233</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
        <cbc:CompanyID>20410411</cbc:CompanyID>
        <cbc:RegistrationDate>1979-02-14</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">CORP</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XBL">12000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
        <cbc:ID>BM-CT-01</cbc:ID>
        <cbc:Name>Buying office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
        <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
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
    </cac:Party>
  </cac:DeliveryCustomerParty>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>LTM-SH-26-0527</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">168</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>LTM-CS-26-0528</cbc:ID>
      <cac:CarrierParty>
        <cbc:WebsiteURI>https://www.bayforth.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5229</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Bayforth Forwarding</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Dockside Way</cbc:StreetName>
          <cbc:BuildingNumber>4</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38525</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
          <cbc:CompanyID>CO-1234932</cbc:CompanyID>
          <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
          <cac:TaxScheme>
            <cbc:ID>STT</cbc:ID>
            <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
            <cac:JurisdictionRegionAddress>
              <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
          <cbc:CompanyID>20411644</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
          <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
          <cbc:Name>Export desk</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 2 38 2144 1644</cbc:Telephone>
          <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:CarrierParty>
    </cac:Consignment>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>The store's spring order of shirts.</cbc:Note>
    <cbc:LineStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode">NoStatus</cbc:LineStatusCode>
    <cbc:DeliveredQuantity unitCode="EA">600</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Men's shirt, woven cotton from Lisavu, in a garment bag.</cbc:Description>
      <cbc:Name>Cotton shirt</cbc:Name>
      <cbc:BrandName>Lumeport</cbc:BrandName>
      <cac:BuyersItemIdentification>
        <cbc:ID>BM-778120</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>LT-SH-01</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">772030000090</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">620520</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">28232</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Material</cbc:Name>
        <cbc:Value>100 % cotton grown on Lisavu</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Sizes</cbc:Name>
        <cbc:Value>S to XL</cbc:Value>
      </cac:AdditionalItemProperty>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
