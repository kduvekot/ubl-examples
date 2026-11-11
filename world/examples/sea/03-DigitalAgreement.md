# Digital Agreement: Lumeway Distribution to Velumi Trading

*Example 3 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Digital Agreement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DIGITAL-AGREEMENT-SCHEMA)*

Before trading, the two parties join the multilateral digital agreement that fixes which UBL processes they use.

[The XML file](03-DigitalAgreement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:sea**  
  The business process the document belongs to: the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-DAG-26-0125**  
  The agreement's number.
- `UUID` = **1992d68e-5c04-58e5-9789-3ddfb5e9b203**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Signed before the first order.
- `IssueTime` = **12:59:00**  
  The time the sender's system issued the document, in the sender's local time.
- `AgreementTypeCode` = **Bilateral**  
  An agreement between two parties.
- `VersionID` = **1.0**  
  The first version of the agreement.
- `PreviousVersionID` = **0.9**  
  The draft both sides commented on.
- `RequiredResponseMessageLevelCode` = **Business**  
  A business response is required for every document.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-DA-1**  
  The distributor's signature as governor.
- `ReasonCode` = **Approval**  
  The signer approves the document.
- `Note` = **Signed with the company's seal certificate.**  
  How.
- `ValidationDate` = **2026-05-05**  
  Checked on receipt.
- `ValidationTime` = **09:05:00**  
  At that time.
- `ValidatorID` = **LTAC-VALIDATOR**  
  The trade accord council's validation service.
- `CanonicalizationMethod` = **http://www.w3.org/2006/12/xml-c14n11**  
  Canonical XML 1.1.
- `SignatureMethod` = **http://www.w3.org/2001/04/xmldsig-more#rsa-sha256**  
  RSA with SHA-256.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalSignatureAttachment/EmbeddedDocumentBinaryObject` = **U2lnbmF0dXJlIHZhbHVlIG9mIExELVNJRy0yNi1EQS0xLCBzaG9ydGVuZWQgZm9yIHRoZSBleGFtcGxlIHdvcmxkLg==** (mimeCode `application/pkcs7-signature`)  
  The signature value, Base64-encoded.
- `OriginalDocumentReference/ID` = **LD-DOC-26-DA-1**  
  The document as signed.

### Governor Party

Inside `GovernorParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Trade Accord Council (world/parties.json).
- `PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Trade Accord Council (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Trade Accord Council**  
  The trading name; identity of Lumeport Trade Accord Council (world/parties.json).
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
- `PostalAddress/StreetName` = **Exchange Street**  
  Street of the postal address. identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/BuildingNumber` = **34**  
  Building number of the postal address. identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/PostalZone` = **38521**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Lumeport Trade Accord Council**  
  The name under which the party is registered, with its legal form; identity of Lumeport Trade Accord Council (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411096**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Trade Accord Council (world/parties.json).
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
- `Contact/Name` = **Secretariat**  
  The desk that handles this document; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/Telephone` = **+999 2 3852 1096**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/ElectronicMail` = **secretariat@tradeaccord.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Trade Accord Council (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411096** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Trade Accord Council (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Participant Party

Inside `ParticipantParty`:

- `InitiatingPartyIndicator` = **true**  
  The distributor proposed joining the agreement.
- `PrivatePartyIndicator` = **true**  
  A private company.
- `PublicPartyIndicator` = **false**  
  Not a public body.
- `ServiceProviderPartyIndicator` = **false**  
  It exchanges its own documents; it is not a service provider.
- `Party/WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `Party/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 0274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `LegalContact/Name` = **Legal department**  
  For legal notices under the agreement.
- `TechnicalContact/Name` = **Integration desk**  
  For the technical connection.
- `SupportContact/Name` = **Service desk**  
  For day-to-day questions.
- `CommercialContact/Name` = **Sales office**  
  For the trade itself.
- `InitiatingPartyIndicator` = **false**  
  The trader accepted the proposal.
- `PrivatePartyIndicator` = **true**  
  A private company.
- `PublicPartyIndicator` = **false**  
  Not a public body.
- `ServiceProviderPartyIndicator` = **false**  
  It exchanges its own documents; it is not a service provider.
- `Party/WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `Party/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Party/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Party/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `LegalContact/Name` = **Legal department**  
  For legal notices under the agreement.
- `TechnicalContact/Name` = **Integration desk**  
  For the technical connection.
- `SupportContact/Name` = **Service desk**  
  For day-to-day questions.
- `CommercialContact/Name` = **Purchasing**  
  For the trade itself.

### Agreement Country

Inside `AgreementCountry`:

- `IdentificationCode` = **XB**  
  Governed by Bayvarra's law.

### Required Certification Document Reference

Inside `RequiredCertificationDocumentReference`:

- `ID` = **LD-EDI-TERMS-1.0**  
  The terms both sides must certify.
- `UUID` = **ed76dcbb-efca-5239-9195-cf2d240a09d4**  
  Its UUID.
- `IssueDate` = **2026-05-05**  
  Its issue date.
- `IssueTime` = **12:00:00**  
  And time.
- `DocumentTypeCode` = **Terms**  
  The kind of document.
- `XPath` = **/DigitalAgreement/DigitalAgreementTerms**  
  The part of this document the reference explains.
- `ReferencedDocumentInternalAddress` = **section-2**  
  The section of the referenced document meant.
- `LanguageID` = **en**  
  In English.
- `LocaleCode` = **EN**  
  The locale, as an ISO 639 code of UBL's language code list.
- `VersionID` = **1.0**  
  The version referred to.
- `DocumentStatusCode` = **Confirmed**  
  The version both sides confirmed.
- `DocumentDescription` = **The terms of the digital trade agreement.**  
  What it is.
- `Attachment/EmbeddedDocumentBinaryObject` = **VGVybXMgb2YgdGhlIGRpZ2l0YWwgdHJhZGUgYWdyZWVtZW50IG9mIHRoZSB3b3JsZCwgdmVyc2lvbiAxLjAu** (mimeCode `text/plain`)  
  A short text, Base64-encoded.
- `Attachment/FileName` = **terms.txt**  
  The file's name.
- `Attachment/ExternalReference/URI` = **https://www.lumeway.example/edi/terms-1.0.pdf**  
  The full text.
- `Attachment/ExternalReference/DocumentHash` = **9f2c4e1ab37d5c8e0f6a2b4d8c1e3f5a7b9d0c2e4f6a8b1c3d5e7f9a0b2c4d6e**  
  The SHA-256 hash of the full text, to check it is unchanged.
- `Attachment/ExternalReference/HashAlgorithmMethod` = **http://www.w3.org/2001/04/xmlenc#sha256**  
  SHA-256.
- `Attachment/ExternalReference/ExpiryDate` = **2027-05-04**  
  The link works for a year.
- `Attachment/ExternalReference/ExpiryTime` = **23:59:00**  
  Until the end of that day.
- `Attachment/ExternalReference/MimeCode` = **application/pdf**  
  A PDF.
- `Attachment/ExternalReference/FormatCode` = **PDF/A-3**  
  An archivable PDF.
- `Attachment/ExternalReference/EncodingCode` = **Binary**  
  Not encoded.
- `Attachment/ExternalReference/CharacterSetCode` = **UTF-8**  
  The character set of its text.
- `Attachment/ExternalReference/FileName` = **terms-1.0.pdf**  
  The file's name.
- `Attachment/ExternalReference/Description` = **The full terms.**  
  What it holds.
- `ValidityPeriod/StartDate` = **2026-05-05**  
  In force from signing.
- `ValidityPeriod/EndDate` = **2027-05-05**  
  For a year.
- `ResultOfVerification/ValidatorID` = **LTAC-VALIDATOR**  
  The council's validation service.
- `ResultOfVerification/ValidationResultCode` = **Valid**  
  The document's signature is valid.
- `ResultOfVerification/ValidationDate` = **2026-05-05**  
  Checked.
- `ResultOfVerification/ValidationTime` = **12:05:00**  
  At that time.
- `ResultOfVerification/ValidateProcess` = **Signature and hash check**  
  What was checked.
- `ResultOfVerification/ValidateTool` = **Accord validator**  
  The tool.
- `ResultOfVerification/ValidateToolVersion` = **3.2**  
  Its version.
- `ResultOfVerification/SignatoryParty/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ResultOfVerification/SignatoryParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.

### Digital Agreement Terms

Inside `DigitalAgreementTerms`:

- `Description` = **Documents are exchanged over the trade accord's network.**  
  The terms.
- `ValidityPeriod/StartDate` = **2026-05-05**  
  From signing.
- `ValidityPeriod/EndDate` = **2027-05-05**  
  For a year.
- `AdoptionPeriod/StartDate` = **2026-05-05**  
  The buyer adopts it
- `AdoptionPeriod/EndDate` = **2026-05-19**  
  within two weeks.
- `ServiceLevelAgreement/ID` = **LD-SLA-1**  
  The service level.
- `ServiceLevelAgreement/ServiceTypeCode` = **Messaging**  
  For the exchange.
- `ServiceLevelAgreement/ServiceType` = **Document exchange**  
  In words.
- `ServiceLevelAgreement/AvailabilityTimePercent` = **99.5**  
  The access point is available 99.5 % of the time.
- `ServiceLevelAgreement/MondayAvailabilityIndicator` = **true**  
  Supported on Mondays.
- `ServiceLevelAgreement/TuesdayAvailabilityIndicator` = **true**  
  Supported on Tuesdays.
- `ServiceLevelAgreement/WednesdayAvailabilityIndicator` = **true**  
  Supported on Wednesdays.
- `ServiceLevelAgreement/ThursdayAvailabilityIndicator` = **true**  
  Supported on Thursdays.
- `ServiceLevelAgreement/FridayAvailabilityIndicator` = **true**  
  Supported on Fridays.
- `ServiceLevelAgreement/SaturdayAvailabilityIndicator` = **false**  
  No support on Saturdays.
- `ServiceLevelAgreement/SundayAvailabilityIndicator` = **false**  
  No support on Sundays.
- `ServiceLevelAgreement/MinimumResponseTimeDurationMeasure` = **4** (unitCode `HUR`)  
  An answer to a problem within four hours.
- `ServiceLevelAgreement/MinimumDownTimeScheduleDurationMeasure` = **48** (unitCode `HUR`)  
  Planned downtime announced 48 hours ahead.
- `ServiceLevelAgreement/MaximumIncidentNotificationDurationMeasure` = **1** (unitCode `HUR`)  
  An incident reported within an hour.
- `ServiceLevelAgreement/MaximumDataLossDurationMeasure` = **0** (unitCode `HUR`)  
  No document may be lost.
- `ServiceLevelAgreement/MeanTimeToRecoverDurationMeasure` = **2** (unitCode `HUR`)  
  Back in two hours on average.
- `ServiceLevelAgreement/ServiceAvailabilityPeriod/StartTime` = **07:00:00**  
  Support from seven.
- `ServiceLevelAgreement/ServiceAvailabilityPeriod/EndTime` = **19:00:00**  
  Until seven.
- `ServiceLevelAgreement/ServiceMaintenancePeriod/StartTime` = **02:00:00**  
  Maintenance at night.
- `ServiceLevelAgreement/ServiceMaintenancePeriod/EndTime` = **04:00:00**  
  Until four.

### Digital Process

Inside `DigitalProcess`:

- `ID` = **ordering**  
  A process the parties agree to exchange electronically.
- `Description` = **Order, order response and order change.**  
  What the process covers.
- `ProfileID` = **urn:ubl-examples:world:process:ordering**  
  The process profile.
- `DigitalCollaboration/ID` = **ordering-1**  
  The main exchange of the process.
- `DigitalCollaboration/SendingDigitalService/ID` = **VT-Order-OUT**  
  The party's service for this document.
- `DigitalCollaboration/SendingDigitalService/CustomizationID` = **urn:ubl-examples:world**  
  The customization the documents follow.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/ID` = **Order**  
  The document type.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd**  
  The schema.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Order**  
  The document type, as a code.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859**  
  The party's address on it.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **ACCORD-CERT-1-xl**  
  The access point's certificate.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH**  
  The business envelope.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.1-xl.example/as4**  
  The access point.
- `DigitalCollaboration/SendingDigitalService/CertificationDocumentReference/ID` = **LTAC-CERT-26-017**  
  The trade accord council's certificate that the distributor's system passed the conformance test.
- `DigitalCollaboration/ReceivingDigitalService/ID` = **LD-Order-IN**  
  The party's service for this document.
- `DigitalCollaboration/ReceivingDigitalService/CustomizationID` = **urn:ubl-examples:world**  
  The customization the documents follow.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/ID` = **Order**  
  The document type.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd**  
  The schema.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Order**  
  The document type, as a code.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274**  
  The party's address on it.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **ACCORD-CERT-6-xb**  
  The access point's certificate.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH**  
  The business envelope.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.6-xb.example/as4**  
  The access point.
- `CertificationDocumentReference/ID` = **ACCORD-CERT-PROC-ordering**  
  The council's certification of the process.
- `ID` = **billing**  
  A process the parties agree to exchange electronically.
- `Description` = **Invoice, credit note, statement and remittance advice.**  
  What the process covers.
- `ProfileID` = **urn:ubl-examples:world:process:billing**  
  The process profile.
- `DigitalCollaboration/ID` = **billing-1**  
  The main exchange of the process.
- `DigitalCollaboration/SendingDigitalService/ID` = **LD-Invoice-OUT**  
  The party's service for this document.
- `DigitalCollaboration/SendingDigitalService/CustomizationID` = **urn:ubl-examples:world**  
  The customization the documents follow.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/ID` = **Invoice**  
  The document type.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd**  
  The schema.
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Invoice**  
  The document type, as a code.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274**  
  The party's address on it.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **ACCORD-CERT-6-xb**  
  The access point's certificate.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH**  
  The business envelope.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.6-xb.example/as4**  
  The access point.
- `DigitalCollaboration/SendingDigitalService/CertificationDocumentReference/ID` = **LTAC-CERT-26-017**  
  The trade accord council's certificate that the distributor's system passed the conformance test.
- `DigitalCollaboration/ReceivingDigitalService/ID` = **VT-Invoice-IN**  
  The party's service for this document.
- `DigitalCollaboration/ReceivingDigitalService/CustomizationID` = **urn:ubl-examples:world**  
  The customization the documents follow.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/ID` = **Invoice**  
  The document type.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/FormatID` = **UBL**  
  The format.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/VersionID` = **2.5**  
  Its version.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/SchemaURI` = **https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd**  
  The schema.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Invoice**  
  The document type, as a code.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859**  
  The party's address on it.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **ACCORD-CERT-1-xl**  
  The access point's certificate.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH**  
  The business envelope.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.1-xl.example/as4**  
  The access point.
- `CertificationDocumentReference/ID` = **ACCORD-CERT-PROC-billing**  
  The council's certification of the process.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DigitalAgreement xmlns="urn:oasis:names:specification:ubl:schema:xsd:DigitalAgreement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-DAG-26-0125</cbc:ID>
  <cbc:UUID>1992d68e-5c04-58e5-9789-3ddfb5e9b203</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>12:59:00</cbc:IssueTime>
  <cbc:AgreementTypeCode>Bilateral</cbc:AgreementTypeCode>
  <cbc:VersionID>1.0</cbc:VersionID>
  <cbc:PreviousVersionID>0.9</cbc:PreviousVersionID>
  <cbc:RequiredResponseMessageLevelCode>Business</cbc:RequiredResponseMessageLevelCode>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-DA-1</cbc:ID>
    <cbc:ReasonCode>Approval</cbc:ReasonCode>
    <cbc:Note>Signed with the company's seal certificate.</cbc:Note>
    <cbc:ValidationDate>2026-05-05</cbc:ValidationDate>
    <cbc:ValidationTime>09:05:00</cbc:ValidationTime>
    <cbc:ValidatorID>LTAC-VALIDATOR</cbc:ValidatorID>
    <cbc:CanonicalizationMethod>http://www.w3.org/2006/12/xml-c14n11</cbc:CanonicalizationMethod>
    <cbc:SignatureMethod>http://www.w3.org/2001/04/xmldsig-more#rsa-sha256</cbc:SignatureMethod>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
    <cac:DigitalSignatureAttachment>
      <cbc:EmbeddedDocumentBinaryObject mimeCode="application/pkcs7-signature">U2lnbmF0dXJlIHZhbHVlIG9mIExELVNJRy0yNi1EQS0xLCBzaG9ydGVuZWQgZm9yIHRoZSBleGFtcGxlIHdvcmxkLg==</cbc:EmbeddedDocumentBinaryObject>
    </cac:DigitalSignatureAttachment>
    <cac:OriginalDocumentReference>
      <cbc:ID>LD-DOC-26-DA-1</cbc:ID>
    </cac:OriginalDocumentReference>
  </cac:Signature>
  <cac:GovernorParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Exchange Street</cbc:StreetName>
      <cbc:BuildingNumber>34</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38521</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeport Trade Accord Council</cbc:RegistrationName>
      <cbc:CompanyID>20411096</cbc:CompanyID>
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
      <cbc:Name>Secretariat</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 2 3852 1096</cbc:Telephone>
      <cbc:ElectronicMail>secretariat@tradeaccord.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411096</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:GovernorParty>
  <cac:ParticipantParty>
    <cbc:InitiatingPartyIndicator>true</cbc:InitiatingPartyIndicator>
    <cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
    <cbc:PublicPartyIndicator>false</cbc:PublicPartyIndicator>
    <cbc:ServiceProviderPartyIndicator>false</cbc:ServiceProviderPartyIndicator>
    <cac:Party>
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
    </cac:Party>
    <cac:LegalContact>
      <cbc:Name>Legal department</cbc:Name>
    </cac:LegalContact>
    <cac:TechnicalContact>
      <cbc:Name>Integration desk</cbc:Name>
    </cac:TechnicalContact>
    <cac:SupportContact>
      <cbc:Name>Service desk</cbc:Name>
    </cac:SupportContact>
    <cac:CommercialContact>
      <cbc:Name>Sales office</cbc:Name>
    </cac:CommercialContact>
  </cac:ParticipantParty>
  <cac:ParticipantParty>
    <cbc:InitiatingPartyIndicator>false</cbc:InitiatingPartyIndicator>
    <cbc:PrivatePartyIndicator>true</cbc:PrivatePartyIndicator>
    <cbc:PublicPartyIndicator>false</cbc:PublicPartyIndicator>
    <cbc:ServiceProviderPartyIndicator>false</cbc:ServiceProviderPartyIndicator>
    <cac:Party>
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
        <cbc:ID>qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en">Reef Street</cbc:StreetName>
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
    </cac:Party>
    <cac:LegalContact>
      <cbc:Name>Legal department</cbc:Name>
    </cac:LegalContact>
    <cac:TechnicalContact>
      <cbc:Name>Integration desk</cbc:Name>
    </cac:TechnicalContact>
    <cac:SupportContact>
      <cbc:Name>Service desk</cbc:Name>
    </cac:SupportContact>
    <cac:CommercialContact>
      <cbc:Name>Purchasing</cbc:Name>
    </cac:CommercialContact>
  </cac:ParticipantParty>
  <cac:AgreementCountry>
    <cbc:IdentificationCode>XB</cbc:IdentificationCode>
  </cac:AgreementCountry>
  <cac:RequiredCertificationDocumentReference>
    <cbc:ID>LD-EDI-TERMS-1.0</cbc:ID>
    <cbc:UUID>ed76dcbb-efca-5239-9195-cf2d240a09d4</cbc:UUID>
    <cbc:IssueDate>2026-05-05</cbc:IssueDate>
    <cbc:IssueTime>12:00:00</cbc:IssueTime>
    <cbc:DocumentTypeCode>Terms</cbc:DocumentTypeCode>
    <cbc:XPath>/DigitalAgreement/DigitalAgreementTerms</cbc:XPath>
    <cbc:ReferencedDocumentInternalAddress>section-2</cbc:ReferencedDocumentInternalAddress>
    <cbc:LanguageID>en</cbc:LanguageID>
    <cbc:LocaleCode>EN</cbc:LocaleCode>
    <cbc:VersionID>1.0</cbc:VersionID>
    <cbc:DocumentStatusCode>Confirmed</cbc:DocumentStatusCode>
    <cbc:DocumentDescription>The terms of the digital trade agreement.</cbc:DocumentDescription>
    <cac:Attachment>
      <cbc:EmbeddedDocumentBinaryObject mimeCode="text/plain">VGVybXMgb2YgdGhlIGRpZ2l0YWwgdHJhZGUgYWdyZWVtZW50IG9mIHRoZSB3b3JsZCwgdmVyc2lvbiAxLjAu</cbc:EmbeddedDocumentBinaryObject>
      <cbc:FileName>terms.txt</cbc:FileName>
      <cac:ExternalReference>
        <cbc:URI>https://www.lumeway.example/edi/terms-1.0.pdf</cbc:URI>
        <cbc:DocumentHash>9f2c4e1ab37d5c8e0f6a2b4d8c1e3f5a7b9d0c2e4f6a8b1c3d5e7f9a0b2c4d6e</cbc:DocumentHash>
        <cbc:HashAlgorithmMethod>http://www.w3.org/2001/04/xmlenc#sha256</cbc:HashAlgorithmMethod>
        <cbc:ExpiryDate>2027-05-04</cbc:ExpiryDate>
        <cbc:ExpiryTime>23:59:00</cbc:ExpiryTime>
        <cbc:MimeCode>application/pdf</cbc:MimeCode>
        <cbc:FormatCode>PDF/A-3</cbc:FormatCode>
        <cbc:EncodingCode>Binary</cbc:EncodingCode>
        <cbc:CharacterSetCode>UTF-8</cbc:CharacterSetCode>
        <cbc:FileName>terms-1.0.pdf</cbc:FileName>
        <cbc:Description>The full terms.</cbc:Description>
      </cac:ExternalReference>
    </cac:Attachment>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-05-05</cbc:StartDate>
      <cbc:EndDate>2027-05-05</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:ResultOfVerification>
      <cbc:ValidatorID>LTAC-VALIDATOR</cbc:ValidatorID>
      <cbc:ValidationResultCode>Valid</cbc:ValidationResultCode>
      <cbc:ValidationDate>2026-05-05</cbc:ValidationDate>
      <cbc:ValidationTime>12:05:00</cbc:ValidationTime>
      <cbc:ValidateProcess>Signature and hash check</cbc:ValidateProcess>
      <cbc:ValidateTool>Accord validator</cbc:ValidateTool>
      <cbc:ValidateToolVersion>3.2</cbc:ValidateToolVersion>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:ResultOfVerification>
  </cac:RequiredCertificationDocumentReference>
  <cac:DigitalAgreementTerms>
    <cbc:Description>Documents are exchanged over the trade accord's network.</cbc:Description>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-05-05</cbc:StartDate>
      <cbc:EndDate>2027-05-05</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:AdoptionPeriod>
      <cbc:StartDate>2026-05-05</cbc:StartDate>
      <cbc:EndDate>2026-05-19</cbc:EndDate>
    </cac:AdoptionPeriod>
    <cac:ServiceLevelAgreement>
      <cbc:ID>LD-SLA-1</cbc:ID>
      <cbc:ServiceTypeCode>Messaging</cbc:ServiceTypeCode>
      <cbc:ServiceType>Document exchange</cbc:ServiceType>
      <cbc:AvailabilityTimePercent>99.5</cbc:AvailabilityTimePercent>
      <cbc:MondayAvailabilityIndicator>true</cbc:MondayAvailabilityIndicator>
      <cbc:TuesdayAvailabilityIndicator>true</cbc:TuesdayAvailabilityIndicator>
      <cbc:WednesdayAvailabilityIndicator>true</cbc:WednesdayAvailabilityIndicator>
      <cbc:ThursdayAvailabilityIndicator>true</cbc:ThursdayAvailabilityIndicator>
      <cbc:FridayAvailabilityIndicator>true</cbc:FridayAvailabilityIndicator>
      <cbc:SaturdayAvailabilityIndicator>false</cbc:SaturdayAvailabilityIndicator>
      <cbc:SundayAvailabilityIndicator>false</cbc:SundayAvailabilityIndicator>
      <cbc:MinimumResponseTimeDurationMeasure unitCode="HUR">4</cbc:MinimumResponseTimeDurationMeasure>
      <cbc:MinimumDownTimeScheduleDurationMeasure unitCode="HUR">48</cbc:MinimumDownTimeScheduleDurationMeasure>
      <cbc:MaximumIncidentNotificationDurationMeasure unitCode="HUR">1</cbc:MaximumIncidentNotificationDurationMeasure>
      <cbc:MaximumDataLossDurationMeasure unitCode="HUR">0</cbc:MaximumDataLossDurationMeasure>
      <cbc:MeanTimeToRecoverDurationMeasure unitCode="HUR">2</cbc:MeanTimeToRecoverDurationMeasure>
      <cac:ServiceAvailabilityPeriod>
        <cbc:StartTime>07:00:00</cbc:StartTime>
        <cbc:EndTime>19:00:00</cbc:EndTime>
      </cac:ServiceAvailabilityPeriod>
      <cac:ServiceMaintenancePeriod>
        <cbc:StartTime>02:00:00</cbc:StartTime>
        <cbc:EndTime>04:00:00</cbc:EndTime>
      </cac:ServiceMaintenancePeriod>
    </cac:ServiceLevelAgreement>
  </cac:DigitalAgreementTerms>
  <cac:DigitalProcess>
    <cbc:ID>ordering</cbc:ID>
    <cbc:Description>Order, order response and order change.</cbc:Description>
    <cbc:ProfileID>urn:ubl-examples:world:process:ordering</cbc:ProfileID>
    <cac:DigitalCollaboration>
      <cbc:ID>ordering-1</cbc:ID>
      <cac:SendingDigitalService>
        <cbc:ID>VT-Order-OUT</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Order</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode>Order</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID>XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>ACCORD-CERT-1-xl</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode>SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.1-xl.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
        <cac:CertificationDocumentReference>
          <cbc:ID>LTAC-CERT-26-017</cbc:ID>
        </cac:CertificationDocumentReference>
      </cac:SendingDigitalService>
      <cac:ReceivingDigitalService>
        <cbc:ID>LD-Order-IN</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Order</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Order-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode>Order</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID>XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>ACCORD-CERT-6-xb</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode>SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.6-xb.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
      </cac:ReceivingDigitalService>
    </cac:DigitalCollaboration>
    <cac:CertificationDocumentReference>
      <cbc:ID>ACCORD-CERT-PROC-ordering</cbc:ID>
    </cac:CertificationDocumentReference>
  </cac:DigitalProcess>
  <cac:DigitalProcess>
    <cbc:ID>billing</cbc:ID>
    <cbc:Description>Invoice, credit note, statement and remittance advice.</cbc:Description>
    <cbc:ProfileID>urn:ubl-examples:world:process:billing</cbc:ProfileID>
    <cac:DigitalCollaboration>
      <cbc:ID>billing-1</cbc:ID>
      <cac:SendingDigitalService>
        <cbc:ID>LD-Invoice-OUT</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Invoice</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode>Invoice</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID>XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>ACCORD-CERT-6-xb</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode>SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.6-xb.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
        <cac:CertificationDocumentReference>
          <cbc:ID>LTAC-CERT-26-017</cbc:ID>
        </cac:CertificationDocumentReference>
      </cac:SendingDigitalService>
      <cac:ReceivingDigitalService>
        <cbc:ID>VT-Invoice-IN</cbc:ID>
        <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
        <cac:DigitalDocumentMetadata>
          <cbc:ID>Invoice</cbc:ID>
          <cbc:FormatID>UBL</cbc:FormatID>
          <cbc:VersionID>2.5</cbc:VersionID>
          <cbc:SchemaURI>https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/UBL-Invoice-2.5.xsd</cbc:SchemaURI>
          <cbc:DocumentTypeCode>Invoice</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID>XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>ACCORD-CERT-1-xl</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode>SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.1-xl.example/as4</cbc:EndpointURI>
          </cac:DigitalMessageDelivery>
        </cac:DigitalDeliveryChannel>
      </cac:ReceivingDigitalService>
    </cac:DigitalCollaboration>
    <cac:CertificationDocumentReference>
      <cbc:ID>ACCORD-CERT-PROC-billing</cbc:ID>
    </cac:CertificationDocumentReference>
  </cac:DigitalProcess>
</DigitalAgreement>
```
