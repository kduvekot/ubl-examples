# Catalogue: Valdara Industries to Lumeport Public Works Department

*Example 25 of the flow "A public tender (Bayvarra)" · [Catalogue in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CATALOGUE-SCHEMA)*

The framework contract is ordered from a catalogue: the manufacturer publishes the awarded items and prices, each line pointing to the call for tenders.

[The XML file](25-Catalogue.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:catalogue:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Catalogue". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:catalogue:1.0**  
  The Trade Accord's process profile the document belongs to: catalogue, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-CAT-26-0212**  
  The provider's catalogue number.
- `UUID` = **6ddf87fc-d391-5f9a-8a2e-22b484da6820**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `Name` = **Valdara Industries catalogue**  
  The catalogue's title.
- `IssueDate` = **2026-03-23**  
  Published on Monday 23 March, the first working day after the contract was signed (D28 point 1).
- `IssueTime` = **10:18:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-03-23**  
  The prices apply from the issue date.
- `EndDate` = **2028-03-22**  
  Until the next catalogue.

### Referenced Contract

Inside `ReferencedContract`:

- `ID` = **PWD-2026-PARKS**  
  The framework contract the catalogue belongs to.
- `ContractType` = **Framework contract**  
  Its kind.

### Provider Party

Inside `ProviderParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Contact/Name` = **Order desk**  
  The party's main desk, which handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Order administrator**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 386 4551**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 351 400 5258**  
  The sales desk's mobile number, also under the reserved +999.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
- `Contact/Telephone` = **+999 2 38 8235 3927**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Valdara Industries**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.

### Contractor Customer Party

Inside `ContractorCustomerParty`:

- `Party/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Catalogue Line

Inside `CatalogueLine`:

- `ID` = **1**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **5** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **1** (unitCode `EA`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats (worklist C25). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **49900** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **CON** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: the price agreed in the framework contract. The code is from the Trade Accord's price type list: CON = Contract price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Contract price**  
  The name of code CON in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-03-23**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2028-03-22**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **VI-PL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force (worklist C25). The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  Goods exported from Urvania: no value added tax is charged on an export (category G, free export item). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XU:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Urvania's national list, the list of the seller's country. The code is from Urvania's national value added tax exemption reason list: EXP = Export of goods outside Urvania.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Export of goods outside Urvania**  
  The name of code EXP in Urvania's national value added tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/Description` = **Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/Description` = **Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Park bench Serra 180** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalInformation` = **Zurhul vek krukzan tarkul ziztan stan drek skubir krir vinstaz karhan.** (languageID `qau`)  
  What comes with the item in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.** (languageID `en-XU`)  
  What comes with the item in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; item bench-serra of Valdara Industries (world/items.json). A second Keyword would have to be in another language (UBL rule IND7).
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Bukdrek stezskir rek drek manskan savir gilrir.** (languageID `qau`)  
  The maker's warranty in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Five years on the frame against corrosion.** (languageID `en-XU`)  
  The maker's warranty in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Valdara Industries gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Valdara Industries and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; item bench-serra of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label: Code 128 carries letters and digits.
- `Item/StandardItemIdentification/IssuerScopeID` = **KXU10014**  
  The scope within which Valdara Industries gives its item numbers: its company prefix, the issuing agency code KXU and its Codana company number; what follows is the company's own reference.
- `Item/CatalogueItemIdentification/ID` = **VI-CAT-26-0212-1**  
  The item's place in the catalogue: the catalogue number and the line.
- `Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Item/CommodityClassification/CommodityCode` = **94017910** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-serra of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 94017910 = Benches for parks and gardens, with metal frames.
- `Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Ductile cast iron EN-GJS-400-15, hot-dip galvanised and powder-coated**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Thermally modified ash**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colour of the frame, one of the colours it is offered in.
- `Item/AdditionalItemProperty/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; item bench-serra of Valdara Industries (world/items.json)). One ListValue only: UBL rule IND7 allows a second one only in another language.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Load capacity**  
  The name of code LOAD in the Trade Accord's item property name list.
