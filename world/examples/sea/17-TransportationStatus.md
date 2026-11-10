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
- `ID` = **PS-TS-26-0142**  
  The sender's status report number.
- `IssueDate` = **2026-05-18**  
  Reported when the container is discharged.

### Consignment

Inside `Consignment`:

- `ID` = **LD-CS-26-0133**  
  The consignment the report is about.
- `ConsigneeParty/WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Language/ID` = **en**  
  English, the language the party does business in.
- `ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `ConsigneeParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `ConsigneeParty/PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `ConsigneeParty/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `ConsigneeParty/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `CarrierParty/Language/Name` = **English**  
  The language's name.
- `CarrierParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `CarrierParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
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
  The state, part of an address in federal Bayvarra. identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CarrierParty/PartyTaxScheme/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered for state sales tax; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyTaxScheme/CompanyID` = **CO-1235754**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `CarrierParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered, with its legal form; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **20411918**  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1974-03-01**  
  The day the company was entered in the register; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **Corp**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The legal form, in words.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/CorporateStockAmount` = **40000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `CarrierParty/Contact/Name` = **Bookings**  
  The desk that handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/Telephone` = **+999 2 3852 1918**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **1**  
  The sea leg.
- `MainCarriageShipmentStage/TerminalOperatorParty/WebsiteURI` = **https://www.port-selanu.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/IndustryClassificationCode` = **5222** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Port of Selanu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Port of Selanu**  
  The trading name; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **en**  
  English, the language the party does business in.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **English**  
  The language's name.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Wharf Road**  
  Street of the postal address. identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address. identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/Description` = **Port of Selanu**  
  Where the party actually operates, apart from its postal address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/InformationURI` = **https://www.port-selanu.example**  
  Where to find more about the place.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **WGS84**  
  The World Geodetic System 1984, as used by satellite navigation.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **40** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **1.20** (unitCode `D61`)  
  The minutes of the latitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South**  
  South of the equator.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **8.40** (unitCode `D61`)  
  The minutes of the longitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West**  
  West of the Greenwich meridian.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Port of Selanu Ltd**  
  The name under which the party is registered, with its legal form; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **IC41037**  
  Number in the Island companies register; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Port control**  
  The desk that handles this document; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 3 3000 1037**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **port@port-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Port of Selanu (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41037** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Port of Selanu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-05-18**  
  The day the event took place.
- `Description` = **Container TWLU4120872 discharged and available for customs clearance.**  
  What happened, in words.
- `Location/Name` = **Port of Selanu**  
  Where it happened.

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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Bayforth Forwarding (world/parties.json).
- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
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
  The state, part of an address in federal Bayvarra. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered for state sales tax; identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1234932**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411644**  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Contact/Name` = **Export desk**  
  The desk that handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 3852 1644**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>PS-TS-26-0142</cbc:ID>
  <cbc:IssueDate>2026-05-18</cbc:IssueDate>
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
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName>Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC41859</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 3000 1859</cbc:Telephone>
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
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Harbour Road</cbc:StreetName>
        <cbc:BuildingNumber>18</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38527</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
        <cbc:CompanyID>CO-1235754</cbc:CompanyID>
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
        <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
        <cbc:CompanyID>20411918</cbc:CompanyID>
        <cbc:RegistrationDate>1974-03-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Corp</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
        <cbc:CorporateStockAmount currencyID="XBL">40000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
        <cbc:Name>Bookings</cbc:Name>
        <cbc:JobTitle>Operations planner</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 2 3852 1918</cbc:Telephone>
        <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
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
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
          <cbc:StreetName>Wharf Road</cbc:StreetName>
          <cbc:BuildingNumber>32</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PhysicalLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Description>Port of Selanu</cbc:Description>
          <cbc:InformationURI>https://www.port-selanu.example</cbc:InformationURI>
          <cac:LocationCoordinate>
            <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
            <cbc:LatitudeDegreesMeasure unitCode="DD">40</cbc:LatitudeDegreesMeasure>
            <cbc:LatitudeMinutesMeasure unitCode="D61">1.20</cbc:LatitudeMinutesMeasure>
            <cbc:LatitudeDirectionCode>South</cbc:LatitudeDirectionCode>
            <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
            <cbc:LongitudeMinutesMeasure unitCode="D61">8.40</cbc:LongitudeMinutesMeasure>
            <cbc:LongitudeDirectionCode>West</cbc:LongitudeDirectionCode>
          </cac:LocationCoordinate>
        </cac:PhysicalLocation>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Port of Selanu Ltd</cbc:RegistrationName>
          <cbc:CompanyID>IC41037</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
          <cbc:Name>Port control</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 3 3000 1037</cbc:Telephone>
          <cbc:ElectronicMail>port@port-selanu.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41037</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
    </cac:MainCarriageShipmentStage>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
    <cbc:Description>Container TWLU4120872 discharged and available for customs clearance.</cbc:Description>
    <cac:Location>
      <cbc:Name>Port of Selanu</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
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
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID>CO-1234932</cbc:CompanyID>
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
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20411644</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 3852 1644</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
</TransportationStatus>
```
