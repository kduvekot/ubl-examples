# Utility Statement: Ferrano Grid to Ferrano Energy

*Example 1 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The grid operator reads the factory's gas meter and sends the retail company the consumption: the volume at line pressure, converted to standard cubic metres and to energy.

[The XML file](01-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:utility-statement:1.0#compliant#urn:ubl-examples:world:community:energy-xu:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Utility statement"; the community specification "Urvania energy market". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **FGR-TX-26-0151**  
  The collaboration this document belongs to: Ferrano Grid's network bill for March to Ferrano Energy. Ferrano Grid started it and gave it this identifier, which every document of it repeats.
- `ID` = **FGR-UST-26-2253**  
  The grid operator's metering report.
- `UUID` = **4dda14a2-d50d-5ef3-84d8-980f6cc7eedb**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Sent with the month's network invoice on Thursday 2 April, once the readings of 31 March are checked.
- `IssueTime` = **08:20:00-01:00**  
  Issued in the same billing run as the network invoice it supplements, each citing the other, and before the retail company bills the gas by it; in the issuer's local time, with its offset from UTC.
- `UtilityStatementTypeCode` = **GAS** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: GAS = Gas.
- `Note` = **Bazbaz binmaz gan drek stekraz nalbaz sidir; drek zhek trizhul trul stan huldan drek geltaz.** (languageID `qau`)  
  The note in Urvanian, the sender's language: What the statement is.
- `Note` = **Metered consumption for the retail company's billing; the grid operator owns and reads the meter.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What the statement is.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, Urvania's currency; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **2026/0157**  
  The network invoice this statement supplements: the metering behind the network charge for gas.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 2026/0157 is the example energy/02, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-106055** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Grid gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:16043** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Ferrano Grid gives it.
- `PartyName/Name` = **Ferrano Grid**  
  The trading name; as Ferrano Grid gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4160202321763926** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Grid gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Hekrul Skaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Grid gives it.
- `PostalAddress/StreetName` = **Via della Rete** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Grid gives it.
- `PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. As Ferrano Grid gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Grid gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Grid gives it.
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). As Ferrano Grid gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Grid gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Network billing**  
  The party's network billing desk: the desk for its role in this document (it is owed the payment); as Ferrano Grid gives it.
- `Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Ferrano Grid gives it.
- `Contact/Department` = **Finance**  
  The department the desk belongs to; as Ferrano Grid gives it.
- `Contact/Telephone` = **+999 1 041 938 7117**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0425 and 5 digits (9); no area code is the start of another. Mobiles start with 3 and have 10 digits. As Ferrano Grid gives it.
- `Contact/ElectronicMail` = **billing@ferranogrid.example**  
  The contact's e-mail address; as Ferrano Grid gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Ferrano Grid gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-106055** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Grid gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Energy gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Energy**  
  The trading name; as Ferrano Energy gives it.
- `PostalAddress/ID` = **4160202777983743** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Energy gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Duznaz Hekrul Skultrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Energy gives it.
- `PostalAddress/StreetName` = **Corso della Repubblica** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Energy gives it.
- `PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Ferrano Energy gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Energy gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Energy gives it.
- `PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). As Ferrano Energy gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Energy gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Ferrano Energy gives it.
- `Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Ferrano Energy gives it.
- `Contact/Department` = **Finance**  
  The department the desk belongs to; as Ferrano Energy gives it.
- `Contact/Telephone` = **+999 1 041 474 7922**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0425 and 5 digits (9); no area code is the start of another. Mobiles start with 3 and have 10 digits. As Ferrano Energy gives it.
- `Contact/ElectronicMail` = **payables@ferranoenergy.example**  
  The contact's e-mail address; as Ferrano Energy gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Ferrano Energy gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Energy gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **FGR-CP-4120-G1-2603**  
  The consumption of the factory's gas point in March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  With the volume conversion. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **Gas for the coating ovens of the factory.**  
  The point.
- `TotalMeteredQuantity` = **1350** (unitCode `MTQ`)  
  Cubic metres through the meter at line pressure.
- `UtilityConsumptionPoint/ID` = **FGR-CP-4120-G1**  
  The factory's gas connection.
- `UtilityConsumptionPoint/Description` = **Valdara Industries, gas connection of the coating line**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **FE-CU-0381206**  
  The subscriber's customer number with the retail company, by which the grid operator reports to it; the gas contract stays in the contract.
- `UtilityConsumptionPoint/SubscriberType` = **Industrial**  
  The name of code IND in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **IND** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: IND = Industrial.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **61200** (unitCode `KWH`)  
  Delivered in March, as energy.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `UtilityConsumptionPoint/Address/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `UtilityConsumptionPoint/Address/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **FGR-G-20417**  
  The gas meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Rotary gas meter, coating line**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  Read directly.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **DIRECT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  No multiplier. The code is from the Trade Accord's meter constant type list: DIRECT = Direct connection.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **1350** (unitCode `MTQ`)  
  Through the meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **FGR-G-20417-2603**  
  The reading of March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2026-02-28**  
  The previous reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **28410** (unitCode `MTQ`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **29760** (unitCode `MTQ`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Remote reading**  
  The name of code REMOTE in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **REMOTE** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: REMOTE = Remote reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **1350** (unitCode `MTQ`)  
  The difference.
- `Consumption/UtilityStatementTypeCode` = **GAS** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: GAS = Gas.
- `Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its end.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **FGR-CP-4120-G1-2603**  
  The report.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Monthly consumption**  
  What it is.
