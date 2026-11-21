# Order: Marrowdale Sawmill to Tostara Wood Modification

*Example 1 of the flow "Modification: bench slats modified under contract (Bayvarra → Urvania)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The sawmill orders the processing of one job under the season agreement: 96 bundles of modified, planed and end-sealed slats from its own blanks, which it supplies free of charge.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **MDS-TX-26-0047**  
  The collaboration this document belongs to: the sawmill's order of thermal modification from Tostara. Marrowdale Sawmill started it and gave it this identifier, which every document of it repeats.
- `ID` = **MDS-PO-26-0047**  
  The sawmill's order number.
- `SalesOrderID` = **TWM-J-2526-014**  
  The plant's job number for this order: the season agreement's kiln slots were each given a job number by the plant when they were allotted, before any order, and the order fills the slot it quotes.
- `UUID` = **d47b6f28-2a6c-5241-91f4-d182ad307e94**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-01-12**  
  The Monday the sawmill fills its slot, the day before the first load of blanks leaves.
- `IssueTime` = **09:20:00-01:00**  
  In the morning; in the issuer's local time, with its offset from UTC.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `Note` = **Job for our season stock of park-bench slats: modify, plane, seal the end grain and bundle our blanks; hold the bundles in your store until we call them off. The blanks come on our truck on 13 and 20 January, 2,400 each time.**  
  What is ordered, in a few words, and how the material comes.
