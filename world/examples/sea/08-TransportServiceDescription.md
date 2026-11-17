# Transport Service Description: Tidewell Ocean Lines to Lumeway Distribution

*Example 8 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Transport Service Description in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORT-SERVICE-DESCRIPTION-SCHEMA)*

The ocean carrier describes its weekly service to Selanu.

[The XML file](08-TransportServiceDescription.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:transport-service-description:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Transport service description"; the community specification "Lumeport port community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TOL-DOC-26-0130**  
  The sender's number for this document.
- `UUID` = **bee924a8-76e1-5c8f-be45-927bde1567a4**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-09**  
  The carrier answers the next day.
- `IssueTime` = **12:03:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Our island service.**  
  What follows.
- `ServiceName` = **Island feeder**  
  The service's name.
- `ResponseCode` = **OFFERED** (listID `urn:ubl-examples:world:codelist:ServiceOfferResponseCode`)  
  The service is offered. The code is from the Trade Accord's service offer response list: OFFERED = Service offered.

### Signature

Inside `Signature`:

- `ID` = **TWL-SIG-TSD**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Department` = **Bookings**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2418 1918**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **logistics@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport Service Description Request Document Reference

Inside `TransportServiceDescriptionRequestDocumentReference`:

- `ID` = **LD-DOC-26-0129**  
  The request answered.

### Transport Service Provider Party

Inside `TransportServiceProviderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Service Charge Payment Terms

Inside `ServiceChargePaymentTerms`:

- `Note` = **Freight prepaid before the bill of lading is released.**  
  When the freight is paid.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-05-09**  
  From now.
- `EndDate` = **2026-08-07**  
  For three months.

### Transportation Service

Inside `TransportationService`:

- `TransportServiceCode` = **OCEANCONT** (listID `urn:ubl-examples:world:codelist:TransportServiceCode`)  
  The service, as a code of the Trade Accord's transport services. The code is from the Trade Accord's transport service list: OCEANCONT = Container liner service.
- `TariffClassCode` = **FAK** (listID `urn:ubl-examples:world:codelist:TariffClassCode`)  
  Freight all kinds: one rate whatever the goods. The code is from the Trade Accord's tariff class list: FAK = Freight all kinds.
- `Priority` = **Standard**  
  The normal service.
- `FreightRateClassCode` = **BOX** (listID `urn:ubl-examples:world:codelist:FreightRateClassCode`)  
  The rate is per container. The code is from the Trade Accord's freight rate class list: BOX = Rate per container.
- `TransportationServiceDescription` = **A weekly feeder sailing from Lumeport to Selanu, two days at sea.**  
  The service in words.
- `TransportationServiceDetailsURI` = **https://www.tidewell.example/services/island**  
  Where the schedule is.
- `NominationDate` = **2026-05-09**  
  The day the service is offered for this shipment.
- `NominationTime` = **10:00:00**  
  In the morning.
- `Name` = **Weekly service Lumeport–Selanu**  
  The name of the service.
- `SequenceNumeric` = **1**  
  The first of the services offered.
- `TransportEquipment/SizeTypeCode` = **42G1** (listID `ISO 6346`)  
  The equipment offered for this shipment: a 40-foot dry container. The code is from the world's copy of ISO 6346 container size and type code: 42G1 = 40 ft, 8 ft 6 in high, general purpose.
- `SupportedTransportEquipment/SizeTypeCode` = **22G1** (listID `ISO 6346`)  
  A 20-foot dry container, as an ISO 6346 size and type: the size type says what equipment is meant, so no identifier is given. The code is from the world's copy of ISO 6346 container size and type code: 22G1 = 20 ft, 8 ft 6 in high, general purpose.
- `SupportedTransportEquipment/SizeTypeCode` = **42G1** (listID `ISO 6346`)  
  A 40-foot dry container, as an ISO 6346 size and type. The code is from the world's copy of ISO 6346 container size and type code: 42G1 = 40 ft, 8 ft 6 in high, general purpose.
- `UnsupportedTransportEquipment/SizeTypeCode` = **45R1** (listID `ISO 6346`)  
  A 40-foot reefer, as an ISO 6346 size and type: the island port has no reefer plugs. The code is from the world's copy of ISO 6346 container size and type code: 45R1 = 40 ft, 9 ft 6 in high, thermal, refrigerated and heated.
- `CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  The benches, as a subclass of the UN Central Product Classification: seats with metal frames. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `SupportedCommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  General cargo in containers. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `UnsupportedCommodityClassification/CargoTypeCode` = **BULK** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  No loose bulk on this service. The code is from the Trade Accord's cargo type list: BULK = Dry bulk.
- `TotalCapacityDimension/AttributeID` = **TEU** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The ship's capacity in twenty-foot units. The code is from the Trade Accord's attribute list: TEU = Container capacity. An identifier that holds a code names the code's list in its schemeID.
- `TotalCapacityDimension/Measure` = **1000** (unitCode `20`)  
  One thousand twenty-foot units (unit 20: twenty foot container).
- `ShipmentStage/ID` = **1**  
  Lumeport to Selanu.
- `ShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `TransportEvent/OccurrenceDate` = **2026-05-14**  
  The next departure from Lumeport.
- `TransportEvent/OccurrenceTime` = **18:00:00**  
  The local time.
- `TransportEvent/TransportEventTypeCode` = **DEPARTURE** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: DEPARTURE = Departure.
- `TransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `TransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `TransportEvent/Location/Name` = **Port of Lumeport**  
  The port the service sails from.
- `TransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ResponsibleTransportServiceProviderParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ResponsibleTransportServiceProviderParty/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.
- `EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Greenhouse gases. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `EnvironmentalEmission/ValueMeasure` = **380** (unitCode `KGM`)  
  Per 40-foot container on the crossing.
- `EstimatedDurationPeriod/DurationMeasure` = **2** (unitCode `DAY`)  
  Two days at sea.
- `ScheduledServiceFrequency/WeekDayCode` = **5** (listID `urn:oasis:names:specification:ubl:codelist:gc:WeekDayCode`)  
  Every Friday (ISO 8601: 5 is Friday). The code is from the world's copy of UBL's Week day list, with a listID: 5 = Friday.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportServiceDescription xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportServiceDescription-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:transport-service-description:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TOL-DOC-26-0130</cbc:ID>
  <cbc:UUID>bee924a8-76e1-5c8f-be45-927bde1567a4</cbc:UUID>
  <cbc:IssueDate>2026-05-09</cbc:IssueDate>
  <cbc:IssueTime>12:03:00</cbc:IssueTime>
  <cbc:Note>Our island service.</cbc:Note>
  <cbc:ServiceName>Island feeder</cbc:ServiceName>
  <cbc:ResponseCode listID="urn:ubl-examples:world:codelist:ServiceOfferResponseCode">OFFERED</cbc:ResponseCode>
  <cac:Signature>
    <cbc:ID>TWL-SIG-TSD</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
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
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Bookings</cbc:Name>
      <cbc:JobTitle>Booking agent</cbc:JobTitle>
      <cbc:Department>Bookings</cbc:Department>
      <cbc:Telephone>+999 2 38 2418 1918</cbc:Telephone>
      <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
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
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
      <cbc:ElectronicMail>logistics@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:TransportServiceDescriptionRequestDocumentReference>
    <cbc:ID>LD-DOC-26-0129</cbc:ID>
  </cac:TransportServiceDescriptionRequestDocumentReference>
  <cac:TransportServiceProviderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:TransportServiceProviderParty>
  <cac:ServiceChargePaymentTerms>
    <cbc:Note>Freight prepaid before the bill of lading is released.</cbc:Note>
  </cac:ServiceChargePaymentTerms>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-05-09</cbc:StartDate>
    <cbc:EndDate>2026-08-07</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:TransportationService>
    <cbc:TransportServiceCode listID="urn:ubl-examples:world:codelist:TransportServiceCode">OCEANCONT</cbc:TransportServiceCode>
    <cbc:TariffClassCode listID="urn:ubl-examples:world:codelist:TariffClassCode">FAK</cbc:TariffClassCode>
    <cbc:Priority>Standard</cbc:Priority>
    <cbc:FreightRateClassCode listID="urn:ubl-examples:world:codelist:FreightRateClassCode">BOX</cbc:FreightRateClassCode>
    <cbc:TransportationServiceDescription>A weekly feeder sailing from Lumeport to Selanu, two days at sea.</cbc:TransportationServiceDescription>
    <cbc:TransportationServiceDetailsURI>https://www.tidewell.example/services/island</cbc:TransportationServiceDetailsURI>
    <cbc:NominationDate>2026-05-09</cbc:NominationDate>
    <cbc:NominationTime>10:00:00</cbc:NominationTime>
    <cbc:Name>Weekly service Lumeport–Selanu</cbc:Name>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cac:TransportEquipment>
      <cbc:SizeTypeCode listID="ISO 6346">42G1</cbc:SizeTypeCode>
    </cac:TransportEquipment>
    <cac:SupportedTransportEquipment>
      <cbc:SizeTypeCode listID="ISO 6346">22G1</cbc:SizeTypeCode>
    </cac:SupportedTransportEquipment>
    <cac:SupportedTransportEquipment>
      <cbc:SizeTypeCode listID="ISO 6346">42G1</cbc:SizeTypeCode>
    </cac:SupportedTransportEquipment>
    <cac:UnsupportedTransportEquipment>
      <cbc:SizeTypeCode listID="ISO 6346">45R1</cbc:SizeTypeCode>
    </cac:UnsupportedTransportEquipment>
    <cac:CommodityClassification>
      <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
    </cac:CommodityClassification>
    <cac:SupportedCommodityClassification>
      <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
    </cac:SupportedCommodityClassification>
    <cac:UnsupportedCommodityClassification>
      <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">BULK</cbc:CargoTypeCode>
    </cac:UnsupportedCommodityClassification>
    <cac:TotalCapacityDimension>
      <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">TEU</cbc:AttributeID>
      <cbc:Measure unitCode="20">1000</cbc:Measure>
    </cac:TotalCapacityDimension>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
    </cac:ShipmentStage>
    <cac:TransportEvent>
      <cbc:OccurrenceDate>2026-05-14</cbc:OccurrenceDate>
      <cbc:OccurrenceTime>18:00:00</cbc:OccurrenceTime>
      <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">DEPARTURE</cbc:TransportEventTypeCode>
      <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
      <cac:Location>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Port of Lumeport</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:Location>
    </cac:TransportEvent>
    <cac:ResponsibleTransportServiceProviderParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
    </cac:ResponsibleTransportServiceProviderParty>
    <cac:EnvironmentalEmission>
      <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
      <cbc:ValueMeasure unitCode="KGM">380</cbc:ValueMeasure>
    </cac:EnvironmentalEmission>
    <cac:EstimatedDurationPeriod>
      <cbc:DurationMeasure unitCode="DAY">2</cbc:DurationMeasure>
    </cac:EstimatedDurationPeriod>
    <cac:ScheduledServiceFrequency>
      <cbc:WeekDayCode listID="urn:oasis:names:specification:ubl:codelist:gc:WeekDayCode">5</cbc:WeekDayCode>
    </cac:ScheduledServiceFrequency>
  </cac:TransportationService>
</TransportServiceDescription>
```
