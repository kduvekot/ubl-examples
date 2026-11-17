# Packing List: Lumeway Distribution to Bayforth Forwarding

*Example 10 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Packing List in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PACKING-LIST-SCHEMA)*

How the goods are packed in the container, for the forwarder's booking and the export declaration.

[The XML file](10-PackingList.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:packing-list:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Packing list"; the community specification "Lumeport port community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-PL-26-0134**  
  The distributor's packing list number.
- `UUID` = **51ffd2ec-220f-52f3-bbda-f00884ed47a2**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-12**  
  Made when the container is packed.
- `IssueTime` = **15:59:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Packing list**  
  What it is.
- `Description` = **The container's contents.**  
  In words.
- `Note` = **25 pallets.**  
  The count.
- `VersionID` = **1**  
  The first version.
- `OtherInstruction` = **Keep with the container's documents.**  
  Where it goes.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
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
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **dispatch@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Export desk**  
  The party's main desk, which handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Export coordinator**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Export**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2144 1644**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **LD-SH-26-0132**  
  The shipment packed.
- `ShippingPriorityLevelCode` = **STANDARD** (listID `urn:ubl-examples:world:codelist:ShippingPriorityCode`)  
  No priority: the next sailing will do. The code is from the Trade Accord's shipping priority list: STANDARD = Standard.
- `HandlingInstructions` = **Castings pallet at the doors.**  
  How the container is stowed.
- `GrossWeightMeasure` = **7856.4** (unitCode `KGM`)  
  The goods (4106.4 kg) and the tare of the transport equipment (3750 kg): a shipment's gross weight includes the equipment (worklist C15).
- `NetWeightMeasure` = **3762** (unitCode `KGM`)  
  The goods without packaging.
- `NetVolumeMeasure` = **38.9** (unitCode `MTQ`)  
  The volume of the goods themselves.
- `TotalTransportHandlingUnitQuantity` = **25** (unitCode `EA`)  
  25 pallets in the container.
- `SpecialInstructions` = **Photograph the load before closing the doors.**  
  For any damage claim.
- `DeliveryInstructions` = **Deliver to the buyer's 3PL, Nalevi Warehousing, Selanu.**  
  Where the goods end up.
- `Consignment/ID` = **LD-CS-26-0133**  
  The consignment.
- `Consignment/GrossWeightMeasure` = **4106.4** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight of the goods.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XB`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 729 1859**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **49920.00** (currencyID `XBL`)  
  The value of the goods, in lume.
- `GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description; item bench-serra-b of Lumeway Distribution (world/items.json).
- `GoodsItem/Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra-b of Lumeway Distribution (world/items.json).
- `GoodsItem/Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; item bench-serra of Valdara Industries (world/items.json). A second Keyword would have to be in another language (UBL rule IND7).
- `GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ID` = **LD-10442**  
  The seller's own item number; item bench-serra-b of Lumeway Distribution (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `GoodsItem/Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-serra.
- `GoodsItem/Item/StandardItemIdentification/ID` = **9520610000012** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none (world/items.json).
- `GoodsItem/Item/AdditionalItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The maker's own number for the item, its Codana item number, which travels along with the GTIN; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **XX** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XX = Miscellaneous manufactured articles.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `GoodsItem/Item/TransactionConditions/ID` = **LD-TC-01**  
  The seller's number for these conditions of sale.
- `GoodsItem/Item/TransactionConditions/Description` = **Sold to trade customers only, per pallet of four benches.**  
  The conditions in words.
- `GoodsItem/Item/TransactionConditions/DocumentReference/ID` = **LD-GTC-2026**  
  The seller's general terms of trade.
- `GoodsItem/Item/TransactionConditions/DocumentReference/DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, Lumeway's general terms of trade, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **Cast steel, hot-dip galvanised**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **Kiln-dried hardwood**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colour of the frame, one of the colours it is offered in.
- `GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `GoodsItem/Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; item bench-serra of Valdara Industries (world/items.json)). One ListValue only: UBL rule IND7 allows a second one only in another language.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `GoodsItem/Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Load capacity**  
  The name of code LOAD in the Trade Accord's item property name list.
- `GoodsItem/Item/AdditionalItemProperty/NameCode` = **LOAD** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: LOAD = Load capacity.
- `GoodsItem/Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **SF**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `GoodsItem/Item/Dimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `GoodsItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `GoodsItem/Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `GoodsItem/Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `GoodsItem/Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `GoodsItem/Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `GoodsItem/Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `GoodsItem/Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `EA`)  
  The emission is per one bench.
