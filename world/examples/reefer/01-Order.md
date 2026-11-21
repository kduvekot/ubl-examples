# Order: Hafefo Fresh Produce to Harrowmead Fruit Growers

*Example 1 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The wholesaler orders one reefer of apples and pears for the island's shops, hotels and hospital kitchen in the autumn season, carriage and insurance paid to the Port of Selanu: the cooperative books and insures the reefer.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0214**  
  The collaboration this document belongs to: Hafefo's order of fruit from Harrowmead Fruit Growers. Hafefo Fresh Produce started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0215**  
  The buyer's order number.
- `UUID` = **4b4ea0bd-86a2-58ba-bf56-cedc820b8d74**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-08**  
  Ordered when the cooperative's price list for the island came out, with the Granny Smith harvest under way.
- `IssueTime` = **13:50:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `Note` = **One 40-foot reefer, apples and pears, on the sailing of 23 April.**  
  What the buyer wants, in a line.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **3**  
  The number of order lines.

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
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
  The contact's e-mail address; as Hafefo Fresh Produce gives it.
- `Party/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; as Hafefo Fresh Produce gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC43529** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Hafefo Fresh Produce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Harrowmead Fruit Growers gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Harrowmead Fruit Growers gives it.
- `Party/PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; as Harrowmead Fruit Growers gives it.
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
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Harrowmead Fruit Growers gives it.
- `Party/Contact/JobTitle` = **Export sales coordinator**  
  The job of the person who answers at the desk; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Telephone` = **+999 2 5164 281 590**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Harrowmead Fruit Growers gives it.
- `Party/Contact/ElectronicMail` = **sales@harrowmeadfruit.example**  
  The contact's e-mail address; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Harrowmead Fruit Growers gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20415873** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Harrowmead Fruit Growers gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-04-26**  
  On Tidewell's sailing of Thursday 23 April, which is at Selanu on the Sunday.
- `RequestedDeliveryPeriod/EndDate` = **2026-04-26**  
  The same day: the shops restock on the Monday.
- `DeliveryParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Hafefo Fresh Produce**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Shipment/ID` = **1**  
  The shipment the order asks for: one reefer.
- `Shipment/GoodsItem/ID` = **1**  
  The fruit of the order.
- `Shipment/GoodsItem/Temperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the cargo space during transport. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Temperature/MeasureCode` = **CHILLED** (listID `urn:ubl-examples:world:codelist:TemperatureClassCode`)  
  The wholesaler asks for the fruit to travel chilled, a class, not a figure: the cooperative and its forwarder set the reefer to the fruit's own set point. The code is from the Trade Accord's temperature class list: CHILLED = Chilled.
- `Shipment/GoodsItem/Temperature/Description` = **Chilled, not frozen**  
  In words.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CIP** (schemeID `INCOTERMS`)  
  Carriage and insurance paid to the port of Selanu (Incoterms 2020 CIP): the cooperative books the reefer, pays its carriage and insures the fruit; the risk passes to the buyer when the reefer is handed to the carrier at Lumeport. The code is from the world's copy of Incoterms 2020: CIP = Carriage and Insurance Paid To. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `DeliveryLocation/Description` = **Port of Selanu**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **29008.00** (currencyID `XBL`)  
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

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **29008.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **29008.00** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **672** (unitCode `EA`)  
  Twelve pallets of 56 cartons: Gala, the island's everyday apple.
- `LineItem/LineExtensionAmount` = **17472.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **26** (currencyID `XBL`)  
  The cooperative's price for the island this season, a carton carriage and insurance paid to the Port of Selanu (CIP): it holds the reefer's haulage to Lumeport, the sea freight and the cargo insurance.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.**  
  The seller's description.
- `LineItem/Item/Name` = **Apples Gala, carton 18 kg, count 100**  
  The item's short name.
- `LineItem/Item/SellersItemIdentification/ID` = **HRW-GAL100**  
  The seller's own item number; as Harrowmead Fruit Growers describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **9527430001014** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers'.
- `LineItem/ID` = **2**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **224** (unitCode `EA`)  
  Four pallets of 56 cartons: Granny Smith, for the shops and for the hotels' and the hospital's kitchens.
- `LineItem/LineExtensionAmount` = **5488.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **24.5** (currencyID `XBL`)  
  The cooperative's price for the island this season, a carton carriage and insurance paid to the Port of Selanu (CIP): it holds the reefer's haulage to Lumeport, the sea freight and the cargo insurance.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.**  
  The seller's description.
- `LineItem/Item/Name` = **Apples Granny Smith, carton 18 kg, count 100**  
  The item's short name.
- `LineItem/Item/SellersItemIdentification/ID` = **HRW-GSM100**  
  The seller's own item number; as Harrowmead Fruit Growers describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **9527430001021** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers'.
- `LineItem/ID` = **3**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **224** (unitCode `EA`)  
  Four pallets of 56 cartons: Packham's Triumph pears.
- `LineItem/LineExtensionAmount` = **6048.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **27** (currencyID `XBL`)  
  The cooperative's price for the island this season, a carton carriage and insurance paid to the Port of Selanu (CIP): it holds the reefer's haulage to Lumeport, the sea freight and the cargo insurance.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.**  
  The seller's description.
- `LineItem/Item/Name` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  The item's short name.
- `LineItem/Item/SellersItemIdentification/ID` = **HRW-PKT080**  
  The seller's own item number; as Harrowmead Fruit Growers describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **9527430002011** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers'.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0214</cbc:ProfileExecutionID>
  <cbc:ID>26-0215</cbc:ID>
  <cbc:UUID>4b4ea0bd-86a2-58ba-bf56-cedc820b8d74</cbc:UUID>
  <cbc:IssueDate>2026-04-08</cbc:IssueDate>
  <cbc:IssueTime>13:50:00+00:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:Note>One 40-foot reefer, apples and pears, on the sailing of 23 April.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
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
        <cbc:Telephone>+999 2 5164 281 590</cbc:Telephone>
        <cbc:ElectronicMail>sales@harrowmeadfruit.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20415873</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-04-26</cbc:StartDate>
      <cbc:EndDate>2026-04-26</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Hafefo Fresh Produce</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
    <cac:Shipment>
      <cbc:ID>1</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cac:Temperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
          <cbc:MeasureCode listID="urn:ubl-examples:world:codelist:TemperatureClassCode">CHILLED</cbc:MeasureCode>
          <cbc:Description>Chilled, not frozen</cbc:Description>
        </cac:Temperature>
      </cac:GoodsItem>
    </cac:Shipment>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CIP</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
      <cbc:Description>Port of Selanu</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">29008.00</cbc:TaxableAmount>
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
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">29008.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">29008.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">672</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">17472.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">26</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.</cbc:Description>
        <cbc:Name>Apples Gala, carton 18 kg, count 100</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>HRW-GAL100</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9527430001014</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="EA">224</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">5488.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">24.5</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.</cbc:Description>
        <cbc:Name>Apples Granny Smith, carton 18 kg, count 100</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>HRW-GSM100</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9527430001021</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="EA">224</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">6048.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">27</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.</cbc:Description>
        <cbc:Name>Pears Packham's Triumph, carton 18 kg, count 80</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>HRW-PKT080</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="GS1 GTIN">9527430002011</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
