# Despatch Advice: Castrano Logistics to Lumeport Public Works Department

*Example 26 of the flow "A public tender (Bayvarra)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The manufacturer's 3PL despatches the call-off and names the carrier.

[The XML file](26-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **CL-DA-26-0212**  
  The despatching party's number.
- `IssueDate` = **2026-03-30**  
  The day the call-off left the 3PL.

### Order Reference

Inside `OrderReference`:

- `ID` = **LPWD-PO-26-0211**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/WebsiteURI` = **https://www.castrano.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Castrano Logistics (world/parties.json).
- `Party/IndustryClassificationCode` = **5210** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Castrano Logistics (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Castrano Logistics (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Castrano Logistics**  
  The trading name; identity of Castrano Logistics (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via del Magazzino**  
  Street of the postal address. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **24**  
  Building number of the postal address. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Castrano Logistics (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Castrano Logistics SRU**  
  The name under which the party is registered for value added tax; identity of Castrano Logistics (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007308887**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Castrano Logistics (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Castrano Logistics SRU**  
  The name under which the party is registered, with its legal form; identity of Castrano Logistics (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104411**  
  Number in the Commercial register of Urvania; identity of Castrano Logistics (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Castrano Logistics (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Castrano Logistics (world/parties.json).
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Party/PartyLegalEntity/ShareholderParty/ParticipationPercent` = **100**  
  The share it holds in this company; identity of Castrano Logistics (world/parties.json).
- `Party/PartyLegalEntity/ShareholderParty/Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyLegalEntity/ShareholderParty/Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/Contact/Name` = **Warehouse office**  
  The desk that handles this document; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4130 4411**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/ElectronicMail` = **warehouse@castrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Castrano Logistics (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Castrano Logistics (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Castrano Logistics (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-410548** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The trading name; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **6**  
  Building number of the postal address. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/InhouseMail` = **Room 2.14**  
  The internal mail code of the procurement office. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/Department` = **Procurement office**  
  The department the post is for. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/MarkAttention` = **Head of procurement**  
  For the attention of the head of procurement. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38517**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeport Public Works Department (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered for state sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-0900002**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/ExemptionReason` = **Public bodies are exempt from the state sales tax**  
  Why purchases by this party carry no sales tax; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeport Public Works Department**  
  The name under which the party is registered, with its legal form; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410548**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Public Works Department (world/parties.json).
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Party/Contact/Name` = **Procurement office**  
  The desk that handles this document; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 3851 0548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/ElectronicMail` = **procurement@publicworks-lumeport.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Public Works Department (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeport Public Works Department (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Public Works Department (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeport Public Works Department**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **CL-SH-26-0213**  
  The despatching party's shipment number.
- `GrossWeightMeasure` = **1660** (unitCode `KGM`)  
  The gross weight loaded.
- `Consignment/ID` = **CL-CS-26-0214**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/CarrierParty/WebsiteURI` = **https://www.trasvia.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/IndustryClassificationCode` = **4923** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/CarrierParty/Language/Name` = **English**  
  The language's name.
- `Consignment/CarrierParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti**  
  Street of the postal address. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/PartyTaxScheme/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered for value added tax; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyTaxScheme/CompanyID` = **XU007337656**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationName` = **Trasvia Haulage SRU**  
  The name under which the party is registered, with its legal form; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104822**  
  Number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Consignment/CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Consignment/CarrierParty/Contact/Name` = **Planning desk**  
  The desk that handles this document; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 4160 4822**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyAuthorization/Purpose` = **International road haulage**  
  What the authority has authorized the party to do; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyAuthorization/ValidityPeriod/EndDate` = **2030-06-30**  
  The authorization expires on this date.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/ID` = **XU-HAUL-2020-0877**  
  The number of the permit.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateTypeCode` = **Permit**  
  A permit issued by an authority of the party's country.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Operating permit**  
  The kind of certificate, in words.
- `Consignment/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Trasvia Haulage (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `DeliveredQuantity` = **40** (unitCode `H87`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.**  
  The seller's description; item bench-serra of Valdara Industries (world/items.json).
- `Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>CL-DA-26-0212</cbc:ID>
  <cbc:IssueDate>2026-03-30</cbc:IssueDate>
  <cac:OrderReference>
    <cbc:ID>LPWD-PO-26-0211</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.castrano.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">5210</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Castrano Logistics</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via del Magazzino</cbc:StreetName>
        <cbc:BuildingNumber>24</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4130</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Castrano Logistics SRU</cbc:RegistrationName>
        <cbc:CompanyID>XU007308887</cbc:CompanyID>
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
        <cbc:RegistrationName>Castrano Logistics SRU</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104411</cbc:CompanyID>
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
        <cac:ShareholderParty>
          <cbc:ParticipationPercent>100</cbc:ParticipationPercent>
          <cac:Party>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Valdara Industries</cbc:Name>
            </cac:PartyName>
          </cac:Party>
        </cac:ShareholderParty>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Warehouse office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4130 4411</cbc:Telephone>
        <cbc:ElectronicMail>warehouse@castrano.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410548</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Civic Square</cbc:StreetName>
        <cbc:BuildingNumber>6</cbc:BuildingNumber>
        <cbc:InhouseMail>Room 2.14</cbc:InhouseMail>
        <cbc:Department>Procurement office</cbc:Department>
        <cbc:MarkAttention>Head of procurement</cbc:MarkAttention>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38517</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>CO-0900002</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cbc:ExemptionReason>Public bodies are exempt from the state sales tax</cbc:ExemptionReason>
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
        <cbc:RegistrationName>Lumeport Public Works Department</cbc:RegistrationName>
        <cbc:CompanyID>20410548</cbc:CompanyID>
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
        <cbc:Name>Procurement office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 3851 0548</cbc:Telephone>
        <cbc:ElectronicMail>procurement@publicworks-lumeport.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410548</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
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
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
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
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4120 4274</cbc:Telephone>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        <cac:OtherCommunication>
          <cbc:ChannelCode>AL</cbc:ChannelCode>
          <cbc:Value>+999 1 7000 4274</cbc:Value>
        </cac:OtherCommunication>
      </cac:Contact>
      <cac:ServiceProviderParty>
        <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
        <cac:Party>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Castrano Logistics</cbc:Name>
          </cac:PartyName>
        </cac:Party>
      </cac:ServiceProviderParty>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>CL-SH-26-0213</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">1660</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>CL-CS-26-0214</cbc:ID>
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
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DeliveredQuantity unitCode="H87">40</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
