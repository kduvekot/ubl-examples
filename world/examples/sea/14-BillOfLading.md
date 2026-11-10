# Bill of Lading: Tidewell Ocean Lines to Bayforth Forwarding

*Example 14 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Bill of Lading in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-BILL-OF-LADING-SCHEMA)*

The negotiable bill of lading, issued to the forwarder that gave the instructions; it names the insurer of the cargo and the buyer's 3PL as party to notify on arrival.

[The XML file](14-BillOfLading.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **TOL-BL-26-0139**  
  The bill of lading number.
- `CarrierAssignedID` = **TWL-BK-26-55710**  
  The booking the bill of lading is issued under.
- `IssueDate` = **2026-05-14**  
  Issued when the goods are shipped on board.
- `ShippingOrderID` = **BF-FI-26-0137**  
  The forwarder's booking with the carrier.
- `ToOrderIndicator` = **true**  
  Made out to order: the buyer can transfer it by endorsement.
- `AdValoremIndicator` = **false**  
  No value declared to the carrier: its liability stays limited.
- `OtherInstruction` = **Three originals issued.**  
  How many originals there are.

### Consignor Party

Inside `ConsignorParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
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
  The state, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
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
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 0274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Carrier Party

Inside `CarrierParty`:

- `WebsiteURI` = **https://www.tidewell.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Tidewell Ocean Lines (world/parties.json).
- `IndustryClassificationCode` = **5012** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered for state sales tax; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1235754**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Tidewell Ocean Lines (world/parties.json).
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
- `PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered, with its legal form; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411918**  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1974-03-01**  
  The day the company was entered in the register; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Corp**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **40000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Contact/Name` = **Bookings**  
  The desk that handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Telephone` = **+999 2 3852 1918**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Shipment

Inside `Shipment`:

- `ID` = **LD-SH-26-0132**  
  The shipment carried.
- `GrossWeightMeasure` = **0** (unitCode `KGM`)  
  The gross weight of the cargo.
- `TotalGoodsItemQuantity` = **2** (unitCode `H87`)  
  Benches and side frames.
- `ConsignmentQuantity` = **1** (unitCode `H87`)  
  One consignment.
- `Consignment/ID` = **LD-CS-26-0133**  
  The distributor's consignment number.
- `Consignment/CarrierAssignedID` = **TWL-BK-26-55710**  
  The carrier's booking number.
- `Consignment/ConsignorAssignedID` = **VT-PO-26-0127**  
  The order the goods were sold under.
- `Consignment/FreightForwarderAssignedID` = **LD-FI-26-0131**  
  The forwarder's file: the instructions it received.
- `Consignment/BrokerAssignedID` = **TCB-26-0331**  
  The customs broker's file in Selanu.
- `Consignment/TotalInvoiceAmount` = **50688.00** (currencyID `XBL`)  
  The value of the goods on the sales invoice.
- `Consignment/DeclaredCustomsValueAmount` = **53778.00** (currencyID `XBL`)  
  The CIF value: goods, freight and insurance.
- `Consignment/TariffDescription` = **Furniture, packed, not hazardous**  
  The carrier's commodity tariff, in words.
- `Consignment/TariffCode` = **9401.79**  
  The tariff of the carrier for this cargo: furniture.
- `Consignment/InsurancePremiumAmount` = **140.00** (currencyID `XBL`)  
  The premium the seller paid under CIF.
- `Consignment/ShippingPriorityLevelCode` = **Standard**  
  The normal sailing, no priority loading.
- `Consignment/HandlingCode` = **Deck**  
  The carrier may stow the container on deck.
- `Consignment/HandlingInstructions` = **Keep dry.**  
  The handling, in words.
- `Consignment/Information` = **Shipped on board in apparent good order and condition.**  
  The carrier's clause.
- `Consignment/InsuranceValueAmount` = **59155.80** (currencyID `XBL`)  
  110 % of the CIF value.
- `Consignment/FreeOnBoardValueAmount` = **50688.00** (currencyID `XBL`)  
  The value on board in Lumeport: the goods alone.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `Consignment/ConsigneeParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
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
- `Consignment/ConsigneeParty/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/NotifyParty/WebsiteURI` = **https://www.nalevi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/IndustryClassificationCode` = **5210** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Nalevi Warehousing (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/NotifyParty/PartyName/Name` = **Nalevi Warehousing**  
  The trading name; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/NotifyParty/Language/Name` = **English**  
  The language's name.
- `Consignment/NotifyParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Consignment/NotifyParty/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Lagoon Road**  
  Street of the postal address. identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/NotifyParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/NotifyParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationName` = **Nalevi Warehousing Ltd**  
  The name under which the party is registered, with its legal form; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyLegalEntity/CompanyID` = **IC41722**  
  Number in the Island companies register; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Consignment/NotifyParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Consignment/NotifyParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Consignment/NotifyParty/Contact/Name` = **Goods inwards**  
  The desk that handles this document; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/Telephone` = **+999 3 3000 1722**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/ElectronicMail` = **goods@nalevi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/NotifyParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41722** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Nalevi Warehousing (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/OriginalDespatchParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDespatchParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FinalDeliveryParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FinalDeliveryParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/LogisticsOperatorParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/LogisticsOperatorParty/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/BillOfLadingHolderParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/BillOfLadingHolderParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDepartureCountry/IdentificationCode` = **XB**  
  From Bayvarra.
- `Consignment/FinalDestinationCountry/IdentificationCode` = **XL**  
  To the island.
- `Consignment/DeliveryTerms/ID` = **CIF**  
  Incoterms 2020: cost, insurance and freight to the port of Selanu.
- `Consignment/DeliveryTerms/LossRiskResponsibilityCode` = **Buyer**  
  The risk is the buyer's from on board in Lumeport.
- `Consignment/DeliveryTerms/LossRisk` = **Risk passes when the goods are on board the vessel in Lumeport.**  
  In words.
- `Consignment/DeliveryTerms/Amount` = **53778.00** (currencyID `XBL`)  
  The CIF value the terms are based on.
- `Consignment/DeliveryTerms/DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/DeliveryTerms/DeliveryLocation/Name` = **Port of Selanu**  
  The named port of destination.
- `Consignment/DeliveryTerms/DeliveryLocation/Address/Country/IdentificationCode` = **XL**  
  The country the place is in.
- `Consignment/DeliveryTerms/AllowanceCharge/ChargeIndicator` = **true**  
  A cost under the terms.
- `Consignment/DeliveryTerms/AllowanceCharge/AllowanceChargeReason` = **Terminal handling at Selanu, for the buyer**  
  Under CIF the buyer pays the unloading.
- `Consignment/DeliveryTerms/AllowanceCharge/Amount` = **185.00** (currencyID `XBL`)  
  The carrier's tariff.
- `Consignment/PaymentTerms/Note` = **Ocean freight payable before release of the bill of lading.**  
  The carrier's terms.
- `Consignment/CollectPaymentTerms/Note` = **Terminal handling at Selanu collect from the consignee.**  
  The buyer pays it there.
- `Consignment/DisbursementPaymentTerms/Note` = **Island customs fees advanced by the broker and recharged to the consignee.**  
  Paid out for someone else.
- `Consignment/PrepaidPaymentTerms/Note` = **Ocean freight and bunker surcharge prepaid by the shipper.**  
  CIF: the seller pays.
- `Consignment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The basic ocean freight.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **Ocean freight, 40-foot container**  
  In words.
- `Consignment/FreightAllowanceCharge/Amount` = **2700.00** (currencyID `XBL`)  
  The carrier's rate.
- `Consignment/ExtraAllowanceCharge/ChargeIndicator` = **true**  
  A surcharge.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReason` = **Bunker surcharge**  
  For the fuel price.
- `Consignment/ExtraAllowanceCharge/Amount` = **250.00** (currencyID `XBL`)  
  Together with the freight: the 2,950 lume the forwarder invoices.
- `Consignment/MainCarriageShipmentStage/ID` = **2**  
  By sea from Lumeport to Selanu.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **TH-26-19E**  
  The voyage number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB**  
  The country the means of transport is registered in.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **Eastbound**  
  The direction of the journey, as the carrier codes its services.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **SEA**  
  The carrier's code for the kind of means: tidewell harbour; the fleet of Tidewell Ocean Lines (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **XBTH7**  
  The radio call sign, with the world's country code.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **999702117**  
  The Maritime Mobile Service Identity, nine digits; 999 is no real country's maritime identification digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipsRequirements` = **Shore power at the container quay.**  
  What the ship needs in port.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/SegregatedBallastMeasure` = **2480** (unitCode `TNE`)  
  The capacity of the tanks for ballast water only.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **Feeder container ship, 1,000 TEU**  
  The kind of vessel.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Port of Lumeport**  
  The port of loading.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XB**  
  The country the place is in.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Port of Selanu**  
  The port of discharge.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XL**  
  The country the place is in.
- `Consignment/MainCarriageShipmentStage/TransshipPortLocation/Name` = **None: a direct sailing**  
  No transhipment on the way.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/OccurrenceDate` = **2026-05-18**  
  The container is available at Selanu.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/OccurrenceTime` = **14:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/AvailabilityTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/OccurrenceDate` = **2026-05-13**  
  Stacked at the quay until loading.
- `Consignment/MainCarriageShipmentStage/StorageTransportEvent/OccurrenceTime` = **10:30:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/OccurrenceDate` = **2026-05-13**  
  The terminal accepted the container.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/OccurrenceTime` = **10:15:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/Name` = **Port of Lumeport**  
  The freight is payable in Lumeport.
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/Address/Country/IdentificationCode` = **XB**  
  The country the place is in.
- `Consignment/PreCarriageShipmentStage/ID` = **1**  
  By truck from Marrowdale to the port.
- `Consignment/PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport.
- `Consignment/PreCarriageShipmentStage/PreCarriageIndicator` = **true**  
  Before the main carriage.
- `Consignment/PreCarriageShipmentStage/CabotageIndicator` = **true**  
  An Urvanian truck carrying within Bayvarra: cabotage, allowed under the trade accord for a return trip.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU**  
  The country the means of transport is registered in.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **TE**  
  The carrier's code for the kind of means: tractor unit 07 with curtain-side trailer; the fleet of Trasvia Haulage (world/parties.json).
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 KT**  
  The registration plate of the truck; the fleet of Trasvia Haulage (world/parties.json).
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **UR TR 3381**  
  The trailer's own plate.
- `Consignment/PreCarriageShipmentStage/TransportMeans/OwnerParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/TransportMeans/OwnerParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **Loading length**  
  The length of the loading floor.
- `Consignment/PreCarriageShipmentStage/TransportMeans/MeasurementDimension/Measure` = **13.6** (unitCode `MTR`)  
  Room for 33 pallets.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceDate` = **2026-05-13**  
  The container was dropped at the container quay.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceTime` = **10:15:00**  
  The local time.
- `Consignment/OnCarriageShipmentStage/ID` = **3**  
  By truck from the port of Selanu to the 3PL.
- `Consignment/OnCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport.
- `Consignment/OnCarriageShipmentStage/OnCarriageIndicator` = **true**  
  After the main carriage.
- `Consignment/OnCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OnCarriageShipmentStage/CarrierParty/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OnCarriageShipmentStage/WarehousingTransportEvent/OccurrenceDate` = **2026-05-19**  
  Stored at the 3PL until called off.
- `Consignment/OnCarriageShipmentStage/WarehousingTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/OccurrenceDate` = **2026-05-19**  
  Planned receipt at the 3PL.
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container's number: the owner code of the ocean carrier, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **42G1**  
  ISO 6346 size and type: 40 feet, 8 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL**  
  A full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **false**  
  A dry container.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **3750** (unitCode `KGM`)  
  The verified gross mass: cargo and the container's own weight of 3,750 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **3750** (unitCode `KGM`)  
  The empty container's own weight, as marked on its door.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **140282**  
  Bay 14, row 02, tier 82: on deck, as planned by the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **TWL-S-0884213**  
  The carrier's seal, put on when the container was packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **Carrier**  
  Issued by the ocean carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  Put on by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-001**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 001 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-001**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-002**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 002 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-002**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-003**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 003 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-003**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-004**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 004 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-004**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-005**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 005 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-005**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-006**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 006 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-006**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-007**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 007 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-007**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-008**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 008 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-008**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-009**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 009 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-009**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-010**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 010 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-010**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-011**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 011 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-011**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-012**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 012 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-012**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-013**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 013 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-013**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-014**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 014 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-014**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-015**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 015 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-015**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-016**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 016 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-016**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-017**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 017 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-017**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-018**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 018 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-018**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-019**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 019 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-019**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-020**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 020 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-020**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-021**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 021 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-021**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-022**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 022 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-022**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-023**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 023 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-023**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-024**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `H87`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 024 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-024**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **LD-26-025**  
  The number on the pallet label.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `H87`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `H87`)  
  12 boxed side frames on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 025 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **LD-26-025**  
  The pallet's barcode, scanned at each handover.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ID` = **1**  
  The goods in the container, as one item for the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/Description` = **Park benches and spare side frames**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ID` = **VGM-26-0510**  
  The shipper's weight declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDate` = **2026-05-12**  
  Weighed when packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingTime` = **15:30:00**  
  After closing the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingMethodCode` = **SM2** (listID `IMO SOLAS`)  
  SOLAS method 2: the cargo and packing weighed and added to the tare.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceID` = **LD-SCALE-03**  
  The scale of the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceType` = **Platform scale**  
  Its kind.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/GrossMassMeasure` = **3750** (unitCode `KGM`)  
  The verified gross mass.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ShipperParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ShipperParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ResponsibleParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ResponsibleParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/ID` = **VGM-26-0510**  
  The signed weight declaration sent to the carrier.
- `Consignment/FirstArrivalPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/FirstArrivalPortLocation/Name` = **Port of Selanu**  
  The first port of call after Lumeport.
- `Consignment/FirstArrivalPortLocation/Address/Country/IdentificationCode` = **XL**  
  The country the place is in.
- `Consignment/LastExitPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/LastExitPortLocation/Name` = **Port of Lumeport**  
  The last port in Bayvarra.
- `Consignment/LastExitPortLocation/Address/Country/IdentificationCode` = **XB**  
  The country the place is in.
- `InsurancePolicy/InsuredValueAmount` = **59155.80** (currencyID `XBL`)  
  The insured value, 110 % of the CIF value.
- `InsurancePolicy/InsurerParty/WebsiteURI` = **https://www.wavesure.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/IndustryClassificationCode` = **6512** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Wavesure Cargo Insurance (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `InsurancePolicy/InsurerParty/PartyName/Name` = **Wavesure Cargo Insurance**  
  The trading name; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Language/ID` = **en**  
  English, the language the party does business in.
- `InsurancePolicy/InsurerParty/Language/Name` = **English**  
  The language's name.
- `InsurancePolicy/InsurerParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `InsurancePolicy/InsurerParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `InsurancePolicy/InsurerParty/PostalAddress/StreetName` = **Beacon Avenue**  
  Street of the postal address. identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/BuildingNumber` = **55**  
  Building number of the postal address. identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/PostalZone` = **38524**  
  Postal code in Bayvarra's format (5 digits). identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `InsurancePolicy/InsurerParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `InsurancePolicy/InsurerParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/RegistrationName` = **Wavesure Cargo Insurance Ltd**  
  The name under which the party is registered for state sales tax; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyTaxScheme/CompanyID` = **CO-1234521**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationName` = **Wavesure Cargo Insurance Ltd**  
  The name under which the party is registered, with its legal form; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyID` = **20411507**  
  Number in the Federal business register of Bayvarra; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `InsurancePolicy/InsurerParty/Contact/Name` = **Cargo claims**  
  The desk that handles this document; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/JobTitle` = **Client relationship manager**  
  The job of the person who answers at the desk; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/Department` = **Client services**  
  The department the desk belongs to; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/Telephone` = **+999 2 3852 1507**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/ElectronicMail` = **cargo@wavesure.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `InsurancePolicy/InsurerParty/ElectronicAddress/ElectronicAddressID` = **XB:20411507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Wavesure Cargo Insurance (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<BillOfLading xmlns="urn:oasis:names:specification:ubl:schema:xsd:BillOfLading-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>TOL-BL-26-0139</cbc:ID>
  <cbc:CarrierAssignedID>TWL-BK-26-55710</cbc:CarrierAssignedID>
  <cbc:IssueDate>2026-05-14</cbc:IssueDate>
  <cbc:ShippingOrderID>BF-FI-26-0137</cbc:ShippingOrderID>
  <cbc:ToOrderIndicator>true</cbc:ToOrderIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Three originals issued.</cbc:OtherInstruction>
  <cac:ConsignorParty>
    <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID>UL-1230822</cbc:CompanyID>
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
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20410274</cbc:CompanyID>
      <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Medium</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 0274</cbc:Telephone>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ConsignorParty>
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
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>LD-SH-26-0132</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">0</cbc:GrossWeightMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="H87">2</cbc:TotalGoodsItemQuantity>
    <cbc:ConsignmentQuantity unitCode="H87">1</cbc:ConsignmentQuantity>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0133</cbc:ID>
      <cbc:CarrierAssignedID>TWL-BK-26-55710</cbc:CarrierAssignedID>
      <cbc:ConsignorAssignedID>VT-PO-26-0127</cbc:ConsignorAssignedID>
      <cbc:FreightForwarderAssignedID>LD-FI-26-0131</cbc:FreightForwarderAssignedID>
      <cbc:BrokerAssignedID>TCB-26-0331</cbc:BrokerAssignedID>
      <cbc:TotalInvoiceAmount currencyID="XBL">50688.00</cbc:TotalInvoiceAmount>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">53778.00</cbc:DeclaredCustomsValueAmount>
      <cbc:TariffDescription>Furniture, packed, not hazardous</cbc:TariffDescription>
      <cbc:TariffCode>9401.79</cbc:TariffCode>
      <cbc:InsurancePremiumAmount currencyID="XBL">140.00</cbc:InsurancePremiumAmount>
      <cbc:ShippingPriorityLevelCode>Standard</cbc:ShippingPriorityLevelCode>
      <cbc:HandlingCode>Deck</cbc:HandlingCode>
      <cbc:HandlingInstructions>Keep dry.</cbc:HandlingInstructions>
      <cbc:Information>Shipped on board in apparent good order and condition.</cbc:Information>
      <cbc:InsuranceValueAmount currencyID="XBL">59155.80</cbc:InsuranceValueAmount>
      <cbc:FreeOnBoardValueAmount currencyID="XBL">50688.00</cbc:FreeOnBoardValueAmount>
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
      <cac:NotifyParty>
        <cbc:WebsiteURI>https://www.nalevi.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">5210</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Nalevi Warehousing</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
          <cbc:StreetName>Lagoon Road</cbc:StreetName>
          <cbc:BuildingNumber>9</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Nalevi Warehousing Ltd</cbc:RegistrationName>
          <cbc:CompanyID>IC41722</cbc:CompanyID>
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
          <cbc:Name>Goods inwards</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 3 3000 1722</cbc:Telephone>
          <cbc:ElectronicMail>goods@nalevi.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41722</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:NotifyParty>
      <cac:OriginalDespatchParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:OriginalDespatchParty>
      <cac:FinalDeliveryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Velumi Trading</cbc:Name>
        </cac:PartyName>
      </cac:FinalDeliveryParty>
      <cac:LogisticsOperatorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Nalevi Warehousing</cbc:Name>
        </cac:PartyName>
      </cac:LogisticsOperatorParty>
      <cac:BillOfLadingHolderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Velumi Trading</cbc:Name>
        </cac:PartyName>
      </cac:BillOfLadingHolderParty>
      <cac:OriginalDepartureCountry>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:FinalDestinationCountry>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
      </cac:FinalDestinationCountry>
      <cac:DeliveryTerms>
        <cbc:ID>CIF</cbc:ID>
        <cbc:LossRiskResponsibilityCode>Buyer</cbc:LossRiskResponsibilityCode>
        <cbc:LossRisk>Risk passes when the goods are on board the vessel in Lumeport.</cbc:LossRisk>
        <cbc:Amount currencyID="XBL">53778.00</cbc:Amount>
        <cac:DeliveryLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:DeliveryLocation>
        <cac:AllowanceCharge>
          <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
          <cbc:AllowanceChargeReason>Terminal handling at Selanu, for the buyer</cbc:AllowanceChargeReason>
          <cbc:Amount currencyID="XBL">185.00</cbc:Amount>
        </cac:AllowanceCharge>
      </cac:DeliveryTerms>
      <cac:PaymentTerms>
        <cbc:Note>Ocean freight payable before release of the bill of lading.</cbc:Note>
      </cac:PaymentTerms>
      <cac:CollectPaymentTerms>
        <cbc:Note>Terminal handling at Selanu collect from the consignee.</cbc:Note>
      </cac:CollectPaymentTerms>
      <cac:DisbursementPaymentTerms>
        <cbc:Note>Island customs fees advanced by the broker and recharged to the consignee.</cbc:Note>
      </cac:DisbursementPaymentTerms>
      <cac:PrepaidPaymentTerms>
        <cbc:Note>Ocean freight and bunker surcharge prepaid by the shipper.</cbc:Note>
      </cac:PrepaidPaymentTerms>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReason>Ocean freight, 40-foot container</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">2700.00</cbc:Amount>
      </cac:FreightAllowanceCharge>
      <cac:ExtraAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReason>Bunker surcharge</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">250.00</cbc:Amount>
      </cac:ExtraAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>2</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>TH-26-19E</cbc:JourneyID>
          <cbc:RegistrationNationalityID>XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:DirectionCode>Eastbound</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode>SEA</cbc:TransportMeansTypeCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
            <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
            <cbc:RadioCallSignID>XBTH7</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>999702117</cbc:MMSIRegistrationID>
            <cbc:ShipsRequirements>Shore power at the container quay.</cbc:ShipsRequirements>
            <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
            <cbc:SegregatedBallastMeasure unitCode="TNE">2480</cbc:SegregatedBallastMeasure>
            <cbc:ShipConfigurationCode>Feeder container ship, 1,000 TEU</cbc:ShipConfigurationCode>
            <cac:RegistryCertificateDocumentReference>
              <cbc:ID>REG-XB-S-20117</cbc:ID>
            </cac:RegistryCertificateDocumentReference>
            <cac:RegistryPortLocation>
              <cbc:Name>Lumeport</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode>XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:TransshipPortLocation>
          <cbc:Name>None: a direct sailing</cbc:Name>
        </cac:TransshipPortLocation>
        <cac:AvailabilityTransportEvent>
          <cbc:OccurrenceDate>2026-05-18</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>14:00:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        </cac:AvailabilityTransportEvent>
        <cac:StorageTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:30:00</cbc:OccurrenceTime>
        </cac:StorageTransportEvent>
        <cac:AcceptanceTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:15:00</cbc:OccurrenceTime>
        </cac:AcceptanceTransportEvent>
        <cac:FreightChargeLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FreightChargeLocation>
      </cac:MainCarriageShipmentStage>
      <cac:PreCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
        <cbc:CabotageIndicator>true</cbc:CabotageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Trasvia Haulage</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID>XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode>TE</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID>UR 4160 KT</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID>UR TR 3381</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
          <cac:OwnerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Trasvia Haulage</cbc:Name>
            </cac:PartyName>
          </cac:OwnerParty>
          <cac:MeasurementDimension>
            <cbc:AttributeID>Loading length</cbc:AttributeID>
            <cbc:Measure unitCode="MTR">13.6</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:TransportMeans>
        <cac:DropoffTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:15:00</cbc:OccurrenceTime>
        </cac:DropoffTransportEvent>
      </cac:PreCarriageShipmentStage>
      <cac:OnCarriageShipmentStage>
        <cbc:ID>3</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:OnCarriageIndicator>true</cbc:OnCarriageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Nalevi Warehousing</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:WarehousingTransportEvent>
          <cbc:OccurrenceDate>2026-05-19</cbc:OccurrenceDate>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        </cac:WarehousingTransportEvent>
        <cac:ReceiptTransportEvent>
          <cbc:OccurrenceDate>2026-05-19</cbc:OccurrenceDate>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        </cac:ReceiptTransportEvent>
      </cac:OnCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode>42G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode>FCL</cbc:FullnessIndicationCode>
          <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
          <cbc:GrossWeightMeasure unitCode="KGM">3750</cbc:GrossWeightMeasure>
          <cbc:TareWeightMeasure unitCode="KGM">3750</cbc:TareWeightMeasure>
          <cbc:StowagePositionID>140282</cbc:StowagePositionID>
          <cac:TransportEquipmentSeal>
            <cbc:ID>TWL-S-0884213</cbc:ID>
            <cbc:SealIssuerTypeCode>Carrier</cbc:SealIssuerTypeCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-001</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 001 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-001</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-002</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 002 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-002</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-003</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 003 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-003</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-004</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 004 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-004</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-005</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 005 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-005</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-006</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 006 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-006</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-007</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 007 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-007</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-008</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 008 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-008</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-009</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 009 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-009</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-010</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 010 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-010</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-011</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 011 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-011</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-012</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 012 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-012</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-013</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 013 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-013</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-014</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 014 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-014</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-015</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 015 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-015</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-016</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 016 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-016</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-017</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 017 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-017</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-018</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 018 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-018</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-019</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 019 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-019</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-020</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 020 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-020</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-021</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 021 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-021</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-022</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 022 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-022</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-023</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 023 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-023</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-024</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 024 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-024</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID>LD-26-025</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode>PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="H87">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="H87">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 025 of 025</cbc:ShippingMarks>
            <cbc:TraceID>LD-26-025</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:GoodsItem>
            <cbc:ID>1</cbc:ID>
            <cbc:Description>Park benches and spare side frames</cbc:Description>
          </cac:GoodsItem>
          <cac:VerifiedGrossMass>
            <cbc:ID>VGM-26-0510</cbc:ID>
            <cbc:WeighingDate>2026-05-12</cbc:WeighingDate>
            <cbc:WeighingTime>15:30:00</cbc:WeighingTime>
            <cbc:WeighingMethodCode listID="IMO SOLAS">SM2</cbc:WeighingMethodCode>
            <cbc:WeighingDeviceID>LD-SCALE-03</cbc:WeighingDeviceID>
            <cbc:WeighingDeviceType>Platform scale</cbc:WeighingDeviceType>
            <cbc:GrossMassMeasure unitCode="KGM">3750</cbc:GrossMassMeasure>
            <cac:WeighingParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeway Distribution</cbc:Name>
              </cac:PartyName>
            </cac:WeighingParty>
            <cac:ShipperParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeway Distribution</cbc:Name>
              </cac:PartyName>
            </cac:ShipperParty>
            <cac:ResponsibleParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeway Distribution</cbc:Name>
              </cac:PartyName>
            </cac:ResponsibleParty>
            <cac:DocumentReference>
              <cbc:ID>VGM-26-0510</cbc:ID>
            </cac:DocumentReference>
          </cac:VerifiedGrossMass>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
      <cac:FirstArrivalPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
        <cbc:Name>Port of Selanu</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FirstArrivalPortLocation>
      <cac:LastExitPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Port of Lumeport</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:LastExitPortLocation>
    </cac:Consignment>
    <cac:InsurancePolicy>
      <cbc:InsuredValueAmount currencyID="XBL">59155.80</cbc:InsuredValueAmount>
      <cac:InsurerParty>
        <cbc:WebsiteURI>https://www.wavesure.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">6512</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Wavesure Cargo Insurance</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
          <cbc:StreetName>Beacon Avenue</cbc:StreetName>
          <cbc:BuildingNumber>55</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38524</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Wavesure Cargo Insurance Ltd</cbc:RegistrationName>
          <cbc:CompanyID>CO-1234521</cbc:CompanyID>
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
          <cbc:RegistrationName>Wavesure Cargo Insurance Ltd</cbc:RegistrationName>
          <cbc:CompanyID>20411507</cbc:CompanyID>
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
          <cbc:Name>Cargo claims</cbc:Name>
          <cbc:JobTitle>Client relationship manager</cbc:JobTitle>
          <cbc:Department>Client services</cbc:Department>
          <cbc:Telephone>+999 2 3852 1507</cbc:Telephone>
          <cbc:ElectronicMail>cargo@wavesure.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411507</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:InsurerParty>
    </cac:InsurancePolicy>
  </cac:Shipment>
</BillOfLading>
```
