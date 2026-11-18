# Utility Statement: Coastal State Water Company to Brightmarket Stores

*Example 5 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The shop's water consumption, read from its meter.

[The XML file](05-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **CSWC-DOC-26-0318**  
  The utility's statement number.
- `UUID` = **7bdfb021-49a1-5341-b641-0343b4c0240e**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **11:55:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of utility the statement is about. The code is from the Trade Accord's utility type list: WATER = Water.
- `Note` = **This statement explains the consumption behind your bill.**  
  What the statement is.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the utility's currency; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `AccountingCostCode` = **8100**  
  The customer's cost centre, as on the bill.
- `AccountingCost` = **Store energy and water**  
  The cost centre in words.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **CSWC-INV-26-0317**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CSWC-INV-26-0317 is the example utilities/06, a Invoice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Invoice.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **CSWC-TARIFF-2026**  
  The utility's tariff sheet for 2026.
- `DocumentTypeCode` = **TARIFF** (listID `urn:ubl-examples:world:codelist:DocumentTypeCode`)  
  What the document is. The code is from the Trade Accord's document type list: TARIFF = Tariff.
- `DocumentDescription` = **Prices per unit and the terms of supply.**  
  What it holds.

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
- `Contact/Telephone` = **+999 2 38 2692 2192**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Coastal State Water Company (world/parties.json).
- `Contact/ElectronicMail` = **billing@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Coastal State Water Company (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Coastal State Water Company (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brightmarket Stores (world/parties.json).
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); identity of Brightmarket Stores (world/parties.json).
- `Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Contact/Department` = **Finance**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2511 0411**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Contact/ElectronicMail` = **payables@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Brightmarket Stores**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **CSW-CP-38510-411-2603**  
  The consumption of the point in March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  A detailed specification. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `Note` = **Shop, Lumeport**  
  The point.
- `TotalMeteredQuantity` = **86** (unitCode `MTQ`)  
  Metered in March.
- `UtilityConsumptionPoint/ID` = **CSW-CP-38510-411**  
  The connection's number.
- `UtilityConsumptionPoint/Description` = **Shop, Lumeport**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **CSW-C-260118**  
  The contract it belongs to.
- `UtilityConsumptionPoint/SubscriberType` = **Commercial**  
  The name of code COM in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **COM** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: COM = Commercial.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **86** (unitCode `MTQ`)  
  Delivered in March.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `UtilityConsumptionPoint/Address/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `UtilityConsumptionPoint/Address/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `UtilityConsumptionPoint/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **CSW-W-55102**  
  The meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Water meter, shop**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  The register is multiplied by this.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **DIRECT** (listID `urn:ubl-examples:world:codelist:MeterConstantTypeCode`)  
  Why: direct. The code is from the Trade Accord's meter constant type list: DIRECT = Direct connection.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **86** (unitCode `MTQ`)  
  Delivered in March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **CSW-W-55102-2603**  
  The reading of March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Monthly reading**  
  The name of code M in the Trade Accord's meter reading type list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **M** (listID `urn:ubl-examples:world:codelist:MeterReadingTypeCode`)  
  As a code. The code is from the Trade Accord's meter reading type list: M = Monthly reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2026-02-28**  
  The previous reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **4212** (unitCode `MTQ`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **4298** (unitCode `MTQ`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Remote reading**  
  The name of code REMOTE in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **REMOTE** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: REMOTE = Remote reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Remote reading**  
  The name of code REMOTE in the Trade Accord's meter reading method list.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **REMOTE** (listID `urn:ubl-examples:world:codelist:MeterReadingMethodCode`)  
  As a code. The code is from the Trade Accord's meter reading method list: REMOTE = Remote reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **86** (unitCode `MTQ`)  
  The difference of the readings.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Accuracy class**  
  The name of code ACC in the Trade Accord's item property name list.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/NameCode` = **ACC** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  As a code. The code is from the Trade Accord's item property name list: ACC = Accuracy class.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Value` = **1**  
  Class 1.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQualifier` = **Calibrated 2024**  
  When it was checked.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Maximum flow**  
  A rating of the meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQuantity` = **2.5** (unitCode `MQH`)  
  Its value.
- `Consumption/UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: WATER = Water.
- `Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `Consumption/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  The tax of this point's consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **CSW-CP-38510-411-2603**  
  The consumption report of the point for March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Description` = **March consumption of Shop, Lumeport.**  
  In words.
- `Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **86** (unitCode `MTQ`)  
  Used in March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/BasicConsumedQuantity` = **86** (unitCode `MTQ`)  
  All at the basic tariff: no reduced-rate hours.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2026-03-01**  
  March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  Its last day.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionReportID` = **CSW-CP-38510-411-2602**  
  The report of February.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionType` = **Monthly consumption**  
  The name of code MON in the Trade Accord's consumption type list.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionTypeCode` = **MON** (listID `urn:ubl-examples:world:codelist:ConsumptionTypeCode`)  
  As a code. The code is from the Trade Accord's consumption type list: MON = Monthly consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/TotalConsumedQuantity` = **79** (unitCode `MTQ`)  
  What February's report said.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/StartDate` = **2026-02-01**  
  February.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/EndDate` = **2026-02-28**  
  Its last day.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-55102**  
  The meter.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **81** (unitCode `MTQ`)  
  The month's consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **190.35** (currencyID `XBL`)  
  What it cost at the tariff.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Description` = **Earlier month.**  
  For comparison.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-01-01**  
  The month.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-01-31**  
  Its end.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-55102**  
  The meter.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **79** (unitCode `MTQ`)  
  The month's consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **185.65** (currencyID `XBL`)  
  What it cost at the tariff.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **NORMAL** (listID `urn:ubl-examples:world:codelist:ConsumptionLevelCode`)  
  Within the usual range. The code is from the Trade Accord's consumption level list: NORMAL = Normal.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  The name of code NORMAL in the Trade Accord's consumption level list.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Description` = **Earlier month.**  
  For comparison.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-02-01**  
  The month.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-02-28**  
  Its end.
- `Consumption/EnergyWaterSupply/ConsumptionAverage/AverageAmount` = **202.10** (currencyID `XBL`)  
  What this month cost.
- `Consumption/EnergyWaterSupply/ConsumptionAverage/Description` = **The average over the last three months is 82 m³.**  
  For comparison.
- `Consumption/LegalMonetaryTotal/LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  The consumption.
- `Consumption/LegalMonetaryTotal/PayableAmount` = **202.10** (currencyID `XBL`)  
  With its tax.
- `SupplierConsumption/Description` = **The supply under the customer's contract.**  
  What follows.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Coastal State Water Company**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/UtilityStatementTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The supply under the contract. The code is from the Trade Accord's utility type list: WATER = Water.
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  The line.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **202.10** (currencyID `XBL`)  
  With its tax.
- `SupplierConsumption/Contract/ID` = **CSW-C-260118**  
  The supply contract.
- `SupplierConsumption/Contract/ContractType` = **Water supply**  
  Its kind.
- `SupplierConsumption/Contract/ValidityPeriod/StartDate` = **2024-01-01**  
  In force since.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **86** (unitCode `MTQ`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **202.10** (currencyID `XBL`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/Delivery/DeliveryLocation/Description` = **The consumption point of the statement.**  
  Where it was delivered.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **CW-M3**  
  The utility's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **CSW-C-260118**  
  The customer's contract.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Water**  
  The name of code WATER in the Trade Accord's utility type list.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The supply the item is for, as a code. The code is from the Trade Accord's utility type list: WATER = Water.
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
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **CSW-C-260118**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **2.35** (currencyID `XBL`)  
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
  <cbc:ID>CSWC-DOC-26-0318</cbc:ID>
  <cbc:UUID>7bdfb021-49a1-5341-b641-0343b4c0240e</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>11:55:00-01:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
  <cbc:Note>This statement explains the consumption behind your bill.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>8100</cbc:AccountingCostCode>
  <cbc:AccountingCost>Store energy and water</cbc:AccountingCost>
  <cac:ParentDocumentReference>
    <cbc:ID>CSWC-INV-26-0317</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>CSWC-TARIFF-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentTypeCode">TARIFF</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Prices per unit and the terms of supply.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
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
      <cbc:Telephone>+999 2 38 2692 2192</cbc:Telephone>
      <cbc:ElectronicMail>billing@coastalwater.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9522610900002</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:TradePartyName>
      <cbc:Name>Brightmarket</cbc:Name>
    </cac:TradePartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-579130</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Accounts payable</cbc:Name>
      <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
      <cbc:ElectronicMail>payables@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>CSW-CP-38510-411-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:Note>Shop, Lumeport</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="MTQ">86</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>CSW-CP-38510-411</cbc:ID>
      <cbc:Description>Shop, Lumeport</cbc:Description>
      <cbc:SubscriberID>CSW-C-260118</cbc:SubscriberID>
      <cbc:SubscriberType>Commercial</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">COM</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="MTQ">86</cbc:TotalDeliveredQuantity>
      <cac:Address>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Market Street</cbc:StreetName>
        <cbc:BuildingNumber>50</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38515</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:Address>
      <cac:UtilityMeter>
        <cbc:MeterNumber>CSW-W-55102</cbc:MeterNumber>
        <cbc:MeterName>Water meter, shop</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode listID="urn:ubl-examples:world:codelist:MeterConstantTypeCode">DIRECT</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="MTQ">86</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>CSW-W-55102-2603</cbc:ID>
          <cbc:MeterReadingType>Monthly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode listID="urn:ubl-examples:world:codelist:MeterReadingTypeCode">M</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2026-02-28</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="MTQ">4212</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="MTQ">4298</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Remote reading</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">REMOTE</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Remote reading</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode listID="urn:ubl-examples:world:codelist:MeterReadingMethodCode">REMOTE</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="MTQ">86</cbc:DeliveredQuantity>
        </cac:MeterReading>
        <cac:MeterProperty>
          <cbc:Name>Accuracy class</cbc:Name>
          <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">ACC</cbc:NameCode>
          <cbc:Value>1</cbc:Value>
          <cbc:ValueQualifier>Calibrated 2024</cbc:ValueQualifier>
        </cac:MeterProperty>
        <cac:MeterProperty>
          <cbc:Name>Maximum flow</cbc:Name>
          <cbc:ValueQuantity unitCode="MQH">2.5</cbc:ValueQuantity>
        </cac:MeterProperty>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:Consumption>
      <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
      <cac:MainPeriod>
        <cbc:StartDate>2026-03-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:MainPeriod>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:EnergyWaterSupply>
        <cac:ConsumptionReport>
          <cbc:ID>CSW-CP-38510-411-2603</cbc:ID>
          <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
          <cbc:Description>March consumption of Shop, Lumeport.</cbc:Description>
          <cbc:TotalConsumedQuantity unitCode="MTQ">86</cbc:TotalConsumedQuantity>
          <cbc:BasicConsumedQuantity unitCode="MTQ">86</cbc:BasicConsumedQuantity>
          <cac:Period>
            <cbc:StartDate>2026-03-01</cbc:StartDate>
            <cbc:EndDate>2026-03-31</cbc:EndDate>
          </cac:Period>
          <cac:ConsumptionReportReference>
            <cbc:ConsumptionReportID>CSW-CP-38510-411-2602</cbc:ConsumptionReportID>
            <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
            <cbc:ConsumptionTypeCode listID="urn:ubl-examples:world:codelist:ConsumptionTypeCode">MON</cbc:ConsumptionTypeCode>
            <cbc:TotalConsumedQuantity unitCode="MTQ">79</cbc:TotalConsumedQuantity>
            <cac:Period>
              <cbc:StartDate>2026-02-01</cbc:StartDate>
              <cbc:EndDate>2026-02-28</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionReportReference>
          <cac:ConsumptionHistory>
            <cbc:MeterNumber>CSW-W-55102</cbc:MeterNumber>
            <cbc:Quantity unitCode="MTQ">81</cbc:Quantity>
            <cbc:Amount currencyID="XBL">190.35</cbc:Amount>
            <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
            <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
            <cbc:Description>Earlier month.</cbc:Description>
            <cac:Period>
              <cbc:StartDate>2026-01-01</cbc:StartDate>
              <cbc:EndDate>2026-01-31</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionHistory>
          <cac:ConsumptionHistory>
            <cbc:MeterNumber>CSW-W-55102</cbc:MeterNumber>
            <cbc:Quantity unitCode="MTQ">79</cbc:Quantity>
            <cbc:Amount currencyID="XBL">185.65</cbc:Amount>
            <cbc:ConsumptionLevelCode listID="urn:ubl-examples:world:codelist:ConsumptionLevelCode">NORMAL</cbc:ConsumptionLevelCode>
            <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
            <cbc:Description>Earlier month.</cbc:Description>
            <cac:Period>
              <cbc:StartDate>2026-02-01</cbc:StartDate>
              <cbc:EndDate>2026-02-28</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionHistory>
        </cac:ConsumptionReport>
        <cac:ConsumptionAverage>
          <cbc:AverageAmount currencyID="XBL">202.10</cbc:AverageAmount>
          <cbc:Description>The average over the last three months is 82 m³.</cbc:Description>
        </cac:ConsumptionAverage>
      </cac:EnergyWaterSupply>
      <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
        <cbc:PayableAmount currencyID="XBL">202.10</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:Consumption>
    <cac:SupplierConsumption>
      <cbc:Description>The supply under the customer's contract.</cbc:Description>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Coastal State Water Company</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brightmarket Stores</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:UtilityStatementTypeCode>
        <cac:MainPeriod>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XBL">202.10</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:Contract>
        <cbc:ID>CSW-C-260118</cbc:ID>
        <cbc:ContractType>Water supply</cbc:ContractType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2024-01-01</cbc:StartDate>
        </cac:ValidityPeriod>
      </cac:Contract>
      <cac:ConsumptionLine>
        <cbc:ID>1</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MTQ">86</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">202.10</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:Delivery>
          <cac:DeliveryLocation>
            <cbc:Description>The consumption point of the statement.</cbc:Description>
          </cac:DeliveryLocation>
        </cac:Delivery>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>CW-M3</cbc:ID>
          <cbc:SubscriberID>CSW-C-260118</cbc:SubscriberID>
          <cbc:SubscriberType>Water</cbc:SubscriberType>
          <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">WATER</cbc:SubscriberTypeCode>
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
            <cbc:ID>CSW-C-260118</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XBL">2.35</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
