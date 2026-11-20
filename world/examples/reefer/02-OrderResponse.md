# Order Response: Harrowmead Fruit Growers to Hafefo Fresh Produce

*Example 2 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Order Response in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-RESPONSE-SCHEMA)*

The cooperative accepts the order on a condition: its stored pears are running short, so it offers three pallets of pears instead of four and a fifth pallet of Granny Smith in their place, the offer open until Friday noon, its cut-off for booking the reefer on the next Thursday's ship.

[The XML file](02-OrderResponse.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order-response:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order response". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **HFG-OR-26-0554**  
  The seller's number for its response.
- `UUID` = **ccc57df8-55d8-508d-b264-68902a934a06**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-09**  
  The cooperative answers the next morning, once it has checked its cold store.
- `IssueTime` = **09:15:00-01:00**  
  In the morning, after the cold store's stock count; in the issuer's local time, with its offset from UTC.
- `OrderResponseCode` = **CA** (listID `UN/EDIFACT EDED 4343`)  
  UN/EDIFACT 4343 code CA: conditionally accepted. The cooperative accepts the order with a change to two of its lines, on condition that the wholesaler agrees before the offer lapses. The code is from the world's copy of UN/EDIFACT 4343 Response type: CA = Conditionally accepted.
- `Note` = **Accepted with a change: our stored Packham's pears are running short, so we offer three pallets of pears instead of four and a fifth pallet of Granny Smith in their place, at the same prices. The offer stands until Friday 17 April at noon, when we must book the reefer for Thursday's ship.**  
  The response in words: what changes, and why.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the cooperative's currency, as in the order; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **3**  
  The number of lines.

### Validity Period

Inside `ValidityPeriod`:

- `EndDate` = **2026-04-17**  
  The changed mix is offered until Friday 17 April, ...
- `EndTime` = **12:00:00**  
  ... at noon: the cooperative's cut-off for booking the reefer on the sailing of Thursday 23 April; after it the offer lapses and the fruit would go on a later ship.

### Order Reference

Inside `OrderReference`:

- `ID` = **HFP-PO-26-0553**  
  The order this response answers.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Harrowmead Fruit Growers gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Harrowmead Fruit Growers gives it.
- `Party/PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; as Harrowmead Fruit Growers gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-418726** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Harrowmead Fruit Growers gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Orchard Road**  
  Street of the postal address. As Harrowmead Fruit Growers gives it.
- `Party/PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. As Harrowmead Fruit Growers gives it.
- `Party/PostalAddress/CityName` = **Harrowmead**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Harrowmead Fruit Growers gives it.
- `Party/PostalAddress/PostalZone` = **71640**  
  Postal code in Bayvarra's format (5 digits). As Harrowmead Fruit Growers gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Harrowmead Fruit Growers gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Harrowmead Fruit Growers gives it.
- `Party/Contact/JobTitle` = **Export sales coordinator**  
  The job of the person who answers at the desk; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Telephone` = **+999 2 7164 281 590**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Harrowmead Fruit Growers gives it.
- `Party/Contact/ElectronicMail` = **sales@harrowmeadfruit.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Harrowmead Fruit Growers gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20415873** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Harrowmead Fruit Growers gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Hafefo Fresh Produce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; as Hafefo Fresh Produce gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `Party/PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Hafefo Fresh Produce gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Hafefo Fresh Produce gives it.
- `Party/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Hafefo Fresh Produce gives it.
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. As Hafefo Fresh Produce gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Hafefo Fresh Produce gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Hafefo Fresh Produce gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Hafefo Fresh Produce gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Hafefo Fresh Produce gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Hafefo Fresh Produce gives it.
- `Party/Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Hafefo Fresh Produce gives it.
- `Party/Contact/ElectronicMail` = **purchasing@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Hafefo Fresh Produce gives it.
- `Party/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; as Hafefo Fresh Produce gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC43529** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Hafefo Fresh Produce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CIP** (schemeID `INCOTERMS`)  
  Incoterms 2020, as ordered. The code is from the world's copy of Incoterms 2020: CIP = Carriage and Insurance Paid To. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `DeliveryLocation/Name` = **Port of Selanu**  
  The named place of destination.
- `DeliveryLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **28868.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export from Bayvarra: the state sales tax is not charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **EXP** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: EXP = Export outside Bayvarra.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  The name of code EXP in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **28868.00** (currencyID `XBL`)  
  The sum of the lines, with the changed mix.
- `PayableAmount` = **28868.00** (currencyID `XBL`)  
  The fruit at its CIP prices, the changed mix: what the invoice will bill.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number, as in the order.
- `LineItem/Note` = **Confirmed as ordered.**  
  The line's answer in words.
- `LineItem/Quantity` = **672** (unitCode `EA`)  
  The quantity the cooperative confirms.
- `LineItem/LineExtensionAmount` = **17472.00** (currencyID `XBL`)  
  Quantity times price.
- `LineItem/Price/PriceAmount` = **26** (currencyID `XBL`)  
  The cooperative's price for the island this season, a carton carriage and insurance paid to the Port of Selanu (CIP): it holds the reefer's haulage to Lumeport, the sea freight and the cargo insurance.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Name` = **Apples Gala, carton 18 kg, count 100**  
  Named only: described in full in the order.
- `LineItem/Item/SellersItemIdentification/ID` = **HFC-GAL100**  
  The seller's number.
- `OrderLineReference/LineID` = **1**  
  The order line answered.
- `LineItem/ID` = **2**  
  The line number, as in the order.
- `LineItem/Note` = **Changed: 280 cartons instead of the 224 ordered.**  
  The line's answer in words.
- `LineItem/Quantity` = **280** (unitCode `EA`)  
  The quantity the cooperative offers in place of the one ordered.
- `LineItem/LineExtensionAmount` = **6860.00** (currencyID `XBL`)  
  Quantity times price.
- `LineItem/Price/PriceAmount` = **24.5** (currencyID `XBL`)  
  The cooperative's price for the island this season, a carton carriage and insurance paid to the Port of Selanu (CIP): it holds the reefer's haulage to Lumeport, the sea freight and the cargo insurance.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Name` = **Apples Granny Smith, carton 18 kg, count 100**  
  Named only: described in full in the order.
- `LineItem/Item/SellersItemIdentification/ID` = **HFC-GSM100**  
  The seller's number.
- `OrderLineReference/LineID` = **2**  
  The order line answered.
- `LineItem/ID` = **3**  
  The line number, as in the order.
- `LineItem/Note` = **Changed: 168 cartons instead of the 224 ordered.**  
  The line's answer in words.
- `LineItem/Quantity` = **168** (unitCode `EA`)  
  The quantity the cooperative offers in place of the one ordered.
- `LineItem/LineExtensionAmount` = **4536.00** (currencyID `XBL`)  
  Quantity times price.
- `LineItem/Price/PriceAmount` = **27** (currencyID `XBL`)  
  The cooperative's price for the island this season, a carton carriage and insurance paid to the Port of Selanu (CIP): it holds the reefer's haulage to Lumeport, the sea freight and the cargo insurance.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Name` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  Named only: described in full in the order.
- `LineItem/Item/SellersItemIdentification/ID` = **HFC-PKT080**  
  The seller's number.
- `OrderLineReference/LineID` = **3**  
  The order line answered.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<OrderResponse xmlns="urn:oasis:names:specification:ubl:schema:xsd:OrderResponse-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order-response:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>HFG-OR-26-0554</cbc:ID>
  <cbc:UUID>ccc57df8-55d8-508d-b264-68902a934a06</cbc:UUID>
  <cbc:IssueDate>2026-04-09</cbc:IssueDate>
  <cbc:IssueTime>09:15:00-01:00</cbc:IssueTime>
  <cbc:OrderResponseCode listID="UN/EDIFACT EDED 4343">CA</cbc:OrderResponseCode>
  <cbc:Note>Accepted with a change: our stored Packham's pears are running short, so we offer three pallets of pears instead of four and a fifth pallet of Granny Smith in their place, at the same prices. The offer stands until Friday 17 April at noon, when we must book the reefer for Thursday's ship.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:ValidityPeriod>
    <cbc:EndDate>2026-04-17</cbc:EndDate>
    <cbc:EndTime>12:00:00</cbc:EndTime>
  </cac:ValidityPeriod>
  <cac:OrderReference>
    <cbc:ID>HFP-PO-26-0553</cbc:ID>
  </cac:OrderReference>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9527430900003</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-418726</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Orchard Road</cbc:StreetName>
        <cbc:BuildingNumber>3</cbc:BuildingNumber>
        <cbc:CityName>Harrowmead</cbc:CityName>
        <cbc:PostalZone>71640</cbc:PostalZone>
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
        <cbc:JobTitle>Export sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7164 281 590</cbc:Telephone>
        <cbc:ElectronicMail>sales@harrowmeadfruit.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20415873</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Hafefo Fresh Produce</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40618392</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
        <cbc:BuildingNumber>58</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 3 726 8104</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@hafefo.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 05:00–14:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC43529</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CIP</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
      <cbc:Name>Port of Selanu</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">28868.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">28868.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">28868.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Note>Confirmed as ordered.</cbc:Note>
      <cbc:Quantity unitCode="EA">672</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">17472.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">26</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Name>Apples Gala, carton 18 kg, count 100</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>HFC-GAL100</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Note>Changed: 280 cartons instead of the 224 ordered.</cbc:Note>
      <cbc:Quantity unitCode="EA">280</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">6860.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">24.5</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Name>Apples Granny Smith, carton 18 kg, count 100</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>HFC-GSM100</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Note>Changed: 168 cartons instead of the 224 ordered.</cbc:Note>
      <cbc:Quantity unitCode="EA">168</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">4536.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">27</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Name>Pears Packham's Triumph, carton 18 kg, count 80</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>HFC-PKT080</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
  </cac:OrderLine>
</OrderResponse>
```
