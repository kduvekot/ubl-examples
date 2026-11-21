# Utility Statement: Selanu Telecom to Velumi Trading

*Example 12 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

Calls, data and subscriptions per telephone line of the buyer, in the telecommunications supply structure.

[The XML file](12-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:utility-statement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Utility statement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **STL-TX-26-75183**  
  The collaboration this document belongs to: Selanu Telecom's bill for March to Velumi. Selanu Telecom started it and gave it this identifier, which every document of it repeats.
- `ID` = **STL-UST-26-75398**  
  The utility's statement number.
- `UUID` = **7b60d4fc-8fd7-5124-9e01-cfc520caed86**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **17:37:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `UtilityStatementTypeCode` = **TEL** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of utility the statement is about. The code is from the Trade Accord's utility type list: TEL = Telephone.
- `Note` = **Mikake votetaka hanano mofilufo kisala vepili vafosu.** (languageID `qal`)  
  The note in Lisavan, the sender's language: What the statement is.
- `Note` = **This statement explains the consumption behind your bill.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: What the statement is.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the utility's currency; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `AccountingCostCode` = **700**  
  The customer's cost centre, as on the bill.
- `AccountingCost` = **Telephone and data**  
  The cost centre in words.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **STL-C-1077-2603**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: STL-C-1077-2603 is the example utilities/13, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **STL-TARIFF-2026**  
  The utility's tariff sheet for 2026.
- `DocumentTypeCode` = **TARIFF** (listID `urn:ubl-examples:world:codelist:DocumentTypeCode`)  
  What the document is. The code is from the Trade Accord's document type list: TARIFF = Tariff.
- `DocumentDescription` = **Prices per unit and the terms of supply.**  
  What it holds.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Telecom gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Telecom**  
  The trading name; as Selanu Telecom gives it.
- `Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: kopele.
- `PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Telecom gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Telecom gives it.
- `PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Telecom gives it.
- `PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. As Selanu Telecom gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Telecom gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); as Selanu Telecom gives it.
- `Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Selanu Telecom gives it.
- `Contact/Department` = **Business sales**  
  The department the desk belongs to; as Selanu Telecom gives it.
- `Contact/Telephone` = **+999 3 727 3193**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Telecom gives it.
- `Contact/ElectronicMail` = **billing@selanutelecom.example**  
  The contact's e-mail address; as Selanu Telecom gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Selanu Telecom gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Telecom gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Velumi Trading gives it.
- `Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Contact/Department` = **Finance**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Contact/Telephone` = **+999 3 729 5794**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `Contact/ElectronicMail` = **payables@velumi.example**  
  The contact's e-mail address; as Velumi Trading gives it.
- `Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Velumi Trading gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Velumi Trading**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **STL-1077-2603**  
  The telecom consumption of March.
- `SpecificationTypeCode` = **DETAILED** (listID `urn:ubl-examples:world:codelist:SpecificationTypeCode`)  
  With the calls. The code is from the Trade Accord's specification type list: DETAILED = Detailed.
- `TotalMeteredQuantity` = **35** (unitCode `E34`)  
  The data beyond the subscriptions.
- `UtilityConsumptionPoint/ID` = **STL-CP-1077**  
  The company's connection.
- `UtilityConsumptionPoint/Description` = **Office of Velumi Trading, Selanu**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **STL-CU-20418**  
  The subscriber's customer number with the telecom company; the contract number stays in the contract.
- `UtilityConsumptionPoint/SubscriberType` = **Business**  
  The name of code BUS in the Trade Accord's subscriber type list.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **BUS** (listID `urn:ubl-examples:world:codelist:SubscriberTypeCode`)  
  As a code. The code is from the Trade Accord's subscriber type list: BUS = Business.
- `UtilityConsumptionPoint/Address/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `UtilityConsumptionPoint/Address/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `UtilityConsumptionPoint/Address/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `UtilityConsumptionPoint/Address/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `UtilityConsumptionPoint/Address/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `UtilityConsumptionPoint/Address/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consumption/UtilityStatementTypeCode` = **TEL** (listID `urn:ubl-examples:world:codelist:UtilityTypeCode`)  
  The kind of supply. The code is from the Trade Accord's utility type list: TEL = Telephone.
