# Utility Statement: Ferrano Energy to Valdara Industries

*Example 1 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The factory's monthly electricity consumption: meter readings and consumption at its main connection, with Ferrano Energy's energy and Ferrano Grid's network charges as the two suppliers of the bill's tariff.

[The XML file](01-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **9409901441**  
  The utility's statement number.
- `UUID` = **939b6614-b83d-522f-883a-72105c1b71f9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **16:31:00-01:00**  
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
- `Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); as Ferrano Energy gives it.
- `Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Ferrano Energy gives it.
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; as Ferrano Energy gives it.
- `Contact/Telephone` = **+999 1 041 474 7922**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Energy gives it.
- `Contact/ElectronicMail` = **billing@ferranoenergy.example**  
  The contact's e-mail address; as Ferrano Energy gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Ferrano Energy gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Energy gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Valdara Industries gives it.
- `Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Finance**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **payables@valdara.example**  
  The contact's e-mail address; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **FGR-CP-4120-E1-2603**  
  The consumption of the point in March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  A detailed specification. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **Factory, main connection at 10 kV**  
  The point.
- `TotalMeteredQuantity` = **412800** (unitCode `KWH`)  
  Metered in March.
- `UtilityConsumptionPoint/ID` = **FGR-CP-4120-E1**  
  The connection, numbered by the grid operator, Ferrano Grid, which owns and reads the meters; the retail company uses its numbers, its own reference being the contract.
- `UtilityConsumptionPoint/Description` = **Factory, main connection at 10 kV**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **FE-CU-0381206**  
  The subscriber's customer number with the utility; the contract number stays in the contract.
- `UtilityConsumptionPoint/SubscriberType` = **Industrial**  
  The name of code IND in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **IND** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: IND = Industrial.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **412800** (unitCode `KWH`)  
  Delivered in March.
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
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **FGR-E-20388**  
  The meter, numbered by the grid operator, Ferrano Grid, which owns and reads the meters; the retail company uses its numbers, its own reference being the contract.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Main meter, factory**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **4000**  
  The register is multiplied by this.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **CTVT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  Why: current and voltage transformers. The code is from the Trade Accord's meter constant type list: CTVT = Current and voltage transformers.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **412800** (unitCode `KWH`)  
  Delivered in March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **FGR-E-20388-2603**  
  The reading of March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Monthly reading**  
  The name of code M in the Trade Accord's meter reading type list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:MeterReadingTypeCode`)  
  As a code. The code is from the Trade Accord's meter reading type list: M = Monthly reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2026-02-28**  
  The previous reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **1324** (unitCode `KWH`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **1427.2** (unitCode `KWH`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Remote reading**  
  The name of code REMOTE in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **REMOTE** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: REMOTE = Remote reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Remote reading**  
  The name of code REMOTE in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **REMOTE** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: REMOTE = Remote reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **412800** (unitCode `KWH`)  
  The difference of the readings, times the meter constant of 4000.
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
  Its value: the secondary current of the current transformers.
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
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **277680** (currencyID `XUF`)  
  The energy tax on this point's electricity.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **60000** (currencyID `XUF`)  
  50000 kWh at 1.2 ferra.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  Per kilowatt hour.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/PerUnitAmount` = **1.2** (currencyID `XUF`)  
  The rate of the tier.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The energy tax applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Name` = **Energy tax**  
  The tax in words.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **EXC** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code EXC: excise duty, the energy tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: EXC = Excise duty. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **217680** (currencyID `XUF`)  
  362800 kWh at 0.6 ferra.
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
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **1797552** (currencyID `XUF`)  
  20 % value added tax on the energy and the energy tax.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **8987760** (currencyID `XUF`)  
  The energy plus the energy tax.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **1797552** (currencyID `XUF`)  
  20 % of it.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **FGR-CP-4120-E1-2603**  
  The consumption report of the point for March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Description` = **March consumption of Factory, main connection at 10 kV.**  
  In words.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **412800** (unitCode `KWH`)  
  Used in March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/BasicConsumedQuantity` = **412800** (unitCode `KWH`)  
  All at the basic tariff: no reduced-rate hours.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionReportID` = **FGR-CP-4120-E1-2602**  
  The report of February.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/TotalConsumedQuantity` = **405100** (unitCode `KWH`)  
  What February's report said.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/StartDate` = **2026-02-01**  
  February.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/EndDate` = **2026-02-28**  
  Its last day.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **FGR-E-20388**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **398400** (unitCode `KWH`)  
  The month's consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **8406240** (currencyID `XUF`)  
  What it cost at the supplier's own tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-01-01**  
  The month.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-01-31**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **FGR-E-20388**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **405100** (unitCode `KWH`)  
  The month's consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **8547610** (currencyID `XUF`)  
  What it cost at the supplier's own tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-02-01**  
  The month.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-02-28**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxEnergyAmount` = **277680** (currencyID `XUF`)  
  This point's share of the bill's energy tax: 50,000 kWh at 1.2 and 362,800 kWh at 0.6 ferra; the tiers apply to the customer's month as a whole, the lower tier counted on the main connection.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxEnergyOnAccountAmount` = **0** (currencyID `XUF`)  
  No energy tax paid on account.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxEnergyBalanceAmount` = **277680** (currencyID `XUF`)  
  Due with this bill.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyTaxReport/TaxScheme/ID` = **EXC** (schemeID `UN/EDIFACT EDED 5153`)  
  Urvania's energy tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: EXC = Excise duty. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/AverageAmount` = **8554643** (currencyID `XUF`)  
  The average amount of the last three months at the supplier's own tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/Description` = **The average over the last three months is 405,433 kWh.**  
  For comparison.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **8710080** (currencyID `XUF`)  
  The lines of this part.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **10785312** (currencyID `XUF`)  
  With its taxes.
- `SupplierConsumption/Contract/ID` = **FE-C-0047120**  
  The supply contract.
- `SupplierConsumption/Contract/ContractType` = **Electricity supply**  
  Its kind.
- `SupplierConsumption/Contract/ValidityPeriod/StartDate` = **2024-01-01**  
  In force since.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **412800** (unitCode `KWH`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **8710080** (currencyID `XUF`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **10785312** (currencyID `XUF`)  
  With the energy tax and the value added tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **2075232** (currencyID `XUF`)  
  The energy tax and the value added tax of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **FE-KWH-E**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **FE-CU-0381206**  
  The subscriber's customer number with the utility.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Industrial**  
  The name of code IND in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **IND** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: IND = Industrial.
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
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **511872** (currencyID `XUF`)  
  The tax of this part of the consumption.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **2559360** (currencyID `XUF`)  
  The lines of this part.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **511872** (currencyID `XUF`)  
  20 % of them.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **2559360** (currencyID `XUF`)  
  The lines of this part.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **3071232** (currencyID `XUF`)  
  With its tax.
- `SupplierConsumption/ConsumptionLine/ID` = **2**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **412800** (unitCode `KWH`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **2559360** (currencyID `XUF`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **3071232** (currencyID `XUF`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **511872** (currencyID `XUF`)  
  20 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **FGR-NET-E**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Industrial**  
  The name of code IND in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **IND** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: IND = Industrial.
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
  <cbc:ID>9409901441</cbc:ID>
  <cbc:UUID>939b6614-b83d-522f-883a-72105c1b71f9</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>16:31:00-01:00</cbc:IssueTime>
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
      <cbc:Name>Billing</cbc:Name>
      <cbc:JobTitle>Billing officer</cbc:JobTitle>
      <cbc:Department>Customer service</cbc:Department>
      <cbc:Telephone>+999 1 041 474 7922</cbc:Telephone>
      <cbc:ElectronicMail>billing@ferranoenergy.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105781</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
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
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Accounts payable</cbc:Name>
      <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>payables@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>FGR-CP-4120-E1-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>Factory, main connection at 10 kV</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="KWH">412800</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>FGR-CP-4120-E1</cbc:ID>
      <cbc:Description>Factory, main connection at 10 kV</cbc:Description>
      <cbc:SubscriberID>FE-CU-0381206</cbc:SubscriberID>
      <cbc:SubscriberType>Industrial</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">IND</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="KWH">412800</cbc:TotalDeliveredQuantity>
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
        <cbc:MeterNumber>FGR-E-20388</cbc:MeterNumber>
        <cbc:MeterName>Main meter, factory</cbc:MeterName>
        <cbc:MeterConstant>4000</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">CTVT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="KWH">412800</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>FGR-E-20388-2603</cbc:ID>
          <cbc:MeterReadingType>Monthly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode listID="urn:ubl-examples:world:codelist:MeterReadingTypeCode">M</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2026-02-28</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="KWH">1324</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="KWH">1427.2</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Remote reading</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">REMOTE</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Remote reading</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">REMOTE</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="KWH">412800</cbc:DeliveredQuantity>
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
          <cbc:TaxAmount currencyID="XUF">277680</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxAmount currencyID="XUF">60000</cbc:TaxAmount>
            <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
            <cbc:PerUnitAmount currencyID="XUF">1.2</cbc:PerUnitAmount>
            <cac:TaxCategory>
              <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
              <cbc:Name>Energy tax</cbc:Name>
              <cac:TaxScheme>
                <cbc:ID schemeID="UN/EDIFACT EDED 5153">EXC</cbc:ID>
              </cac:TaxScheme>
            </cac:TaxCategory>
          </cac:TaxSubtotal>
          <cac:TaxSubtotal>
            <cbc:TaxAmount currencyID="XUF">217680</cbc:TaxAmount>
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
        </cac:TaxTotal>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">1797552</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="XUF">8987760</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="XUF">1797552</cbc:TaxAmount>
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
            <cbc:ID>FGR-CP-4120-E1-2603</cbc:ID>
            <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
            <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
            <cbc:Description>March consumption of Factory, main connection at 10 kV.</cbc:Description>
            <cbc:TotalConsumedQuantity unitCode="KWH">412800</cbc:TotalConsumedQuantity>
            <cbc:BasicConsumedQuantity unitCode="KWH">412800</cbc:BasicConsumedQuantity>
            <cac:Period>
              <cbc:StartDate>2026-03-01</cbc:StartDate>
              <cbc:EndDate>2026-03-31</cbc:EndDate>
            </cac:Period>
            <cac:ConsumptionReportReference>
              <cbc:ConsumptionReportID>FGR-CP-4120-E1-2602</cbc:ConsumptionReportID>
              <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
              <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
              <cbc:TotalConsumedQuantity unitCode="KWH">405100</cbc:TotalConsumedQuantity>
              <cac:Period>
                <cbc:StartDate>2026-02-01</cbc:StartDate>
                <cbc:EndDate>2026-02-28</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionReportReference>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>FGR-E-20388</cbc:MeterNumber>
              <cbc:Quantity unitCode="KWH">398400</cbc:Quantity>
              <cbc:Amount currencyID="XUF">8406240</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cac:Period>
                <cbc:StartDate>2026-01-01</cbc:StartDate>
                <cbc:EndDate>2026-01-31</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>FGR-E-20388</cbc:MeterNumber>
              <cbc:Quantity unitCode="KWH">405100</cbc:Quantity>
              <cbc:Amount currencyID="XUF">8547610</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cac:Period>
                <cbc:StartDate>2026-02-01</cbc:StartDate>
                <cbc:EndDate>2026-02-28</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
          </cac:ConsumptionReport>
          <cac:EnergyTaxReport>
            <cbc:TaxEnergyAmount currencyID="XUF">277680</cbc:TaxEnergyAmount>
            <cbc:TaxEnergyOnAccountAmount currencyID="XUF">0</cbc:TaxEnergyOnAccountAmount>
            <cbc:TaxEnergyBalanceAmount currencyID="XUF">277680</cbc:TaxEnergyBalanceAmount>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">EXC</cbc:ID>
            </cac:TaxScheme>
          </cac:EnergyTaxReport>
          <cac:ConsumptionAverage>
            <cbc:AverageAmount currencyID="XUF">8554643</cbc:AverageAmount>
            <cbc:Description>The average over the last three months is 405,433 kWh.</cbc:Description>
          </cac:ConsumptionAverage>
        </cac:EnergyWaterSupply>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XUF">8710080</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XUF">10785312</cbc:PayableAmount>
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
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="KWH">412800</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XUF">8710080</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">10785312</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">2075232</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>FE-KWH-E</cbc:ID>
          <cbc:SubscriberID>FE-CU-0381206</cbc:SubscriberID>
          <cbc:SubscriberType>Industrial</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">IND</cbc:SubscriberTypeCode>
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
          <cbc:TaxAmount currencyID="XUF">511872</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="XUF">2559360</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="XUF">511872</cbc:TaxAmount>
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
          <cbc:LineExtensionAmount currencyID="XUF">2559360</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XUF">3071232</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:ConsumptionLine>
        <cbc:ID>2</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="KWH">412800</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XUF">2559360</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XUF">3071232</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XUF">511872</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>FGR-NET-E</cbc:ID>
          <cbc:SubscriberType>Industrial</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">IND</cbc:SubscriberTypeCode>
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
