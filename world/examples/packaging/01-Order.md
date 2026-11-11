# Order: Valdara Industries to Rivermouth Packaging

*Example 1 of the flow "Packaging for the benches, clothing for the store" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

Bench packaging, collected by the road carrier the manufacturer books. Delivery terms FCA packaging maker.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **PACKAGING-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-PO-26-0521**  
  The buyer's order number.
- `UUID` = **bb51160f-cb33-5e41-a695-75ac4b4523df**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-27**  
  The manufacturer orders pallet film.
- `IssueTime` = **08:44:00**  
  The time the sender's system issued the document, in the sender's local time.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `AccountingCostCode` = **3100**  
  The buyer's cost centre, to be quoted on the invoice.
- `AccountingCost` = **Raw materials and parts**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `Party/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 3083 persons and its turnover of 23600000000 XUF in 2025, by the Trade Accord's limits; identity of Valdara Industries (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/SecurityListing/ID` = **XU0001042501** (schemeID `ISO 6166`)  
  The identifier of the listed shares, in the form of an ISIN with the world's country code. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `Party/PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `Party/PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The name of code XFER in the Trade Accord's market identifier list.
- `Party/PartyLegalEntity/SecurityListing/MarketCode` = **XFER** (listID `urn:ubl-examples:world:codelist:MarketCode`)  
  The market's code. The code is from the Trade Accord's market identifier list: XFER = Ferrano Stock Exchange.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ServiceProviderParty/ID` = **VI-SP-2026-01**  
  The number of the service contract between the two; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/ServiceTypeCode` = **LOGISTICS** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  The kind of service, as a code. The code is from the Trade Accord's service type list: LOGISTICS = Logistics service.
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/WebsiteURI` = **https://www.rivermouth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rivermouth Packaging (world/parties.json).
- `Party/IndustryClassificationCode` = **2220** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rivermouth Packaging (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 2220 = Manufacture of plastics products.
- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:20274** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Rivermouth Packaging (world/parties.json).
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered for state sales tax; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1238220** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Rivermouth Packaging (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered, with its legal form; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rivermouth Packaging (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 23 persons and its turnover of 6800000.00 XBL in 2025, by the Trade Accord's limits; identity of Rivermouth Packaging (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2440 2740**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `Party/FinancialAccount/ID` = **XB96BLUM38020504712805** (schemeID `urn:ubl-examples:world:account`)  
  The party's account, given with its details so that payments can be sent to it. The number follows the structure of ISO 13616 with its check digits, with the world's country code, and holds the codes of the bank and the branch that keep it; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `Party/FinancialAccount/Name` = **Rivermouth Packaging Ltd**  
  The account holder, as the bank knows it.
- `Party/FinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `Party/FinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `Party/FinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/FinancialAccount/FinancialInstitutionBranch/ID` = **380205** (schemeID `urn:ubl-examples:world:XB:bank-branch`)  
  The branch that keeps the account, by its national code: the sort code of a Bayvarran bank branch (six digits, British style; the first two name the bank). The account number holds it.
- `Party/FinancialAccount/FinancialInstitutionBranch/Name` = **Harbour branch**  
  The branch's name.
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUMXBLX** (schemeID `urn:ubl-examples:world:bank-identifier`)  
  The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 (a BIC) with the world's country codes: the bank code BLUM, the country XB and the location LX; identity of Bank of Lumeport (world/parties.json).
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  The bank's head office; identity of Bank of Lumeport (world/parties.json).
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Its building number; identity of Bank of Lumeport (world/parties.json).
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  Its town; identity of Bank of Lumeport (world/parties.json).
- `Party/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The bank's country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/FinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The town the branch is in.
- `Party/FinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/FinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `Despatch/DespatchParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SellerSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Despatch/DespatchParty/PartyName/Name` = **Rivermouth Packaging**  
  The same party as at SellerSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Despatch/CarrierParty/WebsiteURI` = **https://www.trasvia.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/IndustryClassificationCode` = **4923** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Trasvia Haulage (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4923 = Freight transport by road.
