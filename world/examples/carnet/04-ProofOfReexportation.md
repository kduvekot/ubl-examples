# Proof of Reexportation: Ferrano Chamber of Commerce to Selanu Chamber of Commerce

*Example 4 of the flow "Samples to a trade fair on the island (temporary export)" · [Proof of Reexportation in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PROOF-OF-REEXPORTATION-SCHEMA)*

Urvania's chamber proves the samples were re-exported: they came home through Urvania's customs.

[The XML file](04-ProofOfReexportation.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:carnet**  
  The business process the document belongs to: the flow "Samples to a trade fair on the island (temporary export)".
- `ProfileExecutionID` = **CARNET-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FCC-DOC-26-0728**  
  The sender's number for this document.
- `UUID` = **a5be84f0-33dc-58b3-97e4-10dea98880ab**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-08-28**  
  Urvania's chamber answers with the proof.
- `IssueTime` = **13:19:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **The samples came home on the date stamped.**  
  The proof.
- `VersionID` = **1**  
  The first version.

### Exporting Customs Party

Inside `ExportingCustomsParty`:

- `IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Customs Administration of Urvania (world/parties.json).
- `PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; identity of Customs Administration of Urvania (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Postal**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/StreetName` = **Valico di Confine**  
  Street of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered for value added tax; identity of Customs Administration of Urvania (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007385602**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Customs Administration of Urvania (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered, with its legal form; identity of Customs Administration of Urvania (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-105507**  
  Number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json).
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
- `Contact/Name` = **Border office**  
  The desk that handles this document; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telephone` = **+999 1 4120 5507**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telefax` = **+999 1 4180 0018**  
  The customs office still lists a fax number; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/ElectronicMail` = **border@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Customs Administration of Urvania (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs Administration of Urvania (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importing Guarantor Party

Inside `ImportingGuarantorParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Chamber of Commerce (world/parties.json).
- `PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Chamber of Commerce**  
  The trading name; identity of Selanu Chamber of Commerce (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/BuildingNumber` = **30**  
  Building number of the postal address. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Selanu Chamber of Commerce (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42133**  
  Number in the Island companies register; identity of Selanu Chamber of Commerce (world/parties.json).
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
- `Contact/Name` = **Carnet office**  
  The desk that handles this document; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Telephone` = **+999 3 3000 2133**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/ElectronicMail` = **carnet@chamber-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Chamber of Commerce (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42133** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Exporting Guarantor Party

Inside `ExportingGuarantorParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; identity of Ferrano Chamber of Commerce (world/parties.json).
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
- `PostalAddress/StreetName` = **Piazza del Mercato**  
  Street of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered for value added tax; identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007376017**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-105370**  
  Number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json).
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
- `Contact/Name` = **Certificates office**  
  The desk that handles this document; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/Telephone` = **+999 1 4110 5370**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Chamber of Commerce (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Goods Item Passport Counterfoil

Inside `GoodsItemPassportCounterfoil`:

- `ID` = **REIMP-1**  
  The re-importation counterfoil, stamped by Urvania's customs when the samples came home.

### Reexportation Evidence

Inside `ReexportationEvidence`:

- `ID` = **REIMP-1**  
  The evidence is the re-importation counterfoil itself.
- `Description` = **Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.**  
  What the evidence shows.

### Goods Item Passport Attachment

Inside `GoodsItemPassportAttachment`:

- `EmbeddedDocument` = **Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.**  
  The counterfoil, as clear text.
- `ExternalReference/URI` = **https://www.ferrano-chamber.example/ata/carnet-scan.pdf**  
  A scan of the stamped counterfoil.
- `ExternalReference/MimeCode` = **application/pdf**  
  A PDF.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **XU-CUS-REIMP-26-0044**  
  Urvania's customs' re-import record.

### Signature

Inside `Signature`:

- `ID` = **FCC-SIG-26-POR**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ProofOfReexportation xmlns="urn:oasis:names:specification:ubl:schema:xsd:ProofOfReexportation-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:carnet</cbc:ProfileID>
  <cbc:ProfileExecutionID>CARNET-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FCC-DOC-26-0728</cbc:ID>
  <cbc:UUID>a5be84f0-33dc-58b3-97e4-10dea98880ab</cbc:UUID>
  <cbc:IssueDate>2026-08-28</cbc:IssueDate>
  <cbc:IssueTime>13:19:00</cbc:IssueTime>
  <cbc:Note>The samples came home on the date stamped.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ExportingCustomsParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Customs Administration of Urvania</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Postal</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:Postbox>PB 18</cbc:Postbox>
      <cbc:StreetName>Valico di Confine</cbc:StreetName>
      <cbc:BuildingNumber>22</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Customs Administration of Urvania</cbc:RegistrationName>
      <cbc:CompanyID>XU007385602</cbc:CompanyID>
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
      <cbc:RegistrationName>Customs Administration of Urvania</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-105507</cbc:CompanyID>
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
      <cbc:Name>Border office</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 1 4120 5507</cbc:Telephone>
      <cbc:Telefax>+999 1 4180 0018</cbc:Telefax>
      <cbc:ElectronicMail>border@customs-xu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105507</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExportingCustomsParty>
  <cac:ImportingGuarantorParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
      <cbc:StreetName>Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>30</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Selanu Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID>IC42133</cbc:CompanyID>
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
      <cbc:Name>Carnet office</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 3 3000 2133</cbc:Telephone>
      <cbc:ElectronicMail>carnet@chamber-selanu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42133</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImportingGuarantorParty>
  <cac:ExportingGuarantorParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName>Piazza del Mercato</cbc:StreetName>
      <cbc:BuildingNumber>15</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4110</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID>XU007376017</cbc:CompanyID>
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
      <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-105370</cbc:CompanyID>
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
      <cbc:Name>Certificates office</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 1 4110 5370</cbc:Telephone>
      <cbc:ElectronicMail>certificates@camera-ferrano.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105370</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExportingGuarantorParty>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>REIMP-1</cbc:ID>
  </cac:GoodsItemPassportCounterfoil>
  <cac:ReexportationEvidence>
    <cbc:ID>REIMP-1</cbc:ID>
    <cbc:Description>Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.</cbc:Description>
  </cac:ReexportationEvidence>
  <cac:GoodsItemPassportAttachment>
    <cbc:EmbeddedDocument>Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.</cbc:EmbeddedDocument>
    <cac:ExternalReference>
      <cbc:URI>https://www.ferrano-chamber.example/ata/carnet-scan.pdf</cbc:URI>
      <cbc:MimeCode>application/pdf</cbc:MimeCode>
    </cac:ExternalReference>
  </cac:GoodsItemPassportAttachment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>XU-CUS-REIMP-26-0044</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>FCC-SIG-26-POR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ProofOfReexportation>
```
