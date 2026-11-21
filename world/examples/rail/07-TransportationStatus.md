# Transportation Status: Ferrano Intermodal Hub to Ferrano Rail Cargo

*Example 7 of the flow "Containers by rail under the Accord's common transit (Urvania → Bayvarra)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The intermodal terminal reports to the rail carrier that the containers are loaded on the train.

[The XML file](07-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:transportation-status:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Transportation status". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900043586**  
  The collaboration this document belongs to: the rail carriage Valdara books with Ferrano Rail Cargo. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **FIH-TS-26-11316**  
  The sender's status report number.
- `UUID` = **514b9478-0214-5ce0-9018-7c4cf752cbd3**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-14**  
  Reported when the containers are on the train.
- `IssueTime` = **06:05:00-01:00**  
  Sent by the terminal's system once both boxes were on their wagons; in the issuer's local time, with its offset from UTC.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Two containers loaded on the container train.**  
  In words.
- `Note` = **Krerdan skuskek mir drek stalkan sazhir kaztrir.** (languageID `qau`)  
  The note in Urvanian, the sender's language: How it was made.
- `Note` = **Automatic report from the sender's tracking system.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: How it was made.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do, with the slot it is about.
- `TransportExecutionStatusCode` = **INPROGRESS** (listID `urn:ubl-examples:world:codelist:TransportExecutionStatusCode`)  
  The carriage is under way. The code is from the Trade Accord's transport execution status list: INPROGRESS = In progress.

### Consignment

Inside `Consignment`:

- `ID` = **7300043586**  
  The consignment the report is about.
- `CarrierParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Rail Cargo gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; as Ferrano Rail Cargo gives it.
- `CarrierParty/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `CarrierParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `CarrierParty/PostalAddress/ID` = **4170201115930918** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `CarrierParty/PostalAddress/StreetName` = **Rumir Hekrul Zhuzkek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/StreetName` = **Viale della Stazione** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. As Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). As Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Rail Cargo gives it.
- `CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `CarrierParty/Contact/Name` = **Freight desk**  
  The party's main desk, which handles this document; as Ferrano Rail Cargo gives it.
- `CarrierParty/Contact/JobTitle` = **Freight planner**  
  The job of the person who answers at the desk; as Ferrano Rail Cargo gives it.
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; as Ferrano Rail Cargo gives it.
- `CarrierParty/Contact/Telephone` = **+999 1 0413 67100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Rail Cargo gives it.
- `CarrierParty/Contact/ElectronicMail` = **freight@ferranorail.example**  
  The contact's e-mail address; as Ferrano Rail Cargo gives it.
- `CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Ferrano Rail Cargo gives it.
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Rail Cargo gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **2**  
  The main carriage, by rail.
- `MainCarriageShipmentStage/TransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train the boxes were loaded on.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/OccurrenceDate` = **2026-04-14**  
  If the morning train cannot leave, the boxes go on the evening train.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/OccurrenceTime` = **17:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/DeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  Planned placement at the siding.
- `MainCarriageShipmentStage/DeliveryTransportEvent/OccurrenceTime` = **11:00:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/DeliveryTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/DeliveryTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `MainCarriageShipmentStage/DeliveryTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Intermodal Hub gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Ferrano Intermodal Hub**  
  The trading name; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/ID` = **4160200139820702** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Bek Han Krazhul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Via del Terminal** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **59**  
  Building number of the postal address. As Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/PostalZone` = **4180**  
  Postal code in Urvania's format (4 digits). As Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Terminal control**  
  The party's main desk, which handles this document; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Terminal controller**  
  The job of the person who answers at the desk; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 1 041 371 6482**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **terminal@ferranohub.example**  
  The contact's e-mail address; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Ferrano Intermodal Hub gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105096** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Intermodal Hub gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/TransportEvent/OccurrenceDate` = **2026-04-14**  
  Both boxes lifted onto the train, the second at 05:55.
- `MainCarriageShipmentStage/TransportEvent/OccurrenceTime` = **05:40:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/TransportEvent/TransportEventTypeCode` = **LOADING** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: LOADING = Loaded.
- `MainCarriageShipmentStage/TransportEvent/CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/TransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/TransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `MainCarriageShipmentStage/TransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/ID` = **1**  
  The pre-carriage: the carrier's tractor brings the packed boxes to the hub.
- `PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **37** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container tractor for carrier haulage; the fleet of Ferrano Rail Cargo. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 37 = Truck, container.
- `PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 RC** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Ferrano Rail Cargo. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `PreCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/LoadingPortLocation/Name` = **Castrano Logistics warehouse, Conciaro**  
  Where the boxes are collected.
- `PreCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/UnloadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/UnloadingPortLocation/Name` = **Ferrano Intermodal Hub**  
  Where they are handed to the terminal.
- `PreCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/ActualPickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  The carrier's tractor collected the first box at the warehouse; the second followed at 15:00.
- `PreCarriageShipmentStage/ActualPickupTransportEvent/OccurrenceTime` = **13:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `PreCarriageShipmentStage/ActualPickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/ActualPickupTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `PreCarriageShipmentStage/ActualPickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PreCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceDate` = **2026-04-13**  
  The second box came in at the hub's gate, the end of the haulage.
