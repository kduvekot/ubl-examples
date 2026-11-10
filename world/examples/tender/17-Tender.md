# Tender: Brackenmere Furniture to Lumeport Public Works Department

*Example 17 of the flow "A public tender (Bayvarra)" · [Tender in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TENDER-SCHEMA)*

The furniture maker tenders wooden benches.

[The XML file](17-Tender.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:tender**  
  The business process the document belongs to: the flow "A public tender (Bayvarra)".
- `ProfileExecutionID` = **TENDER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BF-DOC-26-0203**  
  The furniture maker's number for this tender.
- `UUID` = **21770882-3c11-5392-aed3-5bd95b4c3cc7**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `TenderTypeCode` = **Combined**  
  Technical and financial in one.
- `ContractFolderID` = **PWD-2026-PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-02-23**  
  Submitted before the deadline.
- `IssueTime` = **16:37:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ContractName` = **Park benches for the parks renewal programme**  
  The contract tendered for.
- `Note` = **Tender for both lots, with a recycled-plastic variant.**  
  What is offered.

### Validity Period

Inside `ValidityPeriod`:

- `DurationMeasure` = **90** (unitCode `DAY`)  
  Valid for 90 days.

### Call For Tender Document Reference

Inside `CallForTenderDocumentReference`:

- `ID` = **PWD-2026-PARKS-CFT**  
  The call for tenders.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BF-DS-PARK**  
  The datasheet.

### Signature

Inside `Signature`:

- `ID` = **BF-SIG-TENDER-17**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.

### Tenderer Party

Inside `TendererParty`:

- `WebsiteURI` = **https://www.brackenmere.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brackenmere Furniture (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brackenmere Furniture (world/parties.json).
- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; identity of Brackenmere Furniture (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brackenmere Furniture (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered for state sales tax; identity of Brackenmere Furniture (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1237398**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brackenmere Furniture (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered, with its legal form; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412466**  
  Number in the Federal business register of Bayvarra; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Brackenmere Furniture (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Contact/Name` = **Trade sales**  
  The desk that handles this document; identity of Brackenmere Furniture (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Telephone` = **+999 2 7120 2466**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Brackenmere Furniture (world/parties.json).
- `Contact/ElectronicMail` = **trade@brackenmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brackenmere Furniture (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brackenmere Furniture (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brackenmere Furniture (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tenderer Qualification Document Reference

Inside `TendererQualificationDocumentReference`:

- `ID` = **VI-DOC-26-0199**  
  The qualification documents.

### Contracting Party

Inside `ContractingParty`:

- `Party/IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410548** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/ID` = **LUM-ADR-000417**  
  The address's number in the city's address register; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered for state sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-0900002**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/ExemptionReason` = **Public bodies are exempt from the state sales tax**  
  Why purchases by this party carry no sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered, with its legal form; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410548**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Party/Contact/Name` = **Procurement office**  
  The desk that handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 3851 0548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Originator Customer Party

Inside `OriginatorCustomerParty`:

- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Beneficiary Party

Inside `BeneficiaryParty`:

- `PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.

### Tendered Project

Inside `TenderedProject`:

- `VariantID` = **V1**  
  The variant.
- `FeeAmount` = **50.00** (currencyID `XBL`)  
  The documentation fee paid.
- `FeeDescription` = **Paper copy of the documents.**  
  What the fee was for.
- `TenderEnvelopeID` = **ENV-1**  
  The envelope.
- `TenderEnvelopeTypeCode` = **Combined**  
  Technical and price together.
- `AdditionalFee/FeeTypeCode` = **Courier**  
  A courier fee.
- `AdditionalFee/FeeAmount` = **12.00** (currencyID `XBL`)  
  For the signed originals.
- `AdditionalFee/FeeDescription` = **Courier of the guarantee's original.**  
  What.
- `ProcurementProjectLot/ID` = **LOT-1**  
  Lot 1.
- `ProcurementProjectLot/ID` = **LOT-2**  
  Lot 2.
- `EvidenceDocumentReference/ID` = **VI-REF-2025**  
  Reference letters.
- `TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No tax for a public body.
- `LegalMonetaryTotal/LineExtensionAmount` = **127440.00** (currencyID `XBL`)  
  Both lots.
- `LegalMonetaryTotal/PayableAmount` = **127440.00** (currencyID `XBL`)  
  The tender's total.
- `TenderLine/ID` = **1**  
  The benches.
- `TenderLine/Note` = **Serra 180, as specified.**  
  What is offered.
- `TenderLine/Quantity` = **240** (unitCode `H87`)  
  240 benches.
- `TenderLine/LineExtensionAmount` = **123600.00** (currencyID `XBL`)  
  240 at the unit price.
- `TenderLine/TaxInclusiveLineExtensionAmount` = **123600.00** (currencyID `XBL`)  
  No tax for a public body.
- `TenderLine/TotalTaxAmount` = **0.00** (currencyID `XBL`)  
  None.
- `TenderLine/OrderableUnit` = **Pallet of 4**  
  Called off in pallets.
- `TenderLine/ContentUnitQuantity` = **4** (unitCode `H87`)  
  Four per pallet.
- `TenderLine/OrderQuantityIncrementNumeric` = **4**  
  In steps of four.
- `TenderLine/MinimumOrderQuantity` = **20** (unitCode `H87`)  
  A release of at least 20.
- `TenderLine/MaximumOrderQuantity` = **96** (unitCode `H87`)  
  At most a full truck.
- `TenderLine/WarrantyInformation` = **Five years on the frame.**  
  The warranty.
- `TenderLine/PackLevelCode` = **Pallet**  
  The pack level.
- `TenderLine/DocumentReference/ID` = **VI-DS-B180**  
  The datasheet.
- `TenderLine/Item/Name` = **Park bench Serra 180**  
  The item offered.
- `TenderLine/OfferedItemLocationQuantity/LeadTimeMeasure` = **7** (unitCode `DAY`)  
  Seven days per release.
- `TenderLine/ReplacementRelatedItem/ID` = **VI-C180-2026**  
  Spare frames available.
- `TenderLine/ReplacementRelatedItem/Quantity` = **1** (unitCode `H87`)  
  One for one.
- `TenderLine/WarrantyParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderLine/WarrantyParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderLine/WarrantyValidityPeriod/DurationMeasure` = **5** (unitCode `ANN`)  
  Five years.
- `TenderLine/SubTenderLine/ID` = **1.1**  
  The anchors.
- `TenderLine/SubTenderLine/Quantity` = **240** (unitCode `SET`)  
  One set per bench.
- `TenderLine/SubTenderLine/Item/Name` = **Ground anchor set**  
  Included.
- `TenderLine/CallForTendersLineReference/LineID` = **1**  
  The line of the call for tenders.
- `TenderLine/CallForTendersDocumentReference/ID` = **PWD-2026-PARKS-CFT**  
  The call for tenders.
- `TenderLine/ID` = **2**  
  The installation.
- `TenderLine/Quantity` = **240** (unitCode `H87`)  
  240 installations.
- `TenderLine/LineExtensionAmount` = **3840.00** (currencyID `XBL`)  
  240 at the price.
- `TenderLine/Item/Name` = **Installation of a park bench**  
  The service.
- `AwardingCriterionResponse/ID` = **ACR-1**  
  The response to the quality criterion.
- `AwardingCriterionResponse/AwardingCriterionID` = **AC-2**  
  Quality.
- `AwardingCriterionResponse/AwardingCriterionDescription` = **Warranty and coating.**  
  The criterion.
- `AwardingCriterionResponse/Description` = **Ten years on the coating.**  
  The offer.
- `AwardingCriterionResponse/Quantity` = **10** (unitCode `ANN`)  
  Ten years.
- `AwardingCriterionResponse/Amount` = **127440.00** (currencyID `XBL`)  
  The price offered.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/ID` = **ACR-1.1**  
  Durability.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/AwardingCriterionID` = **AC-2.1**  
  Its criterion.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/Description` = **Hot-dip galvanised and powder coated.**  
  The offer.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Tender xmlns="urn:oasis:names:specification:ubl:schema:xsd:Tender-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:tender</cbc:ProfileID>
  <cbc:ProfileExecutionID>TENDER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BF-DOC-26-0203</cbc:ID>
  <cbc:UUID>21770882-3c11-5392-aed3-5bd95b4c3cc7</cbc:UUID>
  <cbc:TenderTypeCode>Combined</cbc:TenderTypeCode>
  <cbc:ContractFolderID>PWD-2026-PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-23</cbc:IssueDate>
  <cbc:IssueTime>16:37:00</cbc:IssueTime>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:Note>Tender for both lots, with a recycled-plastic variant.</cbc:Note>
  <cac:ValidityPeriod>
    <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
  </cac:ValidityPeriod>
  <cac:CallForTenderDocumentReference>
    <cbc:ID>PWD-2026-PARKS-CFT</cbc:ID>
  </cac:CallForTenderDocumentReference>
  <cac:DocumentReference>
    <cbc:ID>BF-DS-PARK</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>BF-SIG-TENDER-17</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brackenmere Furniture</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:TendererParty>
    <cbc:WebsiteURI>https://www.brackenmere.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Joiners Row</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71203</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
      <cbc:CompanyID>UL-1237398</cbc:CompanyID>
      <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
        <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20412466</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FBR</cbc:ID>
        <cbc:Name>Federal business register of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Trade sales</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7120 2466</cbc:Telephone>
      <cbc:ElectronicMail>trade@brackenmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:TendererParty>
  <cac:TendererQualificationDocumentReference>
    <cbc:ID>VI-DOC-26-0199</cbc:ID>
  </cac:TendererQualificationDocumentReference>
  <cac:ContractingParty>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410548</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID>LUM-ADR-000417</cbc:ID>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
        <cbc:Department>Procurement office</cbc:Department>
        <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>CO-0900002</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cbc:ExemptionReason>Public bodies are exempt from the state sales tax</cbc:ExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>20410548</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Procurement office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 3851 0548</cbc:Telephone>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410548</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:ContractingParty>
  <cac:OriginatorCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:OriginatorCustomerParty>
  <cac:BeneficiaryParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Public Works Department</cbc:Name>
    </cac:PartyName>
  </cac:BeneficiaryParty>
  <cac:TenderedProject>
    <cbc:VariantID>V1</cbc:VariantID>
    <cbc:FeeAmount currencyID="XBL">50.00</cbc:FeeAmount>
    <cbc:FeeDescription>Paper copy of the documents.</cbc:FeeDescription>
    <cbc:TenderEnvelopeID>ENV-1</cbc:TenderEnvelopeID>
    <cbc:TenderEnvelopeTypeCode>Combined</cbc:TenderEnvelopeTypeCode>
    <cac:AdditionalFee>
      <cbc:FeeTypeCode>Courier</cbc:FeeTypeCode>
      <cbc:FeeAmount currencyID="XBL">12.00</cbc:FeeAmount>
      <cbc:FeeDescription>Courier of the guarantee's original.</cbc:FeeDescription>
    </cac:AdditionalFee>
    <cac:ProcurementProjectLot>
      <cbc:ID>LOT-1</cbc:ID>
    </cac:ProcurementProjectLot>
    <cac:ProcurementProjectLot>
      <cbc:ID>LOT-2</cbc:ID>
    </cac:ProcurementProjectLot>
    <cac:EvidenceDocumentReference>
      <cbc:ID>VI-REF-2025</cbc:ID>
    </cac:EvidenceDocumentReference>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:LegalMonetaryTotal>
      <cbc:LineExtensionAmount currencyID="XBL">127440.00</cbc:LineExtensionAmount>
      <cbc:PayableAmount currencyID="XBL">127440.00</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
    <cac:TenderLine>
      <cbc:ID>1</cbc:ID>
      <cbc:Note>Serra 180, as specified.</cbc:Note>
      <cbc:Quantity unitCode="H87">240</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">123600.00</cbc:LineExtensionAmount>
      <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">123600.00</cbc:TaxInclusiveLineExtensionAmount>
      <cbc:TotalTaxAmount currencyID="XBL">0.00</cbc:TotalTaxAmount>
      <cbc:OrderableUnit>Pallet of 4</cbc:OrderableUnit>
      <cbc:ContentUnitQuantity unitCode="H87">4</cbc:ContentUnitQuantity>
      <cbc:OrderQuantityIncrementNumeric>4</cbc:OrderQuantityIncrementNumeric>
      <cbc:MinimumOrderQuantity unitCode="H87">20</cbc:MinimumOrderQuantity>
      <cbc:MaximumOrderQuantity unitCode="H87">96</cbc:MaximumOrderQuantity>
      <cbc:WarrantyInformation>Five years on the frame.</cbc:WarrantyInformation>
      <cbc:PackLevelCode>Pallet</cbc:PackLevelCode>
      <cac:DocumentReference>
        <cbc:ID>VI-DS-B180</cbc:ID>
      </cac:DocumentReference>
      <cac:Item>
        <cbc:Name>Park bench Serra 180</cbc:Name>
      </cac:Item>
      <cac:OfferedItemLocationQuantity>
        <cbc:LeadTimeMeasure unitCode="DAY">7</cbc:LeadTimeMeasure>
      </cac:OfferedItemLocationQuantity>
      <cac:ReplacementRelatedItem>
        <cbc:ID>VI-C180-2026</cbc:ID>
        <cbc:Quantity unitCode="H87">1</cbc:Quantity>
      </cac:ReplacementRelatedItem>
      <cac:WarrantyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:WarrantyParty>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">5</cbc:DurationMeasure>
      </cac:WarrantyValidityPeriod>
      <cac:SubTenderLine>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Quantity unitCode="SET">240</cbc:Quantity>
        <cac:Item>
          <cbc:Name>Ground anchor set</cbc:Name>
        </cac:Item>
      </cac:SubTenderLine>
      <cac:CallForTendersLineReference>
        <cbc:LineID>1</cbc:LineID>
      </cac:CallForTendersLineReference>
      <cac:CallForTendersDocumentReference>
        <cbc:ID>PWD-2026-PARKS-CFT</cbc:ID>
      </cac:CallForTendersDocumentReference>
    </cac:TenderLine>
    <cac:TenderLine>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="H87">240</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">3840.00</cbc:LineExtensionAmount>
      <cac:Item>
        <cbc:Name>Installation of a park bench</cbc:Name>
      </cac:Item>
    </cac:TenderLine>
    <cac:AwardingCriterionResponse>
      <cbc:ID>ACR-1</cbc:ID>
      <cbc:AwardingCriterionID>AC-2</cbc:AwardingCriterionID>
      <cbc:AwardingCriterionDescription>Warranty and coating.</cbc:AwardingCriterionDescription>
      <cbc:Description>Ten years on the coating.</cbc:Description>
      <cbc:Quantity unitCode="ANN">10</cbc:Quantity>
      <cbc:Amount currencyID="XBL">127440.00</cbc:Amount>
      <cac:SubordinateAwardingCriterionResponse>
        <cbc:ID>ACR-1.1</cbc:ID>
        <cbc:AwardingCriterionID>AC-2.1</cbc:AwardingCriterionID>
        <cbc:Description>Hot-dip galvanised and powder coated.</cbc:Description>
      </cac:SubordinateAwardingCriterionResponse>
    </cac:AwardingCriterionResponse>
  </cac:TenderedProject>
</Tender>
```
