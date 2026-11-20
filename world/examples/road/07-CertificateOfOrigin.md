# Certificate of Origin: Ferrano Chamber of Commerce to Lumeway Distribution

*Example 7 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Certificate of Origin in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CERTIFICATE-OF-ORIGIN-SCHEMA)*

The chamber, the body Urvania authorises under the Trade Accord to issue proofs of preferential origin, checks the application, issues the certificate under its own number and is its only endorser: a certificate between Accord members needs no legalisation. It makes the certificate available to the importer, who needs it for the import declaration.

[The XML file](07-CertificateOfOrigin.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:certificate-of-origin:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Certificate of origin". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900043291**  
  The collaboration this document belongs to: the certificate of origin Valdara applies for at the Ferrano Chamber of Commerce. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **FCC/CO/2026/0090**  
  The number of the certificate, given by the chamber.
- `UUID` = **3152b116-509a-5a0d-8b57-97a8e2b066d0**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-23**  
  The day the chamber issued the certificate: Monday morning, before the export declaration.
- `IssueTime` = **08:41:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Description` = **Certificate of origin for park benches and castings made in Urvania.**  
  What the document is for.
- `Note` = **Preferential origin under the trade accord.**  
  What the certificate is for.
- `VersionID` = **1**  
  The first version of the certificate.

### Signature

Inside `Signature`:

- `ID` = **FCC-SIG-CO-07**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.

### Importer Party

Inside `ImporterParty`:

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
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; as Lumeway Distribution gives it.
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **customs@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Endorser Party

Inside `EndorserParty`:

- `RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country, the body Urvania authorises under the Accord to issue proofs of preferential origin. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `SequenceNumeric` = **1**  
  The first and only endorsement: a certificate between Accord members needs no legalisation.
- `Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; as Ferrano Chamber of Commerce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; as Ferrano Chamber of Commerce gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `Party/PostalAddress/ID` = **4160202319527073** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Trazhek Han Zhatrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/StreetName` = **Piazza del Mercato** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. As Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). As Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Chamber of Commerce gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The public body's official name; as Ferrano Chamber of Commerce gives it.
- `Party/PartyLegalEntity/CompanyID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  Number in the Index of Public Administrations of Urvania, which gives every public body a number of its own (xu_ and four lower-case letters or digits), derived from no other register ; as Ferrano Chamber of Commerce gives it. The schemeID names the scheme it is from: the index of public administrations of Urvania (xu_ and four lower-case letters or digits, assigned by the index on the body's accreditation; no real IPA code of Italy's index starts with xu_).
- `Party/Contact/Name` = **Certificates office**  
  The party's certificates office desk: the desk for its role in this document (a certificate); as Ferrano Chamber of Commerce gives it.
- `Party/Contact/JobTitle` = **Certificates officer**  
  The job of the person who answers at the desk; as Ferrano Chamber of Commerce gives it.
- `Party/Contact/Department` = **Certificates**  
  The department the desk belongs to; as Ferrano Chamber of Commerce gives it.
- `Party/Contact/Telephone` = **+999 1 041 714 2503**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Chamber of Commerce gives it.
- `Party/Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Ferrano Chamber of Commerce gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Ferrano Chamber of Commerce gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:xu_m2vd** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; as Ferrano Chamber of Commerce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin. UBL defines this contact as the exporter's signer of the application; the element is mandatory in an endorser party, so it names the endorser's signer.
- `SignatoryContact/JobTitle` = **Certificates officer**  
  The signing function: the officer who signs certificates for the chamber.

### Certificate of Origin Application

Inside `CertificateOfOriginApplication`:

- `ReferenceID` = **6800002165**  
  The exporter's reference for its application.
- `CertificateType` = **Preferential**  
  The goods qualify for the preferential duty rate in Bayvarra; the importer needs this certificate to claim it.
