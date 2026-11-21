# Proof of Reexportation Reminder: Selanu Chamber of Commerce to Ferrano Chamber of Commerce

*Example 3 of the flow "Samples to a trade fair on the island (temporary export)" · [Proof of Reexportation Reminder in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PROOF-OF-REEXPORTATION-REMINDER-SCHEMA)*

No answer after a month: a reminder.

[The XML file](03-ProofOfReexportationReminder.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:proof-of-reexportation:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Proof of re-exportation". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:temporary-admission:1.0**  
  The Trade Accord's process profile the document belongs to: temporary admission, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **FCC/2026/3170**  
  The collaboration this document belongs to: the carnet the Ferrano Chamber of Commerce issues and its proof of re-exportation. Ferrano Chamber of Commerce started it and gave it this identifier, which every document of it repeats.
- `ID` = **SCC/ATA/2026/0097**  
  The sender's number for this document.
- `UUID` = **e53b1117-a5c9-5bbc-827c-2dd70a8dbfe4**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-08-24**  
  Monday 24 August, a month after the request: no answer yet (the Sunday a month later is no working day).
- `IssueTime` = **12:04:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `ProcedureCode` = **2000** (listID `urn:ubl-examples:world:codelist:CustomsProcedureCode`)  
  The procedure the samples were under on the island. The code is from the Trade Accord's customs procedure list: 2000 = Temporary admission, no previous procedure.
- `Note` = **Without proof within 30 days, the island's import consumption tax on the samples and the carnet surcharge will be claimed from the guarantee.**  
  What happens otherwise.
- `VersionID` = **1**  
  The first reminder.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the samples travelled under.

### Proof of Reexportation Request Document Reference

Inside `ProofOfReexportationRequestDocumentReference`:

- `ID` = **SCC/ATA/2026/0084**  
  The request unanswered.

### Importing Guarantor Party

Inside `ImportingGuarantorParty`:

- `PartyIdentification/ID` = **GOV-243** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Selanu Chamber of Commerce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Chamber of Commerce**  
  The trading name; as Selanu Chamber of Commerce gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `PostalAddress/ID` = **95763809** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Chamber of Commerce gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Chamber of Commerce gives it.
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Chamber of Commerce gives it.
- `PostalAddress/BuildingNumber` = **30**  
  Building number of the postal address. As Selanu Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Chamber of Commerce gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Chamber of Commerce**  
  The public body's official name; as Selanu Chamber of Commerce gives it.
- `PartyLegalEntity/CompanyID` = **GOV-243** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  Number in the Government list of public bodies of Lisavu, which gives every public body a number of its own (GOV- and 3 digits), derived from no other register ; as Selanu Chamber of Commerce gives it. The schemeID names the scheme it is from: the government list of public bodies of Lisavu (GOV- and 3 digits).
- `Contact/Name` = **Carnet office**  
  The party's carnet office desk: the desk for its role in this document (a carnet); as Selanu Chamber of Commerce gives it.
- `Contact/JobTitle` = **Carnet officer**  
  The job of the person who answers at the desk; as Selanu Chamber of Commerce gives it.
- `Contact/Department` = **Carnets**  
  The department the desk belongs to; as Selanu Chamber of Commerce gives it.
- `Contact/Telephone` = **+999 3 723 0513**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Chamber of Commerce gives it.
- `Contact/ElectronicMail` = **carnets@chamber-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu Chamber of Commerce gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Chamber of Commerce gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:GOV-243** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Selanu Chamber of Commerce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Exporting Guarantor Party

Inside `ExportingGuarantorParty`:

- `PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; as Ferrano Chamber of Commerce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; as Ferrano Chamber of Commerce gives it.
- `PostalAddress/ID` = **4160202319527073** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Chamber of Commerce gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Trazhek Han Zhatrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Chamber of Commerce gives it.
- `PostalAddress/StreetName` = **Piazza del Mercato** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Chamber of Commerce gives it.
- `PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). As Ferrano Chamber of Commerce gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The public body's official name; as Ferrano Chamber of Commerce gives it.
- `PartyLegalEntity/CompanyID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  Number in the Index of Public Administrations of Urvania, which gives every public body a number of its own (xu_ and four lower-case letters or digits), derived from no other register ; as Ferrano Chamber of Commerce gives it. The schemeID names the scheme it is from: the index of public administrations of Urvania (xu_ and four lower-case letters or digits, assigned by the index on the body's accreditation; no real IPA code of Italy's index starts with xu_).
- `Contact/Name` = **Carnet office**  
  The party's carnet office desk: the desk for its role in this document (a carnet); as Ferrano Chamber of Commerce gives it.
- `Contact/JobTitle` = **Carnet officer**  
  The job of the person who answers at the desk; as Ferrano Chamber of Commerce gives it.
- `Contact/Department` = **Carnets**  
  The department the desk belongs to; as Ferrano Chamber of Commerce gives it.
- `Contact/Telephone` = **+999 1 041 714 2503**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Chamber of Commerce gives it.
- `Contact/ElectronicMail` = **carnets@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Ferrano Chamber of Commerce gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Ferrano Chamber of Commerce gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:xu_m2vd** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; as Ferrano Chamber of Commerce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importing Customs Party

Inside `ImportingCustomsParty`:

- `PartyIdentification/ID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Island Customs Service**  
  The trading name; as Island Customs Service gives it.
