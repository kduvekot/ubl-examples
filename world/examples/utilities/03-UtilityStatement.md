# Utility Statement: Ferrano Energy to Castrano Logistics

*Example 3 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The warehouse is the manufacturer's building: the manufacturer owns it and holds the subscription, the 3PL operates the warehouse and receives the statement of its consumption point; the statement names the manufacturer as subscriber and customer.

[The XML file](03-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:utility-statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Utility statement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9909901005**  
  The collaboration this document belongs to: Ferrano Energy's bill for March to Valdara. Ferrano Energy started it and gave it this identifier, which every document of it repeats.
- `ID` = **9409901473**  
  The utility's statement number.
- `UUID` = **a67867a6-9a78-55a4-b129-4e9157f53cff**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **16:45:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `UtilityStatementTypeCode` = **ELEC** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of utility the statement is about. The code is from the Trade Accord's utility type list: ELEC = Electricity.
- `Note` = **Gir zharhan narmir drek binmaz vukrek taz rir.** (languageID `qau`)  
  The note in Urvanian, the sender's language: What the statement is.
- `Note` = **This statement explains the consumption behind your bill.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What the statement is.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, the utility's currency; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `AccountingCostCode` = **6300**  
  The customer's cost centre, as on the bill.
- `AccountingCost` = **Energy**  
  The cost centre in words.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **2026/313046**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 2026/313046 is the example utilities/02, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **FE-TARIFF-2026**  
  The utility's tariff sheet for 2026.
- `DocumentTypeCode` = **TARIFF** (listID `urn:ubl-examples:world:codelist:DocumentTypeCode`)  
  What the document is. The code is from the Trade Accord's document type list: TARIFF = Tariff.
- `DocumentDescription` = **Prices per unit and the terms of supply.**  
  What it holds.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Energy gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Energy**  
  The trading name; as Ferrano Energy gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
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

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Castrano Logistics gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10519** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Castrano Logistics gives it.
- `PartyName/Name` = **Castrano Logistics**  
  The trading name; as Castrano Logistics gives it.
- `PostalAddress/ID` = **4160203920705699** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Castrano Logistics gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Castrano Logistics gives it.
- `PostalAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Castrano Logistics gives it.
- `PostalAddress/BuildingNumber` = **24**  
  Building number of the postal address. As Castrano Logistics gives it.
- `PostalAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `PostalAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `PostalAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Castrano Logistics gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Castrano Logistics gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Castrano Logistics gives it.
- `Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Castrano Logistics gives it.
- `Contact/Department` = **Finance**  
  The department the desk belongs to; as Castrano Logistics gives it.
- `Contact/Telephone` = **+999 1 041 909 1454**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0425 and 5 digits (9); no area code is the start of another. Mobiles start with 3 and have 10 digits. As Castrano Logistics gives it.
- `Contact/ElectronicMail` = **payables@castrano.example**  
  The contact's e-mail address; as Castrano Logistics gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Castrano Logistics gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Castrano Logistics gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customer Party

Inside `CustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at CustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at CustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **FGR-CP-4160-E1-2603**  
  The consumption of the point in March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  A detailed specification. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **Warehouse of Castrano Logistics**  
  The point.
- `TotalMeteredQuantity` = **19350** (unitCode `KWH`)  
  Metered in March.
- `UtilityConsumptionPoint/ID` = **FGR-CP-4160-E1**  
  The connection, numbered by the grid operator, Ferrano Grid, which owns and reads the meters; the retail company uses its numbers, its own reference being the contract.
- `UtilityConsumptionPoint/Description` = **Warehouse of Castrano Logistics**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **FE-CU-0381206**  
  The subscriber's customer number with the utility; the contract number stays in the contract.
- `UtilityConsumptionPoint/SubscriberType` = **Commercial**  
  The name of code COM in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **COM** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: COM = Commercial.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **19350** (unitCode `KWH`)  
  Delivered in March.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `UtilityConsumptionPoint/Address/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/BuildingNumber` = **24**  
  Building number of the postal address. As Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Castrano Logistics gives it.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `UtilityConsumptionPoint/Address/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **FGR-E-20523**  
  The meter, numbered by the grid operator, Ferrano Grid, which owns and reads the meters; the retail company uses its numbers, its own reference being the contract.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Warehouse meter**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  The register is multiplied by this.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **DIRECT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  Why: direct. The code is from the Trade Accord's meter constant type list: DIRECT = Direct connection.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **19350** (unitCode `KWH`)  
  Delivered in March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **FGR-E-20523-2603**  
  The reading of March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Monthly reading**  
  The name of code M in the Trade Accord's meter reading type list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:MeterReadingTypeCode`)  
  As a code. The code is from the Trade Accord's meter reading type list: M = Monthly reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2026-02-28**  
  The previous reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **116500** (unitCode `KWH`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **135850** (unitCode `KWH`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Load profile: derived from the warehouse's load profile between the readings of 31 January and 31 March, in place of February's estimate of 117,250 kWh**  
  The name of code PROFILE in the Trade Accord's meter reading method list, followed by the detail of this case: from the utility's record of the reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **PROFILE** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: PROFILE = Load profile.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Read by the meter reader**  
  The name of code MANUAL in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **MANUAL** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: MANUAL = Read by the meter reader.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingComments` = **The previous reading replaces February's estimate of 117,250 kWh: February used 16,450 kWh, not the 17,200 kWh billed, and the 750 kWh are credited.**  
  Why the previous reading is not the one on February's statement.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **19350** (unitCode `KWH`)  
  The difference of the readings.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Accuracy class**  
  The name of code ACC in the Trade Accord's item property name list.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/NameCode` = **ACC** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  As a code. The code is from the Trade Accord's item property name list: ACC = Accuracy class.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Value` = **1**  
  Class 1.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQualifier` = **Calibrated 2024**  
  When it was checked.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Rated current**  
  A rating of the meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQuantity` = **5** (unitCode `AMP`)  
  Its value.
- `SupplierConsumption/Description` = **The energy, which Ferrano Energy supplies under the customer's contract.**  
  Whose supply this part is, and how it is billed.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Ferrano Energy**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/UtilityStatementTypeCode` = **ELEC** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: ELEC = Electricity.
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **11160** (currencyID `XUF`)  
  The energy tax on this point's electricity.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **11610** (currencyID `XUF`)  
  19350 kWh at 0.6 ferra.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  Per kilowatt hour.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/PerUnitAmount` = **0.6** (currencyID `XUF`)  
  The rate of the tier.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The energy tax applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Name` = **Energy tax**  
  The tax in words.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **EXC** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code EXC: excise duty, the energy tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: EXC = Excise duty. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **-450** (currencyID `XUF`)  
  -750 kWh at 0.6 ferra.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  Per kilowatt hour.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/PerUnitAmount` = **0.6** (currencyID `XUF`)  
  The rate of the tier.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TierRange` = **February's estimate correction: 750 kWh of the warehouse credited at the rate February's bill charged on them, the upper tier**  
  The kWh this subtotal credits.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The energy tax applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Name` = **Energy tax**  
  The tax in words.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **EXC** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code EXC: excise duty, the energy tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: EXC = Excise duty. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **80724** (currencyID `XUF`)  
  20 % value added tax on the energy and the energy tax.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **403620** (currencyID `XUF`)  
  The energy plus the energy tax.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **80724** (currencyID `XUF`)  
  20 % of it.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **FGR-CP-4160-E1-2603**  
  The consumption report of the point for March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Description` = **March consumption of Warehouse of Castrano Logistics.**  
  In words.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **19350** (unitCode `KWH`)  
  Used in March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/BasicConsumedQuantity` = **19350** (unitCode `KWH`)  
  All at the basic tariff: no reduced-rate hours.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionReportID` = **FGR-CP-4160-E1-2602**  
  The report of February.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/TotalConsumedQuantity` = **17200** (unitCode `KWH`)  
  What February's report said, from the estimated reading.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/StartDate` = **2026-02-01**  
  February.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/EndDate` = **2026-02-28**  
  Its last day.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **FGR-E-20523**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **17900** (unitCode `KWH`)  
  The month's consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **377690** (currencyID `XUF`)  
  What it cost at the supplier's own tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-01-01**  
  The month.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-01-31**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **FGR-E-20523**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **16450** (unitCode `KWH`)  
  The month's consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **347095** (currencyID `XUF`)  
  What it cost at the supplier's own tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Description` = **Corrected from the estimate of 17,200 kWh.**  
  Why February's figure differs from February's statement.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-02-01**  
  The month.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-02-28**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxEnergyAmount` = **11160** (currencyID `XUF`)  
  This point's share of the bill's energy tax: 19,350 kWh at 0.6 and -750 kWh at 0.6 ferra; the tiers apply to the customer's month as a whole, the lower tier counted on the main connection; the credit of February's estimate at the rate February charged.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxEnergyOnAccountAmount` = **0** (currencyID `XUF`)  
  No energy tax paid on account.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxEnergyBalanceAmount` = **11160** (currencyID `XUF`)  
  Due with this bill.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxScheme/ID` = **EXC** (schemeID `UN/EDIFACT EDED 5153`)  
  Urvania's energy tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: EXC = Excise duty. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/AverageAmount` = **377690** (currencyID `XUF`)  
  The average amount of the last three months at the supplier's own tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/Description` = **The average over the last three months is 17,900 kWh.**  
  For comparison.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionType` = **Estimate correction**  
  The name of code EST in the Trade Accord's consumption correction type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionTypeCode` = **EST** (listID `urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption correction type list: EST = Estimate correction.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/MeterNumber` = **FGR-E-20523**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/Description` = **February's reading was estimated at 117,250 kWh, as the meter could not be reached; the readings of 31 January and 31 March, split by the warehouse's load profile, put it at 116,500 kWh. February used 16,450 kWh, not the 17,200 kWh billed: the 750 kWh are credited on line 4 of the bill.**  
  Why and how.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **392460** (currencyID `XUF`)  
  The lines of this part, February's credit included.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **484344** (currencyID `XUF`)  
  With its taxes.
- `SupplierConsumption/Contract/ID` = **FE-C-0047120**  
  The supply contract.
- `SupplierConsumption/Contract/ContractType` = **Electricity supply**  
  Its kind.
- `SupplierConsumption/Contract/ValidityPeriod/StartDate` = **2024-01-01**  
  In force since.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **2**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **19350** (unitCode `KWH`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **408285** (currencyID `XUF`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **503874** (currencyID `XUF`)  
  With the energy tax and the value added tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **95589** (currencyID `XUF`)  
  The energy tax and the value added tax of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **FE-KWH-E**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **FE-CU-0381206**  
  The subscriber's customer number with the utility.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Commercial**  
  The name of code COM in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **COM** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: COM = Commercial.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Drek zikdrir skul drek zuktrek tazkraz, ginek zalhaz bantan: drek zhutek FE-KWH zentul drek gatir vatir skul drek zhek.** (languageID `qau`)  
  The tariff in words in Urvanian, the seller's language.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **The energy of the electricity supply, per kilowatt hour: the tariff FE-KWH without the network charge of the grid.** (languageID `en-XU`)  
  The tariff in words in English, the working language between the countries.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **FE-C-0047120**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **21.1** (currencyID `XUF`)  
  The tariff.
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `KWH`)  
  Per unit.
- `SupplierConsumption/ConsumptionLine/ID` = **2**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **4**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **-750** (unitCode `KWH`)  
  The kWh February's estimate charged too much, credited.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **-15825** (currencyID `XUF`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **-19530** (currencyID `XUF`)  
  With the energy tax and the value added tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-02-01**  
  February, the month the line corrects.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-02-28**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **-3705** (currencyID `XUF`)  
  The energy tax and the value added tax of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **FE-KWH-E**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **FE-CU-0381206**  
  The subscriber's customer number with the utility.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Commercial**  
  The name of code COM in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **COM** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: COM = Commercial.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Drek zikdrir skul drek zuktrek tazkraz, ginek zalhaz bantan: drek zhutek FE-KWH zentul drek gatir vatir skul drek zhek.** (languageID `qau`)  
  The tariff in words in Urvanian, the seller's language.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **The energy of the electricity supply, per kilowatt hour: the tariff FE-KWH without the network charge of the grid.** (languageID `en-XU`)  
  The tariff in words in English, the working language between the countries.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **FE-C-0047120**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **21.1** (currencyID `XUF`)  
  The tariff.
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `KWH`)  
  Per unit.
- `SupplierConsumption/Description` = **Ferrano Grid's network charges, which Ferrano Energy collects with its bill and pays to the grid.**  
  Whose supply this part is, and how it is billed.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **XU-R-106055** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Ferrano Grid**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/UtilityStatementTypeCode` = **ELEC** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: ELEC = Electricity.
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **23064** (currencyID `XUF`)  
  The tax of this part of the consumption.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **115320** (currencyID `XUF`)  
  The lines of this part.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **23064** (currencyID `XUF`)  
  20 % of them.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **115320** (currencyID `XUF`)  
  The lines of this part, February's credit included.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **138384** (currencyID `XUF`)  
  With its tax.
- `SupplierConsumption/ConsumptionLine/ID` = **3**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **2**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **19350** (unitCode `KWH`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **119970** (currencyID `XUF`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **143964** (currencyID `XUF`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **23994** (currencyID `XUF`)  
  20 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **FGR-NET-E**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Commercial**  
  The name of code COM in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **COM** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: COM = Commercial.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Krek skul drek zuktrek rirtan gatir, ginek zalhaz bantan kirhan hir drek trekstan.** (languageID `qau`)  
  The tariff in words in Urvanian, the seller's language.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Use of the electricity distribution network, per kilowatt hour taken at the connection.** (languageID `en-XU`)  
  The tariff in words in English, the working language between the countries.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **6.2** (currencyID `XUF`)  
  The tariff.
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `KWH`)  
  Per unit.
- `SupplierConsumption/ConsumptionLine/ID` = **4**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **4**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **-750** (unitCode `KWH`)  
  The kWh February's estimate charged too much, credited.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **-4650** (currencyID `XUF`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **-5580** (currencyID `XUF`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-02-01**  
  February, the month the line corrects.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-02-28**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **-930** (currencyID `XUF`)  
  20 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **FGR-NET-E**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Commercial**  
  The name of code COM in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **COM** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: COM = Commercial.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Krek skul drek zuktrek rirtan gatir, ginek zalhaz bantan kirhan hir drek trekstan.** (languageID `qau`)  
  The tariff in words in Urvanian, the seller's language.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Use of the electricity distribution network, per kilowatt hour taken at the connection.** (languageID `en-XU`)  
  The tariff in words in English, the working language between the countries.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **6.2** (currencyID `XUF`)  
  The tariff.
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `KWH`)  
  Per unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:utility-statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9909901005</cbc:ProfileExecutionID>
  <cbc:ID>9409901473</cbc:ID>
  <cbc:UUID>a67867a6-9a78-55a4-b129-4e9157f53cff</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>16:45:00-01:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">ELEC</cbc:UtilityStatementTypeCode>
  <cbc:Note languageID="qau">Gir zharhan narmir drek binmaz vukrek taz rir.</cbc:Note>
  <cbc:Note languageID="en-XU">This statement explains the consumption behind your bill.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>6300</cbc:AccountingCostCode>
  <cbc:AccountingCost>Energy</cbc:AccountingCost>
  <cac:ParentDocumentReference>
    <cbc:ID>2026/313046</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>FE-TARIFF-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentTypeCode">TARIFF</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Prices per unit and the terms of supply.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Energy</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
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
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10519</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Castrano Logistics</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160203920705699</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
      <cbc:BuildingNumber>24</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
      <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
      <cbc:PostalZone>4190</cbc:PostalZone>
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
      <cbc:Telephone>+999 1 041 909 1454</cbc:Telephone>
      <cbc:ElectronicMail>payables@castrano.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:CustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:CustomerParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>FGR-CP-4160-E1-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>Warehouse of Castrano Logistics</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="KWH">19350</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>FGR-CP-4160-E1</cbc:ID>
      <cbc:Description>Warehouse of Castrano Logistics</cbc:Description>
      <cbc:SubscriberID>FE-CU-0381206</cbc:SubscriberID>
      <cbc:SubscriberType>Commercial</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">COM</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="KWH">19350</cbc:TotalDeliveredQuantity>
      <cac:Address>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
        <cbc:BuildingNumber>24</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
        <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
        <cbc:PostalZone>4190</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:Address>
      <cac:UtilityMeter>
        <cbc:MeterNumber>FGR-E-20523</cbc:MeterNumber>
        <cbc:MeterName>Warehouse meter</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">DIRECT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="KWH">19350</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>FGR-E-20523-2603</cbc:ID>
          <cbc:MeterReadingType>Monthly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode listID="urn:ubl-examples:world:codelist:MeterReadingTypeCode">M</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2026-02-28</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="KWH">116500</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="KWH">135850</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Load profile: derived from the warehouse's load profile between the readings of 31 January and 31 March, in place of February's estimate of 117,250 kWh</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">PROFILE</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Read by the meter reader</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">MANUAL</cbc:LatestMeterReadingMethodCode>
          <cbc:MeterReadingComments>The previous reading replaces February's estimate of 117,250 kWh: February used 16,450 kWh, not the 17,200 kWh billed, and the 750 kWh are credited.</cbc:MeterReadingComments>
          <cbc:DeliveredQuantity unitCode="KWH">19350</cbc:DeliveredQuantity>
        </cac:MeterReading>
        <cac:MeterProperty>
          <cbc:Name>Accuracy class</cbc:Name>
          <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">ACC</cbc:NameCode>
          <cbc:Value>1</cbc:Value>
          <cbc:ValueQualifier>Calibrated 2024</cbc:ValueQualifier>
        </cac:MeterProperty>
        <cac:MeterProperty>
          <cbc:Name>Rated current</cbc:Name>
          <cbc:ValueQuantity unitCode="AMP">5</cbc:ValueQuantity>
        </cac:MeterProperty>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:SupplierConsumption>
      <cbc:Description>The energy, which Ferrano Energy supplies under the customer's contract.</cbc:Description>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Energy</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">ELEC</cbc:UtilityStatementTypeCode>
        <cac:MainPeriod>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">11160</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxAmount currencyID="XUF">11610</cbc:TaxAmount>
            <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
            <cbc:PerUnitAmount currencyID="XUF">0.6</cbc:PerUnitAmount>
            <cac:TaxCategory>
              <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
              <cbc:Name>Energy tax</cbc:Name>
              <cac:TaxScheme>
                <cbc:ID schemeID="UN/EDIFACT EDED 5153">EXC</cbc:ID>
              </cac:TaxScheme>
            </cac:TaxCategory>
          </cac:TaxSubtotal>
          <cac:TaxSubtotal>
            <cbc:TaxAmount currencyID="XUF">-450</cbc:TaxAmount>
            <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
            <cbc:PerUnitAmount currencyID="XUF">0.6</cbc:PerUnitAmount>
            <cbc:TierRange>February's estimate correction: 750 kWh of the warehouse credited at the rate February's bill charged on them, the upper tier</cbc:TierRange>
            <cac:TaxCategory>
              <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
              <cbc:Name>Energy tax</cbc:Name>
              <cac:TaxScheme>
                <cbc:ID schemeID="UN/EDIFACT EDED 5153">EXC</cbc:ID>
              </cac:TaxScheme>
            </cac:TaxCategory>
          </cac:TaxSubtotal>
        </cac:TaxTotal>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">80724</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="XUF">403620</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="XUF">80724</cbc:TaxAmount>
            <cac:TaxCategory>
              <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
              <cbc:Percent>20</cbc:Percent>
              <cac:TaxScheme>
                <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
              </cac:TaxScheme>
            </cac:TaxCategory>
          </cac:TaxSubtotal>
        </cac:TaxTotal>
        <cac:EnergyWaterSupply>
          <cac:ConsumptionReport>
            <cbc:ID>FGR-CP-4160-E1-2603</cbc:ID>
            <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
            <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
            <cbc:Description>March consumption of Warehouse of Castrano Logistics.</cbc:Description>
            <cbc:TotalConsumedQuantity unitCode="KWH">19350</cbc:TotalConsumedQuantity>
            <cbc:BasicConsumedQuantity unitCode="KWH">19350</cbc:BasicConsumedQuantity>
            <cac:Period>
              <cbc:StartDate>2026-03-01</cbc:StartDate>
              <cbc:EndDate>2026-03-31</cbc:EndDate>
            </cac:Period>
            <cac:ConsumptionReportReference>
              <cbc:ConsumptionReportID>FGR-CP-4160-E1-2602</cbc:ConsumptionReportID>
              <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
              <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
              <cbc:TotalConsumedQuantity unitCode="KWH">17200</cbc:TotalConsumedQuantity>
              <cac:Period>
                <cbc:StartDate>2026-02-01</cbc:StartDate>
                <cbc:EndDate>2026-02-28</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionReportReference>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>FGR-E-20523</cbc:MeterNumber>
              <cbc:Quantity unitCode="KWH">17900</cbc:Quantity>
              <cbc:Amount currencyID="XUF">377690</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cac:Period>
                <cbc:StartDate>2026-01-01</cbc:StartDate>
                <cbc:EndDate>2026-01-31</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>FGR-E-20523</cbc:MeterNumber>
              <cbc:Quantity unitCode="KWH">16450</cbc:Quantity>
              <cbc:Amount currencyID="XUF">347095</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cbc:Description>Corrected from the estimate of 17,200 kWh.</cbc:Description>
              <cac:Period>
                <cbc:StartDate>2026-02-01</cbc:StartDate>
                <cbc:EndDate>2026-02-28</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
          </cac:ConsumptionReport>
          <cac:EnergyTaxReport>
            <cbc:TaxEnergyAmount currencyID="XUF">11160</cbc:TaxEnergyAmount>
            <cbc:TaxEnergyOnAccountAmount currencyID="XUF">0</cbc:TaxEnergyOnAccountAmount>
            <cbc:TaxEnergyBalanceAmount currencyID="XUF">11160</cbc:TaxEnergyBalanceAmount>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">EXC</cbc:ID>
            </cac:TaxScheme>
          </cac:EnergyTaxReport>
          <cac:ConsumptionAverage>
            <cbc:AverageAmount currencyID="XUF">377690</cbc:AverageAmount>
            <cbc:Description>The average over the last three months is 17,900 kWh.</cbc:Description>
          </cac:ConsumptionAverage>
          <cac:EnergyWaterConsumptionCorrection>
            <cbc:CorrectionType>Estimate correction</cbc:CorrectionType>
            <cbc:CorrectionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode">EST</cbc:CorrectionTypeCode>
            <cbc:MeterNumber>FGR-E-20523</cbc:MeterNumber>
            <cbc:Description>February's reading was estimated at 117,250 kWh, as the meter could not be reached; the readings of 31 January and 31 March, split by the warehouse's load profile, put it at 116,500 kWh. February used 16,450 kWh, not the 17,200 kWh billed: the 750 kWh are credited on line 4 of the bill.</cbc:Description>
          </cac:EnergyWaterConsumptionCorrection>
        </cac:EnergyWaterSupply>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XUF">392460</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XUF">484344</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:Contract>
        <cbc:ID>FE-C-0047120</cbc:ID>
        <cbc:ContractType>Electricity supply</cbc:ContractType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2024-01-01</cbc:StartDate>
        </cac:ValidityPeriod>
      </cac:Contract>
      <cac:ConsumptionLine>
        <cbc:ID>1</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>2</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="KWH">19350</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XUF">408285</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">503874</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">95589</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>FE-KWH-E</cbc:ID>
          <cbc:SubscriberID>FE-CU-0381206</cbc:SubscriberID>
          <cbc:SubscriberType>Commercial</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">COM</cbc:SubscriberTypeCode>
          <cbc:Description languageID="qau">Drek zikdrir skul drek zuktrek tazkraz, ginek zalhaz bantan: drek zhutek FE-KWH zentul drek gatir vatir skul drek zhek.</cbc:Description>
          <cbc:Description languageID="en-XU">The energy of the electricity supply, per kilowatt hour: the tariff FE-KWH without the network charge of the grid.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
            <cbc:Percent>20</cbc:Percent>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
          <cac:Contract>
            <cbc:ID>FE-C-0047120</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XUF">21.1</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="KWH">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
      <cac:ConsumptionLine>
        <cbc:ID>2</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>4</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="KWH">-750</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XUF">-15825</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">-19530</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-02-01</cbc:StartDate>
          <cbc:EndDate>2026-02-28</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">-3705</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>FE-KWH-E</cbc:ID>
          <cbc:SubscriberID>FE-CU-0381206</cbc:SubscriberID>
          <cbc:SubscriberType>Commercial</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">COM</cbc:SubscriberTypeCode>
          <cbc:Description languageID="qau">Drek zikdrir skul drek zuktrek tazkraz, ginek zalhaz bantan: drek zhutek FE-KWH zentul drek gatir vatir skul drek zhek.</cbc:Description>
          <cbc:Description languageID="en-XU">The energy of the electricity supply, per kilowatt hour: the tariff FE-KWH without the network charge of the grid.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
            <cbc:Percent>20</cbc:Percent>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
          <cac:Contract>
            <cbc:ID>FE-C-0047120</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XUF">21.1</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="KWH">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
    <cac:SupplierConsumption>
      <cbc:Description>Ferrano Grid's network charges, which Ferrano Energy collects with its bill and pays to the grid.</cbc:Description>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106055</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Grid</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">ELEC</cbc:UtilityStatementTypeCode>
        <cac:MainPeriod>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">23064</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="XUF">115320</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="XUF">23064</cbc:TaxAmount>
            <cac:TaxCategory>
              <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
              <cbc:Percent>20</cbc:Percent>
              <cac:TaxScheme>
                <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
              </cac:TaxScheme>
            </cac:TaxCategory>
          </cac:TaxSubtotal>
        </cac:TaxTotal>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XUF">115320</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XUF">138384</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:ConsumptionLine>
        <cbc:ID>3</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>2</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="KWH">19350</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XUF">119970</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">143964</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">23994</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>FGR-NET-E</cbc:ID>
          <cbc:SubscriberType>Commercial</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">COM</cbc:SubscriberTypeCode>
          <cbc:Description languageID="qau">Krek skul drek zuktrek rirtan gatir, ginek zalhaz bantan kirhan hir drek trekstan.</cbc:Description>
          <cbc:Description languageID="en-XU">Use of the electricity distribution network, per kilowatt hour taken at the connection.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
            <cbc:Percent>20</cbc:Percent>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XUF">6.2</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="KWH">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
      <cac:ConsumptionLine>
        <cbc:ID>4</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>4</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="KWH">-750</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XUF">-4650</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">-5580</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-02-01</cbc:StartDate>
          <cbc:EndDate>2026-02-28</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">-930</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>FGR-NET-E</cbc:ID>
          <cbc:SubscriberType>Commercial</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">COM</cbc:SubscriberTypeCode>
          <cbc:Description languageID="qau">Krek skul drek zuktrek rirtan gatir, ginek zalhaz bantan kirhan hir drek trekstan.</cbc:Description>
          <cbc:Description languageID="en-XU">Use of the electricity distribution network, per kilowatt hour taken at the connection.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
            <cbc:Percent>20</cbc:Percent>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XUF">6.2</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="KWH">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
