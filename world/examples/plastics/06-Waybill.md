# Waybill: Fiumella Barges to Rinova Recovery

*Example 6 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The inland waterway consignment note, issued to the shipper.

[The XML file](06-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:plastics**  
  The business process the document belongs to: the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)".
- `ProfileExecutionID` = **PLASTICS-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FB-WB-26-0890**  
  The consignment note number.
- `CarrierAssignedID` = **FB-CMNI-26-0882**  
  The carrier's own number for the carriage.
- `UUID` = **0a38e2bd-26a7-55f9-833d-9ab2e55cfd4a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **Issued**  
  The note is issued and in force.
- `IssueDate` = **2026-04-19**  
  Issued when the barge is loaded.
- `IssueTime` = **09:38:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Inland waterway consignment note under the CMNI**  
  The kind of transport document.
- `Description` = **The barge from the quay next to the recovery plant down the river to the packaging maker.**  
  The carriage in words.
- `Note` = **Three originals: consignor, consignee, carrier.**  
  As the convention prescribes.
- `ShippingOrderID` = **RR-CS-26-0885**  
  The shipper's booking the carriage fulfils.
- `WaybillTypeCode` = **CMNI**  
  The convention the document follows.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `AdValoremIndicator` = **false**  
  No value declared to raise the carrier's liability.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Fiumella Barges**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.fiumella.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Fiumella Barges (world/parties.json).
