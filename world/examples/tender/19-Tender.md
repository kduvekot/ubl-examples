# Tender: Brackenmere Furniture to Lumeport Public Works Department

*Example 19 of the flow "A public tender (Bayvarra)" · [Tender in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TENDER-SCHEMA)*

The furniture maker submits its corrected tender.

[The XML file](19-Tender.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:tender:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Tender"; the community specification "Public procurement community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:tendering:1.0**  
  The Trade Accord's process profile the document belongs to: tendering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **PWD/2026/PARKS**  
  The collaboration this document belongs to: the department's procurement of park benches. Lumeport Public Works Department started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0010**  
  The furniture maker's number for this tender.
- `UUID` = **249604e4-e246-5420-b1d3-0a791c02cd40**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `TenderTypeCode` = **COMBINED** (listID `urn:ubl-examples:world:codelist:TenderTypeCode`)  
  Technical and financial in one. The code is from the Trade Accord's tender type list: COMBINED = Technical and financial together.
- `ContractFolderID` = **PWD/2026/PARKS**  
  The authority's file number for this procurement, the same on every document of the procedure.
- `IssueDate` = **2026-02-23**  
  The corrected tender, submitted after the withdrawal the same day.
- `IssueTime` = **12:10:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `ContractName` = **Park benches for the parks renewal programme**  
  The contract tendered for.
- `Note` = **Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.**  
  What is offered.

### Validity Period

Inside `ValidityPeriod`:

- `DurationMeasure` = **90** (unitCode `DAY`)  
  Valid for 90 days.

### Call For Tender Document Reference

Inside `CallForTenderDocumentReference`:

- `ID` = **PWD/2026/0182**  
  The call for tenders, by its ID.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BKM-DS-PARK**  
  The datasheet.
- `DocumentType` = **Product data sheet**  
  The kind of document referred to, Brackenmere's data sheet of its park bench, in words: no list has an exact code for it.
- `ID` = **3900039354**  
  The certificate of the tender guarantee that covers this tender.
- `DocumentTypeCode` = **GuaranteeCertificate** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document. The code is from the Trade Accord's UBL document type list: GuaranteeCertificate = Guarantee Certificate.

### Signature

Inside `Signature`:

- `ID` = **BF-SIG-TENDER-19**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.

### Tenderer Party

Inside `TendererParty`:

- `WebsiteURI` = **https://www.brackenmere.example**  
  The party's website; as Brackenmere Furniture gives it.
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; as Brackenmere Furniture gives it. The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9523710900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brackenmere Furniture gives it.
- `PartyName/Name` = **Brackenmere Furniture**  
  The trading name; as Brackenmere Furniture gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-821551** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Brackenmere Furniture gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Joiners Row**  
  Street of the postal address. As Brackenmere Furniture gives it.
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. As Brackenmere Furniture gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Brackenmere Furniture gives it.
- `PostalAddress/PostalZone` = **71203**  
  Postal code in Bayvarra's format (5 digits). As Brackenmere Furniture gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Brackenmere Furniture gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered for state sales tax; as Brackenmere Furniture gives it.
- `PartyTaxScheme/CompanyID` = **UL-1237398** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); as Brackenmere Furniture gives it. The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Brackenmere Furniture Ltd**  
  The name under which the party is registered, with its legal form; as Brackenmere Furniture gives it.