- `DocumentCurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The ferra, the plant's currency, in which the season agreement prices; it has no minor unit. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `LineCountNumeric` = **1**  
  One job.

### Contract

Inside `Contract`:

- `ID` = **TWM-SA-2526-MS**  
  The season agreement for kiln slots, October 2025 to March 2026, whose prices and terms the job follows.
- `ContractType` = **Season agreement for kiln slots**  
  What it is.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; as Marrowdale Sawmill gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Marrowdale Sawmill gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Marrowdale Sawmill gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Marrowdale Sawmill gives it.
- `Party/Contact/Telephone` = **+999 2 7121 338 173**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Marrowdale Sawmill gives it.
- `Party/Contact/ElectronicMail` = **purchasing@marrowdalesawmill.example**  
  The contact's e-mail address; as Marrowdale Sawmill gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Marrowdale Sawmill gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Tostara Wood Modification**  
  The trading name; as Tostara Wood Modification gives it.
- `Party/PostalAddress/ID` = **4160205830117402** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Tostara Wood Modification gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Tuntrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Tostara Wood Modification gives it.
- `Party/PostalAddress/StreetName` = **Via delle Concerie** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Tostara Wood Modification gives it.
- `Party/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Tostara Wood Modification gives it.
- `Party/PostalAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `Party/PostalAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `Party/PostalAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Tostara Wood Modification gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Tostara Wood Modification gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; as Tostara Wood Modification gives it.
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Tostara Wood Modification gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Tostara Wood Modification gives it.
- `Party/Contact/Telephone` = **+999 1 041 573 2290**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Tostara Wood Modification gives it.
- `Party/Contact/ElectronicMail` = **sales@tostara.example**  
  The contact's e-mail address; as Tostara Wood Modification gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Tostara Wood Modification gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-106192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `LatestDeliveryDate` = **2026-02-06**  
  The bundles are to be ready in the plant's store by Friday 6 February, the end of the slot the order fills, so that the sawmill has the slats in stock for the orders of the coming quarter.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **EXW** (schemeID `INCOTERMS`)  
  Ex works the plant: the finished bundles are held at the plant and collected there, as the sawmill calls them off. The code is from the world's copy of Incoterms 2020: EXW = Ex Works. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/Description` = **Tostara Wood Modification, Conciaro**  
  Where the delivery terms place the handover.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0** (currencyID `XUF`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **1272000** (currencyID `XUF`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0** (currencyID `XUF`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  A service supplied outside Urvania, to a customer established abroad, is outside the scope of Urvania's value added tax (category O). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **SVCABROAD** (listID `urn:ubl-examples:world:XU:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Urvania's national list, the list of the seller's country. The code is from Urvania's national value added tax exemption reason list: SVCABROAD = Service supplied outside Urvania.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Service supplied outside Urvania**  
  The name of code SVCABROAD in Urvania's national value added tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **1272000** (currencyID `XUF`)  
  The processing of the 96 bundles; storage is billed by the week, as it falls.
- `PayableAmount` = **1272000** (currencyID `XUF`)  
  What the sawmill expects to pay for the processing.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Note` = **96 bundles of 50 slats, our park-bench slat MDS-SL-1800, 1,800 × 95 × 45 mm.**  
  The output the job is to give: the sawmill's own slat, by its number.
- `LineItem/Quantity` = **96** (unitCode `EA`)  
  The bundles to be made: the 4,800 blanks give 4,800 slats.
- `LineItem/LineExtensionAmount` = **1272000** (currencyID `XUF`)  
  Quantity times price.
- `LineItem/Price/PriceAmount` = **13250** (currencyID `XUF`)  
  The season agreement's price for a bundle: modifying 50 of the customer's blanks, planing them to the slat, sealing the end grain and bundling them.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Kruknul sagir skul drek vikkaz hirmek razskir-guzgek darhir hir tekzhek 212 °C trek hunskul, zikdrek rek krukzan krakdaz krir 1800 × 95 × 45 mm, krizbir drek temul zhizvek stan turzul trek rankul skul 50, ginek zhirdul skul nehir.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `LineItem/Item/Description` = **Thermal modification of the customer's own kiln-dried ash at about 212 °C in steam, planing on four sides to 1800 × 95 × 45 mm, sealing the end grain and strapping in bundles of 50, per bundle of output.** (languageID `en-XB`)  
  The seller's description in English, the working language between the countries.
- `LineItem/Item/Name` = **Kruknul sagir stan muldir, zhirdul skul 50 nanskir kalnan** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `LineItem/Item/Name` = **Thermal modification and finishing, bundle of 50 bench slats** (languageID `en-XB`)  
  The item's name in English, the working language between the countries.
- `LineItem/Item/SellersItemIdentification/ID` = **TWM-TM-SL50**  
  The seller's own item number; as Tostara Wood Modification describes the item.
- `LineItem/SubLineItem/ID` = **1.1**  
  The material of the job, a line below the main line.
- `LineItem/SubLineItem/Note` = **Supplied by the customer, free of charge: the sawmill's own kiln-dried ash, which stays its property.**  
  Why the line has no price.
- `LineItem/SubLineItem/Quantity` = **4800** (unitCode `EA`)  
  The blanks that make the 96 bundles, one slat from each.
- `LineItem/SubLineItem/Item/Description` = **Sawn and kiln-dried European ash, 1830 × 101 × 51 mm, a blank for the bench slat MDS-SL-1800 before it is modified and planed.**  
  The seller's description.
- `LineItem/SubLineItem/Item/Name` = **Ash blank 1830, kiln dried**  
  The item's short name.
- `LineItem/SubLineItem/Item/BuyersItemIdentification/ID` = **MDS-BL-1830**  
  The sawmill's own number for its blank: the blank is the material of the buyer of the job, supplied for processing and never sold, so the buyer numbers it.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MDS-TX-26-0047</cbc:ProfileExecutionID>
  <cbc:ID>MDS-PO-26-0047</cbc:ID>
  <cbc:SalesOrderID>TWM-J-2526-014</cbc:SalesOrderID>
  <cbc:UUID>d47b6f28-2a6c-5241-91f4-d182ad307e94</cbc:UUID>
  <cbc:IssueDate>2026-01-12</cbc:IssueDate>
  <cbc:IssueTime>09:20:00-01:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:Note>Job for our season stock of park-bench slats: modify, plane, seal the end grain and bundle our blanks; hold the bundles in your store until we call them off. The blanks come on our truck on 13 and 20 January, 2,400 each time.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XUF</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:Contract>
    <cbc:ID>TWM-SA-2526-MS</cbc:ID>
    <cbc:ContractType>Season agreement for kiln slots</cbc:ContractType>
  </cac:Contract>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Buyer</cbc:JobTitle>
        <cbc:Department>Purchasing</cbc:Department>
        <cbc:Telephone>+999 2 7121 338 173</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tostara Wood Modification</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160205830117402</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Tuntrir</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Concerie</cbc:StreetName>
        <cbc:BuildingNumber>9</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
        <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
        <cbc:PostalZone>4190</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 573 2290</cbc:Telephone>
        <cbc:ElectronicMail>sales@tostara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-106192</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cbc:LatestDeliveryDate>2026-02-06</cbc:LatestDeliveryDate>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">EXW</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>Tostara Wood Modification, Conciaro</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">0</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">1272000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">0</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XU:codelist:TaxExemptionReasonCode">SVCABROAD</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Service supplied outside Urvania</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">1272000</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XUF">1272000</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Note>96 bundles of 50 slats, our park-bench slat MDS-SL-1800, 1,800 × 95 × 45 mm.</cbc:Note>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XUF">1272000</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">13250</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description languageID="qau">Kruknul sagir skul drek vikkaz hirmek razskir-guzgek darhir hir tekzhek 212 °C trek hunskul, zikdrek rek krukzan krakdaz krir 1800 × 95 × 45 mm, krizbir drek temul zhizvek stan turzul trek rankul skul 50, ginek zhirdul skul nehir.</cbc:Description>
        <cbc:Description languageID="en-XB">Thermal modification of the customer's own kiln-dried ash at about 212 °C in steam, planing on four sides to 1800 × 95 × 45 mm, sealing the end grain and strapping in bundles of 50, per bundle of output.</cbc:Description>
        <cbc:Name languageID="qau">Kruknul sagir stan muldir, zhirdul skul 50 nanskir kalnan</cbc:Name>
        <cbc:Name languageID="en-XB">Thermal modification and finishing, bundle of 50 bench slats</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>TWM-TM-SL50</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
      <cac:SubLineItem>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Note>Supplied by the customer, free of charge: the sawmill's own kiln-dried ash, which stays its property.</cbc:Note>
        <cbc:Quantity unitCode="EA">4800</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Sawn and kiln-dried European ash, 1830 × 101 × 51 mm, a blank for the bench slat MDS-SL-1800 before it is modified and planed.</cbc:Description>
          <cbc:Name>Ash blank 1830, kiln dried</cbc:Name>
          <cac:BuyersItemIdentification>
            <cbc:ID>MDS-BL-1830</cbc:ID>
          </cac:BuyersItemIdentification>
        </cac:Item>
      </cac:SubLineItem>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
