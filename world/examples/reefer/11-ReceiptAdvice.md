# Receipt Advice: Hafefo Fresh Produce to Harrowmead Fruit Growers

*Example 11 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Receipt Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-RECEIPT-ADVICE-SCHEMA)*

The wholesaler confirms what it unloaded at its cold store, with the temperatures read from the reefer's log and measured in the fruit.

[The XML file](11-ReceiptAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:receipt-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Receipt advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0214**  
  The collaboration this document belongs to: Hafefo's order of fruit from Harrowmead Fruit Growers. Hafefo Fresh Produce started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0256**  
  The receiving party's number.
- `UUID` = **9f7f7391-8c4f-53d4-8fbc-38ab9c087873**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-27**  
  The wholesaler confirms what it unloaded on the Monday morning.
- `IssueTime` = **09:27:00+00:00**  
  On the Monday morning, once the fruit is counted; in the issuer's local time, with its offset from UTC.
- `ReceiptAdviceTypeCode` = **Actual** (listID `urn:oasis:names:specification:ubl:codelist:gc:ReceiptAdviceTypeCode`)  
  UBL's receipt advice type code: the goods actually received. The code is from the world's copy of UBL's Receipt advice type list, with a listID: Actual = An arrival that has passed goods inspection and is accepted (or not)..
- `DeliveryAcceptanceCode` = **ACCEPTED** (listID `urn:ubl-examples:world:codelist:DeliveryAcceptanceCode`)  
  All goods accepted. The code is from the Trade Accord's delivery acceptance list: ACCEPTED = All accepted.
- `Note` = **Unloaded at our cold store and counted, the mix of your order response: five pallets of Granny Smith and three of pears. The reefer's log read at the door: the supply air stayed between 0.2 and 0.9 °C from loading to unloading.**  
  How the fruit was received: the wholesaler takes the changed mix it agreed to, and the cold chain as the log shows it.
- `LineCountNumeric` = **3**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **26-0215**  
  The order the goods were delivered for.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **HRW-DA-26-0764**  
  The despatch advice this receipt answers.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

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
- `Party/Contact/Name` = **Cold store**  
  The party's cold store desk: the desk for its role in this document (it receives the goods); as Hafefo Fresh Produce gives it.
- `Party/Contact/JobTitle` = **Cold store supervisor**  
  The job of the person who answers at the desk; as Hafefo Fresh Produce gives it.
- `Party/Contact/Department` = **Cold store**  
  The department the desk belongs to; as Hafefo Fresh Produce gives it.
- `Party/Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Hafefo Fresh Produce gives it.
- `Party/Contact/ElectronicMail` = **coldstore@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Hafefo Fresh Produce gives it.
- `Party/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; as Hafefo Fresh Produce gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC43529** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Hafefo Fresh Produce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

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
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Harrowmead Fruit Growers gives it.
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Department` = **Packhouse**  
  The department the desk belongs to; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Telephone` = **+999 2 7164 281 590**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Harrowmead Fruit Growers gives it.
- `Party/Contact/ElectronicMail` = **dispatch@harrowmeadfruit.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Harrowmead Fruit Growers gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Harrowmead Fruit Growers gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20415873** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Harrowmead Fruit Growers gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receipt Line

Inside `ReceiptLine`:

- `ID` = **1**  
  The line number.
- `Note` = **Received as despatched.**  
  The line in words.
- `ReceivedQuantity` = **672** (unitCode `EA`)  
  Counted at the goods-in and found as announced.
- `ReceivedDate` = **2026-04-27**  
  Unloaded.
- `OrderLineReference/LineID` = **1**  
  The order line.
- `DespatchLineReference/LineID` = **1**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **HRW-DA-26-0764**  
  The despatch advice.
- `DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: HRW-DA-26-0764 is the example reefer/06, a DespatchAdvice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `Item/Description` = **Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.**  
  The seller's description.
- `Item/Name` = **Apples Gala, carton 18 kg, count 100**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **HRW-GAL100**  
  The seller's own item number; as Harrowmead Fruit Growers describes the item.
- `Item/StandardItemIdentification/ID` = **9527430001014** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers'.
- `Shipment/ID` = **HRW-SH-26-0730**  
  The shipment the fruit came in.
- `Shipment/GoodsItem/ID` = **1**  
  The fruit of this line.
- `Shipment/GoodsItem/Temperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the fruit itself, its pulp. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Temperature/Measure` = **0.8** (unitCode `CEL`)  
  The pulp temperature measured in a sample of the cartons at unloading: within the range.
- `ID` = **2**  
  The line number.
- `Note` = **Received as despatched.**  
  The line in words.
- `ReceivedQuantity` = **280** (unitCode `EA`)  
  Counted at the goods-in and found as announced.
- `ReceivedDate` = **2026-04-27**  
  Unloaded.
- `OrderLineReference/LineID` = **2**  
  The order line.
- `DespatchLineReference/LineID` = **2**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **HRW-DA-26-0764**  
  The despatch advice.
- `DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: HRW-DA-26-0764 is the example reefer/06, a DespatchAdvice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `Item/Description` = **Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.**  
  The seller's description.
- `Item/Name` = **Apples Granny Smith, carton 18 kg, count 100**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **HRW-GSM100**  
  The seller's own item number; as Harrowmead Fruit Growers describes the item.
- `Item/StandardItemIdentification/ID` = **9527430001021** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers'.
- `Shipment/ID` = **HRW-SH-26-0730**  
  The shipment the fruit came in.
- `Shipment/GoodsItem/ID` = **1**  
  The fruit of this line.
- `Shipment/GoodsItem/Temperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the fruit itself, its pulp. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Temperature/Measure` = **0.7** (unitCode `CEL`)  
  The pulp temperature measured in a sample of the cartons at unloading: within the range.
- `ID` = **3**  
  The line number.
- `Note` = **Received as despatched.**  
  The line in words.
- `ReceivedQuantity` = **168** (unitCode `EA`)  
  Counted at the goods-in and found as announced.
- `ReceivedDate` = **2026-04-27**  
  Unloaded.
- `OrderLineReference/LineID` = **3**  
  The order line.
- `DespatchLineReference/LineID` = **3**  
  The despatch line.
- `DespatchLineReference/DocumentReference/ID` = **HRW-DA-26-0764**  
  The despatch advice.
- `DespatchLineReference/DocumentReference/DocumentTypeCode` = **DespatchAdvice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: HRW-DA-26-0764 is the example reefer/06, a DespatchAdvice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: DespatchAdvice = Despatch Advice.
- `Item/Description` = **Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.**  
  The seller's description.
- `Item/Name` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **HRW-PKT080**  
  The seller's own item number; as Harrowmead Fruit Growers describes the item.
- `Item/StandardItemIdentification/ID` = **9527430002011** (schemeID `GS1 GTIN`)  
  The GTIN Harrowmead Fruit Growers gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; under GS1 rules the brand owner numbers the item, and the brand Harrowmead is Harrowmead Fruit Growers'.
- `Shipment/ID` = **HRW-SH-26-0730**  
  The shipment the fruit came in.
- `Shipment/GoodsItem/ID` = **1**  
  The fruit of this line.
- `Shipment/GoodsItem/Temperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the fruit itself, its pulp. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Temperature/Measure` = **0.6** (unitCode `CEL`)  
  The pulp temperature measured in a sample of the cartons at unloading: within the range.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ReceiptAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:ReceiptAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:receipt-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0214</cbc:ProfileExecutionID>
  <cbc:ID>26-0256</cbc:ID>
  <cbc:UUID>9f7f7391-8c4f-53d4-8fbc-38ab9c087873</cbc:UUID>
  <cbc:IssueDate>2026-04-27</cbc:IssueDate>
  <cbc:IssueTime>09:27:00+00:00</cbc:IssueTime>
  <cbc:ReceiptAdviceTypeCode listID="urn:oasis:names:specification:ubl:codelist:gc:ReceiptAdviceTypeCode">Actual</cbc:ReceiptAdviceTypeCode>
  <cbc:DeliveryAcceptanceCode listID="urn:ubl-examples:world:codelist:DeliveryAcceptanceCode">ACCEPTED</cbc:DeliveryAcceptanceCode>
  <cbc:Note>Unloaded at our cold store and counted, the mix of your order response: five pallets of Granny Smith and three of pears. The reefer's log read at the door: the supply air stayed between 0.2 and 0.9 °C from loading to unloading.</cbc:Note>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>26-0215</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>HRW-DA-26-0764</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:DeliveryCustomerParty>
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
        <cbc:Name>Cold store</cbc:Name>
        <cbc:JobTitle>Cold store supervisor</cbc:JobTitle>
        <cbc:Department>Cold store</cbc:Department>
        <cbc:Telephone>+999 3 726 8104</cbc:Telephone>
        <cbc:ElectronicMail>coldstore@hafefo.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 05:00–14:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC43529</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:DespatchSupplierParty>
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
        <cbc:Name>Dispatch office</cbc:Name>
        <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
        <cbc:Department>Packhouse</cbc:Department>
        <cbc:Telephone>+999 2 7164 281 590</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@harrowmeadfruit.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20415873</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:ReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Received as despatched.</cbc:Note>
    <cbc:ReceivedQuantity unitCode="EA">672</cbc:ReceivedQuantity>
    <cbc:ReceivedDate>2026-04-27</cbc:ReceivedDate>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>1</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>HRW-DA-26-0764</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
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
    <cac:Shipment>
      <cbc:ID>HRW-SH-26-0730</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cac:Temperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">0.8</cbc:Measure>
        </cac:Temperature>
      </cac:GoodsItem>
    </cac:Shipment>
  </cac:ReceiptLine>
  <cac:ReceiptLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Received as despatched.</cbc:Note>
    <cbc:ReceivedQuantity unitCode="EA">280</cbc:ReceivedQuantity>
    <cbc:ReceivedDate>2026-04-27</cbc:ReceivedDate>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>2</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>HRW-DA-26-0764</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
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
    <cac:Shipment>
      <cbc:ID>HRW-SH-26-0730</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cac:Temperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">0.7</cbc:Measure>
        </cac:Temperature>
      </cac:GoodsItem>
    </cac:Shipment>
  </cac:ReceiptLine>
  <cac:ReceiptLine>
    <cbc:ID>3</cbc:ID>
    <cbc:Note>Received as despatched.</cbc:Note>
    <cbc:ReceivedQuantity unitCode="EA">168</cbc:ReceivedQuantity>
    <cbc:ReceivedDate>2026-04-27</cbc:ReceivedDate>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
    <cac:DespatchLineReference>
      <cbc:LineID>3</cbc:LineID>
      <cac:DocumentReference>
        <cbc:ID>HRW-DA-26-0764</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">DespatchAdvice</cbc:DocumentTypeCode>
      </cac:DocumentReference>
    </cac:DespatchLineReference>
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
    <cac:Shipment>
      <cbc:ID>HRW-SH-26-0730</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cac:Temperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">0.6</cbc:Measure>
        </cac:Temperature>
      </cac:GoodsItem>
    </cac:Shipment>
  </cac:ReceiptLine>
</ReceiptAdvice>
```
