# Order Change: Marrowdale Sawmill to Tostara Wood Modification

*Example 7 of the flow "Modification: bench slats modified under contract (Bayvarra → Urvania)" · [Order Change in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-CHANGE-SCHEMA)*

The sawmill calls off the finished job for its buyer: where it goes, the carrier it booked, and the release number the plant hands the goods against.

[The XML file](07-OrderChange.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order-change:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order change". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **MDS-TX-26-0047**  
  The collaboration this document belongs to: the sawmill's order of thermal modification from Tostara. Marrowdale Sawmill started it and gave it this identifier, which every document of it repeats.
- `ID` = **MDS-OC-26-0034**  
  The sawmill's number for the change.
- `SalesOrderID` = **TWM-J-2526-014**  
  The plant's job number of the order changed, which the plant files the call-off under.
- `UUID` = **0381b870-e45a-5a0f-b99c-320a8aa5f632**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-24**  
  The day after Valdara ordered and the sawmill booked the truck.
- `IssueTime` = **09:00:00-01:00**  
  In the morning; in the issuer's local time, with its offset from UTC.
- `SequenceNumberID` = **1**  
  The first change of the order.
- `Note` = **Call-off of job TWM-J-2526-014: all 96 bundles for Valdara Industries, Ferrano, collected by Trasvia Haulage on Thursday 26 February.**  
  What the change adds: the delivery of the finished job.
- `LineCountNumeric` = **1**  
  One line.

### Order Reference

Inside `OrderReference`:

- `ID` = **MDS-PO-26-0047**  
  The order the call-off changes.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; as Marrowdale Sawmill gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **UL-ADR-296778** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Marrowdale Sawmill gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Marrowdale Sawmill gives it.
- `Party/PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits). As Marrowdale Sawmill gives it.
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Marrowdale Sawmill gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; as Marrowdale Sawmill gives it.
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Marrowdale Sawmill gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Marrowdale Sawmill gives it.
- `Party/Contact/Telephone` = **+999 2 7121 338 173**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Marrowdale Sawmill gives it.
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  The contact's e-mail address; as Marrowdale Sawmill gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Marrowdale Sawmill gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Tostara Wood Modification**  
  The trading name; as Tostara Wood Modification gives it.
- `Party/PostalAddress/ID` = **4160205830117402** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Tostara Wood Modification gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Party/PostalAddress/StreetName` = **Bek Stuzman Tuntrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Tostara Wood Modification gives it.
- `Party/PostalAddress/StreetName` = **Via delle Concerie** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Tostara Wood Modification gives it.
- `Party/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Tostara Wood Modification gives it.
- `Party/PostalAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `Party/PostalAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `Party/PostalAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Tostara Wood Modification gives it.
- `Party/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Tostara Wood Modification gives it.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; as Tostara Wood Modification gives it.
- `Party/Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Tostara Wood Modification gives it.
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; as Tostara Wood Modification gives it.
- `Party/Contact/Telephone` = **+999 1 041 573 2290**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Tostara Wood Modification gives it.
- `Party/Contact/ElectronicMail` = **sales@tostara.example**  
  The contact's e-mail address; as Tostara Wood Modification gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Tostara Wood Modification gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-106192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-02-26**  
  Delivered at Valdara the day it is collected.
- `RequestedDeliveryPeriod/EndDate` = **2026-02-26**  
  The same day.
- `DeliveryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `DeliveryParty/AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `DeliveryParty/PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `DeliveryParty/PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `DeliveryParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `DeliveryParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `DeliveryParty/PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `DeliveryParty/PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `DeliveryParty/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `DeliveryParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `DeliveryParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `DeliveryParty/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `DeliveryParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `DeliveryParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `DeliveryParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `DeliveryParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `DeliveryParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Valdara Industries gives it.
- `DeliveryParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `DeliveryParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Valdara Industries gives it.
- `DeliveryParty/Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `DeliveryParty/Contact/ElectronicMail` = **goodsin@valdara.example**  
  The contact's e-mail address; as Valdara Industries gives it.
- `DeliveryParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `Despatch/RequestedDespatchDate` = **2026-02-26**  
  The day Trasvia collects the bundles.
- `Despatch/ReleaseID` = **MDS-REL-26-0212**  
  The sawmill's pick-up release: the plant hands the goods only to the driver who quotes this number, for they are the sawmill's.
- `Despatch/Instructions` = **Load onto Trasvia Haulage's truck against the release number; send the despatch advice to Valdara Industries on our behalf.**  
  What the plant is to do.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **FCA** (schemeID `INCOTERMS`)  
  Free carrier at the plant: the plant loads the bundles onto the carrier the sawmill names, so the change replaces the order's ex works. The code is from the world's copy of Incoterms 2020: FCA = Free Carrier. An identifier that holds a code names the code's list in its schemeID.
- `SpecialTerms` = **Loaded at the plant's dock onto Trasvia Haulage's curtain-side trailer, four bundles to a pallet.**  
  How the handover is made.
- `LossRiskResponsibilityCode` = **BUYER** (listID `urn:ubl-examples:world:codelist:RiskResponsiblePartyCode`)  
  From loading the sawmill bears the risk. The code is from the Trade Accord's party bearing the risk list: BUYER = Buyer.
- `LossRisk` = **The goods are at the sawmill's risk from the moment they are loaded.**  
  In words.
- `DeliveryLocation/Description` = **Loading dock, Tostara Wood Modification, Conciaro**  
  Where the handover is.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The order line called off.
- `LineItem/Quantity` = **96** (unitCode `EA`)  
  All the bundles of the job.
- `LineItem/Item/Name` = **Thermal modification and finishing, bundle of 50 bench slats**  
  The job's line, named only: described in the order.
- `LineItem/Item/SellersItemIdentification/ID` = **TWM-TM-SL50**  
  The plant's number for the job's work.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<OrderChange xmlns="urn:oasis:names:specification:ubl:schema:xsd:OrderChange-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order-change:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MDS-TX-26-0047</cbc:ProfileExecutionID>
  <cbc:ID>MDS-OC-26-0034</cbc:ID>
  <cbc:SalesOrderID>TWM-J-2526-014</cbc:SalesOrderID>
  <cbc:UUID>0381b870-e45a-5a0f-b99c-320a8aa5f632</cbc:UUID>
  <cbc:IssueDate>2026-02-24</cbc:IssueDate>
  <cbc:IssueTime>09:00:00-01:00</cbc:IssueTime>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:Note>Call-off of job TWM-J-2526-014: all 96 bundles for Valdara Industries, Ferrano, collected by Trasvia Haulage on Thursday 26 February.</cbc:Note>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>MDS-PO-26-0047</cbc:ID>
  </cac:OrderReference>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-296778</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Timber Lane</cbc:StreetName>
        <cbc:BuildingNumber>7</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71202</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7121 338 173</cbc:Telephone>
        <cbc:ElectronicMail>sales@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tostara Wood Modification</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160205830117402</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Tuntrir</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Concerie</cbc:StreetName>
        <cbc:BuildingNumber>9</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
        <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
        <cbc:PostalZone>4190</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Sales coordinator</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 041 573 2290</cbc:Telephone>
        <cbc:ElectronicMail>sales@tostara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-106192</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-02-26</cbc:StartDate>
      <cbc:EndDate>2026-02-26</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@valdara.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
    </cac:DeliveryParty>
    <cac:Despatch>
      <cbc:RequestedDespatchDate>2026-02-26</cbc:RequestedDespatchDate>
      <cbc:ReleaseID>MDS-REL-26-0212</cbc:ReleaseID>
      <cbc:Instructions>Load onto Trasvia Haulage's truck against the release number; send the despatch advice to Valdara Industries on our behalf.</cbc:Instructions>
    </cac:Despatch>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">FCA</cbc:ID>
    <cbc:SpecialTerms>Loaded at the plant's dock onto Trasvia Haulage's curtain-side trailer, four bundles to a pallet.</cbc:SpecialTerms>
    <cbc:LossRiskResponsibilityCode listID="urn:ubl-examples:world:codelist:RiskResponsiblePartyCode">BUYER</cbc:LossRiskResponsibilityCode>
    <cbc:LossRisk>The goods are at the sawmill's risk from the moment they are loaded.</cbc:LossRisk>
    <cac:DeliveryLocation>
      <cbc:Description>Loading dock, Tostara Wood Modification, Conciaro</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Thermal modification and finishing, bundle of 50 bench slats</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>TWM-TM-SL50</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</OrderChange>
```