- `Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `Consumption/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance: it lowers the amount.
- `Consumption/AllowanceCharge/AllowanceChargeReasonCode` = **95** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 95 = Discount.
- `Consumption/AllowanceCharge/AllowanceChargeReason` = **Business bundle discount**  
  The reason in words.
- `Consumption/AllowanceCharge/MultiplierFactorNumeric` = **0.05**  
  5 %.
- `Consumption/AllowanceCharge/Amount` = **6.354** (currencyID `XLC`)  
  5 % of the six subscriptions.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyType` = **Business lines and data**  
  The name of code BUS in the Trade Accord's telecommunications supply type list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyTypeCode` = **BUS** (listID `urn:ubl-examples:world:codelist:TelecomSupplyTypeCode`)  
  As a code. The code is from the Trade Accord's telecommunications supply type list: BUS = Business lines and data.
- `Consumption/TelecommunicationsSupply/PrivacyCode` = **MASKED** (listID `urn:ubl-examples:world:codelist:PrivacyCode`)  
  Numbers called inside the island are not listed; calls abroad are, their last digits masked. The code is from the Trade Accord's privacy list: MASKED = Numbers masked.
- `Consumption/TelecommunicationsSupply/Description` = **Six business lines and a mobile data pool.**  
  In words.
- `Consumption/TelecommunicationsSupply/TotalAmount` = **146.224** (currencyID `XLC`)  
  The telecom supply of March.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **1**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1850**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line 1 of the six of subscription STL-L-BUS6, with calls on the island included.**  
  The subscription, as the invoice line names it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island; the bundle discount is given once, on the whole supply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-1**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy): no number, a word where UBL asks for the number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **140** (unitCode `MIN`)  
  Minutes called on the island: UBL's quantity is "the number of calls" and has no sibling for a duration.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **C-0311-01**  
  A call.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-11**  
  The day.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **10:14:00+00:00**  
  The time; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **+999 2 5121 955 *****  
  The distributor in Bayvarra, its last digits masked as the privacy code says.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **International: a call to Bayvarra**  
  The name of code INT in the Trade Accord's telecommunications service category list, followed by the detail of this case: the call went to the distributor in Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategoryCode` = **INT** (listID `urn:ubl-examples:world:codelist:TelecomServiceCategoryCode`)  
  As a code. The code is from the Trade Accord's telecommunications service category list: INT = International.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **12** (unitCode `MIN`)  
  Twelve minutes.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCall` = **Outgoing**  
  The name of code OUT in the Trade Accord's telecommunications call type list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCallCode` = **OUT** (listID `urn:ubl-examples:world:codelist:TelecomCallTypeCode`)  
  As a code. The code is from the Trade Accord's telecommunications call type list: OUT = Outgoing.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallBaseAmount` = **0.050** (currencyID `XLC`)  
  The set-up charge of a call abroad, the base of every call.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  The set-up and the twelve minutes, less the allowance: nothing to pay.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/PriceAmount` = **0.2** (currencyID `XLC`)  
  The tariff per minute for calls abroad.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/BaseQuantity` = **1** (unitCode `MIN`)  
  Per minute.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country called. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/AllowanceChargeReasonCode` = **64** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 64 = Special agreement.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/AllowanceChargeReason` = **Calls to the Trade Accord countries are included in the subscription**  
  Why the service costs nothing.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/Amount` = **2.450** (currencyID `XLC`)  
  The whole charge of the call: 0.050 set-up and 12 minutes at 0.200.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/Amount` = **0.050** (currencyID `XLC`)  
  The set-up charge of the call.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/Duty` = **Set-up**  
  The name of code SETUP in the Trade Accord's telecommunications duty list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDuty/DutyCode` = **SETUP** (listID `urn:ubl-examples:world:codelist:TelecomDutyCode`)  
  As a code. The code is from the Trade Accord's telecommunications duty list: SETUP = Set-up.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TimeDuty/Amount` = **2.400** (currencyID `XLC`)  
  12 minutes at 0.200.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TimeDuty/Duty` = **Per minute**  
  The name of code MIN in the Trade Accord's telecommunications duty list.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TimeDuty/DutyCode` = **MIN** (listID `urn:ubl-examples:world:codelist:TelecomDutyCode`)  
  As a code. The code is from the Trade Accord's telecommunications duty list: MIN = Per minute.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **2**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1851**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line 2 of the six of subscription STL-L-BUS6, with calls on the island included.**  
  The subscription, as the invoice line names it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island; the bundle discount is given once, on the whole supply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-2**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy): no number, a word where UBL asks for the number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **165** (unitCode `MIN`)  
  Minutes called on the island: UBL's quantity is "the number of calls" and has no sibling for a duration.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **V-0320-02**  
  A film rented on line 2.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-20**  
  The day.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **12:30:00+00:00**  
  At lunch; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **video**  
  The operator's video service, no number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Video on demand**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/MovieTitle` = **Safe Lifting in the Warehouse**  
  A training film the trader's staff watched.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/PayPerView` = **true**  
  Paid per film.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **1** (unitCode `EA`)  
  One film.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  The film's price less the allowance.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/PriceAmount` = **2** (currencyID `XLC`)  
  The price of a training film.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/BaseQuantity` = **1** (unitCode `EA`)  
  Per film.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/ChargeIndicator` = **false**  
  An allowance.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/AllowanceChargeReasonCode` = **64** (listID `UN/EDIFACT EDED 5189`)  
  The reason for the allowance as a code of UN/EDIFACT 5189. The code is from the world's copy of UN/EDIFACT 5189 Allowance or charge identification: 64 = Special agreement.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/AllowanceChargeReason` = **Training films are included in the business bundle**  
  Why the service costs nothing.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/AllowanceCharge/Amount` = **2.000** (currencyID `XLC`)  
  The film's price.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **3**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1852**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line 3 of the six of subscription STL-L-BUS6, with calls on the island included.**  
  The subscription, as the invoice line names it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island; the bundle discount is given once, on the whole supply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-3**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy): no number, a word where UBL asks for the number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **190** (unitCode `MIN`)  
  Minutes called on the island: UBL's quantity is "the number of calls" and has no sibling for a duration.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **4**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1853**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line 4 of the six of subscription STL-L-BUS6, with calls on the island included.**  
  The subscription, as the invoice line names it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island; the bundle discount is given once, on the whole supply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-4**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy): no number, a word where UBL asks for the number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **215** (unitCode `MIN`)  
  Minutes called on the island: UBL's quantity is "the number of calls" and has no sibling for a duration.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **5**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1854**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line 5 of the six of subscription STL-L-BUS6, with calls on the island included.**  
  The subscription, as the invoice line names it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island; the bundle discount is given once, on the whole supply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-5**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy): no number, a word where UBL asks for the number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **240** (unitCode `MIN`)  
  Minutes called on the island: UBL's quantity is "the number of calls" and has no sibling for a duration.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **6**  
  A business line.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1855**  
  The line's number; +999 is reserved, no real country's code.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Business line 6 of the six of subscription STL-L-BUS6, with calls on the island included.**  
  The subscription, as the invoice line names it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **21.180** (currencyID `XLC`)  
  The monthly subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **21.180** (currencyID `XLC`)  
  No tax on the island; the bundle discount is given once, on the whole supply.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **S-03-6**  
  The month's calls on the island, summed: they are included.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **island**  
  Calls within the island, not listed (privacy): no number, a word where UBL asks for the number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Island calls**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **265** (unitCode `MIN`)  
  Minutes called on the island: UBL's quantity is "the number of calls" and has no sibling for a duration.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **0.000** (currencyID `XLC`)  
  Included in the subscription.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/ID` = **7**  
  The data pool, a line of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/PhoneNumber` = **+999 3 721 1856**  
  The data pool's own number, which the phones of the six lines share.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/Description` = **Mobile data pool STL-D-0042, shared by the six lines: 35 GB beyond the subscriptions in March, 4 GB of them roaming in Bayvarra.**  
  What it is, as the invoice lines name it.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/LineExtensionAmount` = **19.144** (currencyID `XLC`)  
  The data at the data tariff and the roaming at the roaming tariff.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TaxInclusiveLineExtensionAmount` = **19.144** (currencyID `XLC`)  
  No tax on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **D-03**  
  The month's data on the island beyond the subscriptions.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-01**  
  The start of the month the record sums: UBL asks every service record for a call date and time, a summary has none of its own.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **00:00:00+00:00**  
  The month's first minute; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **data**  
  Mobile data, no number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Mobile data**  
  The kind of service.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **31** (unitCode `E34`)  
  Gigabytes used on the island.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **13.144** (currencyID `XLC`)  
  At the data tariff.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/PriceAmount` = **0.424** (currencyID `XLC`)  
  The data tariff per GB.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/BaseQuantity` = **1** (unitCode `E34`)  
  Per gigabyte.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ID` = **D-0316-01**  
  Mobile data abroad.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallDate` = **2026-03-16**  
  The first day of the trip.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallTime` = **08:00:00+00:00**  
  From the morning; in the issuer's local time, with its offset from UTC.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/ServiceNumberCalled` = **data**  
  Mobile data, no number called.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategory` = **Roaming: mobile data in Bayvarra**  
  The name of code ROAM in the Trade Accord's telecommunications service category list, followed by the detail of this case: the phones used mobile data on a network in Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/TelecommunicationsServiceCategoryCode` = **ROAM** (listID `urn:ubl-examples:world:codelist:TelecomServiceCategoryCode`)  
  As a code. The code is from the Trade Accord's telecommunications service category list: ROAM = Roaming.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/RoamingPartnerName` = **Lumeport mobile network**  
  The network used in Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Quantity` = **4** (unitCode `E34`)  
  Gigabytes used on a business trip to Lumeport, 16 to 18 March, part of the pool's 35 GB.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/CallExtensionAmount` = **6.000** (currencyID `XLC`)  
  At the roaming tariff: the Trade Accord has no roaming rule, so roaming is charged.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/PriceAmount` = **1.5** (currencyID `XLC`)  
  The roaming tariff per GB in Bayvarra.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Price/BaseQuantity` = **1** (unitCode `E34`)  
  Per gigabyte.
