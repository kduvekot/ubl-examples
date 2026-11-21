# Digital Agreement: Lumeway Distribution to Velumi Trading

*Example 3 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Digital Agreement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DIGITAL-AGREEMENT-SCHEMA)*

Before trading, the two parties join the multilateral digital agreement that fixes which UBL processes they use.

[The XML file](03-DigitalAgreement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:digital-agreement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Digital agreement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:onboarding:1.0**  
  The Trade Accord's process profile the document belongs to: onboarding, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **LMW-TX-26-0956**  
  The collaboration this document belongs to: Lumeway's onboarding of Velumi Trading as a new island customer: its business card, the digital agreement they join and the capability statement of the agreement's governor. Lumeway Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **LMW-DAG-26-0048**  
  The agreement's number.
- `UUID` = **1992d68e-5c04-58e5-9789-3ddfb5e9b203**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Signed before the first order.
- `IssueTime` = **12:59:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `AgreementTypeCode` = **MULTILATERAL** (listID `urn:ubl-examples:world:codelist:AgreementTypeCode`)  
  The Trade Accord's multilateral digital agreement, which the Trade Accord Council governs and to which the distributor and the island buyer accede. The code is from the Trade Accord's agreement type list: MULTILATERAL = Multilateral agreement.
- `VersionID` = **1.0**  
  The first version of the agreement.
- `PreviousVersionID` = **0.9**  
  The draft both sides commented on.
- `RequiredResponseMessageLevelCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:ResponseMessageLevelCode`)  
  A business response is required for every document. The code is from the Trade Accord's response message level list: BUSINESS = Business response.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-DA-1**  
  The distributor's signature of its accession; the buyer signs its own accession (what a signature carries waits for the signatures stage).
- `ReasonCode` = **APPROVAL** (listID `urn:ubl-examples:world:codelist:SignatureReasonCode`)  
  The signer approves the document. The code is from the Trade Accord's signature reason list: APPROVAL = Approval.
- `Note` = **Signed with the company's seal certificate.**  
  How.
- `ValidationDate` = **2026-05-05**  
  Verified by the council's validation service before the document was issued, after the terms it binds were verified.
- `ValidationTime` = **12:40:00-01:00**  
  At that time; in the issuer's local time, with its offset from UTC.
- `ValidatorID` = **LTAC-VALIDATOR**  
  The Trade Accord council's validation service.
- `CanonicalizationMethod` = **http://www.w3.org/2006/12/xml-c14n11**  
  Canonical XML 1.1.
- `SignatureMethod` = **http://www.w3.org/2001/04/xmldsig-more#rsa-sha256**  
  RSA with SHA-256.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalSignatureAttachment/EmbeddedDocumentBinaryObject` = **U2lnbmF0dXJlIHZhbHVlIG9mIExELVNJRy0yNi1EQS0xLCBzaG9ydGVuZWQgZm9yIHRoZSBleGFtcGxlIHdvcmxkLg==** (mimeCode `application/pkcs7-signature`)  
  The signature value, Base64-encoded.
- `OriginalDocumentReference/ID` = **LD-DOC-26-DA-1**  
  The document as signed.

### Governor Party

Inside `GovernorParty`:

- `PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Lumeport Trade Accord Council gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Trade Accord Council**  
  The trading name; as Lumeport Trade Accord Council gives it.

### Participant Party

Inside `ParticipantParty`:

- `InitiatingPartyIndicator` = **true**  
  The distributor proposed joining the agreement.
- `PrivatePartyIndicator` = **true**  
  A private company.
- `PublicPartyIndicator` = **false**  
  Not a public body.
