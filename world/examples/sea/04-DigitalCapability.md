# Digital Capability: Lumeport Trade Accord Council to Velumi Trading

*Example 4 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Digital Capability in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DIGITAL-CAPABILITY-SCHEMA)*

The agreement's governor tells the buyer which documents the distributor can send and receive.

[The XML file](04-DigitalCapability.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:digital-capability:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Digital capability". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:onboarding:1.0**  
  The Trade Accord's process profile the document belongs to: onboarding, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **LMW-TX-26-0956**  
  The collaboration this document belongs to: Lumeway's onboarding of Velumi Trading as a new island customer: its business card, the digital agreement they join and the capability statement of the agreement's governor. Lumeway Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **LTAC/2026/0205**  
  The governor's number.
- `UUID` = **5754c138-ef9f-5b93-ae9f-9a48fe182097**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Sent when the buyer joins the agreement.
- `IssueTime` = **09:44:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `VersionID` = **1.0**  
  The first statement of capability.
- `PreviousVersionID` = **0.9**  
  The draft.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-DC**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; as Lumeport Trade Accord Council gives it. The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 9411 = Activities of business and employers membership organizations.
- `PartyIdentification/ID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Lumeport Trade Accord Council gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Trade Accord Council**  
  The trading name; as Lumeport Trade Accord Council gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-268189** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Trade Accord Council gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Exchange Street**  
  Street of the postal address. As Lumeport Trade Accord Council gives it.
- `PostalAddress/BuildingNumber` = **34**  
  Building number of the postal address. As Lumeport Trade Accord Council gives it.
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Trade Accord Council gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Trade Accord Council gives it.
- `PostalAddress/PostalZone` = **38521**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Trade Accord Council gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Trade Accord Council gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Lumeport Trade Accord Council**  
  The public body's official name; as Lumeport Trade Accord Council gives it.
- `PartyLegalEntity/CompanyID` = **8423019675** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register ; as Lumeport Trade Accord Council gives it. The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FLPB**  
  The identifier of the register in the world.
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal list of public bodies of Bayvarra**  
  The register the public body is entered in, kept by the Bayvarra Information Service: a public body is set up by law and is in no register of businesses.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **PUBLIC** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of public bodies, not a register of businesses. The code is from the Trade Accord's corporate registration type list: PUBLIC = Register of public bodies.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Secretariat**  
  The party's main desk, which handles this document; as Lumeport Trade Accord Council gives it.
- `Contact/JobTitle` = **Secretariat officer**  
  The job of the person who answers at the desk; as Lumeport Trade Accord Council gives it.
- `Contact/Department` = **Secretariat**  
  The department the desk belongs to; as Lumeport Trade Accord Council gives it.
- `Contact/Telephone` = **+999 2 38 3068 3960**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Lumeport Trade Accord Council gives it.
- `Contact/ElectronicMail` = **secretariat@tradeaccord.example**  
  The contact's e-mail address; as Lumeport Trade Accord Council gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Trade Accord Council gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:8423019675** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Lumeport Trade Accord Council gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Business Party

Inside `BusinessParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website; as Lumeway Distribution gives it.
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; as Lumeway Distribution gives it. The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; as Lumeway Distribution gives it.
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; as Lumeway Distribution gives it.
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)** (languageID `en-XB`)  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **MEDIUM** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 78 persons and its turnover of 33900000.00 XBL in 2025, by the Trade Accord's limits; as Lumeway Distribution gives it. The code is from the Trade Accord's entity size list: MEDIUM = Medium-sized enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Customer service**  
  The party's main desk, which handles this document; as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 5121 955 964**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  The contact's e-mail address; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Digital Process

Inside `DigitalProcess`:

- `ID` = **ordering**  
  A process the distributor supports.
- `Description` = **Receives orders and order changes, sends order responses.**  
  What it covers.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile, as in the agreement.
- `DigitalCollaboration/ID` = **ordering-1**  
  The exchange as the agreement numbers it.
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
  The exchange as the agreement numbers it.
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
- `ID` = **billing**  
  A process the distributor supports.
- `Description` = **Sends invoices, credit notes and invoice status requests, receives the status responses.**  
  What it covers.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile, as in the agreement.
- `DigitalCollaboration/ID` = **billing-1**  
  The exchange as the agreement numbers it.
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
- `DigitalCollaboration/ID` = **billing-2**  
  The exchange as the agreement numbers it.
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

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DigitalCapability xmlns="urn:oasis:names:specification:ubl:schema:xsd:DigitalCapability-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:digital-capability:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:onboarding:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LMW-TX-26-0956</cbc:ProfileExecutionID>
  <cbc:ID>LTAC/2026/0205</cbc:ID>
  <cbc:UUID>5754c138-ef9f-5b93-ae9f-9a48fe182097</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>09:44:00-01:00</cbc:IssueTime>
  <cbc:VersionID>1.0</cbc:VersionID>
  <cbc:PreviousVersionID>0.9</cbc:PreviousVersionID>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-DC</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-268189</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Exchange Street</cbc:StreetName>
      <cbc:BuildingNumber>34</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38521</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeport Trade Accord Council</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">8423019675</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FLPB</cbc:ID>
        <cbc:Name>Federal list of public bodies of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">PUBLIC</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Secretariat</cbc:Name>
      <cbc:JobTitle>Secretariat officer</cbc:JobTitle>
      <cbc:Department>Secretariat</cbc:Department>
      <cbc:Telephone>+999 2 38 3068 3960</cbc:Telephone>
      <cbc:ElectronicMail>secretariat@tradeaccord.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:8423019675</cbc:ElectronicAddressID>
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
  </cac:ReceiverParty>
  <cac:BusinessParty>
    <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
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
      <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="en-XB">Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">MEDIUM</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
      <cbc:Telephone>+999 2 5121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:BusinessParty>
  <cac:DigitalProcess>
    <cbc:ID>ordering</cbc:ID>
    <cbc:Description>Receives orders and order changes, sends order responses.</cbc:Description>
    <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
    <cac:DigitalCollaboration>
      <cbc:ID>ordering-1</cbc:ID>
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
      </cac:SendingDigitalService>
    </cac:DigitalCollaboration>
  </cac:DigitalProcess>
  <cac:DigitalProcess>
    <cbc:ID>billing</cbc:ID>
    <cbc:Description>Sends invoices, credit notes and invoice status requests, receives the status responses.</cbc:Description>
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
      </cac:SendingDigitalService>
    </cac:DigitalCollaboration>
    <cac:DigitalCollaboration>
      <cbc:ID>billing-2</cbc:ID>
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
  </cac:DigitalProcess>
</DigitalCapability>
```
