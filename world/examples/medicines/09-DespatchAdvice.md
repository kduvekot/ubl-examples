# Despatch Advice: Quillmoor Pharma Distribution to Selanu General Hospital

*Example 9 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Despatch Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DESPATCH-ADVICE-SCHEMA)*

The wholesaler announces the goods to the hospital pharmacy with the lots and their expiry dates and the generator's serial number and reference time.

[The XML file](09-DespatchAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:despatch-advice:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Despatch advice". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:despatch-receipt:1.0**  
  The Trade Accord's process profile the document belongs to: despatch and receipt, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **SGH/2026/1099**  
  The collaboration this document belongs to: the hospital's order of medicines from Quillmoor. Selanu General Hospital started it and gave it this identifier, which every document of it repeats.
- `ID` = **QLM-DA-26-4074**  
  The despatching party's number.
- `UUID` = **db7de944-bab2-50cb-b191-099b052b0ddb**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-15**  
  Sent when the last of the goods, the generator, left the warehouse for the airport.
- `IssueTime` = **05:10:00-01:00**  
  When the wholesaler's van left with the generator; in the issuer's local time, with its offset from UTC.
- `DespatchAdviceTypeCode` = **DELIVERY** (listID `urn:ubl-examples:world:codelist:DespatchAdviceTypeCode`)  
  Advice of goods despatched for delivery. The code is from the Trade Accord's despatch advice type list: DELIVERY = Delivery.
- `Note` = **Please check the goods on arrival and report any damage on the air waybill.**  
  What the receiver should do; the note names the transport document the flow uses.
- `LineCountNumeric` = **4**  
  The number of lines.

### Order Reference

Inside `OrderReference`:

- `ID` = **SGH/2026/1100**  
  The order this despatch fulfils.

### Despatch Supplier Party

Inside `DespatchSupplierParty`:

- `Party/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Quillmoor Pharma Distribution gives it.
- `Party/PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; as Quillmoor Pharma Distribution gives it.
- `Party/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Party/PostalAddress/ID` = **LUM-ADR-718264** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Party/PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/BuildingNumber` = **40**  
  Building number of the postal address. As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). As Quillmoor Pharma Distribution gives it.
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Party/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Quillmoor Pharma Distribution gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Party/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Quillmoor Pharma Distribution gives it.
- `Party/Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Quillmoor Pharma Distribution gives it.
- `Party/Contact/ElectronicMail` = **dispatch@quillmoor.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Quillmoor Pharma Distribution gives it.
- `Party/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Quillmoor Pharma Distribution gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20413425** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Customer Party

Inside `DeliveryCustomerParty`:

- `Party/PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Selanu General Hospital gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu General Hospital**  
  The trading name; as Selanu General Hospital gives it.
- `Party/PostalAddress/ID` = **52968014** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu General Hospital gives it.
- `Party/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Party/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Party/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu General Hospital gives it.
- `Party/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu General Hospital gives it.
- `Party/PostalAddress/BuildingNumber` = **81**  
  Building number of the postal address. As Selanu General Hospital gives it.
- `Party/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu General Hospital gives it.
- `Party/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu General Hospital gives it.
- `Party/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Party/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/Contact/Name` = **Pharmacy goods-in**  
  The party's pharmacy goods-in desk: the desk for its role in this document (it receives the goods); as Selanu General Hospital gives it.
- `Party/Contact/JobTitle` = **Pharmacy technician**  
  The job of the person who answers at the desk; as Selanu General Hospital gives it.
- `Party/Contact/Department` = **Pharmacy**  
  The department the desk belongs to; as Selanu General Hospital gives it.
- `Party/Contact/Telephone` = **+999 3 726 8840**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu General Hospital gives it.
- `Party/Contact/ElectronicMail` = **pharmacy-goodsin@selanu-hospital.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu General Hospital gives it.
- `Party/Contact/Note` = **Weekdays 07:30–17:00**  
  When the desk can be reached; as Selanu General Hospital gives it.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:GOV-317** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Selanu General Hospital gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu General Hospital**  
  The same party as at DeliveryCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Quillmoor Pharma Distribution**  
  The same party as at DespatchSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **QLM-SH-26-3980**  
  The despatching party's shipment number.
- `Consignment/ID` = **QLM-CS-26-3980**  
  The consignment the goods travel in, as numbered when the transport was booked.
- `Consignment/GrossWeightMeasure` = **101.1** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The goods with their packaging, with the dry ice and the frozen vaccine's box, as on the air waybill.
- `Consignment/CarrierParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Kelaro Air Cargo gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/ID` = **58930746** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. As Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Cargo operations**  
  The party's cargo operations desk: the desk for its role in this document (it carries or handles the goods); as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/JobTitle` = **Load controller**  
  The job of the person who answers at the desk; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/Telephone` = **+999 3 721 1044**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/ElectronicMail` = **cargoops@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Kelaro Air Cargo gives it.
- `Consignment/CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Kelaro Air Cargo gives it.
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-06-15**  
  Expected after the usual transit by air.
- `Delivery/EstimatedDeliveryPeriod/EndDate` = **2026-06-15**  
  The same day.
- `Delivery/Despatch/ActualDespatchDate` = **2026-06-15**  
  The goods left on the day of this advice.

### Despatch Line

Inside `DespatchLine`:

- `ID` = **1**  
  The line number.
- `Note` = **3,000 doses, ten to a pack, for the island's winter influenza campaign, which starts on 22 June.**  
  The line as the order put it.
- `DeliveredQuantity` = **300** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **1**  
  The order line this line fulfils.
- `Item/Description` = **Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `Item/Name` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **QLM-VAC-1102**  
  The seller's own item number; as Quillmoor Pharma Distribution describes the item.
- `Item/ManufacturersItemIdentification/ID` = **NLB-FLU-S26-10**  
  The item number of the maker, Nilavar Biologics: the reseller sells the maker's item on.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **NLB-FLU26S-0412**  
  The maker's lot, as its certificate of release names it; a recall names the lot.
- `Item/ItemInstance/LotIdentification/ExpiryDate` = **2027-02-28**  
  The southern hemisphere formula of 2026 is used up by the next winter: the lot expires at the end of February 2027.
- `ID` = **2**  
  The line number.
- `Note` = **The hospital pharmacy's insulin for the next two months, for its wards and its outpatients.**  
  The line as the order put it.
- `DeliveredQuantity` = **240** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **2**  
  The order line this line fulfils.
- `Item/Description` = **Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.**  
  The seller's description.
- `Item/Name` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **QLM-INS-0310**  
  The seller's own item number; as Quillmoor Pharma Distribution describes the item.
- `Item/ManufacturersItemIdentification/ID` = **NLB-INS-R100-10**  
  The item number of the maker, Nilavar Biologics: the reseller sells the maker's item on.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **NLB-INS-2603-118**  
  The maker's lot, as its certificate of release names it; a recall names the lot.
- `Item/ItemInstance/LotIdentification/ExpiryDate` = **2028-02-29**  
  Unopened at 2 to 8 °C, human insulin keeps for two years: the lot of March 2026 expires at the end of February 2028.
- `ID` = **3**  
  The line number.
- `Note` = **Forty doses for the children's vaccination programme of July.**  
  The line as the order put it.
- `DeliveredQuantity` = **40** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **3**  
  The order line this line fulfils.
- `Item/Description` = **Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.**  
  The seller's description.
- `Item/Name` = **Varicella vaccine, live, frozen, single dose**  
  The item's short name.
- `Item/SellersItemIdentification/ID` = **QLM-VAC-2410**  
  The seller's own item number; as Quillmoor Pharma Distribution describes the item.
- `Item/ManufacturersItemIdentification/ID` = **NLB-VZV-1**  
  The item number of the maker, Nilavar Biologics: the reseller sells the maker's item on.
- `Item/ItemInstance/LotIdentification/LotNumberID` = **NLB-VZV-2602-031**  
  The maker's lot, as its certificate of release names it; a recall names the lot.
- `Item/ItemInstance/LotIdentification/ExpiryDate` = **2027-08-31**  
  A frozen live vaccine keeps 18 months at -15 °C or colder: the lot of February 2026 expires at the end of August 2027.
- `ID` = **4**  
  The line number.
- `Note` = **Next week's generator for the nuclear medicine unit: the one in use is spent by Sunday.**  
  The line as the order put it.
- `DeliveredQuantity` = **1** (unitCode `EA`)  
  What was despatched.
- `OrderLineReference/LineID` = **4**  
  The order line this line fulfils.
- `Item/Description` = **A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.**  
  The seller's description.
- `Item/Name` = **Technetium-99m generator, 20 GBq**  
  The item's short name.
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **QLM-RAD-0020**  
  The seller's own item number; as Quillmoor Pharma Distribution describes the item.
- `Item/ManufacturersItemIdentification/ID` = **HVI-TCG-20**  
  The item number of the maker, Haarvliet Isotopes: the reseller sells the maker's item on.
- `Item/HazardousItem/ID` = **HVI-TCG-20-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/AdditionalInformation` = **Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h**  
  What the shipper adds about handling.
- `Item/HazardousItem/UNDGCode` = **2915** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2915 = Radioactive material, Type A package, non-special form, non fissile or fissile-excepted.
- `Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for gases, lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **163** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 163 = Radioactive Materials (Low to High Level Radiation).
- `Item/HazardousItem/ProperShippingName` = **Radioactive material, Type A package, non-special form, non fissile or fissile-excepted**  
  The proper shipping name of the UN entry; the build checks that UN number, name and class agree with the Dangerous Goods List.
- `Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `Item/HazardousItem/MarkingID` = **UN2915**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `Item/HazardousItem/RadioactiveMaterial/Name` = **Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)**  
  The radionuclide and the maximum activity during transport, which the transport document must state in becquerels (IAEA SSR-6 para 546): UBL has no element for the activity of contents that are not fissile, so the name carries it. The activity is the generator's at acceptance at the Lumeport cargo terminal, the highest it has on the way, as Mo-99 decays; the A2 value of Mo-99 allows up to 600 GBq in a Type A package.
