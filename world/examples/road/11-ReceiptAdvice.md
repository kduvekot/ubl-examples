# Receipt Advice: Lumeway Distribution to Castrano Logistics

*Example 11 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Receipt Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-RECEIPT-ADVICE-SCHEMA)*

The distributor confirms what arrived to the party that despatched it, the 3PL, naming the manufacturer as seller.

[The XML file](11-ReceiptAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:receipt-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Receipt advice". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-RA-26-0162**  
  The receiving party's number.
- `UUID` = **496ff071-d380-5baa-87d1-43a590437ea5**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-25**  
  The day the truck was unloaded at the distribution centre.
- `IssueTime` = **15:40:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ReceiptAdviceTypeCode` = **Actual** (listID `urn:oasis:names:specification:ubl:codelist:gc:ReceiptAdviceTypeCode`)  
  UBL's receipt advice type code: the goods actually received. The code is from the world's copy of UBL's Receipt advice type list, with a listID: Actual = An arrival that has passed goods inspection and is accepted (or not)..
- `DeliveryAcceptanceCode` = **ACCEPTED** (listID `urn:ubl-examples:world:codelist:DeliveryAcceptanceCode`)  
  All goods accepted. The code is from the Trade Accord's delivery acceptance list: ACCEPTED = All accepted.
- `Note` = **Counted and checked at goods-in: one bench short, one box of side frames over.**  
  The result.
- `LineCountNumeric` = **2**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **LD-PO-26-0149**  
  The order the goods were delivered for.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **CL-DA-26-0153**  
  The despatch advice this receipt answers.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **TH-WB-26-0159**  
  The consignment note signed on delivery, the consignee's proof of receipt: a transport document, not a delivery note (road/11#F2).
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: TH-WB-26-0159 is the example road/08, a Waybill; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Waybill.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 474 274**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/ElectronicMail` = **goodsin@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Castrano Logistics (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10441** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Castrano Logistics (world/parties.json).
- `Party/PartyName/Name` = **Castrano Logistics**  
  The trading name; identity of Castrano Logistics (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `Party/PostalAddress/ID` = **4160203920705699** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **24**  
  Building number of the postal address. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Loading bays**  
  The party's loading bays desk: the desk for its role in this document (it sends the goods off); identity of Castrano Logistics (world/parties.json).
- `Party/Contact/JobTitle` = **Shift supervisor**  
  The job of the person who answers at the desk; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 677 4411**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Castrano Logistics (world/parties.json).
- `Party/Contact/ElectronicMail` = **loading@castrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Castrano Logistics (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Castrano Logistics (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Order desk**  
  The party's main desk, which handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Order administrator**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.

### Shipment

Inside `Shipment`:

- `ID` = **CL-SH-26-0154**  
  The shipment received.
- `Delivery/ActualDeliveryDate` = **2026-03-25**  
  Unloaded at dock 4.
- `Delivery/ActualDeliveryTime` = **09:40:00**  
  Within the slot.

### Receipt Line

Inside `ReceiptLine`:

- `ID` = **1**  
  The line number.
- `UUID` = **01193af5-785e-5e35-84c8-25a8b365acea**  
  A universally unique identifier of the line, derived from the document and the line number.
- `Note` = **One pallet held three benches and a box of side frames: mis-picked at the 3PL.**  
  What was found.
- `ReceivedQuantity` = **95** (unitCode `EA`)  
  One bench fewer than despatched.
- `ShortQuantity` = **1** (unitCode `EA`)  
  One bench short.
- `ShortageActionCode` = **REPLACE** (listID `urn:ubl-examples:world:codelist:ShortageActionCode`)  
  The distributor asks for the missing bench with the next truck. The code is from the Trade Accord's shortage action list: REPLACE = Deliver the rest.
- `ReceivedDate` = **2026-03-25**  
  Unloaded.
- `OrderLineReference/LineID` = **1**  
  The order line.
- `DespatchLineReference/LineID` = **1**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **CL-DA-26-0153**  
  The despatch advice.
- `DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CL-DA-26-0153 is the example road/04, a DespatchAdvice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `Item/Description` = **Haz nanskir, 1800 mm, manskan skul stezir stan vazzhan nibir, bukdrek serskek kalnan, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Park bench Serra 180** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalInformation` = **Zurhul vek krukzan tarkul ziztan stan drek skubir krir vinstaz karhan.** (languageID `qau`)  
  What comes with the item in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.** (languageID `en-XB`)  
  What comes with the item in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; item bench-serra of Valdara Industries (world/items.json). A second Keyword would have to be in another language (UBL rule IND7).
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Bukdrek stezskir rek drek manskan savir gilrir.** (languageID `qau`)  
  The maker's warranty in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Five years on the frame against corrosion.** (languageID `en-XB`)  
  The maker's warranty in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Item/BuyersItemIdentification/ID` = **LD-10442**  
  The buyer's own item number: it resells this item as its item bench-serra-b.
- `Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The Codana item number of the maker, issued by the Codana Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a number of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label.
- `Item/StandardItemIdentification/IssuerScopeID` = **771**  
  The range of item numbers the agency gives out in the maker's country.
- `Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Item/CommodityClassification/CommodityCode` = **94017910** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-serra of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 94017910 = Benches for parks and gardens, with metal frames.
- `Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Cast steel, hot-dip galvanised**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Kiln-dried hardwood**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colour of the frame, one of the colours it is offered in.
- `Item/AdditionalItemProperty/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; item bench-serra of Valdara Industries (world/items.json)). One ListValue only: UBL rule IND7 allows a second one only in another language.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Load capacity**  
  The name of code LOAD in the Trade Accord's item property name list.
- `Item/AdditionalItemProperty/NameCode` = **LOAD** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: LOAD = Load capacity.
- `Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **SF**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `EA`)  
  The emission is per one bench.
- `Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Item/EnvironmentalEmission/LifecycleStageCode` = **MANUFACTURING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The part of the bench's life the figure covers. The code is from the Trade Accord's life cycle stage list: MANUFACTURING = Manufacturing.
- `Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **CRADLETOGATE** (listID `urn:ubl-examples:world:codelist:EmissionBoundaryCode`)  
  How much of the chain is included. The code is from the Trade Accord's emission boundary list: CRADLETOGATE = Cradle to gate.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/MaintenanceFrequencyCode` = **YEARLY** (listID `urn:ubl-examples:world:codelist:MaintenanceFrequencyCode`)  
  How often the item needs maintenance. The code is from the Trade Accord's maintenance frequency list: YEARLY = Once a year.
- `Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **STEEL** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: STEEL = Steel.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **HARDWOOD** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: HARDWOOD = Hardwood.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **PACKAGING** (listID `urn:ubl-examples:world:codelist:WasteTypeCode`)  
  The kind of waste the item leaves. The code is from the Trade Accord's waste type list: PACKAGING = Packaging.
- `Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **Stretch film and pallet straps, per bench**  
  The waste in words.
- `Item/CircularityProfile/WasteGenerated/WasteMeasure` = **0.4** (unitCode `KGM`)  
  How much of it per item.
- `Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **REPAIR10** (listID `urn:ubl-examples:world:codelist:ScoringSystemCode`)  
  The scale of the score. The code is from the Trade Accord's scoring system list: REPAIR10 = Repairability index, 0 to 10.
- `Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `Shipment/ID` = **CL-SH-26-0154**  
  The shipment received.
- `ID` = **2**  
  The line number.
- `UUID` = **986c8783-e70e-596b-82d0-e70c728412de**  
  A universally unique identifier of the line, derived from the document and the line number.
- `Note` = **The mis-picked box, in place of the missing bench.**  
  What was found.
- `ReceivedQuantity` = **13** (unitCode `EA`)  
  One box more than despatched.
- `OversupplyQuantity` = **1** (unitCode `EA`)  
  The extra box, held for collection by the next truck.
- `ReceivedDate` = **2026-03-25**  
  Unloaded.
- `OrderLineReference/LineID` = **2**  
  The order line.
- `DespatchLineReference/LineID` = **2**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **CL-DA-26-0153**  
  The despatch advice.
- `DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CL-DA-26-0153 is the example road/04, a DespatchAdvice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `Item/Description` = **Zudrir drir manskan gan drek Serra nanskir, stezir nibir, vazzhan.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Item/Description` = **Replacement side frame for the Serra bench, cast steel, galvanised.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Item/Name` = **Bench side frame casting** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-casting of Valdara Industries (world/items.json).
- `Item/ModelName` = **Serra 180 side frame**  
  The model; item bench-casting of Valdara Industries (world/items.json).
- `Item/BuyersItemIdentification/ID` = **LD-10443**  
  The buyer's own item number: it resells this item as its item bench-casting-b.
- `Item/SellersItemIdentification/ID` = **VI-C180**  
  The seller's own item number; item bench-casting of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The Codana item number of the maker, issued by the Codana Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a number of the world, not a GTIN; item bench-casting of Valdara Industries (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Item/CommodityClassification/CommodityCode` = **732599** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 732599 = Other cast articles of iron or steel: other.
- `Item/CommodityClassification/ItemClassificationCode` = **42999** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 42999 = Metal goods n.e.c..
- `Item/CommodityClassification/CommodityCode` = **73259990** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-casting of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 73259990 = Other cast articles of iron or steel.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ReceiptAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ReceiptAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:receipt-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-RA-26-0162</cbc:ID>
  <cbc:UUID>496ff071-d380-5baa-87d1-43a590437ea5</cbc:UUID>
  <cbc:IssueDate>2026-03-25</cbc:IssueDate>
  <cbc:IssueTime>15:40:00</cbc:IssueTime>
  <cbc:ReceiptAdviceTypeCode listID="urn:oasis:names:specification:ubl:codelist:gc:ReceiptAdviceTypeCode">Actual</cbc:ReceiptAdviceTypeCode>
  <cbc:DeliveryAcceptanceCode listID="urn:ubl-examples:world:codelist:DeliveryAcceptanceCode">ACCEPTED</cbc:DeliveryAcceptanceCode>
  <cbc:Note>Counted and checked at goods-in: one bench short, one box of side frames over.</cbc:Note>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>LD-PO-26-0149</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>CL-DA-26-0153</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>TH-WB-26-0159</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:DeliveryCustomerParty>
    <cac:Party>
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
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10441</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Castrano Logistics</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160203920705699</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
        <cbc:BuildingNumber>24</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4130</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Loading bays</cbc:Name>
        <cbc:JobTitle>Shift supervisor</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 1 041 677 4411</cbc:Telephone>
        <cbc:ElectronicMail>loading@castrano.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
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
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Order administrator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
          <cbc:Value>+999 1 344 474 4274</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>CL-SH-26-0154</cbc:ID>
    <cac:Delivery>
      <cbc:ActualDeliveryDate>2026-03-25</cbc:ActualDeliveryDate>
      <cbc:ActualDeliveryTime>09:40:00</cbc:ActualDeliveryTime>
    </cac:Delivery>
  </cac:Shipment>
  <cac:ReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:UUID>01193af5-785e-5e35-84c8-25a8b365acea</cbc:UUID>
    <cbc:Note>One pallet held three benches and a box of side frames: mis-picked at the 3PL.</cbc:Note>
    <cbc:ReceivedQuantity unitCode="EA">95</cbc:ReceivedQuantity>
    <cbc:ShortQuantity unitCode="EA">1</cbc:ShortQuantity>
    <cbc:ShortageActionCode listID="urn:ubl-examples:world:codelist:ShortageActionCode">REPLACE</cbc:ShortageActionCode>
    <cbc:ReceivedDate>2026-03-25</cbc:ReceivedDate>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>CL-DA-26-0153</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
    <cac:Item>
      <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul stezir stan vazzhan nibir, bukdrek serskek kalnan, gan zharsul krir drek tarkul.</cbc:Description>
      <cbc:Description languageID="en-XB">Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
      <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
      <cbc:Name languageID="en-XB">Park bench Serra 180</cbc:Name>
      <cbc:AdditionalInformation languageID="qau">Zurhul vek krukzan tarkul ziztan stan drek skubir krir vinstaz karhan.</cbc:AdditionalInformation>
      <cbc:AdditionalInformation languageID="en-XB">Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
      <cbc:Keyword>park bench, street furniture</cbc:Keyword>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180</cbc:ModelName>
      <cbc:WarrantyInformation languageID="qau">Bukdrek stezskir rek drek manskan savir gilrir.</cbc:WarrantyInformation>
      <cbc:WarrantyInformation languageID="en-XB">Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:BuyersItemIdentification>
        <cbc:ID>LD-10442</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
        <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
        <cbc:IssuerScopeID>771</cbc:IssuerScopeID>
      </cac:StandardItemIdentification>
      <cac:ItemSpecificationDocumentReference>
        <cbc:ID>VI-DS-B180</cbc:ID>
      </cac:ItemSpecificationDocumentReference>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">94017910</cbc:CommodityCode>
      </cac:CommodityClassification>
      <cac:AdditionalItemProperty>
        <cbc:Name>Frame material</cbc:Name>
        <cbc:Value>Cast steel, hot-dip galvanised</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Slat wood</cbc:Name>
        <cbc:Value>Kiln-dried hardwood</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Seats</cbc:Name>
        <cbc:Value>3</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:ID>COL</cbc:ID>
        <cbc:Name>Frame colour</cbc:Name>
        <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
        <cbc:ListValue>Ferro grey</cbc:ListValue>
        <cac:ItemPropertyGroup>
          <cbc:ID>APP</cbc:ID>
          <cbc:Name>Appearance</cbc:Name>
          <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
        </cac:ItemPropertyGroup>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:ID>LOAD</cbc:ID>
        <cbc:Name>Load capacity</cbc:Name>
        <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">LOAD</cbc:NameCode>
        <cbc:TestMethod>Static load on the seat for one hour, three seats loaded evenly, no lasting deformation</cbc:TestMethod>
        <cbc:ValueQuantity unitCode="KGM">450</cbc:ValueQuantity>
        <cbc:ValueQualifier>Distributed over the seat</cbc:ValueQualifier>
        <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
        <cac:ItemPropertyGroup>
          <cbc:ID>SAF</cbc:ID>
          <cbc:Name>Safety</cbc:Name>
          <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
        </cac:ItemPropertyGroup>
        <cac:StandardPropertyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:property">UR-SF-0450</cbc:ID>
          <cbc:IssuerScopeID>SF</cbc:IssuerScopeID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Codana Identification Agency</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:StandardPropertyIdentification>
      </cac:AdditionalItemProperty>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1800</cbc:Measure>
        <cbc:Description>Over the armrests</cbc:Description>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">DEPTH</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">620</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">780</cbc:Measure>
        <cbc:Description>Seat back at its highest point</cbc:Description>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">450</cbc:Measure>
        <cbc:Description>Above the ground when anchored</cbc:Description>
        <cbc:MinimumMeasure unitCode="MMT">440</cbc:MinimumMeasure>
        <cbc:MaximumMeasure unitCode="MMT">460</cbc:MaximumMeasure>
      </cac:Dimension>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">96</cbc:ValueMeasure>
        <cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>
        <cbc:ValueBaseMeasure unitCode="EA">1</cbc:ValueBaseMeasure>
        <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
        <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">MANUFACTURING</cbc:LifecycleStageCode>
        <cbc:LifecycleStageDescription>From the ore at the mine to the bench leaving the factory gate.</cbc:LifecycleStageDescription>
        <cbc:Description>Mining, steel making, casting, galvanising, sawing and the transport between them.</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode">CRADLETOGATE</cbc:FullnessIndicationCode>
          <cbc:EmissionFactorSource>The steelworks' and sawmill's measured energy use of 2025</cbc:EmissionFactorSource>
          <cac:EmissionFactorDocumentReference>
            <cbc:ID>VI-LCA-2025</cbc:ID>
          </cac:EmissionFactorDocumentReference>
        </cac:EmissionCalculationMethod>
        <cac:MeasurementPeriod>
          <cbc:StartDate>2025-01-01</cbc:StartDate>
          <cbc:EndDate>2025-12-31</cbc:EndDate>
        </cac:MeasurementPeriod>
      </cac:EnvironmentalEmission>
      <cac:CircularityProfile>
        <cbc:MaintenanceFrequencyCode listID="urn:ubl-examples:world:codelist:MaintenanceFrequencyCode">YEARLY</cbc:MaintenanceFrequencyCode>
        <cbc:MaintenanceFrequencyDescription>Tighten the slat bolts and touch up the coating once a year.</cbc:MaintenanceFrequencyDescription>
        <cac:ResourceConsumption>
          <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">STEEL</cbc:ResourceTypeCode>
          <cbc:ConsumptionMeasure unitCode="KGM">34</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Steel made from Serravona ore in Urvania</cbc:ResourceOriginDescription>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:ResourceConsumption>
        <cac:ResourceConsumption>
          <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">HARDWOOD</cbc:ResourceTypeCode>
          <cbc:ConsumptionMeasure unitCode="KGM">22.5</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:ResourceConsumption>
        <cac:WasteGenerated>
          <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:WasteTypeCode">PACKAGING</cbc:WasteTypeCode>
          <cbc:WasteTypeDescription>Stretch film and pallet straps, per bench</cbc:WasteTypeDescription>
          <cbc:WasteMeasure unitCode="KGM">0.4</cbc:WasteMeasure>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:WasteGenerated>
        <cac:RepairabilityScore>
          <cbc:ScoreNumeric>8</cbc:ScoreNumeric>
          <cbc:ScoringSystemCode listID="urn:ubl-examples:world:codelist:ScoringSystemCode">REPAIR10</cbc:ScoringSystemCode>
        </cac:RepairabilityScore>
        <cac:ProductDocumentationDocumentReference>
          <cbc:ID>VI-RM-B180</cbc:ID>
        </cac:ProductDocumentationDocumentReference>
      </cac:CircularityProfile>
    </cac:Item>
    <cac:Shipment>
      <cbc:ID>CL-SH-26-0154</cbc:ID>
    </cac:Shipment>
  </cac:ReceiptLine>
  <cac:ReceiptLine>
    <cbc:ID>2</cbc:ID>
    <cbc:UUID>986c8783-e70e-596b-82d0-e70c728412de</cbc:UUID>
    <cbc:Note>The mis-picked box, in place of the missing bench.</cbc:Note>
    <cbc:ReceivedQuantity unitCode="EA">13</cbc:ReceivedQuantity>
    <cbc:OversupplyQuantity unitCode="EA">1</cbc:OversupplyQuantity>
    <cbc:ReceivedDate>2026-03-25</cbc:ReceivedDate>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>2</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>CL-DA-26-0153</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
    <cac:Item>
      <cbc:Description languageID="qau">Zudrir drir manskan gan drek Serra nanskir, stezir nibir, vazzhan.</cbc:Description>
      <cbc:Description languageID="en-XB">Replacement side frame for the Serra bench, cast steel, galvanised.</cbc:Description>
      <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
      <cbc:Name languageID="en-XB">Bench side frame casting</cbc:Name>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180 side frame</cbc:ModelName>
      <cac:BuyersItemIdentification>
        <cbc:ID>LD-10443</cbc:ID>
      </cac:BuyersItemIdentification>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-C180</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="WCO HS 2022">732599</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">42999</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:CommodityClassification>
        <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">73259990</cbc:CommodityCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:ReceiptLine>
</ReceiptAdvice>
```
