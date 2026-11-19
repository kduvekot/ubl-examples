# Utility Statement: Coastal State Water Company to Robin Ashdale

*Example 8 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The household's water consumption.

[The XML file](08-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:utility-statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Utility statement". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **UTILITIES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **CSWC-DOC-26-0320**  
  The utility's statement number.
- `UUID` = **8ee8ec8d-3357-524c-81b1-479a651b524c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **15:10:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of utility the statement is about. The code is from the Trade Accord's utility type list: WATER = Water.
- `Note` = **This statement explains the consumption behind your bill.**  
  What the statement is.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the utility's currency; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **CSWC-INV-26-0319**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CSWC-INV-26-0319 is the example utilities/09, a Invoice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Invoice.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **CSWC-TARIFF-2026**  
  The utility's tariff sheet for 2026.
- `DocumentTypeCode` = **TARIFF** (listID `urn:ubl-examples:world:codelist:DocumentTypeCode`)  
  What the document is. The code is from the Trade Accord's document type list: TARIFF = Tariff.
- `DocumentDescription` = **Prices per unit and the terms of supply.**  
  What it holds.

### Signature

Inside `Signature`:

- `ID` = **CSW-SIG-26-0401**  
  The water company's seal.
- `SignatoryParty/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Coastal State Water Company**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Coastal State Water Company**  
  The trading name; identity of Coastal State Water Company (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-782593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Coastal State Water Company (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); identity of Coastal State Water Company (world/parties.json).
- `Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; identity of Coastal State Water Company (world/parties.json).
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; identity of Coastal State Water Company (world/parties.json).
- `Contact/Telephone` = **+999 2 38 9310 7518**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Coastal State Water Company (world/parties.json).
- `Contact/ElectronicMail` = **billing@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Coastal State Water Company (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyName/Name` = **Robin Ashdale**  
  The trading name; identity of Robin Ashdale (world/parties.json).
- `PostalAddress/ID` = **LUM-ADR-934215** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Robin Ashdale (world/parties.json).
- `PostalAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Robin Ashdale (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Person/FirstName` = **Robin**  
  The consumer's first name; identity of Robin Ashdale (world/parties.json).
- `Person/FamilyName` = **Ashdale**  
  The consumer's family name; identity of Robin Ashdale (world/parties.json).

### Subscriber Party

Inside `SubscriberParty`:

- `PartyName/Name` = **Robin Ashdale**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Main On Account Payment

Inside `MainOnAccountPayment`:

- `EstimatedConsumedQuantity` = **14** (unitCode `MTQ`)  
  The household's expected monthly use.
- `Note` = **The basis of the direct debit limit.**  
  Why it is stated.
- `PaymentTerms/Note` = **Collected by direct debit; the mandate's limit is set well above this estimate.**  
  How it is paid.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **CSW-CP-38516-57-2603**  
  The consumption of the point in March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  A detailed specification. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **Gull Lane 57, Lumeport**  
  The point.
- `TotalMeteredQuantity` = **14** (unitCode `MTQ`)  
  Metered in March.
- `UtilityConsumptionPoint/ID` = **CSW-CP-38516-57**  
  The connection's number.
- `UtilityConsumptionPoint/Description` = **Gull Lane 57, Lumeport**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **CSW-CU-097315**  
  The subscriber's customer number with the utility; the contract number stays in the contract (D31 point 5).
- `UtilityConsumptionPoint/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **14** (unitCode `MTQ`)  
  Delivered in March.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `UtilityConsumptionPoint/Address/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `UtilityConsumptionPoint/Address/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `UtilityConsumptionPoint/Address/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Robin Ashdale (world/parties.json).
- `UtilityConsumptionPoint/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `UtilityConsumptionPoint/Address/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `UtilityConsumptionPoint/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `UtilityConsumptionPoint/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/WebSiteAccess/URI` = **https://www.coastalwater.example/reading**  
  Where the household enters its next meter reading, as it entered this one.
- `UtilityConsumptionPoint/WebSiteAccess/Password` = **RD-4K7-918**  
  The one-time reading code for the next reading, printed on each statement: it opens the reading page only, from 28 April to 5 May 2026, so a household needs no account to send its reading.
- `UtilityConsumptionPoint/WebSiteAccess/Login` = **CSW-CP-38516-57**  
  The household logs in with the number of its connection.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **CSW-W-71844**  
  The meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Water meter, flat**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  The register is multiplied by this.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **DIRECT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  Why: direct. The code is from the Trade Accord's meter constant type list: DIRECT = Direct connection.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **14** (unitCode `MTQ`)  
  Delivered in March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **CSW-W-71844-2603**  
  The reading of March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Monthly reading**  
  The name of code M in the Trade Accord's meter reading type list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:MeterReadingTypeCode`)  
  As a code. The code is from the Trade Accord's meter reading type list: M = Monthly reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2026-02-28**  
  The previous reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **1830** (unitCode `MTQ`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **1844** (unitCode `MTQ`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Read by the customer: the household sent the reading**  
  The name of code CUSTOMER in the Trade Accord's meter reading method list, followed by the detail of this case: from the utility's record of the reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **CUSTOMER** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: CUSTOMER = Read by the customer.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Read by the customer: the household sent the reading**  
  The name of code CUSTOMER in the Trade Accord's meter reading method list, followed by the detail of this case: from the utility's record of the reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **CUSTOMER** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: CUSTOMER = Read by the customer.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **14** (unitCode `MTQ`)  
  The difference of the readings.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Accuracy class**  
  The name of code ACC in the Trade Accord's item property name list.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/NameCode` = **ACC** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  As a code. The code is from the Trade Accord's item property name list: ACC = Accuracy class.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Value` = **1**  
  Class 1.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQualifier` = **Calibrated 2024**  
  When it was checked.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Permanent flow rate (Q3)**  
  A rating of the meter: the flow it measures continuously within its accuracy class (utilities/05#F12).
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQuantity` = **2.5** (unitCode `MQH`)  
  Its value.
- `OnAccountPayment/EstimatedConsumedQuantity` = **14** (unitCode `MTQ`)  
  The expected use next month.
- `OnAccountPayment/Note` = **Paid on account each month for the estimated use; the next bill settles it against the reading.**  
  How the household pays between readings.
- `OnAccountPayment/PaymentTerms/Note` = **By direct debit on the first working day of each month.**  
  When the payment on account is collected.
- `SupplierConsumption/Description` = **The drinking water, which the water company supplies under the customer's contract.**  
  Whose supply this part is, and how it is billed.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Coastal State Water Company**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Robin Ashdale**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: WATER = Water.
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  The tax of this part of the consumption.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **32.90** (currencyID `XBL`)  
  The lines of this part.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of them.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Drinking water is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **CSW-CP-38516-57-2603**  
  The consumption report of the point for March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Description` = **March consumption of Gull Lane 57, Lumeport.**  
  In words.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **14** (unitCode `MTQ`)  
  Used in March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/BasicConsumedQuantity` = **14** (unitCode `MTQ`)  
  All at the basic tariff: no reduced-rate hours.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ResidentOccupantsNumeric` = **2**  
  People living in the flat.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumersEnergyLevelCode` = **LOW** (listID `urn:ubl-examples:world:codelist:ConsumersEnergyLevelCode`)  
  Below the average for two occupants. The code is from the Trade Accord's consumer's energy level list: LOW = Low consumer.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumersEnergyLevel` = **Low consumer**  
  The name of code LOW in the Trade Accord's consumer's energy level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ResidenceType` = **Apartment**  
  The name of code APT in the Trade Accord's residence type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ResidenceTypeCode` = **APT** (listID `urn:ubl-examples:world:codelist:ResidenceTypeCode`)  
  As a code. The code is from the Trade Accord's residence type list: APT = Apartment.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/HeatingType` = **District heating**  
  The name of code DH in the Trade Accord's heating type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/HeatingTypeCode` = **DH** (listID `urn:ubl-examples:world:codelist:HeatingTypeCode`)  
  As a code. The code is from the Trade Accord's heating type list: DH = District heating.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/GuidanceDocumentReference/ID` = **CSW-SAVE-WATER**  
  The company's leaflet on saving water.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/DocumentReference/ID` = **CSW-QUALITY-2026-Q1**  
  The quarterly water quality report.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/DocumentReference/DocumentType` = **Water quality report**  
  The kind of document referred to, the water company's quarterly water quality report, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionReportID` = **CSW-CP-38516-57-2602**  
  The report of February.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/TotalConsumedQuantity` = **13** (unitCode `MTQ`)  
  What February's report said.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/StartDate` = **2026-02-01**  
  February.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/EndDate` = **2026-02-28**  
  Its last day.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-71844**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **15** (unitCode `MTQ`)  
  The month's consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **35.25** (currencyID `XBL`)  
  What it cost at the tariff of the bill, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-01-01**  
  The month.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-01-31**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-71844**  
  The meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **13** (unitCode `MTQ`)  
  The month's consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **30.55** (currencyID `XBL`)  
  What it cost at the tariff of the bill, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-02-01**  
  The month.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-02-28**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/AverageAmount` = **32.90** (currencyID `XBL`)  
  The average amount of the last three months at the tariff of the bill, without tax (utilities/01#F3).
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/Description` = **The average over the last three months is 14 m³.**  
  For comparison.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionType` = **District heating cooling correction**  
  The name of code COOL in the Trade Accord's consumption correction type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionTypeCode` = **COOL** (listID `urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption correction type list: COOL = District heating cooling correction.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/MeterNumber` = **CSW-H-71844**  
  The heat meter of the flat.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/ActualTemperatureReductionQuantity` = **31** (unitCode `CEL`)  
  The water cooled by 31 degrees in the flat.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/NormalTemperatureReductionQuantity` = **35** (unitCode `CEL`)  
  The network's standard cooling.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/DifferenceTemperatureReductionQuantity` = **-4** (unitCode `CEL`)  
  Four degrees less than the standard.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/Description` = **Poor cooling makes the network pump more water; the shortfall is charged on the annual account.**  
  Why.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionUnitAmount` = **0.80** (currencyID `XBL`)  
  The surcharge per cubic metre per degree short.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/ConsumptionWaterQuantity` = **6.2** (unitCode `MTQ`)  
  District heating water that passed the flat in March.
- `SupplierConsumption/Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionAmount` = **19.84** (currencyID `XBL`)  
  6.2 m³ × 4 degrees × 0.80: added to the annual heating account, not to this bill.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **32.90** (currencyID `XBL`)  
  The lines of this part.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **32.90** (currencyID `XBL`)  
  With its tax.
- `SupplierConsumption/Contract/ID` = **CSW-C-311790**  
  The supply contract.
- `SupplierConsumption/Contract/ContractType` = **Water supply**  
  Its kind.
- `SupplierConsumption/Contract/ValidityPeriod/StartDate` = **2024-01-01**  
  In force since.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **14** (unitCode `MTQ`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **32.90** (currencyID `XBL`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **32.90** (currencyID `XBL`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **CW-M3**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **CSW-CU-097315**  
  The subscriber's customer number with the utility (D31 point 5).
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Drinking water supply, per cubic metre.**  
  The tariff in words; world/items.json.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Drinking water is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **CSW-C-311790**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **2.35** (currencyID `XBL`)  
  The tariff (world/items.json).
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  Per unit.
- `SupplierConsumption/Description` = **The city of Lumeport's sewage levy on the water used, which the water company collects with its bill and pays to the city.**  
  Whose supply this part is, and how it is billed.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Robin Ashdale**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: WATER = Water.
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **5.88** (currencyID `XBL`)  
  The lines of this part.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **5.88** (currencyID `XBL`)  
  Outside the scope of the tax: nothing added.
- `SupplierConsumption/ConsumptionLine/ID` = **2**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **2**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **14** (unitCode `MTQ`)  
  The household's water use, on which the city charges its levy.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **5.88** (currencyID `XBL`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **CSW-LEVY**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.**  
  The tariff in words; world/items.json.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  The name of code MET in the Trade Accord's consumption type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MET = Metered.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  The name of code M in the Trade Accord's utility charge type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:ChargeTypeCode`)  
  As a code. The code is from the Trade Accord's utility charge type list: M = Monthly.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O, without a rate). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxExemptionReasonCode` = **LEVY** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: LEVY = Collected for a public body, outside the scope of the state sales tax.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxExemptionReason` = **Collected for a public body, outside the scope of the state sales tax**  
  The name of code LEVY in Bayvarra's national sales tax exemption reason list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **0.42** (currencyID `XBL`)  
  The tariff (world/items.json).
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  Per unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:utility-statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>CSWC-DOC-26-0320</cbc:ID>
  <cbc:UUID>8ee8ec8d-3357-524c-81b1-479a651b524c</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>15:10:00-01:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
  <cbc:Note>This statement explains the consumption behind your bill.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cac:ParentDocumentReference>
    <cbc:ID>CSWC-INV-26-0319</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>CSWC-TARIFF-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentTypeCode">TARIFF</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Prices per unit and the terms of supply.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>CSW-SIG-26-0401</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Coastal State Water Company</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-782593</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Reservoir Road</cbc:StreetName>
      <cbc:BuildingNumber>51</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38500</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Billing</cbc:Name>
      <cbc:JobTitle>Billing officer</cbc:JobTitle>
      <cbc:Department>Customer service</cbc:Department>
      <cbc:Telephone>+999 2 38 9310 7518</cbc:Telephone>
      <cbc:ElectronicMail>billing@coastalwater.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyName>
      <cbc:Name>Robin Ashdale</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-934215</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">RESIDENTIAL</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Gull Lane</cbc:StreetName>
      <cbc:BuildingNumber>57</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Riverside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38516</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Person>
      <cbc:FirstName>Robin</cbc:FirstName>
      <cbc:FamilyName>Ashdale</cbc:FamilyName>
    </cac:Person>
  </cac:ReceiverParty>
  <cac:SubscriberParty>
    <cac:PartyName>
      <cbc:Name>Robin Ashdale</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:MainOnAccountPayment>
    <cbc:EstimatedConsumedQuantity unitCode="MTQ">14</cbc:EstimatedConsumedQuantity>
    <cbc:Note>The basis of the direct debit limit.</cbc:Note>
    <cac:PaymentTerms>
      <cbc:Note>Collected by direct debit; the mandate's limit is set well above this estimate.</cbc:Note>
    </cac:PaymentTerms>
  </cac:MainOnAccountPayment>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>CSW-CP-38516-57-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>Gull Lane 57, Lumeport</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="MTQ">14</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>CSW-CP-38516-57</cbc:ID>
      <cbc:Description>Gull Lane 57, Lumeport</cbc:Description>
      <cbc:SubscriberID>CSW-CU-097315</cbc:SubscriberID>
      <cbc:SubscriberType>Household</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">HH</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="MTQ">14</cbc:TotalDeliveredQuantity>
      <cac:Address>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">RESIDENTIAL</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Gull Lane</cbc:StreetName>
        <cbc:BuildingNumber>57</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Riverside</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38516</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:Address>
      <cac:WebSiteAccess>
        <cbc:URI>https://www.coastalwater.example/reading</cbc:URI>
        <cbc:Password>RD-4K7-918</cbc:Password>
        <cbc:Login>CSW-CP-38516-57</cbc:Login>
      </cac:WebSiteAccess>
      <cac:UtilityMeter>
        <cbc:MeterNumber>CSW-W-71844</cbc:MeterNumber>
        <cbc:MeterName>Water meter, flat</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">DIRECT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="MTQ">14</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>CSW-W-71844-2603</cbc:ID>
          <cbc:MeterReadingType>Monthly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode listID="urn:ubl-examples:world:codelist:MeterReadingTypeCode">M</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2026-02-28</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="MTQ">1830</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="MTQ">1844</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Read by the customer: the household sent the reading</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">CUSTOMER</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Read by the customer: the household sent the reading</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">CUSTOMER</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="MTQ">14</cbc:DeliveredQuantity>
        </cac:MeterReading>
        <cac:MeterProperty>
          <cbc:Name>Accuracy class</cbc:Name>
          <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">ACC</cbc:NameCode>
          <cbc:Value>1</cbc:Value>
          <cbc:ValueQualifier>Calibrated 2024</cbc:ValueQualifier>
        </cac:MeterProperty>
        <cac:MeterProperty>
          <cbc:Name>Permanent flow rate (Q3)</cbc:Name>
          <cbc:ValueQuantity unitCode="MQH">2.5</cbc:ValueQuantity>
        </cac:MeterProperty>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:OnAccountPayment>
      <cbc:EstimatedConsumedQuantity unitCode="MTQ">14</cbc:EstimatedConsumedQuantity>
      <cbc:Note>Paid on account each month for the estimated use; the next bill settles it against the reading.</cbc:Note>
      <cac:PaymentTerms>
        <cbc:Note>By direct debit on the first working day of each month.</cbc:Note>
      </cac:PaymentTerms>
    </cac:OnAccountPayment>
    <cac:SupplierConsumption>
      <cbc:Description>The drinking water, which the water company supplies under the customer's contract.</cbc:Description>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Coastal State Water Company</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyName>
          <cbc:Name>Robin Ashdale</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
        <cac:MainPeriod>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="XBL">32.90</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
            <cac:TaxCategory>
              <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
              <cbc:Percent>0</cbc:Percent>
              <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
              <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
              <cac:TaxScheme>
                <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
              </cac:TaxScheme>
            </cac:TaxCategory>
          </cac:TaxSubtotal>
        </cac:TaxTotal>
        <cac:EnergyWaterSupply>
          <cac:ConsumptionReport>
            <cbc:ID>CSW-CP-38516-57-2603</cbc:ID>
            <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
            <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
            <cbc:Description>March consumption of Gull Lane 57, Lumeport.</cbc:Description>
            <cbc:TotalConsumedQuantity unitCode="MTQ">14</cbc:TotalConsumedQuantity>
            <cbc:BasicConsumedQuantity unitCode="MTQ">14</cbc:BasicConsumedQuantity>
            <cbc:ResidentOccupantsNumeric>2</cbc:ResidentOccupantsNumeric>
            <cbc:ConsumersEnergyLevelCode listID="urn:ubl-examples:world:codelist:ConsumersEnergyLevelCode">LOW</cbc:ConsumersEnergyLevelCode>
            <cbc:ConsumersEnergyLevel>Low consumer</cbc:ConsumersEnergyLevel>
            <cbc:ResidenceType>Apartment</cbc:ResidenceType>
            <cbc:ResidenceTypeCode listID="urn:ubl-examples:world:codelist:ResidenceTypeCode">APT</cbc:ResidenceTypeCode>
            <cbc:HeatingType>District heating</cbc:HeatingType>
            <cbc:HeatingTypeCode listID="urn:ubl-examples:world:codelist:HeatingTypeCode">DH</cbc:HeatingTypeCode>
            <cac:Period>
              <cbc:StartDate>2026-03-01</cbc:StartDate>
              <cbc:EndDate>2026-03-31</cbc:EndDate>
            </cac:Period>
            <cac:GuidanceDocumentReference>
              <cbc:ID>CSW-SAVE-WATER</cbc:ID>
            </cac:GuidanceDocumentReference>
            <cac:DocumentReference>
              <cbc:ID>CSW-QUALITY-2026-Q1</cbc:ID>
              <cbc:DocumentType>Water quality report</cbc:DocumentType>
            </cac:DocumentReference>
            <cac:ConsumptionReportReference>
              <cbc:ConsumptionReportID>CSW-CP-38516-57-2602</cbc:ConsumptionReportID>
              <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
              <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
              <cbc:TotalConsumedQuantity unitCode="MTQ">13</cbc:TotalConsumedQuantity>
              <cac:Period>
                <cbc:StartDate>2026-02-01</cbc:StartDate>
                <cbc:EndDate>2026-02-28</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionReportReference>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>CSW-W-71844</cbc:MeterNumber>
              <cbc:Quantity unitCode="MTQ">15</cbc:Quantity>
              <cbc:Amount currencyID="XBL">35.25</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cac:Period>
                <cbc:StartDate>2026-01-01</cbc:StartDate>
                <cbc:EndDate>2026-01-31</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>CSW-W-71844</cbc:MeterNumber>
              <cbc:Quantity unitCode="MTQ">13</cbc:Quantity>
              <cbc:Amount currencyID="XBL">30.55</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cac:Period>
                <cbc:StartDate>2026-02-01</cbc:StartDate>
                <cbc:EndDate>2026-02-28</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
          </cac:ConsumptionReport>
          <cac:ConsumptionAverage>
            <cbc:AverageAmount currencyID="XBL">32.90</cbc:AverageAmount>
            <cbc:Description>The average over the last three months is 14 m³.</cbc:Description>
          </cac:ConsumptionAverage>
          <cac:EnergyWaterConsumptionCorrection>
            <cbc:CorrectionType>District heating cooling correction</cbc:CorrectionType>
            <cbc:CorrectionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode">COOL</cbc:CorrectionTypeCode>
            <cbc:MeterNumber>CSW-H-71844</cbc:MeterNumber>
            <cbc:ActualTemperatureReductionQuantity unitCode="CEL">31</cbc:ActualTemperatureReductionQuantity>
            <cbc:NormalTemperatureReductionQuantity unitCode="CEL">35</cbc:NormalTemperatureReductionQuantity>
            <cbc:DifferenceTemperatureReductionQuantity unitCode="CEL">-4</cbc:DifferenceTemperatureReductionQuantity>
            <cbc:Description>Poor cooling makes the network pump more water; the shortfall is charged on the annual account.</cbc:Description>
            <cbc:CorrectionUnitAmount currencyID="XBL">0.80</cbc:CorrectionUnitAmount>
            <cbc:ConsumptionWaterQuantity unitCode="MTQ">6.2</cbc:ConsumptionWaterQuantity>
            <cbc:CorrectionAmount currencyID="XBL">19.84</cbc:CorrectionAmount>
          </cac:EnergyWaterConsumptionCorrection>
        </cac:EnergyWaterSupply>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XBL">32.90</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XBL">32.90</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:Contract>
        <cbc:ID>CSW-C-311790</cbc:ID>
        <cbc:ContractType>Water supply</cbc:ContractType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2024-01-01</cbc:StartDate>
        </cac:ValidityPeriod>
      </cac:Contract>
      <cac:ConsumptionLine>
        <cbc:ID>1</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MTQ">14</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XBL">32.90</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">32.90</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>CW-M3</cbc:ID>
          <cbc:SubscriberID>CSW-CU-097315</cbc:SubscriberID>
          <cbc:SubscriberType>Household</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">HH</cbc:SubscriberTypeCode>
          <cbc:Description>Drinking water supply, per cubic metre.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
            <cbc:Percent>0</cbc:Percent>
            <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
            <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
          <cac:Contract>
            <cbc:ID>CSW-C-311790</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XBL">2.35</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
    <cac:SupplierConsumption>
      <cbc:Description>The city of Lumeport's sewage levy on the water used, which the water company collects with its bill and pays to the city.</cbc:Description>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Public Works Department</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyName>
          <cbc:Name>Robin Ashdale</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
        <cac:MainPeriod>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XBL">5.88</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XBL">5.88</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:ConsumptionLine>
        <cbc:ID>2</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>2</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MTQ">14</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XBL">5.88</cbc:LineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:UtilityItem>
          <cbc:ID>CSW-LEVY</cbc:ID>
          <cbc:SubscriberType>Household</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">HH</cbc:SubscriberTypeCode>
          <cbc:Description>The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode listID="urn:ubl-examples:world:codelist:ChargeTypeCode">M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
            <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">LEVY</cbc:TaxExemptionReasonCode>
            <cbc:TaxExemptionReason>Collected for a public body, outside the scope of the state sales tax</cbc:TaxExemptionReason>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XBL">0.42</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