- `PostalAddress/ID` = **65334843** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Island Customs Service gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Island Customs Service gives it.
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Island Customs Service gives it.
- `PostalAddress/BuildingNumber` = **53**  
  Building number of the postal address. As Island Customs Service gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **SCC/ATA/2026/0097**  
  The reminder the chamber endorses, as the guaranteeing association whose guarantee is at stake.
- `ApprovalStatus` = **Endorsed**  
  The status of the endorsement itself; the request's open state is in the note.
- `EndorserParty/RoleCode` = **GUARANTOR** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The importing guarantor. The code is from the Trade Accord's endorser role list: GUARANTOR = Guaranteeing association.
- `EndorserParty/SequenceNumeric` = **1**  
  The only one.
- `EndorserParty/Party/PartyIdentification/ID` = **GOV-243** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/Party/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/SignatoryContact/Name` = **Carnet office**  
  The chamber's carnet office.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **Import consumption tax of 10 % on the declared value of 399.20 coral, 39.920, and the carnet surcharge of 10 % of the tax, 3.992: 43.912 coral fall due if no proof arrives within 30 days. Benches of Accord origin owe no duty.**  
  The claim that would follow.
- `Amount` = **43.912** (currencyID `XLC`)  
  The tax and surcharge at stake.
- `PaymentDueDate` = **2026-09-23**  
  The day they fall due: 30 days after the reminder.

### Goods Item Passport Counterfoil

Inside `GoodsItemPassportCounterfoil`:

- `ID` = **IMP-1**  
  The importation counterfoil (white sheet) of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `FinalReexportationDate` = **2026-06-30**  
  The limit the island's customs set on the importation counterfoil, shorter than the carnet's year: a short fair admission.
- `Note` = **Stamped at Selanu airport on 2 June; no discharged re-exportation voucher on file.**  
  The counterfoil the claim rests on.
- `CustomsOfficeLocation/ID` = **XL001002** (schemeID `urn:ubl-examples:world:XL:customs-office`)  
  The office's number in the customs office list of Lisavu.
- `CustomsOfficeLocation/LocationTypeCode` = **CUSTOMSOFFICE** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs office at the airport. The code is from the Trade Accord's customs location type list: CUSTOMSOFFICE = Customs office.
- `CustomsOfficeLocation/Name` = **Island Customs Service, Selanu airport**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `ImportationDocumentReference/ID` = **XL-CUS/2026/12905**  
  The island's customs' registration of the importation, noted with the stamp.
- `ImportationDocumentReference/IssueDate` = **2026-06-02**  
  The day customs stamped the counterfoil.
- `ImportationDocumentReference/DocumentType` = **Importation registration**  
  The kind of customs record, in words.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **XL-CUS/2026/11199**  
  The customs' notice.
- `DocumentType` = **Customs notice**  
  The kind of document referred to, the island customs' notice to the chamber, a document outside the examples, in words: no list has an exact code for it (cited).

### Signature

Inside `Signature`:

- `ID` = **SCC-SIG-26-PRM**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **GOV-243** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ProofOfReexportationReminder xmlns="urn:oasis:names:specification:ubl:schema:xsd:ProofOfReexportationReminder-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:proof-of-reexportation:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:temporary-admission:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>FCC/2026/3170</cbc:ProfileExecutionID>
  <cbc:ID>SCC/ATA/2026/0097</cbc:ID>
  <cbc:UUID>e53b1117-a5c9-5bbc-827c-2dd70a8dbfe4</cbc:UUID>
  <cbc:IssueDate>2026-08-24</cbc:IssueDate>
  <cbc:IssueTime>12:04:00+00:00</cbc:IssueTime>
  <cbc:ProcedureCode listID="urn:ubl-examples:world:codelist:CustomsProcedureCode">2000</cbc:ProcedureCode>
  <cbc:Note>Without proof within 30 days, the island's import consumption tax on the samples and the carnet surcharge will be claimed from the guarantee.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
  <cac:ProofOfReexportationRequestDocumentReference>
    <cbc:ID>SCC/ATA/2026/0084</cbc:ID>
  </cac:ProofOfReexportationRequestDocumentReference>
  <cac:ImportingGuarantorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-243</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">95763809</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>30</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Selanu Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-243</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Carnet office</cbc:Name>
      <cbc:JobTitle>Carnet officer</cbc:JobTitle>
      <cbc:Department>Carnets</cbc:Department>
      <cbc:Telephone>+999 3 723 0513</cbc:Telephone>
      <cbc:ElectronicMail>carnets@chamber-selanu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-243</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImportingGuarantorParty>
  <cac:ExportingGuarantorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202319527073</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Trazhek Han Zhatrir</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Piazza del Mercato</cbc:StreetName>
      <cbc:BuildingNumber>15</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4110</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Carnet office</cbc:Name>
      <cbc:JobTitle>Carnet officer</cbc:JobTitle>
      <cbc:Department>Carnets</cbc:Department>
      <cbc:Telephone>+999 1 041 714 2503</cbc:Telephone>
      <cbc:ElectronicMail>carnets@camera-ferrano.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:xu_m2vd</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExportingGuarantorParty>
  <cac:ImportingCustomsParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-118</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Island Customs Service</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">65334843</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>53</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ImportingCustomsParty>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>SCC/ATA/2026/0097</cbc:DocumentID>
    <cbc:ApprovalStatus>Endorsed</cbc:ApprovalStatus>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">GUARANTOR</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-243</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Carnet office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
  </cac:IssuerEndorsement>
  <cac:PaymentTerms>
    <cbc:Note>Import consumption tax of 10 % on the declared value of 399.20 coral, 39.920, and the carnet surcharge of 10 % of the tax, 3.992: 43.912 coral fall due if no proof arrives within 30 days. Benches of Accord origin owe no duty.</cbc:Note>
    <cbc:Amount currencyID="XLC">43.912</cbc:Amount>
    <cbc:PaymentDueDate>2026-09-23</cbc:PaymentDueDate>
  </cac:PaymentTerms>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>IMP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:FinalReexportationDate>2026-06-30</cbc:FinalReexportationDate>
    <cbc:Note>Stamped at Selanu airport on 2 June; no discharged re-exportation voucher on file.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-office">XL001002</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">CUSTOMSOFFICE</cbc:LocationTypeCode>
      <cbc:Name>Island Customs Service, Selanu airport</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:ImportationDocumentReference>
      <cbc:ID>XL-CUS/2026/12905</cbc:ID>
      <cbc:IssueDate>2026-06-02</cbc:IssueDate>
      <cbc:DocumentType>Importation registration</cbc:DocumentType>
    </cac:ImportationDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:AdditionalDocumentReference>
    <cbc:ID>XL-CUS/2026/11199</cbc:ID>
    <cbc:DocumentType>Customs notice</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>SCC-SIG-26-PRM</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-243</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ProofOfReexportationReminder>
```