- `Item/AdditionalItemProperty/NameCode` = **LOAD** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: LOAD = Load capacity.
- `Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **SF**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **xu_t6hq** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Over the slats, from slat end to slat end**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **1660** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Over the armrests, between the outer edges of the armrest pads**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Item/EnvironmentalEmission/ValueMeasure` = **26** (unitCode `KGM`)  
  The emission of one item in this stage of its life: a figure from the maker's footprint study, not an activity times a factor, so no factor and base (worklist C09).
- `Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Item/EnvironmentalEmission/LifecycleStageCode` = **SOURCING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The stage of the bench's life the figure covers (D10): the footprint is stated stage by stage. The code is from the Trade Accord's life cycle stage list: SOURCING = Sourcing.
- `Item/EnvironmentalEmission/LifecycleStageDescription` = **Raw material supply and its transport, EN 15804 modules A1 and A2: the ore from the mine, the slats, the stainless bolts, the zinc, the iron's alloys, the powder coat and the packaging, and their transport to Ferrano.**  
  That stage in words, with the modules of EN 15804 it covers.
- `Item/EnvironmentalEmission/Description` = **The fossil greenhouse gases of the materials one bench uses, before they reach Valdara's works. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).**  
  What the figure includes, and what it leaves out.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc**  
  Where the factors come from.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Item/EnvironmentalEmission/ValueMeasure` = **43** (unitCode `KGM`)  
  The emission of one item in this stage of its life: a figure from the maker's footprint study, not an activity times a factor, so no factor and base (worklist C09).
- `Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Item/EnvironmentalEmission/LifecycleStageCode` = **MANUFACTURING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The stage of the bench's life the figure covers (D10): the footprint is stated stage by stage. The code is from the Trade Accord's life cycle stage list: MANUFACTURING = Manufacturing.
- `Item/EnvironmentalEmission/LifecycleStageDescription` = **Making the bench, EN 15804 module A3: iron from the Serravona ore in Valdara's blast furnace, casting in its foundry, galvanising, powder coating and packing.**  
  That stage in words, with the modules of EN 15804 it covers.
- `Item/EnvironmentalEmission/Description` = **The fossil greenhouse gases of making one bench in Valdara's works in Ferrano, most of them from the iron; the pallet is left out as transport packaging that goes back. With the sourcing figure, 69 kg CO2 equivalent from the mine to the factory gate. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).**  
  What the figure includes, and what it leaves out.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc**  
  Where the factors come from.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/MaintenanceFrequencyCode` = **YEARLY** (listID `urn:ubl-examples:world:codelist:MaintenanceFrequencyCode`)  
  How often the item needs maintenance. The code is from the Trade Accord's maintenance frequency list: YEARLY = Once a year.
- `Item/CircularityProfile/MaintenanceFrequencyDescription` = **Once a year: tighten the slat bolts, touch up the frame coating, clean the slats and check them for splits.**  
  What the maintenance is.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **IRON** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: IRON = Iron.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Ductile iron made from Serravona ore in Urvania, as poured for the two side frames less the gates remelted**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **HARDWOOD** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: HARDWOOD = Hardwood.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **21.2** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Thermally modified ash slats from Upland State, Bayvarra**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **PACKAGING** (listID `urn:ubl-examples:world:codelist:WasteTypeCode`)  
  The kind of waste the item leaves. The code is from the Trade Accord's waste type list: PACKAGING = Packaging.
- `Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **The two frame cartons and the slat bundle's straps, edge protectors, end caps and film, and a quarter of the pallet's slip sheet, top cap and stretch film, per bench; the pallet itself goes back**  
  The waste in words.
- `Item/CircularityProfile/WasteGenerated/WasteMeasure` = **3.3** (unitCode `KGM`)  
  How much of it per item.
- `Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **REPAIR10** (listID `urn:ubl-examples:world:codelist:ScoringSystemCode`)  
  The scale of the score. The code is from the Trade Accord's scoring system list: REPAIR10 = Repairability index, 0 to 10.
