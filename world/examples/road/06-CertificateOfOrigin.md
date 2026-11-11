# Certificate of Origin: Valdara Industries to Ferrano Chamber of Commerce

*Example 6 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Certificate of Origin in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CERTIFICATE-OF-ORIGIN-SCHEMA)*

The goods qualify for preferential duty in Bayvarra; the manufacturer applies to its chamber of commerce for a certificate of origin.

[The XML file](06-CertificateOfOrigin.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:certificate-of-origin:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Certificate of origin". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FCC-CO-26-0157**  
  The number of the certificate, given by the chamber.
- `UUID` = **a46337e2-176c-5866-9871-158007b21756**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-20**  
  The day the exporter applies, before the goods leave.
- `IssueTime` = **12:39:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Description` = **Certificate of origin for park benches and castings made in Urvania.**  
  What the certificate is for.
- `Note` = **Drakhan dranan karul drek rizir denskek.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): What the certificate is for.
- `Note` = **Preferential origin under the trade accord.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What the certificate is for.
- `VersionID` = **1**  
  The first version.

### Signature

Inside `Signature`:

- `ID` = **VI-SIG-CO-06**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Exporter Party

Inside `ExporterParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3100 = Manufacture of furniture.
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007299291** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)** (languageID `qau`)  
  The name of code SUA in Urvania's national company legal form list. In Urvanian, the sender's language.
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)** (languageID `en-XU`)  
  The name of code SUA in Urvania's national company legal form list. In English.
- `PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 3083 persons and its turnover of 23600000000 XUF in 2025, by the Trade Accord's limits; identity of Valdara Industries (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/SecurityListing/ID` = **XU0001042501** (schemeID `ISO 6166`)  
  The identifier of the listed shares, in the form of an ISIN with the world's country code. The schemeID names the scheme it is from: the ISO 6166 International Securities Identification Number (the issuer's country code, nine letters or digits, a check digit (Luhn)).
- `PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The name of code XFER in the Trade Accord's market identifier list.
- `PartyLegalEntity/SecurityListing/MarketCode` = **XFER** (listID `urn:ubl-examples:world:codelist:MarketCode`)  
  The market's code. The code is from the Trade Accord's market identifier list: XFER = Ferrano Stock Exchange.
- `Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `ServiceProviderParty/ID` = **VI-SP-2026-01**  
  The number of the service contract between the two; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/ServiceTypeCode` = **LOGISTICS** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  The kind of service, as a code. The code is from the Trade Accord's service type list: LOGISTICS = Logistics service.
- `ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1230822** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
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
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **MEDIUM** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 183 persons and its turnover of 33900000.00 XBL in 2025, by the Trade Accord's limits; identity of Lumeway Distribution (world/parties.json). The code is from the Trade Accord's entity size list: MEDIUM = Medium-sized enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Endorser Party

Inside `EndorserParty`:

