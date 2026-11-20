# Forecast Revision: Lumeport Textile Mill to Selanu Cotton Ginnery

*Example 7 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Forecast Revision in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORECAST-REVISION-SCHEMA)*

Demand for clothing is up; the mill revises its forecast upwards.

[The XML file](07-ForecastRevision.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:forecast:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Forecast". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:collaboration:1.0**  
  The Trade Accord's process profile the document belongs to: collaborative planning, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LTM-FR-26-0197**  
  The revision's number.
- `UUID` = **1680348b-7683-52e2-b21d-f88ff92b0f43**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-21**  
  Late April, when the store's clothing orders for the winter are in and demand has risen.
- `IssueTime` = **11:08:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC.
- `Note` = **Demand for clothing has risen.**  
  Why the forecast is revised.
- `SequenceNumberID` = **1**  
  The first revision of the forecast.
- `RevisionStatusCode` = **REVISED** (listID `urn:ubl-examples:world:codelist:RevisionStatusCode`)  
  A revised forecast. The code is from the Trade Accord's revision status list: REVISED = Revised.
- `PurposeCode` = **ORDER** (listID `urn:ubl-examples:world:codelist:ForecastPurposeCode`)  
  Of what the mill will order. The code is from the Trade Accord's forecast purpose list: ORDER = Order forecast.

### Forecast Period

Inside `ForecastPeriod`:

- `StartDate` = **2026-04-01**  
  The same period as the forecast.
- `EndDate` = **2026-07-31**  
  Its end.

### Original Document Reference

Inside `OriginalDocumentReference`:

- `ID` = **LTM-FC-26-0192**  
  The forecast revised.
- `DocumentTypeCode` = **Forecast** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LTM-FC-26-0192 is the example cotton/02, a Forecast; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Forecast.

### Signature

Inside `Signature`:

- `ID` = **LT-SIG-26-0222**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524010900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeport Textile Mill gives it.
- `PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; as Lumeport Textile Mill gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-933254** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Textile Mill gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. as Lumeport Textile Mill gives it.
- `PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. as Lumeport Textile Mill gives it.
- `PostalAddress/CitySubdivisionName` = **Mill Quarter**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. as Lumeport Textile Mill gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Lumeport Textile Mill gives it.
- `PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). as Lumeport Textile Mill gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Lumeport Textile Mill gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Purchasing**  
  The party's main desk, which handles this document; as Lumeport Textile Mill gives it.
- `Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Lumeport Textile Mill gives it.
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Lumeport Textile Mill gives it.
- `Contact/Telephone` = **+999 2 38 2837 6029**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. as Lumeport Textile Mill gives it.
- `Contact/ElectronicMail` = **purchasing@lumeporttextile.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeport Textile Mill gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Textile Mill gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Cotton Ginnery gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Cotton Ginnery gives it.
- `PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Cotton Ginnery gives it.
- `PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. as Selanu Cotton Ginnery gives it.
- `PostalAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. as Selanu Cotton Ginnery gives it.
- `PostalAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Selanu Cotton Ginnery gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Cotton sales**  
  The party's main desk, which handles this document; as Selanu Cotton Ginnery gives it.
- `Contact/JobTitle` = **Cotton sales manager**  
  The job of the person who answers at the desk; as Selanu Cotton Ginnery gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Selanu Cotton Ginnery gives it.
- `Contact/Telephone` = **+999 3 721 0486**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Selanu Cotton Ginnery gives it.
- `Contact/ElectronicMail` = **cotton@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu Cotton Ginnery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Cotton Ginnery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Forecast Revision Line

Inside `ForecastRevisionLine`:

- `ID` = **1**  
  The only line.
- `Note` = **Twenty per cent more.**  
  The change: 28,800 kg against 24,000 kg.
- `Description` = **More bales over the season.**  
  In words: the season's total, for the whole period of the forecast.
- `RevisedForecastLineID` = **1**  
  The forecast line revised.
- `SourceForecastIssueDate` = **2026-02-02**  
  The issue date of the forecast revised.
- `SourceForecastIssueTime` = **09:00:00**  
  Its issue time.
- `AdjustmentReasonCode` = **DEMAND** (listID `urn:ubl-examples:world:codelist:ForecastAdjustmentReasonCode`)  
  Higher demand. The code is from the Trade Accord's forecast adjustment reason list: DEMAND = Demand change.
- `ForecastPeriod/StartDate` = **2026-04-01**  
  The whole period of the forecast: the new total is the season's.
- `ForecastPeriod/EndDate` = **2026-07-31**  
  To its end.
- `SalesItem/Quantity` = **28800** (unitCode `KGM`)  
  The season's total raised by twenty per cent: 24,000 kg × 1.20.
- `SalesItem/Item/Description` = **Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `SalesItem/Item/Description` = **Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries.
- `SalesItem/Item/Name` = **Tekapa suhema, lafatite senehu** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `SalesItem/Item/Name` = **Cotton lint, compressed bale** (languageID `en-XB`)  
  The item's name in English, the working language between the countries.
- `SalesItem/Item/SellersItemIdentification/ID` = **SCG-LINT**  
  The seller's own item number; as Selanu Cotton Ginnery describes the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForecastRevision xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForecastRevision-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:forecast:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:collaboration:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LTM-FR-26-0197</cbc:ID>
  <cbc:UUID>1680348b-7683-52e2-b21d-f88ff92b0f43</cbc:UUID>
  <cbc:IssueDate>2026-04-21</cbc:IssueDate>
  <cbc:IssueTime>11:08:00-01:00</cbc:IssueTime>
  <cbc:Note>Demand for clothing has risen.</cbc:Note>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:RevisionStatusCode listID="urn:ubl-examples:world:codelist:RevisionStatusCode">REVISED</cbc:RevisionStatusCode>
  <cbc:PurposeCode listID="urn:ubl-examples:world:codelist:ForecastPurposeCode">ORDER</cbc:PurposeCode>
  <cac:ForecastPeriod>
    <cbc:StartDate>2026-04-01</cbc:StartDate>
    <cbc:EndDate>2026-07-31</cbc:EndDate>
  </cac:ForecastPeriod>
  <cac:OriginalDocumentReference>
    <cbc:ID>LTM-FC-26-0192</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Forecast</cbc:DocumentTypeCode>
  </cac:OriginalDocumentReference>
  <cac:Signature>
    <cbc:ID>LT-SIG-26-0222</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9524010900002</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-933254</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Mill Street</cbc:StreetName>
      <cbc:BuildingNumber>21</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Mill Quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38504</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Buyer</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 2 38 2837 6029</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@lumeporttextile.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
      <cbc:BuildingNumber>42</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
      <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Cotton sales</cbc:Name>
      <cbc:JobTitle>Cotton sales manager</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
      <cbc:ElectronicMail>cotton@selanuginnery.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:ForecastRevisionLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Twenty per cent more.</cbc:Note>
    <cbc:Description>More bales over the season.</cbc:Description>
    <cbc:RevisedForecastLineID>1</cbc:RevisedForecastLineID>
    <cbc:SourceForecastIssueDate>2026-02-02</cbc:SourceForecastIssueDate>
    <cbc:SourceForecastIssueTime>09:00:00</cbc:SourceForecastIssueTime>
    <cbc:AdjustmentReasonCode listID="urn:ubl-examples:world:codelist:ForecastAdjustmentReasonCode">DEMAND</cbc:AdjustmentReasonCode>
    <cac:ForecastPeriod>
      <cbc:StartDate>2026-04-01</cbc:StartDate>
      <cbc:EndDate>2026-07-31</cbc:EndDate>
    </cac:ForecastPeriod>
    <cac:SalesItem>
      <cbc:Quantity unitCode="KGM">28800</cbc:Quantity>
      <cac:Item>
        <cbc:Description languageID="qal">Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.</cbc:Description>
        <cbc:Description languageID="en-XB">Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.</cbc:Description>
        <cbc:Name languageID="qal">Tekapa suhema, lafatite senehu</cbc:Name>
        <cbc:Name languageID="en-XB">Cotton lint, compressed bale</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>SCG-LINT</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:SalesItem>
  </cac:ForecastRevisionLine>
</ForecastRevision>
```
