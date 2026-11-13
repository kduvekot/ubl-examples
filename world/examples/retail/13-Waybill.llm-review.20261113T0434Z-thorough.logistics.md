# LLM review: 13-Waybill.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/13-Waybill.xml`, Git blob `0e28ae8a70150ecfdb1e12ab9527a6f9336f5e5e` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 51ac641 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/13#F1 · High · Three different carrier references for the same shipment
- XPath: `/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: CarrierAssignedID is "An identifier (in the form of a reference number) assigned by a carrier or its agent to identify a specific shipment". Bayforth's own reference for shipment LD-SH-26-0230 is `BF-CMR-26-0217` here, the status request 14 quotes the waybill's document ID as the carrier reference, and Bayforth's own status 15 uses a third value. A shipment has one carrier reference; the forwarder would not recognise its own shipment from 14.
- Condition: the carrier-assigned shipment reference is the same in 13, 14 and 15.
- Options: (a, preferred) keep `BF-CMR-26-0217` (the waybill, issued first, is where the carrier assigns it) and use it in 14 and 15; (b) another single value, used in all three.
- Needs decision: no

### retail/13#F2 · Medium · The consignment note lacks the goods, the packages and the places and dates of taking over and delivery
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `996`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- Why: A Waybill is "A transport document describing a shipment"; this one declares itself a CMR consignment note, whose required particulars include the place and date of taking over the goods, the place designated for delivery, the description of the goods, the number of packages with their marks and numbers, and the gross weight (CMR Art. 6(1); own knowledge). Only the gross weight is present: no goods item or description, no handling units or packages (12 has six pallets marked "BRIGHTMARKET LUMEPORT / 001 of 006" …), no pick-up or delivery location, no date of taking over. The consignee is named, but not where the goods are to be delivered. The document's purpose depends on these.
- Condition: the waybill describes the goods (description, number and kind of packages, marks), the place and date of taking over, and the place of delivery.
- Options: (a, preferred) Shipment/GoodsItem with description and the six pallets (TransportHandlingUnit with SSCC and marks, or a package count), Shipment/Delivery with the delivery location `9522610900019` and the pick-up (Despatch) at the distribution centre with its date; (b) at least goods description, number of pallets and both places.
- Needs decision: no

### retail/13#F3 · Medium · Shipping order ID holds the consignment ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". `LD-CS-26-0228` is the consignment's ID (the same value two elements further down). The forwarding instruction for this transport is Lumeway's transport execution plan request 11, `LD-TR-26-0227`. The same misuse is in 14.
- Condition: ShippingOrderID, if present, is the identifier of the shipping order/forwarding instruction, not of the consignment.
- Options: (a, preferred) ShippingOrderID `LD-TR-26-0227`; (b) drop it, since the consignment ID is already present.
- Needs decision: no

### retail/13#F4 · Low · Distribution list contradicts the note about three originals
- XPath: `/Waybill/cbc:Note` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyIdentification/cbc:ID` = `20410274`
- Why: The note says the consignor (Lumeway, `20410274`) gets an original; the distribution list gives Lumeway an electronic copy and lists only one original (the consignee's, `ORIGINALWITHGOODS`). The carrier's original is not listed either (it may be implied for the issuer, but nothing may be implied by absence).
- Condition: the distribution list and the note describe the same originals and copies.
- Options: (a, preferred) list the consignor's original (and the carrier's) as distributions, keeping the electronic copy if wanted; (b) change the note.
- Needs decision: no

### retail/13#F5 · Low · CMR named for a domestic road transport
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cbc:Description` = `The forwarder's truck from the distribution centre to the store.`
- Why: The CMR Convention applies to contracts for the carriage of goods by road where the place of taking over and the place of delivery are in two different countries (CMR Art. 1; own knowledge). This transport runs from Marrowdale to Lumeport, both in Bayvarra (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:CityName` = `Marrowdale`). Some countries apply the CMR rules to domestic carriage by national law; if Bayvarra does, the document should say it is a national consignment note under that law.
- Condition: the legal basis named for the consignment note fits a domestic transport in Bayvarra (national road-carriage rules, or CMR applied by Bayvarran law, stated as such).
- Options: (a) name it a national consignment note; (b) keep CMR and record in the world that Bayvarra applies the CMR to domestic carriage.
- Needs decision: yes (legal framework of the world)

### retail/13#F6 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeway Distribution`
- Why: IssueLocation is "The location where this waybill was issued"; the name is the consignor's company, not a place. The place is Lumeway's distribution centre in Marrowdale, where the goods were taken over.
- Condition: the issue location names (or identifies) the place.
- Options: (a, preferred) "Lumeway distribution centre, Marrowdale" with its address or GLN; (b) the city.
- Needs decision: no

## Checked and consistent
- Shipment ID `LD-SH-26-0230`, consignment ID `LD-CS-26-0228` and gross weight 996 kg agree with 11 and 12.
- Issue time 08:56 on 2026-04-29 precedes the "on its way" status of 15 (11:49), which fits a note handed over at loading; the status request 14 (10:59) follows it.
- Consignor (Lumeway), carrier (Bayforth) and consignee (Brightmarket) agree with 11 and 12; the invoice 16 references this waybill by its ID.
