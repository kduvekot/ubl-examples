# Catalogue: Rinova Recovery to Rivermouth Packaging

*Example 12 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Catalogue in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CATALOGUE-SCHEMA)*

Before the packaging maker orders, Rinova sends it the product information of its granulate for the quarter: the item, its price, and what makes it recycled granulate, the recycled-content certificate of the accredited certification body that audits Rinova's plant and the item's recycled content of 100 %.

[The XML file](12-Catalogue.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:catalogue:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Catalogue". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:catalogue:1.0**  
  The Trade Accord's process profile the document belongs to: catalogue, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0373**  
  The collaboration this document belongs to: Rinova's product information of the quarter for Rivermouth. Rinova Recovery started it and gave it this identifier: the document is the whole exchange.
- `ID` = **26-0002**  
  The provider's catalogue number.
- `UUID` = **c8939b73-1616-5856-9d43-118e4ddb2b7e**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `Name` = **Recycled PE granulate, second quarter 2026**  
  The catalogue's title: one product, for the quarter.
- `IssueDate` = **2026-04-01**  
  Rinova's product information for the quarter, sent before the packaging maker plans its next production run.
- `IssueTime` = **15:16:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-01**  
  The prices apply from the issue date.
- `EndDate` = **2026-06-30**  
  Until the next catalogue.

### Provider Party

Inside `ProviderParty`:

- `WebsiteURI` = **https://www.rinova.example**  
  The party's website; as Rinova Recovery gives it.
- `IndustryClassificationCode` = **3830** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; as Rinova Recovery gives it. The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3830 = Materials recovery.
- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Rinova Recovery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:13362** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rinova Recovery gives it.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; as Rinova Recovery gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Rinova Recovery gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Rinova Recovery gives it.
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Rinova Recovery gives it.
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. As Rinova Recovery gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). As Rinova Recovery gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Rinova Recovery gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered, with its legal form; as Rinova Recovery gives it.
- `PartyLegalEntity/CompanyID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Rinova Recovery gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world.
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Rinova Recovery gives it.
- `Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Rinova Recovery gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Rinova Recovery gives it.
- `Contact/Telephone` = **+999 1 041 697 6856**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Rinova Recovery gives it.
- `Contact/ElectronicMail` = **sales@rinova.example**  
  The contact's e-mail address; as Rinova Recovery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rinova Recovery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Rinova Recovery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Rivermouth Packaging gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:15128** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rivermouth Packaging gives it.
- `PartyName/Name` = **Rivermouth Packaging**  
  The trading name; as Rivermouth Packaging gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Rivermouth Packaging gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. As Rivermouth Packaging gives it.
