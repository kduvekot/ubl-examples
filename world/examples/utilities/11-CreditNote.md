# Credit Note: Coastal State Water Company to Robin Ashdale

*Example 11 of the flow "Electricity, water and telecom (one utility in each country)" · [Credit Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CREDIT-NOTE-SCHEMA)*

After the reminder the household had its water meter tested: it over-read by two cubic metres at the annual reading. The utility credits the water and the city's levy on them, which reduces the balance still open.

[The XML file](11-CreditNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; CreditNote/DefaultLanguageCode first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:billing:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Billing". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:utility-billing:1.0**  
  The Trade Accord's process profile the document belongs to: utility billing, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9924052627**  
  The collaboration this document belongs to: the water company's annual account of the household. Coastal State Water Company started it and gave it this identifier, which every document of it repeats.
- `ID` = **9100373645**  
  The seller's credit note number.
- `UUID` = **b275185e-048c-56dd-9144-cf9ea28b4f48**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Issued when the meter test was in.
- `IssueTime` = **12:03:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `CreditNoteTypeCode` = **381** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 381: credit note. The code is from the world's copy of UN/EDIFACT 1001 Document name: 381 = Credit note.
- `Note` = **The test of water meter CSW-W-71844 found it over-reading by two cubic metres at the annual reading of 31 March: the year used 168 m³, not 170.**  
  Why.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the currency of the invoice credited; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **2**  
  The water and the collection line of the levy; the amount credited includes both.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts. The code is from the world's copy of ISO 639 Language: en = English.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2025-04-01**  
  The account year the settlement bill billed.
- `EndDate` = **2026-03-31**  
  Its end, the annual reading.

### Billing Reference

Inside `BillingReference`:

- `InvoiceDocumentReference/ID` = **CSW-C-311790-2603**  
  The March bill corrected.
- `InvoiceDocumentReference/IssueDate` = **2026-04-02**  
  Its issue date.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered for state sales tax; as Coastal State Water Company gives it.
- `Party/PartyTaxScheme/CompanyID` = **CO-1236576** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); as Coastal State Water Company gives it. The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered, with its legal form; as Coastal State Water Company gives it.
- `Party/PartyLegalEntity/CompanyID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SOC** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: SOC = State-owned company limited by shares.
- `Party/PartyLegalEntity/CompanyLegalForm` = **State-owned company limited by shares** (languageID `en-XB`)  
  The name of code SOC in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Billing**  
  The party's billing desk: the desk for its role in this document (it is owed the payment); as Coastal State Water Company gives it.
- `Party/Contact/JobTitle` = **Billing officer**  
  The job of the person who answers at the desk; as Coastal State Water Company gives it.
- `Party/Contact/Department` = **Customer service**  
  The department the desk belongs to; as Coastal State Water Company gives it.
- `Party/Contact/Telephone` = **+999 2 38 9310 7518**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Coastal State Water Company gives it.
- `Party/Contact/ElectronicMail` = **billing@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Coastal State Water Company gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Coastal State Water Company gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Coastal State Water Company gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyName/Name` = **Robin Ashdale**  
  The trading name; as Robin Ashdale gives it.
- `Party/PostalAddress/ID` = **LUM-ADR-934215** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Robin Ashdale gives it.
- `Party/PostalAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. As Robin Ashdale gives it.
- `Party/PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. As Robin Ashdale gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Riverside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Robin Ashdale gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Robin Ashdale gives it.
- `Party/PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). As Robin Ashdale gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Robin Ashdale gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Person/FirstName` = **Robin**  
  The consumer's first name; as Robin Ashdale gives it.
- `Party/Person/FamilyName` = **Ashdale**  
  The consumer's family name; as Robin Ashdale gives it.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **Set off against the balance of the settlement bill CSW-C-311790-2603, still open after the returned direct debit: 141.20 less 5.54 leaves 135.66 due, with the reminder's fee.**  
  How the credit is settled.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **4.70** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Drinking water is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **4.70** (currencyID `XBL`)  
  The sum of the bill's own lines; the levy collected for the city is added to the amount payable only.
- `TaxExclusiveAmount` = **4.70** (currencyID `XBL`)  
  The bill's own lines without tax; the levy collected for the city is not part of it.
- `TaxInclusiveAmount` = **4.70** (currencyID `XBL`)  
  The bill's own lines with their tax; the levy collected for the city is not part of it.
- `PayableAmount` = **5.54** (currencyID `XBL`)  
  What is credited: the bill's own lines with their tax plus the levy collected for the city.

### Collection Credit Note Line

Inside `CollectionCreditNoteLine`:

- `ID` = **2**  
  The line number.
- `Note` = **The city's levy, credited for the city.**  
  Why it is a collection line.
- `CreditedQuantity` = **2** (unitCode `MTQ`)  
  The city's levy on them.
- `LineExtensionAmount` = **0.84** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `BillingReference/InvoiceDocumentReference/ID` = **CSW-C-311790-2603**  
  The settlement bill.
- `BillingReference/BillingReferenceLine/ID` = **2**  
  The line credited.
