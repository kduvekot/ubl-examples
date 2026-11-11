# Forwarding Instructions: Saltmere Engineering to Bayforth Forwarding

*Example 2 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

The engineering firm instructs the forwarder, with the shipper's declaration of dangerous goods.

[The XML file](02-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:mast**  
  The business process the document belongs to: the flow "Batteries for the island's telecom mast, by air (dangerous goods)".
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SE-FI-26-0714**  
  The instruction number.
- `UUID` = **a587c22d-2b9a-58c7-a95e-3c142f8b615c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-03**  
  With the shipper's declaration of dangerous goods.
- `IssueTime` = **11:57:00**  
  The time the sender's system issued the document, in the sender's local time.

### Consignor Party

Inside `ConsignorParty`:

- `IndustryClassificationCode` = **4290** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Saltmere Engineering (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4290 = Construction of other civil engineering projects.
- `PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered for state sales tax; identity of Saltmere Engineering (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1232055**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Saltmere Engineering (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered, with its legal form; identity of Saltmere Engineering (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410685**  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
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
- `Contact/Name` = **Bids office**  
  The desk that handles this document; identity of Saltmere Engineering (world/parties.json).
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 885 685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `WebsiteURI` = **https://www.bayforth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Bayforth Forwarding (world/parties.json).
- `IndustryClassificationCode` = **5229** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Bayforth Forwarding (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5229 = Other transportation support activities.
- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered for state sales tax; identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1234932**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411644**  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 40 persons and its turnover of 6660000.00 XBL in 2025, by the Trade Accord's limits; identity of Bayforth Forwarding (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Contact/Name` = **Export desk**  
  The desk that handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2144 1644**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **SE-SH-26-0715**  
  The shipment.
- `GrossWeightMeasure` = **376** (unitCode `KGM`)  
  The gross weight.
- `Consignment/ID` = **SE-CS-26-0716**  
  The consignment.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.selanutelecom.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **6110** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Telecom (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 6110 = Wired telecommunications activities.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Consignment/ConsigneeParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **IC42407**  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The name of code LTD in Lisavu's national company legal form list.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 20 persons and its turnover of 3230000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Telecom (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/Contact/Name` = **Business accounts**  
  The desk that handles this document; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 727 2407**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/HazardousItemNotificationParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/HazardousItemNotificationParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/ID` = **RKN-41207-KC**  
  The container as a handling unit.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods inside.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **RKN-41207-KC**  
  The temperature-controlled air container.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **AM** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code AM: refrigerated container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: AM = Refrigerated container.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  The unit is switched on.
- `Consignment/TransportHandlingUnit/TransportEquipment/AirFlowPercent` = **40**  
  The fan's air flow.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumidityPercent` = **50**  
  Humidity kept below 50 %.
- `Consignment/TransportHandlingUnit/TransportEquipment/AnimalFoodApprovedIndicator` = **false**  
  Not for feed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumanFoodApprovedIndicator` = **false**  
  Not for food.
- `Consignment/TransportHandlingUnit/TransportEquipment/DangerousGoodsApprovedIndicator` = **true**  
  Approved for dangerous goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **true**  
  A temperature-controlled unit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **true**  
  Battery-powered cooling and heating.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %.**  
  The conditions.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ID` = **SE-BAT-48100-DG**  
  The battery packs in the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations UN number`)  
  The UN number of the battery packs. The code is from the world's copy of UN Model Regulations dangerous goods list (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/CategoryName` = **Miscellaneous dangerous goods**  
  Class 9 in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ProperShippingName` = **Lithium ion batteries**  
  As on the declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UpperOrangeHazardPlacardID` = **90**  
  The hazard identification number for road transport.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/LowerOrangeHazardPlacardID` = **3480**  
  The UN number on the orange plate.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardClassID` = **9**  
  Class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousTypeCode` = **ARTICLE** (listID `urn:ubl-examples:world:codelist:HazardousGoodsTypeCode`)  
  Batteries are articles, not substances. The code is from the Trade Accord's dangerous goods type list: ARTICLE = Article.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PackagingDangerLevelCode` = **4** (listID `UN/EDIFACT EDED 8339`)  
  The packaging danger level of UN/EDIFACT 8339 that matches the packing group: lithium batteries have none, which 8339 codes as not assigned. The code is from the world's copy of UN/EDIFACT 8339 Packaging danger level: 4 = Not assigned.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/GrossWeightMeasure` = **348** (unitCode `KGM`)  
  Six packs, packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetWeightMeasure` = **312** (unitCode `KGM`)  
  The packs alone.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetVolumeMeasure` = **0.24** (unitCode `MTQ`)  
  Their volume.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Quantity` = **6** (unitCode `EA`)  
  Six packs.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %.**  
  The conditions.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/EmergencyTemperature/AttributeID` = **Emergency**  
  Above this, emergency procedures.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/EmergencyTemperature/Measure` = **60** (unitCode `CEL`)  
  Thermal runaway risk.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/AdditionalTemperature/AttributeID` = **Storage**  
  Recommended storage.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/AdditionalTemperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/LocationID` = **MD-L2**  
  Main deck, position L2.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/Location` = **Main deck, accessible**  
  Where it flies.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/ID` = **SE-CR-1..6**  
  The six crates.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/Quantity` = **6** (unitCode `EA`)  
  Six.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %.**  
  The conditions.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **Battery**  
  Lithium-ion packs must not freeze nor overheat.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `GoodsItem/ID` = **1**  
  A goods item.
- `GoodsItem/Description` = **Lithium-ion battery pack 48 V 100 Ah**  
  The goods.
- `GoodsItem/Item/Description` = **Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.**  
  The seller's description; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/Name` = **Lithium-ion battery pack 48 V 100 Ah**  
  The item's short name; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `GoodsItem/Item/SellersItemIdentification/ID` = **SE-BAT-48100**  
  The seller's own item number; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/StandardItemIdentification/ID` = **772050000117** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **850760** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 850760 = Lithium-ion accumulators.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **46420** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item battery-pack of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 46420 = Electric accumulators.
- `GoodsItem/Item/HazardousItem/ID` = **SE-BAT-48100-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **9**  
  The class shown on the placard.
- `GoodsItem/Item/HazardousItem/PlacardEndorsement` = **9A**  
  The hazard label on the package.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations UN number`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations dangerous goods list (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/EmergencyProceduresCode` = **F-A,S-I** (listID `IMO IMDG EmS`)  
  The emergency schedules for ships (EmS) of the IMDG Code for this UN entry: the fire schedule and the spillage schedule. The code is from the world's copy of IMO IMDG Code emergency schedules (EmS): F-A,S-I = Fire schedule Alpha, spillage schedule India.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **147** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 147 = Lithium Ion and Sodium Ion Batteries.
- `GoodsItem/Item/HazardousItem/TunnelRestrictionCode` = **E** (listID `UNECE ADR tunnel restriction code`)  
  The tunnel restriction code for road transport. The code is from the world's copy of ADR tunnel restriction code: E.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **9** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **9**  
  The UN hazard class.
- `GoodsItem/Temperature/AttributeID` = **Transport**  
  The temperature in transport.
- `GoodsItem/Temperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `GoodsItem/Temperature/MeasureCode` = **TARGET** (listID `urn:ubl-examples:world:codelist:TemperatureQualifierCode`)  
  The target. The code is from the Trade Accord's temperature qualifier list: TARGET = Target.
- `GoodsItem/Temperature/Description` = **Keep away from heat.**  
  Why.
- `GoodsItem/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  At least.
- `GoodsItem/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  At most.
- `GoodsItem/ID` = **2**  
  A goods item.
- `GoodsItem/Description` = **Ionisation smoke detector set**  
  The goods.
- `GoodsItem/Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/Name` = **Ionisation smoke detector set**  
  The item's short name; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `GoodsItem/Item/SellersItemIdentification/ID` = **SE-SMK-10**  
  The seller's own item number; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/StandardItemIdentification/ID` = **772050000124** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **853110** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 853110 = Burglar or fire alarms and similar apparatus.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **46921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item smoke-detector of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 46921 = Burglar or fire alarms and similar apparatus.
- `GoodsItem/Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the placard.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label, the UN number on the package.**  
  What the shipper adds.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2911** (listID `UN Model Regulations UN number`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations dangerous goods list (UN numbers): 2911 = Radioactive material, excepted package – instruments or articles.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/EmergencyProceduresCode` = **F-I,S-S** (listID `IMO IMDG EmS`)  
  The emergency schedules for ships (EmS) of the IMDG Code for this UN entry: the fire schedule and the spillage schedule. The code is from the world's copy of IMO IMDG Code emergency schedules (EmS): F-I,S-S = Fire schedule India, spillage schedule Sierra.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **161** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 161 = Radioactive Materials (Low Level Radiation).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2911**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **7**  
  The UN hazard class.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Americium-241 sources in smoke detectors**  
  The material.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Sealed source, not special form.**  
  Its form.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **0**  
  Excepted package: no dose rate to speak of.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/FissileCriticalitySafetyIndexNumeric` = **0**  
  Not fissile.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/Name` = **Americium-241**  
  The isotope.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/ActivityLevelMeasure` = **37** (unitCode `2Q`)  
  Per detector.
- `GoodsItem/Temperature/AttributeID` = **Transport**  
  The temperature in transport.
- `GoodsItem/Temperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `GoodsItem/Temperature/MeasureCode` = **TARGET** (listID `urn:ubl-examples:world:codelist:TemperatureQualifierCode`)  
  The target. The code is from the Trade Accord's temperature qualifier list: TARGET = Target.
- `GoodsItem/Temperature/Description` = **Keep away from heat.**  
  Why.
- `GoodsItem/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  At least.
- `GoodsItem/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  At most.
- `GoodsItem/ID` = **3**  
  A goods item.
- `GoodsItem/Description` = **Coating stripper for electronics**  
  The goods.
- `GoodsItem/Item/Description` = **Remover for the protective coating of circuit boards, in 5-litre cans.**  
  The seller's description; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/Name` = **Coating stripper for electronics**  
  The item's short name; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `GoodsItem/Item/SellersItemIdentification/ID` = **SE-CS-05**  
  The seller's own item number; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/StandardItemIdentification/ID` = **772050000131** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **381400** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 381400 = Organic composite solvents and thinners, n.e.s.; prepared paint or varnish removers.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **35110** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item coating-stripper of Saltmere Engineering (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 35110 = Paints and varnishes and related products.
- `GoodsItem/Item/HazardousItem/ID` = **SE-CS-05-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **8**  
  The class shown on the placard.
- `GoodsItem/Item/HazardousItem/PlacardEndorsement` = **8**  
  The hazard label on the package.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Packed as the rules require.**  
  What the shipper adds.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2920** (listID `UN Model Regulations UN number`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations dangerous goods list (UN numbers): 2920 = Corrosive liquid, flammable, n.o.s..
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **II** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: II = Medium danger.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **Medium danger**  
  The name of code II in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/EmergencyProceduresCode` = **F-E,S-C** (listID `IMO IMDG EmS`)  
  The emergency schedules for ships (EmS) of the IMDG Code for this UN entry: the fire schedule and the spillage schedule. The code is from the world's copy of IMO IMDG Code emergency schedules (EmS): F-E,S-C = Fire schedule Echo, spillage schedule Charlie.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **132** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 132 = Flammable Liquids - Corrosive.
- `GoodsItem/Item/HazardousItem/TunnelRestrictionCode` = **D/E** (listID `UNECE ADR tunnel restriction code`)  
  The tunnel restriction code for road transport. The code is from the world's copy of ADR tunnel restriction code: D/E.
- `GoodsItem/Item/HazardousItem/MaritimePollutantCode` = **N** (listID `urn:ubl-examples:world:codelist:MarinePollutantCode`)  
  Not a marine pollutant. The code is from the Trade Accord's marine pollutant list: N = Not a marine pollutant.
- `GoodsItem/Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **8** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2920**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **8**  
  The UN hazard class.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/ID` = **3**  
  The subsidiary hazard: flammable.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/PlacardNotation` = **3**  
  Shown on a second label.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/PlacardEndorsement` = **3**  
  The flammable liquid label.
- `GoodsItem/Item/HazardousItem/SecondaryHazard/Extension` = **Subsidiary risk 3**  
  In words.
- `GoodsItem/Item/HazardousItem/FlashpointTemperature/AttributeID` = **Flashpoint**  
  Closed cup.
- `GoodsItem/Item/HazardousItem/FlashpointTemperature/Measure` = **28** (unitCode `CEL`)  
  The flashpoint.
- `GoodsItem/Temperature/AttributeID` = **Transport**  
  The temperature in transport.
- `GoodsItem/Temperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `GoodsItem/Temperature/MeasureCode` = **TARGET** (listID `urn:ubl-examples:world:codelist:TemperatureQualifierCode`)  
  The target. The code is from the Trade Accord's temperature qualifier list: TARGET = Target.
- `GoodsItem/Temperature/Description` = **Keep away from heat.**  
  Why.
- `GoodsItem/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  At least.
- `GoodsItem/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  At most.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:mast</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SE-FI-26-0714</cbc:ID>
  <cbc:UUID>a587c22d-2b9a-58c7-a95e-3c142f8b615c</cbc:UUID>
  <cbc:IssueDate>2026-06-03</cbc:IssueDate>
  <cbc:IssueTime>11:57:00</cbc:IssueTime>
  <cac:ConsignorParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4290</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Saltmere Engineering</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Foundry Road</cbc:StreetName>
      <cbc:BuildingNumber>13</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71218</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
      <cbc:CompanyID>UL-1232055</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
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
      <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
      <cbc:CompanyID>20410685</cbc:CompanyID>
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
      <cbc:JobTitle>Procurement officer</cbc:JobTitle>
      <cbc:Department>Procurement</cbc:Department>
      <cbc:Telephone>+999 2 7121 885 685</cbc:Telephone>
      <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ConsignorParty>
  <cac:FreightForwarderParty>
    <cbc:WebsiteURI>https://www.bayforth.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5229</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID>CO-1234932</cbc:CompanyID>
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
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20411644</cbc:CompanyID>
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
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38 2144 1644</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>SE-SH-26-0715</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">376</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>SE-CS-26-0716</cbc:ID>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:ConsigneeParty>
        <cbc:WebsiteURI>https://www.selanutelecom.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">6110</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Telecom</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XB">Mast Hill Road</cbc:StreetName>
          <cbc:BuildingNumber>58</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Selanu Telecom Ltd</cbc:RegistrationName>
          <cbc:CompanyID>IC42407</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
          <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
          <cac:RegistrationAddress>
            <cbc:CityName>Selanu</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:RegistrationAddress>
          <cac:CorporateRegistrationScheme>
            <cbc:ID>XL:ICR</cbc:ID>
            <cbc:Name>Island companies register</cbc:Name>
            <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
            <cac:JurisdictionRegionAddress>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:CorporateRegistrationScheme>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Business accounts</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 3 727 2407</cbc:Telephone>
          <cbc:ElectronicMail>business@selanutelecom.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
      <cac:HazardousItemNotificationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
      </cac:HazardousItemNotificationParty>
      <cac:TransportHandlingUnit>
        <cbc:ID>RKN-41207-KC</cbc:ID>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportEquipment>
          <cbc:ID>RKN-41207-KC</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">AM</cbc:TransportEquipmentTypeCode>
          <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
          <cbc:AirFlowPercent>40</cbc:AirFlowPercent>
          <cbc:HumidityPercent>50</cbc:HumidityPercent>
          <cbc:AnimalFoodApprovedIndicator>false</cbc:AnimalFoodApprovedIndicator>
          <cbc:HumanFoodApprovedIndicator>false</cbc:HumanFoodApprovedIndicator>
          <cbc:DangerousGoodsApprovedIndicator>true</cbc:DangerousGoodsApprovedIndicator>
          <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
          <cbc:PowerIndicator>true</cbc:PowerIndicator>
          <cac:MinimumTemperature>
            <cbc:AttributeID>Battery</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
          </cac:MinimumTemperature>
          <cac:MaximumTemperature>
            <cbc:AttributeID>Battery</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:HazardousGoodsTransit>
            <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
            <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
            <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
            <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
            <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
            <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %.</cbc:TransitDescription>
            <cac:MaximumTemperature>
              <cbc:AttributeID>Battery</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">35</cbc:Measure>
            </cac:MaximumTemperature>
            <cac:MinimumTemperature>
              <cbc:AttributeID>Battery</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">5</cbc:Measure>
            </cac:MinimumTemperature>
          </cac:HazardousGoodsTransit>
          <cac:LoadedHazardousItem>
            <cbc:ID>SE-BAT-48100-DG</cbc:ID>
            <cbc:UNDGCode listID="UN Model Regulations UN number">3480</cbc:UNDGCode>
            <cbc:CategoryName>Miscellaneous dangerous goods</cbc:CategoryName>
            <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
            <cbc:UpperOrangeHazardPlacardID>90</cbc:UpperOrangeHazardPlacardID>
            <cbc:LowerOrangeHazardPlacardID>3480</cbc:LowerOrangeHazardPlacardID>
            <cbc:HazardClassID>9</cbc:HazardClassID>
            <cbc:HazardousTypeCode listID="urn:ubl-examples:world:codelist:HazardousGoodsTypeCode">ARTICLE</cbc:HazardousTypeCode>
            <cbc:PackagingDangerLevelCode listID="UN/EDIFACT EDED 8339">4</cbc:PackagingDangerLevelCode>
            <cbc:GrossWeightMeasure unitCode="KGM">348</cbc:GrossWeightMeasure>
            <cbc:NetWeightMeasure unitCode="KGM">312</cbc:NetWeightMeasure>
            <cbc:NetVolumeMeasure unitCode="MTQ">0.24</cbc:NetVolumeMeasure>
            <cbc:Quantity unitCode="EA">6</cbc:Quantity>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Saltmere Engineering</cbc:Name>
              </cac:PartyName>
            </cac:ContactParty>
            <cac:HazardousGoodsTransit>
              <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
              <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
              <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
              <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
              <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
              <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %.</cbc:TransitDescription>
              <cac:MaximumTemperature>
                <cbc:AttributeID>Battery</cbc:AttributeID>
                <cbc:Measure unitCode="CEL">35</cbc:Measure>
              </cac:MaximumTemperature>
              <cac:MinimumTemperature>
                <cbc:AttributeID>Battery</cbc:AttributeID>
                <cbc:Measure unitCode="CEL">5</cbc:Measure>
              </cac:MinimumTemperature>
            </cac:HazardousGoodsTransit>
            <cac:EmergencyTemperature>
              <cbc:AttributeID>Emergency</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">60</cbc:Measure>
            </cac:EmergencyTemperature>
            <cac:AdditionalTemperature>
              <cbc:AttributeID>Storage</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">20</cbc:Measure>
            </cac:AdditionalTemperature>
            <cac:PositionOnBoardStowage>
              <cbc:LocationID>MD-L2</cbc:LocationID>
              <cbc:Location>Main deck, accessible</cbc:Location>
            </cac:PositionOnBoardStowage>
            <cac:Package>
              <cbc:ID>SE-CR-1..6</cbc:ID>
              <cbc:Quantity unitCode="EA">6</cbc:Quantity>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
            </cac:Package>
          </cac:LoadedHazardousItem>
        </cac:TransportEquipment>
        <cac:HazardousGoodsTransit>
          <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
          <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
          <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
          <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
          <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %.</cbc:TransitDescription>
          <cac:MaximumTemperature>
            <cbc:AttributeID>Battery</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:MinimumTemperature>
            <cbc:AttributeID>Battery</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
          </cac:MinimumTemperature>
        </cac:HazardousGoodsTransit>
        <cac:MinimumTemperature>
          <cbc:AttributeID>Battery</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">5</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID>Battery</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">35</cbc:Measure>
        </cac:MaximumTemperature>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Lithium-ion battery pack 48 V 100 Ah</cbc:Description>
      <cac:Item>
        <cbc:Description>Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.</cbc:Description>
        <cbc:Name>Lithium-ion battery pack 48 V 100 Ah</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-BAT-48100</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772050000117</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">850760</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">46420</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-BAT-48100-DG</cbc:ID>
          <cbc:PlacardNotation>9</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>9A</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>State of charge below 30 %, as the air rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations UN number">3480</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode listID="IMO IMDG EmS">F-A,S-I</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">147</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode listID="UNECE ADR tunnel restriction code">E</cbc:TunnelRestrictionCode>
          <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">9</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN3480</cbc:MarkingID>
          <cbc:HazardClassID>9</cbc:HazardClassID>
        </cac:HazardousItem>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID>Transport</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">20</cbc:Measure>
        <cbc:MeasureCode listID="urn:ubl-examples:world:codelist:TemperatureQualifierCode">TARGET</cbc:MeasureCode>
        <cbc:Description>Keep away from heat.</cbc:Description>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:Measure unitCode="CEL">35</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Ionisation smoke detector set</cbc:Description>
      <cac:Item>
        <cbc:Description>Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.</cbc:Description>
        <cbc:Name>Ionisation smoke detector set</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-SMK-10</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772050000124</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">853110</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">46921</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-SMK-10-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Excepted package: no radioactive label, the UN number on the package.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations UN number">2911</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode listID="IMO IMDG EmS">F-I,S-S</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">161</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2911</cbc:MarkingID>
          <cbc:HazardClassID>7</cbc:HazardClassID>
          <cac:RadioactiveMaterial>
            <cbc:Name>Americium-241 sources in smoke detectors</cbc:Name>
            <cbc:SpecialFormDescription>Sealed source, not special form.</cbc:SpecialFormDescription>
            <cbc:TransportIndexNumeric>0</cbc:TransportIndexNumeric>
            <cbc:FissileCriticalitySafetyIndexNumeric>0</cbc:FissileCriticalitySafetyIndexNumeric>
            <cac:ApplicableRadioactiveIsotope>
              <cbc:Name>Americium-241</cbc:Name>
              <cbc:ActivityLevelMeasure unitCode="2Q">37</cbc:ActivityLevelMeasure>
            </cac:ApplicableRadioactiveIsotope>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID>Transport</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">20</cbc:Measure>
        <cbc:MeasureCode listID="urn:ubl-examples:world:codelist:TemperatureQualifierCode">TARGET</cbc:MeasureCode>
        <cbc:Description>Keep away from heat.</cbc:Description>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:Measure unitCode="CEL">35</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Coating stripper for electronics</cbc:Description>
      <cac:Item>
        <cbc:Description>Remover for the protective coating of circuit boards, in 5-litre cans.</cbc:Description>
        <cbc:Name>Coating stripper for electronics</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-CS-05</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772050000131</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">381400</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">35110</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-CS-05-DG</cbc:ID>
          <cbc:PlacardNotation>8</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>8</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>Packed as the rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations UN number">2920</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">II</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>Medium danger</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode listID="IMO IMDG EmS">F-E,S-C</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">132</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode listID="UNECE ADR tunnel restriction code">D/E</cbc:TunnelRestrictionCode>
          <cbc:MaritimePollutantCode listID="urn:ubl-examples:world:codelist:MarinePollutantCode">N</cbc:MaritimePollutantCode>
          <cbc:TechnicalName>ethanolamine, propanol</cbc:TechnicalName>
          <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">8</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2920</cbc:MarkingID>
          <cbc:HazardClassID>8</cbc:HazardClassID>
          <cac:SecondaryHazard>
            <cbc:ID>3</cbc:ID>
            <cbc:PlacardNotation>3</cbc:PlacardNotation>
            <cbc:PlacardEndorsement>3</cbc:PlacardEndorsement>
            <cbc:Extension>Subsidiary risk 3</cbc:Extension>
          </cac:SecondaryHazard>
          <cac:FlashpointTemperature>
            <cbc:AttributeID>Flashpoint</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">28</cbc:Measure>
          </cac:FlashpointTemperature>
        </cac:HazardousItem>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID>Transport</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">20</cbc:Measure>
        <cbc:MeasureCode listID="urn:ubl-examples:world:codelist:TemperatureQualifierCode">TARGET</cbc:MeasureCode>
        <cbc:Description>Keep away from heat.</cbc:Description>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:Measure unitCode="CEL">35</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
  </cac:Shipment>
</ForwardingInstructions>
```