- `Despatch/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Despatch/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Despatch/CarrierParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Despatch/CarrierParty/PostalAddress/ID` = **4160203746888095** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Despatch/CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Despatch/CarrierParty/PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Despatch/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Despatch/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Despatch/CarrierParty/PartyTaxScheme/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered for value added tax; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PartyTaxScheme/CompanyID` = **XU007337656** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Trasvia Haulage (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `Despatch/CarrierParty/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Despatch/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Despatch/CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Despatch/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered, with its legal form; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `Despatch/CarrierParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 27 persons and its turnover of 386000000 XUF in 2025, by the Trade Accord's limits; identity of Trasvia Haulage (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Despatch/CarrierParty/Contact/Name` = **Planning desk**  
  The desk that handles this document; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/Contact/Telephone` = **+999 1 041 354 4822**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PartyAuthorization/Purpose` = **International road haulage**  
  What the authority has authorized the party to do; identity of Trasvia Haulage (world/parties.json).
- `Despatch/CarrierParty/PartyAuthorization/ValidityPeriod/EndDate` = **2030-06-30**  
  The authorization expires on this date.
- `Despatch/CarrierParty/PartyAuthorization/Certificate/ID` = **XU-HAUL-2020-0877** (schemeID `urn:ubl-examples:world:XU:haulage-licence`)  
  The number of the permit in the register of road haulage licences of Urvania; the schemeID names the register, and with it the authority that keeps it, so no issuer party is needed (decision ID-Q10).
