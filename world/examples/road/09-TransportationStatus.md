# Transportation Status: Trasvia Haulage to Lumeway Distribution

*Example 9 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The carrier reports that the truck has cleared the border and gives the expected arrival time.

[The XML file](09-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:road**  
  The business process the document belongs to: the flow "Finished goods by truck across the land border (Urvania → Bayvarra)".
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TH-TS-26-0160**  
  The carrier's status report number.
- `UUID` = **bef60481-e21d-568c-918b-caeb273b9ce0**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-24**  
  The morning after collection, when the truck has crossed the border.
- `IssueTime` = **09:10:00**  
  Sent as soon as the truck was through.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Border crossing passed; customs cleared on both sides.**  
  In words.
- `Note` = **Automatic report from the sender's tracking system.**  
  How it was made.
- `ShippingOrderID` = **LD-CS-26-0152**  
  The shipper's booking it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do.
- `TransportationStatusTypeCode` = **Progress**  
  A report on the progress of the carriage.
- `TransportExecutionStatusCode` = **InProgress**  
  The carriage is under way.

### Consignment

Inside `Consignment`:

- `ID` = **LD-CS-26-0152**  
  The consignment the report is about.
- `CarrierAssignedID` = **TH-26-04471**  
  The carrier's job number.
- `Status/ConditionCode` = **InTransit**  
  The consignment is on its way.
- `Status/Description` = **All 25 pallets on board.**  
  Nothing left behind.
- `ConsigneeParty/WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/Language/ID` = **en**  
  English, the language the party does business in.
- `ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `ConsigneeParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `ConsigneeParty/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `ConsigneeParty/PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `ConsigneeParty/PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `ConsigneeParty/PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `ConsigneeParty/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/Contact/Telephone` = **+999 2 7121 0274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `CarrierParty/WebsiteURI` = **https://www.trasvia.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/IndustryClassificationCode` = **4923** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `CarrierParty/Language/Name` = **English**  
  The language's name.
- `CarrierParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `CarrierParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti**  
  Street of the postal address. identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `CarrierParty/PartyTaxScheme/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered for value added tax; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyTaxScheme/CompanyID` = **XU007337656**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered, with its legal form; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104822**  
  Number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `CarrierParty/Contact/Name` = **Planning desk**  
  The desk that handles this document; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/Contact/Telephone` = **+999 1 4160 4822**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyAuthorization/Purpose` = **International road haulage**  
  What the authority has authorized the party to do; identity of Trasvia Haulage (world/parties.json).
- `CarrierParty/PartyAuthorization/ValidityPeriod/EndDate` = **2030-06-30**  
  The authorization expires on this date.
- `CarrierParty/PartyAuthorization/Certificate/ID` = **XU-HAUL-2020-0877**  
  The number of the permit.
- `CarrierParty/PartyAuthorization/Certificate/CertificateTypeCode` = **Permit**  
  A permit issued by an authority of the party's country.
- `CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Operating permit**  
  The kind of certificate, in words.
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Trasvia Haulage (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport Event

Inside `TransportEvent`:

- `IdentificationID` = **TH-26-04471-E03**  
  The reporting party's number for this event.
- `OccurrenceDate` = **2026-03-24**  
  The day and time the truck crossed the land border.
- `OccurrenceTime` = **08:55:00**  
  The local time.
- `TransportEventTypeCode` = **BorderCrossing**  
  The kind of event, as the carriers of the world code them.
- `Description` = **Border crossing passed; customs cleared on both sides.**  
  What happened, in words.
- `CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).
- `ReportedShipment/ID` = **CL-SH-26-0154**  
  The shipment the event concerns.
- `CurrentStatus/ConditionCode` = **OnTime**  
  The carriage runs to plan.
- `CurrentStatus/ReferenceDate` = **2026-03-25**  
  The delivery the status is measured against.
- `CurrentStatus/ReferenceTime` = **10:00:00**  
  The start of the goods-in slot.
- `CurrentStatus/Description` = **In transit in Bayvarra, expected at the distribution centre on time.**  
  The status in words.
- `CurrentStatus/StatusReasonCode` = **Cleared**  
  Why: the border is behind it.
- `CurrentStatus/StatusReason` = **Customs released the goods at the border.**  
  In words.
- `CurrentStatus/SequenceID` = **3**  
  The third report on this truck: collection, departure, border.
- `CurrentStatus/Text` = **Driver resting in Marrowdale tonight under the driving-time rules.**  
  A note for the consignee.
- `CurrentStatus/IndicationIndicator` = **true**  
  The status applies: the truck is on time.
- `CurrentStatus/Percent` = **70**  
  The share of the route driven.
- `CurrentStatus/ReliabilityPercent` = **90**  
  How sure the carrier is of the arrival time.
- `CurrentStatus/DocumentationAttachment/ExternalReference/URI` = **https://www.trasvia.example/tracking/TH-26-04471/seal.jpg**  
  A photograph of the seal.