- `PartyLegalEntity/CompanyID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **2000-01-12**  
  The day the company was entered in the register; as Brackenmere Furniture gives it.
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)** (languageID `en-XB`)  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 45 persons and its turnover of 6830000.00 XBL in 2025, by the Trade Accord's limits; as Brackenmere Furniture gives it. The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world.
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Bids office**  
  The party's bids office desk: the desk for its role in this document (it bids); as Brackenmere Furniture gives it.
- `Contact/JobTitle` = **Bid manager**  
  The job of the person who answers at the desk; as Brackenmere Furniture gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Brackenmere Furniture gives it.
- `Contact/Telephone` = **+999 2 7121 602 606**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Brackenmere Furniture gives it.
- `Contact/ElectronicMail` = **tenders@brackenmere.example**  
  The contact's e-mail address; as Brackenmere Furniture gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Brackenmere Furniture gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412466** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brackenmere Furniture gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tenderer Qualification Document Reference

Inside `TendererQualificationDocumentReference`:

- `ID` = **26-0006**  
  The furniture maker's response to the qualification questionnaire, which qualifies it.
- `DocumentTypeCode` = **QualificationApplicationResponse** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document: the response to the qualification questionnaire, the furniture maker's qualification. The code is from the Trade Accord's UBL document type list: QualificationApplicationResponse = Qualification Application Response.

### Contracting Party

Inside `ContractingParty`:

- `Party/PartyIdentification/ID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; as Lumeport Public Works Department gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-000417** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Public Works Department gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Public Works Department gives it.
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Public Works Department gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Public Works Department gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The public body's official name; as Lumeport Public Works Department gives it.
- `Party/PartyLegalEntity/CompanyID` = **6250397184** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register ; as Lumeport Public Works Department gives it. The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Party/Contact/Name` = **Procurement office**  
  The party's main desk, which handles this document; as Lumeport Public Works Department gives it.
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; as Lumeport Public Works Department gives it.
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; as Lumeport Public Works Department gives it.
- `Party/Contact/Telephone` = **+999 2 38 8235 3927**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeport Public Works Department gives it.
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  The contact's e-mail address; as Lumeport Public Works Department gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Public Works Department gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:6250397184** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Lumeport Public Works Department gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Tendered Project

Inside `TenderedProject`:

- `VariantID` = **V0**  
  The main offer; no variant is tendered.
- `TenderEnvelopeID` = **ENV-1**  
  The envelope.
- `TenderEnvelopeTypeCode` = **COMBINED** (listID `urn:ubl-examples:world:codelist:TenderEnvelopeCode`)  
  Technical and price together. The code is from the Trade Accord's tender envelope list: COMBINED = Technical and financial together.
- `AdditionalFee/FeeTypeCode` = **COURIER** (listID `urn:ubl-examples:world:codelist:FeeTypeCode`)  
  A courier fee. The code is from the Trade Accord's fee type list: COURIER = Courier fee.
- `AdditionalFee/FeeAmount` = **12.00** (currencyID `XBL`)  
  For the signed original.
- `AdditionalFee/FeeDescription` = **Courier of the bank's original certificate of the immobilised bonds to the department.**  
  What: the pledge needs the original, a bank guarantee does not.
- `ProcurementProjectLot/ID` = **LOT-1**  
  Lot 1.
- `ProcurementProjectLot/ID` = **LOT-2**  
  Lot 2.
- `EvidenceDocumentReference/ID` = **BKM-REF-2025**  
  The tenderer's own reference letters.
- `EvidenceDocumentReference/DocumentType` = **Reference letters**  
  The kind of document referred to, Brackenmere's reference letters from customers for its park furniture of 2025, in words: no list has an exact code for it.
- `TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  No tax: the department, a public body, buys exempt from the state sales tax.
- `TaxTotal/TaxSubtotal/TaxableAmount` = **119040.00** (currencyID `XBL`)  
  Both lots, the whole tendered amount.
- `TaxTotal/TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  Nothing at a rate of 0 %.
- `TaxTotal/TaxSubtotal/TaxCategory/ID` = **E** (schemeID `UN/EDIFACT EDED 5305`)  
  A sale to a public body is exempt from the state sales tax (category E). The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: E = Exempt from tax. An identifier that holds a code names the code's list in its schemeID.
- `TaxTotal/TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxTotal/TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **PUBLIC** (listID `urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode`)  
  The exemption reason as a code of Bayvarra's national list, the list of the seller's country. The code is from Bayvarra's national sales tax exemption reason list: PUBLIC = Public body.
