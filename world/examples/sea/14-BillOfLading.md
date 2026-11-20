# Bill of Lading: Tidewell Ocean Lines to Bayforth Forwarding

*Example 14 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Bill of Lading in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-BILL-OF-LADING-SCHEMA)*

The negotiable bill of lading, issued to the forwarder that gave the instructions; it names the insurer of the cargo and the buyer's 3PL as party to notify on arrival.

[The XML file](14-BillOfLading.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:bill-of-lading:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Bill of lading"; the community specification "Lumeport port community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **BYF-TX-26-2501**  
  The collaboration this document belongs to: the sea carriage Bayforth books with Tidewell Ocean Lines. Bayforth Forwarding started it and gave it this identifier, which every document of it repeats.
- `ID` = **TWLU000033415**  
  The bill of lading number.
- `CarrierAssignedID` = **1200033394**  
  The booking the bill of lading is issued under.
- `UUID` = **aa5970ad-efd9-5660-a1d7-8a2f0bf2de7b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-14**  
  Issued when the goods are shipped on board.
- `IssueTime` = **10:54:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Name` = **Bill of lading**  
  What it is.
- `Description` = **Shipped on board.**  
  The kind of bill.
- `Note` = **Freight prepaid.**  
  Who has paid the freight.
- `DocumentStatusCode` = **Confirmed** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  Issued. The code is from the world's copy of UBL's Document status list, with a listID: Confirmed = Document has been confirmed.
- `ShippingOrderID` = **BYF-FI-26-1501**  
  The forwarder's booking with the carrier.
- `ToOrderIndicator` = **true**  
  Made out to order: the buyer can transfer it by endorsement.
- `OtherInstruction` = **Three originals issued.**  
  How many originals there are.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **dispatch@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; as Tidewell Ocean Lines gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Tidewell Ocean Lines gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. As Tidewell Ocean Lines gives it.
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. As Tidewell Ocean Lines gives it.
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Tidewell Ocean Lines gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Tidewell Ocean Lines gives it.
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). As Tidewell Ocean Lines gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Tidewell Ocean Lines gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; as Tidewell Ocean Lines gives it.
- `Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; as Tidewell Ocean Lines gives it.
- `Contact/Department` = **Bookings**  
  The department the desk belongs to; as Tidewell Ocean Lines gives it.
- `Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Tidewell Ocean Lines gives it.
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Tidewell Ocean Lines gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Tidewell Ocean Lines gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; as Bayforth Forwarding gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Bayforth Forwarding gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. As Bayforth Forwarding gives it.
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. As Bayforth Forwarding gives it.
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Bayforth Forwarding gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bayforth Forwarding gives it.
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). As Bayforth Forwarding gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bayforth Forwarding gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Export desk**  
  The party's export desk: the desk for its role in this document (it handles the transport of goods between the countries); as Bayforth Forwarding gives it.
- `Contact/JobTitle` = **Export coordinator**  
  The job of the person who answers at the desk; as Bayforth Forwarding gives it.
- `Contact/Department` = **Export**  
  The department the desk belongs to; as Bayforth Forwarding gives it.
- `Contact/Telephone` = **+999 2 38 5155 2404**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bayforth Forwarding gives it.
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Bayforth Forwarding gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayforth Forwarding gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **LMW-SH-26-1001**  
  The shipment carried.
- `GrossWeightMeasure` = **9545.8** (unitCode `KGM`)  
  The goods (5795.8 kg) and the tare of the transport equipment (3750 kg): a shipment's gross weight includes the equipment.
- `TotalGoodsItemQuantity` = **2** (unitCode `EA`)  
  Benches and side frames.
- `ConsignmentQuantity` = **1** (unitCode `EA`)  
  One consignment.
- `Consignment/ID` = **LMW-CS-26-1001**  
  The distributor's consignment number.
- `Consignment/CarrierAssignedID` = **1200033394**  
  The carrier's booking number.
- `Consignment/FreightForwarderAssignedID` = **BYF-SH-26-0418**  
  The forwarder's own file number for the consignment, not the distributor's instructions.
- `Consignment/BrokerAssignedID` = **TCB-26-0331**  
  The customs broker's file in Selanu.
- `Consignment/TotalInvoiceAmount` = **54896.00** (currencyID `XBL`)  
  The sales invoice: the goods at their CIF prices.
- `Consignment/DeclaredCustomsValueAmount` = **54896.00** (currencyID `XBL`)  
  The CIF value, the price of the goods, which holds the freight and the insurance.
- `Consignment/TariffDescription` = **Furniture, packed, not hazardous**  
  The carrier's commodity tariff, in words.
- `Consignment/TariffCode` = **TWL-T-0940**  
  The item of the carrier's own freight tariff for this cargo: furniture. A code the carrier defines, so it has no code list.
- `Consignment/InsurancePremiumAmount` = **132.85** (currencyID `XBL`)  
  The premium the seller paid under CIF.
- `Consignment/GrossWeightMeasure` = **5795.8** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight of the cargo.
- `Consignment/ShippingPriorityLevelCode` = **STANDARD** (listID `urn:ubl-examples:world:codelist:ShippingPriorityCode`)  
  The normal sailing, no priority loading. The code is from the Trade Accord's shipping priority list: STANDARD = Standard.
- `Consignment/HandlingCode` = **DECK** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier may stow the container on deck. The code is from the Trade Accord's handling instruction list: DECK = On-deck stowage allowed.
- `Consignment/HandlingInstructions` = **Keep dry.**  
  The handling, in words.
- `Consignment/Information` = **Shipped on board in apparent good order and condition.**  
  The carrier's clause.
- `Consignment/InsuranceValueAmount` = **60385.60** (currencyID `XBL`)  
  110 % of the CIF value.
- `Consignment/FreeOnBoardValueAmount` = **51813.15** (currencyID `XBL`)  
  The value on board in Lumeport: the CIF price less the sea freight and the insurance.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 729 5794**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `Consignment/NotifyParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Nalevi Warehousing gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/NotifyParty/PartyName/Name` = **Nalevi Warehousing**  
  The trading name; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/ID` = **95940358** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/NotifyParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Vilafa Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Lagoon Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/NotifyParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/NotifyParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/NotifyParty/Contact/Name` = **Goods inwards**  
  The party's main desk, which handles this document; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/JobTitle` = **Warehouse supervisor**  
  The job of the person who answers at the desk; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/Telephone` = **+999 3 722 1882**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/ElectronicMail` = **goods@nalevi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/Note` = **Monday to Saturday 07:00–18:00**  
  When the desk can be reached; as Nalevi Warehousing gives it.
- `Consignment/OriginalDespatchParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDespatchParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FinalDeliveryParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FinalDeliveryParty/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/LogisticsOperatorParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/LogisticsOperatorParty/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/BillOfLadingHolderParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/BillOfLadingHolderParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDepartureCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  From Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/FinalDestinationCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  To the island. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/DeliveryTerms/ID` = **CIF** (schemeID `INCOTERMS`)  
  Incoterms 2020: cost, insurance and freight to the port of Selanu. The code is from the world's copy of Incoterms 2020: CIF = Cost, Insurance and Freight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/DeliveryTerms/LossRiskResponsibilityCode` = **BUYER** (listID `urn:ubl-examples:world:codelist:RiskResponsiblePartyCode`)  
  The risk is the buyer's from on board in Lumeport. The code is from the Trade Accord's party bearing the risk list: BUYER = Buyer.
- `Consignment/DeliveryTerms/LossRisk` = **Risk passes when the goods are on board the vessel in Lumeport.**  
  In words.
- `Consignment/DeliveryTerms/Amount` = **54896.00** (currencyID `XBL`)  
  The CIF value the terms are based on.
- `Consignment/DeliveryTerms/DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/DeliveryTerms/DeliveryLocation/Name` = **Port of Selanu**  
  The named port of destination.
- `Consignment/DeliveryTerms/DeliveryLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/DeliveryTerms/AllowanceCharge/ChargeIndicator` = **true**  
  A cost under the terms.
- `Consignment/DeliveryTerms/AllowanceCharge/AllowanceChargeReasonCode` = **HD** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: HD = Handling.
- `Consignment/DeliveryTerms/AllowanceCharge/AllowanceChargeReason` = **Terminal handling at Selanu, for the buyer**  
  Under CIF the buyer pays the unloading.
- `Consignment/DeliveryTerms/AllowanceCharge/Amount` = **185.00** (currencyID `XBL`)  
  The carrier's tariff.
- `Consignment/PaymentTerms/Note` = **Ocean freight payable before release of the bill of lading.**  
  The carrier's terms.
- `Consignment/CollectPaymentTerms/Note` = **Terminal handling at Selanu collect from the consignee.**  
  The buyer pays it there.
- `Consignment/DisbursementPaymentTerms/Note` = **Island customs fees advanced by the broker and recharged to the consignee.**  
  Paid out for someone else.
- `Consignment/PrepaidPaymentTerms/Note` = **Ocean freight and bunker surcharge prepaid by the shipper.**  
  CIF: the seller pays.
- `Consignment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The basic ocean freight.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **Ocean freight, 40-foot container**  
  In words.
- `Consignment/FreightAllowanceCharge/Amount` = **2700.00** (currencyID `XBL`)  
  The carrier's rate.
- `Consignment/ExtraAllowanceCharge/ChargeIndicator` = **true**  
  A surcharge.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The bunker surcharge is part of the freight: UN/EDIFACT 7161 has no code of its own for it, so it carries the freight code. The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReason` = **Bunker surcharge**  
  For the fuel price.
- `Consignment/ExtraAllowanceCharge/Amount` = **250.00** (currencyID `XBL`)  
  Together with the freight: the 2,950 lume the forwarder invoices.
- `Consignment/MainCarriageShipmentStage/ID` = **2**  
  By sea from Lumeport to Selanu.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **TH-26-19E**  
  The voyage number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **EB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: EB = Eastbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Harbour; the fleet of Tidewell Ocean Lines. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TradeServiceCode` = **TWL-ISL**  
  The carrier's code for its island service.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/LocationID` = **140282**  
  Bay 14, row 02, tier 82.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/Location` = **On deck, aft of the bridge**  
  In words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/MeasurementDimension/AttributeID` = **SLOTLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The slot length. The code is from the Trade Accord's dimension attribute list: SLOTLENGTH = Slot length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/MeasurementDimension/Measure` = **12.2** (unitCode `MTR`)  
  A 40-foot slot.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QBTH7**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **298702117**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 1,000 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Port of Lumeport**  
  The port of loading.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Port of Selanu**  
  The port of discharge.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/OccurrenceDate` = **2026-05-17**  
  The container is available at Selanu.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/OccurrenceTime` = **14:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/OccurrenceDate` = **2026-05-13**  
  Stacked at the quay until loading.
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/OccurrenceTime` = **10:30:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/Location/Name` = **Port of Lumeport**  
  At the container quay of the Port of Lumeport.
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/OccurrenceDate` = **2026-05-13**  
  The terminal accepted the container.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/OccurrenceTime` = **10:15:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/Location/Name` = **Port of Lumeport**  
  At the container quay of the Port of Lumeport.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/Name` = **Port of Lumeport**  
  The freight is payable in Lumeport.
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/PreCarriageShipmentStage/ID` = **1**  
  By truck from Marrowdale to the port.
- `Consignment/PreCarriageShipmentStage/ShipmentStageTypeCode` = **10** (listID `UN/EDIFACT EDED 8051`)  
  The kind of stage. The code is from the world's copy of UN/EDIFACT 8051 Transport stage code qualifier: 10 = Pre-carriage transport.
- `Consignment/PreCarriageShipmentStage/ShipmentStageType` = **Pre-carriage transport**  
  The name of code 10 in the world's copy of UN/EDIFACT 8051 Transport stage code qualifier.
- `Consignment/PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/PreCarriageShipmentStage/PreCarriageIndicator` = **true**  
  Before the main carriage.
- `Consignment/PreCarriageShipmentStage/CabotageIndicator` = **false**  
  A Bayvarran truck within Bayvarra: no cabotage.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **37** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container chassis truck; the fleet of Bayforth Forwarding. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 37 = Truck, container.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **BV LP 2205** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The registration plate of the truck; the fleet of Bayforth Forwarding. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **BV CH 0412** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceDate` = **2026-05-13**  
  The container was dropped at the container quay.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceTime` = **10:15:00**  
  The local time.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/Location/Name` = **Port of Lumeport**  
  At the container quay of the Port of Lumeport.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/OnCarriageShipmentStage/ID` = **3**  
  By truck from the port of Selanu to the 3PL.
- `Consignment/OnCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/OnCarriageShipmentStage/OnCarriageIndicator` = **true**  
  After the main carriage.
- `Consignment/OnCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OnCarriageShipmentStage/CarrierParty/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OnCarriageShipmentStage/WarehousingTransportEvent/OccurrenceDate` = **2026-05-18**  
  Stored at the 3PL until called off.
- `Consignment/OnCarriageShipmentStage/WarehousingTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/OnCarriageShipmentStage/WarehousingTransportEvent/Location/Name` = **Nalevi Warehousing, Selanu**  
  The 3PL's warehouse on the island, where the goods are received and stored.
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/OccurrenceDate` = **2026-05-18**  
  Planned receipt at the 3PL, the day after discharge, as planned when the bill was issued.
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/Location/Name` = **Nalevi Warehousing, Selanu**  
  The 3PL's warehouse on the island, where the goods are received and stored.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container's number: the owner code of the ocean carrier, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **42G1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet, 8 ft 6 in high, general purpose. The code is from the world's copy of ISO 6346 container size and type code: 42G1 = 40 ft, 8 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL** (listID `urn:ubl-examples:world:codelist:LoadTypeCode`)  
  A full container load. The code is from the Trade Accord's load type list: FCL = Full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **false**  
  A dry container.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **9545.8** (unitCode `KGM`)  
  The verified gross mass: cargo and the container's own weight of 3,750 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **3750** (unitCode `KGM`)  
  The empty container's own weight, as marked on its door.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **140282**  
  Bay 14, row 02, tier 82: on deck, as planned by the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **TWL-S-0884213**  
  The carrier's seal, put on when the container was packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:SealIssuerTypeCode`)  
  Issued by the ocean carrier. The code is from the Trade Accord's seal issuer type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  Put on by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/SupplierParty/Party/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/SupplierParty/Party/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729071** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 001 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729071**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729088** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 002 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729088**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729095** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 003 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729095**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729101** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 004 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729101**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729118** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 005 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729118**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729125** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 006 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729125**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729132** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 007 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729132**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729149** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 008 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729149**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729156** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 009 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729156**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729163** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 010 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729163**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729170** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 011 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729170**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729187** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 012 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729187**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729194** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 013 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729194**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729200** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 014 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729200**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729217** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 015 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729217**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729224** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 016 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729224**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729231** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 017 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729231**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729248** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 018 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729248**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729255** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 019 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729255**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729262** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 020 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729262**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729279** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 021 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729279**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729286** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 022 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729286**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729293** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 023 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729293**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729309** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 024 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729309**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729316** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 025 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729316**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729323** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 026 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729323**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206100003729330** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 12 spare side frames, one to a frame carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 027 of 027**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206100003729330**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ID` = **1**  
  The goods in the container, as one item for the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/Description` = **Park benches and spare side frames**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/ID` = **1.1**  
  The benches.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/Description` = **Park benches**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/ID` = **1.2**  
  The side frames.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/Description` = **Spare side frames**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ID` = **VGM-26-0510**  
  The shipper's weight declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDate` = **2026-05-12**  
  Weighed when packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingTime` = **15:30:00**  
  After closing the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingMethodCode` = **SM2** (listID `IMO SOLAS`)  
  SOLAS method 2: the cargo and packing weighed and added to the tare. The code is from UBL's default Weighing method (IMO SOLAS) list: SM2 = SOLAS verification method 2.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceID` = **LMW-SCALE-03**  
  The scale of the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceType` = **Platform scale**  
  Its kind.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/GrossMassMeasure` = **9545.8** (unitCode `KGM`)  
  The verified gross mass.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ShipperParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ShipperParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ResponsibleParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ResponsibleParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/ID` = **VGM-26-0510**  
  The signed weight declaration sent to the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/DocumentTypeCode` = **749** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, the shipper's verified gross mass of the container, a document outside the examples (cited). The code is from the world's copy of UN/EDIFACT 1001 Document name: 749 = Transport equipment gross mass verification message.
- `Consignment/FirstArrivalPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/FirstArrivalPortLocation/Name` = **Port of Selanu**  
  The first port of call after Lumeport.
- `Consignment/FirstArrivalPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/LastExitPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/LastExitPortLocation/Name` = **Port of Lumeport**  
  The last port in Bayvarra.
- `Consignment/LastExitPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/DocumentReference/ID` = **LMW-PKL-26-0051**  
  The packing list of the container.
- `Consignment/DocumentReference/DocumentTypeCode` = **PackingList** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LMW-PKL-26-0051 is the example sea/10, a PackingList; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: PackingList = Packing List.
- `Consignment/InsurancePolicy/ID` = **WVS-CP-26-4471**  
  The cargo policy of the insurer.
- `Consignment/InsurancePolicy/InsuranceTypeCode` = **ALLRISKS** (listID `urn:ubl-examples:world:codelist:InsuranceCoverCode`)  
  Cover against all risks. The code is from the Trade Accord's insurance cover list: ALLRISKS = All risks.
- `Consignment/InsurancePolicy/InsuredValueAmount` = **60385.60** (currencyID `XBL`)  
  110 % of the CIF value.
- `Consignment/InsurancePolicy/DeductibleAmount` = **250.00** (currencyID `XBL`)  
  The part of a claim the insured bears.
- `Consignment/InsurancePolicy/InsurancePremiumAmount` = **132.85** (currencyID `XBL`)  
  The premium.
- `Consignment/InsurancePolicy/InsurerParty/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Wavesure Cargo Insurance gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/InsurancePolicy/InsurerParty/PartyName/Name` = **Wavesure Cargo Insurance**  
  The trading name; as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/ID` = **LUM-ADR-308716** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/StreetName` = **Beacon Avenue**  
  Street of the postal address. As Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/BuildingNumber` = **55**  
  Building number of the postal address. As Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/PostalZone` = **38524**  
  Postal code in Bayvarra's format (5 digits). As Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Wavesure Cargo Insurance gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/InsurancePolicy/InsurerParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/InsurancePolicy/InsurerParty/Contact/Name` = **Cargo claims**  
  The party's main desk, which handles this document; as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/Contact/JobTitle` = **Claims handler**  
  The job of the person who answers at the desk; as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/Contact/Department` = **Claims**  
  The department the desk belongs to; as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/Contact/Telephone` = **+999 2 38 2115 9838**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/Contact/ElectronicMail` = **cargo@wavesure.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/InsurerParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Wavesure Cargo Insurance gives it.
- `Consignment/InsurancePolicy/BrokerParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/BrokerParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/PolicyHolderParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/PolicyHolderParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/BeneficiaryParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/BeneficiaryParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/PolicyDocumentReference/ID` = **WVS-CERT-26-0884**  
  The insurance certificate that goes with the documents.
- `Consignment/InsurancePolicy/PolicyDocumentReference/DocumentType` = **Insurance certificate**  
  What the document is: the certificate of the shipment under the policy, not the policy itself.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **5621.2** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **104** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Park bench Serra 180**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Bench side frame casting**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **174.6** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **12** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Bench side frame casting**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940199** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940199 = Parts of seats, other.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BYF-FI-26-1501**  
  The forwarding instructions it was issued on.
- `DocumentTypeCode` = **ForwardingInstructions** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: BYF-FI-26-1501 is the example sea/12, a ForwardingInstructions; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ForwardingInstructions = Forwarding Instructions.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The full set of three originals.
- `DocumentTypeCode` = **BillOfLading** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this bill of lading. The code is from the Trade Accord's UBL document type list: BillOfLading = Bill Of Lading.
- `DistributionTypeCode` = **ORIGINALCOURIER** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The originals go by courier to the forwarder, the shipper's agent; the buyer gets them, endorsed, against payment. The code is from the Trade Accord's distribution type list: ORIGINALCOURIER = Original, sent by courier.
- `Party/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The notify party's copy.
- `DocumentTypeCode` = **BillOfLading** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this bill of lading. The code is from the Trade Accord's UBL document type list: BillOfLading = Bill Of Lading.
- `DistributionTypeCode` = **SCANNEDCOPY** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  A scanned copy for the notify party, which arranges the on-carriage at Selanu; a copy gives no title to the goods. The code is from the Trade Accord's distribution type list: SCANNEDCOPY = Scanned copy.
- `Party/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **TWL-SIG-BL-sea**  
  The master's signature, by the carrier's agent.
- `SignatoryParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<BillOfLading xmlns="urn:oasis:names:specification:ubl:schema:xsd:BillOfLading-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:bill-of-lading:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>BYF-TX-26-2501</cbc:ProfileExecutionID>
  <cbc:ID>TWLU000033415</cbc:ID>
  <cbc:CarrierAssignedID>1200033394</cbc:CarrierAssignedID>
  <cbc:UUID>aa5970ad-efd9-5660-a1d7-8a2f0bf2de7b</cbc:UUID>
  <cbc:IssueDate>2026-05-14</cbc:IssueDate>
  <cbc:IssueTime>10:54:00-01:00</cbc:IssueTime>
  <cbc:Name>Bill of lading</cbc:Name>
  <cbc:Description>Shipped on board.</cbc:Description>
  <cbc:Note>Freight prepaid.</cbc:Note>
  <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">Confirmed</cbc:DocumentStatusCode>
  <cbc:ShippingOrderID>BYF-FI-26-1501</cbc:ShippingOrderID>
  <cbc:ToOrderIndicator>true</cbc:ToOrderIndicator>
  <cbc:OtherInstruction>Three originals issued.</cbc:OtherInstruction>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
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
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
  </cac:ConsignorParty>
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
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Export coordinator</cbc:JobTitle>
      <cbc:Department>Export</cbc:Department>
      <cbc:Telephone>+999 2 38 5155 2404</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>LMW-SH-26-1001</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">9545.8</cbc:GrossWeightMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="EA">2</cbc:TotalGoodsItemQuantity>
    <cbc:ConsignmentQuantity unitCode="EA">1</cbc:ConsignmentQuantity>
    <cac:Consignment>
      <cbc:ID>LMW-CS-26-1001</cbc:ID>
      <cbc:CarrierAssignedID>1200033394</cbc:CarrierAssignedID>
      <cbc:FreightForwarderAssignedID>BYF-SH-26-0418</cbc:FreightForwarderAssignedID>
      <cbc:BrokerAssignedID>TCB-26-0331</cbc:BrokerAssignedID>
      <cbc:TotalInvoiceAmount currencyID="XBL">54896.00</cbc:TotalInvoiceAmount>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">54896.00</cbc:DeclaredCustomsValueAmount>
      <cbc:TariffDescription>Furniture, packed, not hazardous</cbc:TariffDescription>
      <cbc:TariffCode>TWL-T-0940</cbc:TariffCode>
      <cbc:InsurancePremiumAmount currencyID="XBL">132.85</cbc:InsurancePremiumAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">5795.8</cbc:GrossWeightMeasure>
      <cbc:ShippingPriorityLevelCode listID="urn:ubl-examples:world:codelist:ShippingPriorityCode">STANDARD</cbc:ShippingPriorityLevelCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">DECK</cbc:HandlingCode>
      <cbc:HandlingInstructions>Keep dry.</cbc:HandlingInstructions>
      <cbc:Information>Shipped on board in apparent good order and condition.</cbc:Information>
      <cbc:InsuranceValueAmount currencyID="XBL">60385.60</cbc:InsuranceValueAmount>
      <cbc:FreeOnBoardValueAmount currencyID="XBL">51813.15</cbc:FreeOnBoardValueAmount>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
        </cac:AdditionalPartyIdentification>
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
          <cbc:Name>Goods-in</cbc:Name>
          <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
          <cbc:Department>Warehouse</cbc:Department>
          <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
          <cbc:ElectronicMail>goodsin@velumi.example</cbc:ElectronicMail>
          <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:NotifyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Nalevi Warehousing</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">95940358</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vilafa Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Lagoon Road</cbc:StreetName>
          <cbc:BuildingNumber>9</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Goods inwards</cbc:Name>
          <cbc:JobTitle>Warehouse supervisor</cbc:JobTitle>
          <cbc:Department>Warehouse</cbc:Department>
          <cbc:Telephone>+999 3 722 1882</cbc:Telephone>
          <cbc:ElectronicMail>goods@nalevi.example</cbc:ElectronicMail>
          <cbc:Note>Monday to Saturday 07:00–18:00</cbc:Note>
        </cac:Contact>
      </cac:NotifyParty>
      <cac:OriginalDespatchParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:OriginalDespatchParty>
      <cac:FinalDeliveryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Nalevi Warehousing</cbc:Name>
        </cac:PartyName>
      </cac:FinalDeliveryParty>
      <cac:LogisticsOperatorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Nalevi Warehousing</cbc:Name>
        </cac:PartyName>
      </cac:LogisticsOperatorParty>
      <cac:BillOfLadingHolderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Bayforth Forwarding</cbc:Name>
        </cac:PartyName>
      </cac:BillOfLadingHolderParty>
      <cac:OriginalDepartureCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:FinalDestinationCountry>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:FinalDestinationCountry>
      <cac:DeliveryTerms>
        <cbc:ID schemeID="INCOTERMS">CIF</cbc:ID>
        <cbc:LossRiskResponsibilityCode listID="urn:ubl-examples:world:codelist:RiskResponsiblePartyCode">BUYER</cbc:LossRiskResponsibilityCode>
        <cbc:LossRisk>Risk passes when the goods are on board the vessel in Lumeport.</cbc:LossRisk>
        <cbc:Amount currencyID="XBL">54896.00</cbc:Amount>
        <cac:DeliveryLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:DeliveryLocation>
        <cac:AllowanceCharge>
          <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
          <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">HD</cbc:AllowanceChargeReasonCode>
          <cbc:AllowanceChargeReason>Terminal handling at Selanu, for the buyer</cbc:AllowanceChargeReason>
          <cbc:Amount currencyID="XBL">185.00</cbc:Amount>
        </cac:AllowanceCharge>
      </cac:DeliveryTerms>
      <cac:PaymentTerms>
        <cbc:Note>Ocean freight payable before release of the bill of lading.</cbc:Note>
      </cac:PaymentTerms>
      <cac:CollectPaymentTerms>
        <cbc:Note>Terminal handling at Selanu collect from the consignee.</cbc:Note>
      </cac:CollectPaymentTerms>
      <cac:DisbursementPaymentTerms>
        <cbc:Note>Island customs fees advanced by the broker and recharged to the consignee.</cbc:Note>
      </cac:DisbursementPaymentTerms>
      <cac:PrepaidPaymentTerms>
        <cbc:Note>Ocean freight and bunker surcharge prepaid by the shipper.</cbc:Note>
      </cac:PrepaidPaymentTerms>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Ocean freight, 40-foot container</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">2700.00</cbc:Amount>
      </cac:FreightAllowanceCharge>
      <cac:ExtraAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Bunker surcharge</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">250.00</cbc:Amount>
      </cac:ExtraAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>2</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>TH-26-19E</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">EB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
          <cbc:TradeServiceCode>TWL-ISL</cbc:TradeServiceCode>
          <cac:Stowage>
            <cbc:LocationID>140282</cbc:LocationID>
            <cbc:Location>On deck, aft of the bridge</cbc:Location>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SLOTLENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MTR">12.2</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:Stowage>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
            <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
            <cbc:RadioCallSignID>QBTH7</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>298702117</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
            <cac:RegistryCertificateDocumentReference>
              <cbc:ID>REG-XB-S-20117</cbc:ID>
            </cac:RegistryCertificateDocumentReference>
            <cac:RegistryPortLocation>
              <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
              <cbc:Name>Lumeport</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:AvailabilityTransportEvent>
          <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>14:00:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
            <cbc:Name>Port of Selanu</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:AvailabilityTransportEvent>
        <cac:StorageTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:30:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:StorageTransportEvent>
        <cac:AcceptanceTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:15:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:AcceptanceTransportEvent>
        <cac:FreightChargeLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FreightChargeLocation>
      </cac:MainCarriageShipmentStage>
      <cac:PreCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:ShipmentStageTypeCode listID="UN/EDIFACT EDED 8051">10</cbc:ShipmentStageTypeCode>
        <cbc:ShipmentStageType>Pre-carriage transport</cbc:ShipmentStageType>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
        <cbc:CabotageIndicator>false</cbc:CabotageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Bayforth Forwarding</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">37</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV LP 2205</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV CH 0412</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
        </cac:TransportMeans>
        <cac:DropoffTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:15:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:DropoffTransportEvent>
      </cac:PreCarriageShipmentStage>
      <cac:OnCarriageShipmentStage>
        <cbc:ID>3</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:OnCarriageIndicator>true</cbc:OnCarriageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Nalevi Warehousing</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:WarehousingTransportEvent>
          <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:Name>Nalevi Warehousing, Selanu</cbc:Name>
          </cac:Location>
        </cac:WarehousingTransportEvent>
        <cac:ReceiptTransportEvent>
          <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:Name>Nalevi Warehousing, Selanu</cbc:Name>
          </cac:Location>
        </cac:ReceiptTransportEvent>
      </cac:OnCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode listID="ISO 6346">42G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
          <cbc:GrossWeightMeasure unitCode="KGM">9545.8</cbc:GrossWeightMeasure>
          <cbc:TareWeightMeasure unitCode="KGM">3750</cbc:TareWeightMeasure>
          <cbc:StowagePositionID>140282</cbc:StowagePositionID>
          <cac:TransportEquipmentSeal>
            <cbc:ID>TWL-S-0884213</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">CARRIER</cbc:SealIssuerTypeCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:SupplierParty>
            <cac:Party>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Tidewell Ocean Lines</cbc:Name>
              </cac:PartyName>
            </cac:Party>
          </cac:SupplierParty>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729071</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 001 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729071</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729088</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 002 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729088</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729095</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 003 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729095</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729101</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 004 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729101</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729118</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 005 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729118</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729125</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 006 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729125</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729132</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 007 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729132</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729149</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 008 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729149</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729156</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 009 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729156</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729163</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 010 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729163</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729170</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 011 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729170</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729187</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 012 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729187</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729194</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 013 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729194</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729200</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 014 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729200</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729217</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 015 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729217</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729224</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 016 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729224</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729231</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 017 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729231</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729248</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 018 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729248</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729255</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 019 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729255</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729262</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 020 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729262</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729279</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 021 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729279</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729286</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 022 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729286</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729293</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 023 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729293</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729309</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 024 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729309</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729316</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 025 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729316</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729323</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 026 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729323</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206100003729330</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 027 of 027</cbc:ShippingMarks>
            <cbc:TraceID>095206100003729330</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:GoodsItem>
            <cbc:ID>1</cbc:ID>
            <cbc:Description>Park benches and spare side frames</cbc:Description>
            <cac:ContainedGoodsItem>
              <cbc:ID>1.1</cbc:ID>
              <cbc:Description>Park benches</cbc:Description>
            </cac:ContainedGoodsItem>
            <cac:ContainedGoodsItem>
              <cbc:ID>1.2</cbc:ID>
              <cbc:Description>Spare side frames</cbc:Description>
            </cac:ContainedGoodsItem>
          </cac:GoodsItem>
          <cac:VerifiedGrossMass>
            <cbc:ID>VGM-26-0510</cbc:ID>
            <cbc:WeighingDate>2026-05-12</cbc:WeighingDate>
            <cbc:WeighingTime>15:30:00</cbc:WeighingTime>
            <cbc:WeighingMethodCode listID="IMO SOLAS">SM2</cbc:WeighingMethodCode>
            <cbc:WeighingDeviceID>LMW-SCALE-03</cbc:WeighingDeviceID>
            <cbc:WeighingDeviceType>Platform scale</cbc:WeighingDeviceType>
            <cbc:GrossMassMeasure unitCode="KGM">9545.8</cbc:GrossMassMeasure>
            <cac:WeighingParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeway Distribution</cbc:Name>
              </cac:PartyName>
            </cac:WeighingParty>
            <cac:ShipperParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeway Distribution</cbc:Name>
              </cac:PartyName>
            </cac:ShipperParty>
            <cac:ResponsibleParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeway Distribution</cbc:Name>
              </cac:PartyName>
            </cac:ResponsibleParty>
            <cac:DocumentReference>
              <cbc:ID>VGM-26-0510</cbc:ID>
              <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">749</cbc:DocumentTypeCode>
            </cac:DocumentReference>
          </cac:VerifiedGrossMass>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
      <cac:FirstArrivalPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
        <cbc:Name>Port of Selanu</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FirstArrivalPortLocation>
      <cac:LastExitPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Port of Lumeport</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:LastExitPortLocation>
      <cac:DocumentReference>
        <cbc:ID>LMW-PKL-26-0051</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">PackingList</cbc:DocumentTypeCode>
      </cac:DocumentReference>
      <cac:InsurancePolicy>
        <cbc:ID>WVS-CP-26-4471</cbc:ID>
        <cbc:InsuranceTypeCode listID="urn:ubl-examples:world:codelist:InsuranceCoverCode">ALLRISKS</cbc:InsuranceTypeCode>
        <cbc:InsuredValueAmount currencyID="XBL">60385.60</cbc:InsuredValueAmount>
        <cbc:DeductibleAmount currencyID="XBL">250.00</cbc:DeductibleAmount>
        <cbc:InsurancePremiumAmount currencyID="XBL">132.85</cbc:InsurancePremiumAmount>
        <cac:InsurerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Wavesure Cargo Insurance</cbc:Name>
          </cac:PartyName>
          <cac:PostalAddress>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-308716</cbc:ID>
            <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
            <cbc:StreetName>Beacon Avenue</cbc:StreetName>
            <cbc:BuildingNumber>55</cbc:BuildingNumber>
            <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
            <cbc:CityName>Lumeport</cbc:CityName>
            <cbc:PostalZone>38524</cbc:PostalZone>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
            <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              <cbc:Name>Bayvarra</cbc:Name>
            </cac:Country>
          </cac:PostalAddress>
          <cac:Contact>
            <cbc:Name>Cargo claims</cbc:Name>
            <cbc:JobTitle>Claims handler</cbc:JobTitle>
            <cbc:Department>Claims</cbc:Department>
            <cbc:Telephone>+999 2 38 2115 9838</cbc:Telephone>
            <cbc:ElectronicMail>cargo@wavesure.example</cbc:ElectronicMail>
            <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
          </cac:Contact>
        </cac:InsurerParty>
        <cac:BrokerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Bayforth Forwarding</cbc:Name>
          </cac:PartyName>
        </cac:BrokerParty>
        <cac:PolicyHolderParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Lumeway Distribution</cbc:Name>
          </cac:PartyName>
        </cac:PolicyHolderParty>
        <cac:BeneficiaryParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Velumi Trading</cbc:Name>
          </cac:PartyName>
        </cac:BeneficiaryParty>
        <cac:PolicyDocumentReference>
          <cbc:ID>WVS-CERT-26-0884</cbc:ID>
          <cbc:DocumentType>Insurance certificate</cbc:DocumentType>
        </cac:PolicyDocumentReference>
      </cac:InsurancePolicy>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">5621.2</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">104</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Bench side frame casting</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">174.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Bench side frame casting</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940199</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>BYF-FI-26-1501</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ForwardingInstructions</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">BillOfLading</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALCOURIER</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bayforth Forwarding</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">BillOfLading</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">SCANNEDCOPY</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Nalevi Warehousing</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>TWL-SIG-BL-sea</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</BillOfLading>
```