- `ServiceProviderPartyIndicator` = **false**  
  It exchanges its own documents; it is not a service provider.
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; as Lumeway Distribution gives it.
- `Party/PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)** (languageID `en-XB`)  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Customer service**  
  The party's main desk, which handles this document; as Lumeway Distribution gives it.
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Party/Contact/Department` = **Customer service**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Party/Contact/Telephone` = **+999 2 7121 955 964**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Party/Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `LegalContact/Name` = **Legal department**  
  For legal notices under the agreement.
- `TechnicalContact/Name` = **Integration desk**  
  For the technical connection.
- `SupportContact/Name` = **Service desk**  
  For day-to-day questions.
- `CommercialContact/Name` = **Sales office**  
  For the trade itself.
- `InitiatingPartyIndicator` = **false**  
  The trader accepted the proposal.
- `PrivatePartyIndicator` = **true**  
  A private company.
- `PublicPartyIndicator` = **false**  
  Not a public body.
- `ServiceProviderPartyIndicator` = **false**  
  It exchanges its own documents; it is not a service provider.
- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `Party/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; as Velumi Trading gives it.
- `Party/PartyLegalEntity/CompanyID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Velumi Trading gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/Contact/Name` = **Purchasing**  
  The party's main desk, which handles this document; as Velumi Trading gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Party/Contact/Telephone` = **+999 3 729 5794**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `Party/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Velumi Trading gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Velumi Trading gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `LegalContact/Name` = **Legal department**  
  For legal notices under the agreement.
- `TechnicalContact/Name` = **Integration desk**  
  For the technical connection.
- `SupportContact/Name` = **Service desk**  
  For day-to-day questions.
- `CommercialContact/Name` = **Purchasing**  
  For the trade itself.

### Agreement Country

Inside `AgreementCountry`:

- `IdentificationCode` = **XU** (listID `ISO 3166`)  
  The agreement applies in the Trade Accord's member countries: Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `IdentificationCode` = **XB** (listID `ISO 3166`)  
  The agreement applies in the Trade Accord's member countries: Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `IdentificationCode` = **XL** (listID `ISO 3166`)  
  The agreement applies in the Trade Accord's member countries: Lisavu. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Required Certification Document Reference

Inside `RequiredCertificationDocumentReference`:

- `ID` = **LTAC-AP-REQ-2.0**  
  The certification the participants' access points must hold, by the Trade Accord Council's requirements.
- `UUID` = **dc787c2a-3f1a-547c-a3f0-172d3721bfb5**  
  Its UUID.
- `IssueDate` = **2026-01-02**  
  The council published version 2.0 at the start of the year.
- `IssueTime` = **12:00:00-01:00**  
  And time; in the issuer's local time, with its offset from UTC.
- `DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document. The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `ReferencedDocumentInternalAddress` = **section-2**  
  The section of the referenced document meant: the requirements for a participant's own access point.
- `LanguageID` = **en**  
  In English.
- `LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  Written in Bayvarran English, by the council in Lumeport. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `VersionID` = **2.0**  
  The version referred to.
- `DocumentStatusCode` = **Confirmed** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  The version in force. The code is from the world's copy of UBL's Document status list, with a listID: Confirmed = Document has been confirmed.
- `DocumentDescription` = **The Trade Accord Council's requirements for the certification of access points on the Trade Accord's network.**  
  What it is.
- `Attachment/ExternalReference/URI` = **https://www.tradeaccord.example/network/ap-requirements-2.0.pdf**  
  The full text, on the council's site.
- `Attachment/ExternalReference/DocumentHash` = **9f2c4e1ab37d5c8e0f6a2b4d8c1e3f5a7b9d0c2e4f6a8b1c3d5e7f9a0b2c4d6e**  
  The SHA-256 hash of the full text, to check it is unchanged.
- `Attachment/ExternalReference/HashAlgorithmMethod` = **http://www.w3.org/2001/04/xmlenc#sha256**  
  SHA-256.
- `Attachment/ExternalReference/ExpiryDate` = **2027-05-05**  
  The link works as long as the reference is valid.
- `Attachment/ExternalReference/ExpiryTime` = **23:59:00-01:00**  
  Until the end of that day; in the issuer's local time, with its offset from UTC.
- `Attachment/ExternalReference/MimeCode` = **application/pdf** (listID `IANA Media Types`)  
  A PDF. The code is from UBL's default Media type (IANA) list: application/pdf.
- `Attachment/ExternalReference/FormatCode` = **fmt/480** (listID `PRONOM`)  
  An archivable PDF. The code is from the world's copy of PRONOM file format registry (PUIDs): fmt/480 = Acrobat PDF/A - Portable Document Format, version 3b.
- `Attachment/ExternalReference/EncodingCode` = **binary** (listID `RFC 2045 Content-Transfer-Encoding`)  
  Not encoded. The code is from the world's copy of RFC 2045 Content-Transfer-Encoding: binary.
