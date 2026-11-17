# Order: Lumeport Textile Mill to Selanu Cotton Ginnery

*Example 8 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

Bales of grade cotton. Delivery terms FOB the island port: the mill arranges the sea freight.

[The XML file](08-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **COTTON-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LTM-PO-26-0198**  
  The buyer's order number.
- `UUID` = **4aa8f3b8-9dcb-52c6-849d-e415d93f4130**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-24**  
  The mill orders the first container of the season.
- `IssueTime` = **10:37:00**  
  The time the sender's system issued the document, in the sender's local time.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `DocumentCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The coral, the seller's currency, in which the seller's prices are; it has three decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `AccountingCostCode` = **2200**  
  The buyer's cost centre, to be quoted on the invoice.
- `AccountingCost` = **Raw cotton**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Textile Mill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-933254** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Textile Mill (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Textile Mill (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's main desk, which handles this document; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2303 2603**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@lumeporttextile.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Textile Mill (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Textile Mill (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Textile Mill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Cotton sales**  
  The party's main desk, which handles this document; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/JobTitle` = **Cotton sales manager**  
  The job of the person who answers at the desk; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 721 2681**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/ElectronicMail` = **cotton@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-03-02**  
  Free on board Selanu: the bales are wanted on board the ship of 2 March.
- `RequestedDeliveryPeriod/EndDate` = **2026-03-02**  
  The last day it is wanted.
- `DeliveryParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Lumeport Textile Mill**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **FOB** (schemeID `INCOTERMS`)  
  Free on board at the port of Selanu: the buyer books and pays the sea freight; the risk passes when the bales are on board. The code is from the world's copy of Incoterms 2020: FOB = Free On Board. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `DeliveryLocation/Description` = **Port of Selanu**  
  Where the delivery terms place the handover of the goods.

### Destination Country

Inside `DestinationCountry`:

- `IdentificationCode` = **XB** (listID `ISO 3166`)  
  The bales go to Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **6055.452** (currencyID `XLC`)  
  The sum of the line amounts.
- `PayableAmount` = **6055.452** (currencyID `XLC`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own (worklist C34).
- `LineItem/Quantity` = **6129** (unitCode `KGM`)  
  27 bales of about 227 kg: one container of lint.
- `LineItem/LineExtensionAmount` = **6055.452** (currencyID `XLC`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **0.988** (currencyID `XLC`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `KGM`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/Description` = **Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `LineItem/Item/PackSizeNumeric` = **227**  
  The units in one pack: 227 kg in a bale; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/Name` = **Tekapa suhema, lafatite senehu** (languageID `qal`)  
  The item's name in Lisavan, the seller's language; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/Name` = **Cotton lint, compressed bale** (languageID `en-XB`)  
  The item's name in English, the working language between the countries; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/BuyersItemIdentification/ID` = **LT-RAW-COT**  
  The number the buyer keeps for this item in its own system (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **SCG-LINT**  
  The seller's own item number; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Where the item was produced; item cotton-bale of Selanu Cotton Ginnery (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `LineItem/Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item cotton-bale of Selanu Cotton Ginnery (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **01921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item cotton-bale of Selanu Cotton Ginnery (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01921 = Cotton, whether or not ginned.
- `LineItem/Item/AdditionalItemProperty/Name` = **Grade**  
  A property buyers ask about.
- `LineItem/Item/AdditionalItemProperty/Value` = **Middling**  
  Its value; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/AdditionalItemProperty/Name` = **Staple length**  
  A measured property of the item.
- `LineItem/Item/AdditionalItemProperty/ValueQuantity` = **28.6** (unitCode `MMT`)  
  Its measured value; item cotton-bale of Selanu Cotton Ginnery (world/items.json).
- `LineItem/Item/OriginAddress/District` = **North coast**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `LineItem/Item/OriginAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `LineItem/Item/Certificate/ID` = **XL-CLS-2026-0042**  
  The number of the certificate, unique only with its issuer, who is named below (decision ID-Q10).
- `LineItem/Item/Certificate/CertificateTypeCode` = **COTTONCLASS** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  The kind of certificate, as a code. The code is from the Trade Accord's certificate type list: COTTONCLASS = Cotton classing.
- `LineItem/Item/Certificate/CertificateType` = **Cotton classing**  
  The name of code COTTONCLASS in the Trade Accord's certificate type list.
- `LineItem/Item/Certificate/Remarks` = **Grade Middling, staple 1-1/8 inch, micronaire 4.2.**  
  What the certificate states about the goods.
- `LineItem/Item/Certificate/IssuerParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Certificate/IssuerParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Certificate/Signature/ID` = **SCC-SIG-2026-0042**  
  The signature's identifier.
- `LineItem/Item/Certificate/Signature/Note` = **Signed by the cotton classer of the chamber.**  
  Who signed.
- `LineItem/Item/Certificate/Signature/ValidationDate` = **2026-02-20**  
  The day the signature was placed.
- `LineItem/Item/Certificate/Signature/SignatoryParty/PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `LineItem/Item/Certificate/Signature/SignatoryParty/PartyName/Name` = **Selanu Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>COTTON-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LTM-PO-26-0198</cbc:ID>
  <cbc:UUID>4aa8f3b8-9dcb-52c6-849d-e415d93f4130</cbc:UUID>
  <cbc:IssueDate>2026-02-24</cbc:IssueDate>
  <cbc:IssueTime>10:37:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>2200</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw cotton</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
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
        <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38504</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 2 38 2303 2603</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@lumeporttextile.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
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
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
        <cbc:BuildingNumber>42</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Cotton sales</cbc:Name>
        <cbc:JobTitle>Cotton sales manager</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 721 2681</cbc:Telephone>
        <cbc:ElectronicMail>cotton@selanuginnery.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
  </cac:FreightForwarderParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-03-02</cbc:StartDate>
      <cbc:EndDate>2026-03-02</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">FOB</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
      <cbc:Description>Port of Selanu</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:DestinationCountry>
    <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
  </cac:DestinationCountry>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">6055.452</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XLC">6055.452</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="KGM">6129</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XLC">6055.452</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XLC">0.988</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="KGM">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description languageID="qal">Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.</cbc:Description>
        <cbc:Description languageID="en-XB">Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.</cbc:Description>
        <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
        <cbc:PackSizeNumeric>227</cbc:PackSizeNumeric>
        <cbc:Name languageID="qal">Tekapa suhema, lafatite senehu</cbc:Name>
        <cbc:Name languageID="en-XB">Cotton lint, compressed bale</cbc:Name>
        <cac:BuyersItemIdentification>
          <cbc:ID>LT-RAW-COT</cbc:ID>
        </cac:BuyersItemIdentification>
        <cac:SellersItemIdentification>
          <cbc:ID>SCG-LINT</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">520100</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01921</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Grade</cbc:Name>
          <cbc:Value>Middling</cbc:Value>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Staple length</cbc:Name>
          <cbc:ValueQuantity unitCode="MMT">28.6</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:OriginAddress>
          <cbc:District>North coast</cbc:District>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
        <cac:Certificate>
          <cbc:ID>XL-CLS-2026-0042</cbc:ID>
          <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">COTTONCLASS</cbc:CertificateTypeCode>
          <cbc:CertificateType>Cotton classing</cbc:CertificateType>
          <cbc:Remarks>Grade Middling, staple 1-1/8 inch, micronaire 4.2.</cbc:Remarks>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
          <cac:Signature>
            <cbc:ID>SCC-SIG-2026-0042</cbc:ID>
            <cbc:Note>Signed by the cotton classer of the chamber.</cbc:Note>
            <cbc:ValidationDate>2026-02-20</cbc:ValidationDate>
            <cac:SignatoryParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
              </cac:PartyName>
            </cac:SignatoryParty>
          </cac:Signature>
        </cac:Certificate>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
