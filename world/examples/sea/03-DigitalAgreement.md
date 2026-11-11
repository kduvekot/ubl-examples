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
- `AgreementTypeCode` = **BILATERAL** (listID `urn:ubl-examples:world:codelist:AgreementTypeCode`)  
  An agreement between two parties. The code is from the Trade Accord's agreement type list: BILATERAL = Bilateral agreement.
- `VersionID` = **1.0**  
  The first version of the agreement.
- `PreviousVersionID` = **0.9**  
  The draft both sides commented on.
- `RequiredResponseMessageLevelCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:ResponseMessageLevelCode`)  
  A business response is required for every document. The code is from the Trade Accord's response message level list: BUSINESS = Business response.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-26-DA-1**  
  The distributor's signature as governor.
- `ReasonCode` = **APPROVAL** (listID `urn:ubl-examples:world:codelist:SignatureReasonCode`)  
  The signer approves the document. The code is from the Trade Accord's signature reason list: APPROVAL = Approval.
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Trade Accord Council (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 9411 = Activities of business and employers membership organizations.
- `PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Trade Accord Council (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Lumeport Trade Accord Council**  
  The trading name; identity of Lumeport Trade Accord Council (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/ID` = **LUM-ADR-268189** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Lumeport Trade Accord Council (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Trade Accord Council (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Lumeport Trade Accord Council**  
  The name under which the party is registered, with its legal form; identity of Lumeport Trade Accord Council (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Lumeport Trade Accord Council (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Secretariat**  
  The desk that handles this document; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Lumeport Trade Accord Council (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2396 1096**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeport Trade Accord Council (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Party/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1230822** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `Party/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **MEDIUM** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 183 persons and its turnover of 33900000.00 XBL in 2025, by the Trade Accord's limits; identity of Lumeway Distribution (world/parties.json). The code is from the Trade Accord's entity size list: MEDIUM = Medium-sized enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 474 274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Party/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The name of code LTD in Lisavu's national company legal form list.
- `Party/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 34 persons and its turnover of 1940000.000 XLC in 2025, by the Trade Accord's limits; identity of Velumi Trading (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 729 1859**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
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

- `IdentificationCode` = **XB** (listID `ISO 3166`)  
  Governed by Bayvarra's law. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

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
- `DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document. The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `XPath` = **/DigitalAgreement/DigitalAgreementTerms**  
  The part of this document the reference explains.
- `ReferencedDocumentInternalAddress` = **section-2**  
  The section of the referenced document meant.
- `LanguageID` = **en**  
  In English.
- `LocaleCode` = **en** (listID `ISO 639`)  
  The locale, as a lower-case ISO 639 code of the world's language list. The code is from the world's copy of ISO 639 Language: en = English.
- `VersionID` = **1.0**  
  The version referred to.
- `DocumentStatusCode` = **Confirmed** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  The version both sides confirmed. The code is from the world's copy of UBL's Document status list, with a listID: Confirmed = Document has been confirmed.
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
- `Attachment/ExternalReference/MimeCode` = **application/pdf** (listID `IANA Media Types`)  
  A PDF. The code is from UBL's default Media type (IANA) list: application/pdf.
- `Attachment/ExternalReference/FormatCode` = **fmt/480** (listID `PRONOM`)  
  An archivable PDF. The code is from the world's copy of PRONOM file format registry (PUIDs): fmt/480 = Acrobat PDF/A - Portable Document Format, version 3b.
- `Attachment/ExternalReference/EncodingCode` = **binary** (listID `RFC 2045 Content-Transfer-Encoding`)  
  Not encoded. The code is from the world's copy of RFC 2045 Content-Transfer-Encoding: binary.
- `Attachment/ExternalReference/CharacterSetCode` = **UTF-8** (listID `IANA Character Sets`)  
  The character set of its text. The code is from the world's copy of IANA Character Sets: UTF-8.
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
- `ResultOfVerification/ValidationResultCode` = **VALID** (listID `urn:ubl-examples:world:codelist:ValidationResultCode`)  
  The document's signature is valid. The code is from the Trade Accord's validation result list: VALID = Valid.
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
- `ServiceLevelAgreement/ServiceTypeCode` = **MESSAGING** (listID `urn:ubl-examples:world:codelist:ServiceTypeCode`)  
  For the exchange. The code is from the Trade Accord's service type list: MESSAGING = Messaging service.
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
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's ubl document type list: Order.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in its country's companies register).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-41859**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network (decision ID-Q10).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.velumi.example/as4**  
  The access point, under the party's own domain.
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
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's ubl document type list: Order.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in its country's companies register).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-20410274**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network (decision ID-Q10).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.lumeway.example/as4**  
  The access point, under the party's own domain.
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
- `DigitalCollaboration/SendingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's ubl document type list: Invoice.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in its country's companies register).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-20410274**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network (decision ID-Q10).
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/SendingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.lumeway.example/as4**  
  The access point, under the party's own domain.
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
- `DigitalCollaboration/ReceivingDigitalService/DigitalDocumentMetadata/DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document type, as a code. The code is from the Trade Accord's ubl document type list: Invoice.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/NetworkID` = **ACCORD-NET**  
  The trade accord's document network.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/ParticipantID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's address on it. The schemeID names the scheme it is from: the electronic address in the Trade Accord's exchange network (the country code, a colon and the party's number in its country's companies register).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/TestIndicator` = **false**  
  In production.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/ID` = **LTAC-AP-41859**  
  The serial number of the access point's X.509 certificate, unique only with its issuer: the Trade Accord Council, the certification authority of the network (decision ID-Q10).
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/CertificateType` = **Access point**  
  Its kind.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalCertificate/IssuerParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/ProtocolID` = **AS4**  
  The transport protocol.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EnvelopeTypeCode` = **SBDH** (listID `urn:ubl-examples:world:codelist:EnvelopeTypeCode`)  
  The business envelope. The code is from the Trade Accord's envelope type list: SBDH = Standard Business Document Header.
- `DigitalCollaboration/ReceivingDigitalService/DigitalDeliveryChannel/DigitalMessageDelivery/EndpointURI` = **https://ap.velumi.example/as4**  
  The access point, under the party's own domain.
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
  <cbc:AgreementTypeCode listID="urn:ubl-examples:world:codelist:AgreementTypeCode">BILATERAL</cbc:AgreementTypeCode>
  <cbc:VersionID>1.0</cbc:VersionID>
  <cbc:PreviousVersionID>0.9</cbc:PreviousVersionID>
  <cbc:RequiredResponseMessageLevelCode listID="urn:ubl-examples:world:codelist:ResponseMessageLevelCode">BUSINESS</cbc:RequiredResponseMessageLevelCode>
  <cac:Signature>
    <cbc:ID>LD-SIG-26-DA-1</cbc:ID>
    <cbc:ReasonCode listID="urn:ubl-examples:world:codelist:SignatureReasonCode">APPROVAL</cbc:ReasonCode>
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
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-268189</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Exchange Street</cbc:StreetName>
      <cbc:BuildingNumber>34</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38521</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeport Trade Accord Council</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:CompanyID>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FBR</cbc:ID>
        <cbc:Name>Federal business register of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Secretariat</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 2 38 2396 1096</cbc:Telephone>
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
        <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Distribution Drive</cbc:StreetName>
        <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
        <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
        <cbc:BuildingNumber>43</cbc:BuildingNumber>
        <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71214</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">UL-1230822</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
          <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:CompanyID>
        <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">MEDIUM</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Marrowdale</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
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
        <cbc:ID schemeID="ISO 639">qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XB">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Selanu</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XL:ICR</cbc:ID>
          <cbc:Name>Island companies register</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 729 1859</cbc:Telephone>
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
    <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
  </cac:AgreementCountry>
  <cac:RequiredCertificationDocumentReference>
    <cbc:ID>LD-EDI-TERMS-1.0</cbc:ID>
    <cbc:UUID>ed76dcbb-efca-5239-9195-cf2d240a09d4</cbc:UUID>
    <cbc:IssueDate>2026-05-05</cbc:IssueDate>
    <cbc:IssueTime>12:00:00</cbc:IssueTime>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
    <cbc:XPath>/DigitalAgreement/DigitalAgreementTerms</cbc:XPath>
    <cbc:ReferencedDocumentInternalAddress>section-2</cbc:ReferencedDocumentInternalAddress>
    <cbc:LanguageID>en</cbc:LanguageID>
    <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    <cbc:VersionID>1.0</cbc:VersionID>
    <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">Confirmed</cbc:DocumentStatusCode>
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
        <cbc:MimeCode listID="IANA Media Types">application/pdf</cbc:MimeCode>
        <cbc:FormatCode listID="PRONOM">fmt/480</cbc:FormatCode>
        <cbc:EncodingCode listID="RFC 2045 Content-Transfer-Encoding">binary</cbc:EncodingCode>
        <cbc:CharacterSetCode listID="IANA Character Sets">UTF-8</cbc:CharacterSetCode>
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
      <cbc:ValidationResultCode listID="urn:ubl-examples:world:codelist:ValidationResultCode">VALID</cbc:ValidationResultCode>
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
      <cbc:ServiceTypeCode listID="urn:ubl-examples:world:codelist:ServiceTypeCode">MESSAGING</cbc:ServiceTypeCode>
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
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-41859</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.velumi.example/as4</cbc:EndpointURI>
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
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-20410274</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.lumeway.example/as4</cbc:EndpointURI>
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
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-20410274</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.lumeway.example/as4</cbc:EndpointURI>
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
          <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
        </cac:DigitalDocumentMetadata>
        <cac:DigitalDeliveryChannel>
          <cbc:NetworkID>ACCORD-NET</cbc:NetworkID>
          <cbc:ParticipantID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ParticipantID>
          <cbc:TestIndicator>false</cbc:TestIndicator>
          <cac:DigitalCertificate>
            <cbc:ID>LTAC-AP-41859</cbc:ID>
            <cbc:CertificateType>Access point</cbc:CertificateType>
            <cac:IssuerParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
              </cac:PartyName>
            </cac:IssuerParty>
          </cac:DigitalCertificate>
          <cac:DigitalMessageDelivery>
            <cbc:ProtocolID>AS4</cbc:ProtocolID>
            <cbc:EnvelopeTypeCode listID="urn:ubl-examples:world:codelist:EnvelopeTypeCode">SBDH</cbc:EnvelopeTypeCode>
            <cbc:EndpointURI>https://ap.velumi.example/as4</cbc:EndpointURI>
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