- `ApplicationStatusCode` = **APPROVED** (listID `urn:ubl-examples:world:codelist:ApplicationStatusCode`)  
  The chamber has approved the application. The code is from the Trade Accord's application status list: APPROVED = Approved.
- `OriginalJobID` = **FCC/2026/1722**  
  The job number the chamber's e-certificate system gave the application when it was lodged, by which it tracks amendments; not the buyer's order.
- `Remarks` = **Side frames cast in Urvania from Urvanian ore and slats of Bayvarran hardwood; the casting, finishing and making of the benches in Urvania give origin.**  
  Why the goods are of Urvanian origin.
- `Shipment/ID` = **CAS-SH-26-1291**  
  The shipment the certificate covers.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **3830400** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **5188.8** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `Shipment/GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `Shipment/GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries.
- `Shipment/GoodsItem/Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180** (languageID `en-XU`)  
  The item's name in English, the working language between the countries.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **94017910** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; as Valdara Industries describes the item. The code is from Urvania's national customs tariff list: 94017910 = Benches for parks and gardens, with metal frames.
- `Shipment/GoodsItem/ContainingPackage/Quantity` = **4** (unitCode `EA`)  
  4 benches to a pallet; the goods item travels on 24 pallets.
- `Shipment/GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The pallet goes back to the party that loaded it.
- `Shipment/GoodsItem/ContainingPackage/PackageLevelCode` = **3** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 3: the outer level, the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 3 = Outer.
- `Shipment/GoodsItem/ContainingPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **57000** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **174.6** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Zudrir drir manskan gan drek Serra nanskir, zhukvan stezir gek, vazzhan stan krarhir-trunnir.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `Shipment/GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, ductile cast iron, galvanised and powder-coated.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries.
- `Shipment/GoodsItem/Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting** (languageID `en-XU`)  
  The item's name in English, the working language between the countries.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940199** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940199 = Parts of seats, other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38160** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38160 = Parts of furniture.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **94019990** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; as Valdara Industries describes the item. The code is from Urvania's national customs tariff list: 94019990 = Other parts of seats.
- `Shipment/GoodsItem/ContainingPackage/Quantity` = **12** (unitCode `EA`)  
  12 side frames to a pallet; the goods item travels on 1 pallet.
- `Shipment/GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The pallet goes back to the party that loaded it.
- `Shipment/GoodsItem/ContainingPackage/PackageLevelCode` = **3** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 3: the outer level, the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 3 = Outer.
- `Shipment/GoodsItem/ContainingPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/Quantity` = **1** (unitCode `EA`)  
  One side frame in each carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The carton stays with the frame.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton, one side frame**  
  The carton in words; the goods item's frames travel one to a carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `EndorserParty/RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country, the body Urvania authorises under the Accord to issue proofs of preferential origin. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement: a certificate between Accord members needs no legalisation.
- `EndorserParty/Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin. UBL defines this contact as the exporter's signer of the application; the element is mandatory in an endorser party, so it names the endorser's signer.
- `EndorserParty/SignatoryContact/JobTitle` = **Certificates officer**  
  The signing function: the officer who signs certificates for the chamber.
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
- `SupportingDocumentReference/ID` = **LMW-PO-26-0573**  
  The commercial document behind the goods.
- `SupportingDocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LMW-PO-26-0573 is the example road/01, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.
- `Signature/ID` = **VI-SIG-COA**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC/2026/1722-E1**  
  The identifier of this endorsement: the first of the chamber's job.
- `ApprovalStatus` = **Approved**  
  The chamber has endorsed the certificate.
- `Remarks` = **Origin verified against the exporter's production records.**  
  What the chamber checked.
- `EndorserParty/RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country, the body Urvania authorises under the Accord to issue proofs of preferential origin. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement: a certificate between Accord members needs no legalisation.
- `EndorserParty/Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin. UBL defines this contact as the exporter's signer of the application; the element is mandatory in an endorser party, so it names the endorser's signer.
- `EndorserParty/SignatoryContact/JobTitle` = **Certificates officer**  
  The signing function: the officer who signs certificates for the chamber.