- `Despatch/CarrierParty/PartyAuthorization/Certificate/CertificateTypeCode` = **PERMIT** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A permit issued by an authority of the party's country. The code is from the Trade Accord's certificate type list: PERMIT = Operating permit.
- `Despatch/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Kusul treznul** (languageID `qau`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `Despatch/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Operating permit** (languageID `en-XU`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In English.
- `Despatch/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Despatch/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Trasvia Haulage (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **FCA** (schemeID `INCOTERMS`)  
  Free carrier at the packaging maker: the buyer books the road carrier that collects. The code is from the world's copy of Incoterms 2020: FCA = Free Carrier. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/Description` = **Rivermouth Packaging, dispatch, Lumeport**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **1488.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **1488.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **1488.00** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **480** (unitCode `KGM`)  
  Thirty rolls of 16 kg: wrapping for a month of bench pallets.
- `LineItem/LineExtensionAmount` = **1488.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **3.1** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `KGM`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Stretch film of recycled polyethylene for pallet wrapping, on rolls of 16 kg.**  
  The seller's description; item film-pe of Rivermouth Packaging (world/items.json).
- `LineItem/Item/Name` = **Recycled stretch film**  
  The item's short name; item film-pe of Rivermouth Packaging (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **RP-SF-23**  
  The seller's own item number; item film-pe of Rivermouth Packaging (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **772040000103** (schemeID `urn:ubl-examples:world:item`)  
  The Codana item number of the maker, issued by the Codana Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a number of the world, not a GTIN; item film-pe of Rivermouth Packaging (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item film-pe of Rivermouth Packaging (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `LineItem/Item/CommodityClassification/CommodityCode` = **392010** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item film-pe of Rivermouth Packaging (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 392010 = Other plates, sheets, film, foil and strip, of polymers of ethylene.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **36330** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item film-pe of Rivermouth Packaging (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 36330 = Plates, sheets, film, foil and strip, of plastics, not self-adhesive, non-cellular and not reinforced, laminated, supported or similarly combined with other materials.
- `LineItem/Item/AdditionalItemProperty/Name` = **Thickness**  
  A measured property of the item.
- `LineItem/Item/AdditionalItemProperty/ValueQuantity` = **23** (unitCode `4H`)  
  Its measured value; item film-pe of Rivermouth Packaging (world/items.json).
- `LineItem/Item/CircularityProfile/CircularityTypeCode` = **RECYCLED** (listID `urn:ubl-examples:world:codelist:CircularityTypeCode`)  
  The circular strategy behind the item. The code is from the Trade Accord's circularity type list: RECYCLED = Recycled material.
- `LineItem/Item/CircularityProfile/RecycledContentPercent` = **100**  
  The share of recycled material: the film is made from the recycled granulate.
- `LineItem/Item/CircularityProfile/RecyclabilityPercent` = **100**  
  The share that can be recycled again.
- `LineItem/Item/CircularityProfile/EndOfLifeTreatment/TreatmentPathwayCode` = **MECHRECYCLE** (listID `urn:ubl-examples:world:codelist:TreatmentPathwayCode`)  
  What happens to the item after use. The code is from the Trade Accord's treatment pathway list: MECHRECYCLE = Mechanical recycling.
- `LineItem/Item/CircularityProfile/EndOfLifeTreatment/ProcessingTypeCode` = **MECHANICAL** (listID `urn:ubl-examples:world:codelist:EndOfLifeProcessingCode`)  
  How the used item is processed. The code is from the Trade Accord's end-of-life processing list: MECHANICAL = Mechanical processing.
- `LineItem/Item/CircularityProfile/EndOfLifeTreatment/ImpactCode` = **LOW** (listID `urn:ubl-examples:world:codelist:EnvironmentalImpactLevelCode`)  
  The environmental impact of that end of life: the film becomes granulate again. The code is from the Trade Accord's environmental impact level list: LOW = Low impact.
- `LineItem/Item/CircularityProfile/EndOfLifeTreatment/TreatmentLocation/Name` = **Rinova Recovery's plant, Ferrano**  
  Where it is treated.
- `LineItem/Item/CircularityProfile/EndOfLifeTreatment/TreatmentLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PACKAGING-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-PO-26-0521</cbc:ID>
  <cbc:UUID>bb51160f-cb33-5e41-a695-75ac4b4523df</cbc:UUID>
  <cbc:IssueDate>2026-04-27</cbc:IssueDate>
  <cbc:IssueTime>08:44:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>3100</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw materials and parts</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007299291</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
        <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
        <cac:SecurityListing>
          <cbc:ID schemeID="ISO 6166">XU0001042501</cbc:ID>
          <cbc:Description>Ordinary shares of Valdara Industries</cbc:Description>
          <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
          <cbc:MarketCode listID="urn:ubl-examples:world:codelist:MarketCode">XFER</cbc:MarketCode>
        </cac:SecurityListing>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
          <cbc:Value>+999 1 344 474 4274</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
      <cac:ServiceProviderParty>
        <cbc:ID>VI-SP-2026-01</cbc:ID>
        <cbc:ServiceTypeCode listID="urn:ubl-examples:world:codelist:ServiceTypeCode">LOGISTICS</cbc:ServiceTypeCode>
        <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
        <cac:Party>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Castrano Logistics</cbc:Name>
          </cac:PartyName>
        </cac:Party>
        <cac:SellerContact>
          <cbc:Name>Key account desk</cbc:Name>
        </cac:SellerContact>
      </cac:ServiceProviderParty>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.rivermouth.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">2220</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:20274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-411619</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Estuary Road</cbc:StreetName>
        <cbc:BuildingNumber>28</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38505</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1238220</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
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
        <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:CompanyID>
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
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 38 2440 2740</cbc:Telephone>
        <cbc:ElectronicMail>order@rivermouth.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:FinancialAccount>
        <cbc:ID schemeID="urn:ubl-examples:world:account">XB96BLUM38020504712805</cbc:ID>
        <cbc:Name>Rivermouth Packaging Ltd</cbc:Name>
        <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
        <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:FinancialInstitutionBranch>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:bank-branch">380205</cbc:ID>
          <cbc:Name>Harbour branch</cbc:Name>
          <cac:FinancialInstitution>
            <cbc:ID schemeID="urn:ubl-examples:world:bank-identifier">BLUMXBLX</cbc:ID>
            <cbc:Name>Bank of Lumeport</cbc:Name>
            <cac:Address>
              <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
              <cbc:StreetName>Exchange Street</cbc:StreetName>
              <cbc:BuildingNumber>48</cbc:BuildingNumber>
              <cbc:CityName>Lumeport</cbc:CityName>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:FinancialInstitution>
          <cac:Address>
            <cbc:CityName>Lumeport</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitutionBranch>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:FinancialAccount>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:Despatch>
      <cac:DespatchParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Rivermouth Packaging</cbc:Name>
        </cac:PartyName>
      </cac:DespatchParty>
      <cac:CarrierParty>
        <cbc:WebsiteURI>https://www.trasvia.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">4923</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Trasvia Haulage</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">qau</cbc:ID>
          <cbc:Name>Urvanian</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160203746888095</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qau">Bek Ban Kumek</cbc:StreetName>
          <cbc:StreetName languageID="en-XU">Via dei Trasporti</cbc:StreetName>
          <cbc:BuildingNumber>45</cbc:BuildingNumber>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
          <cbc:PostalZone>4160</cbc:PostalZone>
          <cbc:Region>Province of Ferrano</cbc:Region>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Trasvia Haulage SRU</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007337656</cbc:CompanyID>
          <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
            <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
            <cac:JurisdictionRegionAddress>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Trasvia Haulage SRU</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
          <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
          <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
          <cac:RegistrationAddress>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:RegistrationAddress>
          <cac:CorporateRegistrationScheme>
            <cbc:ID>XU:CR</cbc:ID>
            <cbc:Name>Commercial register of Urvania</cbc:Name>
            <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
            <cac:JurisdictionRegionAddress>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:CorporateRegistrationScheme>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Planning desk</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 041 354 4822</cbc:Telephone>
          <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:PartyAuthorization>
          <cbc:Purpose>International road haulage</cbc:Purpose>
          <cac:ValidityPeriod>
            <cbc:EndDate>2030-06-30</cbc:EndDate>
          </cac:ValidityPeriod>
          <cac:Certificate>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:haulage-licence">XU-HAUL-2020-0877</cbc:ID>
            <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">PERMIT</cbc:CertificateTypeCode>
            <cbc:CertificateType languageID="qau">Kusul treznul</cbc:CertificateType>
            <cbc:CertificateType languageID="en-XU">Operating permit</cbc:CertificateType>
          </cac:Certificate>
        </cac:PartyAuthorization>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104822</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:CarrierParty>
    </cac:Despatch>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">FCA</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>Rivermouth Packaging, dispatch, Lumeport</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">1488.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">1488.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">1488.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="KGM">480</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">1488.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">3.1</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Stretch film of recycled polyethylene for pallet wrapping, on rolls of 16 kg.</cbc:Description>
        <cbc:Name>Recycled stretch film</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>RP-SF-23</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772040000103</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">392010</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">36330</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Thickness</cbc:Name>
          <cbc:ValueQuantity unitCode="4H">23</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:CircularityProfile>
          <cbc:CircularityTypeCode listID="urn:ubl-examples:world:codelist:CircularityTypeCode">RECYCLED</cbc:CircularityTypeCode>
          <cbc:RecycledContentPercent>100</cbc:RecycledContentPercent>
          <cbc:RecyclabilityPercent>100</cbc:RecyclabilityPercent>
          <cac:EndOfLifeTreatment>
            <cbc:TreatmentPathwayCode listID="urn:ubl-examples:world:codelist:TreatmentPathwayCode">MECHRECYCLE</cbc:TreatmentPathwayCode>
            <cbc:ProcessingTypeCode listID="urn:ubl-examples:world:codelist:EndOfLifeProcessingCode">MECHANICAL</cbc:ProcessingTypeCode>
            <cbc:ImpactCode listID="urn:ubl-examples:world:codelist:EnvironmentalImpactLevelCode">LOW</cbc:ImpactCode>
            <cac:TreatmentLocation>
              <cbc:Name>Rinova Recovery's plant, Ferrano</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:TreatmentLocation>
          </cac:EndOfLifeTreatment>
        </cac:CircularityProfile>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