- `Consumption/TelecommunicationsSupply/TelecommunicationsSupplyLine/TelecommunicationsService/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the data was used. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consumption/LegalMonetaryTotal/LineExtensionAmount` = **146.224** (currencyID `XLC`)  
  The supply.
- `Consumption/LegalMonetaryTotal/AllowanceTotalAmount` = **6.354** (currencyID `XLC`)  
  The bundle discount.
- `Consumption/LegalMonetaryTotal/PayableAmount` = **139.870** (currencyID `XLC`)  
  The supply less the discount; no tax.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:utility-statement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>STL-TX-26-75183</cbc:ProfileExecutionID>
  <cbc:ID>STL-UST-26-75398</cbc:ID>
  <cbc:UUID>7b60d4fc-8fd7-5124-9e01-cfc520caed86</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>17:37:00+00:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">TEL</cbc:UtilityStatementTypeCode>
  <cbc:Note languageID="qal">Mikake votetaka hanano mofilufo kisala vepili vafosu.</cbc:Note>
  <cbc:Note languageID="en-XL">This statement explains the consumption behind your bill.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>700</cbc:AccountingCostCode>
  <cbc:AccountingCost>Telephone and data</cbc:AccountingCost>
  <cac:ParentDocumentReference>
    <cbc:ID>STL-C-1077-2603</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>STL-TARIFF-2026</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentTypeCode">TARIFF</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Prices per unit and the terms of supply.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Telecom</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
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
      <cbc:Name>Billing</cbc:Name>
      <cbc:JobTitle>Billing officer</cbc:JobTitle>
      <cbc:Department>Business sales</cbc:Department>
      <cbc:Telephone>+999 3 727 3193</cbc:Telephone>
      <cbc:ElectronicMail>billing@selanutelecom.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>16</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Accounts payable</cbc:Name>
      <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
      <cbc:ElectronicMail>payables@velumi.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>STL-1077-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode listID="urn:ubl-examples:world:codelist:SpecificationTypeCode">DETAILED</cbc:SpecificationTypeCode>
    <cbc:TotalMeteredQuantity unitCode="E34">35</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>STL-CP-1077</cbc:ID>
      <cbc:Description>Office of Velumi Trading, Selanu</cbc:Description>
      <cbc:SubscriberID>STL-CU-20418</cbc:SubscriberID>
      <cbc:SubscriberType>Business</cbc:SubscriberType>
      <cbc:SubscriberTypeCode listID="urn:ubl-examples:world:codelist:SubscriberTypeCode">BUS</cbc:SubscriberTypeCode>
      <cac:Address>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:Address>
    </cac:UtilityConsumptionPoint>
    <cac:Consumption>
      <cbc:UtilityStatementTypeCode listID="urn:ubl-examples:world:codelist:UtilityTypeCode">TEL</cbc:UtilityStatementTypeCode>
      <cac:MainPeriod>
        <cbc:StartDate>2026-03-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:MainPeriod>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">95</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Business bundle discount</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.05</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="XLC">6.354</cbc:Amount>
      </cac:AllowanceCharge>
      <cac:TelecommunicationsSupply>
        <cbc:TelecommunicationsSupplyType>Business lines and data</cbc:TelecommunicationsSupplyType>
        <cbc:TelecommunicationsSupplyTypeCode listID="urn:ubl-examples:world:codelist:TelecomSupplyTypeCode">BUS</cbc:TelecommunicationsSupplyTypeCode>
        <cbc:PrivacyCode listID="urn:ubl-examples:world:codelist:PrivacyCode">MASKED</cbc:PrivacyCode>
        <cbc:Description>Six business lines and a mobile data pool.</cbc:Description>
        <cbc:TotalAmount currencyID="XLC">146.224</cbc:TotalAmount>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>1</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1850</cbc:PhoneNumber>
          <cbc:Description>Business line 1 of the six of subscription STL-L-BUS6, with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-1</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">140</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
          <cac:TelecommunicationsService>
            <cbc:ID>C-0311-01</cbc:ID>
            <cbc:CallDate>2026-03-11</cbc:CallDate>
            <cbc:CallTime>10:14:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>+999 2 5121 955 ***</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>International: a call to Bayvarra</cbc:TelecommunicationsServiceCategory>
            <cbc:TelecommunicationsServiceCategoryCode listID="urn:ubl-examples:world:codelist:TelecomServiceCategoryCode">INT</cbc:TelecommunicationsServiceCategoryCode>
            <cbc:Quantity unitCode="MIN">12</cbc:Quantity>
            <cbc:TelecommunicationsServiceCall>Outgoing</cbc:TelecommunicationsServiceCall>
            <cbc:TelecommunicationsServiceCallCode listID="urn:ubl-examples:world:codelist:TelecomCallTypeCode">OUT</cbc:TelecommunicationsServiceCallCode>
            <cbc:CallBaseAmount currencyID="XLC">0.050</cbc:CallBaseAmount>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
            <cac:Price>
              <cbc:PriceAmount currencyID="XLC">0.2</cbc:PriceAmount>
              <cbc:BaseQuantity unitCode="MIN">1</cbc:BaseQuantity>
            </cac:Price>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
            <cac:AllowanceCharge>
              <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
              <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">64</cbc:AllowanceChargeReasonCode>
              <cbc:AllowanceChargeReason>Calls to the Trade Accord countries are included in the subscription</cbc:AllowanceChargeReason>
              <cbc:Amount currencyID="XLC">2.450</cbc:Amount>
            </cac:AllowanceCharge>
            <cac:CallDuty>
              <cbc:Amount currencyID="XLC">0.050</cbc:Amount>
              <cbc:Duty>Set-up</cbc:Duty>
              <cbc:DutyCode listID="urn:ubl-examples:world:codelist:TelecomDutyCode">SETUP</cbc:DutyCode>
            </cac:CallDuty>
            <cac:TimeDuty>
              <cbc:Amount currencyID="XLC">2.400</cbc:Amount>
              <cbc:Duty>Per minute</cbc:Duty>
              <cbc:DutyCode listID="urn:ubl-examples:world:codelist:TelecomDutyCode">MIN</cbc:DutyCode>
            </cac:TimeDuty>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>2</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1851</cbc:PhoneNumber>
          <cbc:Description>Business line 2 of the six of subscription STL-L-BUS6, with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-2</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">165</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
          <cac:TelecommunicationsService>
            <cbc:ID>V-0320-02</cbc:ID>
            <cbc:CallDate>2026-03-20</cbc:CallDate>
            <cbc:CallTime>12:30:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>video</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Video on demand</cbc:TelecommunicationsServiceCategory>
            <cbc:MovieTitle>Safe Lifting in the Warehouse</cbc:MovieTitle>
            <cbc:PayPerView>true</cbc:PayPerView>
            <cbc:Quantity unitCode="EA">1</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
            <cac:Price>
              <cbc:PriceAmount currencyID="XLC">2</cbc:PriceAmount>
              <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
            </cac:Price>
            <cac:AllowanceCharge>
              <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
              <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">64</cbc:AllowanceChargeReasonCode>
              <cbc:AllowanceChargeReason>Training films are included in the business bundle</cbc:AllowanceChargeReason>
              <cbc:Amount currencyID="XLC">2.000</cbc:Amount>
            </cac:AllowanceCharge>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>3</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1852</cbc:PhoneNumber>
          <cbc:Description>Business line 3 of the six of subscription STL-L-BUS6, with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-3</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">190</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>4</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1853</cbc:PhoneNumber>
          <cbc:Description>Business line 4 of the six of subscription STL-L-BUS6, with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-4</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">215</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>5</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1854</cbc:PhoneNumber>
          <cbc:Description>Business line 5 of the six of subscription STL-L-BUS6, with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-5</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">240</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>6</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1855</cbc:PhoneNumber>
          <cbc:Description>Business line 6 of the six of subscription STL-L-BUS6, with calls on the island included.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">21.180</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">21.180</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>S-03-6</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>island</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Island calls</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="MIN">265</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">0.000</cbc:CallExtensionAmount>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
        <cac:TelecommunicationsSupplyLine>
          <cbc:ID>7</cbc:ID>
          <cbc:PhoneNumber>+999 3 721 1856</cbc:PhoneNumber>
          <cbc:Description>Mobile data pool STL-D-0042, shared by the six lines: 35 GB beyond the subscriptions in March, 4 GB of them roaming in Bayvarra.</cbc:Description>
          <cbc:LineExtensionAmount currencyID="XLC">19.144</cbc:LineExtensionAmount>
          <cbc:TaxInclusiveLineExtensionAmount currencyID="XLC">19.144</cbc:TaxInclusiveLineExtensionAmount>
          <cac:TelecommunicationsService>
            <cbc:ID>D-03</cbc:ID>
            <cbc:CallDate>2026-03-01</cbc:CallDate>
            <cbc:CallTime>00:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>data</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Mobile data</cbc:TelecommunicationsServiceCategory>
            <cbc:Quantity unitCode="E34">31</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">13.144</cbc:CallExtensionAmount>
            <cac:Price>
              <cbc:PriceAmount currencyID="XLC">0.424</cbc:PriceAmount>
              <cbc:BaseQuantity unitCode="E34">1</cbc:BaseQuantity>
            </cac:Price>
          </cac:TelecommunicationsService>
          <cac:TelecommunicationsService>
            <cbc:ID>D-0316-01</cbc:ID>
            <cbc:CallDate>2026-03-16</cbc:CallDate>
            <cbc:CallTime>08:00:00+00:00</cbc:CallTime>
            <cbc:ServiceNumberCalled>data</cbc:ServiceNumberCalled>
            <cbc:TelecommunicationsServiceCategory>Roaming: mobile data in Bayvarra</cbc:TelecommunicationsServiceCategory>
            <cbc:TelecommunicationsServiceCategoryCode listID="urn:ubl-examples:world:codelist:TelecomServiceCategoryCode">ROAM</cbc:TelecommunicationsServiceCategoryCode>
            <cbc:RoamingPartnerName>Lumeport mobile network</cbc:RoamingPartnerName>
            <cbc:Quantity unitCode="E34">4</cbc:Quantity>
            <cbc:CallExtensionAmount currencyID="XLC">6.000</cbc:CallExtensionAmount>
            <cac:Price>
              <cbc:PriceAmount currencyID="XLC">1.5</cbc:PriceAmount>
              <cbc:BaseQuantity unitCode="E34">1</cbc:BaseQuantity>
            </cac:Price>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:TelecommunicationsService>
        </cac:TelecommunicationsSupplyLine>
      </cac:TelecommunicationsSupply>
      <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="XLC">146.224</cbc:LineExtensionAmount>
        <cbc:AllowanceTotalAmount currencyID="XLC">6.354</cbc:AllowanceTotalAmount>
        <cbc:PayableAmount currencyID="XLC">139.870</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:Consumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
