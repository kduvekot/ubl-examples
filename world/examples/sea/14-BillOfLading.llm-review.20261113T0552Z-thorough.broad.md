# LLM review: 14-BillOfLading.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/14-BillOfLading.xml`, Git blob `661653ae609f88a3a1ea21ce846d10c0b8de2faf` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit c9983d2 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/14#F1 · High · Declared customs value of the consignment differs from both customs declarations
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of all the goods in this consignment". The export declaration declares 50,688.00 XBL (`11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredCustomsValueAmount` = `50688.00`), and the import declaration declares 19,968.000 + 307.200 XLC (`19-ImportCustomsDeclaration.xml`, goods items; at the flow's rate 0.4 that is again 50,688.00 XBL). 53,778.00 is the CIF value (goods + freight + insurance, as in `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:Amount`), which no declaration declares.
- Condition: the bill of lading's declared customs value equals the value declared to customs (or is absent).
- Options: (a) preferred: 50,688.00 XBL, as both declarations; (b) drop it from the bill of lading (the carrier does not declare customs value); if the import value should be CIF, that is a change to the import declaration instead.
- Needs decision: no

### sea/14#F2 · Medium · Order and forwarding-instruction numbers given as consignment identifiers of other parties
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `VT-PO-26-0127`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreightForwarderAssignedID` = `LD-FI-26-0131`
- Why: `ConsignorAssignedID` is "An identifier for this consignment, assigned by the consignor" and `FreightForwarderAssignedID` "… assigned by the freight forwarder". `VT-PO-26-0127` is Velumi's purchase order (`05-Order.xml:/Order/cbc:ID`), assigned by the buyer, not by the consignor Lumeway, and an order, not a consignment. `LD-FI-26-0131` is Lumeway's forwarding instructions document (`09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0131`), assigned by the consignor, not by the forwarder Bayforth. Lumeway's own consignment number is `LD-CS-26-0133`; the forwarder's reference would be a Bayforth number.
- Condition: each assigned ID identifies the consignment and is assigned by the party its element names; order and instruction numbers are given as document references.
- Options: (a) preferred: drop both (the consignment ID is already Lumeway's) or give a Bayforth file number as forwarder-assigned ID; reference the order and the instructions as documents if wanted; (b) none better seen.
- Needs decision: no

### sea/14#F3 · Medium · The road trailer attached to the container on the ship
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:ID` = `BV CH 0412`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:TransportEquipmentTypeCode` = `TE`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:StowagePositionID` = `140282`
- Why: `AttachedTransportEquipment` describes equipment attached to the container. The trailer `BV CH 0412` is the pre-carriage truck's trailer (`/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:TrailerLicensePlateID` = `BV CH 0412`), which dropped the container at the terminal on 2026-05-13. On a cellular container ship, in slot 140282 on deck, the container travels without the trailer. The bill of lading describes the equipment as carried by sea, so the trailer is not attached there.
- Condition: the container's attached equipment is what travels with it on the main carriage (here none); the trailer appears only in the pre-carriage stage.
- Options: (a) preferred: drop `AttachedTransportEquipment`; (b) none better seen.
- Needs decision: no

