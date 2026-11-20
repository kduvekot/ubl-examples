# Catalogue: Lumeway Distribution to Brightmarket Stores

*Example 2 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Catalogue in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CATALOGUE-SCHEMA)*

The distributor's catalogue of items and prices; each item carries the GTIN the distributor gives it, with the distributor named as the GTIN's issuer.

[The XML file](02-Catalogue.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Catalogue/ApplicableTerritoryAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:catalogue:1.0#compliant#urn:ubl-examples:world:community:retail:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Catalogue"; the community specification "Retail community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:catalogue:1.0**  
  The Trade Accord's process profile the document belongs to: catalogue, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900338989**  
  The collaboration this document belongs to: the store's request for Lumeway's catalogue and the catalogue's updates. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **LMW-CAT-26-0005**  
  The provider's catalogue number.
- `UUID` = **f5163e36-0159-5b9f-b172-a86137e369e6**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ActionCode` = **NEW** (listID `urn:ubl-examples:world:codelist:CatalogueActionCode`)  
  A new catalogue, issued for the store on its request. The code is from the Trade Accord's catalogue action list: NEW = New catalogue.
- `Name` = **Lumeway's catalogue for the Lumeport store, 2026**  
  Its name: for the range of the store's reopened home and garden department.
- `IssueDate` = **2026-04-20**  
  Lumeway's catalogue for the store's reopened department.
- `IssueTime` = **09:00:00-01:00**  
  Issued in the morning, for the store to set up the range; in the issuer's local time, with its offset from UTC.
- `RevisionDate` = **2026-04-20**  
  Not revised yet: the issue date.
- `RevisionTime` = **09:00:00-01:00**  
  The issue time; in the local time of Bayvarra, where it happens, with its offset from UTC.
- `Note` = **Prices for trade customers, before sales tax.**  
  What the prices are.
- `Description` = **Benches and spare parts for resale.**  
  What the catalogue holds.
- `VersionID` = **1.0**  
  The first version: a new catalogue for the store, with no version before it.
- `LineCountNumeric` = **2**  
  Two lines.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-20**  
  The prices apply from the issue date.
- `EndDate` = **2026-07-19**  
  Until the next catalogue.

### Referenced Contract

Inside `ReferencedContract`:

- `ID` = **LMW-BM-SUPPLY-2026**  
  The supply agreement with the store.
- `ContractType` = **Supply agreement**  
  Its kind.

### Source Catalogue Reference

Inside `SourceCatalogueReference`:

- `ID` = **VI-CAT-2026**  
  The maker's catalogue the lines come from.

### Document Reference

Inside `DocumentReference`:

- `ID` = **LMW-GTC-2026**  
  The general terms of trade.
- `DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, Lumeway's general terms of trade, a document outside the examples (cited). The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `ID` = **6200003390**  
  The store's request this catalogue answers.
- `DocumentTypeCode` = **CatalogueRequest** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 6200003390 is the example retail/01, a CatalogueRequest; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: CatalogueRequest = Catalogue Request.

### Applicable Territory Address

Inside `ApplicableTerritoryAddress`:

- `Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Sold in Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-0420**  
  The distributor's seal.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Provider Party

Inside `ProviderParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); as Lumeway Distribution gives it.
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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **sales@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brightmarket Stores gives it.
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; as Brightmarket Stores gives it.
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; as Brightmarket Stores gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Brightmarket Stores gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. As Brightmarket Stores gives it.
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. As Brightmarket Stores gives it.
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Brightmarket Stores gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Brightmarket Stores gives it.
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). As Brightmarket Stores gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Brightmarket Stores gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
- `Contact/Name` = **Buying office**  
  The party's main desk, which handles this document; as Brightmarket Stores gives it.
- `Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Brightmarket Stores gives it.
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Brightmarket Stores gives it.
- `Contact/Telephone` = **+999 2 38 4609 7100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Brightmarket Stores gives it.
- `Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Brightmarket Stores gives it.
- `Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Brightmarket Stores gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.

### Contractor Customer Party

Inside `ContractorCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Trading Terms