- `PreCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceTime` = **15:50:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `PreCarriageShipmentStage/ActualArrivalTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PreCarriageShipmentStage/ActualArrivalTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `PreCarriageShipmentStage/ActualArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `TransportHandlingUnit/TransportEquipment/ID` = **FRXU1044175** (schemeID `ISO6346`)  
  A box the report is about.
- `TransportHandlingUnit/TransportEquipment/ID` = **FRXU1044180** (schemeID `ISO6346`)  
  A box the report is about.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-04-14**  
  The day the event took place.
- `TransportEventTypeCode` = **LOADING** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: LOADING = Loaded.
- `Description` = **Two containers loaded on the container train.**  
  What happened, in words.
- `Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Location/Name` = **Ferrano Intermodal Hub**  
  Where it happened.

### Signature

Inside `Signature`:

- `ID` = **FIH-SIG-TS-07**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Intermodal Hub**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Intermodal Hub**  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.

### Transport Execution Plan Document Reference

Inside `TransportExecutionPlanDocumentReference`:

- `ID` = **9500055446**  
  The plan the carriage follows.

### Status Location

Inside `StatusLocation`:

- `ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Name` = **Ferrano Intermodal Hub**  
  Where it happened.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-04-14**  
  The status holds from the report.
- `EndDate` = **2026-04-14**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:transportation-status:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900043586</cbc:ProfileExecutionID>
  <cbc:ID>FIH-TS-26-11316</cbc:ID>
  <cbc:UUID>514b9478-0214-5ce0-9018-7c4cf752cbd3</cbc:UUID>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>06:05:00-01:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Two containers loaded on the container train.</cbc:Description>
  <cbc:Note languageID="qau">Krerdan skuskek mir drek stalkan sazhir kaztrir.</cbc:Note>
  <cbc:Note languageID="en-XU">Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode listID="urn:ubl-examples:world:codelist:TransportExecutionStatusCode">INPROGRESS</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>7300043586</cbc:ID>
    <cac:CarrierParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4170201115930918</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Rumir Hekrul Zhuzkek</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Viale della Stazione</cbc:StreetName>
        <cbc:BuildingNumber>38</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
        <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
        <cbc:PostalZone>4310</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Freight desk</cbc:Name>
        <cbc:JobTitle>Freight planner</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 1 0413 67100</cbc:Telephone>
        <cbc:ElectronicMail>freight@ferranorail.example</cbc:ElectronicMail>
        <cbc:Note>Every day 06:00–22:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>2</cbc:ID>
      <cac:TransportMeans>
        <cac:RailTransport>
          <cbc:TrainID>FRC 4417</cbc:TrainID>
        </cac:RailTransport>
      </cac:TransportMeans>
      <cac:OptionalTakeoverTransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>17:00:00-01:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:OptionalTakeoverTransportEvent>
      <cac:DeliveryTransportEvent>
        <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>11:00:00-01:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
          <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
        </cac:Location>
      </cac:DeliveryTransportEvent>
      <cac:TerminalOperatorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">qau</cbc:ID>
          <cbc:Name>Urvanian</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200139820702</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qau">Bek Han Krazhul</cbc:StreetName>
          <cbc:StreetName languageID="en-XU">Via del Terminal</cbc:StreetName>
          <cbc:BuildingNumber>59</cbc:BuildingNumber>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
          <cbc:PostalZone>4180</cbc:PostalZone>
          <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
          <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Terminal control</cbc:Name>
          <cbc:JobTitle>Terminal controller</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 041 371 6482</cbc:Telephone>
          <cbc:ElectronicMail>terminal@ferranohub.example</cbc:ElectronicMail>
          <cbc:Note>Every day, around the clock</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105096</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
      <cac:TransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>05:40:00-01:00</cbc:OccurrenceTime>
        <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">LOADING</cbc:TransportEventTypeCode>
        <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:TransportEvent>
    </cac:MainCarriageShipmentStage>
    <cac:PreCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">37</cbc:TransportMeansTypeCode>
        <cac:RoadTransport>
          <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 RC</cbc:LicensePlateID>
        </cac:RoadTransport>
      </cac:TransportMeans>
      <cac:LoadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:LoadingPortLocation>
      <cac:UnloadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:UnloadingPortLocation>
      <cac:ActualPickupTransportEvent>
        <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>13:00:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualPickupTransportEvent>
      <cac:ActualArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>15:50:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualArrivalTransportEvent>
    </cac:PreCarriageShipmentStage>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">FRXU1044175</cbc:ID>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">FRXU1044180</cbc:ID>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
    <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">LOADING</cbc:TransportEventTypeCode>
    <cbc:Description>Two containers loaded on the container train.</cbc:Description>
    <cac:Location>
      <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
      <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:Signature>
    <cbc:ID>FIH-SIG-TS-07</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:TransportExecutionPlanDocumentReference>
    <cbc:ID>9500055446</cbc:ID>
  </cac:TransportExecutionPlanDocumentReference>
  <cac:StatusLocation>
    <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
    <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-04-14</cbc:StartDate>
    <cbc:EndDate>2026-04-14</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
