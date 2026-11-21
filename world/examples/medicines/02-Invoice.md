# Invoice: Nilavar Biologics to Quillmoor Pharma Distribution

*Example 2 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The Indian maker invoices the vaccines and the insulin in rupees when they leave Hyderabad; an export, zero-rated in India.

[The XML file](02-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Invoice/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Billing". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **QLM-TX-26-2699**  
  The collaboration this document belongs to: Quillmoor's order of a biological medicine from Nilavar Biologics. Quillmoor Pharma Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **NLB-INV-26-1732**  
  The maker's invoice number.
- `UUID` = **2508e7e3-8979-5015-9f6c-23e390dec466**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-07**  
  Issued when the goods left for Hyderabad airport.
- `IssueTime` = **09:45:00+05:30**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `DueDate` = **2026-06-08**  
  30 days from Thursday 7 May end on Saturday 6 June, no business day in India for a bank transfer abroad, so the payment is due on Monday 8 June.
- `InvoiceTypeCode` = **380** (listID `UN/EDIFACT EDED 1001`)  
  A commercial invoice, as UN/EDIFACT 1001 codes it. The code is from the world's copy of UN/EDIFACT 1001 Document name: 380 = Commercial invoice.
- `Note` = **Payable in euro: 4,050,000.00 rupees at 88.8595 rupees per euro, 45,577.57 euro.**  
  The amount to pay in the payment currency.
- `DocumentCurrencyCode` = **INR** (listID `ISO 4217 Alpha`)  
  The indian rupee, the maker's currency; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: INR = Indian Rupee.
- `PaymentCurrencyCode` = **EUR** (listID `ISO 4217 Alpha`)  
  Payment is asked in euro, the currency the wholesaler pays its suppliers abroad in, at the day's rate: a trade outside the Accord. The code is from the world's copy of UBL's Currency (ISO 4217) list: EUR = Euro.
- `LineCountNumeric` = **3**  
  The number of invoice lines.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  English, the language of the maker's export invoices. The code is from the world's copy of ISO 639 Language: en = English.

### Order Reference

Inside `OrderReference`:

- `ID` = **QLM-PO-26-2699**  
  The wholesaler's order.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

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
- `Party/PartyLegalEntity/RegistrationName` = **Nilavar Biologics Private Limited**  
  The company's registered name, with the legal form of its country; as Nilavar Biologics, a maker abroad, gives it.
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

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Quillmoor Pharma Distribution gives it.
- `Party/PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; as Quillmoor Pharma Distribution gives it.
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
- `Party/PartyLegalEntity/RegistrationName` = **Quillmoor Pharma Distribution Ltd**  
  The name under which the party is registered, with its legal form; as Quillmoor Pharma Distribution gives it.
- `Party/PartyLegalEntity/CompanyID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); as Quillmoor Pharma Distribution gives it.
- `Party/Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Department` = **Finance**  
  The department the desk belongs to; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Quillmoor Pharma Distribution gives it.
- `Party/Contact/ElectronicMail` = **payables@quillmoor.example**  
  The contact's e-mail address; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Quillmoor Pharma Distribution gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20413425** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Quillmoor Pharma Distribution**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyName/Name` = **Nilavar Biologics**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery

Inside `Delivery`:

- `DeliveryLocation/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `DeliveryLocation/Name` = **Lumeport airport**  
  Where they are delivered: Lumeport airport.
- `DeliveryLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Despatch/ActualDespatchDate` = **2026-05-07**  
  The goods left the maker's cold store for the airport.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CPT** (schemeID `INCOTERMS`)  
  Incoterms 2020: carriage paid to Lumeport airport; the buyer clears the import. The code is from the world's copy of Incoterms 2020: CPT = Carriage Paid To. An identifier that holds a code names the code's list in its schemeID.
- `DeliveryLocation/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `DeliveryLocation/Name` = **Lumeport airport**  
  The named place: Lumeport airport.
