# Forwarding Instructions: Saltmere Engineering to Bayforth Forwarding

*Example 2 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

The engineering firm instructs the forwarder, with the shipper's declaration of dangerous goods and how the cargo-aircraft-only packages must be stowed.

[The XML file](02-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:forwarding-instructions:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Forwarding instructions". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SE-FI-26-0714**  
  The instruction number.
- `UUID` = **a587c22d-2b9a-58c7-a95e-3c142f8b615c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-03**  
  With the shipper's declaration of dangerous goods.
- `IssueTime` = **11:57:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Saltmere Engineering (world/parties.json).
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 930 729**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `Contact/ElectronicMail` = **dispatch@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `ID` = **SE-SH-26-0715**  
  The shipment.
- `Consignment/ID` = **SE-CS-26-0716**  
  The consignment.
- `Consignment/GrossWeightMeasure` = **333.75** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Network stores**  
  The party's network stores desk: the desk for its role in this document (it receives the goods); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Stores supervisor**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Network operations**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 727 3193**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **stores@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Consignment/HazardousItemNotificationParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/HazardousItemNotificationParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/ID` = **SE-PL-1**  
  The pallet of battery crates as a handling unit.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Twelve crates of 27 kg on one pallet: move the pallet by fork-lift; a single crate is a two-person lift. Stow where the crew can reach it, and not next to packages with a class 3 label.**  
  How the pallet is handled, and the stowage the airline must give it: what the consignor asks, not the airline's container and position (mast/02#F16).
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA: lithium ion batteries of more than 100 Wh, packed alone. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only: section IA batteries may not fly on passenger aircraft. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.**  
  The conditions, as on the shipper's declaration.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-1**  
  Crate 1 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0001**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-2**  
  Crate 2 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0002**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-3**  
  Crate 3 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0003**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-4**  
  Crate 4 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0004**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-5**  
  Crate 5 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0005**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-6**  
  Crate 6 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0006**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-7**  
  Crate 7 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0007**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-8**  
  Crate 8 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0008**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-9**  
  Crate 9 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0009**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-10**  
  Crate 10 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0010**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-11**  
  Crate 11 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0011**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-12**  
  Crate 12 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0012**  
  The serial number of the data logger fixed to the crate, which records shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/ID` = **SE-BX-2**  
  The box of stripper as a handling unit.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Stow where the crew can reach it, and not next to the lithium batteries.**  
  The stowage asked for (O210).
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/PackingCriteriaCode` = **PI855** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 855, for cargo aircraft (O210). The code is from the Trade Accord's air packing instruction list: PI855 = Packing instruction 855.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only: five litres in one package are more than the 1 litre a package of this entry may hold on a passenger aircraft (O210). The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; five 1-litre tins in one box.**  
  The conditions, as on the shipper's declaration.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-2**  
  The box of coating stripper, the engineering company's own number.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **5** (unitCode `EA`)  
  Five 1-litre tins in the box.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/ID` = **SE-BX-1**  
  The box of smoke detectors as a handling unit.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods: an excepted package, which needs no particular stowage.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-1**  
  The box of smoke detectors, the engineering company's own number.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One box: the pack of ten.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `GoodsItem/ID` = **1**  
  A goods item.
- `GoodsItem/Description` = **Lithium-ion battery module 48 V 50 Ah**  
  The goods.
- `GoodsItem/Item/Description` = **Back-up battery module for telecom masts, lithium-ion, 2.4 kWh, in a steel case.**  
  The seller's description; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/Name` = **Lithium-ion battery module 48 V 50 Ah**  
  The item's short name; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **850760** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 850760 = Lithium-ion accumulators.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **46420** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 46420 = Electric accumulators.
- `GoodsItem/Item/HazardousItem/ID` = **SE-BAT-4850-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **9**  
  The class shown on the hazard label of the packages.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds about handling.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **147** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 147 = Lithium Ion and Sodium Ion Batteries.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **9** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ID` = **2**  
  A goods item.
- `GoodsItem/Description` = **Ionisation smoke detector set**  
  The goods.
- `GoodsItem/Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/Name` = **Ionisation smoke detector set**  
  The item's short name; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **853110** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 853110 = Burglar or fire alarms and similar apparatus.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **46921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 46921 = Burglar or fire alarms and similar apparatus.
- `GoodsItem/Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label; the UN number on the package.**  
  What the shipper adds about handling.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2911** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2911 = Radioactive material, excepted package – instruments or articles.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **161** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 161 = Radioactive Materials (Low Level Radiation).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2911**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Am-241, 10 × 37 kBq (370 kBq) in ionisation smoke detectors**  
  The nuclide and the activity of the pack as carried, in the name: UBL defines ApplicableRadioactiveIsotope for fissile contents only, and americium-241 is not fissile, so the name is the only place left for them (D36, O127).
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Sealed sources inside the detectors, not special form.**  
  Its form.
- `GoodsItem/ID` = **3**  
  A goods item.
- `GoodsItem/Description` = **Coating stripper for electronics**  
  The goods.
- `GoodsItem/Item/Description` = **Remover for the protective coating of circuit boards, in 1-litre tins, five to a box.**  
  The seller's description; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/Name` = **Coating stripper for electronics**  
  The item's short name; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **381400** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 381400 = Organic composite solvents and thinners, n.e.s.; prepared paint or varnish removers.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **35110** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 35110 = Paints and varnishes and related products.
- `GoodsItem/Item/HazardousItem/ID` = **SE-CS-01-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **8**  
  The class shown on the hazard label of the packages.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2920** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2920 = Corrosive liquid, flammable, n.o.s..
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **II** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: II = Medium danger.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **Medium danger**  
  The name of code II in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **132** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 132 = Flammable Liquids - Corrosive.
- `GoodsItem/Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **8** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2920**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **8** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/ID` = **3** (schemeID `UN Model Regulations hazard class`)  
  The subsidiary hazard: flammable. The code is from the world's copy of UN Model Regulations hazard class and division: 3 = Flammable liquids. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/PlacardNotation` = **3**  
  Shown on a second label.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/EmergencyProceduresCode` = **TEC3** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  UBL defines it as "A code signifying the emergency procedures for this secondary hazard": the Trade Accord's emergency card for class 3. The IMDG Code gives one pair of emergency schedules for the whole UN entry, not one per hazard; the instructions in writing of road transport (ADR 5.4.3), which the Accord's cards follow, give the actions per danger label, the subsidiary hazard's label included. The code is from the Trade Accord's transport emergency card list: TEC3 = Emergency card for class 3.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/Extension` = **Subsidiary risk 3**  
  In words.
- `GoodsItem/Item/HazardousItem/FlashpointTemperature/AttributeID` = **FLASHPOINT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Closed cup. The code is from the Trade Accord's temperature attribute list: FLASHPOINT = Flashpoint. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/FlashpointTemperature/Measure` = **28** (unitCode `CEL`)  
  The flashpoint.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:forwarding-instructions:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SE-FI-26-0714</cbc:ID>
  <cbc:UUID>a587c22d-2b9a-58c7-a95e-3c142f8b615c</cbc:UUID>
  <cbc:IssueDate>2026-06-03</cbc:IssueDate>
  <cbc:IssueTime>11:57:00-01:00</cbc:IssueTime>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Saltmere Engineering</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-587295</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Foundry Road</cbc:StreetName>
      <cbc:BuildingNumber>13</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71218</cbc:PostalZone>
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
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 7121 930 729</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@saltmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
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
    <cbc:ID>SE-SH-26-0715</cbc:ID>
    <cac:Consignment>
      <cbc:ID>SE-CS-26-0716</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">333.75</cbc:GrossWeightMeasure>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Telecom</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">34928611</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Mast Hill Road</cbc:StreetName>
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
          <cbc:Name>Network stores</cbc:Name>
          <cbc:JobTitle>Stores supervisor</cbc:JobTitle>
          <cbc:Department>Network operations</cbc:Department>
          <cbc:Telephone>+999 3 727 3193</cbc:Telephone>
          <cbc:ElectronicMail>stores@selanutelecom.example</cbc:ElectronicMail>
          <cbc:Note>Every day, around the clock</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:HazardousItemNotificationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
      </cac:HazardousItemNotificationParty>
      <cac:TransportHandlingUnit>
        <cbc:ID>SE-PL-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Twelve crates of 27 kg on one pallet: move the pallet by fork-lift; a single crate is a two-person lift. Stow where the crew can reach it, and not next to packages with a class 3 label.</cbc:HandlingInstructions>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:HazardousGoodsTransit>
          <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
          <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
          <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.</cbc:TransitDescription>
        </cac:HazardousGoodsTransit>
        <cac:Package>
          <cbc:ID>SE-CR-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0001</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-2</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0002</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-3</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0003</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-4</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0004</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-5</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0005</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-6</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0006</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-7</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0007</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-8</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0008</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-9</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0009</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-10</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0010</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-11</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0011</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-12</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0012</cbc:TraceID>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>SE-BX-2</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Stow where the crew can reach it, and not next to the lithium batteries.</cbc:HandlingInstructions>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:HazardousGoodsTransit>
          <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI855</cbc:PackingCriteriaCode>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
          <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
          <cbc:TransitDescription>Cargo aircraft only; five 1-litre tins in one box.</cbc:TransitDescription>
        </cac:HazardousGoodsTransit>
        <cac:Package>
          <cbc:ID>SE-BX-2</cbc:ID>
          <cbc:Quantity unitCode="EA">5</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>SE-BX-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:Package>
          <cbc:ID>SE-BX-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Lithium-ion battery module 48 V 50 Ah</cbc:Description>
      <cac:Item>
        <cbc:Description>Back-up battery module for telecom masts, lithium-ion, 2.4 kWh, in a steel case.</cbc:Description>
        <cbc:Name>Lithium-ion battery module 48 V 50 Ah</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">850760</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">46420</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-BAT-4850-DG</cbc:ID>
          <cbc:PlacardNotation>9</cbc:PlacardNotation>
          <cbc:AdditionalInformation>State of charge below 30 %, as the air rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">3480</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">147</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">9</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN3480</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">9</cbc:HazardClassID>
        </cac:HazardousItem>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Ionisation smoke detector set</cbc:Description>
      <cac:Item>
        <cbc:Description>Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.</cbc:Description>
        <cbc:Name>Ionisation smoke detector set</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">853110</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">46921</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-SMK-10-DG</cbc:ID>
          <cbc:AdditionalInformation>Excepted package: no radioactive label; the UN number on the package.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2911</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">161</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2911</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
          <cac:RadioactiveMaterial>
            <cbc:Name>Am-241, 10 × 37 kBq (370 kBq) in ionisation smoke detectors</cbc:Name>
            <cbc:SpecialFormDescription>Sealed sources inside the detectors, not special form.</cbc:SpecialFormDescription>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Coating stripper for electronics</cbc:Description>
      <cac:Item>
        <cbc:Description>Remover for the protective coating of circuit boards, in 1-litre tins, five to a box.</cbc:Description>
        <cbc:Name>Coating stripper for electronics</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">381400</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35110</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-CS-01-DG</cbc:ID>
          <cbc:PlacardNotation>8</cbc:PlacardNotation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2920</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">II</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>Medium danger</cbc:UNPackingGroup>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">132</cbc:MedicalFirstAidGuideCode>
          <cbc:TechnicalName>ethanolamine, propanol</cbc:TechnicalName>
          <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">8</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2920</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">8</cbc:HazardClassID>
          <cac:SecondaryHazard>
            <cbc:ID schemeID="UN Model Regulations hazard class">3</cbc:ID>
            <cbc:PlacardNotation>3</cbc:PlacardNotation>
            <cbc:EmergencyProceduresCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC3</cbc:EmergencyProceduresCode>
            <cbc:Extension>Subsidiary risk 3</cbc:Extension>
          </cac:SecondaryHazard>
          <cac:FlashpointTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">FLASHPOINT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">28</cbc:Measure>
          </cac:FlashpointTemperature>
        </cac:HazardousItem>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
</ForwardingInstructions>
```