- `TaxTotal/TaxSubtotal/TaxCategory/TaxExemptionReason` = **Public body**  
  The name of code PUBLIC in Bayvarra's national sales tax exemption reason list.
- `TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `LegalMonetaryTotal/LineExtensionAmount` = **119040.00** (currencyID `XBL`)  
  Both lots.
- `LegalMonetaryTotal/PayableAmount` = **119040.00** (currencyID `XBL`)  
  The tender's total.
- `TenderLine/ID` = **1**  
  The benches.
- `TenderLine/Note` = **A bench of its own make: steel frame, hardwood slats; spare slat sets available.**  
  What is offered.
- `TenderLine/Quantity` = **240** (unitCode `EA`)  
  240 benches.
- `TenderLine/LineExtensionAmount` = **115200.00** (currencyID `XBL`)  
  240 at the unit price.
- `TenderLine/TaxInclusiveLineExtensionAmount` = **115200.00** (currencyID `XBL`)  
  No tax for a public body.
- `TenderLine/TotalTaxAmount` = **0.00** (currencyID `XBL`)  
  No tax for a public body.
- `TenderLine/OrderableUnit` = **Pallet of 2**  
  Called off in pallets.
- `TenderLine/ContentUnitQuantity` = **2** (unitCode `EA`)  
  2 per pallet.
- `TenderLine/OrderQuantityIncrementNumeric` = **2**  
  In steps of 2.
- `TenderLine/MinimumOrderQuantity` = **10** (unitCode `EA`)  
  A release of at least 10.
- `TenderLine/MaximumOrderQuantity` = **60** (unitCode `EA`)  
  At most what its workshop makes in a fortnight.
- `TenderLine/WarrantyInformation` = **Six years on the frame and the slats.**  
  The warranty on the bench, as the quality criterion's answer gives it.
- `TenderLine/PackLevelCode` = **PALLET** (listID `urn:ubl-examples:world:codelist:PackLevelCode`)  
  The pack level. The code is from the Trade Accord's pack level list: PALLET = Pallet.
- `TenderLine/DocumentReference/ID` = **BKM-DS-PARK**  
  The datasheet.
- `TenderLine/DocumentReference/DocumentType` = **Product data sheet**  
  The kind of document referred to, Brackenmere's data sheet of its park bench, in words: no list has an exact code for it.
- `TenderLine/Item/Name` = **Park bench Brackenmere PB-2**  
  The item offered.
- `TenderLine/OfferedItemLocationQuantity/LeadTimeMeasure` = **14** (unitCode `DAY`)  
  14 days per release.
- `TenderLine/OfferedItemLocationQuantity/Price/PriceAmount` = **480** (currencyID `XBL`)  
  The unit price offered, which the procedure evaluates and auctions.
- `TenderLine/OfferedItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  Per bench.
- `TenderLine/WarrantyParty/PartyIdentification/ID` = **20412466** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderLine/WarrantyParty/PartyName/Name` = **Brackenmere Furniture**  
  A party referred to from another party's details: its identifier and name are enough.
- `TenderLine/WarrantyValidityPeriod/DurationMeasure` = **6** (unitCode `ANN`)  
  The years of warranty.
- `TenderLine/SubTenderLine/ID` = **1.1**  
  The anchors.
- `TenderLine/SubTenderLine/Quantity` = **240** (unitCode `SET`)  
  One set per bench.
- `TenderLine/SubTenderLine/Item/Name` = **Ground anchor set**  
  Included.
- `TenderLine/CallForTendersLineReference/LineID` = **1**  
  The line of the call for tenders.
- `TenderLine/CallForTendersDocumentReference/ID` = **PWD/2026/0182**  
  The call for tenders.
- `TenderLine/ID` = **2**  
  The installation.
- `TenderLine/Quantity` = **240** (unitCode `EA`)  
  240 installations.
- `TenderLine/LineExtensionAmount` = **3840.00** (currencyID `XBL`)  
  240 at the price.
- `TenderLine/Item/Name` = **Installation of a park bench**  
  The service.
- `TenderLine/OfferedItemLocationQuantity/Price/PriceAmount` = **16** (currencyID `XBL`)  
  The unit price of one installation.
- `TenderLine/OfferedItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `EA`)  
  Per installation.