- `DeliveryLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **30 days net; payment in euro at the ECB's euro reference rate of the invoice date.**  
  The maker's terms for export customers, as the order accepted them: 30 days from the invoice.
- `PaymentDueDate` = **2026-06-08**  
  As the due date above.

### Payment Exchange Rate

Inside `PaymentExchangeRate`:

- `SourceCurrencyCode` = **INR** (listID `ISO 4217 Alpha`)  
  The invoice's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: INR = Indian Rupee.
- `TargetCurrencyCode` = **EUR** (listID `ISO 4217 Alpha`)  
  The payment currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: EUR = Euro.
- `CalculationRate` = **88.8595**  
  The ECB's euro reference rate of the invoice date, Thursday 7 May: 88.8595 rupees for a euro, the rate that also underlies the Lumeport Exchange's fixing.
- `MathematicOperatorCode` = **Divide** (listID `urn:oasis:names:specification:ubl:codelist:gc:OperatorCode`)  
  The rupee amount divided by the rate gives the euro amount, as the ECB quotes rupees per euro. The code is from the world's copy of UBL's Operator list, with a listID: Divide.
- `Date` = **2026-05-07**  
  The day of the rate.

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

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **4050000.00** (currencyID `INR`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **4050000.00** (currencyID `INR`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **4050000.00** (currencyID `INR`)  
  The total without tax plus the tax.
- `PayableAmount` = **4050000.00** (currencyID `INR`)  
  What the buyer is to pay, stated in full so that it books the amount without working it out.

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **600** (unitCode `EA`)  
  The quantity shipped.
- `LineExtensionAmount` = **2460000.00** (currencyID `INR`)  
  600 × 4100.0, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **1**  
  The line of the wholesaler's order.
- `Item/Description` = **Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `Item/Name` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **NLB-FLU-S26-10**  
  The seller's own item number; as Nilavar Biologics describes the item.
- `Item/ClassifiedTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export of goods is a zero-rated supply under India's integrated goods and services tax (IGST Act 2017, section 16): no tax is charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Zero-rated export supply**  
  Why no tax is charged, stated rather than left out.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **GST** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: goods and services tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: GST = Goods and services tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **4100** (currencyID `INR`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `ID` = **2**  
  The line number.
- `InvoicedQuantity` = **960** (unitCode `EA`)  
  The quantity shipped.
- `LineExtensionAmount` = **1248000.00** (currencyID `INR`)  
  960 × 1300.0, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **2**  
  The line of the wholesaler's order.
- `Item/Description` = **Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `Item/Name` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **NLB-INS-R100-10**  
  The seller's own item number; as Nilavar Biologics describes the item.
- `Item/ClassifiedTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export of goods is a zero-rated supply under India's integrated goods and services tax (IGST Act 2017, section 16): no tax is charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Zero-rated export supply**  
  Why no tax is charged, stated rather than left out.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **GST** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: goods and services tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: GST = Goods and services tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **1300** (currencyID `INR`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.
- `ID` = **3**  
  The line number.
- `InvoicedQuantity` = **120** (unitCode `EA`)  
  The quantity shipped.
- `LineExtensionAmount` = **342000.00** (currencyID `INR`)  
  120 × 2850.0, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **3**  
  The line of the wholesaler's order.
- `Item/Description` = **Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.**  
  The seller's description.
- `Item/Name` = **Varicella vaccine, live, frozen, single dose**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **NLB-VZV-1**  
  The seller's own item number; as Nilavar Biologics describes the item.
- `Item/ClassifiedTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  An export of goods is a zero-rated supply under India's integrated goods and services tax (IGST Act 2017, section 16): no tax is charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Zero-rated export supply**  
  Why no tax is charged, stated rather than left out.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **GST** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: goods and services tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: GST = Goods and services tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **2850** (currencyID `INR`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `EA`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>QLM-TX-26-2699</cbc:ProfileExecutionID>
  <cbc:ID>NLB-INV-26-1732</cbc:ID>
  <cbc:UUID>2508e7e3-8979-5015-9f6c-23e390dec466</cbc:UUID>
  <cbc:IssueDate>2026-05-07</cbc:IssueDate>
  <cbc:IssueTime>09:45:00+05:30</cbc:IssueTime>
  <cbc:DueDate>2026-06-08</cbc:DueDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">380</cbc:InvoiceTypeCode>
  <cbc:Note>Payable in euro: 4,050,000.00 rupees at 88.8595 rupees per euro, 45,577.57 euro.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">INR</cbc:DocumentCurrencyCode>
  <cbc:PaymentCurrencyCode listID="ISO 4217 Alpha">EUR</cbc:PaymentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:OrderReference>
    <cbc:ID>QLM-PO-26-2699</cbc:ID>
  </cac:OrderReference>
  <cac:AccountingSupplierParty>
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
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Nilavar Biologics Private Limited</cbc:RegistrationName>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Export sales</cbc:Name>
        <cbc:JobTitle>Export manager</cbc:JobTitle>
        <cbc:Department>International sales</cbc:Department>
        <cbc:ElectronicMail>exports@nilavar-bio.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:30–18:00</cbc:Note>
      </cac:Contact>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
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
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Quillmoor Pharma Distribution Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Accounts payable</cbc:Name>
        <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
        <cbc:Department>Finance</cbc:Department>
        <cbc:Telephone>+999 2 38 6047 1582</cbc:Telephone>
        <cbc:ElectronicMail>payables@quillmoor.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20413425</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Nilavar Biologics</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
      <cbc:Name>Lumeport airport</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:DeliveryLocation>
    <cac:Despatch>
      <cbc:ActualDespatchDate>2026-05-07</cbc:ActualDespatchDate>
    </cac:Despatch>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CPT</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
      <cbc:Name>Lumeport airport</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:PaymentTerms>
    <cbc:Note>30 days net; payment in euro at the ECB's euro reference rate of the invoice date.</cbc:Note>
    <cbc:PaymentDueDate>2026-06-08</cbc:PaymentDueDate>
  </cac:PaymentTerms>
  <cac:PaymentExchangeRate>
    <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">INR</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">EUR</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>88.8595</cbc:CalculationRate>
    <cbc:MathematicOperatorCode listID="urn:oasis:names:specification:ubl:codelist:gc:OperatorCode">Divide</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-07</cbc:Date>
  </cac:PaymentExchangeRate>
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
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="INR">4050000.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="INR">4050000.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="INR">4050000.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="INR">4050000.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="EA">600</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="INR">2460000.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.</cbc:Description>
      <cbc:Name>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>NLB-FLU-S26-10</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Zero-rated export supply</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">GST</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="INR">4100</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:InvoicedQuantity unitCode="EA">960</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="INR">1248000.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.</cbc:Description>
      <cbc:Name>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>NLB-INS-R100-10</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Zero-rated export supply</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">GST</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="INR">1300</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>3</cbc:ID>
    <cbc:InvoicedQuantity unitCode="EA">120</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="INR">342000.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.</cbc:Description>
      <cbc:Name>Varicella vaccine, live, frozen, single dose</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>NLB-VZV-1</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Zero-rated export supply</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">GST</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="INR">2850</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