- `Attachment/ExternalReference/FileName` = **ap-requirements-2.0.pdf**  
  The file's name.
- `Attachment/ExternalReference/Description` = **The full requirements.**  
  What it holds.
- `ValidityPeriod/StartDate` = **2026-05-05**  
  In force from signing.
- `ValidityPeriod/EndDate` = **2027-05-05**  
  For a year.
- `ResultOfVerification/ValidatorID` = **LTAC-VALIDATOR**  
  The council's validation service.
- `ResultOfVerification/ValidationResultCode` = **VALID** (listID `urn:ubl-examples:world:codelist:ValidationResultCode`)  
  The document's signature is valid. The code is from the Trade Accord's validation result list: VALID = Valid.
- `ResultOfVerification/ValidationDate` = **2026-05-05**  
  Checked.
- `ResultOfVerification/ValidationTime` = **12:05:00-01:00**  
  At that time; in the issuer's local time, with its offset from UTC.
- `ResultOfVerification/ValidateProcess` = **Signature and hash check**  
  What was checked.
- `ResultOfVerification/ValidateTool` = **Accord validator**  
  The tool.
- `ResultOfVerification/ValidateToolVersion` = **3.2**  
  Its version.
- `ResultOfVerification/SignatoryParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ResultOfVerification/SignatoryParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.

### Digital Agreement Terms

Inside `DigitalAgreementTerms`:

- `Description` = **The terms of the Trade Accord's multilateral digital agreement, version 1.0, published by the Trade Accord Council: documents are exchanged over the Trade Accord's network.**  
  The terms: the Accord's own, which the participants accept by acceding, not the distributor's.
- `ValidityPeriod/StartDate` = **2026-05-05**  
  From signing.
- `ValidityPeriod/EndDate` = **2027-05-05**  
  For a year.
- `AdoptionPeriod/StartDate` = **2026-05-05**  
  The buyer adopts it
- `AdoptionPeriod/EndDate` = **2026-05-19**  
  within two weeks.
- `ServiceLevelAgreement/ID` = **LMW-SLA-1**  
  The service level.
- `ServiceLevelAgreement/ServiceTypeCode` = **MESSAGING** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  For the exchange. The code is from the Trade Accord's service type list: MESSAGING = Messaging service.
- `ServiceLevelAgreement/ServiceType` = **Document exchange**  
  In words.
- `ServiceLevelAgreement/AvailabilityTimePercent` = **99.5**  
  The access point is available 99.5 % of the time.
- `ServiceLevelAgreement/MondayAvailabilityIndicator` = **true**  
  Supported on Mondays.
- `ServiceLevelAgreement/TuesdayAvailabilityIndicator` = **true**  
  Supported on Tuesdays.
- `ServiceLevelAgreement/WednesdayAvailabilityIndicator` = **true**  
  Supported on Wednesdays.
- `ServiceLevelAgreement/ThursdayAvailabilityIndicator` = **true**  
  Supported on Thursdays.
- `ServiceLevelAgreement/FridayAvailabilityIndicator` = **true**  
  Supported on Fridays.
- `ServiceLevelAgreement/SaturdayAvailabilityIndicator` = **false**  
  No support on Saturdays.
- `ServiceLevelAgreement/SundayAvailabilityIndicator` = **false**  
  No support on Sundays.
- `ServiceLevelAgreement/MinimumResponseTimeDurationMeasure` = **4** (unitCode `HUR`)  
  An answer to a problem within four hours.
- `ServiceLevelAgreement/MinimumDownTimeScheduleDurationMeasure` = **48** (unitCode `HUR`)  
  Planned downtime announced 48 hours ahead.
- `ServiceLevelAgreement/MaximumIncidentNotificationDurationMeasure` = **1** (unitCode `HUR`)  
  An incident reported within an hour.
- `ServiceLevelAgreement/MaximumDataLossDurationMeasure` = **0** (unitCode `HUR`)  
  No document may be lost.
- `ServiceLevelAgreement/MeanTimeToRecoverDurationMeasure` = **2** (unitCode `HUR`)  
  Back in two hours on average.
- `ServiceLevelAgreement/ServiceAvailabilityPeriod/StartTime` = **07:00:00-01:00**  
  Support from seven; in the issuer's local time, with its offset from UTC.
- `ServiceLevelAgreement/ServiceAvailabilityPeriod/EndTime` = **19:00:00-01:00**  
  Until seven; in the issuer's local time, with its offset from UTC.
- `ServiceLevelAgreement/ServiceMaintenancePeriod/StartTime` = **02:00:00-01:00**  
  Maintenance at night; in the issuer's local time, with its offset from UTC.
- `ServiceLevelAgreement/ServiceMaintenancePeriod/EndTime` = **04:00:00-01:00**  
  Until four; in the issuer's local time, with its offset from UTC.

### Digital Process

Inside `DigitalProcess`:

- `ID` = **ordering**  
  A process the parties agree to exchange electronically.
- `Description` = **Order, order response and order change.**  
  What the process covers.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the agreement covers.
- `DigitalCollaboration/ID` = **ordering-1**  
  The main exchange of the process.
- `DigitalCollaboration/SendingDigitalService/ID` = **VT-Order-OUT**  
  The party's service for this document.
- `DigitalCollaboration/SendingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/ID` = **Order**  
  The document type.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd**  
  The schema.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: Order.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-41859**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.velumi.example/as4**  
  The access point, under the party's own domain.
- `DigitalCollaboration/SendingDigitalService/CertificationDocumentReference/ID` = **LTAC-CERT-26-017**  
  The Trade Accord council's certificate that the distributor's system passed the conformance test.
- `DigitalCollaboration/ReceivingDigitalService/ID` = **LMW-Order-IN**  
  The party's service for this document.
- `DigitalCollaboration/ReceivingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/ID` = **Order**  
  The document type.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd**  
  The schema.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: Order.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-20410274**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.lumeway.example/as4**  
  The access point, under the party's own domain.
- `DigitalCollaboration/ID` = **ordering-2**  
  An exchange of the process: the main one first, then the other way.
- `DigitalCollaboration/SendingDigitalService/ID` = **LMW-OrderResponse-OUT**  
  The party's service for this document.
- `DigitalCollaboration/SendingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:order-response:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/ID` = **OrderResponse**  
  The document type.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-OrderResponse-2.5.xsd**  
  The schema.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **OrderResponse** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: OrderResponse = Order Response.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-20410274**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.lumeway.example/as4**  
  The access point, under the party's own domain.
- `DigitalCollaboration/SendingDigitalService/CertificationDocumentReference/ID` = **LTAC-CERT-26-017**  
  The Trade Accord council's certificate that the distributor's system passed the conformance test.
- `DigitalCollaboration/ReceivingDigitalService/ID` = **VT-OrderResponse-IN**  
  The party's service for this document.
- `DigitalCollaboration/ReceivingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:order-response:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/ID` = **OrderResponse**  
  The document type.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-OrderResponse-2.5.xsd**  
  The schema.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **OrderResponse** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: OrderResponse = Order Response.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-41859**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.velumi.example/as4**  
  The access point, under the party's own domain.
- `CertificationDocumentReference/ID` = **ACCORD-CERT-PROC-ordering**  
  The council's certification of the process.
- `ID` = **billing**  
  A process the parties agree to exchange electronically.
- `Description` = **Invoice and credit note from the distributor, its invoice status request and the buyer's response: the billing between the two participants; the factor's statement and the remittance to the factor are no part of it.**  
  What the process covers.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the agreement covers.
- `DigitalCollaboration/ID` = **billing-1**  
  The main exchange of the process.
- `DigitalCollaboration/SendingDigitalService/ID` = **LMW-Invoice-OUT**  
  The party's service for this document.
- `DigitalCollaboration/SendingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/ID` = **Invoice**  
  The document type.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd**  
  The schema.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: Invoice.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-20410274**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.lumeway.example/as4**  
  The access point, under the party's own domain.
- `DigitalCollaboration/SendingDigitalService/CertificationDocumentReference/ID` = **LTAC-CERT-26-017**  
  The Trade Accord council's certificate that the distributor's system passed the conformance test.
- `DigitalCollaboration/ReceivingDigitalService/ID` = **VT-Invoice-IN**  
  The party's service for this document.
- `DigitalCollaboration/ReceivingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/ID` = **Invoice**  
  The document type.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd**  
  The schema.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: Invoice.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-41859**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.velumi.example/as4**  
  The access point, under the party's own domain.
- `DigitalCollaboration/ID` = **billing-2**  
  An exchange of the process: the main one first, then the other way.
- `DigitalCollaboration/SendingDigitalService/ID` = **VT-InvoiceStatusResponse-OUT**  
  The party's service for this document.
- `DigitalCollaboration/SendingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:invoice-status:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/ID` = **InvoiceStatusResponse**  
  The document type.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-InvoiceStatusResponse-2.5.xsd**  
  The schema.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **InvoiceStatusResponse** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: InvoiceStatusResponse = Invoice Status Response.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-41859**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.velumi.example/as4**  
  The access point, under the party's own domain.
- `DigitalCollaboration/SendingDigitalService/CertificationDocumentReference/ID` = **LTAC-CERT-26-017**  
  The Trade Accord council's certificate that the distributor's system passed the conformance test.
- `DigitalCollaboration/ReceivingDigitalService/ID` = **LMW-InvoiceStatusResponse-IN**  
  The party's service for this document.
- `DigitalCollaboration/ReceivingDigitalService/CustomizationID` = **urn:ubl-examples:world:trns:invoice-status:1.0**  
  The specification the documents of this service follow: the CustomizationID those documents carry in this flow.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/ID` = **InvoiceStatusResponse**  
  The document type.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-InvoiceStatusResponse-2.5.xsd**  
  The schema.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **InvoiceStatusResponse** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's UBL document type list: InvoiceStatusResponse = Invoice Status Response.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The Trade Accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in the register it is entered in: its country's companies register, for a public body its country's register of public bodies, for a grower Lisavu's farm register).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-20410274**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.lumeway.example/as4**  
  The access point, under the party's own domain.
