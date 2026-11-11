# Transportation Status: Ferrano Intermodal Hub to Ferrano Rail Cargo

*Example 7 of the flow "Containers by rail under transit (Urvania → Bayvarra)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The intermodal terminal reports to the rail carrier that the containers are loaded on the train.

[The XML file](07-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:rail**  
  The business process the document belongs to: the flow "Containers by rail under transit (Urvania → Bayvarra)".
- `ProfileExecutionID` = **RAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FIH-TS-26-0333**  
  The sender's status report number.
- `UUID` = **514b9478-0214-5ce0-9018-7c4cf752cbd3**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-14**  
  Reported when the containers are on the train.
- `IssueTime` = **13:11:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Two containers loaded on the container train.**  
  In words.
- `Note` = **Krerdan skuskek mir drek stalkan sazhir kaztrir.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): How it was made.
- `Note` = **Automatic report from the sender's tracking system.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: How it was made.
- `ShippingOrderID` = **VI-CS-26-0327**  
  The shipper's booking it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do.
- `TransportExecutionStatusCode` = **INPROGRESS** (listID `urn:ubl-examples:world:codelist:TransportExecutionStatusCode`)  
  The carriage is under way. The code is from the Trade Accord's transport execution status list: INPROGRESS = In progress.

### Consignment

Inside `Consignment`:

- `ID` = **VI-CS-26-0327**  
  The consignment the report is about.
- `CarrierParty/WebsiteURI` = **https://www.ferranorail.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/IndustryClassificationCode` = **4912** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Rail Cargo (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4912 = Freight rail transport.
- `CarrierParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `CarrierParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `CarrierParty/PostalAddress/ID` = **4170201115930918** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `CarrierParty/PostalAddress/StreetName` = **Rumir Hekrul Zhuzkek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/StreetName` = **Viale della Stazione** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `CarrierParty/PartyTaxScheme/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyTaxScheme/CompanyID` = **XU007328060** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Rail Cargo (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `CarrierParty/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 14 persons and its turnover of 851000000 XUF in 2025, by the Trade Accord's limits; identity of Ferrano Rail Cargo (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `CarrierParty/Contact/Name` = **Freight desk**  
  The desk that handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/Telephone` = **+999 1 0413 44685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Rail Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **1**  
  The main carriage, by rail.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/OccurrenceDate` = **2026-04-14**  
  If the morning train is full, the boxes go on the evening train.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/OccurrenceTime` = **17:00:00**  
  The local time.
- `MainCarriageShipmentStage/OptionalTakeoverTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/ActualPickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  The boxes were collected from the warehouse.
- `MainCarriageShipmentStage/ActualPickupTransportEvent/OccurrenceTime` = **15:00:00**  
  The local time.