Inside `TradingTerms`:

- `Information` = **Delivered duty paid to the store; 30 days net.**  
  The terms.
- `Reference` = **LMW-GTC-2026**  
  Where they are.
- `ApplicableAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  In Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Catalogue Line

Inside `CatalogueLine`:

- `ID` = **1**  
  The line number.
- `ActionCode` = **ADD** (listID `urn:ubl-examples:world:codelist:CatalogueLineActionCode`)  
  The line is new in this catalogue. The code is from the Trade Accord's catalogue line action list: ADD = Add.
- `LifeCycleStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:ItemLifeCycleStatusCode`)  
  The item is sold now. The code is from the Trade Accord's item life cycle status list: ACTIVE = Active.
- `ContractSubdivision` = **Garden**  
  The part of the supply agreement the line falls under.
- `Note` = **Pallets of four only.**  
  How it is sold.
- `OrderableIndicator` = **true**  
  It can be ordered.
- `OrderableUnit` = **Pallet of 4**  
  The unit the store orders in.
- `ContentUnitQuantity` = **4** (unitCode `EA`)  
  Four benches in an orderable unit.
- `OrderQuantityIncrementNumeric` = **4**  
  Orders go up in steps of four.
- `MinimumOrderQuantity` = **4** (unitCode `EA`)  
  One pallet.
- `MaximumOrderQuantity` = **192** (unitCode `EA`)  
  Two containers.
- `WarrantyInformation` = **Five years on the frame, from the maker.**  
  The warranty.
- `PackLevelCode` = **PALLET** (listID `urn:ubl-examples:world:codelist:PackLevelCode`)  
  The pack level the line is for. The code is from the Trade Accord's pack level list: PALLET = Pallet.
- `WarrantyParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `WarrantyParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `WarrantyValidityPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `LineValidityPeriod/StartDate` = **2026-04-20**  
  From the issue.
- `LineValidityPeriod/EndDate` = **2026-07-19**  
  With the catalogue.
- `ComponentRelatedItem/ID` = **MDS-SL-1800**  
  The related item: Bench slat 1800, thermally modified ash.
- `ComponentRelatedItem/Quantity` = **5** (unitCode `EA`)  
  Five slats per bench.
- `ComponentRelatedItem/Description` = **Bench slat 1800, thermally modified ash**  
  In words.
- `ComponentRelatedItem/ID` = **VI-C180**  
  The related item: Bench side frame casting.
- `ComponentRelatedItem/Quantity` = **2** (unitCode `EA`)  
  Two side frames per bench.
- `ComponentRelatedItem/Description` = **Bench side frame casting**  
  In words.
- `AccessoryRelatedItem/ID` = **VI-ANCHOR-4**  
  The ground anchor set.
- `AccessoryRelatedItem/Quantity` = **1** (unitCode `SET`)  
  Supplied with each bench.
