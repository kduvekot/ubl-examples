# Order: Quillmoor Pharma Distribution to Nilavar Biologics

*Example 1 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The wholesaler orders its vaccines and insulin for the southern winter from the maker in India, carriage paid to Lumeport airport, in rupees.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **QLM-TX-26-2699**  
  The collaboration this document belongs to: Quillmoor's order of a biological medicine from Nilavar Biologics. Quillmoor Pharma Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **QLM-PO-26-2699**  
  The buyer's order number.
- `UUID` = **237fea2b-a4ab-5769-b113-06c84ecff8e4**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-20**  
  The wholesaler orders the season's vaccines in April, for the southern winter.
- `IssueTime` = **10:20:00-01:00**  
  During the wholesaler's office hours; in the issuer's local time, with its offset from UTC.
- `OrderTypeCode` = **220** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 220: order. The code is from the world's copy of UN/EDIFACT 1001 Document name: 220 = Order.
- `Note` = **Please ship by scheduled air cargo at 2 to 8 °C, the varicella vaccine frozen, to arrive at Lumeport by Monday 11 May; we pay in euro.**  
  What the wholesaler asks.
- `DocumentCurrencyCode` = **INR** (listID `ISO 4217 Alpha`)  
  The indian rupee, the seller's currency, in which the seller's prices are; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: INR = Indian Rupee.
- `LineCountNumeric` = **3**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Quillmoor Pharma Distribution gives it.
- `Party/PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; as Quillmoor Pharma Distribution gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-718264** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/BuildingNumber` = **40**  
  Building number of the postal address. As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Quillmoor Pharma Distribution gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Purchasing**  
  The party's purchasing desk: the desk for its role in this document (it buys); as Quillmoor Pharma Distribution gives it.
- `Party/Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Quillmoor Pharma Distribution gives it.
- `Party/Contact/ElectronicMail` = **purchasing@quillmoor.example**  
  The contact's e-mail address; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Quillmoor Pharma Distribution gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20413425** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyName/Name` = **Nilavar Biologics**  
  The trading name; as Nilavar Biologics, a maker abroad, gives it. The documents identify the maker by its name and address.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/StreetName` = **Biotech Park Road**  
  Street of the postal address. As Nilavar Biologics gives it.
- `Party/PostalAddress/BuildingNumber` = **27**  
  Building number. As Nilavar Biologics gives it.
- `Party/PostalAddress/CityName` = **Hyderabad**  
  The town. As Nilavar Biologics gives it.
- `Party/PostalAddress/PostalZone` = **500078**  
  Postal code in the format of India. As Nilavar Biologics gives it.
- `Party/PostalAddress/CountrySubentity` = **Telangana**  
  The state of India, part of an address there. As Nilavar Biologics gives it.
- `Party/PostalAddress/TimezoneOffset` = **+05:30**  
  The offset from UTC of Indian Standard Time, the legal time there in June.
- `Party/PostalAddress/Country/IdentificationCode` = **IN** (listID `ISO 3166`)  
  India: the maker is abroad. The code is from the world's copy of UBL's Country identification (ISO 3166) list: IN = India.
- `Party/PostalAddress/Country/Name` = **India**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Export sales**  
  The party's desk that handles this document; as Nilavar Biologics, a maker abroad, gives it.
- `Party/Contact/JobTitle` = **Export manager**  
  The job of the person who answers at the desk; as Nilavar Biologics, a maker abroad, gives it.
- `Party/Contact/Department` = **International sales**  
  The department the desk belongs to; as Nilavar Biologics, a maker abroad, gives it.
- `Party/Contact/ElectronicMail` = **exports@nilavar-bio.example**  
  The desk's e-mail address; as Nilavar Biologics, a maker abroad, gives it.
- `Party/Contact/Note` = **Monday to Saturday 09:30–18:00**  
  When the desk can be reached; as Nilavar Biologics, a maker abroad, gives it.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-05-11**  
  The vaccines and the insulin are wanted at Lumeport airport on Monday 11 May, six weeks before the island's influenza campaign.
- `RequestedDeliveryPeriod/EndDate` = **2026-05-11**  
  The last day it is wanted.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CPT** (schemeID `INCOTERMS`)  
  Carriage paid to Lumeport airport: the maker books the scheduled air cargo from Hyderabad; the wholesaler clears the import. The code is from the world's copy of Incoterms 2020: CPT = Carriage Paid To. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `DeliveryLocation/Description` = **Lumeport airport, cargo terminal**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `INR`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **4050000.00** (currencyID `INR`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `INR`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export of goods is a zero-rated supply under India's integrated goods and services tax (IGST Act 2017, section 16): no tax is charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Zero-rated export supply**  
  Why no tax is charged, stated rather than left out.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **GST** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: goods and services tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: GST = Goods and services tax. An identifier that holds a code names the code's list in its schemeID.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **4050000.00** (currencyID `INR`)  
  The sum of the line amounts.
- `PayableAmount` = **4050000.00** (currencyID `INR`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **600** (unitCode `EA`)  
  6,000 doses for the southern winter: the island hospital's 3,000 and the pharmacies of Bayvarra.
- `LineItem/LineExtensionAmount` = **2460000.00** (currencyID `INR`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **4100** (currencyID `INR`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `LineItem/Item/Name` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **QLM-VAC-1102**  
  The buyer's own item number: it resells this item under its own number.
- `LineItem/Item/SellersItemIdentification/ID` = **NLB-FLU-S26-10**  
  The seller's own item number; as Nilavar Biologics describes the item.
- `LineItem/ID` = **2**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **960** (unitCode `EA`)  
  Four months of insulin for the wholesaler's customers.
- `LineItem/LineExtensionAmount` = **1248000.00** (currencyID `INR`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **1300** (currencyID `INR`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `LineItem/Item/Name` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **QLM-INS-0310**  
  The buyer's own item number: it resells this item under its own number.
- `LineItem/Item/SellersItemIdentification/ID` = **NLB-INS-R100-10**  
  The seller's own item number; as Nilavar Biologics describes the item.
- `LineItem/ID` = **3**  
  The line number: a line added by a change keeps a number of its own.
- `LineItem/Quantity` = **120** (unitCode `EA`)  
  The season's varicella vaccine for three hospitals.
- `LineItem/LineExtensionAmount` = **342000.00** (currencyID `INR`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **2850** (currencyID `INR`)  
  The seller's price per unit.
- `LineItem/Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.**  
  The seller's description.
