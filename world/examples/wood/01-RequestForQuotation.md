# Request For Quotation: Valdara Industries to Marrowdale Sawmill

*Example 1 of the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)" · [Request For Quotation in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REQUEST-FOR-QUOTATION-SCHEMA)*

Slats to the manufacturer's own drawing, of thermally modified ash: it asks the sawmill to quote before ordering.

[The XML file](01-RequestForQuotation.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:request-for-quotation:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Request for quotation". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:sourcing:1.0**  
  The Trade Accord's process profile the document belongs to: sourcing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900042764**  
  The collaboration this document belongs to: Valdara's purchase of slats from Marrowdale Sawmill. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **6000012829**  
  The buyer's request number.
- `UUID` = **60bedaa8-3e5b-540b-b932-135490f03c25**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-16**  
  The manufacturer asks for slats to its own dimensions.
- `IssueTime` = **10:00:00-01:00**  
  The time of the request; quotations refer to it; in the issuer's local time, with its offset from UTC.
- `SubmissionDueDate` = **2026-02-21**  
  Quotations are wanted within five days.
- `Note` = **Slats of thermally modified ash to our drawing VI-DS-SL1800; kiln-dried oak of the same size is acceptable as an alternative if quoted.**  
  What is asked.
- `PricingCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  Prices in lume, the sawmill's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **1**  
  One line.

### Requested Validity Period

Inside `RequestedValidityPeriod`:

- `DurationMeasure` = **30** (unitCode `DAY`)  
  The prices should hold for 30 days.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **VI-DS-SL1800**  
  The drawing of the slat.
- `DocumentTypeCode` = **174** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to: Valdara's drawing of the bench slat. The code is from the world's copy of UN/EDIFACT 1001 Document name: 174 = Drawing.

### Signature

Inside `Signature`:

- `ID` = **VI-SIG-26-RFQ**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; as Marrowdale Sawmill gives it.
- `Party/PostalAddress/ID` = **UL-ADR-296778** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Marrowdale Sawmill gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits). As Marrowdale Sawmill gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Marrowdale Sawmill gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; as Marrowdale Sawmill gives it.
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Marrowdale Sawmill gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Marrowdale Sawmill gives it.
- `Party/Contact/Telephone` = **+999 2 7121 338 173**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Marrowdale Sawmill gives it.
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Marrowdale Sawmill gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Marrowdale Sawmill gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `Party/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `Party/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Valdara Industries gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Party/Contact/ElectronicMail` = **purchasing@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `DeliveryLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `DeliveryLocation/Name` = **Valdara Industries, goods-in, Ferrano**  
  Where the slats are wanted.
- `RequestedDeliveryPeriod/StartDate` = **2026-02-26**  
  From the end of the second week.
- `RequestedDeliveryPeriod/EndDate` = **2026-03-06**  
  Within about a week.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **DAP** (schemeID `INCOTERMS`)  
  Delivered at the factory. The code is from the world's copy of Incoterms 2020: DAP = Delivered at Place. An identifier that holds a code names the code's list in its schemeID.

### Destination Country

Inside `DestinationCountry`:

- `IdentificationCode` = **XU** (listID `ISO 3166`)  
  Into Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Contract

Inside `Contract`:

- `ID` = **VI-PUR-TERMS-2026**  
  The manufacturer's purchasing terms.

### Request For Quotation Line

Inside `RequestForQuotationLine`:

- `ID` = **1**  
  The line's number in the request.
- `UUID` = **69477890-8e3a-52ba-acae-4da29ea0b964**  
  The line's UUID.
- `Note` = **Thermally modified ash, planed on four sides, as drawn.**  
  The requirement.
- `OptionalLineItemIndicator` = **false**  
  A required line.
- `PrivacyCode` = **CONFIDENTIAL** (listID `urn:ubl-examples:world:codelist:PrivacyCode`)  
  The drawing is the manufacturer's own. The code is from the Trade Accord's privacy list: CONFIDENTIAL = Confidential.
- `DocumentReference/ID` = **VI-DS-SL1800**  
  The drawing.
- `DocumentReference/DocumentTypeCode` = **174** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to: Valdara's drawing of the bench slat. The code is from the world's copy of UN/EDIFACT 1001 Document name: 174 = Drawing.
- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **96** (unitCode `EA`)  
  96 bundles of 50 slats, 4,800 slats: enough for 960 benches at five a bench, a quarter's supply.
- `LineItem/Item/Description` = **Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.**  
  The seller's description.
- `LineItem/Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `LineItem/Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; as Marrowdale Sawmill describes the item.
- `LineItem/Item/Name` = **Bench slat 1800, bundle of 50**  
  The item's short name.
- `LineItem/Item/SellersItemIdentification/ID` = **MDS-SL-1800-50**  
  The seller's own item number; as Marrowdale Sawmill describes the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RequestForQuotation xmlns="urn:oasis:names:specification:ubl:schema:xsd:RequestForQuotation-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:request-for-quotation:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:sourcing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900042764</cbc:ProfileExecutionID>
  <cbc:ID>6000012829</cbc:ID>
  <cbc:UUID>60bedaa8-3e5b-540b-b932-135490f03c25</cbc:UUID>
  <cbc:IssueDate>2026-02-16</cbc:IssueDate>
  <cbc:IssueTime>10:00:00-01:00</cbc:IssueTime>
  <cbc:SubmissionDueDate>2026-02-21</cbc:SubmissionDueDate>
  <cbc:Note>Slats of thermally modified ash to our drawing VI-DS-SL1800; kiln-dried oak of the same size is acceptable as an alternative if quoted.</cbc:Note>
  <cbc:PricingCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:PricingCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:RequestedValidityPeriod>
    <cbc:DurationMeasure unitCode="DAY">30</cbc:DurationMeasure>
  </cac:RequestedValidityPeriod>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-DS-SL1800</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">174</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>VI-SIG-26-RFQ</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-296778</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Timber Lane</cbc:StreetName>
        <cbc:BuildingNumber>7</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71202</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 338 173</cbc:Telephone>
        <cbc:ElectronicMail>sales@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:Delivery>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
      <cbc:Name>Valdara Industries, goods-in, Ferrano</cbc:Name>
    </cac:DeliveryLocation>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-02-26</cbc:StartDate>
      <cbc:EndDate>2026-03-06</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">DAP</cbc:ID>
  </cac:DeliveryTerms>
  <cac:DestinationCountry>
    <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
  </cac:DestinationCountry>
  <cac:Contract>
    <cbc:ID>VI-PUR-TERMS-2026</cbc:ID>
  </cac:Contract>
  <cac:RequestForQuotationLine>
    <cbc:ID>1</cbc:ID>
    <cbc:UUID>69477890-8e3a-52ba-acae-4da29ea0b964</cbc:UUID>
    <cbc:Note>Thermally modified ash, planed on four sides, as drawn.</cbc:Note>
    <cbc:OptionalLineItemIndicator>false</cbc:OptionalLineItemIndicator>
    <cbc:PrivacyCode listID="urn:ubl-examples:world:codelist:PrivacyCode">CONFIDENTIAL</cbc:PrivacyCode>
    <cac:DocumentReference>
      <cbc:ID>VI-DS-SL1800</cbc:ID>
      <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">174</cbc:DocumentTypeCode>
    </cac:DocumentReference>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Item>
        <cbc:Description>Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.</cbc:Description>
        <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
        <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
        <cbc:Name>Bench slat 1800, bundle of 50</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>MDS-SL-1800-50</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:RequestForQuotationLine>
</RequestForQuotation>
```
