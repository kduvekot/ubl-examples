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
- `ProfileID` = **urn:ubl-examples:world:process:sea**  
  The business process the document belongs to: the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TOL-BL-26-0139**  
  The bill of lading number.
- `CarrierAssignedID` = **TWL-BK-26-55710**  
  The booking the bill of lading is issued under.
- `UUID` = **aa5970ad-efd9-5660-a1d7-8a2f0bf2de7b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-14**  
  Issued when the goods are shipped on board.
- `IssueTime` = **10:54:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Name` = **Bill of lading**  
  What it is.
- `Description` = **Shipped on board.**  
  The kind of bill.
- `Note` = **Freight prepaid.**  
  Who has paid the freight.
- `DocumentStatusCode` = **Confirmed** (listID `urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode`)  
  Issued. The code is from the world's copy of UBL's Document status list, with a listID: Confirmed = Document has been confirmed.
- `ShippingOrderID` = **BF-FI-26-0137**  
  The forwarder's booking with the carrier.
- `ToOrderIndicator` = **true**  
  Made out to order: the buyer can transfer it by endorsement.
- `AdValoremIndicator` = **false**  
  No value declared to the carrier: its liability stays limited.
- `DeclaredCarriageValueAmount` = **0.00** (currencyID `XBL`)  
  No value declared.
- `OtherInstruction` = **Three originals issued.**  
  How many originals there are.

### Consignor Party

Inside `ConsignorParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1230822** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **MEDIUM** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 183 persons and its turnover of 33900000.00 XBL in 2025, by the Trade Accord's limits; identity of Lumeway Distribution (world/parties.json). The code is from the Trade Accord's entity size list: MEDIUM = Medium-sized enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
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
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 474 274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Tidewell Ocean Lines (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5012 = Sea and coastal freight water transport.
- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered for state sales tax; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1235754** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Tidewell Ocean Lines (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines Corp**  
  The name under which the party is registered, with its legal form; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1974-03-01**  
  The day the company was entered in the register; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **CORP** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: CORP = Corporation (public).
- `PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The name of code CORP in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 776 persons and its turnover of 865000000.00 XBL in 2025, by the Trade Accord's limits; identity of Tidewell Ocean Lines (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **40000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Contact/Name` = **Bookings**  
  The desk that handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2418 1918**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Bayforth Forwarding (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5229 = Other transportation support activities.
- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered for state sales tax; identity of Bayforth Forwarding (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1234932** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Bayforth Forwarding (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 40 persons and its turnover of 6660000.00 XBL in 2025, by the Trade Accord's limits; identity of Bayforth Forwarding (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
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
- `Contact/Name` = **Export desk**  
  The desk that handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2144 1644**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
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
- `GrossWeightMeasure` = **4106.4** (unitCode `KGM`)  
  The gross weight of the cargo.
- `TotalGoodsItemQuantity` = **2** (unitCode `EA`)  
  Benches and side frames.
- `ConsignmentQuantity` = **1** (unitCode `EA`)  
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
- `Consignment/TariffCode` = **TWL-T-0940**  
  The item of the carrier's own freight tariff for this cargo: furniture. A code the carrier defines, so it has no code list.
- `Consignment/InsurancePremiumAmount` = **140.00** (currencyID `XBL`)  
  The premium the seller paid under CIF.
- `Consignment/ShippingPriorityLevelCode` = **STANDARD** (listID `urn:ubl-examples:world:codelist:ShippingPriorityCode`)  
  The normal sailing, no priority loading. The code is from the Trade Accord's shipping priority list: STANDARD = Standard.
- `Consignment/HandlingCode` = **DECK** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier may stow the container on deck. The code is from the Trade Accord's handling instruction list: DECK = On-deck stowage allowed.
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 4649 = Wholesale of other household goods.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/ConsigneeParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The name of code LTD in Lisavu's national company legal form list.
- `Consignment/ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 34 persons and its turnover of 1940000.000 XLC in 2025, by the Trade Accord's limits; identity of Velumi Trading (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Consignment/ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Consignment/ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Consignment/ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 729 1859**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
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
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Nalevi Warehousing (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 5210 = Warehousing and storage.
- `Consignment/NotifyParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Nalevi Warehousing (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/NotifyParty/PartyName/Name` = **Nalevi Warehousing**  
  The trading name; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/NotifyParty/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Consignment/NotifyParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/NotifyParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Vilafa Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Lagoon Road** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/NotifyParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/NotifyParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationName` = **Nalevi Warehousing Ltd**  
  The name under which the party is registered, with its legal form; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyLegalEntity/CompanyID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; identity of Nalevi Warehousing (world/parties.json). The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XL:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Lisavu's national list: only the listID tells the forms of different countries apart. The code is from Lisavu's national company legal form list: LTD = Island limited company.
- `Consignment/NotifyParty/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The name of code LTD in Lisavu's national company legal form list.
- `Consignment/NotifyParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 17 persons and its turnover of 2500000.000 XLC in 2025, by the Trade Accord's limits; identity of Nalevi Warehousing (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `Consignment/NotifyParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Consignment/NotifyParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `Consignment/NotifyParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/NotifyParty/Contact/Name` = **Goods inwards**  
  The desk that handles this document; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Nalevi Warehousing (world/parties.json).
- `Consignment/NotifyParty/Contact/Telephone` = **+999 3 722 1722**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Nalevi Warehousing (world/parties.json).
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
- `Consignment/OriginalDepartureCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  From Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/FinalDestinationCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  To the island. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/DeliveryTerms/ID` = **CIF** (schemeID `INCOTERMS`)  
  Incoterms 2020: cost, insurance and freight to the port of Selanu. The code is from the world's copy of Incoterms 2020: CIF = Cost, Insurance and Freight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/DeliveryTerms/LossRiskResponsibilityCode` = **BUYER** (listID `urn:ubl-examples:world:codelist:RiskResponsiblePartyCode`)  
  The risk is the buyer's from on board in Lumeport. The code is from the Trade Accord's party bearing the risk list: BUYER = Buyer.
- `Consignment/DeliveryTerms/LossRisk` = **Risk passes when the goods are on board the vessel in Lumeport.**  
  In words.
- `Consignment/DeliveryTerms/Amount` = **53778.00** (currencyID `XBL`)  
  The CIF value the terms are based on.
- `Consignment/DeliveryTerms/DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/DeliveryTerms/DeliveryLocation/Name` = **Port of Selanu**  
  The named port of destination.
- `Consignment/DeliveryTerms/DeliveryLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/DeliveryTerms/AllowanceCharge/ChargeIndicator` = **true**  
  A cost under the terms.
- `Consignment/DeliveryTerms/AllowanceCharge/AllowanceChargeReasonCode` = **HD** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: HD = Handling.
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
- `Consignment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **Ocean freight, 40-foot container**  
  In words.
- `Consignment/FreightAllowanceCharge/Amount` = **2700.00** (currencyID `XBL`)  
  The carrier's rate.
- `Consignment/ExtraAllowanceCharge/ChargeIndicator` = **true**  
  A surcharge.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The bunker surcharge is part of the freight: UN/EDIFACT 7161 has no code of its own for it, so it carries the freight code. The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReason` = **Bunker surcharge**  
  For the fuel price.
- `Consignment/ExtraAllowanceCharge/Amount` = **250.00** (currencyID `XBL`)  
  Together with the freight: the 2,950 lume the forwarder invoices.
- `Consignment/MainCarriageShipmentStage/ID` = **2**  
  By sea from Lumeport to Selanu.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **TH-26-19E**  
  The voyage number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **EB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: EB = Eastbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **CONTAINERSHIP** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The kind of means of transport: tidewell harbour; the fleet of Tidewell Ocean Lines (world/parties.json). The code is from the Trade Accord's transport means type list: CONTAINERSHIP = Container ship.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TradeServiceCode` = **TWL-ISL**  
  The carrier's code for its island service.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/LocationID` = **140282**  
  Bay 14, row 02, tier 82.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/Location` = **On deck, aft of the bridge**  
  In words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/MeasurementDimension/AttributeID` = **SLOTLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The slot length. The code is from the Trade Accord's dimension attribute list: SLOTLENGTH = Slot length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/Stowage/MeasurementDimension/Measure` = **12.2** (unitCode `MTR`)  
  A 40-foot slot.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QBTH7**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station (world/countries.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **298702117**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipsRequirements` = **Shore power at the container quay.**  
  What the ship needs in port.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/SegregatedBallastMeasure` = **2480** (unitCode `TNE`)  
  The capacity of the tanks for ballast water only.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 1,000 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Port of Lumeport**  
  The port of loading.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Port of Selanu**  
  The port of discharge.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
- `Consignment/MainCarriageShipmentStage/FreightChargeLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/PreCarriageShipmentStage/ID` = **1**  
  By truck from Marrowdale to the port.
- `Consignment/PreCarriageShipmentStage/ShipmentStageTypeCode` = **10** (listID `UN/EDIFACT EDED 8051`)  
  The kind of stage. The code is from the world's copy of UN/EDIFACT 8051 Transport stage code qualifier: 10 = Pre-carriage transport.
- `Consignment/PreCarriageShipmentStage/ShipmentStageType` = **Pre-carriage transport**  
  The name of code 10 in the world's copy of UN/EDIFACT 8051 Transport stage code qualifier.
- `Consignment/PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/PreCarriageShipmentStage/PreCarriageIndicator` = **true**  
  Before the main carriage.
- `Consignment/PreCarriageShipmentStage/CabotageIndicator` = **false**  
  A Bayvarran truck within Bayvarra: no cabotage.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **TRUCKTRAILER** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The kind of means of transport: container chassis truck; the fleet of Bayforth Forwarding (world/parties.json). The code is from the Trade Accord's transport means type list: TRUCKTRAILER = Truck with trailer.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **BV LP 2205** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The registration plate of the truck; the fleet of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **BV CH 0412** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceDate` = **2026-05-13**  
  The container was dropped at the container quay.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceTime` = **10:15:00**  
  The local time.
- `Consignment/PreCarriageShipmentStage/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The truck to the port.
- `Consignment/PreCarriageShipmentStage/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/PreCarriageShipmentStage/FreightAllowanceCharge/AllowanceChargeReason` = **Pre-carriage by road**  
  In words.
- `Consignment/PreCarriageShipmentStage/FreightAllowanceCharge/Amount` = **310.00** (currencyID `XBL`)  
  The forwarder's own truck; part of its price to the shipper.
- `Consignment/OnCarriageShipmentStage/ID` = **3**  
  By truck from the port of Selanu to the 3PL.
- `Consignment/OnCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
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
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **42G1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet, 8 ft 6 in high, general purpose. The code is from the world's copy of ISO 6346 container size and type code: 42G1 = 40 ft, 8 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL** (listID `urn:ubl-examples:world:codelist:LoadTypeCode`)  
  A full container load. The code is from the Trade Accord's load type list: FCL = Full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **false**  
  A dry container.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7856.4** (unitCode `KGM`)  
  The verified gross mass: cargo and the container's own weight of 3,750 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **3750** (unitCode `KGM`)  
  The empty container's own weight, as marked on its door.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **140282**  
  Bay 14, row 02, tier 82: on deck, as planned by the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **TWL-S-0884213**  
  The carrier's seal, put on when the container was packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:SealIssuerTypeCode`)  
  Issued by the ocean carrier. The code is from the Trade Accord's seal issuer type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  Put on by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/SupplierParty/Party/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/SupplierParty/Party/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000018** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 001 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000018**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000025** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 002 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000025**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000032** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 003 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000032**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000049** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 004 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000049**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000056** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 005 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000056**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000063** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 006 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000063**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000070** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 007 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000070**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000087** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 008 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000087**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000094** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 009 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000094**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000100** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 010 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000100**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000117** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 011 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000117**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000124** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 012 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000124**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000131** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 013 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000131**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000148** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 014 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000148**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000155** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 015 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000155**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000162** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 016 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000162**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000179** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 017 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000179**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000186** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 018 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000186**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000193** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 019 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000193**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000209** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 020 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000209**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000216** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 021 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000216**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000223** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 022 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000223**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000230** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 023 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000230**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000247** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **4** (unitCode `EA`)  
  4 benches on the pallet, each wrapped in film.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 024 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000247**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095206101230000254** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  12 boxed side frames on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **VELUMI SELANU / 025 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095206101230000254**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/AttachedTransportEquipment/ID` = **BV CH 0412** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The forwarder's chassis the container rode on to the port. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/TransportHandlingUnit/TransportEquipment/AttachedTransportEquipment/TransportEquipmentTypeCode` = **TE** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code TE: trailer. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: TE = Trailer.
- `Consignment/TransportHandlingUnit/TransportEquipment/Package/ID` = **095206101230000254** (schemeID `GS1 SSCC`)  
  The pallet of boxed castings, packed last at the doors: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/Package/Quantity` = **12** (unitCode `EA`)  
  Twelve boxes.
- `Consignment/TransportHandlingUnit/TransportEquipment/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/TransportEquipment/Package/ContainingTransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ID` = **1**  
  The goods in the container, as one item for the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/Description` = **Park benches and spare side frames**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/GoodsItemContainer/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container the goods are in. The schemeID names the scheme it is from: the ISO 6346 container number (owner code, U, six digits and the check digit).
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/GoodsItemContainer/Quantity` = **25** (unitCode `EA`)  
  25 pallets in it.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/GoodsItemContainer/TransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container itself, as equipment. The schemeID names the scheme it is from: the ISO 6346 container number (owner code, U, six digits and the check digit).
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/ID` = **1.1**  
  The benches.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/Description` = **Park benches**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/ID` = **1.2**  
  The side frames.
- `Consignment/TransportHandlingUnit/TransportEquipment/GoodsItem/ContainedGoodsItem/Description` = **Spare side frames**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ID` = **VGM-26-0510**  
  The shipper's weight declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDate` = **2026-05-12**  
  Weighed when packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingTime` = **15:30:00**  
  After closing the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingMethodCode` = **SM2** (listID `IMO SOLAS`)  
  SOLAS method 2: the cargo and packing weighed and added to the tare. The code is from UBL's default Weighing method (IMO SOLAS) list: SM2 = SOLAS verification method 2.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceID` = **LD-SCALE-03**  
  The scale of the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceType` = **Platform scale**  
  Its kind.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/GrossMassMeasure` = **7856.4** (unitCode `KGM`)  
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
- `Consignment/FirstArrivalPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/LastExitPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/LastExitPortLocation/Name` = **Port of Lumeport**  
  The last port in Bayvarra.
- `Consignment/LastExitPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/DocumentReference/ID` = **LD-PL-26-0134**  
  The packing list of the container.
- `Consignment/InsurancePolicy/ID` = **WS-CP-26-4471**  
  The cargo policy of the insurer.
- `Consignment/InsurancePolicy/InsuranceTypeCode` = **ALLRISKS** (listID `urn:ubl-examples:world:codelist:InsuranceCoverCode`)  
  Cover against all risks. The code is from the Trade Accord's insurance cover list: ALLRISKS = All risks.
- `Consignment/InsurancePolicy/InsuredValueAmount` = **59155.80** (currencyID `XBL`)  
  110 % of the CIF value.
- `Consignment/InsurancePolicy/DeductibleAmount` = **250.00** (currencyID `XBL`)  
  The part of a claim the insured bears.
- `Consignment/InsurancePolicy/ExcessAmount` = **250.00** (currencyID `XBL`)  
  The excess per claim, as in the policy.
- `Consignment/InsurancePolicy/InsurancePremiumAmount` = **140.00** (currencyID `XBL`)  
  The premium.
- `Consignment/InsurancePolicy/BrokerParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/BrokerParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/PolicyHolderParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/PolicyHolderParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/BeneficiaryParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/BeneficiaryParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/InsurancePolicy/PolicyDocumentReference/ID` = **WS-CERT-26-0884**  
  The insurance certificate that goes with the documents.
- `InsurancePolicy/InsuredValueAmount` = **59155.80** (currencyID `XBL`)  
  The insured value, 110 % of the CIF value.
- `InsurancePolicy/ExcessAmount` = **250.00** (currencyID `XBL`)  
  The excess per claim, as in the policy.
- `InsurancePolicy/InsurerParty/WebsiteURI` = **https://www.wavesure.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/IndustryClassificationCode` = **6512** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Wavesure Cargo Insurance (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 6512 = Non-life insurance.
- `InsurancePolicy/InsurerParty/PartyIdentification/ID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Wavesure Cargo Insurance (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `InsurancePolicy/InsurerParty/PartyName/Name` = **Wavesure Cargo Insurance**  
  The trading name; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `InsurancePolicy/InsurerParty/Language/Name` = **English**  
  The language's name.
- `InsurancePolicy/InsurerParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `InsurancePolicy/InsurerParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `InsurancePolicy/InsurerParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
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
  The name of code XB-CO in Bayvarra's national state or territory list.
- `InsurancePolicy/InsurerParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Wavesure Cargo Insurance (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `InsurancePolicy/InsurerParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `InsurancePolicy/InsurerParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `InsurancePolicy/InsurerParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/RegistrationName` = **Wavesure Cargo Insurance Ltd**  
  The name under which the party is registered for state sales tax; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyTaxScheme/CompanyID` = **CO-1234521** (schemeID `urn:ubl-examples:world:XB:tax`)  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Wavesure Cargo Insurance (world/parties.json). The schemeID names the scheme it is from: the sales tax permit of a Bayvarran state or territory (the state code (UL, CO, NT), a hyphen and 7 digits).
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/ID` = **STT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: STT = State/provincial sales tax. An identifier that holds a code names the code's list in its schemeID.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
- `InsurancePolicy/InsurerParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationName` = **Wavesure Cargo Insurance Ltd**  
  The name under which the party is registered, with its legal form; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyID` = **20411507** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Wavesure Cargo Insurance (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/EntitySizeCode` = **SMALL** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 46 persons and its turnover of 7880000.00 XBL in 2025, by the Trade Accord's limits; identity of Wavesure Cargo Insurance (world/parties.json). The code is from the Trade Accord's entity size list: SMALL = Small enterprise.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `InsurancePolicy/InsurerParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `InsurancePolicy/InsurerParty/Contact/Name` = **Cargo claims**  
  The desk that handles this document; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/JobTitle` = **Client relationship manager**  
  The job of the person who answers at the desk; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/Department` = **Client services**  
  The department the desk belongs to; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/Telephone` = **+999 2 38 2807 1507**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/ElectronicMail` = **cargo@wavesure.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Wavesure Cargo Insurance (world/parties.json).
- `InsurancePolicy/InsurerParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `InsurancePolicy/InsurerParty/ElectronicAddress/ElectronicAddressID` = **XB:20411507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Wavesure Cargo Insurance (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `InsurancePolicy/BrokerParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `InsurancePolicy/BrokerParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Document Reference

Inside `DocumentReference`:

- `ID` = **BF-FI-26-0137**  
  The forwarding instructions it was issued on.

### Exchange Rate

Inside `ExchangeRate`:

- `SourceCurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The freight's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `TargetCurrencyCode` = **XLC** (listID `ISO 4217 Alpha`)  
  The island's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XLC = Coral.
- `CalculationRate` = **0.4**  
  The reference rate.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  Three originals.
- `DocumentTypeCode` = **ORIGINAL** (listID `urn:ubl-examples:world:codelist:DocumentCopyTypeCode`)  
  Originals. The code is from the Trade Accord's document copy type list: ORIGINAL = Original.
- `DistributionTypeCode` = **PAPER** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  On paper, by courier. The code is from the Trade Accord's distribution type list: PAPER = Paper.
- `Party/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **TWL-SIG-BL-sea**  
  The master's signature, by the carrier's agent.
- `SignatoryParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<BillOfLading xmlns="urn:oasis:names:specification:ubl:schema:xsd:BillOfLading-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TOL-BL-26-0139</cbc:ID>
  <cbc:CarrierAssignedID>TWL-BK-26-55710</cbc:CarrierAssignedID>
  <cbc:UUID>aa5970ad-efd9-5660-a1d7-8a2f0bf2de7b</cbc:UUID>
  <cbc:IssueDate>2026-05-14</cbc:IssueDate>
  <cbc:IssueTime>10:54:00</cbc:IssueTime>
  <cbc:Name>Bill of lading</cbc:Name>
  <cbc:Description>Shipped on board.</cbc:Description>
  <cbc:Note>Freight prepaid.</cbc:Note>
  <cbc:DocumentStatusCode listID="urn:oasis:names:specification:ubl:codelist:gc:DocumentStatusCode">Confirmed</cbc:DocumentStatusCode>
  <cbc:ShippingOrderID>BF-FI-26-0137</cbc:ShippingOrderID>
  <cbc:ToOrderIndicator>true</cbc:ToOrderIndicator>
  <cbc:AdValoremIndicator>false</cbc:AdValoremIndicator>
  <cbc:DeclaredCarriageValueAmount currencyID="XBL">0.00</cbc:DeclaredCarriageValueAmount>
  <cbc:OtherInstruction>Three originals issued.</cbc:OtherInstruction>
  <cac:ConsignorParty>
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
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1235754</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Tidewell Ocean Lines Corp</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:CompanyID>
      <cbc:RegistrationDate>1974-03-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">CORP</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XBL">40000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Bookings</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38 2418 1918</cbc:Telephone>
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
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1234932</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
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
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Operations planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38 2144 1644</cbc:Telephone>
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
    <cbc:GrossWeightMeasure unitCode="KGM">4106.4</cbc:GrossWeightMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="EA">2</cbc:TotalGoodsItemQuantity>
    <cbc:ConsignmentQuantity unitCode="EA">1</cbc:ConsignmentQuantity>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0133</cbc:ID>
      <cbc:CarrierAssignedID>TWL-BK-26-55710</cbc:CarrierAssignedID>
      <cbc:ConsignorAssignedID>VT-PO-26-0127</cbc:ConsignorAssignedID>
      <cbc:FreightForwarderAssignedID>LD-FI-26-0131</cbc:FreightForwarderAssignedID>
      <cbc:BrokerAssignedID>TCB-26-0331</cbc:BrokerAssignedID>
      <cbc:TotalInvoiceAmount currencyID="XBL">50688.00</cbc:TotalInvoiceAmount>
      <cbc:DeclaredCustomsValueAmount currencyID="XBL">53778.00</cbc:DeclaredCustomsValueAmount>
      <cbc:TariffDescription>Furniture, packed, not hazardous</cbc:TariffDescription>
      <cbc:TariffCode>TWL-T-0940</cbc:TariffCode>
      <cbc:InsurancePremiumAmount currencyID="XBL">140.00</cbc:InsurancePremiumAmount>
      <cbc:ShippingPriorityLevelCode listID="urn:ubl-examples:world:codelist:ShippingPriorityCode">STANDARD</cbc:ShippingPriorityLevelCode>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">DECK</cbc:HandlingCode>
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
          <cbc:ID schemeID="ISO 639">qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
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
          <cbc:ID schemeID="ISO 639">qal</cbc:ID>
          <cbc:Name>Lisavan</cbc:Name>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vilafa Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XB">Lagoon Road</cbc:StreetName>
          <cbc:BuildingNumber>9</cbc:BuildingNumber>
          <cbc:CityName>Selanu</cbc:CityName>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Nalevi Warehousing Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:CompanyID>
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
          <cbc:Name>Goods inwards</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Sales</cbc:Department>
          <cbc:Telephone>+999 3 722 1722</cbc:Telephone>
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
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:FinalDestinationCountry>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:FinalDestinationCountry>
      <cac:DeliveryTerms>
        <cbc:ID schemeID="INCOTERMS">CIF</cbc:ID>
        <cbc:LossRiskResponsibilityCode listID="urn:ubl-examples:world:codelist:RiskResponsiblePartyCode">BUYER</cbc:LossRiskResponsibilityCode>
        <cbc:LossRisk>Risk passes when the goods are on board the vessel in Lumeport.</cbc:LossRisk>
        <cbc:Amount currencyID="XBL">53778.00</cbc:Amount>
        <cac:DeliveryLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:DeliveryLocation>
        <cac:AllowanceCharge>
          <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
          <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">HD</cbc:AllowanceChargeReasonCode>
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
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Ocean freight, 40-foot container</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">2700.00</cbc:Amount>
      </cac:FreightAllowanceCharge>
      <cac:ExtraAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Bunker surcharge</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">250.00</cbc:Amount>
      </cac:ExtraAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>2</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>TH-26-19E</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">EB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">CONTAINERSHIP</cbc:TransportMeansTypeCode>
          <cbc:TradeServiceCode>TWL-ISL</cbc:TradeServiceCode>
          <cac:Stowage>
            <cbc:LocationID>140282</cbc:LocationID>
            <cbc:Location>On deck, aft of the bridge</cbc:Location>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SLOTLENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MTR">12.2</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:Stowage>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
            <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
            <cbc:RadioCallSignID>QBTH7</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>298702117</cbc:MMSIRegistrationID>
            <cbc:ShipsRequirements>Shore power at the container quay.</cbc:ShipsRequirements>
            <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
            <cbc:SegregatedBallastMeasure unitCode="TNE">2480</cbc:SegregatedBallastMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
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
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
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
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FreightChargeLocation>
      </cac:MainCarriageShipmentStage>
      <cac:PreCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:ShipmentStageTypeCode listID="UN/EDIFACT EDED 8051">10</cbc:ShipmentStageTypeCode>
        <cbc:ShipmentStageType>Pre-carriage transport</cbc:ShipmentStageType>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
        <cbc:CabotageIndicator>false</cbc:CabotageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Bayforth Forwarding</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">TRUCKTRAILER</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV LP 2205</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV CH 0412</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
        </cac:TransportMeans>
        <cac:DropoffTransportEvent>
          <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:15:00</cbc:OccurrenceTime>
        </cac:DropoffTransportEvent>
        <cac:FreightAllowanceCharge>
          <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
          <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
          <cbc:AllowanceChargeReason>Pre-carriage by road</cbc:AllowanceChargeReason>
          <cbc:Amount currencyID="XBL">310.00</cbc:Amount>
        </cac:FreightAllowanceCharge>
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
          <cbc:SizeTypeCode listID="ISO 6346">42G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:RefrigeratedIndicator>false</cbc:RefrigeratedIndicator>
          <cbc:GrossWeightMeasure unitCode="KGM">7856.4</cbc:GrossWeightMeasure>
          <cbc:TareWeightMeasure unitCode="KGM">3750</cbc:TareWeightMeasure>
          <cbc:StowagePositionID>140282</cbc:StowagePositionID>
          <cac:TransportEquipmentSeal>
            <cbc:ID>TWL-S-0884213</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">CARRIER</cbc:SealIssuerTypeCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:SupplierParty>
            <cac:Party>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Tidewell Ocean Lines</cbc:Name>
              </cac:PartyName>
            </cac:Party>
          </cac:SupplierParty>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000018</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 001 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000018</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000025</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 002 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000025</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000032</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 003 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000032</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000049</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 004 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000049</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000056</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 005 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000056</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000063</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 006 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000063</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000070</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 007 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000070</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000087</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 008 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000087</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000094</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 009 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000094</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000100</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 010 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000100</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000117</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 011 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000117</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000124</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 012 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000124</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000131</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 013 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000131</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000148</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 014 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000148</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000155</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 015 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000155</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000162</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 016 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000162</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000179</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 017 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000179</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000186</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 018 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000186</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000193</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 019 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000193</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000209</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 020 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000209</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000216</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 021 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000216</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000223</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 022 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000223</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000230</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 023 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000230</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000247</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">4</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 024 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000247</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095206101230000254</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>VELUMI SELANU / 025 of 025</cbc:ShippingMarks>
            <cbc:TraceID>095206101230000254</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:AttachedTransportEquipment>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV CH 0412</cbc:ID>
            <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">TE</cbc:TransportEquipmentTypeCode>
          </cac:AttachedTransportEquipment>
          <cac:Package>
            <cbc:ID schemeID="GS1 SSCC">095206101230000254</cbc:ID>
            <cbc:Quantity unitCode="EA">12</cbc:Quantity>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
            <cac:ContainingTransportEquipment>
              <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
            </cac:ContainingTransportEquipment>
          </cac:Package>
          <cac:GoodsItem>
            <cbc:ID>1</cbc:ID>
            <cbc:Description>Park benches and spare side frames</cbc:Description>
            <cac:GoodsItemContainer>
              <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
              <cbc:Quantity unitCode="EA">25</cbc:Quantity>
              <cac:TransportEquipment>
                <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
              </cac:TransportEquipment>
            </cac:GoodsItemContainer>
            <cac:ContainedGoodsItem>
              <cbc:ID>1.1</cbc:ID>
              <cbc:Description>Park benches</cbc:Description>
            </cac:ContainedGoodsItem>
            <cac:ContainedGoodsItem>
              <cbc:ID>1.2</cbc:ID>
              <cbc:Description>Spare side frames</cbc:Description>
            </cac:ContainedGoodsItem>
          </cac:GoodsItem>
          <cac:VerifiedGrossMass>
            <cbc:ID>VGM-26-0510</cbc:ID>
            <cbc:WeighingDate>2026-05-12</cbc:WeighingDate>
            <cbc:WeighingTime>15:30:00</cbc:WeighingTime>
            <cbc:WeighingMethodCode listID="IMO SOLAS">SM2</cbc:WeighingMethodCode>
            <cbc:WeighingDeviceID>LD-SCALE-03</cbc:WeighingDeviceID>
            <cbc:WeighingDeviceType>Platform scale</cbc:WeighingDeviceType>
            <cbc:GrossMassMeasure unitCode="KGM">7856.4</cbc:GrossMassMeasure>
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
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:FirstArrivalPortLocation>
      <cac:LastExitPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Port of Lumeport</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:LastExitPortLocation>
      <cac:DocumentReference>
        <cbc:ID>LD-PL-26-0134</cbc:ID>
      </cac:DocumentReference>
      <cac:InsurancePolicy>
        <cbc:ID>WS-CP-26-4471</cbc:ID>
        <cbc:InsuranceTypeCode listID="urn:ubl-examples:world:codelist:InsuranceCoverCode">ALLRISKS</cbc:InsuranceTypeCode>
        <cbc:InsuredValueAmount currencyID="XBL">59155.80</cbc:InsuredValueAmount>
        <cbc:DeductibleAmount currencyID="XBL">250.00</cbc:DeductibleAmount>
        <cbc:ExcessAmount currencyID="XBL">250.00</cbc:ExcessAmount>
        <cbc:InsurancePremiumAmount currencyID="XBL">140.00</cbc:InsurancePremiumAmount>
        <cac:BrokerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Bayforth Forwarding</cbc:Name>
          </cac:PartyName>
        </cac:BrokerParty>
        <cac:PolicyHolderParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Lumeway Distribution</cbc:Name>
          </cac:PartyName>
        </cac:PolicyHolderParty>
        <cac:BeneficiaryParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Velumi Trading</cbc:Name>
          </cac:PartyName>
        </cac:BeneficiaryParty>
        <cac:PolicyDocumentReference>
          <cbc:ID>WS-CERT-26-0884</cbc:ID>
        </cac:PolicyDocumentReference>
      </cac:InsurancePolicy>
    </cac:Consignment>
    <cac:InsurancePolicy>
      <cbc:InsuredValueAmount currencyID="XBL">59155.80</cbc:InsuredValueAmount>
      <cbc:ExcessAmount currencyID="XBL">250.00</cbc:ExcessAmount>
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
          <cbc:ID schemeID="ISO 639">en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Beacon Avenue</cbc:StreetName>
          <cbc:BuildingNumber>55</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38524</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Wavesure Cargo Insurance Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:tax">CO-1234521</cbc:CompanyID>
          <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">STT</cbc:ID>
            <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
            <cac:JurisdictionRegionAddress>
              <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:JurisdictionRegionAddress>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Wavesure Cargo Insurance Ltd</cbc:RegistrationName>
          <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411507</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">SMALL</cbc:EntitySizeCode>
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
          <cbc:Name>Cargo claims</cbc:Name>
          <cbc:JobTitle>Client relationship manager</cbc:JobTitle>
          <cbc:Department>Client services</cbc:Department>
          <cbc:Telephone>+999 2 38 2807 1507</cbc:Telephone>
          <cbc:ElectronicMail>cargo@wavesure.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411507</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:InsurerParty>
      <cac:BrokerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Bayforth Forwarding</cbc:Name>
        </cac:PartyName>
      </cac:BrokerParty>
    </cac:InsurancePolicy>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>BF-FI-26-0137</cbc:ID>
  </cac:DocumentReference>
  <cac:ExchangeRate>
    <cbc:SourceCurrencyCode listID="ISO 4217 Alpha">XBL</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode listID="ISO 4217 Alpha">XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>0.4</cbc:CalculationRate>
  </cac:ExchangeRate>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:DocumentCopyTypeCode">ORIGINAL</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">PAPER</cbc:DistributionTypeCode>
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
    <cbc:ID>TWL-SIG-BL-sea</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</BillOfLading>
```
