# Business Card: Lumeway Distribution to Velumi Trading

*Example 1 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Business Card in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-BUSINESS-CARD-SCHEMA)*

The distributor introduces itself to the new island customer.

[The XML file](01-BusinessCard.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:business-card:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Business card". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:onboarding:1.0**  
  The Trade Accord's process profile the document belongs to: onboarding, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **LMW-TX-26-0956**  
  The collaboration this document belongs to: Lumeway's onboarding of Velumi Trading as a new island customer: its business card, the digital agreement they join and the capability statement of the agreement's governor. Lumeway Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **LMW-BC-26-0048**  
  The sender's number for this document.
- `UUID` = **da594e74-bfa8-5df5-ab8d-930b60c73ea9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Sent before the first offer to the new customer, on Tuesday 5 May, after Bayvarra's Labour Day.
- `IssueTime` = **16:39:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `VersionID` = **2**  
  The card as updated this year.
- `PreviousVersionID` = **1**  
  Last year's card.
- `BriefDescription` = **Distributor of street and garden furniture for Bayvarra and the islands, with a weekly sailing to Selanu (Port Wrenfield in the island's address register).**  
  The business in a sentence. The town is Selanu in running text, also in English; Port Wrenfield is its official English name, which addresses carry.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-BC**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

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
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.

### Business Party

Inside `BusinessParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); as Lumeway Distribution gives it.
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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
- `Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **sales@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Brochure Document Reference

Inside `BrochureDocumentReference`:

- `ID` = **LMW-BROCHURE-2026**  
  The distributor's brochure.
- `Attachment/ExternalReference/URI` = **https://www.lumeway.example/brochure-2026.pdf**  
  Where it is.
- `Attachment/ExternalReference/MimeCode` = **application/pdf** (listID `IANA Media Types`)  
  A PDF. The code is from UBL's default Media type (IANA) list: application/pdf.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **LMW-REG-XB**  
  The distributor's registration extract.
- `DocumentTypeCode` = **101** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, Lumeway's extract from Bayvarra's business register, a document outside the examples (cited). The code is from the world's copy of UN/EDIFACT 1001 Document name: 101 = Registration document.

### Business Capability

Inside `BusinessCapability`:

- `ID` = **CAP-STOCK**  
  A capability.
- `CapabilityTypeCode` = **WAREHOUSING** (listID `urn:ubl-examples:world:codelist:BusinessCapabilityTypeCode`)  
  What it can do. The code is from the Trade Accord's business capability type list: WAREHOUSING = Warehousing.
- `Description` = **Stock of 264 park benches in Marrowdale, as counted on 30 April.**  
  In words: the benches for sale in Lumeway's warehouse at its month-end count, from the March road lot and the April rail lots (the goods chain's ledger).
- `ValueAmount` = **105336.00** (currencyID `XBL`)  
  The stock's value at cost, 399.00 lume a bench, the price Lumeway paid Valdara.
- `ValueQuantity` = **264** (unitCode `EA`)  
  Benches in stock, for sale.
- `SuppliedEvidence/ID` = **LMW-COUNT-26-04**  
  The evidence.
- `SuppliedEvidence/EvidenceTypeCode` = **STOCKCOUNT** (listID `urn:ubl-examples:world:codelist:EvidenceTypeCode`)  
  Lumeway's own count of its stock, not an audit. The code is from the Trade Accord's evidence type list: STOCKCOUNT = Stock count.
- `SuppliedEvidence/Name` = **Stock count of 30 April 2026**  
  Its name.
- `SuppliedEvidence/Description` = **The distributor's own count of its warehouse at the end of April; it counts its stock at the end of every month.**  
  What it is, and how often it is made.
- `SuppliedEvidence/ConfidentialityLevelCode` = **PUBLIC** (listID `urn:ubl-examples:world:codelist:ConfidentialityLevelCode`)  
  May be shared. The code is from the Trade Accord's confidentiality level list: PUBLIC = Public.
- `SuppliedEvidence/EvidenceIssuingParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SuppliedEvidence/EvidenceIssuingParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `ValidityPeriod/StartDate` = **2026-04-30**  
  From the count of 30 April
- `ValidityPeriod/EndDate` = **2026-05-31**  
  to the next, at the end of May.
- `WebSite/ID` = **WEB-1**  
  The stock page.
- `WebSite/Name` = **Stock**  
  Its name.
- `WebSite/Description` = **Live stock levels.**  
  What it shows.
- `WebSite/WebSiteTypeCode` = **EXTRANET** (listID `urn:ubl-examples:world:codelist:WebSiteTypeCode`)  
  For trade customers. The code is from the Trade Accord's web site type list: EXTRANET = Extranet.
- `WebSite/URI` = **https://www.lumeway.example/stock**  
  Where.
- `WebSite/WebSiteAccess/URI` = **https://www.lumeway.example/login**  
  The login page.
- `WebSite/WebSiteAccess/Password` = **Tq7-mR4w-Lz9**  
  The one-time password for the first login, which the extranet asks to be changed at once and accepts only until 2026-05-18: a new customer cannot choose a password before it has an account. It is no secret once used.
- `WebSite/WebSiteAccess/Login` = **velumi**  
  The login the distributor set up for the new customer.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<BusinessCard xmlns="urn:oasis:names:specification:ubl:schema:xsd:BusinessCard-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:business-card:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:onboarding:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LMW-TX-26-0956</cbc:ProfileExecutionID>
  <cbc:ID>LMW-BC-26-0048</cbc:ID>
  <cbc:UUID>da594e74-bfa8-5df5-ab8d-930b60c73ea9</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>16:39:00-01:00</cbc:IssueTime>
  <cbc:VersionID>2</cbc:VersionID>
  <cbc:PreviousVersionID>1</cbc:PreviousVersionID>
  <cbc:BriefDescription>Distributor of street and garden furniture for Bayvarra and the islands, with a weekly sailing to Selanu (Port Wrenfield in the island's address register).</cbc:BriefDescription>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-BC</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
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
      <cbc:Name>Sales office</cbc:Name>
      <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>sales@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:BusinessParty>
  <cac:BrochureDocumentReference>
    <cbc:ID>LMW-BROCHURE-2026</cbc:ID>
    <cac:Attachment>
      <cac:ExternalReference>
        <cbc:URI>https://www.lumeway.example/brochure-2026.pdf</cbc:URI>
        <cbc:MimeCode listID="IANA Media Types">application/pdf</cbc:MimeCode>
      </cac:ExternalReference>
    </cac:Attachment>
  </cac:BrochureDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>LMW-REG-XB</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">101</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:BusinessCapability>
    <cbc:ID>CAP-STOCK</cbc:ID>
    <cbc:CapabilityTypeCode listID="urn:ubl-examples:world:codelist:BusinessCapabilityTypeCode">WAREHOUSING</cbc:CapabilityTypeCode>
    <cbc:Description>Stock of 264 park benches in Marrowdale, as counted on 30 April.</cbc:Description>
    <cbc:ValueAmount currencyID="XBL">105336.00</cbc:ValueAmount>
    <cbc:ValueQuantity unitCode="EA">264</cbc:ValueQuantity>
    <cac:SuppliedEvidence>
      <cbc:ID>LMW-COUNT-26-04</cbc:ID>
      <cbc:EvidenceTypeCode listID="urn:ubl-examples:world:codelist:EvidenceTypeCode">STOCKCOUNT</cbc:EvidenceTypeCode>
      <cbc:Name>Stock count of 30 April 2026</cbc:Name>
      <cbc:Description>The distributor's own count of its warehouse at the end of April; it counts its stock at the end of every month.</cbc:Description>
      <cbc:ConfidentialityLevelCode listID="urn:ubl-examples:world:codelist:ConfidentialityLevelCode">PUBLIC</cbc:ConfidentialityLevelCode>
      <cac:EvidenceIssuingParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:EvidenceIssuingParty>
    </cac:SuppliedEvidence>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-04-30</cbc:StartDate>
      <cbc:EndDate>2026-05-31</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:WebSite>
      <cbc:ID>WEB-1</cbc:ID>
      <cbc:Name>Stock</cbc:Name>
      <cbc:Description>Live stock levels.</cbc:Description>
      <cbc:WebSiteTypeCode listID="urn:ubl-examples:world:codelist:WebSiteTypeCode">EXTRANET</cbc:WebSiteTypeCode>
      <cbc:URI>https://www.lumeway.example/stock</cbc:URI>
      <cac:WebSiteAccess>
        <cbc:URI>https://www.lumeway.example/login</cbc:URI>
        <cbc:Password>Tq7-mR4w-Lz9</cbc:Password>
        <cbc:Login>velumi</cbc:Login>
      </cac:WebSiteAccess>
    </cac:WebSite>
  </cac:BusinessCapability>
</BusinessCard>
```
