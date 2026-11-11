# Credit Note: Coastal State Water Company to Robin Ashdale

*Example 11 of the flow "Electricity, water and telecom (one utility in each country)" · [Credit Note in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CREDIT-NOTE-SCHEMA)*

After the reminder the household had its meter tested: it over-read by two cubic metres in March. The utility credits the water and the city's levy on them.

[The XML file](11-CreditNote.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:utilities**  
  The business process the document belongs to: the flow "Electricity, water and telecom (one utility in each country)".
- `ProfileExecutionID` = **UTILITIES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **CSWC-CN-26-0322**  
  The seller's credit note number.
- `UUID` = **b275185e-048c-56dd-9144-cf9ea28b4f48**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Issued when the meter test was in.
- `IssueTime` = **12:03:00**  
  The time the sender's system issued the document, in the sender's local time.
- `CreditNoteTypeCode` = **381** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 381: credit note. The code is from the world's copy of UN/EDIFACT 1001 Document name: 381 = Credit note.
- `Note` = **The meter test found the meter over-reading by two cubic metres.**  
  Why.
- `DocumentCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The lume, the currency of the invoice credited; it has two decimals. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `LineCountNumeric` = **2**  
  The water and the collection line of the levy; the totals include both.
- `DefaultLanguageCode` = **en** (listID `ISO 639`)  
  The language of the texts. The code is from the world's copy of ISO 639 Language: en = English.

### Billing Reference

Inside `BillingReference`:

- `InvoiceDocumentReference/ID` = **CSWC-INV-26-0319**  
  The March bill corrected.
- `InvoiceDocumentReference/IssueDate` = **2026-04-02**  
  Its issue date.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.coastalwater.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Coastal State Water Company (world/parties.json).
- `Party/IndustryClassificationCode` = **3600** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Coastal State Water Company (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3600 = Water collection, treatment and supply.
- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Coastal State Water Company**  
  The trading name; identity of Coastal State Water Company (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Coastal State Water Company (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered for state sales tax; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1236576**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Coastal State Water Company (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered, with its legal form; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412192**  
  Number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 17 persons and its turnover of 9470000.00 XBL in 2025, by the Trade Accord's limits; identity of Coastal State Water Company (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2692 2192**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Coastal State Water Company (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Coastal State Water Company (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyName/Name` = **Robin Ashdale**  
  The trading name; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **RESIDENTIAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: RESIDENTIAL = Residential address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Person/FirstName` = **Robin**  
  The consumer's first name; identity of Robin Ashdale (world/parties.json).
- `Party/Person/FamilyName` = **Ashdale**  
  The consumer's family name; identity of Robin Ashdale (world/parties.json).
- `Party/Person/FinancialAccount/ID` = **XB95BLUM0007251840** (schemeID `urn:ubl-examples:world:account`)  
  The consumer's own account, from which the bills are paid. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `Party/Person/FinancialAccount/Name` = **Robin Ashdale**  
  The account holder, as the bank knows it.
- `Party/Person/FinancialAccount/AccountTypeCode` = **CACC** (listID `ISO 20022 ExternalCashAccountType1Code`)  
  A current account, for payments in and out. The code is from the world's copy of ISO 20022 ExternalCashAccountType1Code: CACC = Current.
- `Party/Person/FinancialAccount/AccountFormatCode` = **ISO13616** (listID `urn:ubl-examples:world:codelist:AccountFormatCode`)  
  The account number has the structure of ISO 13616. The code is from the Trade Accord's account number format list: ISO13616 = Structure of ISO 13616.
- `Party/Person/FinancialAccount/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The account is kept in the currency of the bank's country. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/ID` = **BLUM-001**  
  The branch that keeps the account.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUM**  
  The bank code, the part of every account number that names the bank; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  The bank's head office; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Its building number; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  Its town; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The bank's country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The branch is at the bank's head office.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Its country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Person/FinancialAccount/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country where the account is kept. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Payment Terms

Inside `PaymentTerms`:

- `Note` = **Settled against the next payment to the seller, unless refunded.**  
  How a credit note is settled in the world.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **4.70** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **E**  
  Drinking water is exempt from the state sales tax (category E).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `TaxSubtotal/TaxableAmount` = **0.84** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **O**  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **LEVY** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: LEVY = Levy collected for a public body.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Levy collected for a public body**  
  The name of code LEVY in Bayvarra's national sales tax exemption reason list.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **5.54** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **5.54** (currencyID `XBL`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **5.54** (currencyID `XBL`)  
  The total without tax plus the tax.
- `PayableAmount` = **5.54** (currencyID `XBL`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

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
- `BeneficiaryParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `BeneficiaryParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Description` = **The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.**  
  The seller's description; item sewage-levy of Coastal State Water Company (world/items.json).
- `Item/Name` = **Sewage levy of the city of Lumeport**  
  The item's short name; item sewage-levy of Coastal State Water Company (world/items.json).
- `Item/SellersItemIdentification/ID` = **CSW-LEVY**  
  The seller's own item number; item sewage-levy of Coastal State Water Company (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **O**  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **LEVY** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: LEVY = Levy collected for a public body.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Levy collected for a public body**  
  The name of code LEVY in Bayvarra's national sales tax exemption reason list.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: SERVICES = Services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **0.42** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.

### Credit Note Line

Inside `CreditNoteLine`:

- `ID` = **1**  
  The line number.
- `CreditedQuantity` = **2** (unitCode `MTQ`)  
  Two cubic metres the meter over-read in March.
- `LineExtensionAmount` = **4.70** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `Item/Description` = **Drinking water supply, per cubic metre.**  
  The seller's description; item water of Coastal State Water Company (world/items.json).
- `Item/Name` = **Drinking water**  
  The item's short name; item water of Coastal State Water Company (world/items.json).
- `Item/SellersItemIdentification/ID` = **CW-M3**  
  The seller's own item number; item water of Coastal State Water Company (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **E**  
  Drinking water is exempt from the state sales tax (category E).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **WATER** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: WATER = Drinking water.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Drinking water**  
  The name of code WATER in Bayvarra's national sales tax exemption reason list.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **SERVICES** (listID `urn:ubl-examples:world:codelist:SupplyTypeCode`)  
  Whether the category applies to goods or services. The code is from the Trade Accord's supply type list: SERVICES = Services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **2.35** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CreditNote xmlns="urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:utilities</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>CSWC-CN-26-0322</cbc:ID>
  <cbc:UUID>b275185e-048c-56dd-9144-cf9ea28b4f48</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>12:03:00</cbc:IssueTime>
  <cbc:CreditNoteTypeCode listID="UN/EDIFACT EDED 1001">381</cbc:CreditNoteTypeCode>
  <cbc:Note>The meter test found the meter over-reading by two cubic metres.</cbc:Note>
  <cbc:DocumentCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode listID="ISO 639">en</cbc:DefaultLanguageCode>
  <cac:BillingReference>
    <cac:InvoiceDocumentReference>
      <cbc:ID>CSWC-INV-26-0319</cbc:ID>
      <cbc:IssueDate>2026-04-02</cbc:IssueDate>
    </cac:InvoiceDocumentReference>
  </cac:BillingReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.coastalwater.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3600</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Reservoir Road</cbc:StreetName>
        <cbc:BuildingNumber>51</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38500</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
        <cbc:CompanyID>CO-1236576</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
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
        <cbc:CompanyID>20412192</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
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
        <cbc:Name>Customer service</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 38 2692 2192</cbc:Telephone>
        <cbc:ElectronicMail>customer@coastalwater.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
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
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">RESIDENTIAL</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Gull Lane</cbc:StreetName>
        <cbc:BuildingNumber>57</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38516</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Person>
        <cbc:FirstName>Robin</cbc:FirstName>
        <cbc:FamilyName>Ashdale</cbc:FamilyName>
        <cac:FinancialAccount>
          <cbc:ID schemeID="urn:ubl-examples:world:account">XB95BLUM0007251840</cbc:ID>
          <cbc:Name>Robin Ashdale</cbc:Name>
          <cbc:AccountTypeCode listID="ISO 20022 ExternalCashAccountType1Code">CACC</cbc:AccountTypeCode>
          <cbc:AccountFormatCode listID="urn:ubl-examples:world:codelist:AccountFormatCode">ISO13616</cbc:AccountFormatCode>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:FinancialInstitutionBranch>
            <cbc:ID>BLUM-001</cbc:ID>
            <cbc:Name>Main branch</cbc:Name>
            <cac:FinancialInstitution>
              <cbc:ID>BLUM</cbc:ID>
              <cbc:Name>Bank of Lumeport</cbc:Name>
              <cac:Address>
                <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
                <cbc:StreetName>Exchange Street</cbc:StreetName>
                <cbc:BuildingNumber>48</cbc:BuildingNumber>
                <cbc:CityName>Lumeport</cbc:CityName>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:FinancialInstitution>
            <cac:Address>
              <cbc:CityName>Lumeport</cbc:CityName>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:FinancialInstitutionBranch>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:FinancialAccount>
      </cac:Person>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:PaymentTerms>
    <cbc:Note>Settled against the next payment to the seller, unless refunded.</cbc:Note>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">4.70</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">0.84</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">LEVY</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Levy collected for a public body</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">5.54</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">5.54</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">5.54</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XBL">5.54</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:CollectionCreditNoteLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>The city's levy, credited for the city.</cbc:Note>
    <cbc:CreditedQuantity unitCode="MTQ">2</cbc:CreditedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">0.84</cbc:LineExtensionAmount>
    <cac:BeneficiaryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:BeneficiaryParty>
    <cac:Item>
      <cbc:Description>The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.</cbc:Description>
      <cbc:Name>Sewage levy of the city of Lumeport</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CSW-LEVY</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">LEVY</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Levy collected for a public body</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">SERVICES</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
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
    <cac:Item>
      <cbc:Description>Drinking water supply, per cubic metre.</cbc:Description>
      <cbc:Name>Drinking water</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CW-M3</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode listID="urn:ubl-examples:world:codelist:SupplyTypeCode">SERVICES</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
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