- `CertificationDocumentReference/ID` = **ACCORD-CERT-PROC-billing**  
  The council's certification of the process.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DigitalAgreement xmlns="urn:oasis:names:specification:ubl:schema:xsd:DigitalAgreement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:digital-agreement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:onboarding:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LMW-TX-26-0956</cbc:ProfileExecutionID>
  <cbc:ID>LMW-DAG-26-0048</cbc:ID>
  <cbc:UUID>1992d68e-5c04-58e5-9789-3ddfb5e9b203</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>12:59:00-01:00</cbc:IssueTime>
  <cbc:AgreementTypeCode listID="urn:ubl-examples:world:codelist:AgreementTypeCode">MULTILATERAL</cbc:AgreementTypeCode>
  <cbc:VersionID>1.0</cbc:VersionID>
  <cbc:PreviousVersionID>0.9</cbc:PreviousVersionID>
  <cbc:RequiredResponseMessageLevelCode listID="urn:ubl-examples:world:codelist:ResponseMessageLevelCode">BUSINESS</cbc:RequiredResponseMessageLevelCode>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-DA-1</cbc:ID>
    <cbc:ReasonCode listID="urn:ubl-examples:world:codelist:SignatureReasonCode">APPROVAL</cbc:ReasonCode>
    <cbc:Note>Signed with the company's seal certificate.</cbc:Note>
    <cbc:ValidationDate>2026-05-05</cbc:ValidationDate>
    <cbc:ValidationTime>12:40:00-01:00</cbc:ValidationTime>
    <cbc:ValidatorID>LTAC-VALIDATOR</cbc:ValidatorID>
    <cbc:CanonicalizationMethod>http://www.w3.org/2006/12/xml-c14n11</cbc:CanonicalizationMethod>
    <cbc:SignatureMethod>http://www.w3.org/2001/04/xmldsig-more#rsa-sha256</cbc:SignatureMethod>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
    <cac:DigitalSignatureAttachment>
      <cbc:EmbeddedDocumentBinaryObject mimeCode="application/pkcs7-signature">U2lnbmF0dXJlIHZhbHVlIG9mIExELVNJRy0yNi1EQS0xLCBzaG9ydGVuZWQgZm9yIHRoZSBleGFtcGxlIHdvcmxkLg==</cbc:EmbeddedDocumentBinaryObject>
    </cac:DigitalSignatureAttachment>
    <cac:OriginalDocumentReference>
      <cbc:ID>LD-DOC-26-DA-1</cbc:ID>
    </cac:OriginalDocumentReference>
  </cac:Signature>
  <cac:GovernorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
    </cac:PartyName>
  </cac:GovernorParty>
  <cac:ParticipantParty>
    <cbc:InitiatingPartyIndicator>true</cbc:InitiatingPartyIndicator>
    <cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
    <cbc:PublicPartyIndicator>false</cbc:PublicPartyIndicator>
    <cbc:ServiceProviderPartyIndicator>false</cbc:ServiceProviderPartyIndicator>
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
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="en-XB">Limited company (private)</cbc:CompanyLegalForm>
        <cac:RegistrationAddress>
          <cbc:CityName>Marrowdale</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Customer service</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Customer service</cbc:Department>
        <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
        <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
    <cac:LegalContact>
      <cbc:Name>Legal department</cbc:Name>
    </cac:LegalContact>
    <cac:TechnicalContact>
      <cbc:Name>Integration desk</cbc:Name>
    </cac:TechnicalContact>
    <cac:SupportContact>
      <cbc:Name>Service desk</cbc:Name>
    </cac:SupportContact>
    <cac:CommercialContact>
      <cbc:Name>Sales office</cbc:Name>
    </cac:CommercialContact>
  </cac:ParticipantParty>
  <cac:ParticipantParty>
    <cbc:InitiatingPartyIndicator>false</cbc:InitiatingPartyIndicator>
    <cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
    <cbc:PublicPartyIndicator>false</cbc:PublicPartyIndicator>
    <cbc:ServiceProviderPartyIndicator>false</cbc:ServiceProviderPartyIndicator>
    <cac:Party>
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
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
        <cac:RegistrationAddress>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
    <cac:LegalContact>
      <cbc:Name>Legal department</cbc:Name>
    </cac:LegalContact>
    <cac:TechnicalContact>
      <cbc:Name>Integration desk</cbc:Name>
    </cac:TechnicalContact>
    <cac:SupportContact>
      <cbc:Name>Service desk</cbc:Name>
    </cac:SupportContact>
    <cac:CommercialContact>
      <cbc:Name>Purchasing</cbc:Name>
    </cac:CommercialContact>
  </cac:ParticipantParty>
  <cac:AgreementCountry>
    <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
  </cac:AgreementCountry>
  <cac:AgreementCountry>
    <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
  </cac:AgreementCountry>
  <cac:AgreementCountry>
    <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
  </cac:AgreementCountry>
  <cac:RequiredCertificationDocumentReference>
    <cbc:ID>LTAC-AP-REQ-2.0</cbc:ID>
    <cbc:UUID>dc787c2a-3f1a-547c-a3f0-172d3721bfb5</cbc:UUID>
    <cbc:IssueDate>2026-01-02</cbc:IssueDate>
    <cbc:IssueTime>12:00:00-01:00</cbc:IssueTime>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
    <cbc:ReferencedDocumentInternalAddress>section-2</cbc:ReferencedDocumentInternalAddress>
    <cbc:LanguageID>en</cbc:LanguageID>
    <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    <cbc:VersionID>2.0</cbc:VersionID>
    <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">Confirmed</cbc:DocumentStatusCode>
    <cbc:DocumentDescription>The Trade Accord Council's requirements for the certification of access points on the Trade Accord's network.</cbc:DocumentDescription>
    <cac:Attachment>
      <cac:ExternalReference>
        <cbc:URI>https://www.tradeaccord.example/network/ap-requirements-2.0.pdf</cbc:URI>
        <cbc:DocumentHash>9f2c4e1ab37d5c8e0f6a2b4d8c1e3f5a7b9d0c2e4f6a8b1c3d5e7f9a0b2c4d6e</cbc:DocumentHash>
        <cbc:HashAlgorithmMethod>http://www.w3.org/2001/04/xmlenc#sha256</cbc:HashAlgorithmMethod>
        <cbc:ExpiryDate>2027-05-05</cbc:ExpiryDate>
        <cbc:ExpiryTime>23:59:00-01:00</cbc:ExpiryTime>
        <cbc:MimeCode listID="IANA Media Types">application/pdf</cbc:MimeCode>
        <cbc:FormatCode listID="PRONOM">fmt/480</cbc:FormatCode>
        <cbc:EncodingCode listID="RFC 2045 Content-Transfer-Encoding">binary</cbc:EncodingCode>
        <cbc:FileName>ap-requirements-2.0.pdf</cbc:FileName>
        <cbc:Description>The full requirements.</cbc:Description>
      </cac:ExternalReference>
    </cac:Attachment>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-05-05</cbc:StartDate>
      <cbc:EndDate>2027-05-05</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:ResultOfVerification>
      <cbc:ValidatorID>LTAC-VALIDATOR</cbc:ValidatorID>
      <cbc:ValidationResultCode listID="urn:ubl-examples:world:codelist:ValidationResultCode">VALID</cbc:ValidationResultCode>
      <cbc:ValidationDate>2026-05-05</cbc:ValidationDate>
      <cbc:ValidationTime>12:05:00-01:00</cbc:ValidationTime>
      <cbc:ValidateProcess>Signature and hash check</cbc:ValidateProcess>
      <cbc:ValidateTool>Accord validator</cbc:ValidateTool>
      <cbc:ValidateToolVersion>3.2</cbc:ValidateToolVersion>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:ResultOfVerification>
  </cac:RequiredCertificationDocumentReference>
  <cac:DigitalAgreementTerms>
    <cbc:Description>The terms of the Trade Accord's multilateral digital agreement, version 1.0, published by the Trade Accord Council: documents are exchanged over the Trade Accord's network.</cbc:Description>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-05-05</cbc:StartDate>
      <cbc:EndDate>2027-05-05</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:AdoptionPeriod>
      <cbc:StartDate>2026-05-05</cbc:StartDate>
      <cbc:EndDate>2026-05-19</cbc:EndDate>
    </cac:AdoptionPeriod>
    <cac:ServiceLevelAgreement>
      <cbc:ID>LMW-SLA-1</cbc:ID>
      <cbc:ServiceTypeCode listID="urn:ubl-examples:world:codelist:ServiceTypeCode">MESSAGING</cbc:ServiceTypeCode>
      <cbc:ServiceType>Document exchange</cbc:ServiceType>
      <cbc:AvailabilityTimePercent>99.5</cbc:AvailabilityTimePercent>
      <cbc:MondayAvailabilityIndicator>true</cbc:MondayAvailabilityIndicator>
      <cbc:TuesdayAvailabilityIndicator>true</cbc:TuesdayAvailabilityIndicator>
      <cbc:WednesdayAvailabilityIndicator>true</cbc:WednesdayAvailabilityIndicator>
      <cbc:ThursdayAvailabilityIndicator>true</cbc:ThursdayAvailabilityIndicator>
      <cbc:FridayAvailabilityIndicator>true</cbc:FridayAvailabilityIndicator>
      <cbc:SaturdayAvailabilityIndicator>false</cbc:SaturdayAvailabilityIndicator>
      <cbc:SundayAvailabilityIndicator>false</cbc:SundayAvailabilityIndicator>
      <cbc:MinimumResponseTimeDurationMeasure unitCode="HUR">4</cbc:MinimumResponseTimeDurationMeasure>
      <cbc:MinimumDownTimeScheduleDurationMeasure unitCode="HUR">48</cbc:MinimumDownTimeScheduleDurationMeasure>
      <cbc:MaximumIncidentNotificationDurationMeasure unitCode="HUR">1</cbc:MaximumIncidentNotificationDurationMeasure>
      <cbc:MaximumDataLossDurationMeasure unitCode="HUR">0</cbc:MaximumDataLossDurationMeasure>
      <cbc:MeanTimeToRecoverDurationMeasure unitCode="HUR">2</cbc:MeanTimeToRecoverDurationMeasure>
      <cac:ServiceAvailabilityPeriod>
        <cbc:StartTime>07:00:00-01:00</cbc:StartTime>
        <cbc:EndTime>19:00:00-01:00</cbc:EndTime>
      </cac:ServiceAvailabilityPeriod>
      <cac:ServiceMaintenancePeriod>
        <cbc:StartTime>02:00:00-01:00</cbc:StartTime>
        <cbc:EndTime>04:00:00-01:00</cbc:EndTime>
      </cac:ServiceMaintenancePeriod>
    </cac:ServiceLevelAgreement>
  </cac:DigitalAgreementTerms>
  <cac:DigitalProcess>
    <cbc:ID>ordering</cbc:ID>
    <cbc:Description>Order, order response and order change.</cbc:Description>
    <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
    <cac:DigitalCollaboration>
      <cbc:ID>ordering-1</cbc:ID>
      <cac:SendingDigitalService>
        <cbc:ID>VT-Order-OUT</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Order</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-41859</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.velumi.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
        <cac:CertificationDocumentReference>
          <cbc:ID>LTAC-CERT-26-017</cbc:ID>
        </cac:CertificationDocumentReference>
      </cac:SendingDigitalService>
      <cac:ReceivingDigitalService>
        <cbc:ID>LMW-Order-IN</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Order</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-20410274</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.lumeway.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
      </cac:ReceivingDigitalService>
    </cac:DigitalCollaboration>
    <cac:DigitalCollaboration>
      <cbc:ID>ordering-2</cbc:ID>
      <cac:SendingDigitalService>
        <cbc:ID>LMW-OrderResponse-OUT</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:order-response:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>OrderResponse</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-OrderResponse-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">OrderResponse</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-20410274</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.lumeway.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
        <cac:CertificationDocumentReference>
          <cbc:ID>LTAC-CERT-26-017</cbc:ID>
        </cac:CertificationDocumentReference>
      </cac:SendingDigitalService>
      <cac:ReceivingDigitalService>
        <cbc:ID>VT-OrderResponse-IN</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:order-response:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>OrderResponse</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-OrderResponse-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">OrderResponse</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-41859</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.velumi.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
      </cac:ReceivingDigitalService>
    </cac:DigitalCollaboration>
    <cac:CertificationDocumentReference>
      <cbc:ID>ACCORD-CERT-PROC-ordering</cbc:ID>
    </cac:CertificationDocumentReference>
  </cac:DigitalProcess>
  <cac:DigitalProcess>
    <cbc:ID>billing</cbc:ID>
    <cbc:Description>Invoice and credit note from the distributor, its invoice status request and the buyer's response: the billing between the two participants; the factor's statement and the remittance to the factor are no part of it.</cbc:Description>
    <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
    <cac:DigitalCollaboration>
      <cbc:ID>billing-1</cbc:ID>
      <cac:SendingDigitalService>
        <cbc:ID>LMW-Invoice-OUT</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Invoice</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-20410274</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.lumeway.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
        <cac:CertificationDocumentReference>
          <cbc:ID>LTAC-CERT-26-017</cbc:ID>
        </cac:CertificationDocumentReference>
      </cac:SendingDigitalService>
      <cac:ReceivingDigitalService>
        <cbc:ID>VT-Invoice-IN</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Invoice</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-41859</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.velumi.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
      </cac:ReceivingDigitalService>
    </cac:DigitalCollaboration>
    <cac:DigitalCollaboration>
      <cbc:ID>billing-2</cbc:ID>
      <cac:SendingDigitalService>
        <cbc:ID>VT-InvoiceStatusResponse-OUT</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:invoice-status:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>InvoiceStatusResponse</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-InvoiceStatusResponse-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">InvoiceStatusResponse</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-41859</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.velumi.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
        <cac:CertificationDocumentReference>
          <cbc:ID>LTAC-CERT-26-017</cbc:ID>
        </cac:CertificationDocumentReference>
      </cac:SendingDigitalService>
      <cac:ReceivingDigitalService>
        <cbc:ID>LMW-InvoiceStatusResponse-IN</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world:trns:invoice-status:1.0</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>InvoiceStatusResponse</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-InvoiceStatusResponse-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">InvoiceStatusResponse</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-20410274</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.lumeway.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
      </cac:ReceivingDigitalService>
    </cac:DigitalCollaboration>
    <cac:CertificationDocumentReference>
      <cbc:ID>ACCORD-CERT-PROC-billing</cbc:ID>
    </cac:CertificationDocumentReference>
  </cac:DigitalProcess>
</DigitalAgreement>
```
