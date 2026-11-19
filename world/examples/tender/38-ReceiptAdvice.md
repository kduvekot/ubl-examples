# Receipt Advice: Lumeport Public Works Department to Valdara Industries

*Example 38 of the flow "A public tender (Bayvarra)" · [Receipt Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-RECEIPT-ADVICE-SCHEMA)*

The department accepts the release: 39 benches and their installation, one bench rejected as damaged; the contract's 30 days of payment run from this acceptance (D28 point 9, O69).

[The XML file](38-ReceiptAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:receipt-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Receipt advice". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-RA-26-0223**  
  The department's number for the acceptance.
- `UUID` = **7b7a0126-4c5e-5e7b-b42d-9f93027b3319**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-13**  
  Monday 13 April, after the installation ended on Friday 10 April: Upland State Day, but Lumeport, in Coastal State, works (D28 point 9).
- `IssueTime` = **11:42:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `ReceiptAdviceTypeCode` = **Actual** (listID `urn:oasis:names:specification:ubl:codelist:gc:ReceiptAdviceTypeCode`)  
  UBL's receipt advice type code: the goods actually received. The code is from the world's copy of UBL's Receipt advice type list, with a listID: Actual = An arrival that has passed goods inspection and is accepted (or not)..
- `DeliveryAcceptanceCode` = **PARTIAL** (listID `urn:ubl-examples:world:codelist:DeliveryAcceptanceCode`)  
  39 benches and their installation accepted, one bench rejected. The code is from the Trade Accord's delivery acceptance list: PARTIAL = Partly refused.
- `Note` = **Release 1 accepted: 39 benches installed and accepted; one bench, damaged during installation on 2 April, rejected, with no replacement in this release. The 30 days of payment run from today.**  
  The acceptance the contract's payment term counts from (O69, D22).
- `LineCountNumeric` = **2**  
  The benches and the installation.

### Order Reference

Inside `OrderReference`:

- `ID` = **LPWD-PO-26-0213**  
  The call-off accepted.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **CL-DA-26-0216**  
  The despatch advice of the benches.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **PWD-CONTRACT-2026-PARKS**  
  The contract whose payment term counts from this acceptance.
- `DocumentType` = **Framework contract**  
  What it is.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-RA**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Parks depot**  
  The party's parks depot desk: the desk for its role in this document (it receives the goods); identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Depot supervisor**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Parks maintenance**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 8235 3927**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **parksdepot@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XU = Urvanian English.
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
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **dispatch@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receipt Line

Inside `ReceiptLine`:

- `ID` = **1**  
  The benches.
- `ReceivedQuantity` = **40** (unitCode `EA`)  
  Forty benches delivered on 31 March.
- `RejectedQuantity` = **1** (unitCode `EA`)  
  One bench rejected.
- `RejectReasonCode` = **DAMAGED** (listID `urn:ubl-examples:world:codelist:RejectReasonCode`)  
  Why refused. The code is from the Trade Accord's reject reason list: DAMAGED = Damaged.
- `RejectReason` = **Side frame cracked while the bench was anchored on 2 April.**  
  In words.
- `RejectActionCode` = **CREDIT** (listID `urn:ubl-examples:world:codelist:RejectActionCode`)  
  A credit, not a replacement: the department's 40th bench comes with release 2 (D28). The code is from the Trade Accord's reject action list: CREDIT = Credit requested.
- `ReceivedDate` = **2026-03-31**  
  Delivered.
- `OrderLineReference/LineID` = **1**  
  The order line.
- `DespatchLineReference/LineID` = **1**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **CL-DA-26-0216**  
  The despatch advice.
- `DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: CL-DA-26-0216 is the example tender/29, a DespatchAdvice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `Item/Description` = **Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek trek skan sakmul (RAL 6005), sir galtan maksul, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-serra-g of Valdara Industries (world/items.json).
- `Item/Description` = **Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron in moss green (RAL 6005), a special colour, five slats of thermally modified ash, for bolting to the ground.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item bench-serra-g of Valdara Industries (world/items.json).
- `Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra-g of Valdara Industries (world/items.json).
- `Item/Name` = **Park bench Serra 180** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item bench-serra-g of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra-g of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ExtendedID` = **GRN**  
  The variant of the item: the frame colour, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRN** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRN = Green.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in moss green, RAL 6005**  
  The variant in words.
- `Item/StandardItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Valdara Industries gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Valdara Industries and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; item bench-serra-g of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label: Code 128 carries letters and digits.
- `Item/StandardItemIdentification/IssuerScopeID` = **KXU10014**  
  The scope within which Valdara Industries gives its item numbers: its company prefix, the issuing agency code KXU and its Codana company number; what follows is the company's own reference.
- `ID` = **2**  
  The installation.
- `ReceivedQuantity` = **39** (unitCode `EA`)  
  39 benches assembled and anchored by Saltmere Engineering.
- `ReceivedDate` = **2026-04-10**  
  The work ended on Friday 10 April.
- `TimingComplaintCode` = **LATE** (listID `urn:ubl-examples:world:codelist:TimingComplaintCode`)  
  Completed after the date the order asked. The code is from the Trade Accord's timing complaint list: LATE = Late.
- `TimingComplaint` = **Completed on 10 April, three working days after 7 April; one day is waived because the department delayed access to one site.**  
  What the penalty clause counts (tender/34#F3).
- `OrderLineReference/LineID` = **2**  
  The order line.
- `Item/Description` = **Hiktran skul zan nanskir stan nakskek kartran trek drek tarkul vek drek zurhul ziztan.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-installation of Valdara Industries (world/items.json).
- `Item/Description` = **Assembly of one bench and its anchoring in the ground with the supplied anchors.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item bench-installation of Valdara Industries (world/items.json).
- `Item/Name` = **Dreknul skul sir haz nanskir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-installation of Valdara Industries (world/items.json).
- `Item/Name` = **Installation of a park bench** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item bench-installation of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **VI-INST-B**  
  The seller's own item number; item bench-installation of Valdara Industries (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ReceiptAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ReceiptAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:receipt-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-RA-26-0223</cbc:ID>
  <cbc:UUID>7b7a0126-4c5e-5e7b-b42d-9f93027b3319</cbc:UUID>
  <cbc:IssueDate>2026-04-13</cbc:IssueDate>
  <cbc:IssueTime>11:42:00-01:00</cbc:IssueTime>
  <cbc:ReceiptAdviceTypeCode listID="urn:oasis:names:specification:ubl:codelist:gc:ReceiptAdviceTypeCode">Actual</cbc:ReceiptAdviceTypeCode>
  <cbc:DeliveryAcceptanceCode listID="urn:ubl-examples:world:codelist:DeliveryAcceptanceCode">PARTIAL</cbc:DeliveryAcceptanceCode>
  <cbc:Note>Release 1 accepted: 39 benches installed and accepted; one bench, damaged during installation on 2 April, rejected, with no replacement in this release. The 30 days of payment run from today.</cbc:Note>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>LPWD-PO-26-0213</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>CL-DA-26-0216</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>PWD-CONTRACT-2026-PARKS</cbc:ID>
    <cbc:DocumentType>Framework contract</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>PWD-SIG-RA</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-000417</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Parks depot</cbc:Name>
        <cbc:JobTitle>Depot supervisor</cbc:JobTitle>
        <cbc:Department>Parks maintenance</cbc:Department>
        <cbc:Telephone>+999 2 38 8235 3927</cbc:Telephone>
        <cbc:ElectronicMail>parksdepot@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:6250397184</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:DespatchSupplierParty>
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
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
      </cac:Language>
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
        <cbc:Name>Dispatch office</cbc:Name>
        <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:ReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:ReceivedQuantity unitCode="EA">40</cbc:ReceivedQuantity>
    <cbc:RejectedQuantity unitCode="EA">1</cbc:RejectedQuantity>
    <cbc:RejectReasonCode listID="urn:ubl-examples:world:codelist:RejectReasonCode">DAMAGED</cbc:RejectReasonCode>
    <cbc:RejectReason>Side frame cracked while the bench was anchored on 2 April.</cbc:RejectReason>
    <cbc:RejectActionCode listID="urn:ubl-examples:world:codelist:RejectActionCode">CREDIT</cbc:RejectActionCode>
    <cbc:ReceivedDate>2026-03-31</cbc:ReceivedDate>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>CL-DA-26-0216</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
    <cac:Item>
      <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek trek skan sakmul (RAL 6005), sir galtan maksul, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.</cbc:Description>
      <cbc:Description languageID="en-XB">Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron in moss green (RAL 6005), a special colour, five slats of thermally modified ash, for bolting to the ground.</cbc:Description>
      <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
      <cbc:Name languageID="en-XB">Park bench Serra 180</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
        <cbc:ExtendedID>GRN</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
          <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
          <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRN</cbc:DescriptionCode>
          <cbc:Description>Frame in moss green, RAL 6005</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
        <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
        <cbc:IssuerScopeID>KXU10014</cbc:IssuerScopeID>
      </cac:StandardItemIdentification>
    </cac:Item>
  </cac:ReceiptLine>
  <cac:ReceiptLine>
    <cbc:ID>2</cbc:ID>
    <cbc:ReceivedQuantity unitCode="EA">39</cbc:ReceivedQuantity>
    <cbc:ReceivedDate>2026-04-10</cbc:ReceivedDate>
    <cbc:TimingComplaintCode listID="urn:ubl-examples:world:codelist:TimingComplaintCode">LATE</cbc:TimingComplaintCode>
    <cbc:TimingComplaint>Completed on 10 April, three working days after 7 April; one day is waived because the department delayed access to one site.</cbc:TimingComplaint>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description languageID="qau">Hiktran skul zan nanskir stan nakskek kartran trek drek tarkul vek drek zurhul ziztan.</cbc:Description>
      <cbc:Description languageID="en-XB">Assembly of one bench and its anchoring in the ground with the supplied anchors.</cbc:Description>
      <cbc:Name languageID="qau">Dreknul skul sir haz nanskir</cbc:Name>
      <cbc:Name languageID="en-XB">Installation of a park bench</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-INST-B</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
  </cac:ReceiptLine>
</ReceiptAdvice>
```
