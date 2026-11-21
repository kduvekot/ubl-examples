# Catalogue: Lumeway Distribution to Velumi Trading

*Example 2 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Catalogue in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CATALOGUE-SCHEMA)*

The export catalogue for the island customer.

[The XML file](02-Catalogue.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:catalogue:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Catalogue". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:catalogue:1.0**  
  The Trade Accord's process profile the document belongs to: catalogue, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **LMW-TX-26-0955**  
  The collaboration this document belongs to: Lumeway's export catalogue for Velumi Trading. Lumeway Distribution started it and gave it this identifier: the document is the whole exchange.
- `ID` = **LMW-CAT-26-0006**  
  The provider's catalogue number.
- `UUID` = **40262193-531c-5797-8c01-d23252c67188**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `Name` = **Lumeway Distribution catalogue**  
  The catalogue's title.
- `IssueDate` = **2026-05-05**  
  The export catalogue for the island customer, sent on Tuesday 5 May, after Bayvarra's Labour Day.
- `IssueTime` = **09:17:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-05-05**  
  The prices apply from the issue date.
- `EndDate` = **2026-11-01**  
  Until the next catalogue.

### Provider Party

Inside `ProviderParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website; as Lumeway Distribution gives it.
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; as Lumeway Distribution gives it. The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; as Lumeway Distribution gives it.
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)** (languageID `en-XB`)  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 5121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **sales@lumeway.example**  
  The contact's e-mail address; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Purchasing**  
  The party's main desk, which handles this document; as Velumi Trading gives it.
- `Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Contact/Telephone` = **+999 3 729 5794**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `Contact/ElectronicMail` = **purchasing@velumi.example**  
  The contact's e-mail address; as Velumi Trading gives it.
- `Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Velumi Trading gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.

### Catalogue Line

Inside `CatalogueLine`:

- `ID` = **1**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **3** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **4** (unitCode `EA`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/MaximumQuantity` = **288** (unitCode `EA`)  
  The most one order can take from stock: two full 40-foot containers.
- `RequiredItemLocationQuantity/TradingRestrictions` = **Not sold to consumers.**  
  The bench is sold through retailers.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **520** (currencyID `XBL`)  
  The seller's price per unit.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-05-05**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-11-01**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **LMW-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/PriceAmount` = **208** (currencyID `XLC`)  
  The same price in the buyer's currency, at the world's reference rate on the catalogue's issue day; for information only.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/BaseQuantity` = **1** (unitCode `EA`)  
  Per one unit.
- `RequiredItemLocationQuantity/DeliveryUnit/BatchQuantity` = **4** (unitCode `EA`)  
  The benches are delivered per pallet of four.
- `RequiredItemLocationQuantity/DeliveryUnit/ConsumerUnitQuantity` = **1** (unitCode `EA`)  
  One bench is one consumer unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/Package/ID` = **PAL-4**  
  The pallet the price is for.
- `RequiredItemLocationQuantity/Package/Quantity` = **4** (unitCode `EA`)  
  Four benches to a pallet.
- `RequiredItemLocationQuantity/Package/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/StartDate` = **2026-05-12**  
  The first deliveries from the season's stock.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/EndDate` = **2026-11-01**  
  The last.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **3** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **144** (unitCode `EA`)  
  A full 40-foot container: 36 pallets of four benches in two layers; a smaller order does not qualify.
- `RequiredItemLocationQuantity/TradingRestrictions` = **Not sold to consumers.**  
  The bench is sold through retailers.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **520** (currencyID `XBL`)  
  The seller's price per unit.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-05-05**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-11-01**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **LMW-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/PriceAmount` = **208** (currencyID `XLC`)  
  The same price in the buyer's currency, at the world's reference rate on the catalogue's issue day; for information only.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/BaseQuantity` = **1** (unitCode `EA`)  
  Per one unit.
- `RequiredItemLocationQuantity/DeliveryUnit/BatchQuantity` = **4** (unitCode `EA`)  
  The benches are delivered per pallet of four.
- `RequiredItemLocationQuantity/DeliveryUnit/ConsumerUnitQuantity` = **1** (unitCode `EA`)  
  One bench is one consumer unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/Package/ID` = **PAL-4**  
  The pallet the price is for.
- `RequiredItemLocationQuantity/Package/Quantity` = **4** (unitCode `EA`)  
  Four benches to a pallet.
- `RequiredItemLocationQuantity/Package/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `RequiredItemLocationQuantity/AllowanceCharge/ChargeIndicator` = **false**  
  A discount.
- `RequiredItemLocationQuantity/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189: a discount for the full container. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `RequiredItemLocationQuantity/AllowanceCharge/AllowanceChargeReason` = **Full container**  
  The discount for a full container.
- `RequiredItemLocationQuantity/AllowanceCharge/MultiplierFactorNumeric` = **0.03**  
  Three percent off.
- `RequiredItemLocationQuantity/AllowanceCharge/Amount` = **15.60** (currencyID `XBL`)  
  The discount per bench.
- `RequiredItemLocationQuantity/AllowanceCharge/BaseAmount` = **520.00** (currencyID `XBL`)  
  The catalogue price the discount is taken from.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/StartDate` = **2026-05-12**  
  The first deliveries from the season's stock.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/EndDate` = **2026-11-01**  
  The last.
- `Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description.
- `Item/Name` = **Park bench Serra 180**  
  The item's short name.
- `Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item.
- `Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; as Valdara Industries describes the item. A second Keyword would have to be in another language.
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; as Valdara Industries describes the item.
- `Item/ModelName` = **Serra 180**  
  The model; as Valdara Industries describes the item.
- `Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty.
- `Item/SellersItemIdentification/ID` = **LMW-10442**  
  The seller's own item number; as Lumeway Distribution describes the item.
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
- `Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller sells the maker's item on.
- `Item/StandardItemIdentification/ID` = **9520610000012** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none.
- `Item/StandardItemIdentification/IssuerParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Item/StandardItemIdentification/IssuerParty/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Item/CatalogueItemIdentification/ID` = **LMW-CAT-26-0006-1**  
  The item's place in the catalogue: the catalogue number and the line.
- `Item/AdditionalItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The maker's number for the item in its globally unique form under ISO/IEC 15459 (KXU and the company number Codana gave Valdara Industries), which travels along with the GTIN, as an importer may carry it; as Valdara Industries describes the item.
- `Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Item/TransactionConditions/ID` = **LMW-TC-01**  
  The seller's number for these conditions of sale.
- `Item/TransactionConditions/Description` = **Sold to trade customers only, per pallet of four benches.**  
  The conditions in words.
- `Item/TransactionConditions/DocumentReference/ID` = **LMW-GTC-2026**  
  The seller's general terms of trade.
- `Item/TransactionConditions/DocumentReference/DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to: Lumeway's general terms of trade. The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Ductile cast iron EN-GJS-400-15, hot-dip galvanised and powder-coated**  
  Its value; as Valdara Industries describes the item.
- `Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Thermally modified ash**  
  Its value; as Valdara Industries describes the item.
- `Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **3**  
  Its value; as Valdara Industries describes the item.
- `Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colour of the frame, one of the colours it is offered in.
- `Item/AdditionalItemProperty/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; as Valdara Industries describes the item). One ListValue only: a second one may stand only in another language.
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
  Its measured value; as Valdara Industries describes the item.
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
- `Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyName/Name` = **Valdara Industries**  
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
- `Item/EnvironmentalEmission/ValueMeasure` = **25** (unitCode `KGM`)  
  The emission of one item in this stage of its life: a figure from the maker's footprint study, not an activity times a factor, so no factor and base.
- `Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Item/EnvironmentalEmission/LifecycleStageCode` = **SOURCING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The stage of the bench's life the figure covers: the footprint is stated stage by stage. The code is from the Trade Accord's life cycle stage list: SOURCING = Sourcing.
- `Item/EnvironmentalEmission/LifecycleStageDescription` = **Raw material supply and its transport, EN 15804 modules A1 and A2: the ore from the mine for the 65 % of the iron made from ore, the steel and iron scrap for the other 35 %, the slats, the stainless bolts, the zinc, the iron's alloys, the powder coat and the packaging, and their transport to Ferrano.**  
  That stage in words, with the modules of EN 15804 it covers.
- `Item/EnvironmentalEmission/Description` = **The fossil greenhouse gases of the materials one bench uses, before they reach Valdara's works; the scrap carries none of the burden of its first life (cut-off, EN 15804), only its collection, sorting and haulage. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).**  
  What the figure includes, and what it leaves out.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc; the scrap counted with the burden of its collection, sorting and haulage only (cut-off, EN 15804)**  
  Where the factors come from.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Item/EnvironmentalEmission/ValueMeasure` = **33** (unitCode `KGM`)  
  The emission of one item in this stage of its life: a figure from the maker's footprint study, not an activity times a factor, so no factor and base.
- `Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Item/EnvironmentalEmission/LifecycleStageCode` = **MANUFACTURING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The stage of the bench's life the figure covers: the footprint is stated stage by stage. The code is from the Trade Accord's life cycle stage list: MANUFACTURING = Manufacturing.
- `Item/EnvironmentalEmission/LifecycleStageDescription` = **Making the bench, EN 15804 module A3: iron from the Serravona ore in Valdara's blast furnace for 65 % of the frames' iron, melting it with 35 % steel and iron scrap in the induction furnace, casting in its foundry, galvanising, powder coating and packing.**  
  That stage in words, with the modules of EN 15804 it covers.
- `Item/EnvironmentalEmission/Description` = **The fossil greenhouse gases of making one bench in Valdara's works in Ferrano, most of them from the blast furnace's iron; the 35 % of scrap needs no blast furnace, only melting; the pallet is left out as transport packaging that goes back. With the sourcing figure, 58 kg CO2 equivalent from the mine to the factory gate. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).**  
  What the figure includes, and what it leaves out.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc; the scrap counted with the burden of its collection, sorting and haulage only (cut-off, EN 15804)**  
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
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **14.0** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Ore-based ductile iron, 65 % of the frames' iron: blast-furnace iron from Serravona ore in Urvania, as poured for the two side frames less the gates remelted**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **IRON** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: IRON = Iron.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **7.6** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Recycled ductile iron, 35 % of the frames' iron: steel and iron scrap melted in Valdara's induction furnace, as poured for the two side frames less the gates remelted**  
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
- `ID` = **2**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **2** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **1** (unitCode `EA`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **68** (currencyID `XBL`)  
  Lumeway's price for the island, CIF Selanu, as its export catalogue gives it: the trade price with the frame's share of the container haulage, sea freight, export clearance and insurance in it, which leaves Lumeway a distributor's margin of about 16 % (decided by the owner on 2026-11-19; 68.00 instead of 67.00 once the haulage to the port is in the freight). It holds for goods shipped CIF; the urgent frames by air are sold at the trade price, carriage paid, with the air freight recharged.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-05-05**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-11-01**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **LMW-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/PriceAmount` = **27.2** (currencyID `XLC`)  
  The same price in the buyer's currency, at the world's reference rate on the catalogue's issue day; for information only.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/BaseQuantity` = **1** (unitCode `EA`)  
  Per one unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description.
- `Item/Name` = **Bench side frame casting**  
  The item's short name.
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; as Valdara Industries describes the item.
- `Item/ModelName` = **Serra 180 side frame**  
  The model; as Valdara Industries describes the item.
- `Item/SellersItemIdentification/ID` = **LMW-10443**  
  The seller's own item number; as Lumeway Distribution describes the item.
- `Item/ManufacturersItemIdentification/ID` = **VI-C180**  
  The item number of the maker, Valdara Industries: the reseller sells the maker's item on.
- `Item/ManufacturersItemIdentification/ExtendedID` = **2026**  
  The 2026 casting with the reinforced foot, which replaced the 2025 casting from the order response of the road delivery on: Valdara tells the versions of the same part number apart by the casting year, and every frame made since carries it. As Valdara Industries describes the item.
- `Item/StandardItemIdentification/ID` = **9520610000029** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none.
- `Item/StandardItemIdentification/IssuerParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Item/StandardItemIdentification/IssuerParty/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Item/CatalogueItemIdentification/ID` = **LMW-CAT-26-0006-2**  
  The item's place in the catalogue: the catalogue number and the line.
- `Item/AdditionalItemIdentification/ID` = **KXU10014C180** (schemeID `ISO 15459-6`)  
  The maker's number for the item in its globally unique form under ISO/IEC 15459 (KXU and the company number Codana gave Valdara Industries), which travels along with the GTIN, as an importer may carry it; as Valdara Industries describes the item.
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **940199** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940199 = Parts of seats, other.
- `Item/CommodityClassification/ItemClassificationCode` = **38160** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38160 = Parts of furniture.
- `Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Catalogue xmlns="urn:oasis:names:specification:ubl:schema:xsd:Catalogue-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:catalogue:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:catalogue:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LMW-TX-26-0955</cbc:ProfileExecutionID>
  <cbc:ID>LMW-CAT-26-0006</cbc:ID>
  <cbc:UUID>40262193-531c-5797-8c01-d23252c67188</cbc:UUID>
  <cbc:Name>Lumeway Distribution catalogue</cbc:Name>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>09:17:00-01:00</cbc:IssueTime>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-05-05</cbc:StartDate>
    <cbc:EndDate>2026-11-01</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ProviderParty>
    <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
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
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:CompanyID>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="en-XB">Limited company (private)</cbc:CompanyLegalForm>
      <cac:RegistrationAddress>
        <cbc:CityName>Marrowdale</cbc:CityName>
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
      <cbc:Name>Sales office</cbc:Name>
      <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 5121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>sales@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ProviderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>16</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Buyer</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
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
  <cac:CatalogueLine>
    <cbc:ID>1</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">4</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">288</cbc:MaximumQuantity>
      <cbc:TradingRestrictions>Not sold to consumers.</cbc:TradingRestrictions>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">520</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-05-05</cbc:StartDate>
          <cbc:EndDate>2026-11-01</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>LMW-PRL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
        <cac:AlternativeCurrencyPrice>
          <cbc:PriceAmount currencyID="XLC">208</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        </cac:AlternativeCurrencyPrice>
      </cac:Price>
      <cac:DeliveryUnit>
        <cbc:BatchQuantity unitCode="EA">4</cbc:BatchQuantity>
        <cbc:ConsumerUnitQuantity unitCode="EA">1</cbc:ConsumerUnitQuantity>
      </cac:DeliveryUnit>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
      <cac:Package>
        <cbc:ID>PAL-4</cbc:ID>
        <cbc:Quantity unitCode="EA">4</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
      </cac:Package>
      <cac:ApplicableDeliveryPeriod>
        <cbc:StartDate>2026-05-12</cbc:StartDate>
        <cbc:EndDate>2026-11-01</cbc:EndDate>
      </cac:ApplicableDeliveryPeriod>
    </cac:RequiredItemLocationQuantity>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">144</cbc:MinimumQuantity>
      <cbc:TradingRestrictions>Not sold to consumers.</cbc:TradingRestrictions>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">520</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-05-05</cbc:StartDate>
          <cbc:EndDate>2026-11-01</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>LMW-PRL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
        <cac:AlternativeCurrencyPrice>
          <cbc:PriceAmount currencyID="XLC">208</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        </cac:AlternativeCurrencyPrice>
      </cac:Price>
      <cac:DeliveryUnit>
        <cbc:BatchQuantity unitCode="EA">4</cbc:BatchQuantity>
        <cbc:ConsumerUnitQuantity unitCode="EA">1</cbc:ConsumerUnitQuantity>
      </cac:DeliveryUnit>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
      <cac:Package>
        <cbc:ID>PAL-4</cbc:ID>
        <cbc:Quantity unitCode="EA">4</cbc:Quantity>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
      </cac:Package>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Full container</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.03</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="XBL">15.60</cbc:Amount>
        <cbc:BaseAmount currencyID="XBL">520.00</cbc:BaseAmount>
      </cac:AllowanceCharge>
      <cac:ApplicableDeliveryPeriod>
        <cbc:StartDate>2026-05-12</cbc:StartDate>
        <cbc:EndDate>2026-11-01</cbc:EndDate>
      </cac:ApplicableDeliveryPeriod>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
      <cbc:Keyword>park bench, street furniture</cbc:Keyword>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180</cbc:ModelName>
      <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:SellersItemIdentification>
        <cbc:ID>LMW-10442</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9520610000012</cbc:ID>
        <cac:IssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Lumeway Distribution</cbc:Name>
          </cac:PartyName>
        </cac:IssuerParty>
      </cac:StandardItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>LMW-CAT-26-0006-1</cbc:ID>
      </cac:CatalogueItemIdentification>
      <cac:AdditionalItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
      </cac:AdditionalItemIdentification>
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
      <cac:TransactionConditions>
        <cbc:ID>LMW-TC-01</cbc:ID>
        <cbc:Description>Sold to trade customers only, per pallet of four benches.</cbc:Description>
        <cac:DocumentReference>
          <cbc:ID>LMW-GTC-2026</cbc:ID>
          <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
        </cac:DocumentReference>
      </cac:TransactionConditions>
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
      <cac:ManufacturerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:ManufacturerParty>
      <cac:InformationContentProviderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:InformationContentProviderParty>
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
        <cbc:ValueMeasure unitCode="KGM">25</cbc:ValueMeasure>
        <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
        <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">SOURCING</cbc:LifecycleStageCode>
        <cbc:LifecycleStageDescription>Raw material supply and its transport, EN 15804 modules A1 and A2: the ore from the mine for the 65 % of the iron made from ore, the steel and iron scrap for the other 35 %, the slats, the stainless bolts, the zinc, the iron's alloys, the powder coat and the packaging, and their transport to Ferrano.</cbc:LifecycleStageDescription>
        <cbc:Description>The fossil greenhouse gases of the materials one bench uses, before they reach Valdara's works; the scrap carries none of the burden of its first life (cut-off, EN 15804), only its collection, sorting and haulage. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:EmissionFactorSource>Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc; the scrap counted with the burden of its collection, sorting and haulage only (cut-off, EN 15804)</cbc:EmissionFactorSource>
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
        <cbc:ValueMeasure unitCode="KGM">33</cbc:ValueMeasure>
        <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
        <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">MANUFACTURING</cbc:LifecycleStageCode>
        <cbc:LifecycleStageDescription>Making the bench, EN 15804 module A3: iron from the Serravona ore in Valdara's blast furnace for 65 % of the frames' iron, melting it with 35 % steel and iron scrap in the induction furnace, casting in its foundry, galvanising, powder coating and packing.</cbc:LifecycleStageDescription>
        <cbc:Description>The fossil greenhouse gases of making one bench in Valdara's works in Ferrano, most of them from the blast furnace's iron; the 35 % of scrap needs no blast furnace, only melting; the pallet is left out as transport packaging that goes back. With the sourcing figure, 58 kg CO2 equivalent from the mine to the factory gate. The carbon stored in the slats, about 40 kg CO2 a bench, is not included: product declarations state biogenic carbon apart from the fossil figure (EN 15804+A2, the Greenhouse Gas Protocol).</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:EmissionFactorSource>Valdara's measured energy use of 2025 in its blast furnace, foundry and coating lines, and its suppliers' figures for the slats, the bolts and the zinc; the scrap counted with the burden of its collection, sorting and haulage only (cut-off, EN 15804)</cbc:EmissionFactorSource>
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
          <cbc:ConsumptionMeasure unitCode="KGM">14.0</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Ore-based ductile iron, 65 % of the frames' iron: blast-furnace iron from Serravona ore in Urvania, as poured for the two side frames less the gates remelted</cbc:ResourceOriginDescription>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:ResourceConsumption>
        <cac:ResourceConsumption>
          <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">IRON</cbc:ResourceTypeCode>
          <cbc:ConsumptionMeasure unitCode="KGM">7.6</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Recycled ductile iron, 35 % of the frames' iron: steel and iron scrap melted in Valdara's induction furnace, as poured for the two side frames less the gates remelted</cbc:ResourceOriginDescription>
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
  </cac:CatalogueLine>
  <cac:CatalogueLine>
    <cbc:ID>2</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">2</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">1</cbc:MinimumQuantity>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">68</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-05-05</cbc:StartDate>
          <cbc:EndDate>2026-11-01</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>LMW-PRL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
        <cac:AlternativeCurrencyPrice>
          <cbc:PriceAmount currencyID="XLC">27.2</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        </cac:AlternativeCurrencyPrice>
      </cac:Price>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
      <cbc:Name>Bench side frame casting</cbc:Name>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180 side frame</cbc:ModelName>
      <cac:SellersItemIdentification>
        <cbc:ID>LMW-10443</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-C180</cbc:ID>
        <cbc:ExtendedID>2026</cbc:ExtendedID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="GS1 GTIN">9520610000029</cbc:ID>
        <cac:IssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Lumeway Distribution</cbc:Name>
          </cac:PartyName>
        </cac:IssuerParty>
      </cac:StandardItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>LMW-CAT-26-0006-2</cbc:ID>
      </cac:CatalogueItemIdentification>
      <cac:AdditionalItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014C180</cbc:ID>
      </cac:AdditionalItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">940199</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38160</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ManufacturerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:ManufacturerParty>
      <cac:InformationContentProviderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:InformationContentProviderParty>
    </cac:Item>
  </cac:CatalogueLine>
</Catalogue>
```
