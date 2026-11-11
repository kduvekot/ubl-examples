# Waybill: Ferrano Rail Cargo to Valdara Industries

*Example 8 of the flow "Containers by rail under transit (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The rail consignment note goes to the transport user, now the seller.

[The XML file](08-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **FRC-WB-26-0334**  
  The consignment note number.
- `CarrierAssignedID` = **FRC-CMR-26-0325**  
  The carrier's own number for the carriage.
- `UUID` = **2af02244-330b-5e9f-85c5-1ad7dcce9c43**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **Issued**  
  The note is issued and in force.
- `IssueDate` = **2026-04-14**  
  Issued when the carrier takes over the containers.
- `IssueTime` = **13:10:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Consignment note under the road convention, the CMR**  
  The kind of transport document.
- `Description` = **Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.**  
  The carriage in words.
- `Note` = **Gurbul mizstan: dadrek, miran, sundraz.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): As the convention prescribes.
- `Note` = **Three originals: consignor, consignee, carrier.** (languageID `en`)  
  The same note in English, the working language between the countries: As the convention prescribes.
- `ShippingOrderID` = **VI-CS-26-0327**  
  The shipper's booking the carriage fulfils.
- `WaybillTypeCode` = **CMR**  
  The convention the document follows.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `AdValoremIndicator` = **false**  
  No value declared to raise the carrier's liability.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Castrano Logistics**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.ferranorail.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Rail Cargo (world/parties.json).
