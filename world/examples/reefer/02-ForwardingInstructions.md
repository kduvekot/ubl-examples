# Forwarding Instructions: Harrowmead Fruit Growers to Bayforth Forwarding

*Example 2 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

The cooperative instructs its forwarder: book a reefer on the sailing, with its settings for the fruit, bring it pre-cooled to the packhouse and back to the port, declare the export and insure the cargo (CIP obliges the seller to insure).

[The XML file](02-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:forwarding-instructions:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Forwarding instructions". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **HFG-FI-26-0554**  
  The cooperative's instruction number.
- `UUID` = **dfd9428d-d416-5644-94ad-a60cf64f2bde**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-14**  
  The cooperative books the reefer on Tuesday 14 April, after Upland State Day on the Monday, nine days before the sailing.
- `IssueTime` = **12:36:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Harrowmead Fruit Growers (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-415873** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; identity of Harrowmead Fruit Growers (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-418726** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Orchard Road**  
  Street of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/CityName` = **Harrowmead**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/PostalZone` = **71640**  
  Postal code in Bayvarra's format (5 digits). identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Harrowmead Fruit Growers (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Department` = **Packhouse**  
  The department the desk belongs to; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Telephone` = **+999 2 7164 281 590**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/ElectronicMail` = **dispatch@harrowmeadfruit.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; identity of Harrowmead Fruit Growers (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20415873** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Export desk**  
  The party's export desk: the desk for its role in this document (it handles the transport of goods between the countries); identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Export coordinator**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Export**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 5155 2404**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **HFG-SH-26-0555**  
  The shipment to be booked.
- `Consignment/ID` = **HFG-CS-26-0556**  
  The cooperative's consignment number.
- `Consignment/GrossWeightMeasure` = **21728** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight of the fruit on its pallets.
- `Consignment/ForwarderServiceInstructions` = **Book a 40-foot reefer on Tidewell's sailing of 23 April to Selanu; have it pre-trip inspected and pre-cooled; bring it to our packhouse on 22 April and back to the port on a generator set; declare the export and insure the fruit.**  
  What the forwarder is to do.
- `Consignment/ConsolidatableIndicator` = **false**  
  A full reefer: not to be grouped with other cargo.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Hafefo Fresh Produce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-043529** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Cold store**  
  The party's cold store desk: the desk for its role in this document (it receives the goods); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Cold store supervisor**  
  The job of the person who answers at the desk; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Cold store**  
  The department the desk belongs to; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **coldstore@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ExporterParty/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/ExporterParty/PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/ImporterParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/ImporterParty/PartyName/Name` = **Hafefo Fresh Produce**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsuranceParty/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsuranceParty/PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDespatchTransportationService/TransportServiceCode` = **MERCHHAUL** (listID `urn:ubl-examples:world:codelist:TransportServiceCode`)  
  The forwarder, not the shipping line, brings the reefer to the port. The code is from the Trade Accord's transport service list: MERCHHAUL = Merchant haulage.
- `Consignment/OriginalDespatchTransportationService/Name` = **Reefer truck from Harrowmead to the port of Lumeport**  
  In words.
- `GoodsItem/ID` = **1**  
  The fruit in the reefer, as one item for the carrier.
- `GoodsItem/Description` = **Fresh apples and pears in cartons, on 20 pallets**  
  In words.
- `GoodsItem/GrossWeightMeasure` = **21728** (unitCode `KGM`)  
  The fruit in its cartons and the pallets.
- `GoodsItem/Temperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Temperature/Measure` = **0.5** (unitCode `CEL`)  
  The set point the reefer is to hold: 0.5 °C, the middle of the fruit's range.
- `GoodsItem/Temperature/Description` = **Set point**  
  In words.
- `GoodsItem/ContainedGoodsItem/ID` = **1.1**  
  The apples, Gala and Granny Smith.
- `GoodsItem/ContainedGoodsItem/Description` = **Fresh apples**  
  In words.
- `GoodsItem/ContainedGoodsItem/Item/Name` = **Fresh apples**  
  The goods.
- `GoodsItem/ContainedGoodsItem/Item/CommodityClassification/CommodityCode` = **080810** (listID `WCO HS 2022`)  
  The Harmonized System subheading of fresh apples, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080810 = Apples, fresh.
- `GoodsItem/ContainedGoodsItem/ID` = **1.2**  
  The pears.
- `GoodsItem/ContainedGoodsItem/Description` = **Fresh pears**  
  In words.
- `GoodsItem/ContainedGoodsItem/Item/Name` = **Fresh pears**  
  The goods.
- `GoodsItem/ContainedGoodsItem/Item/CommodityClassification/CommodityCode` = **080830** (listID `WCO HS 2022`)  
  The Harmonized System subheading of fresh pears. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080830 = Pears, fresh.
- `GoodsItem/MinimumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **0** (unitCode `CEL`)  
  The coldest the fruit may be carried at.
- `GoodsItem/MaximumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **1** (unitCode `CEL`)  
  The warmest.
- `TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45R1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet, 9 ft 6 in high (high cube), a refrigerated container with its own refrigerating machinery. The code is from the world's copy of ISO 6346 container size and type code: 45R1 = 40 ft, 9 ft 6 in high, thermal, refrigerated and heated.
- `TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  The refrigeration runs, from the pre-cooling before loading to the unloading at the cold store: fresh fruit must not warm up.
- `TransportHandlingUnit/TransportEquipment/AirFlowPercent` = **15**  
  The fresh-air vent's setting: open to 15 % of its full opening, about 25 m³ of outside air an hour on Tidewell's units. Apples and pears breathe; fresh air carries off the carbon dioxide and the ethylene that would ripen them.
- `TransportHandlingUnit/TransportEquipment/HumidityPercent` = **90**  
  The relative humidity the reefer is set to hold: about 90 %, so that the fruit does not dry out and shrivel.
- `TransportHandlingUnit/TransportEquipment/HumanFoodApprovedIndicator` = **true**  
  The reefer is approved for food: its interior is of food-grade materials and cleaned to carry food, which unpacked fruit in open trays needs.
- `TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **true**  
  A refrigerated container.
- `TransportHandlingUnit/TransportEquipment/MinimumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/TransportEquipment/MinimumTemperature/Measure` = **0** (unitCode `CEL`)  
  The lowest air temperature the reefer may reach: colder, the fruit begins to freeze.
- `TransportHandlingUnit/TransportEquipment/MaximumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/TransportEquipment/MaximumTemperature/Measure` = **1** (unitCode `CEL`)  
  The highest: warmer, it ripens on the way.
- `InsurancePolicy/InsuranceTypeDescription` = **Cargo insurance on Institute Cargo Clauses (A), all risks, including loss from a breakdown of the refrigeration**  
  The cover Incoterms 2020 CIP asks of the seller, and the risk that matters for fruit.
- `InsurancePolicy/InsuredValueAmount` = **31908.80** (currencyID `XBL`)  
  CIP requires insurance of at least 110 % of the value: the fruit at its CIP prices plus 10 %.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:forwarding-instructions:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>HFG-FI-26-0554</cbc:ID>
  <cbc:UUID>dfd9428d-d416-5644-94ad-a60cf64f2bde</cbc:UUID>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>12:36:00-01:00</cbc:IssueTime>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9527430900003</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-415873</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-418726</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Orchard Road</cbc:StreetName>
      <cbc:BuildingNumber>3</cbc:BuildingNumber>
      <cbc:CityName>Harrowmead</cbc:CityName>
      <cbc:PostalZone>71640</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Packhouse</cbc:Department>
      <cbc:Telephone>+999 2 7164 281 590</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@harrowmeadfruit.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20415873</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ConsignorParty>
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
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Export coordinator</cbc:JobTitle>
      <cbc:Department>Export</cbc:Department>
      <cbc:Telephone>+999 2 38 5155 2404</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>HFG-SH-26-0555</cbc:ID>
    <cac:Consignment>
      <cbc:ID>HFG-CS-26-0556</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">21728</cbc:GrossWeightMeasure>
      <cbc:ForwarderServiceInstructions>Book a 40-foot reefer on Tidewell's sailing of 23 April to Selanu; have it pre-trip inspected and pre-cooled; bring it to our packhouse on 22 April and back to the port on a generator set; declare the export and insure the fruit.</cbc:ForwarderServiceInstructions>
      <cbc:ConsolidatableIndicator>false</cbc:ConsolidatableIndicator>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-043529</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Hafefo Fresh Produce</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40618392</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
          <cbc:BuildingNumber>58</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Cold store</cbc:Name>
          <cbc:JobTitle>Cold store supervisor</cbc:JobTitle>
          <cbc:Department>Cold store</cbc:Department>
          <cbc:Telephone>+999 3 726 8104</cbc:Telephone>
          <cbc:ElectronicMail>coldstore@hafefo.example</cbc:ElectronicMail>
          <cbc:Note>Monday to Saturday 05:00–14:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:ExporterParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
        </cac:PartyName>
      </cac:ExporterParty>
      <cac:ImporterParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Hafefo Fresh Produce</cbc:Name>
        </cac:PartyName>
      </cac:ImporterParty>
      <cac:InsuranceParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
        </cac:PartyName>
      </cac:InsuranceParty>
      <cac:OriginalDespatchTransportationService>
        <cbc:TransportServiceCode listID="urn:ubl-examples:world:codelist:TransportServiceCode">MERCHHAUL</cbc:TransportServiceCode>
        <cbc:Name>Reefer truck from Harrowmead to the port of Lumeport</cbc:Name>
      </cac:OriginalDespatchTransportationService>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Fresh apples and pears in cartons, on 20 pallets</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">21728</cbc:GrossWeightMeasure>
      <cac:Temperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">0.5</cbc:Measure>
        <cbc:Description>Set point</cbc:Description>
      </cac:Temperature>
      <cac:ContainedGoodsItem>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Description>Fresh apples</cbc:Description>
        <cac:Item>
          <cbc:Name>Fresh apples</cbc:Name>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">080810</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:ContainedGoodsItem>
      <cac:ContainedGoodsItem>
        <cbc:ID>1.2</cbc:ID>
        <cbc:Description>Fresh pears</cbc:Description>
        <cac:Item>
          <cbc:Name>Fresh pears</cbc:Name>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">080830</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:ContainedGoodsItem>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">0</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">1</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
        <cbc:SizeTypeCode listID="ISO 6346">45R1</cbc:SizeTypeCode>
        <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
        <cbc:AirFlowPercent>15</cbc:AirFlowPercent>
        <cbc:HumidityPercent>90</cbc:HumidityPercent>
        <cbc:HumanFoodApprovedIndicator>true</cbc:HumanFoodApprovedIndicator>
        <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">0</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">1</cbc:Measure>
        </cac:MaximumTemperature>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    <cac:InsurancePolicy>
      <cbc:InsuranceTypeDescription>Cargo insurance on Institute Cargo Clauses (A), all risks, including loss from a breakdown of the refrigeration</cbc:InsuranceTypeDescription>
      <cbc:InsuredValueAmount currencyID="XBL">31908.80</cbc:InsuredValueAmount>
    </cac:InsurancePolicy>
  </cac:Shipment>
</ForwardingInstructions>
```