- `PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. As Rivermouth Packaging gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Rivermouth Packaging gives it.
- `PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). As Rivermouth Packaging gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Rivermouth Packaging gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Rivermouth Packaging gives it.
- `Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Rivermouth Packaging gives it.
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Rivermouth Packaging gives it.
- `Contact/Telephone` = **+999 2 38 7320 9007**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Rivermouth Packaging gives it.
- `Contact/ElectronicMail` = **purchasing@rivermouth.example**  
  The contact's e-mail address; as Rivermouth Packaging gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rivermouth Packaging gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Rivermouth Packaging gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Rinova Recovery**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.

### Catalogue Line

Inside `CatalogueLine`:

- `ID` = **1**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **5** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **1** (unitCode `TNE`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **83200** (currencyID `XUF`)  
  The seller's price per unit.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-04-01**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-06-30**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **RR-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
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
- `Item/Description` = **Zhaldrek skalsir razkir mir huntaz drunvir, tidrek krirstul 0.94, trek sazdran nihan skul 1 zhurkaz.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries.
- `Item/Name` = **Ranstan PE skalsir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `Item/Name` = **Recycled PE granulate** (languageID `en-XU`)  
  The item's name in English, the working language between the countries.
- `Item/SellersItemIdentification/ID` = **RR-PE-R1**  
  The seller's own item number; as Rinova Recovery describes the item.
- `Item/StandardItemIdentification/ID` = **KXU13362PER1** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Rinova Recovery gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Rinova Recovery and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; as Rinova Recovery describes the item.
- `Item/CatalogueItemIdentification/ID` = **26-0002-1**  
  The item's place in the catalogue: the catalogue number and the line.
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Rinova Recovery describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **390110** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Rinova Recovery describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 390110 = Polyethylene having a specific gravity of less than 0.94, in primary forms.
- `Item/CommodityClassification/ItemClassificationCode` = **34710** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Rinova Recovery describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 34710 = Polymers of ethylene, in primary forms.
- `Item/AdditionalItemProperty/Name` = **Density**  
  A measured property of the item.
- `Item/AdditionalItemProperty/ValueQuantity` = **0.92** (unitCode `23`)  
  Its measured value; as Rinova Recovery describes the item.
- `Item/EnvironmentalCertificate/ID` = **CVC-RC-26-0118**  
  The number of the environmental certificate, unique only with its issuer, who is named with it.
- `Item/EnvironmentalCertificate/CertificateTypeCode` = **RECYCLED** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  The kind of claim, as a code. The code is from the Trade Accord's certificate type list: RECYCLED = Recycled content.
- `Item/EnvironmentalCertificate/CertificateType` = **Recycled content**  
  The name of code RECYCLED in the Trade Accord's certificate type list.
- `Item/EnvironmentalCertificate/Remarks` = **100 % recycled content: polyethylene recovered from sorted production waste. The plant's traceability and recycled content audited under the Lumeport Trade Accord's rules for tracing recycled content; the certificate is the Accord's recycled-content certificate.**  
  What the certificate states.
- `Item/EnvironmentalCertificate/IssuerParty/PartyIdentification/ID` = **XU-R-106329** (schemeID `urn:ubl-examples:world:XU:register`)  
  An accredited certification body in Ferrano (a private company): it audits recycling plants for the traceability and the recycled content of what they make, under the Lumeport Trade Accord's rules for tracing recycled content, and issues the Accord's recycled-content certificates to the plants that meet them; it audits Rinova Recovery's plant every year. Referenced only, as the issuer of Rinova's certificate. Its identifier and name are enough (referenced).
- `Item/EnvironmentalCertificate/IssuerParty/PartyName/Name` = **Certovira Certification**  
  An accredited certification body in Ferrano (a private company): it audits recycling plants for the traceability and the recycled content of what they make, under the Lumeport Trade Accord's rules for tracing recycled content, and issues the Accord's recycled-content certificates to the plants that meet them; it audits Rinova Recovery's plant every year. Referenced only, as the issuer of Rinova's certificate. Its identifier and name are enough (referenced).
- `Item/CircularityProfile/CircularityTypeCode` = **RECYCLED** (listID `urn:ubl-examples:world:codelist:CircularityTypeCode`)  
  The circular strategy behind the item. The code is from the Trade Accord's circularity type list: RECYCLED = Recycled material.
- `Item/CircularityProfile/RecycledContentPercent` = **100**  
  The share of recycled material: all of it, polyethylene recovered from production waste, as the certificate states.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Catalogue xmlns="urn:oasis:names:specification:ubl:schema:xsd:Catalogue-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:catalogue:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:catalogue:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0373</cbc:ProfileExecutionID>
  <cbc:ID>26-0002</cbc:ID>
  <cbc:UUID>c8939b73-1616-5856-9d43-118e4ddb2b7e</cbc:UUID>
  <cbc:Name>Recycled PE granulate, second quarter 2026</cbc:Name>
  <cbc:IssueDate>2026-04-01</cbc:IssueDate>
  <cbc:IssueTime>15:16:00-01:00</cbc:IssueTime>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-01</cbc:StartDate>
    <cbc:EndDate>2026-06-30</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ProviderParty>
    <cbc:WebsiteURI>https://www.rinova.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3830</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:13362</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202983340277</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:CompanyID>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
      <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
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
      <cbc:Name>Sales office</cbc:Name>
      <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 697 6856</cbc:Telephone>
      <cbc:ElectronicMail>sales@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ProviderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:15128</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rivermouth Packaging</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-411619</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Estuary Road</cbc:StreetName>
      <cbc:BuildingNumber>28</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38505</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Buyer</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 2 38 7320 9007</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@rivermouth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:CatalogueLine>
    <cbc:ID>1</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">5</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="TNE">1</cbc:MinimumQuantity>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">83200</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-04-01</cbc:StartDate>
          <cbc:EndDate>2026-06-30</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>RR-PRL-2026</cbc:ID>
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
      <cbc:Description languageID="qau">Zhaldrek skalsir razkir mir huntaz drunvir, tidrek krirstul 0.94, trek sazdran nihan skul 1 zhurkaz.</cbc:Description>
      <cbc:Description languageID="en-XU">Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.</cbc:Description>
      <cbc:Name languageID="qau">Ranstan PE skalsir</cbc:Name>
      <cbc:Name languageID="en-XU">Recycled PE granulate</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>RR-PE-R1</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU13362PER1</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>26-0002-1</cbc:ID>
      </cac:CatalogueItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">390110</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">34710</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Density</cbc:Name>
        <cbc:ValueQuantity unitCode="23">0.92</cbc:ValueQuantity>
      </cac:AdditionalItemProperty>
      <cac:EnvironmentalCertificate>
        <cbc:ID>CVC-RC-26-0118</cbc:ID>
        <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">RECYCLED</cbc:CertificateTypeCode>
        <cbc:CertificateType>Recycled content</cbc:CertificateType>
        <cbc:Remarks>100 % recycled content: polyethylene recovered from sorted production waste. The plant's traceability and recycled content audited under the Lumeport Trade Accord's rules for tracing recycled content; the certificate is the Accord's recycled-content certificate.</cbc:Remarks>
        <cac:IssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106329</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Certovira Certification</cbc:Name>
          </cac:PartyName>
        </cac:IssuerParty>
      </cac:EnvironmentalCertificate>
      <cac:CircularityProfile>
        <cbc:CircularityTypeCode listID="urn:ubl-examples:world:codelist:CircularityTypeCode">RECYCLED</cbc:CircularityTypeCode>
        <cbc:RecycledContentPercent>100</cbc:RecycledContentPercent>
      </cac:CircularityProfile>
    </cac:Item>
  </cac:CatalogueLine>
</Catalogue>
```
