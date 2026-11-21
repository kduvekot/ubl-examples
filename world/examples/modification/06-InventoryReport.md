# Inventory Report: Tostara Wood Modification to Marrowdale Sawmill

*Example 6 of the flow "Modification: bench slats modified under contract (Bayvarra → Urvania)" · [Inventory Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVENTORY-REPORT-SCHEMA)*

The plant reports the sawmill's goods in its store: the first charge ready, the second ready a few days later.

[The XML file](06-InventoryReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:inventory-report:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Inventory report". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:collaboration:1.0**  
  The Trade Accord's process profile the document belongs to: collaborative planning, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **MDS-TX-26-0047**  
  The collaboration this document belongs to: the sawmill's order of thermal modification from Tostara. Marrowdale Sawmill started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0004**  
  The plant's stock report number.
- `UUID` = **3b5324eb-8267-5d6b-baac-5d4d633644b7**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-01-30**  
  The plant's stock report to the owners of the goods it holds, each Friday.
- `IssueTime` = **14:00:00-01:00**  
  After the week's count, in the afternoon; in the issuer's local time, with its offset from UTC.
- `Note` = **Job TWM-J-2526-014. Both loads of blanks are modified, and no blank is left over; the first charge is in store, the second is being planed and sealed.**  
  What the report covers: every blank has been through the kiln, and how far each charge is.

### Inventory Period

Inside `InventoryPeriod`:

- `StartDate` = **2026-01-26**  
  The week.
- `EndDate` = **2026-01-30**  
  Its end.

### Document Reference

Inside `DocumentReference`:

- `ID` = **MDS-PO-26-0047**  
  The sawmill's order for the job.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: MDS-PO-26-0047 is the example modification/01, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.

### Retailer Customer Party

Inside `RetailerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Tostara Wood Modification**  
  The trading name; as Tostara Wood Modification gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XU = Urvanian English.
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
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0425 and 5 digits (9); no area code is the start of another. Mobiles start with 3 and have 10 digits. As Tostara Wood Modification gives it.
- `Party/Contact/ElectronicMail` = **sales@tostara.example**  
  The contact's e-mail address; as Tostara Wood Modification gives it.
- `Party/Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Tostara Wood Modification gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-106192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Inventory Reporting Party

Inside `InventoryReportingParty`:

- `PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at RetailerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tostara Wood Modification**  
  The same party as at RetailerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; as Marrowdale Sawmill gives it.
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
- `Party/Contact/Telephone` = **+999 2 5121 338 173**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Marrowdale Sawmill gives it.
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  The contact's e-mail address; as Marrowdale Sawmill gives it.
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Marrowdale Sawmill gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Inventory Report Line

Inside `InventoryReportLine`:

- `ID` = **1**  
  Kiln charge 1, from the first load of blanks.
- `Note` = **Kiln charge 1, from the first load of blanks (lot MDS-BL26-0109), output lot MDS-L26-0119: modified, planed, sealed and bundled.**  
  What the line holds.
- `Quantity` = **48** (unitCode `EA`)  
  The bundles of the charge.
- `AvailabilityStatusCode` = **AVAILABLE** (listID `urn:ubl-examples:world:codelist:AvailabilityStatusCode`)  
  Finished and in store: available now, so no date. The code is from the Trade Accord's availability status list: AVAILABLE = Available.
- `Item/Description` = **Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.**  
  The seller's description.
- `Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; as Marrowdale Sawmill describes the item.
- `Item/Name` = **Bench slat 1800, bundle of 50**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **MDS-SL-1800-50**  
  The seller's own item number; as Marrowdale Sawmill describes the item.
- `InventoryLocation/Name` = **Store bay 3, Tostara Wood Modification, Conciaro**  
  Where the sawmill's bundles stand, kept apart as its goods.
- `ID` = **2**  
  Kiln charge 2, from the second load of blanks.
- `Note` = **Kiln charge 2, from the second load of blanks (lot MDS-BL26-0116), output lot MDS-L26-0126: modified; still being planed and sealed, so the 48 bundles are the expected output, available from 4 February.**  
  What the line holds.
- `Quantity` = **48** (unitCode `EA`)  
  The bundles the charge will give: stock that will be in store once bundled.
- `AvailabilityDate` = **2026-02-04**  
  Available from Wednesday 4 February, when its planing, sealing and bundling are finished.
- `Item/Description` = **Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.**  
  The seller's description.
- `Item/PackQuantity` = **1** (unitCode `EA`)  
  One pack of this item.
- `Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; as Marrowdale Sawmill describes the item.
- `Item/Name` = **Bench slat 1800, bundle of 50**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **MDS-SL-1800-50**  
  The seller's own item number; as Marrowdale Sawmill describes the item.
- `InventoryLocation/Name` = **Planing hall, Tostara Wood Modification, Conciaro**  
  Where the slats are now.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<InventoryReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:InventoryReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:inventory-report:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:collaboration:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MDS-TX-26-0047</cbc:ProfileExecutionID>
  <cbc:ID>26-0004</cbc:ID>
  <cbc:UUID>3b5324eb-8267-5d6b-baac-5d4d633644b7</cbc:UUID>
  <cbc:IssueDate>2026-01-30</cbc:IssueDate>
  <cbc:IssueTime>14:00:00-01:00</cbc:IssueTime>
  <cbc:Note>Job TWM-J-2526-014. Both loads of blanks are modified, and no blank is left over; the first charge is in store, the second is being planed and sealed.</cbc:Note>
  <cac:InventoryPeriod>
    <cbc:StartDate>2026-01-26</cbc:StartDate>
    <cbc:EndDate>2026-01-30</cbc:EndDate>
  </cac:InventoryPeriod>
  <cac:DocumentReference>
    <cbc:ID>MDS-PO-26-0047</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:RetailerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tostara Wood Modification</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
      </cac:Language>
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
  </cac:RetailerCustomerParty>
  <cac:InventoryReportingParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tostara Wood Modification</cbc:Name>
    </cac:PartyName>
  </cac:InventoryReportingParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
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
        <cbc:Telephone>+999 2 5121 338 173</cbc:Telephone>
        <cbc:ElectronicMail>sales@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:InventoryReportLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>Kiln charge 1, from the first load of blanks (lot MDS-BL26-0109), output lot MDS-L26-0119: modified, planed, sealed and bundled.</cbc:Note>
    <cbc:Quantity unitCode="EA">48</cbc:Quantity>
    <cbc:AvailabilityStatusCode listID="urn:ubl-examples:world:codelist:AvailabilityStatusCode">AVAILABLE</cbc:AvailabilityStatusCode>
    <cac:Item>
      <cbc:Description>Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.</cbc:Description>
      <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
      <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
      <cbc:Name>Bench slat 1800, bundle of 50</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>MDS-SL-1800-50</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
    <cac:InventoryLocation>
      <cbc:Name>Store bay 3, Tostara Wood Modification, Conciaro</cbc:Name>
    </cac:InventoryLocation>
  </cac:InventoryReportLine>
  <cac:InventoryReportLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Kiln charge 2, from the second load of blanks (lot MDS-BL26-0116), output lot MDS-L26-0126: modified; still being planed and sealed, so the 48 bundles are the expected output, available from 4 February.</cbc:Note>
    <cbc:Quantity unitCode="EA">48</cbc:Quantity>
    <cbc:AvailabilityDate>2026-02-04</cbc:AvailabilityDate>
    <cac:Item>
      <cbc:Description>Bundle of 50 bench slats of thermally modified ash, the sawmill's slat MDS-SL-1800 (Valdara's part VI-R-SL1800), 1800 × 95 × 45 mm; five across and ten high, strapped.</cbc:Description>
      <cbc:PackQuantity unitCode="EA">1</cbc:PackQuantity>
      <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
      <cbc:Name>Bench slat 1800, bundle of 50</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>MDS-SL-1800-50</cbc:ID>
      </cac:SellersItemIdentification>
    </cac:Item>
    <cac:InventoryLocation>
      <cbc:Name>Planing hall, Tostara Wood Modification, Conciaro</cbc:Name>
    </cac:InventoryLocation>
  </cac:InventoryReportLine>
</InventoryReport>
```
