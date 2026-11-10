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
- `Note` = **Automatic report from the sender's tracking system.**  
  How it was made.
- `ShippingOrderID` = **VI-CS-26-0327**  
  The shipper's booking it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do.
- `TransportExecutionStatusCode` = **InProgress**  
  The carriage is under way.

### Consignment

Inside `Consignment`:

- `ID` = **VI-CS-26-0327**  
  The consignment the report is about.
- `CarrierParty/WebsiteURI` = **https://www.ferranorail.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/IndustryClassificationCode` = **4912** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `CarrierParty/Language/Name` = **English**  
  The language's name.
- `CarrierParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `CarrierParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `CarrierParty/PostalAddress/StreetName` = **Viale della Stazione**  
  Street of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `CarrierParty/PartyTaxScheme/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyTaxScheme/CompanyID` = **XU007328060**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104685**  
  Number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
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
- `CarrierParty/Contact/Name` = **Freight desk**  
  The desk that handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Rail Cargo (world/parties.json).
- `CarrierParty/Contact/Telephone` = **+999 1 4150 4685**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Rail Cargo (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Intermodal Hub (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Ferrano Intermodal Hub**  
  The trading name; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **en**  
  English, the language the party does business in.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **English**  
  The language's name.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Via del Terminal**  
  Street of the postal address. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **59**  
  Building number of the postal address. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/PostalZone` = **4180**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/RegistrationName` = **Ferrano Intermodal Hub SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/CompanyID` = **XU007356833**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Ferrano Intermodal Hub SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **XU-R-105096**  
  Number in the Commercial register of Urvania; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Terminal control**  
  The desk that handles this document; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Intermodal Hub (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 1 4180 5096**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Intermodal Hub (world/parties.json).
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
  <cbc:Note>Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>VI-CS-26-0327</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode>InProgress</cbc:TransportExecutionStatusCode>
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
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Viale della Stazione</cbc:StreetName>
        <cbc:BuildingNumber>38</cbc:BuildingNumber>
        <cbc:CityName>Serravona</cbc:CityName>
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
        <cbc:Telephone>+999 1 4150 4685</cbc:Telephone>
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
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
          <cbc:StreetName>Via del Terminal</cbc:StreetName>
          <cbc:BuildingNumber>59</cbc:BuildingNumber>
          <cbc:CityName>Ferrano</cbc:CityName>
          <cbc:PostalZone>4180</cbc:PostalZone>
          <cbc:Region>Province of Ferrano</cbc:Region>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Ferrano Intermodal Hub SRU</cbc:RegistrationName>
          <cbc:CompanyID>XU007356833</cbc:CompanyID>
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
          <cbc:RegistrationName>Ferrano Intermodal Hub SRU</cbc:RegistrationName>
          <cbc:CompanyID>XU-R-105096</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
          <cbc:Name>Terminal control</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 4180 5096</cbc:Telephone>
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
