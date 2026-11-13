# LLM review: 12-DespatchAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/12-DespatchAdvice.xml`, Git blob `d93dffcfbe79b292ad495776e25413987734c7cc` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/12#F1 · High · Despatch line `1` exists twice, with 4 and with 24 benches
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:DeliveredQuantity` = `4`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `24`
- XPath: `/DespatchAdvice/cbc:LineCountNumeric` = `1`
- Why: HandlingUnitDespatchLine is "A despatch line associated with this transport handling unit"; its ID is "An identifier for this despatch line". The six handling units carry despatch lines `1` to `6` with 4 benches each, and the document-level despatch line is also `1`, with 24. Line `1` therefore has two quantities, and lines 2–6 exist only inside handling units although LineCountNumeric says the document has one line. The receipt advice, invoice and credit note all point to "despatch line 1 of LD-DA-26-0229" (`18-Invoice.xml:/Invoice/cac:InvoiceLine/cac:DespatchLineReference/cbc:LineID` = `1`), which can be either.
- Condition: every despatch line ID in the document identifies one line with one quantity; the handling units either repeat the document's line (same ID, with the quantity of that unit stated as a unit-level quantity) or carry lines with IDs of their own that do not collide with the document line, consistent with LineCountNumeric.
- Options: (a, preferred) give the handling-unit lines IDs that cannot be confused with the document line (e.g. `1-1` … `1-6`, each referring to order line 1) and keep DespatchLine `1` = 24; (b) drop the HandlingUnitDespatchLines and state the content per pallet through TotalPackageQuantity and the goods item.
- Needs decision: no

### retail/12#F2 · High · Packages per pallet: 4 counted, one listed, and that one is the pallet itself
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:Quantity` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `PX`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks` = `One carton torn, the bench's armrest bent.`
- Why: Each handling unit is a pallet (`PX`) with TotalPackageQuantity 4 ("The total number of packages in this transport handling unit"), but lists one ActualPackage ("A package contained in this transport handling unit"), which is again a pallet (`PX`, a returnable GRAI asset) containing 1 item. A pallet does not contain a pallet, and the four packages are nowhere described. The receipt advice 17 and the credit note 19 speak of a torn carton, so each bench travelled in a carton: the four cartons are the packages, each with 1 bench. The same pattern is repeated in all six handling units (`TransportHandlingUnit[1]` to `[6]`).
- Condition: in every handling unit, the packages listed match TotalPackageQuantity and the goods (four cartons of one bench each), and the pallet is described as the handling unit itself (its GRAI as the unit's or the equipment's identifier), not as a package inside it.
- Options: (a, preferred) four ActualPackage per unit, PackagingTypeCode for a carton (Rec. 21 `CT`), Quantity 1 each; the pallet's GRAI moved to the handling unit (e.g. as a returnable-asset reference); (b) if the benches travel unpacked, TotalPackageQuantity 0/absent, and 17 and 19 must not speak of cartons.
- Needs decision: no

