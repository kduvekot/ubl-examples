# Transportation Status: Port of Selanu to Bayforth Forwarding

*Example 17 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The port of discharge reports the container discharged and available.

[The XML file](17-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:sea**  
  The business process the document belongs to: the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **PS-TS-26-0142**  
  The sender's status report number.
- `UUID` = **1713d8c6-6d60-56cc-af96-b2eb848695b4**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-18**  
  Reported when the container is discharged.
- `IssueTime` = **16:36:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Container TWLU4120872 discharged and available for customs clearance.**  
  In words.
- `Note` = **Keavate tafese lesama kanela temati kalale.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): How it was made.
- `Note` = **Automatic report from the sender's tracking system.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: How it was made.
- `ShippingOrderID` = **LD-CS-26-0133**  
  The shipper's booking it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do.
- `TransportExecutionStatusCode` = **INPROGRESS** (listID `urn:ubl-examples:world:codelist:TransportExecutionStatusCode`)  
  The carriage is under way. The code is from the Trade Accord's transport execution status list: INPROGRESS = In progress.

### Consignment

Inside `Consignment`:

- `ID` = **LD-CS-26-0133**  
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
- `ConsigneeParty/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
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
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
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
- `CarrierParty/WebsiteURI` = **https://www.tidewell.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/IndustryClassificationCode` = **5012** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Tidewell Ocean Lines (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5012 = Sea and coastal freight water transport.
- `CarrierParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `CarrierParty/Language/Name` = **English**  
  The language's name.
- `CarrierParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `CarrierParty/PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `CarrierParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CarrierParty/PartyTaxScheme/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered for state sales tax; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyTaxScheme/CompanyID` = **CO-1235754** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Tidewell Ocean Lines (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `CarrierParty/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `CarrierParty/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered, with its legal form; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1974-03-01**  
  The day the company was entered in the register; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **CORP** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: CORP = Corporation (public).
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The name of code CORP in Bayvarra's national company legal form list.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 776 persons and its turnover of 865000000.00 XBL in 2025, by the Trade Accord's limits; identity of Tidewell Ocean Lines (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `CarrierParty/PartyLegalEntity/CorporateStockAmount` = **40000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CarrierParty/Contact/Name` = **Bookings**  
  The desk that handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/Telephone` = **+999 2 38 2418 1918**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **2**  
  The sea leg, stage 2 as on the bill of lading.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-05-18**  
  The container came off the ship.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **11:20:00**  
  The local time.
- `MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/TerminalOperatorParty/WebsiteURI` = **https://www.port-selanu.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/IndustryClassificationCode` = **5222** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Port of Selanu (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5222 = Service activities incidental to water transportation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Port of Selanu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Port of Selanu**  
  The trading name; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address. identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/Description` = **Port of Selanu**  
  Where the party actually operates, apart from its postal address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/InformationURI` = **https://www.port-selanu.example**  
  Where to find more about the place.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **40** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **1.20** (unitCode `D61`)  
  The minutes of the latitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **8.40** (unitCode `D61`)  
  The minutes of the longitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Port of Selanu Ltd**  
  The name under which the party is registered, with its legal form; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Port of Selanu (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Tivufo kilika humaki** (languageID `qal`)  
  The name of code LTD in Lisavu's national company legal form list. In Lisavan, the sender's language.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company** (languageID `en-XL`)  
  The name of code LTD in Lisavu's national company legal form list. In English.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 28 persons and its turnover of 3490000.000 XLC in 2025, by the Trade Accord's limits; identity of Port of Selanu (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Port control**  
  The desk that handles this document; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 3 727 1037**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **port@port-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41037** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Port of Selanu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/DetentionTransportEvent/OccurrenceDate` = **2026-05-18**  
  Held by customs for a check of the pallets.
- `MainCarriageShipmentStage/DetentionTransportEvent/OccurrenceTime` = **12:00:00**  
  The local time.
- `MainCarriageShipmentStage/DetentionTransportEvent/Description` = **Wooden pallets must carry the heat-treatment mark.**  
  What happened, in words.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceDate` = **2026-05-18**  
  The ship berthed at Selanu.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceTime` = **06:30:00**  
  The local time.
- `MainCarriageShipmentStage/ReportingPerson/FirstName` = **Ama**  
  The terminal's duty officer who reports.
- `MainCarriageShipmentStage/ReportingPerson/FamilyName` = **Kelune**  
  The family name.
- `MainCarriageShipmentStage/ReportingPerson/JobTitle` = **Duty officer**  
  The person's position.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/OccurrenceDate` = **2026-05-18**  
  Released from the quarantine check: all pallets heat-treated.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/OccurrenceTime` = **15:00:00**  
  The local time.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).
- `TransportHandlingUnit/TransportEquipment/TransportEvent/OccurrenceDate` = **2026-05-18**  
  Stacked in the import yard.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/OccurrenceTime` = **11:40:00**  
  The local time.
- `TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/ChargeIndicator` = **true**  
  A service charge.
- `TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/AllowanceChargeReasonCode` = **HD** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: HD = Handling.
- `TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/AllowanceChargeReason` = **Terminal handling at Selanu**  
  For unloading the box.
- `TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/Amount` = **185.00** (currencyID `XBL`)  
  As in the carrier's tariff.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-05-18**  
  The day the event took place.
- `Description` = **Container TWLU4120872 discharged and available for customs clearance.**  
  What happened, in words.
- `Location/Name` = **Port of Selanu**  
  Where it happened.

### Document Reference

Inside `DocumentReference`:

- `ID` = **TOL-BL-26-0139**  
  The transport document of the consignment.

### Signature

Inside `Signature`:

- `ID` = **PS-SIG-TS-17**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Port of Selanu**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Port of Selanu**  
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
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
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
- `PartyTaxScheme/CompanyID` = **CO-1234932** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
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

- `Name` = **Port of Selanu**  
  Where the status was recorded.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-05-18**  
  The status holds from the report.
- `EndDate` = **2026-05-18**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>PS-TS-26-0142</cbc:ID>
  <cbc:UUID>1713d8c6-6d60-56cc-af96-b2eb848695b4</cbc:UUID>
  <cbc:IssueDate>2026-05-18</cbc:IssueDate>
  <cbc:IssueTime>16:36:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Container TWLU4120872 discharged and available for customs clearance.</cbc:Description>
  <cbc:Note languageID="qal">Keavate tafese lesama kanela temati kalale.</cbc:Note>
  <cbc:Note languageID="en-XL">Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>LD-CS-26-0133</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode listID="urn:ubl-examples:world:codelist:TransportExecutionStatusCode">INPROGRESS</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>LD-CS-26-0133</cbc:ID>
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
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
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
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:CompanyID>
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
      <cbc:WebsiteURI>https://www.tidewell.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">5012</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Harbour Road</cbc:StreetName>
        <cbc:BuildingNumber>18</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38527</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1235754</cbc:CompanyID>
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
        <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:CompanyID>
        <cbc:RegistrationDate>1974-03-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">CORP</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XBL">40000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
        <cbc:Name>Bookings</cbc:Name>
        <cbc:JobTitle>Operations planner</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 2 38 2418 1918</cbc:Telephone>
        <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>2</cbc:ID>
      <cac:DischargeTransportEvent>
        <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>11:20:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
      </cac:DischargeTransportEvent>
      <cac:TerminalOperatorParty>
        <cbc:WebsiteURI>https://www.port-selanu.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5222</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Port of Selanu</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
          <cbc:BuildingNumber>32</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PhysicalLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Description>Port of Selanu</cbc:Description>
          <cbc:InformationURI>https://www.port-selanu.example</cbc:InformationURI>
          <cac:LocationCoordinate>
            <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
            <cbc:LatitudeDegreesMeasure unitCode="DD">40</cbc:LatitudeDegreesMeasure>
            <cbc:LatitudeMinutesMeasure unitCode="D61">1.20</cbc:LatitudeMinutesMeasure>
            <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
            <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
            <cbc:LongitudeMinutesMeasure unitCode="D61">8.40</cbc:LongitudeMinutesMeasure>
            <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
          </cac:LocationCoordinate>
        </cac:PhysicalLocation>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Port of Selanu Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:CompanyID>
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
          <cbc:Name>Port control</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 3 727 1037</cbc:Telephone>
          <cbc:ElectronicMail>port@port-selanu.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41037</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
      <cac:DetentionTransportEvent>
        <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>12:00:00</cbc:OccurrenceTime>
        <cbc:Description>Wooden pallets must carry the heat-treatment mark.</cbc:Description>
      </cac:DetentionTransportEvent>
      <cac:ActualArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>06:30:00</cbc:OccurrenceTime>
      </cac:ActualArrivalTransportEvent>
      <cac:ReportingPerson>
        <cbc:FirstName>Ama</cbc:FirstName>
        <cbc:FamilyName>Kelune</cbc:FamilyName>
        <cbc:JobTitle>Duty officer</cbc:JobTitle>
      </cac:ReportingPerson>
    </cac:MainCarriageShipmentStage>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
        <cac:QuarantineTransportEvent>
          <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>15:00:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
        </cac:QuarantineTransportEvent>
        <cac:TransportEvent>
          <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>11:40:00</cbc:OccurrenceTime>
        </cac:TransportEvent>
        <cac:ServiceAllowanceCharge>
          <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
          <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">HD</cbc:AllowanceChargeReasonCode>
          <cbc:AllowanceChargeReason>Terminal handling at Selanu</cbc:AllowanceChargeReason>
          <cbc:Amount currencyID="XBL">185.00</cbc:Amount>
        </cac:ServiceAllowanceCharge>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
    <cbc:Description>Container TWLU4120872 discharged and available for customs clearance.</cbc:Description>
    <cac:Location>
      <cbc:Name>Port of Selanu</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:DocumentReference>
    <cbc:ID>TOL-BL-26-0139</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>PS-SIG-TS-17</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Port of Selanu</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Selanu</cbc:Name>
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
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
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
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1234932</cbc:CompanyID>
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
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:CompanyID>
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
    <cbc:Name>Port of Selanu</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-05-18</cbc:StartDate>
    <cbc:EndDate>2026-05-18</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