- `GoodsItem/Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `GoodsItem/Item/EnvironmentalEmission/LifecycleStageCode` = **MANUFACTURING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The part of the bench's life the figure covers. The code is from the Trade Accord's life cycle stage list: MANUFACTURING = Manufacturing.
- `GoodsItem/Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `GoodsItem/Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **CRADLETOGATE** (listID `urn:ubl-examples:world:codelist:EmissionBoundaryCode`)  
  How much of the chain is included. The code is from the Trade Accord's emission boundary list: CRADLETOGATE = Cradle to gate.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `GoodsItem/Item/CircularityProfile/MaintenanceFrequencyCode` = **YEARLY** (listID `urn:ubl-examples:world:codelist:MaintenanceFrequencyCode`)  
  How often the item needs maintenance. The code is from the Trade Accord's maintenance frequency list: YEARLY = Once a year.
- `GoodsItem/Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **STEEL** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: STEEL = Steel.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **HARDWOOD** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: HARDWOOD = Hardwood.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **PACKAGING** (listID `urn:ubl-examples:world:codelist:WasteTypeCode`)  
  The kind of waste the item leaves. The code is from the Trade Accord's waste type list: PACKAGING = Packaging.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **Stretch film and pallet straps, per bench**  
  The waste in words.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/WasteMeasure` = **0.4** (unitCode `KGM`)  
  How much of it per item.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **REPAIR10** (listID `urn:ubl-examples:world:codelist:ScoringSystemCode`)  
  The scale of the score. The code is from the Trade Accord's scoring system list: REPAIR10 = Repairability index, 0 to 10.
- `GoodsItem/Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **768.00** (currencyID `XBL`)  
  The value of the goods, in lume.
- `GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description; item bench-casting-b of Lumeway Distribution (world/items.json).
- `GoodsItem/Item/Name` = **Bench side frame casting**  
  The item's short name; item bench-casting-b of Lumeway Distribution (world/items.json).
- `GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/ModelName` = **Serra 180 side frame**  
  The model; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ID` = **LD-10443**  
  The seller's own item number; item bench-casting-b of Lumeway Distribution (world/items.json).
- `GoodsItem/Item/ManufacturersItemIdentification/ID` = **VI-C180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-casting.
- `GoodsItem/Item/StandardItemIdentification/ID` = **9520610000029** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none (world/items.json).
- `GoodsItem/Item/AdditionalItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The maker's own number for the item, its Codana item number, which travels along with the GTIN; item bench-casting of Valdara Industries (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **XV** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XV = Base metals and articles of base metal.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **732599** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 732599 = Other cast articles of iron or steel: other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **42999** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 42999 = Metal goods n.e.c..
- `GoodsItem/Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container's number: the owner code of the ocean carrier, U for a freight container, six digits and the ISO 6346 check digit.
- `TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7856.4** (unitCode `KGM`)  
  The verified gross mass: cargo and the container's own weight of 3,750 kg.
- `TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **3750** (unitCode `KGM`)  
  The empty container's own weight, as marked on its door.

### Document Reference

Inside `DocumentReference`:

- `ID` = **VT-PO-26-0127**  
  The buyer's order.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: VT-PO-26-0127 is the example sea/05, a Order; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Order.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  To the forwarder.