### retail/12#F3 · High · Emission value is not factor × base
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/12#F4 · Medium · The despatch advice gives no despatch date, delivery place or expected delivery
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0230`
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-04-29`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: A Despatch Advice tells the receiver what has been despatched and when and where it will arrive, so that goods-in can plan (the order asked for delivery at goods-in `9522610900019`; the receipt 17 complains about a delivery slot). The shipment has no Delivery (no actual despatch date, no delivery location or address, no estimated delivery period), the document has no Delivery either; the only date is the issue date. The receiver learns the expected arrival only from the forwarder's status 15, which it does not receive.
- Condition: the despatch advice states when the goods were despatched and where and when they are expected (delivery location with the order's GLN, estimated delivery date/time or slot).
- Options: (a, preferred) Shipment/Delivery with DeliveryLocation `9522610900019`, Despatch/ActualDespatchDate (and time), EstimatedDeliveryPeriod; (b) at least the delivery location and an estimated delivery date.
- Needs decision: no

### retail/12#F5 · Medium · Issued hours after the truck left, and after the arrival time the forwarder expected
- XPath: `/DespatchAdvice/cbc:IssueTime` = `15:34:00`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- Why: By 11:49 on 2026-04-29 the truck was already on its way and expected at the store at 14:00 (15); the despatch advice, which should reach the receiver at despatch so that it can prepare the receipt, is issued at 15:34, after that expected arrival. The receipt advice 17 then records receipt the next morning (2026-04-30 10:40), which contradicts the 14:00 expectation of 15 for a 38 km trip (`16-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38`). Either the goods left on 2026-04-29 morning and arrived that afternoon (then this advice is late and 17 is wrong), or they arrived on 2026-04-30 (then 15's expectation and "on its way" on 2026-04-29 do not fit).
- Condition: the despatch advice is issued no later than the despatch, and despatch, the forwarder's status and the receipt describe one consistent sequence.
- Options: (a, preferred) issue the despatch advice at loading (before the "on its way" status of 11:49) and make the delivery day the same in 15 and 17; (b) if the delivery was on 2026-04-30, move the departure and the status 15 to that day.
- Needs decision: yes (which day the benches were delivered is part of the story)

### retail/12#F6 · Low · Vehicle, goods item and shipping document only on the first pallet
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `BV LP 2203`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:GoodsItem/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[2]/cbc:TotalGoodsItemQuantity` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ShipmentDocumentReference/cbc:ID` = `LD-TR-26-0227`
- Why: All six pallets travel on the same truck, but the TransportMeans (truck BV LP 2203 with trailer BV TR 0817), the goods item and the shipping-document reference appear only in the first handling unit. Units 2–6 each declare TotalGoodsItemQuantity 1 but contain no goods item, and unit 1's goods item has only an ID. A means of transport that carries the whole shipment belongs at shipment level (Shipment/Delivery or a transport stage), not to one pallet. The shipping document referenced is the transport request 11, not the consignment note 13 (`13-Waybill.xml:/Waybill/cbc:ID` = `BF-WB-26-0231`), which exists and was issued at 08:56 that day.
- Condition: data that apply to the whole shipment (vehicle, shipping documents) are stated once for the shipment, or equally for every unit; each declared goods item exists; the shipping document reference names the consignment note where one exists.
- Options: (a, preferred) move the vehicle to Shipment/ShipmentStage/TransportMeans (with the loading length), reference `BF-WB-26-0231` as shipping document, and describe the goods item once at shipment level (or drop TotalGoodsItemQuantity on the units); (b) repeat vehicle and goods item on every unit.
- Needs decision: no

## Checked and consistent
- SSCCs `095206102170000014` … `095206102170000069` and GRAIs pass their check digits (check_ids.py); prefix 952 is GS1's demonstration range. The SSCC of pallet 3 (`…038`) is the one the receipt advice 17 reports as damaged.
- Shipping marks "001 of 006" to "006 of 006" match the six handling units; 6 × 4 = 24 = DespatchLine quantity = order quantity (08) = invoice quantity (18).
- Gross weight 996 kg equals the consignment weight in 11 and the shipment weight in 13; see 11 for the weight per bench (about 34 kg, plausible).
- Loading length 13.6 m: a standard semi-trailer length (own knowledge). Six pallets of 1800 mm benches need at most about 6 × 1.0 m of loading length when placed two abreast across a 2.45 m wide trailer (own estimate), well within it.
- TransportMeansTypeCode `395` (Rec. 28 "Truck, with trailer") agrees with the separate trailer plate; Rec. 28 has no separate code for a tractor with semi-trailer.
- OrderReference `BS-PO-26-0224` and OrderLineReference `1` resolve to the order 08; consignment `LD-CS-26-0228` and carrier Bayforth agree with 11 and 13.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:ID` = `095206100000122217`: suspected that the GRAI repeats the bench's GTIN (its first 13 digits after the leading 0 are `9520610000012`, the GTIN of the bench) — refuted as a finding because a GRAI and a GTIN are different GS1 keys with different application identifiers, so the same digit string does not make them the same identifier; noted only because it may confuse a human reader.

## Outside this review
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-04-26`: benches made in Urvania (origin XU) on Sunday 2026-04-26 and despatched from the distributor's stock in Marrowdale, Bayvarra, on 2026-04-29 — whether manufacture, the cross-border transport and stocking fit in three days is a timeline question across flows.
