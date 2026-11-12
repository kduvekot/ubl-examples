# LLM review: 08-Waybill.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/08-Waybill.xml`, Git blob `d66e8c026ae9b2002457ba46ff93f8f963503f91` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### rail/08#F1 · High · Customs as issuer of the declaration that Valdara made
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- Why: Customs Declaration. Issuer_ Party is "The Party who issues this Customs Declaration." The declaration referenced is `06-TransitCustomsDeclaration.xml` (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cbc:ID` = `VI-TD-26-0331`, a number in Valdara's own series). There Valdara is the Transit Exporter ("The Party who makes the Transit Customs Declaration, or on whose behalf…") and signs it (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`); the customs administration is the authority that processes it (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`). The waybill thus contradicts the declaration it refers to about who issued it.
- Condition: the issuer of the customs declaration referenced in both transport handling units is the party that issued `06-TransitCustomsDeclaration.xml` (Valdara Industries, `XU-R-104274`), or the referenced ID is a customs-assigned number (e.g. a movement reference number) that the declaration also carries.
- Options: (a) Valdara Industries as IssuerParty (preferred: matches the declaration as it stands); (b) if the waybill is meant to quote the customs-assigned reference, add that reference to the declaration's story and quote it, keeping customs as issuer of that reference.
- Needs decision: no

### rail/08#F2 · Medium · Province in Region of sender and receiver
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"). The consignee's address in the same document does so (`/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/08#F3 · Medium · Language code in LocaleCode of the consignee
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language. Locale Code is "A code signifying the locale in which this language is used." `en` (listID ISO 639) is a language code and repeats `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`. The value occurs 362 times in 213 example files (`grep -o 'LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: the consignee's Language has no LocaleCode, or one that names a locale from a list of locales.
- Options: (a) drop it (preferred); (b) a locale such as `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no

### rail/08#F4 · Medium · Gate in AdditionalStreetName of the consignee's postal address
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: Address. Additional Street Name is "An additional street name used to further clarify the address". "Gate 3" is an entrance of the site, not a street name. The waybill delivers by rail to the siding (`/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Rail siding of Lumeway Distribution, Marrowdale`), so the gate in the postal address is neither the delivery point nor part of the address.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) remove it from the postal address (preferred); (b) where a gate matters, state it at the delivery location.
- Needs decision: no

### rail/08#F5 · Medium · Terminal named as operator of a carrier-owned container
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:OperatingParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:OwnerParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ProviderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: Transport Equipment. Operating_ Party is "The Party who operates this piece of Transport Equipment." The operator of a container is the party that controls its use and deployment (in container logistics the "container operator", own knowledge). This container is owned and provided by the carrier (`/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:OwnerTypeCode` = `CARRIER`), which sends it to the warehouse and back under carrier haulage and orders its empty return to the hub. The hub stores and handles the box (`/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:StorageLocation/cbc:Name` = `Ferrano Intermodal Hub, stack C`); storing and lifting are terminal services, not operating the equipment. The second container has no operating party at all.
- Condition: the operating party of the container, if given, is the party that controls its use (here the carrier), and both containers are described alike.
- Options: (a) drop OperatingParty (preferred: owner and provider already name the carrier, and nothing implies otherwise); (b) Ferrano Rail Cargo as operator, if the element must stay; (c) if the hub's role is to be shown, a handling or storage location/event with the hub.
- Needs decision: no

### rail/08#F6 · Medium · EmissionCalculationLocation names a company office, not a geographic context
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionCalculationLocation/cbc:Name` = `Ferrano Rail Cargo, energy office`
- Why: Emission Calculation Method. Emission Calculation_ Location is "The geographical context in which this environmental emission was calculated or for which the emission factor applies, such as the country of a national database or regulatory regime." The value names the office of the carrier that did the calculation, which is neither a geographic area nor the area for which an emission factor applies (for electric rail traction this would be the grid or country whose electricity factor is used: Urvania, Bayvarra, or the Trade Accord area).
- Condition: EmissionCalculationLocation names the geographic area for which the emission factor applies (e.g. a country with its code), not an organisation or office.
- Options: (a) the country or grid area of the electricity factor (e.g. Urvania with country code) (preferred); (b) drop it, if no area-specific factor is used.
- Needs decision: no

### rail/08#F7 · Medium · Distribution of the originals contradicts the note
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: Document Distribution. Party is "The interested Party who receives this Document." The consignee's original is distributed to the terminal, not to the consignee (Lumeway, `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`); the consignor, which by the note receives an original, is listed for an electronic copy only; and the carrier's original is not listed. Travelling "with the goods" explains why the hub may hold the paper on the way, but not why the hub is the interested party receiving the consignee's original.
- Condition: the distribution list agrees with the note: the consignee's original goes to the consignee (it may travel with the goods), the consignor receives its original, and any copies are listed in addition; or the note is changed to what is distributed.
- Options: (a) consignee's original to Lumeway, consignor's original to Valdara, the carrier keeping its own (preferred: CMR practice, own knowledge of CMR art. 5); (b) change the note if the world's procedure differs.
- Needs decision: yes

### rail/08#F8 · Low · "English" renderings of Urvanian addresses and legal forms are Italian
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/08#F9 · Low · The warehouse and the hub named after their companies, and differently
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cac:Location/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:MeasurementFromLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, not the company, with identifiers where the same place is identified elsewhere. The issue location is the company Castrano Logistics; the pickup location, the same warehouse, is "Castrano Logistics warehouse, Ferrano" here and "Castrano Logistics" with a street address in `02-TransportExecutionPlanRequest.xml` and `03-TransportExecutionPlan.xml` (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`). The hub appears as the operator's name only. The same document identifies other places properly (`/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`, and the siding's GLN).
- Condition: each place (the warehouse, the terminal) has one name that names the place, the same in every example of the flow, and an identifier where the flow has one.
- Options: (a) one place name per location, plus a GLN or similar identifier (preferred); (b) at least the warehouse's address at the issue and pickup locations.
- Needs decision: no

