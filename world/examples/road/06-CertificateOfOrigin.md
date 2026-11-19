# Certificate of Origin: Valdara Industries to Ferrano Chamber of Commerce

*Example 6 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Certificate of Origin in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CERTIFICATE-OF-ORIGIN-SCHEMA)*

The goods qualify for preferential duty in Bayvarra; the manufacturer applies to its chamber of commerce for a certificate of origin.

[The XML file](06-CertificateOfOrigin.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:certificate-of-origin:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Certificate of origin". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FCC-CO-26-0157**  
  The number of the certificate, given by the chamber.
- `UUID` = **a46337e2-176c-5866-9871-158007b21756**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-20**  
  The day the exporter applies, before the goods leave.
- `IssueTime` = **12:39:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Description` = **Certificate of origin for park benches and castings made in Urvania.**  
  What the certificate is for.
- `Note` = **Drakhan dranan karul drek rizir denskek.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): What the certificate is for.
- `Note` = **Preferential origin under the trade accord.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What the certificate is for.
- `VersionID` = **1**  
  The first version.

### Signature

Inside `Signature`:

- `ID` = **VI-SIG-CO-06**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk desk: the desk for its role in this document (it deals with customs); identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **customs@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Endorser Party

Inside `EndorserParty`:

- `RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `SequenceNumeric` = **1**  
  The first and only endorsement.
- `Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/ID` = **4160202319527073** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Trazhek Han Zhatrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/StreetName` = **Piazza del Mercato** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The public body's official name; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  Number in the Index of Public Administrations of Urvania, which gives every public body a number of its own (xu_ and four lower-case letters or digits), derived from no other register (O142); identity of Ferrano Chamber of Commerce (world/parties.json). The schemeID names the scheme it is from: the index of public administrations of Urvania (xu_ and four lower-case letters or digits, assigned by the index on the body's accreditation; no real IPA code of Italy's index starts with xu_ (world/codelists/sources/ipa/)).
- `Party/Contact/Name` = **Certificates office**  
  The party's certificates office desk: the desk for its role in this document (a certificate); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/JobTitle` = **Certificates officer**  
  The job of the person who answers at the desk; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Department` = **Certificates**  
  The department the desk belongs to; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 714 2503**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:xu_m2vd** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

### Certificate of Origin Application

Inside `CertificateOfOriginApplication`:

- `ReferenceID` = **VI-AP-26-0158**  
  The exporter's reference for its application.
- `CertificateType` = **Preferential**  
  The goods qualify for the preferential duty rate in Bayvarra; the importer needs this certificate to claim it.
- `ApplicationStatusCode` = **SUBMITTED** (listID `urn:ubl-examples:world:codelist:ApplicationStatusCode`)  
  The exporter submits the application. The code is from the Trade Accord's application status list: SUBMITTED = Submitted.
- `OriginalJobID` = **LD-PO-26-0149**  
  The order the goods are for.
- `PreviousJobID` = **VI-CO-25-0412**  
  The exporter's application of last year for the same goods.
- `Remarks` = **Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.**  
  Why the goods are of Urvanian origin.
- `Shipment/ID` = **CL-SH-26-0154**  
  The shipment the certificate covers.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **3830400** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Haz nanskir, 1800 mm, manskan skul stezir stan vazzhan nibir, bukdrek serskek kalnan, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **94017910** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-serra of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 94017910 = Benches for parks and gardens, with metal frames.
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **57000** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Zudrir drir manskan gan drek Serra nanskir, stezir nibir, vazzhan.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, cast steel, galvanised.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **732599** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 732599 = Other cast articles of iron or steel: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **42999** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 42999 = Metal goods n.e.c..
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **73259990** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-casting of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 73259990 = Other cast articles of iron or steel.
- `EndorserParty/RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.
- `PreparationParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PreparationParty/PartyName/Name` = **Valdara Industries**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `ExporterParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ExporterParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `ImporterParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ImporterParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuingCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The goods were made in Urvania, and the certificate is issued there. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `DocumentDistribution/ID` = **1**  
  The importer's copy.
- `DocumentDistribution/DocumentTypeCode` = **CertificateOfOrigin** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this certificate. The code is from the Trade Accord's UBL document type list: CertificateOfOrigin = Certificate Of Origin.
- `DocumentDistribution/DistributionTypeCode` = **ELECTRONICCOPY** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The importer gets a copy as a message; it declares the origin at import. The code is from the Trade Accord's distribution type list: ELECTRONICCOPY = Electronic copy.
- `DocumentDistribution/Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DocumentDistribution/Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupportingDocumentReference/ID` = **LD-PO-26-0149**  
  The commercial document behind the goods.
- `SupportingDocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LD-PO-26-0149 is the example road/01, a Order; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Order.
- `Signature/ID` = **VI-SIG-COA**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC-CO-26-0157**  
  The certificate this endorsement belongs to.
- `ApprovalStatus` = **Pending**  
  Not yet endorsed: the application is with the chamber.
- `EndorserParty/RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

### Insurance Endorsement

Inside `InsuranceEndorsement`:

- `DocumentID` = **WS-CP-26-4471-E1**  
  The insurer's endorsement of the cargo policy for this consignment.
- `ApprovalStatus` = **Endorsed**  
  The insurer confirms the cover.
- `Remarks` = **The goods described in this certificate are insured door to door.**  
  What it confirms.
- `EndorserParty/RoleCode` = **INSURER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  It endorses as insurer. The code is from the Trade Accord's endorser role list: INSURER = Insurer.
- `EndorserParty/SequenceNumeric` = **2**  
  After the chamber; the embassy legalises separately.
- `EndorserParty/Party/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/Party/PartyName/Name` = **Wavesure Cargo Insurance**  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/SignatoryContact/Name` = **Cargo claims desk**  
  Who signs for the insurer.
- `Signature/ID` = **WS-SIG-26-E1**  
  The insurer's seal on the endorsement.
- `Signature/SignatoryParty/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Wavesure Cargo Insurance**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CertificateOfOrigin xmlns="urn:oasis:names:specification:ubl:schema:xsd:CertificateOfOrigin-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:certificate-of-origin:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FCC-CO-26-0157</cbc:ID>
  <cbc:UUID>a46337e2-176c-5866-9871-158007b21756</cbc:UUID>
  <cbc:IssueDate>2026-03-20</cbc:IssueDate>
  <cbc:IssueTime>12:39:00-01:00</cbc:IssueTime>
  <cbc:Description>Certificate of origin for park benches and castings made in Urvania.</cbc:Description>
  <cbc:Note languageID="qau">Drakhan dranan karul drek rizir denskek.</cbc:Note>
  <cbc:Note languageID="en-XU">Preferential origin under the trade accord.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:Signature>
    <cbc:ID>VI-SIG-CO-06</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:ExporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>customs@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:ImporterParty>
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
  </cac:ImporterParty>
  <cac:EndorserParty>
    <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">CHAMBER</cbc:RoleCode>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cac:Party>
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
        <cbc:Name>Certificates office</cbc:Name>
        <cbc:JobTitle>Certificates officer</cbc:JobTitle>
        <cbc:Department>Certificates</cbc:Department>
        <cbc:Telephone>+999 1 041 714 2503</cbc:Telephone>
        <cbc:ElectronicMail>certificates@camera-ferrano.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:xu_m2vd</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
    <cac:SignatoryContact>
      <cbc:Name>Certificates office</cbc:Name>
    </cac:SignatoryContact>
  </cac:EndorserParty>
  <cac:CertificateOfOriginApplication>
    <cbc:ReferenceID>VI-AP-26-0158</cbc:ReferenceID>
    <cbc:CertificateType>Preferential</cbc:CertificateType>
    <cbc:ApplicationStatusCode listID="urn:ubl-examples:world:codelist:ApplicationStatusCode">SUBMITTED</cbc:ApplicationStatusCode>
    <cbc:OriginalJobID>LD-PO-26-0149</cbc:OriginalJobID>
    <cbc:PreviousJobID>VI-CO-25-0412</cbc:PreviousJobID>
    <cbc:Remarks>Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.</cbc:Remarks>
    <cac:Shipment>
      <cbc:ID>CL-SH-26-0154</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Park bench Serra 180</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">3830400</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">96</cbc:Quantity>
        <cac:Item>
          <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul stezir stan vazzhan nibir, bukdrek serskek kalnan, gan zharsul krir drek tarkul.</cbc:Description>
          <cbc:Description languageID="en-XU">Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
          <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
          <cbc:Name languageID="en-XU">Park bench Serra 180</cbc:Name>
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
        </cac:Item>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Bench side frame casting</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">57000</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description languageID="qau">Zudrir drir manskan gan drek Serra nanskir, stezir nibir, vazzhan.</cbc:Description>
          <cbc:Description languageID="en-XU">Replacement side frame for the Serra bench, cast steel, galvanised.</cbc:Description>
          <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
          <cbc:Name languageID="en-XU">Bench side frame casting</cbc:Name>
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
      </cac:GoodsItem>
    </cac:Shipment>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">CHAMBER</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:PreparationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:PreparationParty>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:ExporterParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:ExporterParty>
    <cac:ImporterParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:ImporterParty>
    <cac:IssuingCountry>
      <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
    </cac:IssuingCountry>
    <cac:DocumentDistribution>
      <cbc:ID>1</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">CertificateOfOrigin</cbc:DocumentTypeCode>
      <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONICCOPY</cbc:DistributionTypeCode>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:DocumentDistribution>
    <cac:SupportingDocumentReference>
      <cbc:ID>LD-PO-26-0149</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
    </cac:SupportingDocumentReference>
    <cac:Signature>
      <cbc:ID>VI-SIG-COA</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:CertificateOfOriginApplication>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>FCC-CO-26-0157</cbc:DocumentID>
    <cbc:ApprovalStatus>Pending</cbc:ApprovalStatus>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">CHAMBER</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
  </cac:IssuerEndorsement>
  <cac:InsuranceEndorsement>
    <cbc:DocumentID>WS-CP-26-4471-E1</cbc:DocumentID>
    <cbc:ApprovalStatus>Endorsed</cbc:ApprovalStatus>
    <cbc:Remarks>The goods described in this certificate are insured door to door.</cbc:Remarks>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">INSURER</cbc:RoleCode>
      <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Wavesure Cargo Insurance</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Cargo claims desk</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:Signature>
      <cbc:ID>WS-SIG-26-E1</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Wavesure Cargo Insurance</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:InsuranceEndorsement>
</CertificateOfOrigin>
```