- `LineItem/Item/Name` = **Varicella vaccine, live, frozen, single dose**  
  The item's short name.
- `LineItem/Item/BuyersItemIdentification/ID` = **QLM-VAC-2410**  
  The buyer's own item number: it resells this item under its own number.
- `LineItem/Item/SellersItemIdentification/ID` = **NLB-VZV-1**  
  The seller's own item number; as Nilavar Biologics describes the item.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>QLM-TX-26-2699</cbc:ProfileExecutionID>
  <cbc:ID>QLM-PO-26-2699</cbc:ID>
  <cbc:UUID>237fea2b-a4ab-5769-b113-06c84ecff8e4</cbc:UUID>
  <cbc:IssueDate>2026-04-20</cbc:IssueDate>
  <cbc:IssueTime>10:20:00-01:00</cbc:IssueTime>
  <cbc:OrderTypeCode listID="UN/EDIFACT EDED 1001">220</cbc:OrderTypeCode>
  <cbc:Note>Please ship by scheduled air cargo at 2 to 8 °C, the varicella vaccine frozen, to arrive at Lumeport by Monday 11 May; we pay in euro.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">INR</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9524910900003</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-718264</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Airport Road</cbc:StreetName>
        <cbc:BuildingNumber>40</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38528</cbc:PostalZone>
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
        <cbc:Telephone>+999 2 38 6047 1582</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@quillmoor.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20413425</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Nilavar Biologics</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:StreetName>Biotech Park Road</cbc:StreetName>
        <cbc:BuildingNumber>27</cbc:BuildingNumber>
        <cbc:CityName>Hyderabad</cbc:CityName>
        <cbc:PostalZone>500078</cbc:PostalZone>
        <cbc:CountrySubentity>Telangana</cbc:CountrySubentity>
        <cbc:TimezoneOffset>+05:30</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">IN</cbc:IdentificationCode>
          <cbc:Name>India</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Export sales</cbc:Name>
        <cbc:JobTitle>Export manager</cbc:JobTitle>
        <cbc:Department>International sales</cbc:Department>
        <cbc:ElectronicMail>exports@nilavar-bio.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:30–18:00</cbc:Note>
      </cac:Contact>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-05-11</cbc:StartDate>
      <cbc:EndDate>2026-05-11</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CPT</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
      <cbc:Description>Lumeport airport, cargo terminal</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="INR">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="INR">4050000.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="INR">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Zero-rated export supply</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">GST</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="INR">4050000.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="INR">4050000.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">600</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="INR">2460000.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="INR">4100</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.</cbc:Description>
        <cbc:Name>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Name>
        <cac:BuyersItemIdentification>
          <cbc:ID>QLM-VAC-1102</cbc:ID>
        </cac:BuyersItemIdentification>
        <cac:SellersItemIdentification>
          <cbc:ID>NLB-FLU-S26-10</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="EA">960</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="INR">1248000.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="INR">1300</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.</cbc:Description>
        <cbc:Name>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Name>
        <cac:BuyersItemIdentification>
          <cbc:ID>QLM-INS-0310</cbc:ID>
        </cac:BuyersItemIdentification>
        <cac:SellersItemIdentification>
          <cbc:ID>NLB-INS-R100-10</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="EA">120</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="INR">342000.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="INR">2850</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.</cbc:Description>
        <cbc:Name>Varicella vaccine, live, frozen, single dose</cbc:Name>
        <cac:BuyersItemIdentification>
          <cbc:ID>QLM-VAC-2410</cbc:ID>
        </cac:BuyersItemIdentification>
        <cac:SellersItemIdentification>
          <cbc:ID>NLB-VZV-1</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
