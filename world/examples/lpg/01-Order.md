# Order: Coastal State Water Company to Kelpstone Gas

*Example 1 of the flow "Propane by road tanker to Lumeport's district heating (dangerous goods, domestic, Bayvarra)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The water company orders a tanker load of propane for the peak boilers of its district heating, delivered into its storage tank in Lumeport.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9924528384**  
  The collaboration this document belongs to: the water company's order of liquefied petroleum gas from Kelpstone. Coastal State Water Company started it and gave it this identifier, which every document of it repeats.
- `ID` = **4500028302**  
  The buyer's order number.
- `UUID` = **9ce589ee-2c67-5bed-bd7f-25588d33a18c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-08**  
  Ordered when the storage reading of Monday morning showed a third left.
- `IssueTime` = **09:47:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **1**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Coastal State Water Company**  
  The trading name; as Coastal State Water Company gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-782593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Coastal State Water Company gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. As Coastal State Water Company gives it.
- `Party/PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. As Coastal State Water Company gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Coastal State Water Company gives it.
- `Party/PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). As Coastal State Water Company gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Coastal State Water Company gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Coastal State Water Company gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Coastal State Water Company gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Coastal State Water Company gives it.
- `Party/Contact/Telephone` = **+999 2 38 9310 7518**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Coastal State Water Company gives it.
- `Party/Contact/ElectronicMail` = **purchasing@coastalwater.example**  
  The contact's e-mail address; as Coastal State Water Company gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Coastal State Water Company gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Kelpstone Gas gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **0990:19676** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Kelpstone Gas gives it.
- `Party/PartyName/Name` = **Kelpstone Gas**  
  The trading name; as Kelpstone Gas gives it.
- `Party/PostalAddress/ID` = **NT-ADR-587853** (schemeID `urn:ubl-examples:world:XB:NT:address-register`)  
  The address's number in the address register of Northern Territory (NT-ADR- and six digits); as Kelpstone Gas gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Shoreline Road**  
  Street of the postal address. As Kelpstone Gas gives it.
- `Party/PostalAddress/BuildingNumber` = **2**  
  Building number of the postal address. As Kelpstone Gas gives it.
- `Party/PostalAddress/CityName` = **Gullhaven**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Kelpstone Gas gives it.
- `Party/PostalAddress/PostalZone` = **90540**  
  Postal code in Bayvarra's format (5 digits). As Kelpstone Gas gives it.
- `Party/PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Kelpstone Gas gives it. The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PhysicalLocation/Description` = **Gas treatment plant on the north coast; the platform of the offshore field lies about 80 kilometres out.**  
  Where the party actually operates, apart from its postal address. The distance is measured along the route on the map, rounded to 10 km.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **28** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **15.95** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **33.76** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Party/Contact/Name` = **Gas sales**  
  The party's main desk, which handles this document; as Kelpstone Gas gives it.
- `Party/Contact/JobTitle` = **Gas sales manager**  
  The job of the person who answers at the desk; as Kelpstone Gas gives it.
- `Party/Contact/Department` = **Commercial**  
  The department the desk belongs to; as Kelpstone Gas gives it.
- `Party/Contact/Telephone` = **+999 2 1563 683 300**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Kelpstone Gas gives it.
- `Party/Contact/ElectronicMail` = **gas@kelpstone.example**  
  The contact's e-mail address; as Kelpstone Gas gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Kelpstone Gas gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412877** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Kelpstone Gas gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-06-10**  
  The propane is wanted on Wednesday 10 June, before the cold weekend the forecast gives.
- `RequestedDeliveryPeriod/EndDate` = **2026-06-10**  
  The last day it is wanted.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **DPU** (schemeID `INCOTERMS`)  
  Delivered at place unloaded: Kelpstone has the propane carried and pumped into the water company's storage tank. The code is from the world's copy of Incoterms 2020: DPU = Delivered at Place Unloaded. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/Description` = **Into the propane storage of the district heating plant, Reservoir Road, Lumeport**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **728.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **11200.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **728.00** (currencyID `XBL`)  
  6.5 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  Goods a business uses up or keeps, such as the fuel it burns, are not bought for resale or manufacture: they do not become part of what it sells, so Bayvarra's retail sales tax applies to their sale, at the rate of Coastal State, where the goods are delivered (category S). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **11200.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **11928.00** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **20** (unitCode `TNE`)  
  A full tanker load, about 20 tonnes: the storage at the boiler house is down to a third in the cold spell, and one load fills it again.
- `LineItem/LineExtensionAmount` = **11200.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **560** (currencyID `XBL`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Commercial propane separated from the field's gas at the Gullhaven plant and liquefied under pressure, hydrocarbon gas mixture C; sold by the tonne, weighed on the plant's weighbridge, and delivered by road tanker.**  
  The seller's description.
- `LineItem/Item/Name` = **Propane, commercial**  
  The item's short name.
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **KG-LPG**  
  The seller's own item number; as Kelpstone Gas describes the item.
- `LineItem/Item/StandardItemIdentification/ID` = **KXU19676LPG** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Kelpstone Gas gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Kelpstone Gas and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; as Kelpstone Gas describes the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9924528384</cbc:ProfileExecutionID>
  <cbc:ID>4500028302</cbc:ID>
  <cbc:UUID>9ce589ee-2c67-5bed-bd7f-25588d33a18c</cbc:UUID>
  <cbc:IssueDate>2026-06-08</cbc:IssueDate>
  <cbc:IssueTime>09:47:00-01:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-782593</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Reservoir Road</cbc:StreetName>
        <cbc:BuildingNumber>51</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38500</cbc:PostalZone>
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
        <cbc:Telephone>+999 2 38 9310 7518</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@coastalwater.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:19676</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelpstone Gas</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:NT:address-register">NT-ADR-587853</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Shoreline Road</cbc:StreetName>
        <cbc:BuildingNumber>2</cbc:BuildingNumber>
        <cbc:CityName>Gullhaven</cbc:CityName>
        <cbc:PostalZone>90540</cbc:PostalZone>
        <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-NT</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:Description>Gas treatment plant on the north coast; the platform of the offshore field lies about 80 kilometres out.</cbc:Description>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">28</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">15.95</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">33.76</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:Contact>
        <cbc:Name>Gas sales</cbc:Name>
        <cbc:JobTitle>Gas sales manager</cbc:JobTitle>
        <cbc:Department>Commercial</cbc:Department>
        <cbc:Telephone>+999 2 1563 683 300</cbc:Telephone>
        <cbc:ElectronicMail>gas@kelpstone.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412877</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-06-10</cbc:StartDate>
      <cbc:EndDate>2026-06-10</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">DPU</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>Into the propane storage of the district heating plant, Reservoir Road, Lumeport</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">728.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">11200.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">728.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">11200.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">11928.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="TNE">20</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">11200.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">560</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Commercial propane separated from the field's gas at the Gullhaven plant and liquefied under pressure, hydrocarbon gas mixture C; sold by the tonne, weighed on the plant's weighbridge, and delivered by road tanker.</cbc:Description>
        <cbc:Name>Propane, commercial</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>KG-LPG</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="ISO 15459-6">KXU19676LPG</cbc:ID>
        </cac:StandardItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