- `CollectedForParty/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `CollectedForParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Description` = **The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.**  
  The seller's description.
- `Item/Name` = **Sewage levy of the city of Lumeport**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **CSW-LEVY**  
  The seller's own item number; as Coastal State Water Company describes the item.
- `Item/ClassifiedTaxCategory/ID` = **O** (schemeID `UN/EDIFACT EDED 5305`)  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O, without a rate). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: O = Services outside scope of tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **LEVY** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: LEVY = Collected for a public body, outside the scope of the state sales tax.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Collected for a public body, outside the scope of the state sales tax**  
  The name of code LEVY in Bayvarra's national sales tax exemption reason list.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **0.42** (currencyID `XBL`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.

### Credit Note Line

Inside `CreditNoteLine`:

- `ID` = **1**  
  The line number.
- `CreditedQuantity` = **2** (unitCode `MTQ`)  
  Two cubic metres the water meter CSW-W-71844 over-read at the annual reading of 31 March.
- `LineExtensionAmount` = **4.70** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `BillingReference/InvoiceDocumentReference/ID` = **CSW-C-311790-2603**  
  The settlement bill.
- `BillingReference/BillingReferenceLine/ID` = **1**  
  The line credited.
- `Item/Description` = **Drinking water supply, per cubic metre.**  
  The seller's description.
- `Item/Name` = **Drinking water**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **CW-M3**  
  The seller's own item number; as Coastal State Water Company describes the item.
- `Item/ClassifiedTaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  Drinking water is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **GOODS** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: GOODS = Goods.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Price/PriceAmount` = **2.35** (currencyID `XBL`)  
  The seller's price per unit.
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CreditNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:billing:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:utility-billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9924052627</cbc:ProfileExecutionID>
  <cbc:ID>9100373645</cbc:ID>
  <cbc:UUID>b275185e-048c-56dd-9144-cf9ea28b4f48</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>12:03:00-01:00</cbc:IssueTime>
  <cbc:CreditNoteTypeCode listID="UN/EDIFACT EDED 1001">381</cbc:CreditNoteTypeCode>
  <cbc:Note>The test of water meter CSW-W-71844 found it over-reading by two cubic metres at the annual reading of 31 March: the year used 168 m³, not 170.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2025-04-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
  </cac:InvoicePeriod>
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>CSW-C-311790-2603</cbc:ID>
      <cbc:IssueDate>2026-04-02</cbc:IssueDate>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
  <cac:AccountingSupplierParty>
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
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1236576</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:CompanyID>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">SOC</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="en-XB">State-owned company limited by shares</cbc:CompanyLegalForm>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Billing</cbc:Name>
        <cbc:JobTitle>Billing officer</cbc:JobTitle>
        <cbc:Department>Customer service</cbc:Department>
        <cbc:Telephone>+999 2 38 9310 7518</cbc:Telephone>
        <cbc:ElectronicMail>billing@coastalwater.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Robin Ashdale</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-934215</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">RESIDENTIAL</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Gull Lane</cbc:StreetName>
        <cbc:BuildingNumber>57</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Riverside</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38516</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Person>
        <cbc:FirstName>Robin</cbc:FirstName>
        <cbc:FamilyName>Ashdale</cbc:FamilyName>
      </cac:Person>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:PaymentTerms>
    <cbc:Note>Set off against the balance of the settlement bill CSW-C-311790-2603, still open after the returned direct debit: 141.20 less 5.54 leaves 135.66 due, with the reminder's fee.</cbc:Note>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">4.70</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">4.70</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">4.70</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">4.70</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XBL">5.54</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:CollectionCreditNoteLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>The city's levy, credited for the city.</cbc:Note>
    <cbc:CreditedQuantity unitCode="MTQ">2</cbc:CreditedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">0.84</cbc:LineExtensionAmount>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>CSW-C-311790-2603</cbc:ID>
      </cac:InvoiceDocumentReference>
      <cac:BillingReferenceLine>
        <cbc:ID>2</cbc:ID>
      </cac:BillingReferenceLine>
    </cac:BillingReference>
    <cac:CollectedForParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:CollectedForParty>
    <cac:Item>
      <cbc:Description>The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.</cbc:Description>
      <cbc:Name>Sewage levy of the city of Lumeport</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CSW-LEVY</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">O</cbc:ID>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">LEVY</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Collected for a public body, outside the scope of the state sales tax</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">0.42</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:CollectionCreditNoteLine>
  <cac:CreditNoteLine>
    <cbc:ID>1</cbc:ID>
    <cbc:CreditedQuantity unitCode="MTQ">2</cbc:CreditedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">4.70</cbc:LineExtensionAmount>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>CSW-C-311790-2603</cbc:ID>
      </cac:InvoiceDocumentReference>
      <cac:BillingReferenceLine>
        <cbc:ID>1</cbc:ID>
      </cac:BillingReferenceLine>
    </cac:BillingReference>
    <cac:Item>
      <cbc:Description>Drinking water supply, per cubic metre.</cbc:Description>
      <cbc:Name>Drinking water</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CW-M3</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">GOODS</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">2.35</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:CreditNoteLine>
</CreditNote>
```
