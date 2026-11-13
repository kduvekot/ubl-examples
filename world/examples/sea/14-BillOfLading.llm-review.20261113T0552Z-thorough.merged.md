# LLM review: 14-BillOfLading.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/14-BillOfLading.xml`, Git blob `661653ae609f88a3a1ea21ce846d10c0b8de2faf` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/14#F1 · High · One SSCC for the frames pallet and for a box in the container, with package counts that disagree
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TransportHandlingUnitTypeCode` = `PX`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:PackagingTypeCode` = `BX`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:Quantity` = `12`
- Why: an SSCC identifies exactly one logistic unit (own knowledge of the GS1 rules). The same SSCC is the ID of the 25th handling unit, a pallet (`PX`) with "The total number of packages in this transport handling unit" 12, and of a box (`BX`) directly in the container with "The quantity of items contained in this package" 12. Either pallet and box are one object described twice with two packaging types, or two objects share a key; and if the frames are one box of 12 on the pallet, the pallet holds 1 package, not 12. The box also stands beside the 25 pallets as a 26th unit (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`). Two values of this document contradict each other (High).
- Condition: each SSCC identifies one unit of one type, and the castings are described once, with counts that agree (12 packages on pallet 25, or one box of 12 on pallet 25 with its own identifier).
- Options: (a) preferred: drop the container-level `Package` and keep pallet 25 with its 12 side frames (broad, context; matches the "castings pallet" of the packing list); (b) the box as a package inside pallet 25, with its own ID or none, and the pallet's package count 1 (logistics' preference).
- Needs decision: no
- From: logistics (F1, High), context (F1, High), broad (F5, Medium)

### sea/14#F2 · High · Shipment gross weight smaller than the gross weight of its own container
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:VerifiedGrossMass/cbc:GrossMassMeasure` = `7856.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The shipment's only container weighs 7,856.4 kg gross, also as verified gross mass (recomputed 4,106.4 + tare 3,750 = 7,856.4); the shipment cannot weigh less than its container. 4,106.4 kg is the goods-and-packaging weight practice prints on a bill of lading, which the semantic-conformance rule does not follow. Contradiction within the document (High), as in `10-PackingList.xml`.
- Condition: the shipment's gross weight includes the container, or the goods-and-packaging weight is carried on the goods item.
- Options: (a) preferred: 4,106.4 kg on the goods item's `GrossWeightMeasure` (which excludes the carrier's equipment) and 7,856.4 kg or nothing on the shipment; (b) 7,856.4 kg on the shipment only.
- Needs decision: no
- From: context (F5, Medium), logistics (F4, Medium)

