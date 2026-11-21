# Utility Statement: Coastal State Water Company to Robin Ashdale

*Example 8 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The household's annual statement for water and district heat, April 2025 to March 2026: the annual readings, the year's water with the city's levy, the heat with its cooling correction, and the new payments on account from April.

[The XML file](08-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:utility-statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Utility statement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9924052627**  
  The collaboration this document belongs to: the water company's annual account of the household. Coastal State Water Company started it and gave it this identifier, which every document of it repeats.
- `ID` = **9424052721**  
  The utility's statement number.
- `UUID` = **8ee8ec8d-3357-524c-81b1-479a651b524c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **15:10:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of utility the statement is about. The code is from the Trade Accord's utility type list: WATER = Water.
- `Note` = **This annual statement explains the year's water and heat behind your settlement bill, and sets the payments on account for the next year.**  
  What the statement is.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the utility's currency; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **CSW-C-311790-2603**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CSW-C-311790-2603 is the example utilities/09, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **CSW-TARIFF-2026**  
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
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Coastal State Water Company**  
  The trading name; as Coastal State Water Company gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-782593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Coastal State Water Company gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. As Coastal State Water Company gives it.
- `PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. As Coastal State Water Company gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Coastal State Water Company gives it.
- `PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). As Coastal State Water Company gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Coastal State Water Company gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); as Coastal State Water Company gives it.
- `Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Coastal State Water Company gives it.
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; as Coastal State Water Company gives it.
- `Contact/Telephone` = **+999 2 38 9310 7518**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Coastal State Water Company gives it.
- `Contact/ElectronicMail` = **billing@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Coastal State Water Company gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Coastal State Water Company gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyName/Name` = **Robin Ashdale**  
  The trading name; as Robin Ashdale gives it.
- `PostalAddress/ID` = **LUM-ADR-934215** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Robin Ashdale gives it.
- `PostalAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. As Robin Ashdale gives it.
- `PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. As Robin Ashdale gives it.
- `PostalAddress/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Robin Ashdale gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Robin Ashdale gives it.
- `PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). As Robin Ashdale gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Robin Ashdale gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Person/FirstName` = **Robin**  
  The consumer's first name; as Robin Ashdale gives it.
- `Person/FamilyName` = **Ashdale**  
  The consumer's family name; as Robin Ashdale gives it.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyName/Name` = **Robin Ashdale**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Main On Account Payment

Inside `MainOnAccountPayment`:

- `EstimatedConsumedQuantity` = **170** (unitCode `MTQ`)  
  The year's estimate of water; the heat's estimate is with its subscription: UBL gives an on-account payment one quantity.
- `Note` = **The one monthly direct debit for water, levy and heat from April 2026: 94 lume, a twelfth of the year's estimate with the sales tax on the heat, rounded up to a whole lume; it was 84 lume.**  
  What the household pays from now on.
- `PaymentTerms/Note` = **Collected by direct debit on the first working day of each month.**  
  How it is paid.
- `PaymentTerms/Amount` = **94.00** (currencyID `XBL`)  
  The monthly payment on account.
- `PaymentTerms/ValidityPeriod/StartDate` = **2026-04-01**  
  From April.
- `PaymentTerms/ValidityPeriod/EndDate` = **2027-03-31**  
  To the next annual reading.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **CSW-CP-38516-57-2526**  
  The water of the account year.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  A detailed specification. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **Water**  
  The subscription.
- `TotalMeteredQuantity` = **170** (unitCode `MTQ`)  
  Metered in the account year.
- `UtilityConsumptionPoint/ID` = **CSW-CP-38516-57**  
  The water connection's number.
- `UtilityConsumptionPoint/Description` = **Gull Lane 57, Lumeport**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **CSW-CU-097315**  
  The subscriber's customer number with the utility.
