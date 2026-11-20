# Unawarded Notification: Lumeport Public Works Department to Brackenmere Furniture

*Example 23 of the flow "A public tender (Bayvarra)" · [Unawarded Notification in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UNAWARDED-NOTIFICATION-SCHEMA)*

The furniture maker is told that the contract went to another tenderer.

[The XML file](23-UnawardedNotification.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:award-notification:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Award notification"; the community specification "Public procurement community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LPWD-DOC-26-0209**  
  The sender's number for this document.
- `UUID` = **e1de7889-b36e-5db6-b38b-dcbd566f2280**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-03-09**  
  Told on the day of the award decision, as the winner is.
- `IssueTime` = **10:15:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `ContractName` = **Park benches for the parks renewal programme**  
  The name of the contract the procedure is for.
- `Note` = **Your tender ranked second. It was lower in price, but the warranty offered scored lower on quality.**  
  Why it lost.

### Signature

Inside `Signature`:

- `ID` = **PWD-SIG-UNAWD**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/Department` = **Procurement office**  
  The department the post is for. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The public body's official name; identity of Lumeport Public Works Department (world/parties.json).
- `PartyLegalEntity/CompanyID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register (O142); identity of Lumeport Public Works Department (world/parties.json). The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Telephone` = **+999 2 38 8235 3927**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Public Works Department (world/parties.json).
- `Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brackenmere Furniture (world/parties.json).
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Trade sales**  
  The party's main desk, which handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Contact/JobTitle` = **Trade sales manager**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 602 606**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brackenmere Furniture (world/parties.json).
- `Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Minutes Document Reference

Inside `MinutesDocumentReference`:

- `ID` = **PWD-MIN-AWARD-26**  
  The minutes of the evaluation.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **PWD-EVAL-SCORES-BF**  
  The furniture maker's scores.
- `DocumentType` = **Evaluation scores**  
  The kind of document referred to, Brackenmere's scores in the evaluation, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Tender Result

Inside `TenderResult`:

- `AwardID` = **PWD-2026-PARKS-AWARD-1**  
  The award decision.
- `TenderResultCode` = **AWARDED** (listID `urn:ubl-examples:world:codelist:TenderResultCode`)  
  The contract is awarded. The code is from the Trade Accord's tender result list: AWARDED = Awarded.
- `Description` = **Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.**  
  Why it won.
- `AwardDate` = **2026-03-09**  
  The day the contract was awarded to another tenderer.
- `AwardTime` = **09:30:00**  
  The time of the decision, before the tenderers are told.
- `Contract/ID` = **PWD-2026-PARKS**  
  The framework contract.
- `Contract/ContractTypeCode` = **FRAMEWORK** (listID `urn:ubl-examples:world:codelist:ContractTypeCode`)  
  A framework contract. The code is from the Trade Accord's contract type list: FRAMEWORK = Framework agreement.
- `Contract/ValidityPeriod/StartDate` = **2026-03-20**  
  From its signature.
- `Contract/ValidityPeriod/DurationMeasure` = **24** (unitCode `MON`)  
  Two years.
- `AwardedTenderedProject/VariantID` = **V0**  
  The main offer.
- `AwardedTenderedProject/ProcurementProjectLot/ID` = **LOT-1**  
  Lot 1 of the procedure.
- `AwardedTenderedProject/ProcurementProjectLot/ID` = **LOT-2**  
  Lot 2 of the procedure.
- `AwardedTenderedProject/LegalMonetaryTotal/PayableAmount` = **124080.00** (currencyID `XBL`)  
  240 benches at 499 lume and their installation at 18 lume each.
- `ContractFormalizationPeriod/StartDate` = **2026-03-20**  
  The day after the standstill period ended (tender/22#F5).
- `ContractFormalizationPeriod/EndDate` = **2026-03-23**  
  Before the first call-off.
- `WinningParty/Rank` = **1**  
  First in the evaluation.
- `WinningParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `WinningParty/Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Appeal Terms

Inside `AppealTerms`:

- `Description` = **An appeal against the decision goes to the review board within ten days.**  
  How to appeal.
- `PresentationPeriod/StartDate` = **2026-03-10**  
  From the day after the award decision was sent, Tuesday 10 March (D28 point 1).
- `PresentationPeriod/EndDate` = **2026-03-19**  
  Ten days, to Thursday 19 March, the end of the standstill period.
- `AppealReceiverParty/PartyIdentification/ID` = **4718260539** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AppealReceiverParty/PartyName/Name` = **Procurement Review Board of Bayvarra**  
  The trading name; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/ID` = **LUM-ADR-075593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `AppealReceiverParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `AppealReceiverParty/PostalAddress/StreetName` = **Justice Row**  
  Street of the postal address. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/BuildingNumber` = **20**  
  Building number of the postal address. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/PostalZone` = **38519**  
  Postal code in Bayvarra's format (5 digits). identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `AppealReceiverParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Procurement Review Board of Bayvarra (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `AppealReceiverParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `AppealReceiverParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `AppealReceiverParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `AppealReceiverParty/Contact/Name` = **Registry**  
  The party's main desk, which handles this document; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/Contact/JobTitle` = **Registrar**  
  The job of the person who answers at the desk; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/Contact/Department` = **Registry**  
  The department the desk belongs to; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/Contact/Telephone` = **+999 2 38 4119 7873**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/Contact/ElectronicMail` = **registry@review-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Procurement Review Board of Bayvarra (world/parties.json).
- `AppealReceiverParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `AppealReceiverParty/ElectronicAddress/ElectronicAddressID` = **XB:4718260539** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Procurement Review Board of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UnawardedNotification xmlns="urn:oasis:names:specification:ubl:schema:xsd:UnawardedNotification-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:award-notification:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LPWD-DOC-26-0209</cbc:ID>
  <cbc:UUID>e1de7889-b36e-5db6-b38b-dcbd566f2280</cbc:UUID>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-03-09</cbc:IssueDate>
  <cbc:IssueTime>10:15:00-01:00</cbc:IssueTime>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:Note>Your tender ranked second. It was lower in price, but the warranty offered scored lower on quality.</cbc:Note>
  <cac:Signature>
    <cbc:ID>PWD-SIG-UNAWD</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
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
      <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
      <cbc:Department>Procurement office</cbc:Department>
      <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Procurement office</cbc:Name>
      <cbc:JobTitle>Procurement officer</cbc:JobTitle>
      <cbc:Department>Procurement</cbc:Department>
      <cbc:Telephone>+999 2 38 8235 3927</cbc:Telephone>
      <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:6250397184</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-821551</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Joiners Row</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71203</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Trade sales</cbc:Name>
      <cbc:JobTitle>Trade sales manager</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 602 606</cbc:Telephone>
      <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:MinutesDocumentReference>
    <cbc:ID>PWD-MIN-AWARD-26</cbc:ID>
  </cac:MinutesDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>PWD-EVAL-SCORES-BF</cbc:ID>
    <cbc:DocumentType>Evaluation scores</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:TenderResult>
    <cbc:AwardID>PWD-2026-PARKS-AWARD-1</cbc:AwardID>
    <cbc:TenderResultCode listID="urn:ubl-examples:world:codelist:TenderResultCode">AWARDED</cbc:TenderResultCode>
    <cbc:Description>Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.</cbc:Description>
    <cbc:AwardDate>2026-03-09</cbc:AwardDate>
    <cbc:AwardTime>09:30:00</cbc:AwardTime>
    <cac:Contract>
      <cbc:ID>PWD-2026-PARKS</cbc:ID>
      <cbc:ContractTypeCode listID="urn:ubl-examples:world:codelist:ContractTypeCode">FRAMEWORK</cbc:ContractTypeCode>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-03-20</cbc:StartDate>
        <cbc:DurationMeasure unitCode="MON">24</cbc:DurationMeasure>
      </cac:ValidityPeriod>
    </cac:Contract>
    <cac:AwardedTenderedProject>
      <cbc:VariantID>V0</cbc:VariantID>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-1</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:ProcurementProjectLot>
        <cbc:ID>LOT-2</cbc:ID>
      </cac:ProcurementProjectLot>
      <cac:LegalMonetaryTotal>
        <cbc:PayableAmount currencyID="XBL">124080.00</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:AwardedTenderedProject>
    <cac:ContractFormalizationPeriod>
      <cbc:StartDate>2026-03-20</cbc:StartDate>
      <cbc:EndDate>2026-03-23</cbc:EndDate>
    </cac:ContractFormalizationPeriod>
    <cac:WinningParty>
      <cbc:Rank>1</cbc:Rank>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:WinningParty>
  </cac:TenderResult>
  <cac:AppealTerms>
    <cbc:Description>An appeal against the decision goes to the review board within ten days.</cbc:Description>
    <cac:PresentationPeriod>
      <cbc:StartDate>2026-03-10</cbc:StartDate>
      <cbc:EndDate>2026-03-19</cbc:EndDate>
    </cac:PresentationPeriod>
    <cac:AppealReceiverParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">4718260539</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Procurement Review Board of Bayvarra</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-075593</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Justice Row</cbc:StreetName>
        <cbc:BuildingNumber>20</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38519</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Registry</cbc:Name>
        <cbc:JobTitle>Registrar</cbc:JobTitle>
        <cbc:Department>Registry</cbc:Department>
        <cbc:Telephone>+999 2 38 4119 7873</cbc:Telephone>
        <cbc:ElectronicMail>registry@review-xb.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:4718260539</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:AppealReceiverParty>
  </cac:AppealTerms>
</UnawardedNotification>
```