### rail/08#F10 · Low · Receiver's contact is the sales order desk
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara receives the waybill as consignor and transport user; questions about the consignment note (and its original) go to Valdara's shipping function, not to the order desk that takes customer orders.
- Condition: the receiver's contact is Valdara's shipping or logistics function.
- Options: (a) a shipping/logistics contact (preferred); (b) role-specific contacts in Valdara's master data.
- Needs decision: no

### rail/08#F11 · Low · Consignee's contact is its sales customer service
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Section 5: a consignee's contact receives goods. The waybill asks to "Deliver against signature of the consignee" (`/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`); the carrier needs the goods-in or siding contact, not Lumeway's sales customer service.
- Condition: the consignee's contact is Lumeway's goods-receiving (warehouse, siding) function.
- Options: (a) a goods-in contact (preferred); (b) role-specific contacts in Lumeway's master data.
- Needs decision: no

### rail/08#F12 · Low · Legal-entity master data the waybill does nothing with
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: a waybill does nothing with the consignor's stock-exchange listing or with the share capital of consignor and consignee.
- Condition: every legal-entity element present has a purpose in the waybill.
- Options: (a) drop SecurityListing and CorporateStockAmount here (preferred); (b) a reduced party description for transport documents.
- Needs decision: no

### rail/08#F13 · Low · Performing carrier repeats the carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:PerformingCarrierParty/cac:PartyIdentification/cbc:ID` = `XU-R-104685`
- XPath: `/Waybill/cac:CarrierParty/cac:PartyIdentification/cbc:ID` = `XU-R-104685`
- Why: Consignment. Performing Carrier_ Party is "The Party who performs the carriage of this Consignment"; next to the (contracting) carrier it has a reason when another carrier performs all or part of the carriage. Here both are Ferrano Rail Cargo, also on the Bayvarran side, so the element repeats the carrier (section 4.8). The two carrier-assigned consignment IDs (contract call-off and journey reference) can both be kept without it.
- Condition: PerformingCarrierParty is absent, or names a carrier other than the contracting carrier that performs (part of) the carriage.
- Options: (a) drop PerformingCarrierParty (preferred); (b) if another undertaking hauls the train in Bayvarra, name it there.
- Needs decision: no

## Checked and consistent
- Sender, carrier and signatory Ferrano Rail Cargo; receiver and consignor Valdara; consignee Lumeway: same identifiers and full descriptions as in the other examples of the flow, and the same roles as in the plan referenced (`03-TransportExecutionPlan.xml`).
- Loading proof party Castrano Logistics (`XU-R-104411`) is the warehousing provider named in Valdara's ServiceProviderParty, and the pickup took place at its warehouse; owner and provider of the container are the carrier, matching `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:ProviderTypeCode` = `CARRIER`.
- Delivery location GLN `9520610900015` and Lumeway's GLN `9520610900008`: check digits correct; prefix 952 is GS1's range for demonstrations.
- Containers `FRXU1044175` and `FRXU1044180`: ISO 6346 check digits correct; the same containers as in `06-TransitCustomsDeclaration.xml`.

## Considered and refuted
- `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: master data copied — refuted: Castrano Logistics loads and certifies the load (LoadingProofParty) and is the pickup place, so the waybill uses it.
- `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Valdara Industries`: consignor without address, although a CMR states the sender's name and address — refuted: the same party (same ID) is the receiver with its full address in the same document.
- `/Waybill/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`: a CMR is signed by sender and carrier — refuted: UBL's Signature is the signature of the electronic document by its issuer, the carrier; the consignor's signature on the paper originals is outside what this element describes.

## Outside this review
- The waybill (`/Waybill/cbc:IssueTime` = `13:10:00`) cites the transit declaration `VI-TD-26-0331`, which is issued at 17:29 the same day (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cbc:IssueTime` = `17:29:00`): a timeline question across documents.