- `AwardingCriterionResponse/ID` = **ACR-1**  
  The response to the price criterion.
- `AwardingCriterionResponse/AwardingCriterionID` = **AC-1**  
  Price.
- `AwardingCriterionResponse/AwardingCriterionDescription` = **The lowest total of unit prices.**  
  The criterion.
- `AwardingCriterionResponse/Description` = **480.00 lume a bench and 16.00 lume an installation.**  
  The unit prices the criterion evaluates.
- `AwardingCriterionResponse/Amount` = **119040.00** (currencyID `XBL`)  
  The tendered total of the unit prices for both lots.
- `AwardingCriterionResponse/ID` = **ACR-2**  
  The response to the quality criterion.
- `AwardingCriterionResponse/AwardingCriterionID` = **AC-2**  
  Quality.
- `AwardingCriterionResponse/AwardingCriterionDescription` = **Durability and warranty of the coating, and the lead time per release.**  
  The criterion.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/ID` = **ACR-2.1**  
  Durability.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/AwardingCriterionID` = **AC-2.1**  
  Its criterion.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/Description` = **Oiled hardwood, painted steel.**  
  The offer.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/ID` = **ACR-2.2**  
  Warranty.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/AwardingCriterionID` = **AC-2.2**  
  Its criterion.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/Description` = **Six years on the frame and the slats.**  
  The offer.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/Quantity` = **6** (unitCode `ANN`)  
  The years of warranty offered.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/ID` = **ACR-2.3**  
  Lead time.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/AwardingCriterionID` = **AC-2.3**  
  Its criterion.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/Description` = **14 days per release.**  
  The offer, as the tender line gives it.
