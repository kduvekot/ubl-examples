# Waybill: Kelaro Air Cargo to Bayforth Forwarding

*Example 3 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The air waybill for cargo aircraft only, with the dangerous goods on it.

[The XML file](03-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **KAC-WB-26-0717**  
  The consignment note number.
- `CarrierAssignedID` = **KAC-AWB-26-0713**  
  The carrier's own number for the carriage.
- `UUID` = **bf007d9d-013c-5ef5-8c7c-b450b24811d3**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **Issued**  
  The note is issued and in force.
- `IssueDate` = **2026-06-04**  
  The air waybill, cargo aircraft only.
- `IssueTime` = **17:15:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Air waybill under the Montreal Convention**  
  The kind of transport document.
- `Description` = **A cargo-aircraft-only flight to the island.**  
  The carriage in words.
- `Note` = **Tasela kukohane: titoluva, hivokefi, topatu.** (languageID `qal`)  
  The note in Lisavan, the sender's language (world/countries.json): As the convention prescribes.
- `Note` = **Three originals: consignor, consignee, carrier.** (languageID `en`)  
  The same note in English, the working language between the countries: As the convention prescribes.
- `ShippingOrderID` = **SE-CS-26-0716**  
  The shipper's booking the carriage fulfils.
- `WaybillTypeCode` = **AWB**  
  The convention the document follows.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `AdValoremIndicator` = **false**  
  No value declared to raise the carrier's liability.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Lumeport Airport Cargo Terminal**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.kelaro.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Kelaro Air Cargo (world/parties.json).
- `IndustryClassificationCode` = **5120** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Kelaro Air Cargo (world/parties.json).
- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; identity of Kelaro Air Cargo (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/StreetName` = **Airfield Road** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Kelaro Air Cargo Ltd**  
  The name under which the party is registered, with its legal form; identity of Kelaro Air Cargo (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41311**  
  Number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Kelaro Air Cargo (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Kelaro Air Cargo (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Contact/Name` = **Cargo sales**  
  The desk that handles this document; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Telephone` = **+999 3 3000 1311**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/ElectronicMail` = **cargo@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Kelaro Air Cargo (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41311** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Kelaro Air Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
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
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
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

### Consignor Party

Inside `ConsignorParty`:

- `IndustryClassificationCode` = **4290** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Saltmere Engineering (world/parties.json).
- `PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
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
- `PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered for state sales tax; identity of Saltmere Engineering (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1232055**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Saltmere Engineering (world/parties.json).
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
- `PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered, with its legal form; identity of Saltmere Engineering (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410685**  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json).
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
- `Contact/Name` = **Bids office**  
  The desk that handles this document; identity of Saltmere Engineering (world/parties.json).
- `Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 0685**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Saltmere Engineering (world/parties.json).
- `Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Bayforth Forwarding**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SE-SH-26-0715**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **376** (unitCode `KGM`)  
  The gross weight.
- `Consignment/ID` = **SE-CS-26-0716**  
  The consignment of the transport booking.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.selanutelecom.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **6110** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Consignment/ConsigneeParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **IC42407**  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Consignment/ConsigneeParty/Contact/Name` = **Business accounts**  
  The desk that handles this document; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 3000 2407**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Selanu Telecom (world/parties.json).
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
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Air transport.
- `Consignment/MainCarriageShipmentStage/HazardousRiskIndicator` = **true**  
  Dangerous goods on the flight.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **KAC209**  
  The cargo flight of the day.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XL**  
  The country the means of transport is registered in.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Lisavu**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **AIR**  
  The carrier's code for the kind of means: freighter of kelaro air cargo; the fleet of Kelaro Air Cargo (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/AirTransport/AircraftID` = **XL-KAC**  
  The aircraft's registration, with the world's country code as its nationality mark.
- `Consignment/TransportHandlingUnit/ID` = **RKN-41207-KC**  
  The container as a handling unit.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods inside.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **RKN-41207-KC**  
  The temperature-controlled air container.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **AM** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code AM: refrigerated container.
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
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC-90-3480**  
  The emergency card on board.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/PackingCriteriaCode` = **PI965-IA**  
  IATA packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/HazardousRegulationCode` = **IATA**  
  Air: the IATA Dangerous Goods Regulations.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/InhalationToxicityZoneCode` = **None**  
  Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO**  
  Cargo aircraft only.
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
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **3480** (listID `UNCL8273`)  
  UN 3480.
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
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousTypeCode` = **Article**  
  Batteries are articles, not substances.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PackagingDangerLevelCode` = **None**  
  Lithium batteries have no packing group.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/GrossWeightMeasure` = **348** (unitCode `KGM`)  
  Six packs, packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetWeightMeasure` = **312** (unitCode `KGM`)  
  The packs alone.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetVolumeMeasure` = **0.24** (unitCode `MTQ`)  
  Their volume.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Quantity` = **6** (unitCode `H87`)  
  Six packs.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC-90-3480**  
  The emergency card on board.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/PackingCriteriaCode` = **PI965-IA**  
  IATA packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **IATA**  
  Air: the IATA Dangerous Goods Regulations.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/InhalationToxicityZoneCode` = **None**  
  Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO**  
  Cargo aircraft only.
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
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/Quantity` = **6** (unitCode `H87`)  
  Six.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/PackagingTypeCode` = **CR**  
  UN/ECE Recommendation 21 code CR: crate.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC-90-3480**  
  The emergency card on board.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/PackingCriteriaCode` = **PI965-IA**  
  IATA packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **IATA**  
  Air: the IATA Dangerous Goods Regulations.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/InhalationToxicityZoneCode` = **None**  
  Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO**  
  Cargo aircraft only.
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

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The first original.
- `DocumentTypeCode` = **Original**  
  An original.
- `DistributionTypeCode` = **Paper**  
  Handed over on paper.
- `DistributionType` = **With the goods**  
  It travels with the goods.
- `Party/PartyIdentification/ID` = **IC41174** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Selanu Airport Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The electronic copy.
- `DocumentTypeCode` = **Copy**  
  A copy.
- `DistributionTypeCode` = **Electronic**  
  Sent as this UBL document.
- `Party/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **KAC-SIG-KAC-WB-26-0717**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Kelaro Air Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:mast</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>KAC-WB-26-0717</cbc:ID>
  <cbc:CarrierAssignedID>KAC-AWB-26-0713</cbc:CarrierAssignedID>
  <cbc:UUID>bf007d9d-013c-5ef5-8c7c-b450b24811d3</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode>Issued</cbc:StatusCode>
  <cbc:IssueDate>2026-06-04</cbc:IssueDate>
  <cbc:IssueTime>17:15:00</cbc:IssueTime>
  <cbc:Name>Air waybill under the Montreal Convention</cbc:Name>
  <cbc:Description>A cargo-aircraft-only flight to the island.</cbc:Description>
  <cbc:Note languageID="qal">Tasela kukohane: titoluva, hivokefi, topatu.</cbc:Note>
  <cbc:Note languageID="en">Three originals: consignor, consignee, carrier.</cbc:Note>
  <cbc:ShippingOrderID>SE-CS-26-0716</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode>AWB</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
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
      <cbc:Telephone>+999 3 3000 1311</cbc:Telephone>
      <cbc:ElectronicMail>cargo@kelaro.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41311</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
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
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Foundry Road</cbc:StreetName>
      <cbc:BuildingNumber>13</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71218</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
      <cbc:CompanyID>UL-1232055</cbc:CompanyID>
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
      <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
      <cbc:CompanyID>20410685</cbc:CompanyID>
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
      <cbc:Name>Bids office</cbc:Name>
      <cbc:JobTitle>Procurement officer</cbc:JobTitle>
      <cbc:Department>Procurement</cbc:Department>
      <cbc:Telephone>+999 2 7121 0685</cbc:Telephone>
      <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
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
          <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
          <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
          <cbc:StreetName languageID="en">Mast Hill Road</cbc:StreetName>
          <cbc:BuildingNumber>58</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Selanu Telecom Ltd</cbc:RegistrationName>
          <cbc:CompanyID>IC42407</cbc:CompanyID>
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
          <cbc:Name>Business accounts</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 3 3000 2407</cbc:Telephone>
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
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportMeans>
          <cbc:JourneyID>KAC209</cbc:JourneyID>
          <cbc:RegistrationNationalityID>XL</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Lisavu</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode>AIR</cbc:TransportMeansTypeCode>
          <cac:AirTransport>
            <cbc:AircraftID>XL-KAC</cbc:AircraftID>
          </cac:AirTransport>
        </cac:TransportMeans>
      </cac:MainCarriageShipmentStage>
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
            <cbc:TransportEmergencyCardCode>TEC-90-3480</cbc:TransportEmergencyCardCode>
            <cbc:PackingCriteriaCode>PI965-IA</cbc:PackingCriteriaCode>
            <cbc:HazardousRegulationCode>IATA</cbc:HazardousRegulationCode>
            <cbc:InhalationToxicityZoneCode>None</cbc:InhalationToxicityZoneCode>
            <cbc:TransportAuthorizationCode>CAO</cbc:TransportAuthorizationCode>
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
            <cbc:UNDGCode listID="UNCL8273">3480</cbc:UNDGCode>
            <cbc:CategoryName>Miscellaneous dangerous goods</cbc:CategoryName>
            <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
            <cbc:UpperOrangeHazardPlacardID>90</cbc:UpperOrangeHazardPlacardID>
            <cbc:LowerOrangeHazardPlacardID>3480</cbc:LowerOrangeHazardPlacardID>
            <cbc:HazardClassID>9</cbc:HazardClassID>
            <cbc:HazardousTypeCode>Article</cbc:HazardousTypeCode>
            <cbc:PackagingDangerLevelCode>None</cbc:PackagingDangerLevelCode>
            <cbc:GrossWeightMeasure unitCode="KGM">348</cbc:GrossWeightMeasure>
            <cbc:NetWeightMeasure unitCode="KGM">312</cbc:NetWeightMeasure>
            <cbc:NetVolumeMeasure unitCode="MTQ">0.24</cbc:NetVolumeMeasure>
            <cbc:Quantity unitCode="H87">6</cbc:Quantity>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Saltmere Engineering</cbc:Name>
              </cac:PartyName>
            </cac:ContactParty>
            <cac:HazardousGoodsTransit>
              <cbc:TransportEmergencyCardCode>TEC-90-3480</cbc:TransportEmergencyCardCode>
              <cbc:PackingCriteriaCode>PI965-IA</cbc:PackingCriteriaCode>
              <cbc:HazardousRegulationCode>IATA</cbc:HazardousRegulationCode>
              <cbc:InhalationToxicityZoneCode>None</cbc:InhalationToxicityZoneCode>
              <cbc:TransportAuthorizationCode>CAO</cbc:TransportAuthorizationCode>
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
              <cbc:Quantity unitCode="H87">6</cbc:Quantity>
              <cbc:PackagingTypeCode>CR</cbc:PackagingTypeCode>
            </cac:Package>
          </cac:LoadedHazardousItem>
        </cac:TransportEquipment>
        <cac:HazardousGoodsTransit>
          <cbc:TransportEmergencyCardCode>TEC-90-3480</cbc:TransportEmergencyCardCode>
          <cbc:PackingCriteriaCode>PI965-IA</cbc:PackingCriteriaCode>
          <cbc:HazardousRegulationCode>IATA</cbc:HazardousRegulationCode>
          <cbc:InhalationToxicityZoneCode>None</cbc:InhalationToxicityZoneCode>
          <cbc:TransportAuthorizationCode>CAO</cbc:TransportAuthorizationCode>
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
  </cac:Shipment>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode>Original</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode>Paper</cbc:DistributionTypeCode>
    <cbc:DistributionType>With the goods</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41174</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Airport Cargo</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode>Copy</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode>Electronic</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bayforth Forwarding</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>KAC-SIG-KAC-WB-26-0717</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelaro Air Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