- `CurrentStatus/DocumentationAttachment/ExternalReference/MimeCode` = **image/jpeg**  
  A photograph.
- `CurrentStatus/SubStatus/ConditionCode` = **Released**  
  The customs part of the status.
- `CurrentStatus/SubStatus/Description` = **Import declaration accepted by Bayvarra's customs.**  
  In words.
- `CurrentStatus/Condition/AttributeID` = **Seal**  
  The condition checked.
- `CurrentStatus/Condition/Description` = **Intact, as checked by customs.**  
  Its state.
- `CurrentStatus/Condition/AttributeID` = **Trailer temperature**  
  Recorded by the trailer's sensor.
- `CurrentStatus/Condition/Measure` = **14** (unitCode `CEL`)  
  The temperature in the trailer.
- `CurrentStatus/Condition/Description` = **No protection needed for steel benches.**  
  Why it is only noted.
- `CurrentStatus/Condition/MinimumMeasure` = **4** (unitCode `CEL`)  
  The lowest during the night.
- `CurrentStatus/Condition/MaximumMeasure` = **18** (unitCode `CEL`)  
  The highest in the afternoon.
- `ResponsibleParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ResponsibleParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `Contact/Name` = **Planning desk**  
  Whom to call about the truck.
- `Contact/Telephone` = **+999 1 4160 4822**  
  The planners' number.
- `Location/Name` = **Land border crossing Urvania–Bayvarra**  
  The road border crossing between the customs posts of both countries.
- `Signature/ID` = **XB-CUS-SIG-0884**  
  The border customs' release stamp, as an electronic signature.
- `Signature/ValidationDate` = **2026-03-24**  
  Signed at the border.
- `Signature/SignatoryParty/PartyIdentification/ID` = **20410137** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Customs and Border Service of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.
- `Period/StartTime` = **07:30:00**  
  The truck joined the queue at the border.
- `Period/EndTime` = **08:55:00**  
  And left the customs post.

### Document Reference

Inside `DocumentReference`:

- `ID` = **TH-WB-26-0159**  
  The transport document of the consignment.

### Signature

Inside `Signature`:

- `ID` = **TH-SIG-TS-09**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Trasvia Haulage**  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at Consignment/ConsigneeParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Lumeway Distribution**  
  The same party as at Consignment/ConsigneeParty, where its full details are given; only its identifier and name are repeated.

### Updated Pickup Transport Event

Inside `UpdatedPickupTransportEvent`:

- `OccurrenceDate` = **2026-03-23**  
  The collection as it happened.
- `OccurrenceTime` = **15:05:00**  
  The local time.

### Updated Delivery Transport Event

Inside `UpdatedDeliveryTransportEvent`:

- `OccurrenceDate` = **2026-03-25**  
  The delivery as now expected.
- `OccurrenceTime` = **09:30:00**  
  The local time.

### Status Location

Inside `StatusLocation`:

- `Name` = **Trasvia Haulage**  
  Where the status was recorded.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-03-24**  
  The status holds from the report.
- `EndDate` = **2026-03-24**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:road</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TH-TS-26-0160</cbc:ID>
  <cbc:UUID>bef60481-e21d-568c-918b-caeb273b9ce0</cbc:UUID>
  <cbc:IssueDate>2026-03-24</cbc:IssueDate>
  <cbc:IssueTime>09:10:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Border crossing passed; customs cleared on both sides.</cbc:Description>
  <cbc:Note>Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>LD-CS-26-0152</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportationStatusTypeCode>Progress</cbc:TransportationStatusTypeCode>
  <cbc:TransportExecutionStatusCode>InProgress</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>LD-CS-26-0152</cbc:ID>
    <cbc:CarrierAssignedID>TH-26-04471</cbc:CarrierAssignedID>
    <cac:Status>
      <cbc:ConditionCode>InTransit</cbc:ConditionCode>
      <cbc:Description>All 25 pallets on board.</cbc:Description>
    </cac:Status>
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
        <cbc:Telephone>+999 2 7121 0274</cbc:Telephone>
        <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:ConsigneeParty>
    <cac:CarrierParty>
      <cbc:WebsiteURI>https://www.trasvia.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4923</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Trasvia Haulage</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via dei Trasporti</cbc:StreetName>
        <cbc:BuildingNumber>45</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4160</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Trasvia Haulage SRU</cbc:RegistrationName>
        <cbc:CompanyID>XU007337656</cbc:CompanyID>
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
        <cbc:RegistrationName>Trasvia Haulage SRU</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104822</cbc:CompanyID>
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
        <cbc:Name>Planning desk</cbc:Name>
        <cbc:JobTitle>Operations planner</cbc:JobTitle>
        <cbc:Department>Operations</cbc:Department>
        <cbc:Telephone>+999 1 4160 4822</cbc:Telephone>
        <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:PartyAuthorization>
        <cbc:Purpose>International road haulage</cbc:Purpose>
        <cac:ValidityPeriod>
          <cbc:EndDate>2030-06-30</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:Certificate>
          <cbc:ID>XU-HAUL-2020-0877</cbc:ID>
          <cbc:CertificateTypeCode>Permit</cbc:CertificateTypeCode>
          <cbc:CertificateType>Operating permit</cbc:CertificateType>
        </cac:Certificate>
      </cac:PartyAuthorization>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104822</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:IdentificationID>TH-26-04471-E03</cbc:IdentificationID>
    <cbc:OccurrenceDate>2026-03-24</cbc:OccurrenceDate>
    <cbc:OccurrenceTime>08:55:00</cbc:OccurrenceTime>
    <cbc:TransportEventTypeCode>BorderCrossing</cbc:TransportEventTypeCode>
    <cbc:Description>Border crossing passed; customs cleared on both sides.</cbc:Description>
    <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
    <cac:ReportedShipment>
      <cbc:ID>CL-SH-26-0154</cbc:ID>
    </cac:ReportedShipment>
    <cac:CurrentStatus>
      <cbc:ConditionCode>OnTime</cbc:ConditionCode>
      <cbc:ReferenceDate>2026-03-25</cbc:ReferenceDate>
      <cbc:ReferenceTime>10:00:00</cbc:ReferenceTime>
      <cbc:Description>In transit in Bayvarra, expected at the distribution centre on time.</cbc:Description>
      <cbc:StatusReasonCode>Cleared</cbc:StatusReasonCode>
      <cbc:StatusReason>Customs released the goods at the border.</cbc:StatusReason>
      <cbc:SequenceID>3</cbc:SequenceID>
      <cbc:Text>Driver resting in Marrowdale tonight under the driving-time rules.</cbc:Text>
      <cbc:IndicationIndicator>true</cbc:IndicationIndicator>
      <cbc:Percent>70</cbc:Percent>
      <cbc:ReliabilityPercent>90</cbc:ReliabilityPercent>
      <cac:DocumentationAttachment>
        <cac:ExternalReference>
          <cbc:URI>https://www.trasvia.example/tracking/TH-26-04471/seal.jpg</cbc:URI>
          <cbc:MimeCode>image/jpeg</cbc:MimeCode>
        </cac:ExternalReference>
      </cac:DocumentationAttachment>
      <cac:SubStatus>
        <cbc:ConditionCode>Released</cbc:ConditionCode>
        <cbc:Description>Import declaration accepted by Bayvarra's customs.</cbc:Description>
      </cac:SubStatus>
      <cac:Condition>
        <cbc:AttributeID>Seal</cbc:AttributeID>
        <cbc:Description>Intact, as checked by customs.</cbc:Description>
      </cac:Condition>
      <cac:Condition>
        <cbc:AttributeID>Trailer temperature</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">14</cbc:Measure>
        <cbc:Description>No protection needed for steel benches.</cbc:Description>
        <cbc:MinimumMeasure unitCode="CEL">4</cbc:MinimumMeasure>
        <cbc:MaximumMeasure unitCode="CEL">18</cbc:MaximumMeasure>
      </cac:Condition>
    </cac:CurrentStatus>
    <cac:ResponsibleParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Trasvia Haulage</cbc:Name>
      </cac:PartyName>
    </cac:ResponsibleParty>
    <cac:Contact>
      <cbc:Name>Planning desk</cbc:Name>
      <cbc:Telephone>+999 1 4160 4822</cbc:Telephone>
    </cac:Contact>
    <cac:Location>
      <cbc:Name>Land border crossing Urvania–Bayvarra</cbc:Name>
    </cac:Location>
    <cac:Signature>
      <cbc:ID>XB-CUS-SIG-0884</cbc:ID>
      <cbc:ValidationDate>2026-03-24</cbc:ValidationDate>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410137</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Customs and Border Service of Bayvarra</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
    <cac:Period>
      <cbc:StartTime>07:30:00</cbc:StartTime>
      <cbc:EndTime>08:55:00</cbc:EndTime>
    </cac:Period>
  </cac:TransportEvent>
  <cac:DocumentReference>
    <cbc:ID>TH-WB-26-0159</cbc:ID>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>TH-SIG-TS-09</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Trasvia Haulage</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Trasvia Haulage</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:UpdatedPickupTransportEvent>
    <cbc:OccurrenceDate>2026-03-23</cbc:OccurrenceDate>
    <cbc:OccurrenceTime>15:05:00</cbc:OccurrenceTime>
  </cac:UpdatedPickupTransportEvent>
  <cac:UpdatedDeliveryTransportEvent>
    <cbc:OccurrenceDate>2026-03-25</cbc:OccurrenceDate>
    <cbc:OccurrenceTime>09:30:00</cbc:OccurrenceTime>
  </cac:UpdatedDeliveryTransportEvent>
  <cac:StatusLocation>
    <cbc:Name>Trasvia Haulage</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-03-24</cbc:StartDate>
    <cbc:EndDate>2026-03-24</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
