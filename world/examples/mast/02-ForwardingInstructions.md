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

### Freight Forwarder Party

Inside `FreightForwarderParty`:

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
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mast Hill Road**  
  Street of the postal address. identity of Selanu Telecom (world/parties.json).
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
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **8507.60** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item battery-pack of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/HazardousItem/ID` = **SE-BAT-48100-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **9**  
  The class shown on the placard.
- `GoodsItem/Item/HazardousItem/PlacardEndorsement` = **9A**  
  The hazard label on the package.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **3480** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `GoodsItem/Item/HazardousItem/EmergencyProceduresCode` = **F-A, S-I**  
  The emergency schedules for ships (EmS).
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **147**  
  The emergency response guide number.
- `GoodsItem/Item/HazardousItem/TunnelRestrictionCode` = **E**  
  The tunnel restriction code for road transport.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **9**  
  The UN hazard class.
- `GoodsItem/Temperature/AttributeID` = **Transport**  
  The temperature in transport.
- `GoodsItem/Temperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `GoodsItem/Temperature/MeasureCode` = **Target**  
  The target.
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
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **8531.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item smoke-detector of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the placard.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label, the UN number on the package.**  
  What the shipper adds.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2911** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `GoodsItem/Item/HazardousItem/EmergencyProceduresCode` = **None**  
  The emergency schedules for ships (EmS).
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **161**  
  The emergency response guide number.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
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
- `GoodsItem/Temperature/MeasureCode` = **Target**  
  The target.
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
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **3814.00** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item coating-stripper of Saltmere Engineering (world/items.json).
- `GoodsItem/Item/HazardousItem/ID` = **SE-CS-05-DG**  
  The seller's dangerous goods record of the item.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **8**  
  The class shown on the placard.
- `GoodsItem/Item/HazardousItem/PlacardEndorsement` = **8**  
  The hazard label on the package.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Packed as the rules require.**  
  What the shipper adds.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2920** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **II**  
  The packing group: medium danger.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **Medium danger**  
  In words.
- `GoodsItem/Item/HazardousItem/EmergencyProceduresCode` = **F-E, S-C**  
  The emergency schedules for ships (EmS).
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **132**  
  The emergency response guide number.
- `GoodsItem/Item/HazardousItem/TunnelRestrictionCode` = **D/E**  
  The tunnel restriction code for road transport.
- `GoodsItem/Item/HazardousItem/MaritimePollutantCode` = **N**  
  Not a marine pollutant.
- `GoodsItem/Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
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
- `GoodsItem/Item/HazardousItem/SecondaryHazard/EmergencyProceduresCode` = **F-E**  
  The fire schedule.
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
- `GoodsItem/Temperature/MeasureCode` = **Target**  
  The target.
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
          <cbc:StreetName>Mast Hill Road</cbc:StreetName>
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
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">8507.60</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-BAT-48100-DG</cbc:ID>
          <cbc:PlacardNotation>9</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>9A</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>State of charge below 30 %, as the air rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UNCL8273">3480</cbc:UNDGCode>
          <cbc:EmergencyProceduresCode>F-A, S-I</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode>147</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode>E</cbc:TunnelRestrictionCode>
          <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode>UN</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN3480</cbc:MarkingID>
          <cbc:HazardClassID>9</cbc:HazardClassID>
        </cac:HazardousItem>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID>Transport</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">20</cbc:Measure>
        <cbc:MeasureCode>Target</cbc:MeasureCode>
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
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">8531.10</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-SMK-10-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Excepted package: no radioactive label, the UN number on the package.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UNCL8273">2911</cbc:UNDGCode>
          <cbc:EmergencyProceduresCode>None</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode>161</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode>UN</cbc:HazardousCategoryCode>
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
        <cbc:MeasureCode>Target</cbc:MeasureCode>
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
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">3814.00</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-CS-05-DG</cbc:ID>
          <cbc:PlacardNotation>8</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>8</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>Packed as the rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UNCL8273">2920</cbc:UNDGCode>
          <cbc:UNPackingGroupCode>II</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>Medium danger</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode>F-E, S-C</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode>132</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode>D/E</cbc:TunnelRestrictionCode>
          <cbc:MaritimePollutantCode>N</cbc:MaritimePollutantCode>
          <cbc:TechnicalName>ethanolamine, propanol</cbc:TechnicalName>
          <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode>UN</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2920</cbc:MarkingID>
          <cbc:HazardClassID>8</cbc:HazardClassID>
          <cac:SecondaryHazard>
            <cbc:ID>3</cbc:ID>
            <cbc:PlacardNotation>3</cbc:PlacardNotation>
            <cbc:PlacardEndorsement>3</cbc:PlacardEndorsement>
            <cbc:EmergencyProceduresCode>F-E</cbc:EmergencyProceduresCode>
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
        <cbc:MeasureCode>Target</cbc:MeasureCode>
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