### sea/14#F4 · Medium · One goods item said to be 25 goods items in the container; two goods items in the shipment
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem/cac:GoodsItemContainer/cbc:Quantity` = `25`
- XPath: `/BillOfLading/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem/cbc:Description` = `Park benches and spare side frames`
- Why: `GoodsItemContainer/Quantity` is "The number of goods items loaded into or onto one piece of transport equipment"; 25 is the number of pallets (handling units), not of goods items. The bill of lading has one goods item (with two contained goods items) while the shipment total says 2, and the packing list has two goods items (`10-PackingList.xml:/PackingList/cac:Shipment/cac:GoodsItem[2]/cbc:ID` = `2`). The goods item also carries no weight, quantity or package count of its own, and its `GoodsItemContainer` repeats the same container a third time (`/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem/cac:GoodsItemContainer/cac:TransportEquipment/cbc:ID` = `TWLU4120872`).
- Condition: the number of goods items is the same in every place (goods items, `TotalGoodsItemQuantity`, `GoodsItemContainer/Quantity`) and agrees with the packing list.
- Options: (a) preferred: two goods items (benches, side frames) with quantity, weight and packages, each in `GoodsItemContainer` quantity 1 (or the quantity of their goods items); (b) one goods item and `TotalGoodsItemQuantity` 1.
- Needs decision: no

### sea/14#F5 · Medium · The castings pallet also given as a box of twelve
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:Quantity` = `12`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:PackagingTypeCode` = `BX`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`
- Why: the same SSCC identifies a pallet (`PX`) carrying 12 packages and a box (`BX`) containing 12 items. An SSCC identifies one logistic unit; the castings cannot be both twelve packages on a pallet and twelve items in one box. The package also counts as a 26th unit beside the 25 pallets the packing list states (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`).
- Condition: each SSCC identifies one unit, and the castings are described once, consistently (12 packages on pallet 25, or one box on the pallet with its own identifier).
- Options: (a) preferred: drop the container-level `Package` (the pallet already says it carries 12 packages); (b) give the box as a package inside pallet 25 with its own ID.
- Needs decision: no

### sea/14#F6 · Medium · Language code in LocaleCode
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/14#F7 · Medium · A gate in AdditionalStreetName
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/14#F8 · Low · Total invoice amount is the goods value, not the invoice total
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:TotalInvoiceAmount` = `50688.00`
- Why: `TotalInvoiceAmount` is "The total of all invoice amounts declared in this consignment". The commercial invoice for these goods totals 53,778.00 XBL (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`: goods 50,688.00 + freight 2,950.00 + insurance 140.00, as CIF requires). The bill of lading gives the goods value without the freight and insurance the same invoice bills. Since the invoice is issued after the bill of lading (12:32 vs 10:54), the carrier can only know a declared amount from the shipper.
- Condition: the total invoice amount equals the invoice total of the consignment's commercial invoice, or the element is absent.
- Options: (a) preferred: drop it (the carrier does not need it); (b) 53,778.00.
- Needs decision: no

### sea/14#F9 · Low · Bill of lading holder named as the consignee while the originals go to the forwarder
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:BillOfLadingHolderParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/BillOfLading/cbc:ToOrderIndicator` = `true`
- Why: `BillOfLadingHolderParty` is the party holding the bill of lading. At issue the three originals go by courier to the forwarder (as instructed, `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`); the bill is to order, so Velumi becomes holder only when the originals are endorsed and handed over. Naming Velumi as holder in the bill as issued contradicts the distribution.
- Condition: the holder named is the party that holds the originals at issue, or the element is absent.
- Options: (a) preferred: drop `BillOfLadingHolderParty` (the holder changes with endorsement); (b) Bayforth (or Lumeway) as holder.
- Needs decision: no

### sea/14#F10 · Low · Two insurance policies for one cover
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: the consignment's policy has number, cover, premium, holder, beneficiary and certificate but no insurer; the shipment's policy has the insurer and the same insured value and excess, but no number. As written these are two policies covering 59,155.80 XBL each; the flow has one cover (premium 140.00 once, `22-Invoice.xml:/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`).
- Condition: the cover is described once, with insurer, policy number and amounts together.
- Options: (a) preferred: one `InsurancePolicy` at consignment level including the insurer; (b) none better seen.
- Needs decision: no

### sea/14#F11 · Low · Data the bill of lading does nothing with
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipsRequirements` = `Shore power at the container quay.`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:SegregatedBallastMeasure` = `2480`
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: `ShipsRequirements` is "Information about what services a vessel will require when it arrives at a port", a matter between the ship and the port, not for the shipper's bill of lading; the segregated ballast tonnage belongs to port and IMO reporting. The exchange rate converts nothing: every amount of the bill is in lume. They read as vessel and party master data copied into the document.
- Condition: the bill of lading carries vessel data that identify the vessel and the voyage, and an exchange rate only where it converts an amount of the document.
- Options: (a) preferred: drop ship's requirements, segregated ballast and the exchange rate; (b) none better seen.
- Needs decision: no

### sea/14#F12 · Low · Contacts whose function does not fit
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:Name` = `Cargo claims`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: the shipper's contact is Sales' customer service; the consignee's purchasing contact and the notify party's goods-inwards contact both have the job title and department of a seller's customer service; the insurer's claims contact is a client relationship manager.
- Condition: each contact's name, job title and department agree with each other and fit the party's role.
- Options: (a) preferred: shipping, goods-in and claims functions respectively.
- Needs decision: no

### sea/14#F13 · Low · Lisavu addresses tagged as Bayvarran English
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- Why: Velumi's and Nalevi's addresses in Lisavu are tagged `en-XL` in the order Velumi sent (`05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); across the flow the tag follows the sender's country (for Velumi 16 × `en-XB`, 8 × `en-XL` over `world/examples/sea/*.xml`).
- Condition: the same address carries the same `languageID` in every example.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu addresses everywhere.
- Needs decision: no

## Checked and consistent
- Freight: ocean freight 2,700.00 + bunker surcharge 250.00 = 2,950.00, the freight the invoice bills (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`); premium 140.00 and insured value 59,155.80 (110 % of CIF 53,778.00) agree with the invoice and the forwarding instructions; delivery-terms amount 53,778.00 = CIF value; THC at Selanu 185.00 for the buyer agrees with the collect terms.
- CIF: risk passes on board at Lumeport, delivery location Selanu (`XLSEL`), freight prepaid at Lumeport (`XBLMP`), as the order and the service description say.
- Weights: shipment gross 4,106.4 kg + tare 3,750 kg = container gross 7,856.4 kg = verified gross mass; VGM method SM2 (all packages weighed plus tare) fits a platform scale at the shipper on 2026-05-12, before the cargo acceptance on 2026-05-13.
- Pallets: 24 × 4 + 1 × 12 packages = 108, as `06-OrderResponse.xml` states (`TotalPackagesQuantity`); shipping marks 001 to 025 of 025; all 25 SSCCs and the container number have valid check digits (`check_ids.py`); prefix 9520610 is Lumeway's GS1 company prefix (GLN `9520610900008`).
- Stowage: position 140282 (bay 14, row 02, tier 82) is an even, 40-foot bay on deck, as the text and the 12.2 m slot length say (own knowledge of the bay-row-tier convention).
- Vessel: gross tonnage 9,940 fits a 1,000 TEU feeder (`08-TransportServiceDescription.xml`); call sign `QBTH7` and MMSI `298702117` are in unallocated ITU series (recorded in `world/codelists/sources/PROVENANCE-second-round.md`).
- Pre-carriage drop-off 2026-05-13 10:15 = cargo acceptance; storage from 10:30; availability at Selanu 2026-05-18 14:00 after a two-day crossing from the departure of 2026-05-14 (`13-TransportationStatus.xml`).
- References: `BF-FI-26-0137` (`12-ForwardingInstructions.xml`, also as `ShippingOrderID`, which the definition allows for forwarding instructions) and `LD-PL-26-0134` (`10-PackingList.xml`) resolve; booking number `TWL-BK-26-55710` as in `12-ForwardingInstructions.xml`.

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:HandlingCode` = `DECK` with "Keep dry." — refuted because a closed general-purpose container on deck keeps its contents dry; the two do not contradict.
- `/BillOfLading/cbc:OtherInstruction` = `Three originals issued.`: a statement rather than an instruction — refuted because the number of originals is the usual free-text clause of a bill of lading and has no element of its own here.
- `/BillOfLading/cbc:Description` = `Shipped on board.` at 10:54 while the loading is reported later that day — not settled from this example alone (the status report gives no loading time); see "Outside this review".
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `TH-26-19E`: "19" against ISO week 20 of the sailing — refuted because the journey ID is the carrier's own voyage number, not a week.
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:BrokerAssignedID` = `TCB-26-0331` — refuted: a reference of the import broker (Tevaro Customs Brokers, notifier in `19-ImportCustomsDeclaration.xml`) for the consignment, as defined.

## Outside this review
- Timeline across documents: a shipped-on-board bill issued at 10:54 on 2026-05-14, while the port's report of the loading on board is issued at 16:05 that day (`13-TransportationStatus.xml`) and the departure is at 18:10.
