# Transportation Status: Tidewell Ocean Lines to Hafefo Fresh Produce

*Example 10 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The carrier reports the reefer discharged at Selanu and on the port's power, with the temperatures its monitoring recorded at sea.

[The XML file](10-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:transportation-status:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Transportation status". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TOL-TS-26-0565**  
  The sender's status report number.
- `UUID` = **8a5ddf6d-b855-5fa3-9a91-f88a50a3daf6**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-26**  
  Reported when the reefer is discharged and plugged in.
- `IssueTime` = **07:45:00-01:00**  
  Sent from the carrier's system in Lumeport once the reefer was plugged in: 08:45 at Selanu; in the issuer's local time, with its offset from UTC.

### Consignment

Inside `Consignment`:

- `ID` = **HFG-CS-26-0557**  
  The consignment the report is about.
- `ConsigneeParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Hafefo Fresh Produce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-043529** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `ConsigneeParty/Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `ConsigneeParty/PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ConsigneeParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Hafefo Fresh Produce gives it.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `ConsigneeParty/Contact/Name` = **Cold store**  
  The party's cold store desk: the desk for its role in this document (it receives the goods); as Hafefo Fresh Produce gives it.
- `ConsigneeParty/Contact/JobTitle` = **Cold store supervisor**  
  The job of the person who answers at the desk; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/Contact/Department` = **Cold store**  
  The department the desk belongs to; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Hafefo Fresh Produce gives it.
- `ConsigneeParty/Contact/ElectronicMail` = **coldstore@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; as Hafefo Fresh Produce gives it.
- `ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XL:IC43529** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Hafefo Fresh Produce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `CarrierParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; as Tidewell Ocean Lines gives it.
- `CarrierParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `CarrierParty/Language/Name` = **English**  
  The language's name.
- `CarrierParty/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `CarrierParty/PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `CarrierParty/PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `CarrierParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Tidewell Ocean Lines gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CarrierParty/Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/Department` = **Bookings**  
  The department the desk belongs to; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Tidewell Ocean Lines gives it.
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **2**  
  The sea leg, stage 2 as on the bill of lading.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-04-26**  
  The reefer came off the ship, among the first boxes.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **08:10:00**  
  The local time.
- `MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceDate` = **2026-04-26**  
  The ship berthed at Selanu at first light: its pilot boarded at dawn; it had been off the port since the evening.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceTime` = **06:40:00**  
  The local time.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU5316047** (schemeID `ISO6346`)  
  The reefer.
- `TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  Its refrigeration running again on the port's power.
- `TransportHandlingUnit/TransportEquipment/StorageLocation/ID` = **XLSEL-RR-07**  
  The power point in the port's reefer rack where the reefer stands until it is collected.
- `TransportHandlingUnit/TransportEquipment/StorageLocation/Name` = **Reefer rack, power point 7**  
  In words.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/OccurrenceDate` = **2026-04-26**  
  Plugged in at the reefer rack, fifteen minutes after discharge.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/OccurrenceTime` = **08:25:00**  
  The local time.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/TransportEventTypeCode` = **STORAGE** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: STORAGE = Stored.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/ConditionCode` = **COMPLETED** (listID `urn:ubl-examples:world:codelist:StatusConditionCode`)  
  The voyage is over. The code is from the Trade Accord's status condition list: COMPLETED = Completed.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/Description` = **The reefer's own log, read by the carrier's monitoring at sea, over the voyage from loading at Lumeport to discharge.**  
  What the readings cover.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/Condition/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The air the reefer blows into its cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/Condition/Measure` = **0.5** (unitCode `CEL`)  
  The average over the voyage: the set point.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/Condition/Description` = **Supply air, every hour of the voyage.**  
  The readings.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/Condition/MinimumMeasure` = **0.2** (unitCode `CEL`)  
  The lowest reading.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/CurrentStatus/Condition/MaximumMeasure` = **0.9** (unitCode `CEL`)  
  The highest, while the reefer was off power between the quay and the ship.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-04-26**  
  The day the event took place.
- `TransportEventTypeCode` = **DISCHARGE** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: DISCHARGE = Discharged.
- `Description` = **Reefer TWLU5316047 discharged and on the port's power; released by customs.**  
  What happened, in words.
- `Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Location/Name` = **Port of Selanu**  
  Where it happened.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at Consignment/ConsigneeParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Hafefo Fresh Produce**  
  The same party as at Consignment/ConsigneeParty, where its full details are given; only its identifier and name are repeated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:transportation-status:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TOL-TS-26-0565</cbc:ID>
  <cbc:UUID>8a5ddf6d-b855-5fa3-9a91-f88a50a3daf6</cbc:UUID>
  <cbc:IssueDate>2026-04-26</cbc:IssueDate>
  <cbc:IssueTime>07:45:00-01:00</cbc:IssueTime>
  <cac:Consignment>
    <cbc:ID>HFG-CS-26-0557</cbc:ID>
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
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
      </cac:Language>
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
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC43529</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:ConsigneeParty>
    <cac:CarrierParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-547539</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Harbour Road</cbc:StreetName>
        <cbc:BuildingNumber>18</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38527</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Bookings</cbc:Name>
        <cbc:JobTitle>Booking agent</cbc:JobTitle>
        <cbc:Department>Bookings</cbc:Department>
        <cbc:Telephone>+999 2 38 2058 7929</cbc:Telephone>
        <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
        <cbc:Note>Every day 06:00–22:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>2</cbc:ID>
      <cac:DischargeTransportEvent>
        <cbc:OccurrenceDate>2026-04-26</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>08:10:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:DischargeTransportEvent>
      <cac:ActualArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-04-26</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>06:40:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualArrivalTransportEvent>
    </cac:MainCarriageShipmentStage>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU5316047</cbc:ID>
        <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
        <cac:StorageLocation>
          <cbc:ID>XLSEL-RR-07</cbc:ID>
          <cbc:Name>Reefer rack, power point 7</cbc:Name>
        </cac:StorageLocation>
        <cac:TransportEvent>
          <cbc:OccurrenceDate>2026-04-26</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>08:25:00</cbc:OccurrenceTime>
          <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">STORAGE</cbc:TransportEventTypeCode>
          <cac:CurrentStatus>
            <cbc:ConditionCode listID="urn:ubl-examples:world:codelist:StatusConditionCode">COMPLETED</cbc:ConditionCode>
            <cbc:Description>The reefer's own log, read by the carrier's monitoring at sea, over the voyage from loading at Lumeport to discharge.</cbc:Description>
            <cac:Condition>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">0.5</cbc:Measure>
              <cbc:Description>Supply air, every hour of the voyage.</cbc:Description>
              <cbc:MinimumMeasure unitCode="CEL">0.2</cbc:MinimumMeasure>
              <cbc:MaximumMeasure unitCode="CEL">0.9</cbc:MaximumMeasure>
            </cac:Condition>
          </cac:CurrentStatus>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
            <cbc:Name>Port of Selanu</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:TransportEvent>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-04-26</cbc:OccurrenceDate>
    <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">DISCHARGE</cbc:TransportEventTypeCode>
    <cbc:Description>Reefer TWLU5316047 discharged and on the port's power; released by customs.</cbc:Description>
    <cac:Location>
      <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
      <cbc:Name>Port of Selanu</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Hafefo Fresh Produce</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
</TransportationStatus>
```