- `MainCarriageShipmentStage/DeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  Planned placement at the siding.
- `MainCarriageShipmentStage/DeliveryTransportEvent/OccurrenceTime` = **11:00:00**  
  The local time.
- `MainCarriageShipmentStage/DeliveryTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/TerminalOperatorParty/WebsiteURI` = **https://www.ferranohub.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/IndustryClassificationCode` = **5221** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Intermodal Hub (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5221 = Service activities incidental to land transportation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Intermodal Hub (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Ferrano Intermodal Hub**  
  The trading name; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/ID` = **4160200139820702** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Bek Han Krazhul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Via del Terminal** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **59**  
  Building number of the postal address. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/PostalZone` = **4180**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/RegistrationName` = **Ferrano Intermodal Hub SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/CompanyID` = **XU007356833** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Intermodal Hub (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Ferrano Intermodal Hub SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Ferrano Intermodal Hub (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SRU = Società a responsabilità urvaniana (private limited company).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)** (languageID `qau`)  
  The name of code SRU in Urvania's national company legal form list. In Urvanian, the sender's language.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)** (languageID `en-XU`)  
  The name of code SRU in Urvania's national company legal form list. In English.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 14 persons and its turnover of 549000000 XUF in 2025, by the Trade Accord's limits; identity of Ferrano Intermodal Hub (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Terminal control**  
  The desk that handles this document; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 1 041 672 5096**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **terminal@ferranohub.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105096** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Intermodal Hub (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/TransportEvent/OccurrenceDate` = **2026-04-14**  
  Both boxes lifted onto the train.
- `MainCarriageShipmentStage/TransportEvent/OccurrenceTime` = **05:40:00**  
  The local time.
- `MainCarriageShipmentStage/TransportEvent/CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-04-14**  
  The day the event took place.
- `Description` = **Two containers loaded on the container train.**  
  What happened, in words.
- `Location/Name` = **Ferrano Intermodal Hub**  
  Where it happened.

### Document Reference

Inside `DocumentReference`:

- `ID` = **VI-CS-26-0327**  
  The transport document of the consignment.

### Signature

Inside `Signature`:

- `ID` = **FIH-SIG-TS-07**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Intermodal Hub**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Intermodal Hub**  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.

### Transport Execution Plan Document Reference

Inside `TransportExecutionPlanDocumentReference`:

- `ID` = **FRC-TEP-26-0328**  
  The plan the carriage follows.

### Status Location

Inside `StatusLocation`:

- `Name` = **Ferrano Intermodal Hub**  
  Where the status was recorded.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-04-14**  
  The status holds from the report.
- `EndDate` = **2026-04-14**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:rail</cbc:ProfileID>
  <cbc:ProfileExecutionID>RAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FIH-TS-26-0333</cbc:ID>
  <cbc:UUID>514b9478-0214-5ce0-9018-7c4cf752cbd3</cbc:UUID>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>13:11:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Two containers loaded on the container train.</cbc:Description>
  <cbc:Note languageID="qau">Krerdan skuskek mir drek stalkan sazhir kaztrir.</cbc:Note>
  <cbc:Note languageID="en-XU">Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>VI-CS-26-0327</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode listID="urn:ubl-examples:world:codelist:TransportExecutionStatusCode">INPROGRESS</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>VI-CS-26-0327</cbc:ID>
    <cac:CarrierParty>
      <cbc:WebsiteURI>https://www.ferranorail.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4912</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4170201115930918</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Rumir Hekrul Zhuzkek</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Viale della Stazione</cbc:StreetName>
        <cbc:BuildingNumber>38</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
        <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
        <cbc:PostalZone>4150</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Ferrano Rail Cargo SRU</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007328060</cbc:CompanyID>
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
        <cbc:RegistrationName>Ferrano Rail Cargo SRU</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
        <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Serravona</cbc:CityName>
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
        <cbc:Name>Freight desk</cbc:Name>
        <cbc:JobTitle>Operations planner</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 1 0413 44685</cbc:Telephone>
        <cbc:ElectronicMail>freight@ferranorail.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cac:OptionalTakeoverTransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>17:00:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
      </cac:OptionalTakeoverTransportEvent>
      <cac:ActualPickupTransportEvent>
        <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>15:00:00</cbc:OccurrenceTime>
      </cac:ActualPickupTransportEvent>
      <cac:DeliveryTransportEvent>
        <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>11:00:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
      </cac:DeliveryTransportEvent>
      <cac:TerminalOperatorParty>
        <cbc:WebsiteURI>https://www.ferranohub.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5221</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">qau</cbc:ID>
          <cbc:Name>Urvanian</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200139820702</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qau">Bek Han Krazhul</cbc:StreetName>
          <cbc:StreetName languageID="en-XU">Via del Terminal</cbc:StreetName>
          <cbc:BuildingNumber>59</cbc:BuildingNumber>
          <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
          <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
          <cbc:PostalZone>4180</cbc:PostalZone>
          <cbc:Region>Province of Ferrano</cbc:Region>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Ferrano Intermodal Hub SRU</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007356833</cbc:CompanyID>
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
          <cbc:RegistrationName>Ferrano Intermodal Hub SRU</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SRU</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm languageID="qau">Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)</cbc:CompanyLegalForm>
          <cbc:CompanyLegalForm languageID="en-XU">Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
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
          <cbc:Name>Terminal control</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 041 672 5096</cbc:Telephone>
          <cbc:ElectronicMail>terminal@ferranohub.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105096</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
      <cac:TransportEvent>
        <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>05:40:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
      </cac:TransportEvent>
    </cac:MainCarriageShipmentStage>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
    <cbc:Description>Two containers loaded on the container train.</cbc:Description>
    <cac:Location>
      <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:DocumentReference>
    <cbc:ID>VI-CS-26-0327</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>FIH-SIG-TS-07</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:TransportExecutionPlanDocumentReference>
    <cbc:ID>FRC-TEP-26-0328</cbc:ID>
  </cac:TransportExecutionPlanDocumentReference>
  <cac:StatusLocation>
    <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-04-14</cbc:StartDate>
    <cbc:EndDate>2026-04-14</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