- `Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **61200** (unitCode `KWH`)  
  Energy in March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2026-03-01**  
  March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  Its end.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionType` = **Volume conversion**  
  The name of code CONV in the Trade Accord's consumption correction type list.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionTypeCode` = **CONV** (listID `urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption correction type list: CONV = Volume conversion.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/MeterNumber` = **FGR-G-20417**  
  The meter.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/GasPressureQuantity` = **4** (unitCode `BAR`)  
  The meter runs at 4 bar above the atmosphere: the gas is compressed, so the volume is corrected for the pressure.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/Description` = **1350 m³ at line pressure × 4.9477 (pressure) = 6679 m³ at standard conditions, × 9.163 kWh/m³ (calorific value of March) = 61200 kWh.**  
  The conversion, whose result is the consumption report's energy.
- `Consumption/LegalMonetaryTotal/LineExtensionAmount` = **116280** (currencyID `XUF`)  
  61200 kWh at the gas network tariff of 1.9 ferra: line 3 of the network invoice.
- `Consumption/LegalMonetaryTotal/TaxExclusiveAmount` = **116280** (currencyID `XUF`)  
  Without the value added tax.
- `Consumption/LegalMonetaryTotal/TaxInclusiveAmount` = **139536** (currencyID `XUF`)  
  With 20 % value added tax.
- `Consumption/LegalMonetaryTotal/PayableAmount` = **139536** (currencyID `XUF`)  
  What the network invoice charges the retail company for this consumption.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:utility-statement:1.0#compliant#urn:ubl-examples:world:community:energy-xu:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>FGR-TX-26-0151</cbc:ProfileExecutionID>
  <cbc:ID>FGR-UST-26-2253</cbc:ID>
  <cbc:UUID>4dda14a2-d50d-5ef3-84d8-980f6cc7eedb</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>08:20:00-01:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">GAS</cbc:UtilityStatementTypeCode>
  <cbc:Note languageID="qau">Bazbaz binmaz gan drek stekraz nalbaz sidir; drek zhek trizhul trul stan huldan drek geltaz.</cbc:Note>
  <cbc:Note languageID="en-XU">Metered consumption for the retail company's billing; the grid operator owns and reads the meter.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cac:ParentDocumentReference>
    <cbc:ID>2026/0157</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:ParentDocumentReference>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106055</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:16043</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Grid</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202321763926</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Hekrul Skaz</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via della Rete</cbc:StreetName>
      <cbc:BuildingNumber>3</cbc:BuildingNumber>
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
    <cac:Contact>
      <cbc:Name>Network billing</cbc:Name>
      <cbc:JobTitle>Billing officer</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 1 041 938 7117</cbc:Telephone>
      <cbc:ElectronicMail>billing@ferranogrid.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-106055</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Energy</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202777983743</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Duznaz Hekrul Skultrir</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Corso della Repubblica</cbc:StreetName>
      <cbc:BuildingNumber>9</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4150</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Accounts payable</cbc:Name>
      <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 1 041 474 7922</cbc:Telephone>
      <cbc:ElectronicMail>payables@ferranoenergy.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105781</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>FGR-CP-4120-G1-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>Gas for the coating ovens of the factory.</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="MTQ">1350</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>FGR-CP-4120-G1</cbc:ID>
      <cbc:Description>Valdara Industries, gas connection of the coating line</cbc:Description>
      <cbc:SubscriberID>FE-CU-0381206</cbc:SubscriberID>
      <cbc:SubscriberType>Industrial</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">IND</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="KWH">61200</cbc:TotalDeliveredQuantity>
      <cac:Address>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:Address>
      <cac:UtilityMeter>
        <cbc:MeterNumber>FGR-G-20417</cbc:MeterNumber>
        <cbc:MeterName>Rotary gas meter, coating line</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">DIRECT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="MTQ">1350</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>FGR-G-20417-2603</cbc:ID>
          <cbc:PreviousMeterReadingDate>2026-02-28</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="MTQ">28410</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="MTQ">29760</cbc:LatestMeterQuantity>
          <cbc:LatestMeterReadingMethod>Remote reading</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">REMOTE</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="MTQ">1350</cbc:DeliveredQuantity>
        </cac:MeterReading>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:Consumption>
      <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">GAS</cbc:UtilityStatementTypeCode>
      <cac:MainPeriod>
        <cbc:StartDate>2026-03-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:MainPeriod>
      <cac:EnergyWaterSupply>
        <cac:ConsumptionReport>
          <cbc:ID>FGR-CP-4120-G1-2603</cbc:ID>
          <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
          <cbc:TotalConsumedQuantity unitCode="KWH">61200</cbc:TotalConsumedQuantity>
          <cac:Period>
            <cbc:StartDate>2026-03-01</cbc:StartDate>
            <cbc:EndDate>2026-03-31</cbc:EndDate>
          </cac:Period>
        </cac:ConsumptionReport>
        <cac:EnergyWaterConsumptionCorrection>
          <cbc:CorrectionType>Volume conversion</cbc:CorrectionType>
          <cbc:CorrectionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode">CONV</cbc:CorrectionTypeCode>
          <cbc:MeterNumber>FGR-G-20417</cbc:MeterNumber>
          <cbc:GasPressureQuantity unitCode="BAR">4</cbc:GasPressureQuantity>
          <cbc:Description>1350 m³ at line pressure × 4.9477 (pressure) = 6679 m³ at standard conditions, × 9.163 kWh/m³ (calorific value of March) = 61200 kWh.</cbc:Description>
        </cac:EnergyWaterConsumptionCorrection>
      </cac:EnergyWaterSupply>
      <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="XUF">116280</cbc:LineExtensionAmount>
        <cbc:TaxExclusiveAmount currencyID="XUF">116280</cbc:TaxExclusiveAmount>
        <cbc:TaxInclusiveAmount currencyID="XUF">139536</cbc:TaxInclusiveAmount>
        <cbc:PayableAmount currencyID="XUF">139536</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:Consumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
