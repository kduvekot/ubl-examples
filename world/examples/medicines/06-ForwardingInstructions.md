# Forwarding Instructions: Quillmoor Pharma Distribution to Bayforth Forwarding

*Example 6 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

The wholesaler asks its forwarder to book the Monday morning flight: the cold chain goods in the airline's active container, the frozen vaccine on dry ice, and the generator under the shipper's declaration of its own.

[The XML file](06-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:forwarding-instructions:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Forwarding instructions". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **MEDICINES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **QPD-FI-26-0329**  
  The instruction number.
- `UUID` = **9c9dac7e-9d28-5eec-bf12-be960571ab4f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-11**  
  The wholesaler books the Monday flight on Thursday.
- `IssueTime` = **09:20:00-01:00**  
  In the morning; in the issuer's local time, with its offset from UTC (D27).
- `Name` = **Forwarding instructions**  
  What they are.
- `Note` = **Please book KXL207 of Monday 15 June with the airline's active container at 5 °C; collect the container and the dry-ice box at our cold rooms at 04:15. Our van brings the generator to the cargo terminal by 05:30 with its shipper's declaration.**  
  What the wholesaler asks: the forwarder books the whole consignment, and the wholesaler brings the radioactive package itself (O202 choice 4).

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Quillmoor Pharma Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Quillmoor Pharma Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-413425** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Quillmoor Pharma Distribution (world/parties.json).
- `PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-718264** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **40**  
  Building number of the postal address. identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). identity of Quillmoor Pharma Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Quillmoor Pharma Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/ElectronicMail` = **dispatch@quillmoor.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Quillmoor Pharma Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 07:00–19:00**  
  When the desk can be reached; identity of Quillmoor Pharma Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20413425** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Quillmoor Pharma Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `ID` = **QPD-SH-26-0323**  
  The shipment.
- `Consignment/ID` = **QPD-CS-26-0330**  
  The consignment.
- `Consignment/GrossWeightMeasure` = **101.1** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The goods in their packages, with the dry ice and its box.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; identity of Selanu General Hospital (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu General Hospital**  
  The trading name; identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **52968014** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **81**  
  Building number of the postal address. identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Pharmacy goods-in**  
  The party's pharmacy goods-in desk: the desk for its role in this document (it receives the goods); identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Pharmacy technician**  
  The job of the person who answers at the desk; identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Pharmacy**  
  The department the desk belongs to; identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 726 8840**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **pharmacy-goodsin@selanu-hospital.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu General Hospital (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 07:30–17:00**  
  When the desk can be reached; identity of Selanu General Hospital (world/parties.json).
- `Consignment/HazardousItemNotificationParty/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/HazardousItemNotificationParty/PartyName/Name` = **Quillmoor Pharma Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/ID` = **QPD-TC-1**  
  The cold-chain consignment as one handling unit, the wholesaler's own number: the forwarder books the airline's active container for it.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: the cartons, which the airline loads into its container. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Keep at 2 to 8 °C; do not freeze; do not open before the island's cargo terminal.**  
  What the cold chain needs.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The vaccines and the insulin must not fall below 2 °C: they lose their potency when they freeze. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Nor rise above 8 °C. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-1**  
  Shipper carton 1: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-2**  
  Shipper carton 2: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-3**  
  Shipper carton 3: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-4**  
  Shipper carton 4: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-5**  
  Shipper carton 5: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-6**  
  Shipper carton 6: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-7**  
  Shipper carton 7: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-8**  
  Shipper carton 8: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-9**  
  Shipper carton 9: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-10**  
  Shipper carton 10: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-11**  
  Shipper carton 11: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-12**  
  Shipper carton 12: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-13**  
  Shipper carton 13: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-CT-14**  
  Shipper carton 14: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/ID` = **QPD-BX-1**  
  The insulated box of the frozen vaccine, the wholesaler's own number.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Frozen vaccine on 6 kg of dry ice: keep the box upright and its vent clear; do not put it in the active container.**  
  How the box is handled: dry ice gives off carbon dioxide, and at -78 °C it would freeze the goods at 2 to 8 °C.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  The dry ice is dangerous goods of class 9.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The live vaccine is kept frozen, at -50 °C or warmer. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **-50** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  And at -15 °C or colder. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **-15** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-BX-1**  
  The box itself.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **40** (unitCode `EA`)  
  Forty vials of the varicella vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/ID` = **QPD-RA-1**  
  The generator's Type A package, the wholesaler's own number.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box, the outer package. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Radioactive, Category III-YELLOW, transport index 1.5: stow in the aft hold, away from the crew and from the frozen vaccine's box.**  
  How the package is stowed: away from persons, by the distance its transport index asks.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Radioactive material of class 7.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/Package/ID` = **QPD-RA-1**  
  The package itself.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One generator.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of the outer package. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **400** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of the outer package. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **300** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of the outer package. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **300** (unitCode `MMT`)  
  In millimetres.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **60** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **300** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  The goods, named.
- `GoodsItem/Temperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The temperature to carry the goods at: the middle of their range, which the active container is set to. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Temperature/Measure` = **5** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/Temperature/MeasureCode` = **TARGET** (listID `urn:ubl-examples:world:codelist:TemperatureQualifierCode`)  
  Which value of the range it is: the one to keep. The code is from the Trade Accord's temperature qualifier list: TARGET = Target.
- `GoodsItem/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **12** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **240** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  The goods, named.
- `GoodsItem/Temperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The temperature to carry the goods at: the middle of their range, which the active container is set to. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Temperature/Measure` = **5** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/Temperature/MeasureCode` = **TARGET** (listID `urn:ubl-examples:world:codelist:TemperatureQualifierCode`)  
  Which value of the range it is: the one to keep. The code is from the Trade Accord's temperature qualifier list: TARGET = Target.
- `GoodsItem/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Varicella vaccine, live, frozen, single dose**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **1.6** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **40** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Varicella vaccine, live, frozen, single dose**  
  The goods, named.
- `GoodsItem/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: frozen, -50 to -15 °C. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **-50** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: frozen, -50 to -15 °C. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **-15** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/ID` = **4**  
  The goods item number.
- `GoodsItem/Description` = **Technetium-99m generator, 20 GBq**  
  What is carried, in words.
- `GoodsItem/HazardousRiskIndicator` = **true**  
  Radioactive material.
- `GoodsItem/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **1** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Technetium-99m generator, 20 GBq**  
  The goods, named.
- `GoodsItem/Item/HazardousItem/ID` = **QPD-RAD-0020-DG**  
  The wholesaler's dangerous goods record of the generator.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the hazard label of the packages.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h**  
  What the shipper adds about handling.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2915** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2915 = Radioactive material, Type A package, non-special form, non fissile or fissile-excepted.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **163** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 163 = Radioactive Materials (Low to High Level Radiation).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, Type A package, non-special form, non fissile or fissile-excepted**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2915**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The Type A package with the generator.
- `GoodsItem/Item/HazardousItem/Quantity` = **1** (unitCode `EA`)  
  One package.
- `GoodsItem/Item/HazardousItem/ContactParty/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/HazardousItem/ContactParty/PartyName/Name` = **Quillmoor Pharma Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/HazardousItem/ContactParty/Contact/Name` = **Dangerous goods emergency line**  
  Whom to call in an incident with the generator: the wholesaler's radiation protection officer.
- `GoodsItem/Item/HazardousItem/ContactParty/Contact/Telephone` = **+999 2 38 6047 1590**  
  The line answers around the clock while the goods are on the way; under the reserved +999.
- `GoodsItem/Item/HazardousItem/ContactParty/Contact/Note` = **Every day, around the clock**  
  When it answers.
- `GoodsItem/Item/HazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `GoodsItem/Item/HazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **PCA** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  A Type A package with a transport index of 1.5 may fly on passenger aircraft too; it flies on the freighter because that is the island's cargo flight. The code is from the Trade Accord's transport authorization list: PCA = Passenger and cargo aircraft.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)**  
  The radionuclide and the maximum activity during transport, which the transport document must state in becquerels (IAEA SSR-6 para 546): UBL has no element for the activity of contents that are not fissile, so the name carries it, a finding for the TC (O202 choice 6). The activity is the generator's at acceptance at the Lumeport cargo terminal, the highest it has on the way, as Mo-99 decays (O202 choice 4); the A2 value of Mo-99 allows up to 600 GBq in a Type A package.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.**  
  The physical and chemical form: not special form, so the A2 value applies.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **1.5**  
  The transport index of the package: the highest dose rate at 1 m in mSv/h times 100, rounded up to the first decimal (IAEA SSR-6 para 523); above 1, so the package carries the Category III-YELLOW label (para 529, the higher category winning over the surface rate; O202 choice 1).

### Document Reference

Inside `DocumentReference`:

- `ID` = **SGH-PO-26-0327**  
  The hospital's order the goods are for.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: SGH-PO-26-0327 is the example medicines/04, a Order; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Order.
- `ID` = **QPD-DGD-26-0615**  
  The shipper's declaration for dangerous goods of the generator, a declaration of its own: radioactive material may not share one with other dangerous goods, and the dry ice needs none, only its entry on the air waybill (O202 choice 5; resting on secondary sources, O211). It goes with the package, signed when the generator's activity is measured on Monday.
- `DocumentTypeCode` = **890** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, the wholesaler's shipper's declaration for dangerous goods of the technetium generator, a declaration of its own (O202 choice 5), a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 890 = Dangerous goods declaration.

### Signature

Inside `Signature`:

- `ID` = **QPD-SIG-FI-26**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Quillmoor Pharma Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:forwarding-instructions:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MEDICINES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>QPD-FI-26-0329</cbc:ID>
  <cbc:UUID>9c9dac7e-9d28-5eec-bf12-be960571ab4f</cbc:UUID>
  <cbc:IssueDate>2026-06-11</cbc:IssueDate>
  <cbc:IssueTime>09:20:00-01:00</cbc:IssueTime>
  <cbc:Name>Forwarding instructions</cbc:Name>
  <cbc:Note>Please book KXL207 of Monday 15 June with the airline's active container at 5 °C; collect the container and the dry-ice box at our cold rooms at 04:15. Our van brings the generator to the cargo terminal by 05:30 with its shipper's declaration.</cbc:Note>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9524910900003</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-413425</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-718264</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Airport Road</cbc:StreetName>
      <cbc:BuildingNumber>40</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38528</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 38 6047 1582</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@quillmoor.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:00–19:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20413425</cbc:ElectronicAddressID>
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
    <cbc:ID>QPD-SH-26-0323</cbc:ID>
    <cac:Consignment>
      <cbc:ID>QPD-CS-26-0330</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">101.1</cbc:GrossWeightMeasure>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu General Hospital</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">52968014</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
          <cbc:BuildingNumber>81</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Pharmacy goods-in</cbc:Name>
          <cbc:JobTitle>Pharmacy technician</cbc:JobTitle>
          <cbc:Department>Pharmacy</cbc:Department>
          <cbc:Telephone>+999 3 726 8840</cbc:Telephone>
          <cbc:ElectronicMail>pharmacy-goodsin@selanu-hospital.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 07:30–17:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:HazardousItemNotificationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
        </cac:PartyName>
      </cac:HazardousItemNotificationParty>
      <cac:TransportHandlingUnit>
        <cbc:ID>QPD-TC-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Keep at 2 to 8 °C; do not freeze; do not open before the island's cargo terminal.</cbc:HandlingInstructions>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">2</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">8</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:Package>
          <cbc:ID>QPD-CT-1</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-2</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-3</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-4</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-5</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-6</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-7</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-8</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-9</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-10</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-11</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-12</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-13</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QPD-CT-14</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>QPD-BX-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Frozen vaccine on 6 kg of dry ice: keep the box upright and its vent clear; do not put it in the active container.</cbc:HandlingInstructions>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">-50</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">-15</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:Package>
          <cbc:ID>QPD-BX-1</cbc:ID>
          <cbc:Quantity unitCode="EA">40</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>QPD-RA-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Radioactive, Category III-YELLOW, transport index 1.5: stow in the aft hold, away from the crew and from the frozen vaccine's box.</cbc:HandlingInstructions>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:HazardousGoodsTransit>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
        </cac:HazardousGoodsTransit>
        <cac:Package>
          <cbc:ID>QPD-RA-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">400</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">DEPTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">300</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">300</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">60</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">300</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Name>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
        <cbc:MeasureCode listID="urn:ubl-examples:world:codelist:TemperatureQualifierCode">TARGET</cbc:MeasureCode>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">2</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">8</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">12</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Name>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
        <cbc:MeasureCode listID="urn:ubl-examples:world:codelist:TemperatureQualifierCode">TARGET</cbc:MeasureCode>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">2</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">8</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Varicella vaccine, live, frozen, single dose</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">1.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">40</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Varicella vaccine, live, frozen, single dose</cbc:Name>
      </cac:Item>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">-50</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">-15</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>4</cbc:ID>
      <cbc:Description>Technetium-99m generator, 20 GBq</cbc:Description>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cbc:GrossWeightMeasure unitCode="KGM">18</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Technetium-99m generator, 20 GBq</cbc:Name>
        <cac:HazardousItem>
          <cbc:ID>QPD-RAD-0020-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2915</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">163</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, Type A package, non-special form, non fissile or fissile-excepted</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2915</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
          <cbc:GrossWeightMeasure unitCode="KGM">18</cbc:GrossWeightMeasure>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cac:ContactParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
            </cac:PartyName>
            <cac:Contact>
              <cbc:Name>Dangerous goods emergency line</cbc:Name>
              <cbc:Telephone>+999 2 38 6047 1590</cbc:Telephone>
              <cbc:Note>Every day, around the clock</cbc:Note>
            </cac:Contact>
          </cac:ContactParty>
          <cac:HazardousGoodsTransit>
            <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
            <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">PCA</cbc:TransportAuthorizationCode>
          </cac:HazardousGoodsTransit>
          <cac:RadioactiveMaterial>
            <cbc:Name>Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)</cbc:Name>
            <cbc:SpecialFormDescription>Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.</cbc:SpecialFormDescription>
            <cbc:TransportIndexNumeric>1.5</cbc:TransportIndexNumeric>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>SGH-PO-26-0327</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentReference>
    <cbc:ID>QPD-DGD-26-0615</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">890</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>QPD-SIG-FI-26</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ForwardingInstructions>
```