- `Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `CallForTendersLineReference/LineID` = **1**  
  The line of the call for tenders.
- `CallForTendersDocumentReference/ID` = **LPWD-DOC-26-0189**  
  The call for tenders the line was awarded under.
- `ID` = **2**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **5** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **1** (unitCode `EA`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats (worklist C25). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **1800** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **CON** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: the price agreed in the framework contract. The code is from the Trade Accord's price type list: CON = Contract price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Contract price**  
  The name of code CON in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-03-23**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2028-03-22**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **VI-PL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force (worklist C25). The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  A service supplied outside Urvania, to a customer established abroad, is outside the scope of Urvania's value added tax (category O). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **SVCABROAD** (listID `urn:ubl-examples:world:XU:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Urvania's national list, the list of the seller's country. The code is from Urvania's national value added tax exemption reason list: SVCABROAD = Service supplied outside Urvania.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Service supplied outside Urvania**  
  The name of code SVCABROAD in Urvania's national value added tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/Description` = **Kartran zan nanskir trek drek tarkul vek drek zurhul ziztan, man drek sikgir bakbek.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-installation of Valdara Industries (world/items.json).
- `Item/Description` = **Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries; item bench-installation of Valdara Industries (world/items.json).
- `Item/Name` = **Dreknul skul sir haz nanskir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-installation of Valdara Industries (world/items.json).
- `Item/Name` = **Installation of a park bench** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-installation of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **VI-INST-B**  
  The seller's own item number; item bench-installation of Valdara Industries (world/items.json).
- `Item/CatalogueItemIdentification/ID` = **VI-CAT-26-0212-2**  
  The item's place in the catalogue: the catalogue number and the line.
- `CallForTendersLineReference/LineID` = **2**  
  The line of the call for tenders.
