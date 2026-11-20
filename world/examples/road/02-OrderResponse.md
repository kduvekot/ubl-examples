# Order Response: Valdara Industries to Lumeway Distribution

*Example 2 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Order Response in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-RESPONSE-SCHEMA)*

The manufacturer accepts the order with one change: the 2026 casting with the reinforced foot replaces the side frame ordered, at the same price, for the old casting is no longer made. It confirms the collection at its 3PL's warehouse by the buyer's carrier.

[The XML file](02-OrderResponse.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order-response:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order response". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **LMW-TX-26-0573**  
  The collaboration this document belongs to: Lumeway's order of benches from Valdara, from the order to the payment. Lumeway Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **1100043246**  
  The seller's number for its response.
- `UUID` = **1146579f-1ec8-554d-82aa-cfc09cc9d888**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-17**  
  The manufacturer answers the next day.
- `IssueTime` = **17:42:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `OrderResponseCode` = **CA** (listID `UN/EDIFACT EDED 4343`)  
  UN/EDIFACT 4343 code CA: conditionally accepted, with the substitution of line 2. The code is from the world's copy of UN/EDIFACT 4343 Response type: CA = Conditionally accepted.
- `Note` = **Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the same price.**  
  The condition in words.

### Order Reference

Inside `OrderReference`:

- `ID` = **LMW-PO-26-0573**  
  The order this response answers.

### Seller Supplier Party

Inside `SellerSupplierParty`:

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
- `Party/Contact/Name` = **Order desk**  
  The party's main desk, which handles this document; as Valdara Industries gives it.
- `Party/Contact/JobTitle` = **Order administrator**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Party/Contact/Telephone` = **+999 1 041 386 4551**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `Party/Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 351 400 5258**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

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
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Lumeway Distribution gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Party/Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Party/Contact/ElectronicMail` = **purchasing@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `PromisedDeliveryPeriod/StartDate` = **2026-03-23**  
  Under FCA delivery is the handover to the buyer's carrier: on day 7.
- `PromisedDeliveryPeriod/EndDate` = **2026-03-24**  
  Or the morning after, by the guaranteed despatch.
- `Despatch/EstimatedDespatchDate` = **2026-03-23**  
  The goods will be ready on the requested day.
- `Despatch/EstimatedDespatchTime` = **14:00:00**  
  At the requested time.
- `Despatch/GuaranteedDespatchDate` = **2026-03-24**  
  At the latest the next day.
- `Despatch/GuaranteedDespatchTime` = **12:00:00**  
  By noon.
- `Despatch/NotifyParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Despatch/NotifyParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Despatch/ResponsibleParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Despatch/ResponsibleParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `Despatch/EstimatedDespatchPeriod/StartDate` = **2026-03-23**  
  The afternoon of day 7.
- `Despatch/EstimatedDespatchPeriod/EndDate` = **2026-03-24**  
  Or the morning after.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The benches.
- `LineItem/Quantity` = **96** (unitCode `EA`)  
  As ordered.
- `LineItem/Item/Name` = **Park bench Serra 180**  
  Named only.
- `LineItem/Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's number.
- `OrderLineReference/LineID` = **1**  
  The order line.
- `OrderLineReference/UUID` = **da67b26b-2501-5b9b-9b6f-d03d5ce50a97**  
  A universally unique identifier of the line, derived from the document and the line number.
- `DocumentReference/ID` = **VI-DS-B180**  
  The datasheet of the item confirmed.
- `DocumentReference/DocumentType` = **Product data sheet**  
  The kind of document referred to, Valdara's data sheet of the Serra bench, a document outside the examples, in words: no list has an exact code for it (cited).
- `SubstitutionStatusCode` = **Substitution** (listID `urn:oasis:names:specification:ubl:codelist:gc:SubstitutionStatusCode`)  
  The line is delivered with a substitute item. The code is from the world's copy of UBL's Substitution status list, with a listID: Substitution.
- `Note` = **Same fit and price; the old casting is no longer made.**  
  Why the substitute is offered.
- `LineItem/ID` = **2**  
  The side frames, as ordered.
- `LineItem/LineStatusCode` = **Revised** (listID `urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode`)  
  Changed by the seller. The code is from the world's copy of UBL's Line status list, with a listID: Revised = Line has been revised..
- `LineItem/Quantity` = **12** (unitCode `EA`)  
  As ordered.
- `LineItem/Item/Name` = **Bench side frame casting**  
  The frame ordered.
- `LineItem/Item/SellersItemIdentification/ID` = **VI-C180**  
  Its number.
- `SellerSubstitutedLineItem/ID` = **2**  
  The substitute for line 2.
- `SellerSubstitutedLineItem/Quantity` = **12** (unitCode `EA`)  
  The same quantity.
- `SellerSubstitutedLineItem/Price/PriceAmount` = **4750** (currencyID `XUF`)  
  Valdara's distributor price for Lumeway Distribution, its distributor for Bayvarra and the island under the distribution agreement of 1996: below the list price, which a direct customer pays.
- `SellerSubstitutedLineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `SellerSubstitutedLineItem/Item/Name` = **Bench side frame casting, 2026**  
  The substitute.
- `SellerSubstitutedLineItem/Item/SellersItemIdentification/ID` = **VI-C180**  
  The same item number.
- `SellerSubstitutedLineItem/Item/SellersItemIdentification/ExtendedID` = **2026**  
  The new version, the 2026 casting: every later document of the flow identifies the frame so.
- `OrderLineReference/LineID` = **2**  
  The order line.
- `OrderLineReference/SalesOrderLineID` = **2**  
  The seller's line.
- `OrderLineReference/UUID` = **058a35ee-7283-5e0f-831e-dc6fe709773f**  
  A universally unique identifier of the line, derived from the document and the line number.
- `OrderLineReference/LineStatusCode` = **Revised** (listID `urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode`)  
  The line is answered with a substitute. The code is from the world's copy of UBL's Line status list, with a listID: Revised = Line has been revised..
- `DocumentReference/ID` = **VI-DS-C180-2026**  
  The datasheet of the item confirmed.
- `DocumentReference/DocumentType` = **Product data sheet**  
  The kind of document referred to, Valdara's data sheet of the 2026 side frame, a document outside the examples, in words: no list has an exact code for it (cited).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<OrderResponse xmlns="urn:oasis:names:specification:ubl:schema:xsd:OrderResponse-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order-response:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LMW-TX-26-0573</cbc:ProfileExecutionID>
  <cbc:ID>1100043246</cbc:ID>
  <cbc:UUID>1146579f-1ec8-554d-82aa-cfc09cc9d888</cbc:UUID>
  <cbc:IssueDate>2026-03-17</cbc:IssueDate>
  <cbc:IssueTime>17:42:00-01:00</cbc:IssueTime>
  <cbc:OrderResponseCode listID="UN/EDIFACT EDED 4343">CA</cbc:OrderResponseCode>
  <cbc:Note>Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the same price.</cbc:Note>
  <cac:OrderReference>
    <cbc:ID>LMW-PO-26-0573</cbc:ID>
  </cac:OrderReference>
  <cac:SellerSupplierParty>
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
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Order administrator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
          <cbc:Value>+999 1 351 400 5258</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
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
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:Delivery>
    <cac:PromisedDeliveryPeriod>
      <cbc:StartDate>2026-03-23</cbc:StartDate>
      <cbc:EndDate>2026-03-24</cbc:EndDate>
    </cac:PromisedDeliveryPeriod>
    <cac:Despatch>
      <cbc:EstimatedDespatchDate>2026-03-23</cbc:EstimatedDespatchDate>
      <cbc:EstimatedDespatchTime>14:00:00</cbc:EstimatedDespatchTime>
      <cbc:GuaranteedDespatchDate>2026-03-24</cbc:GuaranteedDespatchDate>
      <cbc:GuaranteedDespatchTime>12:00:00</cbc:GuaranteedDespatchTime>
      <cac:NotifyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:NotifyParty>
      <cac:ResponsibleParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Trasvia Haulage</cbc:Name>
        </cac:PartyName>
      </cac:ResponsibleParty>
      <cac:EstimatedDespatchPeriod>
        <cbc:StartDate>2026-03-23</cbc:StartDate>
        <cbc:EndDate>2026-03-24</cbc:EndDate>
      </cac:EstimatedDespatchPeriod>
    </cac:Despatch>
  </cac:Delivery>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>VI-B180</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cbc:UUID>da67b26b-2501-5b9b-9b6f-d03d5ce50a97</cbc:UUID>
    </cac:OrderLineReference>
    <cac:DocumentReference>
      <cbc:ID>VI-DS-B180</cbc:ID>
      <cbc:DocumentType>Product data sheet</cbc:DocumentType>
    </cac:DocumentReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cbc:SubstitutionStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:SubstitutionStatusCode">Substitution</cbc:SubstitutionStatusCode>
    <cbc:Note>Same fit and price; the old casting is no longer made.</cbc:Note>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:LineStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode">Revised</cbc:LineStatusCode>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Bench side frame casting</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>VI-C180</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
    <cac:SellerSubstitutedLineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">4750</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Name>Bench side frame casting, 2026</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>VI-C180</cbc:ID>
          <cbc:ExtendedID>2026</cbc:ExtendedID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:SellerSubstitutedLineItem>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
      <cbc:SalesOrderLineID>2</cbc:SalesOrderLineID>
      <cbc:UUID>058a35ee-7283-5e0f-831e-dc6fe709773f</cbc:UUID>
      <cbc:LineStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:LineStatusCode">Revised</cbc:LineStatusCode>
    </cac:OrderLineReference>
    <cac:DocumentReference>
      <cbc:ID>VI-DS-C180-2026</cbc:ID>
      <cbc:DocumentType>Product data sheet</cbc:DocumentType>
    </cac:DocumentReference>
  </cac:OrderLine>
</OrderResponse>
```