- `DocumentTypeCode` = **PackingList** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this packing list. The code is from the Trade Accord's UBL document type list: PackingList = Packing List.
- `DistributionTypeCode` = **ELECTRONICCOPY** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  A copy for the forwarder, who keeps it with the container's documents. The code is from the Trade Accord's distribution type list: ELECTRONICCOPY = Electronic copy.
- `Party/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-PL**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PackingList xmlns="urn:oasis:names:specification:ubl:schema:xsd:PackingList-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:packing-list:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-PL-26-0134</cbc:ID>
  <cbc:UUID>51ffd2ec-220f-52f3-bbda-f00884ed47a2</cbc:UUID>
  <cbc:IssueDate>2026-05-12</cbc:IssueDate>
  <cbc:IssueTime>15:59:00</cbc:IssueTime>
  <cbc:Name>Packing list</cbc:Name>
  <cbc:Description>The container's contents.</cbc:Description>
  <cbc:Note>25 pallets.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:OtherInstruction>Keep with the container's documents.</cbc:OtherInstruction>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
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
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
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
    <cac:Contact>
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Export coordinator</cbc:JobTitle>
      <cbc:Department>Export</cbc:Department>
      <cbc:Telephone>+999 2 38 2144 1644</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>LD-SH-26-0132</cbc:ID>
    <cbc:ShippingPriorityLevelCode listID="urn:ubl-examples:world:codelist:ShippingPriorityCode">STANDARD</cbc:ShippingPriorityLevelCode>
    <cbc:HandlingInstructions>Castings pallet at the doors.</cbc:HandlingInstructions>
    <cbc:GrossWeightMeasure unitCode="KGM">7856.4</cbc:GrossWeightMeasure>
    <cbc:NetWeightMeasure unitCode="KGM">3762</cbc:NetWeightMeasure>
    <cbc:NetVolumeMeasure unitCode="MTQ">38.9</cbc:NetVolumeMeasure>
    <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">25</cbc:TotalTransportHandlingUnitQuantity>
    <cbc:SpecialInstructions>Photograph the load before closing the doors.</cbc:SpecialInstructions>
    <cbc:DeliveryInstructions>Deliver to the buyer's 3PL, Nalevi Warehousing, Selanu.</cbc:DeliveryInstructions>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0133</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">4106.4</cbc:GrossWeightMeasure>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Velumi Trading</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
          <cbc:StreetName languageID="en-XB">Reef Street</cbc:StreetName>
          <cbc:BuildingNumber>16</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XB">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Goods-in</cbc:Name>
          <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
          <cbc:Department>Warehouse</cbc:Department>
          <cbc:Telephone>+999 3 729 1859</cbc:Telephone>
          <cbc:ElectronicMail>goodsin@velumi.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">49920.00</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Item>
        <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
        <cbc:Keyword>park bench, street furniture</cbc:Keyword>
        <cbc:BrandName>Valdara</cbc:BrandName>
        <cbc:ModelName>Serra 180</cbc:ModelName>
        <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
        <cac:SellersItemIdentification>
          <cbc:ID>LD-10442</cbc:ID>
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
        </cac:StandardItemIdentification>
        <cac:AdditionalItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
        </cac:AdditionalItemIdentification>
        <cac:ItemSpecificationDocumentReference>
          <cbc:ID>VI-DS-B180</cbc:ID>
        </cac:ItemSpecificationDocumentReference>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">XX</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:TransactionConditions>
          <cbc:ID>LD-TC-01</cbc:ID>
          <cbc:Description>Sold to trade customers only, per pallet of four benches.</cbc:Description>
          <cac:DocumentReference>
            <cbc:ID>LD-GTC-2026</cbc:ID>
            <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
          </cac:DocumentReference>
        </cac:TransactionConditions>
        <cac:AdditionalItemProperty>
          <cbc:Name>Frame material</cbc:Name>
          <cbc:Value>Cast steel, hot-dip galvanised</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Slat wood</cbc:Name>
          <cbc:Value>Kiln-dried hardwood</cbc:Value>
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
                <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
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
        <cac:Dimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1800</cbc:Measure>
          <cbc:Description>Over the armrests</cbc:Description>
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
          <cbc:ValueMeasure unitCode="KGM">96</cbc:ValueMeasure>
          <cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>
          <cbc:ValueBaseMeasure unitCode="EA">1</cbc:ValueBaseMeasure>
          <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
          <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">MANUFACTURING</cbc:LifecycleStageCode>
          <cbc:LifecycleStageDescription>From the ore at the mine to the bench leaving the factory gate.</cbc:LifecycleStageDescription>
          <cbc:Description>Mining, steel making, casting, galvanising, sawing and the transport between them.</cbc:Description>
          <cac:EmissionCalculationMethod>
            <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
            <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode">CRADLETOGATE</cbc:FullnessIndicationCode>
            <cbc:EmissionFactorSource>The steelworks' and sawmill's measured energy use of 2025</cbc:EmissionFactorSource>
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
          <cbc:MaintenanceFrequencyDescription>Tighten the slat bolts and touch up the coating once a year.</cbc:MaintenanceFrequencyDescription>
          <cac:ResourceConsumption>
            <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">STEEL</cbc:ResourceTypeCode>
            <cbc:ConsumptionMeasure unitCode="KGM">34</cbc:ConsumptionMeasure>
            <cbc:ResourceOriginDescription>Steel made from Serravona ore in Urvania</cbc:ResourceOriginDescription>
            <cac:MeasurementPeriod>
              <cbc:StartDate>2025-01-01</cbc:StartDate>
              <cbc:EndDate>2025-12-31</cbc:EndDate>
            </cac:MeasurementPeriod>
          </cac:ResourceConsumption>
          <cac:ResourceConsumption>
            <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">HARDWOOD</cbc:ResourceTypeCode>
            <cbc:ConsumptionMeasure unitCode="KGM">22.5</cbc:ConsumptionMeasure>
            <cbc:ResourceOriginDescription>Slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
            <cac:MeasurementPeriod>
              <cbc:StartDate>2025-01-01</cbc:StartDate>
              <cbc:EndDate>2025-12-31</cbc:EndDate>
            </cac:MeasurementPeriod>
          </cac:ResourceConsumption>
          <cac:WasteGenerated>
            <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:WasteTypeCode">PACKAGING</cbc:WasteTypeCode>
            <cbc:WasteTypeDescription>Stretch film and pallet straps, per bench</cbc:WasteTypeDescription>
            <cbc:WasteMeasure unitCode="KGM">0.4</cbc:WasteMeasure>
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
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Bench side frame casting</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">768.00</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
        <cbc:Name>Bench side frame casting</cbc:Name>
        <cbc:BrandName>Valdara</cbc:BrandName>
        <cbc:ModelName>Serra 180 side frame</cbc:ModelName>
        <cac:SellersItemIdentification>
          <cbc:ID>LD-10443</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:ManufacturersItemIdentification>
          <cbc:ID>VI-C180</cbc:ID>
        </cac:ManufacturersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9520610000029</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:AdditionalItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
        </cac:AdditionalItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">XV</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">732599</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">42999</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ManufacturerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Valdara Industries</cbc:Name>
          </cac:PartyName>
        </cac:ManufacturerParty>
      </cac:Item>
    </cac:GoodsItem>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
        <cbc:GrossWeightMeasure unitCode="KGM">7856.4</cbc:GrossWeightMeasure>
        <cbc:TareWeightMeasure unitCode="KGM">3750</cbc:TareWeightMeasure>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>VT-PO-26-0127</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">PackingList</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONICCOPY</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bayforth Forwarding</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>LD-SIG-PL</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</PackingList>
```
