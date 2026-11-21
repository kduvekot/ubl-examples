# Retail Event: Brightmarket Stores to Lumeway Distribution

*Example 6 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Retail Event in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-RETAIL-EVENT-SCHEMA)*

The reopening of the home and garden department on 11 May, with two weeks at 10 % off, will lift demand; the distributor needs to know before it orders from the manufacturer.

[The XML file](06-RetailEvent.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:retail-event:1.0#compliant#urn:ubl-examples:world:community:retail:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Retail event"; the community specification "Retail community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:collaboration:1.0**  
  The Trade Accord's process profile the document belongs to: collaborative planning, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900339162**  
  The collaboration this document belongs to: the store's forecast, promotion and stock report for Lumeway. Brightmarket Stores started it and gave it this identifier, which every document of it repeats.
- `ID` = **6500016959**  
  The store's event number.
- `UUID` = **31926ddb-5dfd-59d6-bb1b-86b3926753e7**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-22**  
  Announced with the forecast.
- `IssueTime` = **11:13:00-01:00**  
  Issued a few minutes after the last thing of its day that it reports, cites or answers, in the sender's local time, with its offset from UTC.
- `Note` = **Agreed with the distributor's sales team.**  
  Status of the agreement.
- `RetailEventName` = **Reopening of the home and garden department**  
  The name of the event: the department reopens after its renovation.
- `RetailEventStatusCode` = **CONFIRMED** (listID `urn:ubl-examples:world:codelist:RetailEventStatusCode`)  
  The reopening and its promotion are decided, not only planned. The code is from the Trade Accord's retail event status list: CONFIRMED = Confirmed.
- `SellerEventID` = **LMW-PROMO-26-03**  
  The distributor's number for the promotion.
- `BuyerEventID` = **BM-REOPEN-HG-26**  
  The store's number for the reopening.
- `Description` = **After its renovation the home and garden department of the Lumeport store reopens on Monday 11 May: ten per cent off the department's range for two weeks, the Elderwick Marrow line excepted.**  
  What the event is (the promotion does not apply to the Marrow line).

### Period

Inside `Period`:

- `StartDate` = **2026-05-11**  
  The promotion starts in three weeks.
- `EndDate` = **2026-05-24**  
  It lasts two weeks.

### Signature

Inside `Signature`:

- `ID` = **BM-SIG-26-0422E**  
  The store's seal.
- `SignatoryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Brightmarket Stores gives it.
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; as Brightmarket Stores gives it.
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; as Brightmarket Stores gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-579130** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Brightmarket Stores gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. As Brightmarket Stores gives it.
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. As Brightmarket Stores gives it.
- `PostalAddress/CitySubdivisionName` = **Old Town**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Brightmarket Stores gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Brightmarket Stores gives it.
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). As Brightmarket Stores gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Brightmarket Stores gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
- `Contact/Name` = **Buying office**  
  The party's main desk, which handles this document; as Brightmarket Stores gives it.
- `Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; as Brightmarket Stores gives it.
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Brightmarket Stores gives it.
- `Contact/Telephone` = **+999 2 38 4609 7100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Brightmarket Stores gives it.
- `Contact/ElectronicMail` = **buying@brightmarket.example**  
  The contact's e-mail address; as Brightmarket Stores gives it.
- `Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Brightmarket Stores gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Brightmarket Stores gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Sales office**  
  The party's sales office desk: the desk for its role in this document (it sells); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Sales coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 5121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **sales@lumeway.example**  
  The contact's e-mail address; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Event Comment

Inside `EventComment`:

- `Comment` = **Floor space for 12 benches at the entrance of the renovated department.**  
  What the store prepares.
- `IssueDate` = **2026-04-22**  
  Written with the announcement.
- `IssueTime` = **11:00:00-01:00**  
  At that time; in the issuer's local time, with its offset from UTC.

### Promotional Event

Inside `PromotionalEvent`:

- `PromotionalEventTypeCode` = **OPENING** (listID `urn:ubl-examples:world:codelist:PromotionalEventTypeCode`)  
  An opening promotion: the reopening of the department. The code is from the Trade Accord's promotional event type list: OPENING = Opening promotion.
- `SubmissionDate` = **2026-04-22**  
  Submitted now; the distributor has agreed it, so no acceptance deadline follows.
- `FirstShipmentAvailabilityDate` = **2026-04-29**  
  Stock can arrive from day 9.
- `PromotionalSpecification/SpecificationID` = **BM-REOPEN-HG-26/1**  
  The first part of the promotion.
- `PromotionalSpecification/PromotionalEventLineItem/Amount` = **674.10** (currencyID `XBL`)  
  The promotional price per bench: 749.00 less 10 %.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/LineNumberNumeric` = **1**  
  The line.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/ParticipatingLocationsLocation/Name` = **Brightmarket Stores, Lumeport**  
  The shop.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/RetailPlannedImpact/Amount` = **16178.40** (currencyID `XBL`)  
  24 benches more at the promotional price of 674.10.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/RetailPlannedImpact/ForecastPurposeCode` = **SALES** (listID `urn:ubl-examples:world:codelist:ForecastPurposeCode`)  
  Planned extra sales. The code is from the Trade Accord's forecast purpose list: SALES = Sales forecast.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/RetailPlannedImpact/ForecastTypeCode` = **TOTAL** (listID `urn:ubl-examples:world:codelist:ForecastTypeCode`)  
  In total. The code is from the Trade Accord's forecast type list: TOTAL = Total.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/RetailPlannedImpact/Period/StartDate` = **2026-05-11**  
  The promotion.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/RetailPlannedImpact/Period/EndDate` = **2026-05-24**  
  Its end.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/SupplyItem/Name` = **Park bench Serra 180**  
  The item promoted.
- `PromotionalSpecification/PromotionalEventLineItem/EventLineItem/SupplyItem/SellersItemIdentification/ID` = **LMW-10442**  
  The distributor's number.
- `PromotionalSpecification/EventTactic/Comment` = **Benches on a floor stand at the entrance, with a price board.**  
  What the store does.
- `PromotionalSpecification/EventTactic/Quantity` = **12** (unitCode `EA`)  
  Twelve benches on display.
- `PromotionalSpecification/EventTactic/EventTacticEnumeration/ConsumerIncentiveTacticTypeCode` = **TPR** (listID `urn:ubl-examples:world:codelist:ConsumerIncentiveTacticCode`)  
  A temporary price reduction. The code is from the Trade Accord's consumer incentive tactic list: TPR = Temporary price reduction.
- `PromotionalSpecification/EventTactic/EventTacticEnumeration/DisplayTacticTypeCode` = **FLOORSTAND** (listID `urn:ubl-examples:world:codelist:DisplayTacticCode`)  
  A floor stand at the entrance. The code is from the Trade Accord's display tactic list: FLOORSTAND = Floor stand.
- `PromotionalSpecification/EventTactic/EventTacticEnumeration/FeatureTacticTypeCode` = **FLYER** (listID `urn:ubl-examples:world:codelist:FeatureTacticCode`)  
  In the store's flyer. The code is from the Trade Accord's feature tactic list: FLYER = Store flyer.
- `PromotionalSpecification/EventTactic/EventTacticEnumeration/TradeItemPackingLabelingTypeCode` = **STICKER** (listID `urn:ubl-examples:world:codelist:PackingLabelingTypeCode`)  
  A price sticker on each bench. The code is from the Trade Accord's packing and labelling type list: STICKER = Price sticker.
- `PromotionalSpecification/EventTactic/Period/StartDate` = **2026-05-11**  
  During the promotion.
- `PromotionalSpecification/EventTactic/Period/EndDate` = **2026-05-24**  
  Its end.

### Miscellaneous Event

Inside `MiscellaneousEvent`:

- `MiscellaneousEventTypeCode` = **STOREOPEN** (listID `urn:ubl-examples:world:codelist:MiscellaneousEventTypeCode`)  
  The department's reopening on Monday 11 May, after its renovation: the event the promotion is for. The code is from the Trade Accord's miscellaneous retail event list: STOREOPEN = Store opening.
- `EventLineItem/LineNumberNumeric` = **1**  
  The line.
- `EventLineItem/SupplyItem/Name` = **Park bench Serra 180**  
  The item promoted.
- `EventLineItem/SupplyItem/SellersItemIdentification/ID` = **LMW-10442**  
  The distributor's number.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RetailEvent xmlns="urn:oasis:names:specification:ubl:schema:xsd:RetailEvent-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:retail-event:1.0#compliant#urn:ubl-examples:world:community:retail:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:collaboration:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900339162</cbc:ProfileExecutionID>
  <cbc:ID>6500016959</cbc:ID>
  <cbc:UUID>31926ddb-5dfd-59d6-bb1b-86b3926753e7</cbc:UUID>
  <cbc:IssueDate>2026-04-22</cbc:IssueDate>
  <cbc:IssueTime>11:13:00-01:00</cbc:IssueTime>
  <cbc:Note>Agreed with the distributor's sales team.</cbc:Note>
  <cbc:RetailEventName>Reopening of the home and garden department</cbc:RetailEventName>
  <cbc:RetailEventStatusCode listID="urn:ubl-examples:world:codelist:RetailEventStatusCode">CONFIRMED</cbc:RetailEventStatusCode>
  <cbc:SellerEventID>LMW-PROMO-26-03</cbc:SellerEventID>
  <cbc:BuyerEventID>BM-REOPEN-HG-26</cbc:BuyerEventID>
  <cbc:Description>After its renovation the home and garden department of the Lumeport store reopens on Monday 11 May: ten per cent off the department's range for two weeks, the Elderwick Marrow line excepted.</cbc:Description>
  <cac:Period>
    <cbc:StartDate>2026-05-11</cbc:StartDate>
    <cbc:EndDate>2026-05-24</cbc:EndDate>
  </cac:Period>
  <cac:Signature>
    <cbc:ID>BM-SIG-26-0422E</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9522610900002</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:TradePartyName>
      <cbc:Name>Brightmarket</cbc:Name>
    </cac:TradePartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-579130</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old Town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:ID>BM-CT-01</cbc:ID>
      <cbc:Name>Buying office</cbc:Name>
      <cbc:JobTitle>Buyer</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 2 38 4609 7100</cbc:Telephone>
      <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
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
      <cbc:Telephone>+999 2 5121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>sales@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:EventComment>
    <cbc:Comment>Floor space for 12 benches at the entrance of the renovated department.</cbc:Comment>
    <cbc:IssueDate>2026-04-22</cbc:IssueDate>
    <cbc:IssueTime>11:00:00-01:00</cbc:IssueTime>
  </cac:EventComment>
  <cac:PromotionalEvent>
    <cbc:PromotionalEventTypeCode listID="urn:ubl-examples:world:codelist:PromotionalEventTypeCode">OPENING</cbc:PromotionalEventTypeCode>
    <cbc:SubmissionDate>2026-04-22</cbc:SubmissionDate>
    <cbc:FirstShipmentAvailabilityDate>2026-04-29</cbc:FirstShipmentAvailabilityDate>
    <cac:PromotionalSpecification>
      <cbc:SpecificationID>BM-REOPEN-HG-26/1</cbc:SpecificationID>
      <cac:PromotionalEventLineItem>
        <cbc:Amount currencyID="XBL">674.10</cbc:Amount>
        <cac:EventLineItem>
          <cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
          <cac:ParticipatingLocationsLocation>
            <cbc:Name>Brightmarket Stores, Lumeport</cbc:Name>
          </cac:ParticipatingLocationsLocation>
          <cac:RetailPlannedImpact>
            <cbc:Amount currencyID="XBL">16178.40</cbc:Amount>
            <cbc:ForecastPurposeCode listID="urn:ubl-examples:world:codelist:ForecastPurposeCode">SALES</cbc:ForecastPurposeCode>
            <cbc:ForecastTypeCode listID="urn:ubl-examples:world:codelist:ForecastTypeCode">TOTAL</cbc:ForecastTypeCode>
            <cac:Period>
              <cbc:StartDate>2026-05-11</cbc:StartDate>
              <cbc:EndDate>2026-05-24</cbc:EndDate>
            </cac:Period>
          </cac:RetailPlannedImpact>
          <cac:SupplyItem>
            <cbc:Name>Park bench Serra 180</cbc:Name>
            <cac:SellersItemIdentification>
              <cbc:ID>LMW-10442</cbc:ID>
            </cac:SellersItemIdentification>
          </cac:SupplyItem>
        </cac:EventLineItem>
      </cac:PromotionalEventLineItem>
      <cac:EventTactic>
        <cbc:Comment>Benches on a floor stand at the entrance, with a price board.</cbc:Comment>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cac:EventTacticEnumeration>
          <cbc:ConsumerIncentiveTacticTypeCode listID="urn:ubl-examples:world:codelist:ConsumerIncentiveTacticCode">TPR</cbc:ConsumerIncentiveTacticTypeCode>
          <cbc:DisplayTacticTypeCode listID="urn:ubl-examples:world:codelist:DisplayTacticCode">FLOORSTAND</cbc:DisplayTacticTypeCode>
          <cbc:FeatureTacticTypeCode listID="urn:ubl-examples:world:codelist:FeatureTacticCode">FLYER</cbc:FeatureTacticTypeCode>
          <cbc:TradeItemPackingLabelingTypeCode listID="urn:ubl-examples:world:codelist:PackingLabelingTypeCode">STICKER</cbc:TradeItemPackingLabelingTypeCode>
        </cac:EventTacticEnumeration>
        <cac:Period>
          <cbc:StartDate>2026-05-11</cbc:StartDate>
          <cbc:EndDate>2026-05-24</cbc:EndDate>
        </cac:Period>
      </cac:EventTactic>
    </cac:PromotionalSpecification>
  </cac:PromotionalEvent>
  <cac:MiscellaneousEvent>
    <cbc:MiscellaneousEventTypeCode listID="urn:ubl-examples:world:codelist:MiscellaneousEventTypeCode">STOREOPEN</cbc:MiscellaneousEventTypeCode>
    <cac:EventLineItem>
      <cbc:LineNumberNumeric>1</cbc:LineNumberNumeric>
      <cac:SupplyItem>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>LMW-10442</cbc:ID>
        </cac:SellersItemIdentification>
      </cac:SupplyItem>
    </cac:EventLineItem>
  </cac:MiscellaneousEvent>
</RetailEvent>
```