- `AccessoryRelatedItem/Description` = **Four ground anchors and bolts.**  
  In words.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **3** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **4** (unitCode `EA`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/MaximumQuantity` = **288** (unitCode `EA`)  
  The most one order can take from stock: two full 40-foot containers.
- `RequiredItemLocationQuantity/TradingRestrictions` = **Not sold to consumers.**  
  The bench is sold through retailers.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **520** (currencyID `XBL`)  
  The seller's price per unit.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-04-20**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-07-19**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **LMW-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/DeliveryUnit/BatchQuantity` = **4** (unitCode `EA`)  
  The benches are delivered per pallet of four.
- `RequiredItemLocationQuantity/DeliveryUnit/ConsumerUnitQuantity` = **1** (unitCode `EA`)  
  One bench is one consumer unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a business that resells or processes the goods is exempt from the state sales tax, which is charged only on the sale to the final consumer (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **RESALE** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: RESALE = Sale for resale or manufacture.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Sale for resale or manufacture**  
  The name of code RESALE in Bayvarra's national sales tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/Package/ID` = **PAL-4**  
  The pallet the price is for.
- `RequiredItemLocationQuantity/Package/Quantity` = **4** (unitCode `EA`)  
  Four benches to a pallet.
- `RequiredItemLocationQuantity/Package/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/StartDate` = **2026-04-27**  
  The first deliveries from the season's stock.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/EndDate` = **2026-07-19**  
  The last.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **3** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **144** (unitCode `EA`)  
  A full 40-foot container: 36 pallets of four benches in two layers; a smaller order does not qualify.
- `RequiredItemLocationQuantity/TradingRestrictions` = **Not sold to consumers.**  
  The bench is sold through retailers.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **520** (currencyID `XBL`)  
  The seller's price per unit.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-04-20**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-07-19**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **LMW-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/DeliveryUnit/BatchQuantity` = **4** (unitCode `EA`)  
  The benches are delivered per pallet of four.
- `RequiredItemLocationQuantity/DeliveryUnit/ConsumerUnitQuantity` = **1** (unitCode `EA`)  
  One bench is one consumer unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a business that resells or processes the goods is exempt from the state sales tax, which is charged only on the sale to the final consumer (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **RESALE** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: RESALE = Sale for resale or manufacture.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Sale for resale or manufacture**  
  The name of code RESALE in Bayvarra's national sales tax exemption reason list.
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
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/StartDate` = **2026-04-27**  
  The first deliveries from the season's stock.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/EndDate` = **2026-07-19**  
  The last.
- `DocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet.
- `DocumentReference/DocumentType` = **Product data sheet**  
  The kind of document referred to, Valdara's data sheet of the Serra bench, a document outside the examples, in words: no list has an exact code for it (cited).
- `Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description.
- `Item/Name` = **Park bench Serra 180**  
  The item's short name.
- `Item/ItemTypeCode` = **PRODUCT** (listID `urn:ubl-examples:world:codelist:ItemTypeCode`)  
  A physical product, not a service. The code is from the Trade Accord's item type list: PRODUCT = Product.
- `Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item.
- `Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; as Valdara Industries describes the item. A second Keyword would have to be in another language (UBL rule IND7).
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
- `Item/CatalogueItemIdentification/ID` = **LMW-CAT-26-0005-1**  
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
  The kind of document referred to, Lumeway's general terms of trade, a document outside the examples (cited). The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
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
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; as Valdara Industries describes the item). One ListValue only: UBL rule IND7 allows a second one only in another language.
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
- `KeywordItemProperty/Name` = **Keyword**  
  A search word of the catalogue.
- `KeywordItemProperty/Value` = **park bench**  
  The word.
- `ID` = **2**  
  The line number.
- `ActionCode` = **ADD** (listID `urn:ubl-examples:world:codelist:CatalogueLineActionCode`)  
  The line is new in this catalogue. The code is from the Trade Accord's catalogue line action list: ADD = Add.
- `LifeCycleStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:ItemLifeCycleStatusCode`)  
  The item is sold now. The code is from the Trade Accord's item life cycle status list: ACTIVE = Active.
- `Note` = **Spare part for the Serra 180.**  
  What it is for.
- `OrderableIndicator` = **true**  
  It can be ordered.
- `OrderableUnit` = **Box**  
  One frame per box.
- `MinimumOrderQuantity` = **1** (unitCode `EA`)  
  Any quantity.
- `LineValidityPeriod/StartDate` = **2026-04-20**  
  From the issue.
- `LineValidityPeriod/EndDate` = **2026-07-19**  
  With the catalogue.
- `RequiredRelatedItem/ID` = **LMW-10442**  
  The related item: Park bench Serra 180.
- `RequiredRelatedItem/Quantity` = **1** (unitCode `EA`)  
  Fits only the Serra 180.
- `RequiredRelatedItem/Description` = **Park bench Serra 180**  
  In words.
- `ReplacedRelatedItem/ID` = **VI-C180**  
  The casting this one replaced, the same part number: Valdara tells its versions apart by the year.
- `ReplacedRelatedItem/Quantity` = **1** (unitCode `EA`)  
  One for one.
- `ReplacedRelatedItem/Description` = **Side frame, 2025 casting**  
  Which version: the 2025 casting, which the 2026 casting with the reinforced foot replaced.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **2** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **1** (unitCode `EA`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The market the price is offered for: the buyer's country, whose sales the tax category below treats. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **64** (currencyID `XBL`)  
  The seller's price per unit.
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD** (listID `urn:ubl-examples:world:codelist:PriceTypeCode`)  
  The kind of price, which buyer and seller both understand: a trade price. The code is from the Trade Accord's price type list: TRD = Trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  The name of code TRD in the Trade Accord's price type list.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-04-20**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-07-19**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **LMW-PRL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The first issue of the price list: UBL names original, copy, revision or cancellation here, not whether the list is in force. The code is from the Trade Accord's record status list: ORIGINAL = Original.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a business that resells or processes the goods is exempt from the state sales tax, which is charged only on the sale to the final consumer (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **RESALE** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: RESALE = Sale for resale or manufacture.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Sale for resale or manufacture**  
  The name of code RESALE in Bayvarra's national sales tax exemption reason list.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description.
- `Item/Name` = **Bench side frame casting**  
  The item's short name.
- `Item/ItemTypeCode` = **PRODUCT** (listID `urn:ubl-examples:world:codelist:ItemTypeCode`)  
  A physical product, not a service. The code is from the Trade Accord's item type list: PRODUCT = Product.
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
- `Item/CatalogueItemIdentification/ID` = **LMW-CAT-26-0005-2**  
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
  <cbc:CustomizationID>urn:ubl-examples:world:trns:catalogue:1.0#compliant#urn:ubl-examples:world:community:retail:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:catalogue:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900338989</cbc:ProfileExecutionID>
  <cbc:ID>LMW-CAT-26-0005</cbc:ID>
  <cbc:UUID>f5163e36-0159-5b9f-b172-a86137e369e6</cbc:UUID>
  <cbc:ActionCode listID="urn:ubl-examples:world:codelist:CatalogueActionCode">NEW</cbc:ActionCode>
  <cbc:Name>Lumeway's catalogue for the Lumeport store, 2026</cbc:Name>
  <cbc:IssueDate>2026-04-20</cbc:IssueDate>
  <cbc:IssueTime>09:00:00-01:00</cbc:IssueTime>
  <cbc:RevisionDate>2026-04-20</cbc:RevisionDate>
  <cbc:RevisionTime>09:00:00-01:00</cbc:RevisionTime>
  <cbc:Note>Prices for trade customers, before sales tax.</cbc:Note>
  <cbc:Description>Benches and spare parts for resale.</cbc:Description>
  <cbc:VersionID>1.0</cbc:VersionID>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-20</cbc:StartDate>
    <cbc:EndDate>2026-07-19</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ReferencedContract>
    <cbc:ID>LMW-BM-SUPPLY-2026</cbc:ID>
    <cbc:ContractType>Supply agreement</cbc:ContractType>
  </cac:ReferencedContract>
  <cac:SourceCatalogueReference>
    <cbc:ID>VI-CAT-2026</cbc:ID>
  </cac:SourceCatalogueReference>
  <cac:DocumentReference>
    <cbc:ID>LMW-GTC-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentReference>
    <cbc:ID>6200003390</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">CatalogueRequest</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:ApplicableTerritoryAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
    </cac:Country>
  </cac:ApplicableTerritoryAddress>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-0420</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
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
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
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
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-579130</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:ID>BM-CT-01</cbc:ID>
      <cbc:Name>Buying office</cbc:Name>
      <cbc:JobTitle>Buyer</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
      <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
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
  <cac:TradingTerms>
    <cbc:Information>Delivered duty paid to the store; 30 days net.</cbc:Information>
    <cbc:Reference>LMW-GTC-2026</cbc:Reference>
    <cac:ApplicableAddress>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:ApplicableAddress>
  </cac:TradingTerms>
  <cac:CatalogueLine>
    <cbc:ID>1</cbc:ID>
    <cbc:ActionCode listID="urn:ubl-examples:world:codelist:CatalogueLineActionCode">ADD</cbc:ActionCode>
    <cbc:LifeCycleStatusCode listID="urn:ubl-examples:world:codelist:ItemLifeCycleStatusCode">ACTIVE</cbc:LifeCycleStatusCode>
    <cbc:ContractSubdivision>Garden</cbc:ContractSubdivision>
    <cbc:Note>Pallets of four only.</cbc:Note>
    <cbc:OrderableIndicator>true</cbc:OrderableIndicator>
    <cbc:OrderableUnit>Pallet of 4</cbc:OrderableUnit>
    <cbc:ContentUnitQuantity unitCode="EA">4</cbc:ContentUnitQuantity>
    <cbc:OrderQuantityIncrementNumeric>4</cbc:OrderQuantityIncrementNumeric>
    <cbc:MinimumOrderQuantity unitCode="EA">4</cbc:MinimumOrderQuantity>
    <cbc:MaximumOrderQuantity unitCode="EA">192</cbc:MaximumOrderQuantity>
    <cbc:WarrantyInformation>Five years on the frame, from the maker.</cbc:WarrantyInformation>
    <cbc:PackLevelCode listID="urn:ubl-examples:world:codelist:PackLevelCode">PALLET</cbc:PackLevelCode>
    <cac:WarrantyParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:WarrantyParty>
    <cac:WarrantyValidityPeriod>
      <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
    </cac:WarrantyValidityPeriod>
    <cac:LineValidityPeriod>
      <cbc:StartDate>2026-04-20</cbc:StartDate>
      <cbc:EndDate>2026-07-19</cbc:EndDate>
    </cac:LineValidityPeriod>
    <cac:ComponentRelatedItem>
      <cbc:ID>MDS-SL-1800</cbc:ID>
      <cbc:Quantity unitCode="EA">5</cbc:Quantity>
      <cbc:Description>Bench slat 1800, thermally modified ash</cbc:Description>
    </cac:ComponentRelatedItem>
    <cac:ComponentRelatedItem>
      <cbc:ID>VI-C180</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
      <cbc:Description>Bench side frame casting</cbc:Description>
    </cac:ComponentRelatedItem>
    <cac:AccessoryRelatedItem>
      <cbc:ID>VI-ANCHOR-4</cbc:ID>
      <cbc:Quantity unitCode="SET">1</cbc:Quantity>
      <cbc:Description>Four ground anchors and bolts.</cbc:Description>
    </cac:AccessoryRelatedItem>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">4</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="EA">288</cbc:MaximumQuantity>
      <cbc:TradingRestrictions>Not sold to consumers.</cbc:TradingRestrictions>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">520</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-04-20</cbc:StartDate>
          <cbc:EndDate>2026-07-19</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>LMW-PRL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
      </cac:Price>
      <cac:DeliveryUnit>
        <cbc:BatchQuantity unitCode="EA">4</cbc:BatchQuantity>
        <cbc:ConsumerUnitQuantity unitCode="EA">1</cbc:ConsumerUnitQuantity>
      </cac:DeliveryUnit>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">RESALE</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Sale for resale or manufacture</cbc:TaxExemptionReason>
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
        <cbc:StartDate>2026-04-27</cbc:StartDate>
        <cbc:EndDate>2026-07-19</cbc:EndDate>
      </cac:ApplicableDeliveryPeriod>
    </cac:RequiredItemLocationQuantity>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">144</cbc:MinimumQuantity>
      <cbc:TradingRestrictions>Not sold to consumers.</cbc:TradingRestrictions>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">520</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-04-20</cbc:StartDate>
          <cbc:EndDate>2026-07-19</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>LMW-PRL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
      </cac:Price>
      <cac:DeliveryUnit>
        <cbc:BatchQuantity unitCode="EA">4</cbc:BatchQuantity>
        <cbc:ConsumerUnitQuantity unitCode="EA">1</cbc:ConsumerUnitQuantity>
      </cac:DeliveryUnit>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">RESALE</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Sale for resale or manufacture</cbc:TaxExemptionReason>
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
        <cbc:StartDate>2026-04-27</cbc:StartDate>
        <cbc:EndDate>2026-07-19</cbc:EndDate>
      </cac:ApplicableDeliveryPeriod>
    </cac:RequiredItemLocationQuantity>
    <cac:DocumentReference>
      <cbc:ID>VI-DS-B180</cbc:ID>
      <cbc:DocumentType>Product data sheet</cbc:DocumentType>
    </cac:DocumentReference>
    <cac:Item>
      <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cbc:ItemTypeCode listID="urn:ubl-examples:world:codelist:ItemTypeCode">PRODUCT</cbc:ItemTypeCode>
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
        <cbc:ID>LMW-CAT-26-0005-1</cbc:ID>
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
    <cac:KeywordItemProperty>
      <cbc:Name>Keyword</cbc:Name>
      <cbc:Value>park bench</cbc:Value>
    </cac:KeywordItemProperty>
  </cac:CatalogueLine>
  <cac:CatalogueLine>
    <cbc:ID>2</cbc:ID>
    <cbc:ActionCode listID="urn:ubl-examples:world:codelist:CatalogueLineActionCode">ADD</cbc:ActionCode>
    <cbc:LifeCycleStatusCode listID="urn:ubl-examples:world:codelist:ItemLifeCycleStatusCode">ACTIVE</cbc:LifeCycleStatusCode>
    <cbc:Note>Spare part for the Serra 180.</cbc:Note>
    <cbc:OrderableIndicator>true</cbc:OrderableIndicator>
    <cbc:OrderableUnit>Box</cbc:OrderableUnit>
    <cbc:MinimumOrderQuantity unitCode="EA">1</cbc:MinimumOrderQuantity>
    <cac:LineValidityPeriod>
      <cbc:StartDate>2026-04-20</cbc:StartDate>
      <cbc:EndDate>2026-07-19</cbc:EndDate>
    </cac:LineValidityPeriod>
    <cac:RequiredRelatedItem>
      <cbc:ID>LMW-10442</cbc:ID>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cbc:Description>Park bench Serra 180</cbc:Description>
    </cac:RequiredRelatedItem>
    <cac:ReplacedRelatedItem>
      <cbc:ID>VI-C180</cbc:ID>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cbc:Description>Side frame, 2025 casting</cbc:Description>
    </cac:ReplacedRelatedItem>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">2</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="EA">1</cbc:MinimumQuantity>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">64</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode listID="urn:ubl-examples:world:codelist:PriceTypeCode">TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-04-20</cbc:StartDate>
          <cbc:EndDate>2026-07-19</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>LMW-PRL-2026</cbc:ID>
          <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ORIGINAL</cbc:StatusCode>
        </cac:PriceList>
      </cac:Price>
      <cac:ApplicableTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">RESALE</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Sale for resale or manufacture</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
      <cbc:Name>Bench side frame casting</cbc:Name>
      <cbc:ItemTypeCode listID="urn:ubl-examples:world:codelist:ItemTypeCode">PRODUCT</cbc:ItemTypeCode>
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
        <cbc:ID>LMW-CAT-26-0005-2</cbc:ID>
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
