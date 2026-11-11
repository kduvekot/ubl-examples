# Transportation Status: Selanu Airport Cargo to Bayforth Forwarding

*Example 9 of the flow "An urgent part of the order by air (Bayvarra → island Lisavu)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The island's air cargo terminal reports the cargo arrived and ready for customs clearance.

[The XML file](09-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:air**  
  The business process the document belongs to: the flow "An urgent part of the order by air (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **AIR-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **SAC-TS-26-0330**  
  The sender's status report number.
- `UUID` = **699cd30a-3784-5a9d-8770-15e1898e75ec**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-14**  
  Reported when the cargo has landed.
- `IssueTime` = **17:58:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Cargo arrived and ready for customs clearance.**  
  In words.
- `Note` = **Keavate tafese lesama kanela temati kalale.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): How it was made.
- `Note` = **Automatic report from the sender's tracking system.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: How it was made.
- `ShippingOrderID` = **LD-CS-26-0324**  
  The shipper's booking it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do.
- `TransportExecutionStatusCode` = **INPROGRESS** (listID `urn:ubl-examples:world:codelist:TransportExecutionStatusCode`)  
  The carriage is under way. The code is from the Trade Accord's transport execution status list: INPROGRESS = In progress.

### Consignment

Inside `Consignment`:

- `ID` = **LD-CS-26-0324**  
  The consignment the report is about.
- `ConsigneeParty/WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `ConsigneeParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `ConsigneeParty/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 34 persons and its turnover of 1940000.000 XLC in 2025, by the Trade Accord's limits; identity of Velumi Trading (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/Telephone` = **+999 3 729 1859**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `CarrierParty/WebsiteURI` = **https://www.kelaro.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/IndustryClassificationCode` = **5120** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Kelaro Air Cargo (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5120 = Freight air transport.
- `CarrierParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `CarrierParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `CarrierParty/PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `CarrierParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Kelaro Air Cargo Ltd**  
  The name under which the party is registered, with its legal form; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **IC41311**  
  Number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 13 persons and its turnover of 2590000.000 XLC in 2025, by the Trade Accord's limits; identity of Kelaro Air Cargo (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `CarrierParty/Contact/Name` = **Cargo sales**  
  The desk that handles this document; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/Telephone` = **+999 3 721 1311**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/ElectronicMail` = **cargo@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41311** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Kelaro Air Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `MainCarriageShipmentStage/TerminalOperatorParty/WebsiteURI` = **https://www.selanu-cargo.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/IndustryClassificationCode` = **5223** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Airport Cargo (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5223 = Service activities incidental to air transportation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41174** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Airport Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Selanu Airport Cargo**  
  The trading name; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **39**  
  Building number of the postal address. identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Selanu Airport Cargo Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **IC41174**  
  Number in the Island companies register; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 15 persons and its turnover of 1220000.000 XLC in 2025, by the Trade Accord's limits; identity of Selanu Airport Cargo (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/HeadOfficeParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/HeadOfficeParty/PartyName/Name` = **Port of Selanu**  
  A party referred to from another party's details: its identifier and name are enough.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Import desk**  
  The desk that handles this document; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 3 724 1174**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **import@selanu-cargo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Airport Cargo (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41174** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Airport Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-05-14**  
  The day the event took place.
- `Description` = **Cargo arrived and ready for customs clearance.**  
  What happened, in words.
- `Location/Name` = **Selanu airport, cargo terminal**  
  Where it happened.

### Document Reference

Inside `DocumentReference`:

- `ID` = **KAC-WB-26-0325**  
  The transport document of the consignment.

### Signature

Inside `Signature`:

- `ID` = **SAC-SIG-TS-09**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC41174** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Selanu Airport Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC41174** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu Airport Cargo**  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

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

### Status Location

Inside `StatusLocation`:

- `Name` = **Selanu Airport Cargo**  
  Where the status was recorded.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-05-14**  
  The status holds from the report.
- `EndDate` = **2026-05-14**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:air</cbc:ProfileID>
  <cbc:ProfileExecutionID>AIR-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SAC-TS-26-0330</cbc:ID>
  <cbc:UUID>699cd30a-3784-5a9d-8770-15e1898e75ec</cbc:UUID>
  <cbc:IssueDate>2026-05-14</cbc:IssueDate>
  <cbc:IssueTime>17:58:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Cargo arrived and ready for customs clearance.</cbc:Description>
  <cbc:Note languageID="qal">Keavate tafese lesama kanela temati kalale.</cbc:Note>
  <cbc:Note languageID="en-XL">Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>LD-CS-26-0324</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode listID="urn:ubl-examples:world:codelist:TransportExecutionStatusCode">INPROGRESS</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>LD-CS-26-0324</cbc:ID>
    <cac:ConsigneeParty>
      <cbc:WebsiteURI>https://www.velumi.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC41859</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 729 1859</cbc:Telephone>
        <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:ConsigneeParty>
    <cac:CarrierParty>
      <cbc:WebsiteURI>https://www.kelaro.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">5120</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelaro Air Cargo</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Airfield Road</cbc:StreetName>
        <cbc:BuildingNumber>46</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Kelaro Air Cargo Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC41311</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
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
        <cbc:Name>Cargo sales</cbc:Name>
        <cbc:JobTitle>Operations planner</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 3 721 1311</cbc:Telephone>
        <cbc:ElectronicMail>cargo@kelaro.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41311</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cac:TerminalOperatorParty>
        <cbc:WebsiteURI>https://www.selanu-cargo.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5223</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41174</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Airport Cargo</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Airfield Road</cbc:StreetName>
          <cbc:BuildingNumber>39</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Selanu Airport Cargo Ltd</cbc:RegistrationName>
          <cbc:CompanyID>IC41174</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm languageID="qal">Tivufo kilika humaki</cbc:CompanyLegalForm>
          <cbc:CompanyLegalForm languageID="en-XL">Island limited company</cbc:CompanyLegalForm>
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
          <cac:HeadOfficeParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Port of Selanu</cbc:Name>
            </cac:PartyName>
          </cac:HeadOfficeParty>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Import desk</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 3 724 1174</cbc:Telephone>
          <cbc:ElectronicMail>import@selanu-cargo.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41174</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
    </cac:MainCarriageShipmentStage>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-05-14</cbc:OccurrenceDate>
    <cbc:Description>Cargo arrived and ready for customs clearance.</cbc:Description>
    <cac:Location>
      <cbc:Name>Selanu airport, cargo terminal</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:DocumentReference>
    <cbc:ID>KAC-WB-26-0325</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>SAC-SIG-TS-09</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41174</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Airport Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41174</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Airport Cargo</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
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
  </cac:ReceiverParty>
  <cac:StatusLocation>
    <cbc:Name>Selanu Airport Cargo</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-05-14</cbc:StartDate>
    <cbc:EndDate>2026-05-14</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