### sea/14#F3 · High · Declared customs value of the consignment differs from the values both customs declarations declare
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`
- XPath: `11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredCustomsValueAmount` = `50688.00`
- XPath: `19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`
- XPath: `19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `307.200`
- Why: `Consignment/DeclaredCustomsValueAmount` is "The total declared value for customs purposes of all the goods in this consignment …". 53,778.00 is the CIF value (goods 50,688.00 + freight 2,700.00 + bunker 250.00 + premium 140.00, recomputed; the same as `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:Amount`). The export declaration declares 50,688.00 XBL; the import declaration declares 19,968.000 + 307.200 = 20,275.200 XLC, which at the flow's rate 0.4 is 20,275.200 / 0.4 = 50,688.00 XBL again (recomputed), i.e. the goods value, with a freight share carried separately on goods item 1 (`19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:Amount` = `1162.121`, = 2,905.30 XBL, 2,950.00 × 49,920 / 50,688). No declaration declares 53,778.00. The money and context parts refuted the difference because the import into Lisavu is valued CIF; but the import declaration in the flow does not declare a CIF value, so the bill of lading contradicts it either way. Which value is right depends on Lisavu's valuation basis (a question the cotton merges also left open).
- Condition: the bill of lading's declared customs value equals the value declared to customs for the consignment, or is absent.
- Options: (a) preferred: Lisavu values CIF: keep 53,778.00 here and change the import declaration's declared values to the CIF basis (21,511.200 XLC = 53,778.00 × 0.4, recomputed), as the merge of 16–22 prefers for `19-ImportCustomsDeclaration.xml`; (b) drop the value from the bill of lading (the carrier declares no customs value); (c) 50,688.00 XBL, if Lisavu values on the goods price.
- Needs decision: yes (Lisavu's customs valuation basis)
- From: broad (F1); money and context considered and refuted it (not followed)

### sea/14#F4 · High · Total invoice amount is the goods value, not the invoice total
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:TotalInvoiceAmount` = `50688.00`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:Amount` = `53778.00`
- XPath: `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`
- Why: `TotalInvoiceAmount` is "The total of all invoice amounts declared in this consignment". The consignment is invoiced once, by Lumeway to Velumi, for 53,778.00 (goods 50,688.00 + freight 2,950.00 + insurance 140.00, as CIF requires); the bill of lading states the goods value only (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`), while its own delivery terms give the CIF amount for the same sale. The bill (10:54) precedes the invoice (12:32), so the carrier can only have the amount from the shipper; it still contradicts the invoice and the document's own delivery terms (High; broad had Low).
- Condition: the total invoice amount equals the invoice total of the consignment's commercial invoice (53,778.00 as the invoice stands), or is absent.
- Options: (a) preferred: drop it (the carrier does nothing with it, and the bill is issued before the invoice); (b) 53,778.00 (money's preference, which also matches the delivery terms).
- Needs decision: no
- From: money (F1, High), broad (F8, Low)

### sea/14#F5 · High · Final delivery party is the buyer, while the goods are delivered to its 3PL Nalevi Warehousing
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:FinalDeliveryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:LogisticsOperatorParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: `FinalDeliveryParty` is "The final delivery party for this consignment", the party to which the goods are finally delivered; the consignee is a separate element. The goods go from Selanu port to Nalevi's warehouse, which in this document carries them on (with warehousing and receipt events) and operates the logistics; the order names Nalevi as delivery party (`05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`) and the packing list says `10-PackingList.xml:/PackingList/cac:Shipment/cbc:DeliveryInstructions` = `Deliver to the buyer's 3PL, Nalevi Warehousing, Selanu.`. Naming Velumi (consignee, office in Reef Street) contradicts the document's own on-carriage and two other examples.
- Condition: `FinalDeliveryParty` is the party where the consignment is finally delivered, consistent with the on-carriage and with 05 and 10, or absent.
- Options: (a) preferred: Nalevi Warehousing, Velumi stays consignee; (b) drop it (on-carriage and notify party already say enough).
- Needs decision: no
- From: parties (F1, High), context (F8, Low)

### sea/14#F6 · Medium · Consignor's and forwarder's consignment IDs hold other parties' document numbers
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `VT-PO-26-0127`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreightForwarderAssignedID` = `LD-FI-26-0131`
- Why: `ConsignorAssignedID` is "An identifier for this consignment, assigned by the consignor", `FreightForwarderAssignedID` "… assigned by the freight forwarder". `VT-PO-26-0127` is Velumi's purchase order (`05-Order.xml`), assigned by the buyer and an order, not a consignment; `LD-FI-26-0131` is Lumeway's forwarding instructions (`09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0131`), a document of the consignor. Lumeway's own consignment number is `LD-CS-26-0133` (`Consignment/ID`); Bayforth's own reference is its shipping order `BF-FI-26-0137`. The bill's `ShippingOrderID` `BF-FI-26-0137` itself is right (it is `12-ForwardingInstructions.xml`); the contradicting values are in 12 and 13 (findings there).
- Condition: each party-assigned consignment ID is assigned by that party and identifies the consignment; order and instruction numbers, if wanted, are document references with a type.
- Options: (a) preferred: drop `ConsignorAssignedID` (the consignment's `ID` is Lumeway's) and give a Bayforth file number as `FreightForwarderAssignedID` or drop it; reference the order and the instructions as typed documents if wanted.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2, High, grouped with the shipping order)

### sea/14#F7 · Medium · Goods-item container quantity counts pallets, not goods items
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem/cac:GoodsItemContainer/cbc:Quantity` = `25`
- XPath: `/BillOfLading/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2`
- Why: `GoodsItemContainer/Quantity` is "The number of goods items loaded into or onto one piece of transport equipment as a total consignment or part of a consignment". The container holds one goods item with two contained goods items (1.1 benches, 1.2 frames), the shipment counts 2; 25 is the number of pallets. The goods item's `GoodsItemContainer` also repeats the container it already sits in.
- Condition: the quantity is the number of goods items in the container, consistent with `TotalGoodsItemQuantity`, or `GoodsItemContainer` is absent.
- Options: (a) preferred: drop `GoodsItemContainer` (the goods item lies wholly in this container); (b) the goods-item count (1, or 2 if the two goods items are given as such).
- Needs decision: no
- From: broad (F4), logistics (F3), context (F3)

### sea/14#F8 · Medium · The road trailer still attached to the container on a shipped-on-board bill
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:ID` = `BV CH 0412`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:TransportEquipmentTypeCode` = `TE`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:StowagePositionID` = `140282`
- Why: `AttachedTransportEquipment` is "A piece of transport equipment attached to this piece of transport equipment". `BV CH 0412` is the pre-carriage trailer (`/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:TrailerLicensePlateID` = `BV CH 0412`), which dropped the container at the terminal on 13 May; the bill describes the container on board, in slot 14-02-82 on deck of a cellular feeder, where no road chassis is attached. The element states something false of the carriage the bill covers.
- Condition: the container's attached equipment is what is attached during the carriage the bill covers (here none); the trailer stays in the pre-carriage stage.
- Options: (a) preferred: drop `AttachedTransportEquipment`.
- Needs decision: no
- From: broad (F3), context (F4), logistics (F5, Low)

### sea/14#F9 · Medium · Language code in LocaleCode
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) repeats the language. 362 occurrences in 213 examples.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB`.
- Needs decision: no
- From: broad (F6), parties (F3), context (F6)

### sea/14#F10 · Medium · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address"; a gate is not a street, and a postal address has no use for it. 79 occurrences in 76 examples.
- Condition: no street element of the postal address holds a gate.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (F7), parties (F4), context (F14, Low)

### sea/14#F11 · Low · Bill of lading holder named as the consignee while the originals go to the forwarder
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:BillOfLadingHolderParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cbc:ToOrderIndicator` = `true`
- XPath: `/BillOfLading/cbc:OtherInstruction` = `Three originals issued.`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `BillOfLadingHolderParty` is "The Party who holds the Bill of Lading for this Consignment". The bill is to order, in three originals, sent by courier to Bayforth as instructed (`12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`). At issue the holder is the shipper's side; Velumi becomes holder only when the originals are endorsed and handed over, which no document shows. The definition does not say whether the holder at issue or the intended holder is meant, so the merge cannot settle whether this is a contradiction (parties: Medium; broad, context: Low).
- Condition: the holder named is the party that holds the originals at the time the document states, consistent with the distribution, or the element is absent.
- Options: (a) preferred: drop it (the holder changes with endorsement; broad, context); (b) Bayforth (or Lumeway) as holder (parties); (c) keep Velumi and send the originals to Velumi.
- Needs decision: yes (who holds the originals in the story)
- From: parties (F2, Medium, yes), broad (F9), context (F7)

### sea/14#F12 · Low · One cargo insurance split over two policies, and the certificate referenced as the policy document
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:PolicyHolderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:PolicyDocumentReference/cbc:ID` = `WS-CERT-26-0884`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: the consignment's policy `WS-CP-26-4471` has number, cover, premium, broker, holder and beneficiary but no insurer; the shipment carries a second policy without ID, with the same insured value and excess, naming the insurer and again the broker. Read as written, the shipment (one consignment) is covered twice, 2 × 59,155.80 = 118,311.60, against one premium of 140.00 in the flow (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`) and one policy in the import declaration (`19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`); the insurer cannot be linked to the policy number. `PolicyDocumentReference` is "A reference to the policy document"; `WS-CERT-26-0884` is by its number a certificate under the policy, which is what a CIF seller provides.
- Condition: the cover is described once, at one level, with number, insurer, holder, broker, beneficiary and amounts together, and a certificate is referenced as such.
- Options: (a) preferred: one `InsurancePolicy` on the consignment with the insurer added and the certificate reference typed as an insurance certificate; (b) both levels kept, each complete with the same ID.
- Needs decision: no
- From: broad (F10), money (F4), parties (F10), context (F9)

### sea/14#F13 · Low · Deductible and excess of the policy both 250.00
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:DeductibleAmount` = `250.00`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ExcessAmount` = `250.00`
- Why: "The deductible amount specified in the policy" and "The excess amount specified in the policy"; in cargo insurance the two terms name the same retention (own knowledge, money). Stating both with the same figure either repeats one term or claims two retentions of 250.00 on one loss; nothing in the bill needs both.
- Condition: one retention in the element that fits it, or two distinct, explained retentions.
- Options: (a) preferred: keep one (e.g. `ExcessAmount`).
- Needs decision: no
- From: money (F3); context deferred it to money

### sea/14#F14 · Low · Pre-carriage freight of 310.00 that no one bills, for haulage the shipper arranges
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:FreightAllowanceCharge/cbc:Amount` = `310.00`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Ocean freight and bunker surcharge prepaid by the shipper.`
- Why: the ocean carrier's bill states 310.00 for the road leg Marrowdale–Lumeport by Bayforth, booked as merchant haulage (`09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:OriginalDespatchTransportationService/cbc:TransportServiceCode` = `MERCHHAUL`), i.e. outside the carrier's contract; the bill's payment terms cover only ocean freight and bunker. Nobody bills it: Bayforth's invoice to Lumeway is 2,950.00 + 85.00 + 140.00 = 3,175.00 (`18-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3175.00`, recomputed), and Lumeway does not pass it on.
- Condition: a pre-carriage charge in the bill is a charge under its contract of carriage with payment terms and is billed in the flow, or the bill does not state it.
- Options: (a) preferred: remove it from the carrier's bill and, if Bayforth's haulage is to be paid, bill it in `18-Invoice.xml`; (b) carrier haulage under the bill, included in the prepaid terms.
- Needs decision: yes
- From: money (F2)

### sea/14#F15 · Low · Vessel master data and port requirements in a bill of lading
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipsRequirements` = `Shore power at the container quay.`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:SegregatedBallastMeasure` = `2480`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:NetTonnageMeasure` = `5120`
- Why: `ShipsRequirements` is "Information about what services a vessel will require when it arrives at a port", a matter between ship and port; segregated ballast and tonnages are port-dues and port-call data. Shipper and consignee do nothing with them; they look copied from the vessel's master data (they belong in `15-Manifest.xml` and the port reports).
- Condition: the bill's vessel data identify the vessel and voyage.
- Options: (a) preferred: drop requirements, ballast and tonnages here.
- Needs decision: no
- From: broad (F11, vessel part), context (F10)

### sea/14#F16 · Low · Exchange rate the bill does nothing with
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: all amounts of the bill are in lume, including the terminal handling collect at Selanu (185.00); nothing is converted, and the rate has no date.
- Condition: an exchange rate only with an amount that needs it, dated.
- Options: (a) preferred: drop it; (b) collect charges stated in coral, with a dated rate.
- Needs decision: no
- From: broad (F11, rate part), money (F5), context (F11)

### sea/14#F17 · Low · References with only an ID, and a broker reference that ties to nothing
- XPath: `/BillOfLading/cac:DocumentReference/cbc:ID` = `BF-FI-26-0137`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:DocumentReference/cbc:ID` = `LD-PL-26-0134`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:BrokerAssignedID` = `TCB-26-0331`
- Why: the forwarding instructions and the packing list are referenced without a type. The broker's number occurs in no other example (`grep -rl --include='*.xml' 'TCB-26-0331' world/examples`: only this file), not even in the import declaration of the broker's client. Broad refuted the broker ID as a legitimate broker reference for the consignment (Tevaro Customs Brokers, notifier in `19-ImportCustomsDeclaration.xml`); the element fits, but the value links to nothing — the weakest part of this finding.
- Condition: references carry a type; the broker's ID is one the broker uses in the flow, or absent.
- Options: (a) preferred: type codes on the references; use the broker's reference in 19 or drop it here.
- Needs decision: no
- From: context (F12)

### sea/14#F18 · Low · On-carriage events without place
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:WarehousingTransportEvent/cbc:OccurrenceDate` = `2026-05-19`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:ReceiptTransportEvent/cbc:OccurrenceDate` = `2026-05-19`
- Why: the two planned on-carriage events have a date but no location; where the goods are warehoused and received is only implied by the on-carrier.
- Condition: each event carries its location (Nalevi's warehouse in Selanu, identified as elsewhere in the flow).
- Options: (a) preferred: the warehouse location on both events, or one location for the stage.
- Needs decision: no
- From: logistics (F6)

### sea/14#F19 · Low · Port of registry named but not identified
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- Why: name only, while the document identifies Lumeport as `XBLMP` elsewhere.
- Condition: the registry port carries `XBLMP`.
- Options: (a) preferred: add `ID` `XBLMP`.
- Needs decision: no
- From: logistics (F7)

### sea/14#F20 · Low · Contacts whose function does not fit the role
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:Name` = `Cargo claims`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: the shipper's contact is Sales' customer service; the consignee's "Purchasing" and the notify party's "Goods inwards" (the contacts the carrier calls on arrival) both carry a seller's customer-service title and department; the insurer's claims contact is a client relationship manager.
- Condition: contacts with agreeing name, title and department that fit the role, or none.
- Options: (a) preferred: shipping, goods-receipt (warehouse operations) and claims functions.
- Needs decision: no
- From: broad (F12), parties (F5, F7, F8), context (F13)

### sea/14#F21 · Low · Velumi's and Nalevi's Lisavu addresses tagged as Bayvarran English
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: tagged `en-XB` here (issued by Tidewell), `en-XL` in the order Velumi sent (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`); the tag follows the issuer across the flow, a convention no document records.
- Condition: the same `languageID` in every example, or the issuer rule recorded.
- Options: (a) preferred: `en-XL` everywhere; (b) record the rule.
- Needs decision: yes (one rule for the world)
- From: broad (F13), parties (F6, address part)

### sea/14#F22 · Low · Legal forms of Velumi and Nalevi given once, in English, without the Lisavan form
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: the order gives Velumi's legal form in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); here only the English, untagged.
- Condition: the same renderings in every example.
- Options: (a) preferred: both renderings, tagged.
- Needs decision: no
- From: parties (F6, legal-form part; split by the merge)

### sea/14#F23 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Bayforth, Velumi, Nalevi and Wavesure share New Year's Day 1996; 271 occurrences in 181 examples; a default value, not a fact of the world.
- Condition: own dates, or absent.
- Options: (a) preferred: own dates; (b) leave the element out.
- Needs decision: yes
- From: parties (F9)

### sea/14#F24 · Low · Party master data the bill does nothing with
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/BillOfLading/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234521`
- Why: share capital of shipper and carrier, and the state sales-tax registrations of forwarder and insurer, play no role in a bill of lading; they look copied from master data (section 4.8). The carrier's own tax registration (it charges the freight) is left out of the finding. Not raised by any part; added by the merge, as in the earlier flows.
- Condition: the parties carry only what the bill uses.
- Options: (a) preferred: drop them.
- Needs decision: no
- From: merge

### sea/14#F25 · Low · A signature with an ID and the signatory only, its ID carrying the flow name
- XPath: `/BillOfLading/cac:Signature/cbc:ID` = `TWL-SIG-BL-sea`
- Why: a bill of lading is signed by or for the carrier (or master); this signature has no method, date, attachment or signing person, and its ID ends in `sea`, the name of the example flow. Not raised by any part; added by the merge, as in 09–13.
- Condition: the signature says how, when and by whom the bill was signed, with the carrier's own reference.
- Options: (a) preferred: complete it (for a bill of lading a signature has a business reason); (b) drop it.
- Needs decision: yes (whether the world's documents are signed at all)
- From: merge

## Checked and consistent
- Freight (recomputed): ocean freight 2,700.00 + bunker 250.00 = 2,950.00, as billed in `22-Invoice.xml` and `18-Invoice.xml`; premium 140.00 and insured value 59,155.80 (110 % of 53,778.00) agree with the invoices and 09; CIF Selanu, risk on board at Lumeport, freight prepaid at `XBLMP`; terminal handling at Selanu 185.00 for the buyer, collect from the consignee, as the port reports in 17.
- Weights: 3,984 + 122.4 = 4,106.4 kg; + tare 3,750 = 7,856.4 kg = container gross = VGM, method SM2 by the shipper on 2026-05-12, before acceptance on 2026-05-13 10:15; 7,856 kg is far below a 40-foot box's maximum gross (about 30,480 kg); 41.5 m³ gross in about 67.7 m³ (61 %).
- Pallets: 24 × 4 + 1 × 12 = 108 packages, as in `06-OrderResponse.xml`; marks 001–025 of 025; all 25 SSCCs and the container number have valid check digits (`check_ids.py`, from the parts); SSCC prefix 9520610 is Lumeway's.
- Stowage 140282 (bay 14, row 02, tier 82): an even 40-foot bay on deck, consistent with "On deck" and `DECK` (own knowledge of ISO 9711, from broad and logistics).
- Vessel: gross tonnage 9,940 fits a 1,000 TEU feeder; vessel data agree with `15-Manifest.xml`. Call sign `QBTH7` (Q prefix not allocated to countries) and MMSI `298702117`: `world/codelists/sources/PROVENANCE-second-round.md` records that the ITU MID table re-read on 2026-11-11 lists none of 280–299, so MID 298 is unallocated and the MMSI cannot be mistaken for a real ship (from broad, logistics; verified against the provenance file by the merge).
- References: `BF-FI-26-0137` (document reference and shipping order) → `12-ForwardingInstructions.xml`; `LD-PL-26-0134` → `10-PackingList.xml`; booking `TWL-BK-26-55710` as in 12.
- Parties: consignor, carrier, forwarder, consignee as in 09, 10, 12; VGM weighing, shipper and responsible party Lumeway fit SOLAS method 2; policy holder Lumeway and beneficiary Velumi fit CIF; the scanned copy goes to Nalevi, which collects the container.

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:HandlingCode` = `DECK` with "Keep dry." — refuted: a closed general-purpose container on deck keeps its contents dry (from broad, context, logistics).
- `/BillOfLading/cbc:OtherInstruction` = `Three originals issued.`: a statement rather than an instruction — refuted: the number of originals is the usual free-text clause of a bill (from broad).
- `/BillOfLading/cbc:Description` = `Shipped on board.` at 10:54, while the port reports the loading at 16:05 — refuted for this example: no example gives the loading time, so loading may have taken place before 10:54 (from logistics; broad left it open). See "Outside this review".
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `TH-26-19E`: "19" against ISO week 20 — refuted: the carrier's own voyage number (from broad).
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:BrokerAssignedID` = `TCB-26-0331` — refuted by broad as a legitimate reference of the import broker. Partly not followed: the missing link to any other document is kept in F17.
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00` against the export declaration's 50,688.00 — refuted by money and context (Consignment-level definition; CIF basis at import). Not followed: F3, because the import declaration does not declare a CIF value either.
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreeOnBoardValueAmount` = `50688.00` against its loose UBL definition — refuted: the element is the FOB value, the CIF amount is in the delivery terms (from money).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:ExtraAllowanceCharge/cbc:AllowanceChargeReasonCode` = `FC` for the bunker surcharge — refuted: UN/EDIFACT 7161 has no bunker code; the reason text names it (from money).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cac:AllowanceCharge/cbc:Amount` = `185.00` for the buyer in the delivery terms — refuted: the delivery terms settle the allocation of destination THC under CIF (from money).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty` = the forwarder as road carrier — refuted: 09 asks Bayforth to "arrange the truck to the port" (from parties).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty` = Nalevi Warehousing — refuted: a 3PL that collects containers with its own trucks is normal (from parties).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem` (one goods item) against `/BillOfLading/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2` — refuted: the goods item contains the two goods items 1.1 and 1.2 (from logistics; broad's F4 had folded this in, the merge kept only the quantity 25 in F7).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:Stowage/cbc:Location` = `On deck, aft of the bridge` with bay 14 — refuted: nothing places the bridge (from logistics).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealIssuerTypeCode` = `CARRIER` applied by the shipper — refuted: common for FCL (from logistics).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:VerifiedGrossMass/cac:DocumentReference/cbc:ID` = `VGM-26-0510`: the VGM's ID equal to its evidence — refuted: the VGM declaration carries that number (from context).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ExcessAmount`: deductible and excess both 250.00 — deferred by context to the money lens; kept as F13.

## Changed in the merge
- broad/F5 (Medium) → F1 (High), with logistics and context: the two descriptions of one SSCC contradict each other.
- context/F5, logistics/F4 (Medium) → F2: High, because the same document states the container's gross weight and VGM (contradiction), as in 10.
- money/F1 (High), broad/F8 (Low) → F4: High kept; options from both.
- parties/F1 (High), context/F8 (Low) → F5: High kept (contradiction with the on-carriage and with 05 and 10).
- context/F2 (High) → F6 (Medium): the shipping order part of context's finding concerns 12 and 13 (High there); in this bill `ShippingOrderID` is right, so only the misuse of the assigned IDs remains.
- logistics/F5 (Low) → F8: Medium, with broad and context.
- context/F14 (Low) → F10: Medium, aligned.
- parties/F2 (Medium, yes), broad/F9 and context/F7 (Low) → F11: Low, needs decision yes, because the definition does not settle whether holder at issue or intended holder is meant.
- broad/F10, money/F4, parties/F10, context/F9 → F12: grouped; context's certificate point folded in.
- broad/F11 → F15 and F16: split into vessel data and exchange rate.
- parties/F6 → F21 and F22 (split); broad/F13 (no) aligned to yes.
- broad/F1 → F3: High kept against money's and context's refutation; needs decision yes added (valuation basis) and the preferred option aligned with the merge of 16–22 (CIF basis, fix 19). That merge rates the same pair Medium/yes in 19 because the basis is undecided; here it stays High because this document's value contradicts the value declared in 19 whichever basis is chosen (section 6), and the fix may lie in either document.
- LocaleCode: preferred option set to drop.
- F24, F25 added by the merge.

## Outside this review
- Timeline across documents: a shipped-on-board bill issued at 10:54 on 2026-05-14, while the port's report of the loading is issued at 16:05 that day (`13-TransportationStatus.xml`, loading without a time) and the manifest still estimates the departure for 2026-05-15 06:00 (`15-Manifest.xml`) (from broad, context).