- `AwardingCriterionResponse/SubordinateAwardingCriterionResponse/Quantity` = **14** (unitCode `DAY`)  
  The days from an order to its delivery.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Tender xmlns="urn:oasis:names:specification:ubl:schema:xsd:Tender-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:tender:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:tendering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>PWD/2026/PARKS</cbc:ProfileExecutionID>
  <cbc:ID>26-0010</cbc:ID>
  <cbc:UUID>249604e4-e246-5420-b1d3-0a791c02cd40</cbc:UUID>
  <cbc:TenderTypeCode listID="urn:ubl-examples:world:codelist:TenderTypeCode">COMBINED</cbc:TenderTypeCode>
  <cbc:ContractFolderID>PWD/2026/PARKS</cbc:ContractFolderID>
  <cbc:IssueDate>2026-02-23</cbc:IssueDate>
  <cbc:IssueTime>12:10:00-01:00</cbc:IssueTime>
  <cbc:ContractName>Park benches for the parks renewal programme</cbc:ContractName>
  <cbc:Note>Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.</cbc:Note>
  <cac:ValidityPeriod>
    <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
  </cac:ValidityPeriod>
  <cac:CallForTenderDocumentReference>
    <cbc:ID>PWD/2026/0182</cbc:ID>
  </cac:CallForTenderDocumentReference>
  <cac:DocumentReference>
    <cbc:ID>BKM-DS-PARK</cbc:ID>
    <cbc:DocumentType>Product data sheet</cbc:DocumentType>
  </cac:DocumentReference>
  <cac:DocumentReference>
    <cbc:ID>3900039354</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">GuaranteeCertificate</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>BF-SIG-TENDER-19</cbc:ID>
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
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9523710900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brackenmere Furniture</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-821551</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Joiners Row</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71203</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1237398</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Brackenmere Furniture Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:CompanyID>
      <cbc:RegistrationDate>2000-01-12</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="en-XB">Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Marrowdale</cbc:CityName>
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
      <cbc:Name>Bids office</cbc:Name>
      <cbc:JobTitle>Bid manager</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 602 606</cbc:Telephone>
      <cbc:ElectronicMail>tenders@brackenmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412466</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:TendererParty>
  <cac:TendererQualificationDocumentReference>
    <cbc:ID>26-0006</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">QualificationApplicationResponse</cbc:DocumentTypeCode>
  </cac:TendererQualificationDocumentReference>
  <cac:ContractingParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-000417</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
        <cbc:Department>Procurement office</cbc:Department>
        <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
        <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">6250397184</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Procurement office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 38 8235 3927</cbc:Telephone>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:6250397184</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:ContractingParty>
  <cac:TenderedProject>
    <cbc:VariantID>V0</cbc:VariantID>
    <cbc:TenderEnvelopeID>ENV-1</cbc:TenderEnvelopeID>
    <cbc:TenderEnvelopeTypeCode listID="urn:ubl-examples:world:codelist:TenderEnvelopeCode">COMBINED</cbc:TenderEnvelopeTypeCode>
    <cac:AdditionalFee>
      <cbc:FeeTypeCode listID="urn:ubl-examples:world:codelist:FeeTypeCode">COURIER</cbc:FeeTypeCode>
      <cbc:FeeAmount currencyID="XBL">12.00</cbc:FeeAmount>
      <cbc:FeeDescription>Courier of the bank's original certificate of the immobilised bonds to the department.</cbc:FeeDescription>
    </cac:AdditionalFee>
    <cac:ProcurementProjectLot>
      <cbc:ID>LOT-1</cbc:ID>
    </cac:ProcurementProjectLot>
    <cac:ProcurementProjectLot>
      <cbc:ID>LOT-2</cbc:ID>
    </cac:ProcurementProjectLot>
    <cac:EvidenceDocumentReference>
      <cbc:ID>BKM-REF-2025</cbc:ID>
      <cbc:DocumentType>Reference letters</cbc:DocumentType>
    </cac:EvidenceDocumentReference>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxSubtotal>
        <cbc:TaxableAmount currencyID="XBL">119040.00</cbc:TaxableAmount>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
        <cac:TaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">E</cbc:ID>
          <cbc:Percent>0</cbc:Percent>
          <cbc:TaxExemptionReasonCode listID="urn:ubl-examples:world:XB:codelist:TaxExemptionReasonCode">PUBLIC</cbc:TaxExemptionReasonCode>
          <cbc:TaxExemptionReason>Public body</cbc:TaxExemptionReason>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          </cac:TaxScheme>
        </cac:TaxCategory>
      </cac:TaxSubtotal>
    </cac:TaxTotal>
    <cac:LegalMonetaryTotal>
      <cbc:LineExtensionAmount currencyID="XBL">119040.00</cbc:LineExtensionAmount>
      <cbc:PayableAmount currencyID="XBL">119040.00</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
    <cac:TenderLine>
      <cbc:ID>1</cbc:ID>
      <cbc:Note>A bench of its own make: steel frame, hardwood slats; spare slat sets available.</cbc:Note>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">115200.00</cbc:LineExtensionAmount>
      <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">115200.00</cbc:TaxInclusiveLineExtensionAmount>
      <cbc:TotalTaxAmount currencyID="XBL">0.00</cbc:TotalTaxAmount>
      <cbc:OrderableUnit>Pallet of 2</cbc:OrderableUnit>
      <cbc:ContentUnitQuantity unitCode="EA">2</cbc:ContentUnitQuantity>
      <cbc:OrderQuantityIncrementNumeric>2</cbc:OrderQuantityIncrementNumeric>
      <cbc:MinimumOrderQuantity unitCode="EA">10</cbc:MinimumOrderQuantity>
      <cbc:MaximumOrderQuantity unitCode="EA">60</cbc:MaximumOrderQuantity>
      <cbc:WarrantyInformation>Six years on the frame and the slats.</cbc:WarrantyInformation>
      <cbc:PackLevelCode listID="urn:ubl-examples:world:codelist:PackLevelCode">PALLET</cbc:PackLevelCode>
      <cac:DocumentReference>
        <cbc:ID>BKM-DS-PARK</cbc:ID>
        <cbc:DocumentType>Product data sheet</cbc:DocumentType>
      </cac:DocumentReference>
      <cac:Item>
        <cbc:Name>Park bench Brackenmere PB-2</cbc:Name>
      </cac:Item>
      <cac:OfferedItemLocationQuantity>
        <cbc:LeadTimeMeasure unitCode="DAY">14</cbc:LeadTimeMeasure>
        <cac:Price>
          <cbc:PriceAmount currencyID="XBL">480</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:OfferedItemLocationQuantity>
      <cac:WarrantyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412466</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brackenmere Furniture</cbc:Name>
        </cac:PartyName>
      </cac:WarrantyParty>
      <cac:WarrantyValidityPeriod>
        <cbc:DurationMeasure unitCode="ANN">6</cbc:DurationMeasure>
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
        <cbc:ID>PWD/2026/0182</cbc:ID>
      </cac:CallForTendersDocumentReference>
    </cac:TenderLine>
    <cac:TenderLine>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">3840.00</cbc:LineExtensionAmount>
      <cac:Item>
        <cbc:Name>Installation of a park bench</cbc:Name>
      </cac:Item>
      <cac:OfferedItemLocationQuantity>
        <cac:Price>
          <cbc:PriceAmount currencyID="XBL">16</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="EA">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:OfferedItemLocationQuantity>
    </cac:TenderLine>
    <cac:AwardingCriterionResponse>
      <cbc:ID>ACR-1</cbc:ID>
      <cbc:AwardingCriterionID>AC-1</cbc:AwardingCriterionID>
      <cbc:AwardingCriterionDescription>The lowest total of unit prices.</cbc:AwardingCriterionDescription>
      <cbc:Description>480.00 lume a bench and 16.00 lume an installation.</cbc:Description>
      <cbc:Amount currencyID="XBL">119040.00</cbc:Amount>
    </cac:AwardingCriterionResponse>
    <cac:AwardingCriterionResponse>
      <cbc:ID>ACR-2</cbc:ID>
      <cbc:AwardingCriterionID>AC-2</cbc:AwardingCriterionID>
      <cbc:AwardingCriterionDescription>Durability and warranty of the coating, and the lead time per release.</cbc:AwardingCriterionDescription>
      <cac:SubordinateAwardingCriterionResponse>
        <cbc:ID>ACR-2.1</cbc:ID>
        <cbc:AwardingCriterionID>AC-2.1</cbc:AwardingCriterionID>
        <cbc:Description>Oiled hardwood, painted steel.</cbc:Description>
      </cac:SubordinateAwardingCriterionResponse>
      <cac:SubordinateAwardingCriterionResponse>
        <cbc:ID>ACR-2.2</cbc:ID>
        <cbc:AwardingCriterionID>AC-2.2</cbc:AwardingCriterionID>
        <cbc:Description>Six years on the frame and the slats.</cbc:Description>
        <cbc:Quantity unitCode="ANN">6</cbc:Quantity>
      </cac:SubordinateAwardingCriterionResponse>
      <cac:SubordinateAwardingCriterionResponse>
        <cbc:ID>ACR-2.3</cbc:ID>
        <cbc:AwardingCriterionID>AC-2.3</cbc:AwardingCriterionID>
        <cbc:Description>14 days per release.</cbc:Description>
        <cbc:Quantity unitCode="DAY">14</cbc:Quantity>
      </cac:SubordinateAwardingCriterionResponse>
    </cac:AwardingCriterionResponse>
  </cac:TenderedProject>
</Tender>
```