- `RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `SequenceNumeric` = **1**  
  The first and only endorsement.
- `Party/IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Chamber of Commerce (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 9411 = Activities of business and employers membership organizations.
- `Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Party/PostalAddress/ID` = **4160202319527073** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Trazhek Han Zhatrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/StreetName` = **Piazza del Mercato** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered for value added tax; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007376017** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Chamber of Commerce (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `Party/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/Contact/Name` = **Certificates office**  
  The desk that handles this document; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 041 990 5370**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

### Certificate of Origin Application

Inside `CertificateOfOriginApplication`:

- `ReferenceID` = **VI-AP-26-0158**  
  The exporter's reference for its application.
- `CertificateType` = **Preferential**  
  The goods qualify for the preferential duty rate in Bayvarra; the importer needs this certificate to claim it.
- `ApplicationStatusCode` = **SUBMITTED** (listID `urn:ubl-examples:world:codelist:ApplicationStatusCode`)  
  The exporter submits the application. The code is from the Trade Accord's application status list: SUBMITTED = Submitted.
- `OriginalJobID` = **LD-PO-26-0149**  
  The order the goods are for.
- `PreviousJobID` = **VI-CO-25-0412**  
  The exporter's application of last year for the same goods.
- `Remarks` = **Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.**  
  Why the goods are of Urvanian origin.
- `Shipment/ID` = **CL-SH-26-0154**  
  The shipment the certificate covers.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **4790400** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.**  
  The seller's description; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; item bench-serra of Valdara Industries (world/items.json). A second Keyword would have to be in another language (UBL rule IND7).
- `Shipment/GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The Codana item number of the maker, issued by the Codana Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a number of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label.
- `Shipment/GoodsItem/Item/StandardItemIdentification/IssuerScopeID` = **771**  
  The range of item numbers the agency gives out in the maker's country.
- `Shipment/GoodsItem/Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **94017910** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-serra of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 94017910 = Benches for parks and gardens, with metal frames.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Value` = **Cast steel, hot-dip galvanised**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Value` = **Kiln-dried hardwood**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colour of the frame, one of the colours it is offered in.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; item bench-serra of Valdara Industries (world/items.json)). One ListValue only: UBL rule IND7 allows a second one only in another language.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Load capacity**  
  The name of code LOAD in the Trade Accord's item property name list.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/NameCode` = **LOAD** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: LOAD = Load capacity.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **SF**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `Shipment/GoodsItem/Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `EA`)  
  The emission is per one bench.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/LifecycleStageCode` = **MANUFACTURING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The part of the bench's life the figure covers. The code is from the Trade Accord's life cycle stage list: MANUFACTURING = Manufacturing.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **CRADLETOGATE** (listID `urn:ubl-examples:world:codelist:EmissionBoundaryCode`)  
  How much of the chain is included. The code is from the Trade Accord's emission boundary list: CRADLETOGATE = Cradle to gate.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/MaintenanceFrequencyCode` = **YEARLY** (listID `urn:ubl-examples:world:codelist:MaintenanceFrequencyCode`)  
  How often the item needs maintenance. The code is from the Trade Accord's maintenance frequency list: YEARLY = Once a year.
- `Shipment/GoodsItem/Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **STEEL** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: STEEL = Steel.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **HARDWOOD** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: HARDWOOD = Hardwood.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **PACKAGING** (listID `urn:ubl-examples:world:codelist:WasteTypeCode`)  
  The kind of waste the item leaves. The code is from the Trade Accord's waste type list: PACKAGING = Packaging.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **Stretch film and pallet straps, per bench**  
  The waste in words.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteMeasure` = **0.4** (unitCode `KGM`)  
  How much of it per item.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `Shipment/GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **REPAIR10** (listID `urn:ubl-examples:world:codelist:ScoringSystemCode`)  
  The scale of the score. The code is from the Trade Accord's scoring system list: REPAIR10 = Repairability index, 0 to 10.
- `Shipment/GoodsItem/Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **71760** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, cast steel, galvanised.**  
  The seller's description; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Nanskir drir manskan telstir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting** (languageID `en-XU`)  
  The item's name in English, the working language between the countries; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ModelName` = **Serra 180 side frame**  
  The model; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **VI-C180**  
  The seller's own item number; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The Codana item number of the maker, issued by the Codana Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a number of the world, not a GTIN; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **732599** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 732599 = Other cast articles of iron or steel: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **42999** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 42999 = Metal goods n.e.c..
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **73259990** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; item bench-casting of Valdara Industries (world/items.json). The code is from Urvania's national customs tariff list: 73259990 = Other cast articles of iron or steel.
- `EndorserParty/RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.
- `PreparationParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PreparationParty/PartyName/Name` = **Valdara Industries**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `ExporterParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ExporterParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `ImporterParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ImporterParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuingCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The goods were made in Urvania, and the certificate is issued there. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `DocumentDistribution/ID` = **1**  
  The importer's copy.
- `DocumentDistribution/DistributionTypeCode` = **ELECTRONIC** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  As this document. The code is from the Trade Accord's distribution type list: ELECTRONIC = Electronic.
- `DocumentDistribution/Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DocumentDistribution/Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupportingDocumentReference/ID` = **LD-PO-26-0149**  
  The commercial document behind the goods.
- `Signature/ID` = **VI-SIG-COA**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC-CO-26-0157**  
  The certificate this endorsement belongs to.
- `ApprovalStatus` = **Pending**  
  Not yet endorsed: the application is with the chamber.
- `EndorserParty/RoleCode` = **CHAMBER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The endorser is the chamber of commerce of the exporting country. The code is from the Trade Accord's endorser role list: CHAMBER = Chamber of commerce.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

### Insurance Endorsement

Inside `InsuranceEndorsement`:

- `DocumentID` = **WS-CP-26-4471-E1**  
  The insurer's endorsement of the cargo policy for this consignment.
- `ApprovalStatus` = **Endorsed**  
  The insurer confirms the cover.
- `Remarks` = **The goods described in this certificate are insured door to door.**  
  What it confirms.
- `EndorserParty/RoleCode` = **INSURER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  It endorses as insurer. The code is from the Trade Accord's endorser role list: INSURER = Insurer.
- `EndorserParty/SequenceNumeric` = **2**  
  After the chamber; the embassy legalises separately.
- `EndorserParty/Party/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/Party/PartyName/Name` = **Wavesure Cargo Insurance**  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/SignatoryContact/Name` = **Cargo claims desk**  
  Who signs for the insurer.
- `Signature/ID` = **WS-SIG-26-E1**  
  The insurer's seal on the endorsement.
- `Signature/SignatoryParty/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Wavesure Cargo Insurance**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CertificateOfOrigin xmlns="urn:oasis:names:specification:ubl:schema:xsd:CertificateOfOrigin-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:certificate-of-origin:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FCC-CO-26-0157</cbc:ID>
  <cbc:UUID>a46337e2-176c-5866-9871-158007b21756</cbc:UUID>
  <cbc:IssueDate>2026-03-20</cbc:IssueDate>
  <cbc:IssueTime>12:39:00</cbc:IssueTime>
  <cbc:Description>Certificate of origin for park benches and castings made in Urvania.</cbc:Description>
  <cbc:Note languageID="qau">Drakhan dranan karul drek rizir denskek.</cbc:Note>
  <cbc:Note languageID="en-XU">Preferential origin under the trade accord.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:Signature>
    <cbc:ID>VI-SIG-CO-06</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:ExporterParty>
    <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007299291</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
      <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm languageID="qau">Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)</cbc:CompanyLegalForm>
      <cbc:CompanyLegalForm languageID="en-XU">Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XU:CR</cbc:ID>
        <cbc:Name>Commercial register of Urvania</cbc:Name>
        <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
      <cac:SecurityListing>
        <cbc:ID schemeID="ISO 6166">XU0001042501</cbc:ID>
        <cbc:Description>Ordinary shares of Valdara Industries</cbc:Description>
        <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
        <cbc:MarketCode listID="urn:ubl-examples:world:codelist:MarketCode">XFER</cbc:MarketCode>
      </cac:SecurityListing>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
        <cbc:Value>+999 1 344 474 4274</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
    <cac:ServiceProviderParty>
      <cbc:ID>VI-SP-2026-01</cbc:ID>
      <cbc:ServiceTypeCode listID="urn:ubl-examples:world:codelist:ServiceTypeCode">LOGISTICS</cbc:ServiceTypeCode>
      <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Castrano Logistics</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SellerContact>
        <cbc:Name>Key account desk</cbc:Name>
      </cac:SellerContact>
    </cac:ServiceProviderParty>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:ImporterParty>
    <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1230822</cbc:CompanyID>
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
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:CompanyID>
      <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">MEDIUM</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:EndorserParty>
    <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">CHAMBER</cbc:RoleCode>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202319527073</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Trazhek Han Zhatrir</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Piazza del Mercato</cbc:StreetName>
        <cbc:BuildingNumber>15</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4110</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007376017</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Certificates office</cbc:Name>
        <cbc:JobTitle>Public service officer</cbc:JobTitle>
        <cbc:Department>Public services</cbc:Department>
        <cbc:Telephone>+999 1 041 990 5370</cbc:Telephone>
        <cbc:ElectronicMail>certificates@camera-ferrano.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105370</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
    <cac:SignatoryContact>
      <cbc:Name>Certificates office</cbc:Name>
    </cac:SignatoryContact>
  </cac:EndorserParty>
  <cac:CertificateOfOriginApplication>
    <cbc:ReferenceID>VI-AP-26-0158</cbc:ReferenceID>
    <cbc:CertificateType>Preferential</cbc:CertificateType>
    <cbc:ApplicationStatusCode listID="urn:ubl-examples:world:codelist:ApplicationStatusCode">SUBMITTED</cbc:ApplicationStatusCode>
    <cbc:OriginalJobID>LD-PO-26-0149</cbc:OriginalJobID>
    <cbc:PreviousJobID>VI-CO-25-0412</cbc:PreviousJobID>
    <cbc:Remarks>Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.</cbc:Remarks>
    <cac:Shipment>
      <cbc:ID>CL-SH-26-0154</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Park bench Serra 180</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">4790400</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">96</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
          <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
          <cbc:Name languageID="en-XU">Park bench Serra 180</cbc:Name>
          <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
          <cbc:Keyword>park bench, street furniture</cbc:Keyword>
          <cbc:BrandName>Valdara</cbc:BrandName>
          <cbc:ModelName>Serra 180</cbc:ModelName>
          <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
          <cac:SellersItemIdentification>
            <cbc:ID>VI-B180</cbc:ID>
            <cbc:ExtendedID>GRY</cbc:ExtendedID>
            <cac:PhysicalAttribute>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
              <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
              <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
              <cbc:Description>Frame in Ferro grey</cbc:Description>
            </cac:PhysicalAttribute>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
            <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
            <cbc:IssuerScopeID>771</cbc:IssuerScopeID>
          </cac:StandardItemIdentification>
          <cac:ItemSpecificationDocumentReference>
            <cbc:ID>VI-DS-B180</cbc:ID>
          </cac:ItemSpecificationDocumentReference>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">94017910</cbc:CommodityCode>
          </cac:CommodityClassification>
          <cac:AdditionalItemProperty>
            <cbc:Name>Frame material</cbc:Name>
            <cbc:Value>Cast steel, hot-dip galvanised</cbc:Value>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>Slat wood</cbc:Name>
            <cbc:Value>Kiln-dried hardwood</cbc:Value>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>Seats</cbc:Name>
            <cbc:Value>3</cbc:Value>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:ID>COL</cbc:ID>
            <cbc:Name>Frame colour</cbc:Name>
            <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
            <cbc:ListValue>Ferro grey</cbc:ListValue>
            <cac:ItemPropertyGroup>
              <cbc:ID>APP</cbc:ID>
              <cbc:Name>Appearance</cbc:Name>
              <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
            </cac:ItemPropertyGroup>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:ID>LOAD</cbc:ID>
            <cbc:Name>Load capacity</cbc:Name>
            <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">LOAD</cbc:NameCode>
            <cbc:TestMethod>Static load on the seat for one hour, three seats loaded evenly, no lasting deformation</cbc:TestMethod>
            <cbc:ValueQuantity unitCode="KGM">450</cbc:ValueQuantity>
            <cbc:ValueQualifier>Distributed over the seat</cbc:ValueQualifier>
            <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
            <cac:ItemPropertyGroup>
              <cbc:ID>SAF</cbc:ID>
              <cbc:Name>Safety</cbc:Name>
              <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
            </cac:ItemPropertyGroup>
            <cac:StandardPropertyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:property">UR-SF-0450</cbc:ID>
              <cbc:IssuerScopeID>SF</cbc:IssuerScopeID>
              <cac:IssuerParty>
                <cac:PartyIdentification>
                  <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
                </cac:PartyIdentification>
                <cac:PartyName>
                  <cbc:Name>Codana Identification Agency</cbc:Name>
                </cac:PartyName>
              </cac:IssuerParty>
            </cac:StandardPropertyIdentification>
          </cac:AdditionalItemProperty>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">1800</cbc:Measure>
            <cbc:Description>Over the armrests</cbc:Description>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">DEPTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">620</cbc:Measure>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">780</cbc:Measure>
            <cbc:Description>Seat back at its highest point</cbc:Description>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">450</cbc:Measure>
            <cbc:Description>Above the ground when anchored</cbc:Description>
            <cbc:MinimumMeasure unitCode="MMT">440</cbc:MinimumMeasure>
            <cbc:MaximumMeasure unitCode="MMT">460</cbc:MaximumMeasure>
          </cac:Dimension>
          <cac:EnvironmentalEmission>
            <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
            <cbc:ValueMeasure unitCode="KGM">96</cbc:ValueMeasure>
            <cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>
            <cbc:ValueBaseMeasure unitCode="EA">1</cbc:ValueBaseMeasure>
            <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
            <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">MANUFACTURING</cbc:LifecycleStageCode>
            <cbc:LifecycleStageDescription>From the ore at the mine to the bench leaving the factory gate.</cbc:LifecycleStageDescription>
            <cbc:Description>Mining, steel making, casting, galvanising, sawing and the transport between them.</cbc:Description>
            <cac:EmissionCalculationMethod>
              <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
              <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode">CRADLETOGATE</cbc:FullnessIndicationCode>
              <cbc:EmissionFactorSource>The steelworks' and sawmill's measured energy use of 2025</cbc:EmissionFactorSource>
              <cac:EmissionFactorDocumentReference>
                <cbc:ID>VI-LCA-2025</cbc:ID>
              </cac:EmissionFactorDocumentReference>
            </cac:EmissionCalculationMethod>
            <cac:MeasurementPeriod>
              <cbc:StartDate>2025-01-01</cbc:StartDate>
              <cbc:EndDate>2025-12-31</cbc:EndDate>
            </cac:MeasurementPeriod>
          </cac:EnvironmentalEmission>
          <cac:CircularityProfile>
            <cbc:MaintenanceFrequencyCode listID="urn:ubl-examples:world:codelist:MaintenanceFrequencyCode">YEARLY</cbc:MaintenanceFrequencyCode>
            <cbc:MaintenanceFrequencyDescription>Tighten the slat bolts and touch up the coating once a year.</cbc:MaintenanceFrequencyDescription>
            <cac:ResourceConsumption>
              <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">STEEL</cbc:ResourceTypeCode>
              <cbc:ConsumptionMeasure unitCode="KGM">34</cbc:ConsumptionMeasure>
              <cbc:ResourceOriginDescription>Steel made from Serravona ore in Urvania</cbc:ResourceOriginDescription>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:ResourceConsumption>
            <cac:ResourceConsumption>
              <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">HARDWOOD</cbc:ResourceTypeCode>
              <cbc:ConsumptionMeasure unitCode="KGM">22.5</cbc:ConsumptionMeasure>
              <cbc:ResourceOriginDescription>Slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:ResourceConsumption>
            <cac:WasteGenerated>
              <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:WasteTypeCode">PACKAGING</cbc:WasteTypeCode>
              <cbc:WasteTypeDescription>Stretch film and pallet straps, per bench</cbc:WasteTypeDescription>
              <cbc:WasteMeasure unitCode="KGM">0.4</cbc:WasteMeasure>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:WasteGenerated>
            <cac:RepairabilityScore>
              <cbc:ScoreNumeric>8</cbc:ScoreNumeric>
              <cbc:ScoringSystemCode listID="urn:ubl-examples:world:codelist:ScoringSystemCode">REPAIR10</cbc:ScoringSystemCode>
            </cac:RepairabilityScore>
            <cac:ProductDocumentationDocumentReference>
              <cbc:ID>VI-RM-B180</cbc:ID>
            </cac:ProductDocumentationDocumentReference>
          </cac:CircularityProfile>
        </cac:Item>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Bench side frame casting</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">71760</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Replacement side frame for the Serra bench, cast steel, galvanised.</cbc:Description>
          <cbc:Name languageID="qau">Nanskir drir manskan telstir</cbc:Name>
          <cbc:Name languageID="en-XU">Bench side frame casting</cbc:Name>
          <cbc:BrandName>Valdara</cbc:BrandName>
          <cbc:ModelName>Serra 180 side frame</cbc:ModelName>
          <cac:SellersItemIdentification>
            <cbc:ID>VI-C180</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">732599</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">42999</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">73259990</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:Shipment>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">CHAMBER</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:PreparationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:PreparationParty>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:ExporterParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:ExporterParty>
    <cac:ImporterParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:ImporterParty>
    <cac:IssuingCountry>
      <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
    </cac:IssuingCountry>
    <cac:DocumentDistribution>
      <cbc:ID>1</cbc:ID>
      <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONIC</cbc:DistributionTypeCode>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:DocumentDistribution>
    <cac:SupportingDocumentReference>
      <cbc:ID>LD-PO-26-0149</cbc:ID>
    </cac:SupportingDocumentReference>
    <cac:Signature>
      <cbc:ID>VI-SIG-COA</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:CertificateOfOriginApplication>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>FCC-CO-26-0157</cbc:DocumentID>
    <cbc:ApprovalStatus>Pending</cbc:ApprovalStatus>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">CHAMBER</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
  </cac:IssuerEndorsement>
  <cac:InsuranceEndorsement>
    <cbc:DocumentID>WS-CP-26-4471-E1</cbc:DocumentID>
    <cbc:ApprovalStatus>Endorsed</cbc:ApprovalStatus>
    <cbc:Remarks>The goods described in this certificate are insured door to door.</cbc:Remarks>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">INSURER</cbc:RoleCode>
      <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Wavesure Cargo Insurance</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Cargo claims desk</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:Signature>
      <cbc:ID>WS-SIG-26-E1</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Wavesure Cargo Insurance</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:InsuranceEndorsement>
</CertificateOfOrigin>
```