- `UtilityConsumptionPoint/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **170** (unitCode `MTQ`)  
  Delivered in the account year.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `UtilityConsumptionPoint/Address/StreetName` = **Gull Lane**  
  Street of the postal address. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/BuildingNumber` = **57**  
  Building number of the postal address. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `UtilityConsumptionPoint/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Robin Ashdale gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `UtilityConsumptionPoint/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **CSW-W-71844**  
  The water meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Water meter, flat**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  The register is read as it is.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **DIRECT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  Why: direct connection. The code is from the Trade Accord's meter constant type list: DIRECT = Direct connection.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **170** (unitCode `MTQ`)  
  Delivered in the account year.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **CSW-W-71844-2603**  
  The annual reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Yearly reading**  
  The name of code Y in the Trade Accord's meter reading type list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **Y** (listID `urn:ubl-examples:world:codelist:MeterReadingTypeCode`)  
  As a code. The code is from the Trade Accord's meter reading type list: Y = Yearly reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2025-03-31**  
  Last year's annual reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **1674** (unitCode `MTQ`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This year's annual reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **1844** (unitCode `MTQ`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Read by the meter reader**  
  The name of code MANUAL in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **MANUAL** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: MANUAL = Read by the meter reader.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Read by the meter reader**  
  The name of code MANUAL in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **MANUAL** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: MANUAL = Read by the meter reader.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **170** (unitCode `MTQ`)  
  The difference of the readings.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Accuracy class**  
  The name of code ACC in the Trade Accord's item property name list.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/NameCode` = **ACC** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  As a code. The code is from the Trade Accord's item property name list: ACC = Accuracy class.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Value` = **1**  
  Class 1.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQualifier` = **Calibrated 2024**  
  When it was checked.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Permanent flow rate**  
  A rating of the meter: the flow it measures continuously within its accuracy class.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQuantity` = **2.5** (unitCode `MQH`)  
  Its value.
- `OnAccountPayment/EstimatedConsumedQuantity` = **170** (unitCode `MTQ`)  
  The estimate of water and the city's levy for April 2026 to March 2027: this year's use.
- `OnAccountPayment/Note` = **The payments on account planned for water and the city's levy in the next account year.**  
  What the schedule is.
- `OnAccountPayment/PaymentTerms/Amount` = **39.24** (currencyID `XBL`)  
  A twelfth of the estimate's cost of water and the city's levy, part of the monthly direct debit.
- `OnAccountPayment/PaymentTerms/ValidityPeriod/StartDate` = **2026-04-01**  
  From April.
- `OnAccountPayment/PaymentTerms/ValidityPeriod/EndDate` = **2027-03-31**  
  To the next annual reading.
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
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2025-04-01**  
  The account year.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `SupplierConsumption/Consumption/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  Drinking water is exempt.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **399.50** (currencyID `XBL`)  
  The water.
- `SupplierConsumption/Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  Exempt.
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
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **CSW-CP-38516-57-2526**  
  The water report of the account year.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Yearly consumption**  
  The name of code YEAR in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **YEAR** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: YEAR = Yearly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **170** (unitCode `MTQ`)  
  Used in the account year.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/BasicConsumedQuantity` = **170** (unitCode `MTQ`)  
  All at the one water tariff.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ResidentOccupantsNumeric` = **2**  
  People living in the flat.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ResidenceType` = **Apartment**  
  The name of code APT in the Trade Accord's residence type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ResidenceTypeCode` = **APT** (listID `urn:ubl-examples:world:codelist:ResidenceTypeCode`)  
  As a code. The code is from the Trade Accord's residence type list: APT = Apartment.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/HeatingType` = **District heating**  
  The name of code DH in the Trade Accord's heating type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/HeatingTypeCode` = **DH** (listID `urn:ubl-examples:world:codelist:HeatingTypeCode`)  
  As a code. The code is from the Trade Accord's heating type list: DH = District heating.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2025-04-01**  
  The account year.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/GuidanceDocumentReference/ID` = **CSW-SAVE-WATER**  
  The company's leaflet on saving water.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/DocumentReference/ID` = **CSW-QUALITY-2026-Q1**  
  The quarterly water quality report.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/DocumentReference/DocumentType` = **Water quality report**  
  The kind of document referred to, the water company's quarterly water quality report, in words: no list has an exact code for it.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionReportID` = **CSW-CP-38516-57-2425**  
  Last year's water report.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionType` = **Yearly consumption**  
  The name of code YEAR in the Trade Accord's consumption type list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionTypeCode` = **YEAR** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: YEAR = Yearly consumption.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/TotalConsumedQuantity` = **158** (unitCode `MTQ`)  
  What last year's report said.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/StartDate` = **2024-04-01**  
  Last year's account year.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/EndDate` = **2025-03-31**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-71844**  
  The water meter.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **158** (unitCode `MTQ`)  
  Last year's water.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **371.30** (currencyID `XBL`)  
  What it cost at the tariff, without the levy.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2024-04-01**  
  Last year's account year.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2025-03-31**  
  Its end.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/AverageAmount` = **385.40** (currencyID `XBL`)  
  The average of the last two years' water at the tariff, without tax.
- `SupplierConsumption/Consumption/EnergyWaterSupply/ConsumptionAverage/Description` = **The average of the last two years is 164 m³.**  
  For comparison.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **399.50** (currencyID `XBL`)  
  The lines of this part.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **399.50** (currencyID `XBL`)  
  Nothing added: exempt, or outside the tax.
- `SupplierConsumption/Contract/ID` = **CSW-C-311790**  
  The supply contract for water and heat: one account.
- `SupplierConsumption/Contract/ContractType` = **Water and district heat supply**  
  Its kind.
- `SupplierConsumption/Contract/ValidityPeriod/StartDate` = **2024-09-01**  
  In force since the household moved in.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **170** (unitCode `MTQ`)  
  The household's water in the account year, from the annual readings.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **399.50** (currencyID `XBL`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **399.50** (currencyID `XBL`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2025-04-01**  
  The account year.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **CW-M3**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **CSW-CU-097315**  
  The subscriber's customer number with the utility.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Drinking water supply, per cubic metre.**  
  The tariff in words.
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
  The tariff.
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
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2025-04-01**  
  The account year.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **71.40** (currencyID `XBL`)  
  The lines of this part.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **71.40** (currencyID `XBL`)  
  Nothing added: exempt, or outside the tax.
- `SupplierConsumption/ConsumptionLine/ID` = **2**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **2**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **170** (unitCode `MTQ`)  
  The household's water use, on which the city charges its levy.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **71.40** (currencyID `XBL`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2025-04-01**  
  The account year.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **CSW-LEVY**  
  The supplier's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.**  
  The tariff in words.
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
  The tariff.
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  Per unit.
- `ConsumptionID` = **CSW-CP-38516-57-H-2526**  
  The district heat of the account year.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  A detailed specification. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **District heat**  
  The subscription.
- `TotalMeteredQuantity` = **6.6** (unitCode `MWH`)  
  Metered in the account year.
- `UtilityConsumptionPoint/ID` = **CSW-CP-38516-57-H**  
  The flat's connection to the district heating.
- `UtilityConsumptionPoint/Description` = **Gull Lane 57, Lumeport, district heating**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **CSW-CU-097315**  
  The subscriber's customer number with the utility.
- `UtilityConsumptionPoint/SubscriberType` = **Household**  
  The name of code HH in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **HH** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: HH = Household.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **6.6** (unitCode `MWH`)  
  Delivered in the account year.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `UtilityConsumptionPoint/Address/StreetName` = **Gull Lane**  
  Street of the postal address. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/BuildingNumber` = **57**  
  Building number of the postal address. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). As Robin Ashdale gives it.
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `UtilityConsumptionPoint/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Robin Ashdale gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `UtilityConsumptionPoint/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **CSW-H-71844**  
  The flat's heat meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Heat meter, flat**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  The register is read as it is.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **DIRECT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  Why: direct connection. The code is from the Trade Accord's meter constant type list: DIRECT = Direct connection.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **6.6** (unitCode `MWH`)  
  Delivered in the account year.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **CSW-H-71844-2603**  
  The annual reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Yearly reading**  
  The name of code Y in the Trade Accord's meter reading type list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **Y** (listID `urn:ubl-examples:world:codelist:MeterReadingTypeCode`)  
  As a code. The code is from the Trade Accord's meter reading type list: Y = Yearly reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2025-03-31**  
  Last year's annual reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **41.2** (unitCode `MWH`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This year's annual reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **47.8** (unitCode `MWH`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Read by the meter reader**  
  The name of code MANUAL in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **MANUAL** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: MANUAL = Read by the meter reader.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Read by the meter reader**  
  The name of code MANUAL in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **MANUAL** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: MANUAL = Read by the meter reader.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **6.6** (unitCode `MWH`)  
  The difference of the readings.
- `OnAccountPayment/EstimatedConsumedQuantity` = **6.6** (unitCode `MWH`)  
  The estimate of district heat for April 2026 to March 2027: this year's use.
- `OnAccountPayment/Note` = **The payments on account planned for district heat in the next account year.**  
  What the schedule is.
- `OnAccountPayment/PaymentTerms/Amount` = **54.18** (currencyID `XBL`)  
  A twelfth of the estimate's cost of district heat with the 6.500 % sales tax, part of the monthly direct debit.
- `OnAccountPayment/PaymentTerms/ValidityPeriod/StartDate` = **2026-04-01**  
  From April.
- `OnAccountPayment/PaymentTerms/ValidityPeriod/EndDate` = **2027-03-31**  
  To the next annual reading.
- `Consumption/UtilityStatementTypeCode` = **HEAT** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: HEAT = District heating.
- `Consumption/MainPeriod/StartDate` = **2025-04-01**  
  The account year.
- `Consumption/MainPeriod/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `Consumption/TaxTotal/TaxAmount` = **41.40** (currencyID `XBL`)  
  6.5 % sales tax on the heat.
- `Consumption/TaxTotal/TaxSubtotal/TaxableAmount` = **636.90** (currencyID `XBL`)  
  The heat and its correction.
- `Consumption/TaxTotal/TaxSubtotal/TaxAmount` = **41.40** (currencyID `XBL`)  
  6.5 % of it.
- `Consumption/TaxTotal/TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `Consumption/TaxTotal/TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Consumption/TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **CSW-CP-38516-57-H-2526**  
  The heat report of the account year.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Yearly consumption**  
  The name of code YEAR in the Trade Accord's consumption type list.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **YEAR** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: YEAR = Yearly consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **6.6** (unitCode `MWH`)  
  Heat used in the account year.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ResidentOccupantsNumeric` = **2**  
  People living in the flat.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumersEnergyLevelCode` = **LOW** (listID `urn:ubl-examples:world:codelist:ConsumersEnergyLevelCode`)  
  Below the average heat use of a flat of its size on the network. The code is from the Trade Accord's consumer's energy level list: LOW = Low consumer.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumersEnergyLevel` = **Low consumer**  
  The name of code LOW in the Trade Accord's consumer's energy level list.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2025-04-01**  
  The account year.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  The account year's end, the annual reading.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-H-71844**  
  The heat meter.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **6.3** (unitCode `MWH`)  
  Last year's heat.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **582.75** (currencyID `XBL`)  
  What it cost at the tariff, without tax.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2024-04-01**  
  Last year's account year.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2025-03-31**  
  Its end.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionType` = **District heating cooling correction**  
  The name of code COOL in the Trade Accord's consumption correction type list.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionTypeCode` = **COOL** (listID `urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption correction type list: COOL = District heating cooling correction.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/MeterNumber` = **CSW-H-71844**  
  The heat meter, which also measures the temperatures.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/ActualTemperatureReductionQuantity` = **31** (unitCode `CEL`)  
  The water cooled by this much in the flat, on average.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/NormalTemperatureReductionQuantity` = **35** (unitCode `CEL`)  
  The network's standard cooling.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/DifferenceTemperatureReductionQuantity` = **-4** (unitCode `CEL`)  
  Degrees short.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/Description` = **Poor cooling makes the network pump more water: 1.00 per MWh for each degree short of the standard.**  
  Why and how.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionUnitAmount` = **4.00** (currencyID `XBL`)  
  Per MWh: the rate per degree times the degrees short.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/ConsumptionEnergyQuantity` = **6.6** (unitCode `MWH`)  
  The year's heat the correction applies to (the district-heating element).
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/ConsumptionWaterQuantity` = **183** (unitCode `MTQ`)  
  The network water that passed the flat in the year.
- `Consumption/EnergyWaterSupply/EnergyWaterConsumptionCorrection/CorrectionAmount` = **26.40** (currencyID `XBL`)  
  The unit amount times the year's heat: line 4 of the settlement bill.
- `Consumption/LegalMonetaryTotal/LineExtensionAmount` = **636.90** (currencyID `XBL`)  
  The heat and its correction.
- `Consumption/LegalMonetaryTotal/PayableAmount` = **678.30** (currencyID `XBL`)  
  With the sales tax.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:utility-statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9924052627</cbc:ProfileExecutionID>
  <cbc:ID>9424052721</cbc:ID>
  <cbc:UUID>8ee8ec8d-3357-524c-81b1-479a651b524c</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>15:10:00-01:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
  <cbc:Note>This annual statement explains the year's water and heat behind your settlement bill, and sets the payments on account for the next year.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cac:ParentDocumentReference>
    <cbc:ID>CSW-C-311790-2603</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>CSW-TARIFF-2026</cbc:ID>
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
    <cbc:EstimatedConsumedQuantity unitCode="MTQ">170</cbc:EstimatedConsumedQuantity>
    <cbc:Note>The one monthly direct debit for water, levy and heat from April 2026: 94 lume, a twelfth of the year's estimate with the sales tax on the heat, rounded up to a whole lume; it was 84 lume.</cbc:Note>
    <cac:PaymentTerms>
      <cbc:Note>Collected by direct debit on the first working day of each month.</cbc:Note>
      <cbc:Amount currencyID="XBL">94.00</cbc:Amount>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-04-01</cbc:StartDate>
        <cbc:EndDate>2027-03-31</cbc:EndDate>
      </cac:ValidityPeriod>
    </cac:PaymentTerms>
  </cac:MainOnAccountPayment>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>CSW-CP-38516-57-2526</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>Water</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="MTQ">170</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>CSW-CP-38516-57</cbc:ID>
      <cbc:Description>Gull Lane 57, Lumeport</cbc:Description>
      <cbc:SubscriberID>CSW-CU-097315</cbc:SubscriberID>
      <cbc:SubscriberType>Household</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">HH</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="MTQ">170</cbc:TotalDeliveredQuantity>
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
      <cac:UtilityMeter>
        <cbc:MeterNumber>CSW-W-71844</cbc:MeterNumber>
        <cbc:MeterName>Water meter, flat</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">DIRECT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="MTQ">170</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>CSW-W-71844-2603</cbc:ID>
          <cbc:MeterReadingType>Yearly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode listID="urn:ubl-examples:world:codelist:MeterReadingTypeCode">Y</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2025-03-31</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="MTQ">1674</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="MTQ">1844</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Read by the meter reader</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">MANUAL</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Read by the meter reader</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">MANUAL</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="MTQ">170</cbc:DeliveredQuantity>
        </cac:MeterReading>
        <cac:MeterProperty>
          <cbc:Name>Accuracy class</cbc:Name>
          <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">ACC</cbc:NameCode>
          <cbc:Value>1</cbc:Value>
          <cbc:ValueQualifier>Calibrated 2024</cbc:ValueQualifier>
        </cac:MeterProperty>
        <cac:MeterProperty>
          <cbc:Name>Permanent flow rate</cbc:Name>
          <cbc:ValueQuantity unitCode="MQH">2.5</cbc:ValueQuantity>
        </cac:MeterProperty>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:OnAccountPayment>
      <cbc:EstimatedConsumedQuantity unitCode="MTQ">170</cbc:EstimatedConsumedQuantity>
      <cbc:Note>The payments on account planned for water and the city's levy in the next account year.</cbc:Note>
      <cac:PaymentTerms>
        <cbc:Amount currencyID="XBL">39.24</cbc:Amount>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-04-01</cbc:StartDate>
          <cbc:EndDate>2027-03-31</cbc:EndDate>
        </cac:ValidityPeriod>
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
          <cbc:StartDate>2025-04-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
          <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="XBL">399.50</cbc:TaxableAmount>
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
            <cbc:ID>CSW-CP-38516-57-2526</cbc:ID>
            <cbc:ConsumptionType>Yearly consumption</cbc:ConsumptionType>
            <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">YEAR</cbc:ConsumptionTypeCode>
            <cbc:TotalConsumedQuantity unitCode="MTQ">170</cbc:TotalConsumedQuantity>
            <cbc:BasicConsumedQuantity unitCode="MTQ">170</cbc:BasicConsumedQuantity>
            <cbc:ResidentOccupantsNumeric>2</cbc:ResidentOccupantsNumeric>
            <cbc:ResidenceType>Apartment</cbc:ResidenceType>
            <cbc:ResidenceTypeCode listID="urn:ubl-examples:world:codelist:ResidenceTypeCode">APT</cbc:ResidenceTypeCode>
            <cbc:HeatingType>District heating</cbc:HeatingType>
            <cbc:HeatingTypeCode listID="urn:ubl-examples:world:codelist:HeatingTypeCode">DH</cbc:HeatingTypeCode>
            <cac:Period>
              <cbc:StartDate>2025-04-01</cbc:StartDate>
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
              <cbc:ConsumptionReportID>CSW-CP-38516-57-2425</cbc:ConsumptionReportID>
              <cbc:ConsumptionType>Yearly consumption</cbc:ConsumptionType>
              <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">YEAR</cbc:ConsumptionTypeCode>
              <cbc:TotalConsumedQuantity unitCode="MTQ">158</cbc:TotalConsumedQuantity>
              <cac:Period>
                <cbc:StartDate>2024-04-01</cbc:StartDate>
                <cbc:EndDate>2025-03-31</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionReportReference>
            <cac:ConsumptionHistory>
              <cbc:MeterNumber>CSW-W-71844</cbc:MeterNumber>
              <cbc:Quantity unitCode="MTQ">158</cbc:Quantity>
              <cbc:Amount currencyID="XBL">371.30</cbc:Amount>
              <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
              <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
              <cac:Period>
                <cbc:StartDate>2024-04-01</cbc:StartDate>
                <cbc:EndDate>2025-03-31</cbc:EndDate>
              </cac:Period>
            </cac:ConsumptionHistory>
          </cac:ConsumptionReport>
          <cac:ConsumptionAverage>
            <cbc:AverageAmount currencyID="XBL">385.40</cbc:AverageAmount>
            <cbc:Description>The average of the last two years is 164 m³.</cbc:Description>
          </cac:ConsumptionAverage>
        </cac:EnergyWaterSupply>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XBL">399.50</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XBL">399.50</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:Contract>
        <cbc:ID>CSW-C-311790</cbc:ID>
        <cbc:ContractType>Water and district heat supply</cbc:ContractType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2024-09-01</cbc:StartDate>
        </cac:ValidityPeriod>
      </cac:Contract>
      <cac:ConsumptionLine>
        <cbc:ID>1</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MTQ">170</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XBL">399.50</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">399.50</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2025-04-01</cbc:StartDate>
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
          <cbc:StartDate>2025-04-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XBL">71.40</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XBL">71.40</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:ConsumptionLine>
        <cbc:ID>2</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>2</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MTQ">170</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XBL">71.40</cbc:LineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2025-04-01</cbc:StartDate>
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
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>CSW-CP-38516-57-H-2526</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>District heat</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="MWH">6.6</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>CSW-CP-38516-57-H</cbc:ID>
      <cbc:Description>Gull Lane 57, Lumeport, district heating</cbc:Description>
      <cbc:SubscriberID>CSW-CU-097315</cbc:SubscriberID>
      <cbc:SubscriberType>Household</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">HH</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="MWH">6.6</cbc:TotalDeliveredQuantity>
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
      <cac:UtilityMeter>
        <cbc:MeterNumber>CSW-H-71844</cbc:MeterNumber>
        <cbc:MeterName>Heat meter, flat</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">DIRECT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="MWH">6.6</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>CSW-H-71844-2603</cbc:ID>
          <cbc:MeterReadingType>Yearly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode listID="urn:ubl-examples:world:codelist:MeterReadingTypeCode">Y</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2025-03-31</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="MWH">41.2</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="MWH">47.8</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Read by the meter reader</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">MANUAL</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Read by the meter reader</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">MANUAL</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="MWH">6.6</cbc:DeliveredQuantity>
        </cac:MeterReading>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:OnAccountPayment>
      <cbc:EstimatedConsumedQuantity unitCode="MWH">6.6</cbc:EstimatedConsumedQuantity>
      <cbc:Note>The payments on account planned for district heat in the next account year.</cbc:Note>
      <cac:PaymentTerms>
        <cbc:Amount currencyID="XBL">54.18</cbc:Amount>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-04-01</cbc:StartDate>
          <cbc:EndDate>2027-03-31</cbc:EndDate>
        </cac:ValidityPeriod>
      </cac:PaymentTerms>
    </cac:OnAccountPayment>
    <cac:Consumption>
      <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">HEAT</cbc:UtilityStatementTypeCode>
      <cac:MainPeriod>
        <cbc:StartDate>2025-04-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:MainPeriod>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">41.40</cbc:TaxAmount>
        <cac:TaxSubtotal>
          <cbc:TaxableAmount currencyID="XBL">636.90</cbc:TaxableAmount>
          <cbc:TaxAmount currencyID="XBL">41.40</cbc:TaxAmount>
          <cac:TaxCategory>
            <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
            <cbc:Percent>6.5</cbc:Percent>
            <cac:TaxScheme>
              <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
        </cac:TaxSubtotal>
      </cac:TaxTotal>
      <cac:EnergyWaterSupply>
        <cac:ConsumptionReport>
          <cbc:ID>CSW-CP-38516-57-H-2526</cbc:ID>
          <cbc:ConsumptionType>Yearly consumption</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">YEAR</cbc:ConsumptionTypeCode>
          <cbc:TotalConsumedQuantity unitCode="MWH">6.6</cbc:TotalConsumedQuantity>
          <cbc:ResidentOccupantsNumeric>2</cbc:ResidentOccupantsNumeric>
          <cbc:ConsumersEnergyLevelCode listID="urn:ubl-examples:world:codelist:ConsumersEnergyLevelCode">LOW</cbc:ConsumersEnergyLevelCode>
          <cbc:ConsumersEnergyLevel>Low consumer</cbc:ConsumersEnergyLevel>
          <cac:Period>
            <cbc:StartDate>2025-04-01</cbc:StartDate>
            <cbc:EndDate>2026-03-31</cbc:EndDate>
          </cac:Period>
          <cac:ConsumptionHistory>
            <cbc:MeterNumber>CSW-H-71844</cbc:MeterNumber>
            <cbc:Quantity unitCode="MWH">6.3</cbc:Quantity>
            <cbc:Amount currencyID="XBL">582.75</cbc:Amount>
            <cac:Period>
              <cbc:StartDate>2024-04-01</cbc:StartDate>
              <cbc:EndDate>2025-03-31</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionHistory>
        </cac:ConsumptionReport>
        <cac:EnergyWaterConsumptionCorrection>
          <cbc:CorrectionType>District heating cooling correction</cbc:CorrectionType>
          <cbc:CorrectionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionCorrectionTypeCode">COOL</cbc:CorrectionTypeCode>
          <cbc:MeterNumber>CSW-H-71844</cbc:MeterNumber>
          <cbc:ActualTemperatureReductionQuantity unitCode="CEL">31</cbc:ActualTemperatureReductionQuantity>
          <cbc:NormalTemperatureReductionQuantity unitCode="CEL">35</cbc:NormalTemperatureReductionQuantity>
          <cbc:DifferenceTemperatureReductionQuantity unitCode="CEL">-4</cbc:DifferenceTemperatureReductionQuantity>
          <cbc:Description>Poor cooling makes the network pump more water: 1.00 per MWh for each degree short of the standard.</cbc:Description>
          <cbc:CorrectionUnitAmount currencyID="XBL">4.00</cbc:CorrectionUnitAmount>
          <cbc:ConsumptionEnergyQuantity unitCode="MWH">6.6</cbc:ConsumptionEnergyQuantity>
          <cbc:ConsumptionWaterQuantity unitCode="MTQ">183</cbc:ConsumptionWaterQuantity>
          <cbc:CorrectionAmount currencyID="XBL">26.40</cbc:CorrectionAmount>
        </cac:EnergyWaterConsumptionCorrection>
      </cac:EnergyWaterSupply>
      <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="XBL">636.90</cbc:LineExtensionAmount>
        <cbc:PayableAmount currencyID="XBL">678.30</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:Consumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
