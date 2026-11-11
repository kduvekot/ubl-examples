# Transportation Status: Lumeport Airport Cargo Terminal to Kelaro Air Cargo

*Example 5 of the flow "An urgent part of the order by air (Bayvarra → island Lisavu)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The air cargo terminal reports the cargo accepted and built up for the flight.

[The XML file](05-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **LACT-TS-26-0326**  
  The sender's status report number.
- `UUID` = **6938a110-04c3-536b-96b3-9bd3bd8bb1c1**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-13**  
  Reported when the cargo is built up for the flight.
- `IssueTime` = **10:05:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Cargo accepted and built up for the flight.**  
  In words.
- `Note` = **Automatic report from the sender's tracking system.**  
  How it was made.
- `ShippingOrderID` = **LD-CS-26-0324**  
  The shipper's booking it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do.
- `TransportExecutionStatusCode` = **InProgress**  
  The carriage is under way.

### Consignment

Inside `Consignment`:

- `ID` = **LD-CS-26-0324**  
  The consignment the report is about.
- `CarrierParty/WebsiteURI` = **https://www.kelaro.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/IndustryClassificationCode` = **5120** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `CarrierParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `CarrierParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `CarrierParty/PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/StreetName` = **Airfield Road** (languageID `en`)  
  The street's name in English, the country's other official language; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CarrierParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Kelaro Air Cargo Ltd**  
  The name under which the party is registered, with its legal form; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **IC41311**  
  Number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
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
- `MainCarriageShipmentStage/TerminalOperatorParty/WebsiteURI` = **https://www.lumeport-cargo.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/IndustryClassificationCode` = **5223** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **20412055** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Airport Cargo Terminal (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Lumeport Airport Cargo Terminal**  
  The trading name; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **en**  
  English, the language the party does business in.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **English**  
  The language's name.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **25**  
  Building number of the postal address. identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state or territory, part of an address in federal Bayvarra. identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CountrySubentityCode` = **CO**  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/Description` = **Lumeport airport**  
  Where the party actually operates, apart from its postal address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/InformationURI` = **https://www.lumeport-cargo.example**  
  Where to find more about the place.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **WGS84**  
  The World Geodetic System 1984, as used by satellite navigation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **59.40** (unitCode `D61`)  
  The minutes of the latitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South**  
  South of the equator.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **16.20** (unitCode `D61`)  
  The minutes of the longitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West**  
  West of the Greenwich meridian.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/AltitudeMeasure` = **14** (unitCode `MTR`)  
  The height of the place above sea level.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/RegistrationName` = **Lumeport Airport Cargo Terminal Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/CompanyID` = **CO-1236165**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Lumeport Airport Cargo Terminal Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **20412055**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Cargo acceptance**  
  The desk that handles this document; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 2 38 2555 2055**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **cargo@lumeport-cargo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XB:20412055** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Airport Cargo Terminal (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-05-13**  
  The day the event took place.
- `Description` = **Cargo accepted and built up for the flight.**  
  What happened, in words.
- `Location/Name` = **Lumeport airport, cargo terminal**  
  Where it happened.

### Document Reference

Inside `DocumentReference`:

- `ID` = **KAC-WB-26-0325**  
  The transport document of the consignment.

### Signature

Inside `Signature`:

- `ID` = **LACT-SIG-TS-05**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412055** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Airport Cargo Terminal**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20412055** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Lumeport Airport Cargo Terminal**  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.

### Status Location

Inside `StatusLocation`:

- `Name` = **Lumeport Airport Cargo Terminal**  
  Where the status was recorded.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-05-13**  
  The status holds from the report.
- `EndDate` = **2026-05-13**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:air</cbc:ProfileID>
  <cbc:ProfileExecutionID>AIR-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LACT-TS-26-0326</cbc:ID>
  <cbc:UUID>6938a110-04c3-536b-96b3-9bd3bd8bb1c1</cbc:UUID>
  <cbc:IssueDate>2026-05-13</cbc:IssueDate>
  <cbc:IssueTime>10:05:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Cargo accepted and built up for the flight.</cbc:Description>
  <cbc:Note>Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>LD-CS-26-0324</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode>InProgress</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>LD-CS-26-0324</cbc:ID>
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
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
        <cbc:StreetName languageID="en">Airfield Road</cbc:StreetName>
        <cbc:BuildingNumber>46</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Kelaro Air Cargo Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC41311</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XL</cbc:IdentificationCode>
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
        <cbc:WebsiteURI>https://www.lumeport-cargo.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5223</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412055</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
          <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
          <cbc:StreetName>Airport Road</cbc:StreetName>
          <cbc:BuildingNumber>25</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38528</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PhysicalLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
          <cbc:Description>Lumeport airport</cbc:Description>
          <cbc:InformationURI>https://www.lumeport-cargo.example</cbc:InformationURI>
          <cac:LocationCoordinate>
            <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
            <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
            <cbc:LatitudeMinutesMeasure unitCode="D61">59.40</cbc:LatitudeMinutesMeasure>
            <cbc:LatitudeDirectionCode>South</cbc:LatitudeDirectionCode>
            <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
            <cbc:LongitudeMinutesMeasure unitCode="D61">16.20</cbc:LongitudeMinutesMeasure>
            <cbc:LongitudeDirectionCode>West</cbc:LongitudeDirectionCode>
            <cbc:AltitudeMeasure unitCode="MTR">14</cbc:AltitudeMeasure>
          </cac:LocationCoordinate>
        </cac:PhysicalLocation>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Lumeport Airport Cargo Terminal Ltd</cbc:RegistrationName>
          <cbc:CompanyID>CO-1236165</cbc:CompanyID>
          <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
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
          <cbc:RegistrationName>Lumeport Airport Cargo Terminal Ltd</cbc:RegistrationName>
          <cbc:CompanyID>20412055</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
          <cbc:Name>Cargo acceptance</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 2 38 2555 2055</cbc:Telephone>
          <cbc:ElectronicMail>cargo@lumeport-cargo.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412055</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
    </cac:MainCarriageShipmentStage>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
    <cbc:Description>Cargo accepted and built up for the flight.</cbc:Description>
    <cac:Location>
      <cbc:Name>Lumeport airport, cargo terminal</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:DocumentReference>
    <cbc:ID>KAC-WB-26-0325</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>LACT-SIG-TS-05</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412055</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412055</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:StatusLocation>
    <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-05-13</cbc:StartDate>
    <cbc:EndDate>2026-05-13</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
