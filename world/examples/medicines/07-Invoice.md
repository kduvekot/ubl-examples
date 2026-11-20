# Invoice: Haarvliet Isotopes to Quillmoor Pharma Distribution

*Example 7 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The Dutch maker invoices the generator in euro when it leaves for Amsterdam airport; an export, zero-rated in the Netherlands.

[The XML file](07-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Invoice/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Billing". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **QLM-TX-26-3960**  
  The collaboration this document belongs to: Quillmoor's order of a technetium generator from Haarvliet Isotopes. Quillmoor Pharma Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **HVI-INV-26-1344**  
  The maker's invoice number.
- `UUID` = **3cf34a08-9641-59d5-a039-a316fccf582f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-13**  
  Issued when the generator left the maker for Amsterdam airport, on the Saturday: isotopes are made and shipped every day.
- `IssueTime` = **11:30:00+02:00**  
  In the morning, when the generator left; in the issuer's local time, with its offset from UTC.
- `DueDate` = **2026-06-29**  
  14 days from Saturday 13 June end on Saturday 27 June, no business day for a bank transfer, so the payment is due on Monday 29 June.
- `InvoiceTypeCode` = **380** (listID `UN/EDIFACT EDED 1001`)  
  A commercial invoice, as UN/EDIFACT 1001 codes it. The code is from the world's copy of UN/EDIFACT 1001 Document name: 380 = Commercial invoice.
- `DocumentCurrencyCode` = **EUR** (listID `ISO 4217 Alpha`)  
  The euro, the maker's currency; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: EUR = Euro.
- `LineCountNumeric` = **1**  
  The number of invoice lines.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  English, the language of the maker's export invoices. The code is from the world's copy of ISO 639 Language: en = English.

### Order Reference

Inside `OrderReference`:

- `ID` = **QLM-PO-26-3960**  
  The wholesaler's call-off.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyName/Name` = **Haarvliet Isotopes**  
  The trading name; as Haarvliet Isotopes, a maker outside the three countries, gives it. It carries no identifier of a real register: a Dutch Chamber of Commerce number or VAT number in the real format could be someone's; the documents identify it by its name and address, as a supplier outside the world.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/StreetName` = **Isotopenweg**  
  Street of the postal address. As Haarvliet Isotopes gives it; the address is fictional, in a real town.
- `Party/PostalAddress/BuildingNumber` = **14**  
  Building number. As Haarvliet Isotopes gives it; the address is fictional, in a real town.
- `Party/PostalAddress/CityName` = **Alkmaar**  
  The town. As Haarvliet Isotopes gives it; the address is fictional, in a real town.
- `Party/PostalAddress/PostalZone` = **1812 RN**  
  Postal code in the format of Netherlands. As Haarvliet Isotopes gives it; the address is fictional, in a real town.
- `Party/PostalAddress/TimezoneOffset` = **+02:00**  
  The offset from UTC of Central European Summer Time, the legal time there in June.
- `Party/PostalAddress/Country/IdentificationCode` = **NL** (listID `ISO 3166`)  
  Netherlands, a real country outside the world. The code is from the world's copy of UBL's Country identification (ISO 3166) list: NL = Netherlands (the).
- `Party/PostalAddress/Country/Name` = **Netherlands**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Haarvliet Isotopes B.V.**  
  The company's registered name, with the legal form of its country; as Haarvliet Isotopes, a maker outside the three countries, gives it.
- `Party/Contact/Name` = **Order desk**  
  The party's desk that handles this document; as Haarvliet Isotopes, a maker outside the three countries, gives it.
- `Party/Contact/JobTitle` = **Order coordinator**  
  The job of the person who answers at the desk; as Haarvliet Isotopes, a maker outside the three countries, gives it.
- `Party/Contact/Department` = **Customer service**  
  The department the desk belongs to; as Haarvliet Isotopes, a maker outside the three countries, gives it.
- `Party/Contact/ElectronicMail` = **orders@haarvliet-isotopes.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; no telephone number is given, as one in the real country's plan could reach someone; as Haarvliet Isotopes, a maker outside the three countries, gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Haarvliet Isotopes, a maker outside the three countries, gives it.

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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
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

- `Party/PartyName/Name` = **Haarvliet Isotopes**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery

Inside `Delivery`:

- `DeliveryLocation/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `DeliveryLocation/Name` = **Lumeport airport**  
  Where it is delivered: Lumeport airport.
- `DeliveryLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Despatch/ActualDespatchDate` = **2026-06-13**  
  The generator left the maker for Amsterdam airport.

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

- `Note` = **14 days net.**  
  The maker's terms for wholesalers: 14 days from the invoice.
- `PaymentDueDate` = **2026-06-29**  
  As the due date above.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `EUR`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **1000.00** (currencyID `EUR`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `EUR`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  Goods exported outside the European Union are zero-rated under Dutch VAT: no tax is charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export outside the European Union**  
  Why no tax is charged, stated rather than left out.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **1000.00** (currencyID `EUR`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **1000.00** (currencyID `EUR`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **1000.00** (currencyID `EUR`)  
  The total without tax plus the tax.
- `PayableAmount` = **1000.00** (currencyID `EUR`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **1** (unitCode `EA`)  
  The quantity shipped.
- `LineExtensionAmount` = **1000.00** (currencyID `EUR`)  
  1 × 1000.0, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **1**  
  The line of the wholesaler's order.
- `Item/Description` = **A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.**  
  The seller's description.
- `Item/Name` = **Technetium-99m generator, 20 GBq**  
  The item's short name.
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **HVI-TCG-20**  
  The seller's own item number; as Haarvliet Isotopes describes the item.
- `Item/ClassifiedTaxCategory/ID` = **G** (schemeID `UN/EDIFACT EDED 5305`)  
  Goods exported outside the European Union are zero-rated under Dutch VAT: no tax is charged (category G). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: G = Free export item, tax not charged. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Export outside the European Union**  
  Why no tax is charged, stated rather than left out.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/ItemInstance/SerialID` = **HVI-TCG20-26-0137**  
  The generator's serial number, from its maker: each generator is traced from its filling to its return.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Nominal activity**  
  The generator's size: its Mo-99 at the reference time, the figure the item is sold by.
- `Item/ItemInstance/AdditionalItemProperty/ValueQuantity` = **20** (unitCode `GBQ`)  
  20 GBq.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Reference time**  
  When the generator holds its nominal activity: European generators are pre-calibrated to a time some days after delivery, so that the hospital has its nominal activity at the end of its week.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **2026-06-21T12:00:00+00:00**  
  Sunday 21 June at 12:00 UTC, six days after delivery.
- `Price/PriceAmount` = **1000** (currencyID `EUR`)  
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
  <cbc:ProfileExecutionID>QLM-TX-26-3960</cbc:ProfileExecutionID>
  <cbc:ID>HVI-INV-26-1344</cbc:ID>
  <cbc:UUID>3cf34a08-9641-59d5-a039-a316fccf582f</cbc:UUID>
  <cbc:IssueDate>2026-06-13</cbc:IssueDate>
  <cbc:IssueTime>11:30:00+02:00</cbc:IssueTime>
  <cbc:DueDate>2026-06-29</cbc:DueDate>
  <cbc:InvoiceTypeCode listID="UN/EDIFACT EDED 1001">380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">EUR</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:OrderReference>
    <cbc:ID>QLM-PO-26-3960</cbc:ID>
  </cac:OrderReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Haarvliet Isotopes</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:StreetName>Isotopenweg</cbc:StreetName>
        <cbc:BuildingNumber>14</cbc:BuildingNumber>
        <cbc:CityName>Alkmaar</cbc:CityName>
        <cbc:PostalZone>1812 RN</cbc:PostalZone>
        <cbc:TimezoneOffset>+02:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">NL</cbc:IdentificationCode>
          <cbc:Name>Netherlands</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Haarvliet Isotopes B.V.</cbc:RegistrationName>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Order coordinator</cbc:JobTitle>
        <cbc:Department>Customer service</cbc:Department>
        <cbc:ElectronicMail>orders@haarvliet-isotopes.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
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
        <cbc:Note>Every day, around the clock</cbc:Note>
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
        <cbc:Name>Haarvliet Isotopes</cbc:Name>
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
      <cbc:ActualDespatchDate>2026-06-13</cbc:ActualDespatchDate>
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
    <cbc:Note>14 days net.</cbc:Note>
    <cbc:PaymentDueDate>2026-06-29</cbc:PaymentDueDate>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="EUR">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="EUR">1000.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="EUR">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Export outside the European Union</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="EUR">1000.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="EUR">1000.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="EUR">1000.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="EUR">1000.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="EA">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="EUR">1000.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.</cbc:Description>
      <cbc:Name>Technetium-99m generator, 20 GBq</cbc:Name>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:SellersItemIdentification>
        <cbc:ID>HVI-TCG-20</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Export outside the European Union</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
      <cac:ItemInstance>
        <cbc:SerialID>HVI-TCG20-26-0137</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Nominal activity</cbc:Name>
          <cbc:ValueQuantity unitCode="GBQ">20</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Reference time</cbc:Name>
          <cbc:Value>2026-06-21T12:00:00+00:00</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="EUR">1000</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