- `CallForTendersDocumentReference/ID` = **LPWD-DOC-26-0189**  
  The call for tenders the line was awarded under.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Catalogue xmlns="urn:oasis:names:specification:ubl:schema:xsd:Catalogue-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:catalogue:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:catalogue:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-CAT-26-0212</cbc:ID>
  <cbc:UUID>6ddf87fc-d391-5f9a-8a2e-22b484da6820</cbc:UUID>
  <cbc:Name>Valdara Industries catalogue</cbc:Name>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>10:18:00-01:00</cbc:IssueTime>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-03-23</cbc:StartDate>
    <cbc:EndDate>2028-03-22</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ReferencedContract>
    <cbc:ID>PWD-2026-PARKS</cbc:ID>
    <cbc:ContractType>Framework contract</cbc:ContractType>
  </cac:ReferencedContract>
  <cac:ProviderParty>
    <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
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
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
      <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
      <cac:RegistrationAddress>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
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
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Order administrator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
        <cbc:Value>+999 1 351 400 5258</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ProviderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Public Works Department</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
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
  </cac:ReceiverParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ContractorCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:ContractorCustomerParty>
  <cac:CatalogueLine>
    <cbc:ID>1</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">5</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">1</cbc:MinimumQuantity>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">49900</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">CON</cbc:PriceTypeCode>
        <cbc:PriceType>Contract price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-03-23</cbc:StartDate>
          <cbc:EndDate>2028-03-22</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>VI-PL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
      </cac:Price>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XU:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export of goods outside Urvania</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.</cbc:Description>
      <cbc:Description languageID="en-XU">Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.</cbc:Description>
      <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
      <cbc:Name languageID="en-XU">Park bench Serra 180</cbc:Name>
      <cbc:AdditionalInformation languageID="qau">Zurhul vek krukzan tarkul ziztan stan drek skubir krir vinstaz karhan.</cbc:AdditionalInformation>
      <cbc:AdditionalInformation languageID="en-XU">Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
      <cbc:Keyword>park bench, street furniture</cbc:Keyword>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180</cbc:ModelName>
      <cbc:WarrantyInformation languageID="qau">Bukdrek stezskir rek drek manskan savir gilrir.</cbc:WarrantyInformation>
      <cbc:WarrantyInformation languageID="en-XU">Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
        <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
        <cbc:IssuerScopeID>KXU10014</cbc:IssuerScopeID>
      </cac:StandardItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>VI-CAT-26-0212-1</cbc:ID>
      </cac:CatalogueItemIdentification>
      <cac:ItemSpecificationDocumentReference>
        <cbc:ID>VI-DS-B180</cbc:ID>
      </cac:ItemSpecificationDocumentReference>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">94017910</cbc:CommodityCode>
      </cac:CommodityClassification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Frame material</cbc:Name>
        <cbc:Value>Ductile cast iron EN-GJS-400-15, hot-dip galvanised and powder-coated</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Slat wood</cbc:Name>
        <cbc:Value>Thermally modified ash</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Seats</cbc:Name>
        <cbc:Value>3</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:ID>COL</cbc:ID>
        <cbc:Name>Frame colour</cbc:Name>
        <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
        <cbc:ListValue>Ferro grey</cbc:ListValue>
        <cac:ItemPropertyGroup>
          <cbc:ID>APP</cbc:ID>
          <cbc:Name>Appearance</cbc:Name>
          <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
        </cac:ItemPropertyGroup>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:ID>LOAD</cbc:ID>
        <cbc:Name>Load capacity</cbc:Name>
        <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">LOAD</cbc:NameCode>
        <cbc:TestMethod>Static load on the seat for one hour, three seats loaded evenly, no lasting deformation</cbc:TestMethod>
        <cbc:ValueQuantity unitCode="KGM">450</cbc:ValueQuantity>
        <cbc:ValueQualifier>Distributed over the seat</cbc:ValueQualifier>
        <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
        <cac:ItemPropertyGroup>
          <cbc:ID>SAF</cbc:ID>
          <cbc:Name>Safety</cbc:Name>
          <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
        </cac:ItemPropertyGroup>
        <cac:StandardPropertyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:property">UR-SF-0450</cbc:ID>
          <cbc:IssuerScopeID>SF</cbc:IssuerScopeID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_t6hq</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Codana Identification Agency</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:StandardPropertyIdentification>
      </cac:AdditionalItemProperty>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1800</cbc:Measure>
        <cbc:Description>Over the slats, from slat end to slat end</cbc:Description>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1660</cbc:Measure>
        <cbc:Description>Over the armrests, between the outer edges of the armrest pads</cbc:Description>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">DEPTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">620</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">780</cbc:Measure>
        <cbc:Description>Seat back at its highest point</cbc:Description>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">450</cbc:Measure>
        <cbc:Description>Above the ground when anchored</cbc:Description>
        <cbc:MinimumMeasure unitCode="MMT">440</cbc:MinimumMeasure>
        <cbc:MaximumMeasure unitCode="MMT">460</cbc:MaximumMeasure>
      </cac:Dimension>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">26</cbc:ValueMeasure>
        <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
        <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">SOURCING</cbc:LifecycleStageCode>
        <cbc:LifecycleStageDescription>Raw material supply and its transport, EN 15804 modules A1 and A2: the ore from the mine, the slats, the stainless bolts, the zinc, the iron's alloys, the powder coat and the packaging, and their transport to Ferrano.</cbc:LifecycleStageDescription>
        <cbc:Description>The fossil greenhouse gases of the materials one bench uses, before they reach Valdara's works. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:EmissionFactorSource>Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc</cbc:EmissionFactorSource>
          <cac:EmissionFactorDocumentReference>
            <cbc:ID>VI-LCA-2025</cbc:ID>
          </cac:EmissionFactorDocumentReference>
        </cac:EmissionCalculationMethod>
        <cac:MeasurementPeriod>
          <cbc:StartDate>2025-01-01</cbc:StartDate>
          <cbc:EndDate>2025-12-31</cbc:EndDate>
        </cac:MeasurementPeriod>
      </cac:EnvironmentalEmission>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">43</cbc:ValueMeasure>
        <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
        <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">MANUFACTURING</cbc:LifecycleStageCode>
        <cbc:LifecycleStageDescription>Making the bench, EN 15804 module A3: iron from the Serravona ore in Valdara's blast furnace, casting in its foundry, galvanising, powder coating and packing.</cbc:LifecycleStageDescription>
        <cbc:Description>The fossil greenhouse gases of making one bench in Valdara's works in Ferrano, most of them from the iron; the pallet is left out as transport packaging that goes back. With the sourcing figure, 69 kg CO2 equivalent from the mine to the factory gate. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:EmissionFactorSource>Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc</cbc:EmissionFactorSource>
          <cac:EmissionFactorDocumentReference>
            <cbc:ID>VI-LCA-2025</cbc:ID>
          </cac:EmissionFactorDocumentReference>
        </cac:EmissionCalculationMethod>
        <cac:MeasurementPeriod>
          <cbc:StartDate>2025-01-01</cbc:StartDate>
          <cbc:EndDate>2025-12-31</cbc:EndDate>
        </cac:MeasurementPeriod>
      </cac:EnvironmentalEmission>
      <cac:CircularityProfile>
        <cbc:MaintenanceFrequencyCode listID="urn:ubl-examples:world:codelist:MaintenanceFrequencyCode">YEARLY</cbc:MaintenanceFrequencyCode>
        <cbc:MaintenanceFrequencyDescription>Once a year: tighten the slat bolts, touch up the frame coating, clean the slats and check them for splits.</cbc:MaintenanceFrequencyDescription>
        <cac:ResourceConsumption>
          <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">IRON</cbc:ResourceTypeCode>
          <cbc:ConsumptionMeasure unitCode="KGM">22</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Ductile iron made from Serravona ore in Urvania, as poured for the two side frames less the gates remelted</cbc:ResourceOriginDescription>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:ResourceConsumption>
        <cac:ResourceConsumption>
          <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">HARDWOOD</cbc:ResourceTypeCode>
          <cbc:ConsumptionMeasure unitCode="KGM">21.2</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Thermally modified ash slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:ResourceConsumption>
        <cac:WasteGenerated>
          <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:WasteTypeCode">PACKAGING</cbc:WasteTypeCode>
          <cbc:WasteTypeDescription>The two frame cartons and the slat bundle's straps, edge protectors, end caps and film, and a quarter of the pallet's slip sheet, top cap and stretch film, per bench; the pallet itself goes back</cbc:WasteTypeDescription>
          <cbc:WasteMeasure unitCode="KGM">3.3</cbc:WasteMeasure>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:WasteGenerated>
        <cac:RepairabilityScore>
          <cbc:ScoreNumeric>8</cbc:ScoreNumeric>
          <cbc:ScoringSystemCode listID="urn:ubl-examples:world:codelist:ScoringSystemCode">REPAIR10</cbc:ScoringSystemCode>
        </cac:RepairabilityScore>
        <cac:ProductDocumentationDocumentReference>
          <cbc:ID>VI-RM-B180</cbc:ID>
        </cac:ProductDocumentationDocumentReference>
      </cac:CircularityProfile>
    </cac:Item>
    <cac:CallForTendersLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:CallForTendersLineReference>
    <cac:CallForTendersDocumentReference>
      <cbc:ID>LPWD-DOC-26-0189</cbc:ID>
    </cac:CallForTendersDocumentReference>
  </cac:CatalogueLine>
  <cac:CatalogueLine>
    <cbc:ID>2</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">5</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">1</cbc:MinimumQuantity>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">1800</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">CON</cbc:PriceTypeCode>
        <cbc:PriceType>Contract price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-03-23</cbc:StartDate>
          <cbc:EndDate>2028-03-22</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>VI-PL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
      </cac:Price>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XU:codelist:TaxExemptionReasonCode">SVCABROAD</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Service supplied outside Urvania</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description languageID="qau">Kartran zan nanskir trek drek tarkul vek drek zurhul ziztan, man drek sikgir bakbek.</cbc:Description>
      <cbc:Description languageID="en-XU">Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.</cbc:Description>
      <cbc:Name languageID="qau">Dreknul skul sir haz nanskir</cbc:Name>
      <cbc:Name languageID="en-XU">Installation of a park bench</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-INST-B</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>VI-CAT-26-0212-2</cbc:ID>
      </cac:CatalogueItemIdentification>
    </cac:Item>
    <cac:CallForTendersLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:CallForTendersLineReference>
    <cac:CallForTendersDocumentReference>
      <cbc:ID>LPWD-DOC-26-0189</cbc:ID>
    </cac:CallForTendersDocumentReference>
  </cac:CatalogueLine>
</Catalogue>
```
