# LLM review: 04-DespatchAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/04-DespatchAdvice.xml`, Git blob `d5694687ad07a0bd4b1b8412513e13a712a00375` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### road/04#F1 · High · Despatch advice issued before the despatch it reports as actual
- XPath: `/DespatchAdvice/cbc:IssueTime` = `15:15:00`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate` = `2026-03-23`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `16:20:00`
- Why: The document is issued on 2026-03-23 at 15:15 but reports an actual despatch on the same day at 16:20, 65 minutes in the future. An "actual" time cannot be known before it happens; both times are local times of the same place (Ferrano, TimezoneOffset -1 in the despatch address of the order).
- Condition: the issue time is not earlier than every actual event the despatch advice reports (or the event is given as estimated).
- Options: (a) preferred: issue the despatch advice after the truck has left (e.g. 16:30), which also fits its role of advising the consignee of goods on the way; (b) keep the issue time and give the departure as an estimate.
- Needs decision: no

### road/04#F2 · High · Emission factor × base does not give the emission value
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated. No other reading fits: 96 / 0.82 = 117.1, which is neither a count in the flow, nor the bench's materials (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg net). The same three values are in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) preferred: relate the factor to the activity it really measures (e.g. per kg of steel, base in KGM), so the value can be recalculated; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep the total.
- Needs decision: no

### road/04#F3 · Medium · "Actual despatch (pickup)" time is the departure, not the pickup
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `16:20:00`
- Why: ActualDespatchTime is "the actual despatch (pickup) time". The waybill records the carrier's pickup at 15:05 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`) and the departure at 16:20 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`); the transportation status repeats the 15:05 pickup (`09-TransportationStatus.xml:/TransportationStatus/cac:UpdatedPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`). The despatch advice therefore gives the departure time in an element defined as the pickup.
- Condition: ActualDespatchTime equals the pickup time the transport documents record (15:05), or the transport documents and the despatch advice agree on one pickup time.
- Options: (a) preferred: 15:05 in the despatch advice (the hand-over to the carrier, which is also the FCA delivery); (b) if 16:20 is meant to be the hand-over (after export release), move the waybill's pickup event to 16:20.
- Needs decision: no

### road/04#F4 · Low · Side frames despatched without saying they are the substituted 2026 casting
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- Why: The order response replaced the ordered side frame by the 2026 casting with a reinforced foot (`02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`), and the 2025 version is also offered there as a proposed substitute. The despatch advice, which tells the consignee what was actually shipped, identifies the item only as VI-C180 without the version, so it cannot be told which casting is on pallet 25. No example after the order response carries ExtendedID 2026 (`grep -l '<cbc:ExtendedID>2026<'` over `road/*.xml` finds only 02); the application response says the invoice line "matched the substituted casting" (`16-ApplicationResponse.xml`), which the goods documents do not show.
- Condition: the despatch line identifies the casting version actually shipped in the same way the order response does (SellersItemIdentification/ExtendedID or an equivalent property), and the receipt and customs documents agree with it.
- Options: (a) preferred: carry ExtendedID 2026 on line 2 (and on the documents that follow); (b) if the item number alone is enough by agreement, drop the version distinction from the order response.
- Needs decision: no

### road/04#F5 · Low · Release identifier that no other example issues
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ReleaseID` = `XU-EX-REL-55120`
- Why: ReleaseID is "an identifier for the release of the despatch used as security control or cargo control (pick-up)"; its prefix makes it an export release by Urvanian customs. The export declaration of this shipment (`05-ExportCustomsDeclaration.xml`, IDs VI-EX-26-0155 and VI-CD-26-0156) carries no release number, and the waybill only says the truck waits until customs has released the declaration. The release cannot be linked to the declaration it belongs to.
- Condition: the release identifier can be traced to the export clearance it confirms (e.g. the same number appears with the export declaration or its acceptance), or ReleaseID is absent.
- Options: (a) preferred: let the export declaration (or the waybill's customs reference) carry the same release number; (b) remove ReleaseID.
- Needs decision: no

## Checked and consistent
- Delivered quantities 96 and 12 equal the order lines and the order response; LineCountNumeric 2 = number of despatch lines.
- Shipment ID CL-SH-26-0154, consignment ID LD-CS-26-0152 and gross weight 4106.4 kg are the same in the waybill, the customs documents and the certificates of origin.
- Note "24 pallets of 4 benches" agrees with the waybill's 24 bench pallets of 4 packages each (`08-Waybill.xml`, TransportHandlingUnit[1]–[24]) plus one pallet of 12 boxes.
- Manufacture date 2026-03-20 of the bench lot and of the 12 side-frame instances lies before the despatch; the 12 serials VI-SF-01490 … 01501 are consecutive and unique.
- Packaging waste 0.4 kg per bench × 96 = 38.4 kg, within the 344.4 kg difference between gross (4106.4) and net (3762) weight in the waybill.
- Physics of the bench: 34 kg steel + 22.5 kg hardwood consumed per bench against an implied net bench weight of about 38 kg (waybill net 3762 kg for 96 benches and 12 castings): consumption includes casting and sawing losses, so the figures are compatible.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure`: Shipment gross weight is defined as "goods plus packaging plus transport equipment", yet equals the consignment gross weight without equipment (4106.4) — refuted because the goods travel loose on the haulier's trailer, with no container or other transport equipment of the shipment; the trailer is part of the means of transport.