- `IndustryClassificationCode` = **5022** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Fiumella Barges (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Fiumella Barges**  
  The trading name; identity of Fiumella Barges (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Banchina del Fiume**  
  Street of the postal address. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits). identity of Fiumella Barges (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Fiumella Barges (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Fiumella Barges SRU**  
  The name under which the party is registered for value added tax; identity of Fiumella Barges (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007347248**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Fiumella Barges (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Fiumella Barges SRU**  
  The name under which the party is registered, with its legal form; identity of Fiumella Barges (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104959**  
  Number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Fiumella Barges (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Fiumella Barges (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Contact/Name` = **Chartering desk**  
  The desk that handles this document; identity of Fiumella Barges (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Fiumella Barges (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Fiumella Barges (world/parties.json).
- `Contact/Telephone` = **+999 1 4170 4959**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Fiumella Barges (world/parties.json).
- `Contact/ElectronicMail` = **chartering@fiumella.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Fiumella Barges (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Fiumella Barges (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Fiumella Barges (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.rinova.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rinova Recovery (world/parties.json).
- `IndustryClassificationCode` = **3830** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rinova Recovery (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Rinova Recovery (world/parties.json).
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Via del Riciclo**  
  Street of the postal address. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered for value added tax; identity of Rinova Recovery (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007318479**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Rinova Recovery (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered, with its legal form; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104548**  
  Number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Rinova Recovery (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rinova Recovery (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rinova Recovery (world/parties.json).
- `Contact/Telephone` = **+999 1 4140 4548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Rinova Recovery (world/parties.json).
- `Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/Purpose` = **Recovery of non-hazardous plastic waste**  
  What the authority has authorized the party to do; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/ValidityPeriod/EndDate` = **2029-12-31**  
  The authorization expires on this date.
- `PartyAuthorization/Certificate/ID` = **XU-ENV-2024-0311**  
  The number of the permit.
- `PartyAuthorization/Certificate/CertificateTypeCode` = **Permit**  
  A permit issued by an authority of the party's country.
- `PartyAuthorization/Certificate/CertificateType` = **Operating permit**  
  The kind of certificate, in words.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rinova Recovery**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Fiumella Barges**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **RR-SH-26-0889**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight on board.
- `Consignment/ID` = **RR-CS-26-0885**  
  The seller's consignment number.
- `Consignment/CarrierAssignedID` = **FB4-26-031/2**  
  The barge operator's number: the second lot of the voyage.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.rivermouth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **2220** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `Consignment/ConsigneeParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyTaxScheme/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered for state sales tax; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyTaxScheme/CompanyID` = **CO-1238220**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered, with its legal form; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **20412740**  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Consignment/ConsigneeParty/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 3850 2740**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The freight, a charge.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **River freight**  
  What it is for.
- `Consignment/FreightAllowanceCharge/Amount` = **179400** (currencyID `XUF`)  
  120 tonnes at 1,495 ferra.
- `Consignment/FreightAllowanceCharge/BaseAmount` = **1495** (currencyID `XUF`)  
  The rate per tonne.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  Down the river, from the recovery plant's quay to the river quay in Lumeport.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **8** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 8: inland water transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **FB4-26-031**  
  The barge operator's voyage number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU**  
  The country the means of transport is registered in.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **Downstream**  
  The direction of the journey, as the carrier codes its services.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **INLAND**  
  The carrier's code for the kind of means: fiumella iv; the fleet of Fiumella Barges (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XU-IW-08042** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Fiumella IV**  
  The vessel's name; the fleet of Fiumella Barges (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **XUBF4**  
  The radio call sign, with the world's country code.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **999801042**  
  The Maritime Mobile Service Identity, nine digits; 999 is no real country's maritime identification digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **1210** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **860** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **Dry cargo barge**  
  The kind of vessel.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Ferrano**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Quay of Rinova Recovery, Ferrano**  
  Where the bags are loaded.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **River quay, Lumeport**  
  The place named in the CPT terms.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceDate` = **2026-04-19**  
  Loading finished: 120 bags in the hold.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceTime` = **13:30:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceDate` = **2026-04-20**  
  The barge leaves Urvania at the river border.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceTime` = **16:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-04-22**  
  Planned unloading at the Lumeport quay.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **08:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceDate` = **2026-04-19**  
  The barge operator takes over the bags at the quay.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceTime` = **09:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedTransitPeriod/DurationMeasure` = **3** (unitCode `DAY`)  
  Three days downstream, with the locks.
- `Consignment/MainCarriageShipmentStage/MasterPerson/FirstName` = **Tomaso**  
  The skipper of the barge.
- `Consignment/MainCarriageShipmentStage/MasterPerson/FamilyName` = **Riverra**  
  The family name.
- `Consignment/MainCarriageShipmentStage/MasterPerson/JobTitle` = **Skipper**  
  The person's position.
- `GoodsItem/ID` = **1**  
  The only goods item.
- `GoodsItem/SequenceNumberID` = **1**  
  Its place in the cargo list.
- `GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are.
- `GoodsItem/DeclaredForCarriageValueAmount` = **9984000** (currencyID `XUF`)  
  Declared to the barge operator, which raises its liability to this value.
- `GoodsItem/ValueAmount` = **9984000** (currencyID `XUF`)  
  The value of the goods, the sales price under CPT.
- `GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  With the bags.
- `GoodsItem/NetWeightMeasure` = **120000** (unitCode `KGM`)  
  The granulate alone.
- `GoodsItem/NetNetWeightMeasure` = **120000** (unitCode `KGM`)  
  No inner packaging: the same as the net weight.
- `GoodsItem/ChargeableWeightMeasure` = **120000** (unitCode `KGM`)  
  The freight is charged per tonne of granulate.
- `GoodsItem/GrossVolumeMeasure` = **204** (unitCode `MTQ`)  
  The 120 bags take 1.7 m³ each.
- `GoodsItem/NetVolumeMeasure` = **130** (unitCode `MTQ`)  
  The granulate's own volume, at 0.92 tonne per m³.
- `GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  120 tonnes.
- `GoodsItem/ChargeableQuantity` = **120** (unitCode `TNE`)  
  The tonnes charged.
- `GoodsItem/ReturnableQuantity` = **120** (unitCode `H87`)  
  The 120 jumbo bags go back to the recovery plant.
- `GoodsItem/TraceID` = **RR-PE-LOT-26-0416**  
  The lot on the bags' labels.
- `GoodsItem/OrderLineReference/LineID` = **1**  
  The order line.
- `GoodsItem/OrderLineReference/OrderReference/ID` = **RP-PO-26-0882**  
  The buyer's order.
- `GoodsItem/OriginAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `GoodsItem/OriginAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `GoodsItem/OriginAddress/StreetName` = **Via del Riciclo**  
  Street of the postal address. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Rinova Recovery (world/parties.json).
- `GoodsItem/OriginAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `GoodsItem/OriginAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `GoodsItem/OriginAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `GoodsItem/Delivery/LatestDeliveryDate` = **2026-04-23**  
  The packaging maker's production starts the day after.
- `GoodsItem/Pickup/EarliestPickupDate` = **2026-04-19**  
  The bags are ready on the quay.
- `GoodsItem/Pickup/EarliestPickupTime` = **08:00:00**  
  From eight.
- `GoodsItem/Pickup/LatestPickupDate` = **2026-04-19**  
  They must go the same day.
- `GoodsItem/Pickup/LatestPickupTime` = **16:00:00**  
  Before the quay closes.
- `GoodsItem/Despatch/ActualDespatchDate` = **2026-04-19**  
  The barge cast off.
- `GoodsItem/Despatch/ActualDespatchTime` = **15:10:00**  
  In the afternoon.
- `GoodsItem/MeasurementDimension/AttributeID` = **Height**  
  The height of one filled bag.
- `GoodsItem/MeasurementDimension/Measure` = **1300** (unitCode `MMT`)  
  In millimetres.
- `GoodsItem/ContainingPackage/ID` = **JB-001..120**  
  The bags, numbered 1 to 120.
- `GoodsItem/ContainingPackage/Quantity` = **120** (unitCode `H87`)  
  120 bags.
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The bags go back for reuse.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **JB**  
  UN/ECE Recommendation 21 code JB: bag, jumbo.
- `GoodsItem/ContainingPackage/PackagingType` = **Jumbo bag of one tonne with four lifting loops**  
  In words.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Woven polypropylene**  
  What the bags are made of.
- `GoodsItem/ShipmentDocumentReference/ID` = **FB-TEP-26-0886**  
  The transport plan of the sailing.
- `GoodsItem/EnergyConsumptionAllocation/EnergySourceTypeCode` = **Diesel**  
  The barge's engine fuel.
- `GoodsItem/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **5400** (unitCode `KWH`)  
  The goods' share of the voyage's energy, as fuel energy.

### Document Reference

Inside `DocumentReference`:

- `ID` = **FB-TEP-26-0886**  
  The transport plan under which the carriage is performed.

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
- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The electronic copy.
- `DocumentTypeCode` = **Copy**  
  A copy.
- `DistributionTypeCode` = **Electronic**  
  Sent as this UBL document.
- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FB-SIG-FB-WB-26-0890**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Fiumella Barges**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:plastics</cbc:ProfileID>
  <cbc:ProfileExecutionID>PLASTICS-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FB-WB-26-0890</cbc:ID>
  <cbc:CarrierAssignedID>FB-CMNI-26-0882</cbc:CarrierAssignedID>
  <cbc:UUID>0a38e2bd-26a7-55f9-833d-9ab2e55cfd4a</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode>Issued</cbc:StatusCode>
  <cbc:IssueDate>2026-04-19</cbc:IssueDate>
  <cbc:IssueTime>09:38:00</cbc:IssueTime>
  <cbc:Name>Inland waterway consignment note under the CMNI</cbc:Name>
  <cbc:Description>The barge from the quay next to the recovery plant down the river to the packaging maker.</cbc:Description>
  <cbc:Note>Three originals: consignor, consignee, carrier.</cbc:Note>
  <cbc:ShippingOrderID>RR-CS-26-0885</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode>CMNI</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Fiumella Barges</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.fiumella.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">5022</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName>Banchina del Fiume</cbc:StreetName>
      <cbc:BuildingNumber>52</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4170</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Fiumella Barges SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU007347248</cbc:CompanyID>
      <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Fiumella Barges SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104959</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XU:CR</cbc:ID>
        <cbc:Name>Commercial register of Urvania</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Chartering desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 4170 4959</cbc:Telephone>
      <cbc:ElectronicMail>chartering@fiumella.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104959</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.rinova.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3830</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName>Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU007318479</cbc:CompanyID>
      <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104548</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XU:CR</cbc:ID>
        <cbc:Name>Commercial register of Urvania</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 4140 4548</cbc:Telephone>
      <cbc:ElectronicMail>customer@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:PartyAuthorization>
      <cbc:Purpose>Recovery of non-hazardous plastic waste</cbc:Purpose>
      <cac:ValidityPeriod>
        <cbc:EndDate>2029-12-31</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:Certificate>
        <cbc:ID>XU-ENV-2024-0311</cbc:ID>
        <cbc:CertificateTypeCode>Permit</cbc:CertificateTypeCode>
        <cbc:CertificateType>Operating permit</cbc:CertificateType>
      </cac:Certificate>
    </cac:PartyAuthorization>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>RR-SH-26-0889</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>RR-CS-26-0885</cbc:ID>
      <cbc:CarrierAssignedID>FB4-26-031/2</cbc:CarrierAssignedID>
      <cac:ConsigneeParty>
        <cbc:WebsiteURI>https://www.rivermouth.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">2220</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Rivermouth Packaging</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
          <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
          <cbc:StreetName>Estuary Road</cbc:StreetName>
          <cbc:BuildingNumber>28</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38505</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
          <cbc:CompanyID>CO-1238220</cbc:CompanyID>
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
          <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
          <cbc:CompanyID>20412740</cbc:CompanyID>
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
          <cbc:Name>Order desk</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 2 3850 2740</cbc:Telephone>
          <cbc:ElectronicMail>order@rivermouth.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReason>River freight</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XUF">179400</cbc:Amount>
        <cbc:BaseAmount currencyID="XUF">1495</cbc:BaseAmount>
      </cac:FreightAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">8</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>FB4-26-031</cbc:JourneyID>
          <cbc:RegistrationNationalityID>XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode>Downstream</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode>INLAND</cbc:TransportMeansTypeCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XU-IW-08042</cbc:VesselID>
            <cbc:VesselName>Fiumella IV</cbc:VesselName>
            <cbc:RadioCallSignID>XUBF4</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>999801042</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">1210</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">860</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode>Dry cargo barge</cbc:ShipConfigurationCode>
            <cac:RegistryPortLocation>
              <cbc:Name>Ferrano</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:Name>River quay, Lumeport</cbc:Name>
        </cac:UnloadingPortLocation>
        <cac:LoadingTransportEvent>
          <cbc:OccurrenceDate>2026-04-19</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:30:00</cbc:OccurrenceTime>
        </cac:LoadingTransportEvent>
        <cac:ExportationTransportEvent>
          <cbc:OccurrenceDate>2026-04-20</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>16:00:00</cbc:OccurrenceTime>
        </cac:ExportationTransportEvent>
        <cac:DischargeTransportEvent>
          <cbc:OccurrenceDate>2026-04-22</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>08:00:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        </cac:DischargeTransportEvent>
        <cac:TakeoverTransportEvent>
          <cbc:OccurrenceDate>2026-04-19</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>09:00:00</cbc:OccurrenceTime>
        </cac:TakeoverTransportEvent>
        <cac:EstimatedTransitPeriod>
          <cbc:DurationMeasure unitCode="DAY">3</cbc:DurationMeasure>
        </cac:EstimatedTransitPeriod>
        <cac:MasterPerson>
          <cbc:FirstName>Tomaso</cbc:FirstName>
          <cbc:FamilyName>Riverra</cbc:FamilyName>
          <cbc:JobTitle>Skipper</cbc:JobTitle>
        </cac:MasterPerson>
      </cac:MainCarriageShipmentStage>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
      <cbc:Description>Recycled PE granulate</cbc:Description>
      <cbc:DeclaredForCarriageValueAmount currencyID="XUF">9984000</cbc:DeclaredForCarriageValueAmount>
      <cbc:ValueAmount currencyID="XUF">9984000</cbc:ValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cbc:NetWeightMeasure unitCode="KGM">120000</cbc:NetWeightMeasure>
      <cbc:NetNetWeightMeasure unitCode="KGM">120000</cbc:NetNetWeightMeasure>
      <cbc:ChargeableWeightMeasure unitCode="KGM">120000</cbc:ChargeableWeightMeasure>
      <cbc:GrossVolumeMeasure unitCode="MTQ">204</cbc:GrossVolumeMeasure>
      <cbc:NetVolumeMeasure unitCode="MTQ">130</cbc:NetVolumeMeasure>
      <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
      <cbc:ChargeableQuantity unitCode="TNE">120</cbc:ChargeableQuantity>
      <cbc:ReturnableQuantity unitCode="H87">120</cbc:ReturnableQuantity>
      <cbc:TraceID>RR-PE-LOT-26-0416</cbc:TraceID>
      <cac:OrderLineReference>
        <cbc:LineID>1</cbc:LineID>
        <cac:OrderReference>
          <cbc:ID>RP-PO-26-0882</cbc:ID>
        </cac:OrderReference>
      </cac:OrderLineReference>
      <cac:OriginAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via del Riciclo</cbc:StreetName>
        <cbc:BuildingNumber>31</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4140</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:OriginAddress>
      <cac:Delivery>
        <cbc:LatestDeliveryDate>2026-04-23</cbc:LatestDeliveryDate>
      </cac:Delivery>
      <cac:Pickup>
        <cbc:EarliestPickupDate>2026-04-19</cbc:EarliestPickupDate>
        <cbc:EarliestPickupTime>08:00:00</cbc:EarliestPickupTime>
        <cbc:LatestPickupDate>2026-04-19</cbc:LatestPickupDate>
        <cbc:LatestPickupTime>16:00:00</cbc:LatestPickupTime>
      </cac:Pickup>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-04-19</cbc:ActualDespatchDate>
        <cbc:ActualDespatchTime>15:10:00</cbc:ActualDespatchTime>
      </cac:Despatch>
      <cac:MeasurementDimension>
        <cbc:AttributeID>Height</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1300</cbc:Measure>
      </cac:MeasurementDimension>
      <cac:ContainingPackage>
        <cbc:ID>JB-001..120</cbc:ID>
        <cbc:Quantity unitCode="H87">120</cbc:Quantity>
        <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
        <cbc:PackagingTypeCode>JB</cbc:PackagingTypeCode>
        <cbc:PackagingType>Jumbo bag of one tonne with four lifting loops</cbc:PackagingType>
        <cbc:PackingMaterial>Woven polypropylene</cbc:PackingMaterial>
      </cac:ContainingPackage>
      <cac:ShipmentDocumentReference>
        <cbc:ID>FB-TEP-26-0886</cbc:ID>
      </cac:ShipmentDocumentReference>
      <cac:EnergyConsumptionAllocation>
        <cbc:EnergySourceTypeCode>Diesel</cbc:EnergySourceTypeCode>
        <cbc:AllocatedEnergyMeasure unitCode="KWH">5400</cbc:AllocatedEnergyMeasure>
      </cac:EnergyConsumptionAllocation>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>FB-TEP-26-0886</cbc:ID>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode>Original</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode>Paper</cbc:DistributionTypeCode>
    <cbc:DistributionType>With the goods</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode>Copy</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode>Electronic</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FB-SIG-FB-WB-26-0890</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Fiumella Barges</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