- `IndustryClassificationCode` = **4912** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Rail Cargo (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `PostalAddress/StreetName` = **Rumir Hekrul Zhuzkek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/StreetName` = **Viale della Stazione** (languageID `en`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/CityName` = **Serravona** (languageID `en`)  
  The town's English name, inherited from the Italian; identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Rail Cargo (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007328060**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Rail Cargo (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Rail Cargo (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104685**  
  Number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Rail Cargo (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Rail Cargo (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
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
- `Contact/Name` = **Freight desk**  
  The desk that handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/Telephone` = **+999 1 0413 44685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Rail Cargo (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Rail Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en`)  
  The town's English name, inherited from the Italian; identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `PartyLegalEntity/SecurityListing/ID` = **XU0001042505**  
  The identifier of the listed shares, in the form of an ISIN with the world's country code.
- `PartyLegalEntity/SecurityListing/Description` = **Ordinary shares of Valdara Industries**  
  What is listed.
- `PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The regulated market where the shares are listed.
- `PartyLegalEntity/SecurityListing/MarketCode` = **FSE**  
  The market's code.
- `Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `ServiceProviderParty/ID` = **5-xu-SP-8-xu**  
  The service contract between the two.
- `ServiceProviderParty/ServiceTypeCode` = **Logistics**  
  The kind of service, as a code.
- `ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **VI-SH-26-0332**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **7968** (unitCode `KGM`)  
  The gross weight of the two containers' cargo.
- `Consignment/ID` = **VI-CS-26-0327**  
  The manufacturer's consignment number.
- `Consignment/ContractedCarrierAssignedID` = **FRC-CON-2026-005/88**  
  The call-off under the framework contract.
- `Consignment/PerformingCarrierAssignedID` = **FRC-J-26-3318**  
  The rail carrier's job number.
- `Consignment/SummaryDescription` = **192 park benches in two 40-foot containers.**  
  The goods in a few words.
- `Consignment/ContainerizedIndicator` = **true**  
  Two full containers.
- `Consignment/TotalTransportHandlingUnitQuantity` = **2** (unitCode `C62`)  
  Two containers.
- `Consignment/LoadingSequenceID` = **7**  
  The consignment's turn in the loading of the train.
- `Consignment/ConsigneeParty/WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `Consignment/ConsigneeParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Upland State**  
  The state or territory, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **UL**  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `Consignment/ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
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
- `Consignment/ConsigneeParty/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 7121 474 274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/PerformingCarrierParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PerformingCarrierParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportContract/ID` = **FRC-CON-2026-005**  
  The framework contract for container slots.
- `Consignment/TransportContract/IssueDate` = **2026-01-05**  
  Signed at the start of the year.
- `Consignment/TransportContract/ContractType` = **Framework contract for container slots**  
  What it is.
- `Consignment/PrepaidPaymentTerms/Note` = **Freight prepaid by the consignor under DAP.**  
  The seller pays the carriage.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The main carriage, by rail.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **2** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 2: rail transport.
- `Consignment/MainCarriageShipmentStage/LoadingSequenceID` = **7**  
  The order the boxes go on the train: these two are the seventh lift.
- `Consignment/MainCarriageShipmentStage/SuccessiveSequenceID` = **1**  
  The first and only rail stage.
- `Consignment/MainCarriageShipmentStage/Instructions` = **Shunt to the Lumeway siding on arrival in Marrowdale.**  
  What the railway must do.
- `Consignment/MainCarriageShipmentStage/DemurrageInstructions` = **Free time five days at the siding, then demurrage per container day.**  
  What waiting costs.
- `Consignment/MainCarriageShipmentStage/CrewQuantity` = **2** (unitCode `C62`)  
  A driver and a train manager.
- `Consignment/MainCarriageShipmentStage/PassengerQuantity` = **0** (unitCode `C62`)  
  A freight train carries no passengers.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **CT 4471**  
  The number of the container train in the hub's timetable.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU**  
  The country the means of transport is registered in.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **Westbound**  
  The direction of the journey, as the carrier codes its services.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **RAIL**  
  The carrier's code for the kind of means: container train ferrano–marrowdale; the fleet of Ferrano Rail Cargo (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train number; the fleet of Ferrano Rail Cargo (world/parties.json).
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The timetable departure from the hub.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **06:45:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The timetable arrival in Marrowdale.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **10:30:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceDate` = **2026-04-14**  
  Planned passage of the border station.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceTime` = **13:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The train left the hub.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/OccurrenceTime` = **06:52:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  Where.
- `Consignment/MainCarriageShipmentStage/ActualWaypointTransportEvent/OccurrenceDate` = **2026-04-14**  
  The train passed the border station.
- `Consignment/MainCarriageShipmentStage/ActualWaypointTransportEvent/OccurrenceTime` = **13:20:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The departure as expected that morning.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceTime` = **06:50:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The arrival as expected.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceTime` = **10:40:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRCU1044171** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **VI-CS-26-0327**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderTypeCode` = **Carrier**  
  The rail carrier provides the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerTypeCode` = **Carrier**  
  And owns it.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1**  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/DispositionCode` = **Loaded**  
  Loaded with cargo.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL**  
  A full container load for one consignee.
- `Consignment/TransportHandlingUnit/TransportEquipment/Information` = **Return empty to the Ferrano hub within five days.**  
  What happens to the box afterwards.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The container goes back to its owner.
- `Consignment/TransportHandlingUnit/TransportEquipment/LegalStatusIndicator` = **false**  
  Not under a customs container convention; the goods travel under transit.
- `Consignment/TransportHandlingUnit/TransportEquipment/Characteristics` = **Steel, high cube, wooden floor.**  
  What kind of box it is.
- `Consignment/TransportHandlingUnit/TransportEquipment/DamageRemarks` = **Small dent in the left side panel, noted at pick-up; no effect on the cargo.**  
  Damage noted at the hub, so it is not blamed on this carriage.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **40-foot high cube container**  
  The container in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/SpecialTransportRequirements` = **Load with the doors to the rear of the wagon.**  
  How it rides.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7884** (unitCode `KGM`)  
  Half the benches and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossVolumeMeasure` = **76.3** (unitCode `MTQ`)  
  The inside volume of a 40-foot high cube.
- `Consignment/TransportHandlingUnit/TransportEquipment/TrackingDeviceCode` = **GPS**  
  The box carries a satellite tracker.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **false**  
  It needs no power: not a reefer.
- `Consignment/TransportHandlingUnit/TransportEquipment/TraceID` = **TRK-FRCU1044171**  
  The tracker's number.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **XU-FRC 4521 0042 / A**  
  The wagon and the slot on it the box rides in.
- `Consignment/TransportHandlingUnit/TransportEquipment/MeasurementDimension/AttributeID` = **Length**  
  The outside length.
- `Consignment/TransportHandlingUnit/TransportEquipment/MeasurementDimension/Measure` = **12192** (unitCode `MMT`)  
  Forty feet.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-VI-30411**  
  The number of the bolt seal on the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **Shipper**  
  The seal was issued by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/Condition` = **Intact**  
  As found at the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **Applied**  
  The seal is in place.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  And put on by the shipper when it packed the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingProofParty/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingProofParty/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OperatingParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OperatingParty/PartyName/Name` = **Ferrano Intermodal Hub**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/Name` = **Ferrano**  
  Packed at the 3PL's warehouse in Ferrano.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/Address/Country/IdentificationCode` = **XU**  
  The country the place is in.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/Name` = **Marrowdale**  
  Unpacked at the distributor's siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/Address/Country/IdentificationCode` = **XB**  
  The country the place is in.
- `Consignment/TransportHandlingUnit/TransportEquipment/StorageLocation/Name` = **Ferrano Intermodal Hub, stack C**  
  Where the box waited for the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceDate` = **2026-04-12**  
  The empty box was delivered to the warehouse for packing.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceTime` = **08:00:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  Planned arrival at the siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceTime` = **11:00:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  Collected packed from the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceTime` = **15:00:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceDate` = **2026-04-13**  
  Stacked at the hub overnight.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceTime` = **18:30:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceDate` = **2026-04-14**  
  Lifted onto the wagon.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceTime` = **05:40:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/ApplicableTransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train.
- `Consignment/TransportHandlingUnit/TransportEquipment/ApplicableTransportMeans/RailTransport/RailCarID` = **XU-FRC 4521 0042**  
  The container wagon it rides on.
- `Consignment/TransportHandlingUnit/TransportEquipment/HaulageTradingTerms/Information` = **Carrier haulage: the rail carrier brings the box to the warehouse and back.**  
  Who moves the empty box.
- `Consignment/TransportHandlingUnit/TransportEquipment/HaulageTradingTerms/Reference` = **FRC-HT-2026**  
  The carrier's haulage terms.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The freight for this box.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/AllowanceChargeReason` = **Rail freight per container**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/Amount` = **54600** (currencyID `XUF`)  
  The price of one container slot (world/items.json).
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/LatestDeliveryDate` = **2026-04-16**  
  At the latest.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/Name` = **Rail siding of Lumeway Distribution, Marrowdale**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupDate` = **2026-04-13**  
  Collected.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupTime` = **15:00:00**  
  At three.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/Name` = **Castrano Logistics warehouse, Ferrano**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/ActualDespatchDate` = **2026-04-14**  
  The train left the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/ActualDespatchTime` = **06:50:00**  
  Ten to seven.
- `Consignment/TransportHandlingUnit/TransportEquipment/ShipmentDocumentReference/ID` = **FRC-WB-26-0334**  
  The rail consignment note.
- `Consignment/TransportHandlingUnit/TransportEquipment/ContainedInTransportEquipment/ID` = **XU-FRC 4521 0042**  
  The container wagon the box rides on.
- `Consignment/TransportHandlingUnit/TransportEquipment/ContainedInTransportEquipment/TransportEquipmentTypeCode` = **RR** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code RR: rail car.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/ID` = **VI-TD-26-0331**  
  The transit declaration the box travels under.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyName/Name` = **Customs Administration of Urvania**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/EnergySourceTypeCode` = **Electricity**  
  The train runs on electricity.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **610** (unitCode `KWH`)  
  This box's share of the train's energy, by weight.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRCU1044187** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **VI-CS-26-0327**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1**  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL**  
  A full container load for one consignee.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7884** (unitCode `KGM`)  
  Half the benches and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-VI-30412**  
  The number of the bolt seal on the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **Shipper**  
  The seal was issued by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/Condition` = **Intact**  
  As found at the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **Applied**  
  The seal is in place.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  And put on by the shipper when it packed the container.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/ID` = **VI-TD-26-0331**  
  The transit declaration the box travels under.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyName/Name` = **Customs Administration of Urvania**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/EnergySourceTypeCode` = **Electricity**  
  The train runs on electricity.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **610** (unitCode `KWH`)  
  This box's share of the train's energy, by weight.
- `Consignment/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2e**  
  Greenhouse gases of the carriage, as CO2 equivalent.
- `Consignment/EnvironmentalEmission/ValueMeasure` = **410** (unitCode `KGM`)  
  For the two containers over the route.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **Calculated**  
  From the electric train's energy use.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementFromLocation/Name` = **Ferrano Intermodal Hub**  
  From.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/Name` = **Marrowdale**  
  To.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/EmissionCalculationLocation/Name` = **Ferrano Rail Cargo, energy office**  
  Where the figure was calculated.

### Document Reference

Inside `DocumentReference`:

- `ID` = **FRC-TEP-26-0328**  
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
- `Party/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Ferrano Intermodal Hub**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The electronic copy.
- `DocumentTypeCode` = **Copy**  
  A copy.
- `DistributionTypeCode` = **Electronic**  
  Sent as this UBL document.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FRC-SIG-FRC-WB-26-0334**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:rail</cbc:ProfileID>
  <cbc:ProfileExecutionID>RAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FRC-WB-26-0334</cbc:ID>
  <cbc:CarrierAssignedID>FRC-CMR-26-0325</cbc:CarrierAssignedID>
  <cbc:UUID>2af02244-330b-5e9f-85c5-1ad7dcce9c43</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode>Issued</cbc:StatusCode>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>13:10:00</cbc:IssueTime>
  <cbc:Name>Consignment note under the road convention, the CMR</cbc:Name>
  <cbc:Description>Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.</cbc:Description>
  <cbc:Note languageID="qau">Gurbul mizstan: dadrek, miran, sundraz.</cbc:Note>
  <cbc:Note languageID="en">Three originals: consignor, consignee, carrier.</cbc:Note>
  <cbc:ShippingOrderID>VI-CS-26-0327</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode>CMR</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Castrano Logistics</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.ferranorail.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4912</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Rumir Hekrul Zhuzkek</cbc:StreetName>
      <cbc:StreetName languageID="en">Viale della Stazione</cbc:StreetName>
      <cbc:BuildingNumber>38</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
      <cbc:CityName languageID="en">Serravona</cbc:CityName>
      <cbc:PostalZone>4150</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Ferrano Rail Cargo SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU007328060</cbc:CompanyID>
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
      <cbc:RegistrationName>Ferrano Rail Cargo SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104685</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Serravona</cbc:CityName>
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
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
      <cbc:StreetName languageID="en">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU007299291</cbc:CompanyID>
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
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
      <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cac:SecurityListing>
        <cbc:ID>XU0001042505</cbc:ID>
        <cbc:Description>Ordinary shares of Valdara Industries</cbc:Description>
        <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
        <cbc:MarketCode>FSE</cbc:MarketCode>
      </cac:SecurityListing>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode>AL</cbc:ChannelCode>
        <cbc:Value>+999 1 344 474 4274</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
    <cac:ServiceProviderParty>
      <cbc:ID>5-xu-SP-8-xu</cbc:ID>
      <cbc:ServiceTypeCode>Logistics</cbc:ServiceTypeCode>
      <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Castrano Logistics</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SellerContact>
        <cbc:Name>Key account desk</cbc:Name>
      </cac:SellerContact>
    </cac:ServiceProviderParty>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>VI-SH-26-0332</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">7968</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>VI-CS-26-0327</cbc:ID>
      <cbc:ContractedCarrierAssignedID>FRC-CON-2026-005/88</cbc:ContractedCarrierAssignedID>
      <cbc:PerformingCarrierAssignedID>FRC-J-26-3318</cbc:PerformingCarrierAssignedID>
      <cbc:SummaryDescription>192 park benches in two 40-foot containers.</cbc:SummaryDescription>
      <cbc:ContainerizedIndicator>true</cbc:ContainerizedIndicator>
      <cbc:TotalTransportHandlingUnitQuantity unitCode="C62">2</cbc:TotalTransportHandlingUnitQuantity>
      <cbc:LoadingSequenceID>7</cbc:LoadingSequenceID>
      <cac:ConsigneeParty>
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
          <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
          <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
          <cbc:Telephone>+999 2 7121 474 274</cbc:Telephone>
          <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
      <cac:PerformingCarrierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Rail Cargo</cbc:Name>
        </cac:PartyName>
      </cac:PerformingCarrierParty>
      <cac:TransportContract>
        <cbc:ID>FRC-CON-2026-005</cbc:ID>
        <cbc:IssueDate>2026-01-05</cbc:IssueDate>
        <cbc:ContractType>Framework contract for container slots</cbc:ContractType>
      </cac:TransportContract>
      <cac:PrepaidPaymentTerms>
        <cbc:Note>Freight prepaid by the consignor under DAP.</cbc:Note>
      </cac:PrepaidPaymentTerms>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">2</cbc:TransportModeCode>
        <cbc:LoadingSequenceID>7</cbc:LoadingSequenceID>
        <cbc:SuccessiveSequenceID>1</cbc:SuccessiveSequenceID>
        <cbc:Instructions>Shunt to the Lumeway siding on arrival in Marrowdale.</cbc:Instructions>
        <cbc:DemurrageInstructions>Free time five days at the siding, then demurrage per container day.</cbc:DemurrageInstructions>
        <cbc:CrewQuantity unitCode="C62">2</cbc:CrewQuantity>
        <cbc:PassengerQuantity unitCode="C62">0</cbc:PassengerQuantity>
        <cac:TransportMeans>
          <cbc:JourneyID>CT 4471</cbc:JourneyID>
          <cbc:RegistrationNationalityID>XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode>Westbound</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode>RAIL</cbc:TransportMeansTypeCode>
          <cac:RailTransport>
            <cbc:TrainID>FRC 4417</cbc:TrainID>
          </cac:RailTransport>
        </cac:TransportMeans>
        <cac:PlannedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:45:00</cbc:OccurrenceTime>
        </cac:PlannedDepartureTransportEvent>
        <cac:PlannedArrivalTransportEvent>
          <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:30:00</cbc:OccurrenceTime>
        </cac:PlannedArrivalTransportEvent>
        <cac:PlannedWaypointTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:00:00</cbc:OccurrenceTime>
        </cac:PlannedWaypointTransportEvent>
        <cac:ActualDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:52:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          </cac:Location>
        </cac:ActualDepartureTransportEvent>
        <cac:ActualWaypointTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:20:00</cbc:OccurrenceTime>
        </cac:ActualWaypointTransportEvent>
        <cac:EstimatedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:50:00</cbc:OccurrenceTime>
        </cac:EstimatedDepartureTransportEvent>
        <cac:EstimatedArrivalTransportEvent>
          <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:40:00</cbc:OccurrenceTime>
        </cac:EstimatedArrivalTransportEvent>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRCU1044171</cbc:ID>
          <cbc:ReferencedConsignmentID>VI-CS-26-0327</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:ProviderTypeCode>Carrier</cbc:ProviderTypeCode>
          <cbc:OwnerTypeCode>Carrier</cbc:OwnerTypeCode>
          <cbc:SizeTypeCode>45G1</cbc:SizeTypeCode>
          <cbc:DispositionCode>Loaded</cbc:DispositionCode>
          <cbc:FullnessIndicationCode>FCL</cbc:FullnessIndicationCode>
          <cbc:Information>Return empty to the Ferrano hub within five days.</cbc:Information>
          <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
          <cbc:LegalStatusIndicator>false</cbc:LegalStatusIndicator>
          <cbc:Characteristics>Steel, high cube, wooden floor.</cbc:Characteristics>
          <cbc:DamageRemarks>Small dent in the left side panel, noted at pick-up; no effect on the cargo.</cbc:DamageRemarks>
          <cbc:Description>40-foot high cube container</cbc:Description>
          <cbc:SpecialTransportRequirements>Load with the doors to the rear of the wagon.</cbc:SpecialTransportRequirements>
          <cbc:GrossWeightMeasure unitCode="KGM">7884</cbc:GrossWeightMeasure>
          <cbc:GrossVolumeMeasure unitCode="MTQ">76.3</cbc:GrossVolumeMeasure>
          <cbc:TrackingDeviceCode>GPS</cbc:TrackingDeviceCode>
          <cbc:PowerIndicator>false</cbc:PowerIndicator>
          <cbc:TraceID>TRK-FRCU1044171</cbc:TraceID>
          <cbc:StowagePositionID>XU-FRC 4521 0042 / A</cbc:StowagePositionID>
          <cac:MeasurementDimension>
            <cbc:AttributeID>Length</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">12192</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30411</cbc:ID>
            <cbc:SealIssuerTypeCode>Shipper</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode>Applied</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:ProviderParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Rail Cargo</cbc:Name>
            </cac:PartyName>
          </cac:ProviderParty>
          <cac:LoadingProofParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Castrano Logistics</cbc:Name>
            </cac:PartyName>
          </cac:LoadingProofParty>
          <cac:OwnerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Rail Cargo</cbc:Name>
            </cac:PartyName>
          </cac:OwnerParty>
          <cac:OperatingParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
            </cac:PartyName>
          </cac:OperatingParty>
          <cac:LoadingLocation>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode>XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:LoadingLocation>
          <cac:UnloadingLocation>
            <cbc:ID schemeID="UN/LOCODE">XBMRW</cbc:ID>
            <cbc:Name>Marrowdale</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode>XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:UnloadingLocation>
          <cac:StorageLocation>
            <cbc:Name>Ferrano Intermodal Hub, stack C</cbc:Name>
          </cac:StorageLocation>
          <cac:PositioningTransportEvent>
            <cbc:OccurrenceDate>2026-04-12</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>08:00:00</cbc:OccurrenceTime>
          </cac:PositioningTransportEvent>
          <cac:DeliveryTransportEvent>
            <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>11:00:00</cbc:OccurrenceTime>
            <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          </cac:DeliveryTransportEvent>
          <cac:PickupTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>15:00:00</cbc:OccurrenceTime>
          </cac:PickupTransportEvent>
          <cac:HandlingTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>18:30:00</cbc:OccurrenceTime>
          </cac:HandlingTransportEvent>
          <cac:LoadingTransportEvent>
            <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>05:40:00</cbc:OccurrenceTime>
          </cac:LoadingTransportEvent>
          <cac:ApplicableTransportMeans>
            <cac:RailTransport>
              <cbc:TrainID>FRC 4417</cbc:TrainID>
              <cbc:RailCarID>XU-FRC 4521 0042</cbc:RailCarID>
            </cac:RailTransport>
          </cac:ApplicableTransportMeans>
          <cac:HaulageTradingTerms>
            <cbc:Information>Carrier haulage: the rail carrier brings the box to the warehouse and back.</cbc:Information>
            <cbc:Reference>FRC-HT-2026</cbc:Reference>
          </cac:HaulageTradingTerms>
          <cac:FreightAllowanceCharge>
            <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReason>Rail freight per container</cbc:AllowanceChargeReason>
            <cbc:Amount currencyID="XUF">54600</cbc:Amount>
          </cac:FreightAllowanceCharge>
          <cac:Delivery>
            <cbc:LatestDeliveryDate>2026-04-16</cbc:LatestDeliveryDate>
            <cac:DeliveryLocation>
              <cbc:Name>Rail siding of Lumeway Distribution, Marrowdale</cbc:Name>
            </cac:DeliveryLocation>
          </cac:Delivery>
          <cac:Pickup>
            <cbc:ActualPickupDate>2026-04-13</cbc:ActualPickupDate>
            <cbc:ActualPickupTime>15:00:00</cbc:ActualPickupTime>
            <cac:PickupLocation>
              <cbc:Name>Castrano Logistics warehouse, Ferrano</cbc:Name>
            </cac:PickupLocation>
          </cac:Pickup>
          <cac:Despatch>
            <cbc:ActualDespatchDate>2026-04-14</cbc:ActualDespatchDate>
            <cbc:ActualDespatchTime>06:50:00</cbc:ActualDespatchTime>
          </cac:Despatch>
          <cac:ShipmentDocumentReference>
            <cbc:ID>FRC-WB-26-0334</cbc:ID>
          </cac:ShipmentDocumentReference>
          <cac:ContainedInTransportEquipment>
            <cbc:ID>XU-FRC 4521 0042</cbc:ID>
            <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">RR</cbc:TransportEquipmentTypeCode>
          </cac:ContainedInTransportEquipment>
        </cac:TransportEquipment>
        <cac:CustomsDeclaration>
          <cbc:ID>VI-TD-26-0331</cbc:ID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Customs Administration of Urvania</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:CustomsDeclaration>
        <cac:EnergyConsumptionAllocation>
          <cbc:EnergySourceTypeCode>Electricity</cbc:EnergySourceTypeCode>
          <cbc:AllocatedEnergyMeasure unitCode="KWH">610</cbc:AllocatedEnergyMeasure>
        </cac:EnergyConsumptionAllocation>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRCU1044187</cbc:ID>
          <cbc:ReferencedConsignmentID>VI-CS-26-0327</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode>45G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode>FCL</cbc:FullnessIndicationCode>
          <cbc:GrossWeightMeasure unitCode="KGM">7884</cbc:GrossWeightMeasure>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30412</cbc:ID>
            <cbc:SealIssuerTypeCode>Shipper</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode>Applied</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
        </cac:TransportEquipment>
        <cac:CustomsDeclaration>
          <cbc:ID>VI-TD-26-0331</cbc:ID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Customs Administration of Urvania</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:CustomsDeclaration>
        <cac:EnergyConsumptionAllocation>
          <cbc:EnergySourceTypeCode>Electricity</cbc:EnergySourceTypeCode>
          <cbc:AllocatedEnergyMeasure unitCode="KWH">610</cbc:AllocatedEnergyMeasure>
        </cac:EnergyConsumptionAllocation>
      </cac:TransportHandlingUnit>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode>CO2e</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">410</cbc:ValueMeasure>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode>Calculated</cbc:CalculationMethodCode>
          <cac:MeasurementFromLocation>
            <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          </cac:MeasurementFromLocation>
          <cac:MeasurementToLocation>
            <cbc:Name>Marrowdale</cbc:Name>
          </cac:MeasurementToLocation>
          <cac:EmissionCalculationLocation>
            <cbc:Name>Ferrano Rail Cargo, energy office</cbc:Name>
          </cac:EmissionCalculationLocation>
        </cac:EmissionCalculationMethod>
      </cac:EnvironmentalEmission>
    </cac:Consignment>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>FRC-TEP-26-0328</cbc:ID>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode>Original</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode>Paper</cbc:DistributionTypeCode>
    <cbc:DistributionType>With the goods</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode>Copy</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode>Electronic</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FRC-SIG-FRC-WB-26-0334</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