- `Signature/ID` = **FCC-SIG-26-0309**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CertificateOfOrigin xmlns="urn:oasis:names:specification:ubl:schema:xsd:CertificateOfOrigin-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:certificate-of-origin:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900043291</cbc:ProfileExecutionID>
  <cbc:ID>FCC/CO/2026/0090</cbc:ID>
  <cbc:UUID>3152b116-509a-5a0d-8b57-97a8e2b066d0</cbc:UUID>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>08:41:00-01:00</cbc:IssueTime>
  <cbc:Description>Certificate of origin for park benches and castings made in Urvania.</cbc:Description>
  <cbc:Note>Preferential origin under the trade accord.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:Signature>
    <cbc:ID>FCC-SIG-CO-07</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>customs@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
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
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
      </cac:Language>
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
      <cbc:JobTitle>Certificates officer</cbc:JobTitle>
    </cac:SignatoryContact>
  </cac:EndorserParty>
  <cac:CertificateOfOriginApplication>
    <cbc:ReferenceID>6800002165</cbc:ReferenceID>
    <cbc:CertificateType>Preferential</cbc:CertificateType>
    <cbc:ApplicationStatusCode listID="urn:ubl-examples:world:codelist:ApplicationStatusCode">APPROVED</cbc:ApplicationStatusCode>
    <cbc:OriginalJobID>FCC/2026/1722</cbc:OriginalJobID>
    <cbc:Remarks>Side frames cast in Urvania from Urvanian ore and slats of Bayvarran hardwood; the casting, finishing and making of the benches in Urvania give origin.</cbc:Remarks>
    <cac:Shipment>
      <cbc:ID>CAS-SH-26-1291</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Park bench Serra 180</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">3830400</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">5188.8</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">96</cbc:Quantity>
        <cac:Item>
          <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.</cbc:Description>
          <cbc:Description languageID="en-XU">Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.</cbc:Description>
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
        <cac:ContainingPackage>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">3</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
          <cac:ContainedPackage>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
            <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
            <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">790</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">680</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">100</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:ContainedPackage>
          <cac:ContainedPackage>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
            <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
            <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">790</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">680</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">100</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">13</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:ContainedPackage>
          <cac:ContainedPackage>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
            <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
            <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1810</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">295</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">100</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:ContainedPackage>
        </cac:ContainingPackage>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Bench side frame casting</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">57000</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">174.6</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description languageID="qau">Zudrir drir manskan gan drek Serra nanskir, zhukvan stezir gek, vazzhan stan krarhir-trunnir.</cbc:Description>
          <cbc:Description languageID="en-XU">Replacement side frame for the Serra bench, ductile cast iron, galvanised and powder-coated.</cbc:Description>
          <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
          <cbc:Name languageID="en-XU">Bench side frame casting</cbc:Name>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">940199</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38160</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">94019990</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
        <cac:ContainingPackage>
          <cbc:Quantity unitCode="EA">12</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">3</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
          <cac:ContainedPackage>
            <cbc:Quantity unitCode="EA">1</cbc:Quantity>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
            <cbc:PackagingType>Frame carton, one side frame</cbc:PackagingType>
            <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
          </cac:ContainedPackage>
        </cac:ContainingPackage>
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
        <cbc:JobTitle>Certificates officer</cbc:JobTitle>
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
      <cbc:ID>LMW-PO-26-0573</cbc:ID>
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
    <cbc:DocumentID>FCC/2026/1722-E1</cbc:DocumentID>
    <cbc:ApprovalStatus>Approved</cbc:ApprovalStatus>
    <cbc:Remarks>Origin verified against the exporter's production records.</cbc:Remarks>
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
        <cbc:JobTitle>Certificates officer</cbc:JobTitle>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:Signature>
      <cbc:ID>FCC-SIG-26-0309</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:IssuerEndorsement>
</CertificateOfOrigin>
```