- `Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.**  
  The physical and chemical form: not special form, so the A2 value applies.
- `Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **1.5**  
  The transport index of the package: the highest dose rate at 1 m in mSv/h times 100, rounded up to the first decimal (IAEA SSR-6 para 523); above 1, so the package carries the Category III-YELLOW label (para 529, the higher category winning over the surface rate).
- `Item/ItemInstance/SerialID` = **HVI-TCG20-26-0137**  
  The generator's serial number, from its maker: each generator is traced from its filling to its return.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Nominal activity**  
  The generator's size: its Mo-99 at the reference time, the figure the item is sold by.
- `Item/ItemInstance/AdditionalItemProperty/ValueQuantity` = **20** (unitCode `GBQ`)  
  20 GBq.
- `Item/ItemInstance/AdditionalItemProperty/Name` = **Reference time**  
  When the generator holds its nominal activity: European generators are pre-calibrated to a time some days after delivery, so that the hospital has its nominal activity at the end of its week.
- `Item/ItemInstance/AdditionalItemProperty/Value` = **2026-06-21T12:00:00+00:00**  
  Sunday 21 June at 12:00 UTC, six days after delivery.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DespatchAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:DespatchAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:despatch-advice:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:despatch-receipt:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SGH/2026/1099</cbc:ProfileExecutionID>
  <cbc:ID>QLM-DA-26-4074</cbc:ID>
  <cbc:UUID>db7de944-bab2-50cb-b191-099b052b0ddb</cbc:UUID>
  <cbc:IssueDate>2026-06-15</cbc:IssueDate>
  <cbc:IssueTime>05:10:00-01:00</cbc:IssueTime>
  <cbc:DespatchAdviceTypeCode listID="urn:ubl-examples:world:codelist:DespatchAdviceTypeCode">DELIVERY</cbc:DespatchAdviceTypeCode>
  <cbc:Note>Please check the goods on arrival and report any damage on the air waybill.</cbc:Note>
  <cbc:LineCountNumeric>4</cbc:LineCountNumeric>
  <cac:OrderReference>
    <cbc:ID>SGH/2026/1100</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="GS1 GLN">9524910900003</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID schemeID="ISO 639">en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-718264</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Airport Road</cbc:StreetName>
        <cbc:BuildingNumber>40</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38528</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Dispatch office</cbc:Name>
        <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 2 38 6047 1582</cbc:Telephone>
        <cbc:ElectronicMail>dispatch@quillmoor.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20413425</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DespatchSupplierParty>
  <cac:DeliveryCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu General Hospital</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">52968014</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>81</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Pharmacy goods-in</cbc:Name>
        <cbc:JobTitle>Pharmacy technician</cbc:JobTitle>
        <cbc:Department>Pharmacy</cbc:Department>
        <cbc:Telephone>+999 3 726 8840</cbc:Telephone>
        <cbc:ElectronicMail>pharmacy-goodsin@selanu-hospital.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:30–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-317</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:DeliveryCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu General Hospital</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Shipment>
    <cbc:ID>QLM-SH-26-3980</cbc:ID>
    <cac:Consignment>
      <cbc:ID>QLM-CS-26-3980</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">101.1</cbc:GrossWeightMeasure>
      <cac:CarrierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Kelaro Air Cargo</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">58930746</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Airfield Road</cbc:StreetName>
          <cbc:BuildingNumber>46</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Kefalasa</cbc:CityName>
          <cbc:CityName languageID="en-XL">Lintwell</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Cargo operations</cbc:Name>
          <cbc:JobTitle>Load controller</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 3 721 1044</cbc:Telephone>
          <cbc:ElectronicMail>cargoops@kelaro.example</cbc:ElectronicMail>
          <cbc:Note>Every day 06:00–22:00</cbc:Note>
        </cac:Contact>
      </cac:CarrierParty>
    </cac:Consignment>
    <cac:Delivery>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-06-15</cbc:StartDate>
        <cbc:EndDate>2026-06-15</cbc:EndDate>
      </cac:EstimatedDeliveryPeriod>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-06-15</cbc:ActualDespatchDate>
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:DespatchLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Note>3,000 doses, ten to a pack, for the island's winter influenza campaign, which starts on 22 June.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">300</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Seasonal influenza vaccine, inactivated split virion, of the southern hemisphere formula for 2026: a pack of ten prefilled syringes of 0.5 ml, one dose each. Store at 2 to 8 °C; do not freeze.</cbc:Description>
      <cbc:Name>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>QLM-VAC-1102</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>NLB-FLU-S26-10</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:ItemInstance>
        <cac:LotIdentification>
          <cbc:LotNumberID>NLB-FLU26S-0412</cbc:LotNumberID>
          <cbc:ExpiryDate>2027-02-28</cbc:ExpiryDate>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>The hospital pharmacy's insulin for the next two months, for its wards and its outpatients.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">240</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Soluble human insulin, 100 international units per ml, in a vial of 10 ml. Store unopened at 2 to 8 °C; do not freeze.</cbc:Description>
      <cbc:Name>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>QLM-INS-0310</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>NLB-INS-R100-10</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:ItemInstance>
        <cac:LotIdentification>
          <cbc:LotNumberID>NLB-INS-2603-118</cbc:LotNumberID>
          <cbc:ExpiryDate>2028-02-29</cbc:ExpiryDate>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>3</cbc:ID>
    <cbc:Note>Forty doses for the children's vaccination programme of July.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">40</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>Live attenuated varicella vaccine, freeze-dried, one dose in a vial with its diluent. Store frozen at -50 to -15 °C until it is used.</cbc:Description>
      <cbc:Name>Varicella vaccine, live, frozen, single dose</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>QLM-VAC-2410</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>NLB-VZV-1</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:ItemInstance>
        <cac:LotIdentification>
          <cbc:LotNumberID>NLB-VZV-2602-031</cbc:LotNumberID>
          <cbc:ExpiryDate>2027-08-31</cbc:ExpiryDate>
        </cac:LotIdentification>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
  <cac:DespatchLine>
    <cbc:ID>4</cbc:ID>
    <cbc:Note>Next week's generator for the nuclear medicine unit: the one in use is spent by Sunday.</cbc:Note>
    <cbc:DeliveredQuantity unitCode="EA">1</cbc:DeliveredQuantity>
    <cac:OrderLineReference>
      <cbc:LineID>4</cbc:LineID>
    </cac:OrderLineReference>
    <cac:Item>
      <cbc:Description>A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration): a column of Mo-99 in a shielded housing, from which the hospital elutes sodium pertechnetate (Tc-99m) every morning for a week.</cbc:Description>
      <cbc:Name>Technetium-99m generator, 20 GBq</cbc:Name>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:SellersItemIdentification>
        <cbc:ID>QLM-RAD-0020</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>HVI-TCG-20</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:HazardousItem>
        <cbc:ID>HVI-TCG-20-DG</cbc:ID>
        <cbc:AdditionalInformation>Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h</cbc:AdditionalInformation>
        <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2915</cbc:UNDGCode>
        <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
        <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
        <cbc:MedicalFirstAidGuideCode listID="ERG 2024">163</cbc:MedicalFirstAidGuideCode>
        <cbc:ProperShippingName>Radioactive material, Type A package, non-special form, non fissile or fissile-excepted</cbc:ProperShippingName>
        <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
        <cbc:MarkingID>UN2915</cbc:MarkingID>
        <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
        <cac:RadioactiveMaterial>
          <cbc:Name>Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)</cbc:Name>
          <cbc:SpecialFormDescription>Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.</cbc:SpecialFormDescription>
          <cbc:TransportIndexNumeric>1.5</cbc:TransportIndexNumeric>
        </cac:RadioactiveMaterial>
      </cac:HazardousItem>
      <cac:ItemInstance>
        <cbc:SerialID>HVI-TCG20-26-0137</cbc:SerialID>
        <cac:AdditionalItemProperty>
          <cbc:Name>Nominal activity</cbc:Name>
          <cbc:ValueQuantity unitCode="GBQ">20</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
        <cac:AdditionalItemProperty>
          <cbc:Name>Reference time</cbc:Name>
          <cbc:Value>2026-06-21T12:00:00+00:00</cbc:Value>
        </cac:AdditionalItemProperty>
      </cac:ItemInstance>
    </cac:Item>
  </cac:DespatchLine>
</DespatchAdvice>
```
