# LLM review: 14-TransportationStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/14-TransportationStatusRequest.xml`, Git blob `e728f33a6fcfaa9b61feef53866fa38361baf8dd` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/14#F1 · High · Reference to a transport execution plan that does not exist
- XPath: `/TransportationStatusRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `BF-TEP-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: TransportExecutionPlanDocumentReference is "A reference to the Transport Execution Plan associated with the transport service for which status is requested". No example has the ID `BF-TEP-26-0227` (`grep -rn --include='*.xml' 'BF-TEP' world/examples`: this file only). The flow contains Lumeway's request 11 (`LD-TR-26-0227`, "Please confirm by return"), but no Transport Execution Plan from Bayforth answering it.
- Condition: the reference resolves to a transport execution plan that exists in the flow, or the reference is absent (and, if wanted, the request 11 is referenced through a generic document reference with its type).
- Options: (a) add Bayforth's Transport Execution Plan `BF-TEP-26-0227` to the flow, between 11 and 13 (it would also give 10's "booked" a basis); (b, simpler) drop this reference and reference `LD-TR-26-0227` as a DocumentReference of type "Transport execution plan request".
- Needs decision: yes (adding a document to the flow)

### retail/14#F2 · High · Carrier-assigned ID holds the waybill's document number, which differs from the carrier's own reference
- XPath: `/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:ID` = `BF-WB-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: CarrierAssignedID is "A reference number assigned by a carrier or its agent to identify a specific shipment, such as a booking reference number". The value is the ID of the waybill document 13, not a shipment reference; the waybill gives Bayforth's shipment reference as `BF-CMR-26-0217`, and the answer 15 uses yet another value. A document ID used as a shipment reference, and three values for one shipment.
- Condition: the carrier-assigned ID is the carrier's shipment reference, the same as in 13 and 15; a reference to the waybill, if wanted, is a document reference.
- Options: (a, preferred) `BF-CMR-26-0217`, as in 13; (b) a document reference to `BF-WB-26-0231` in addition.
- Needs decision: no

### retail/14#F3 · Medium · Shipping order ID holds the consignment ID
- XPath: `/TransportationStatusRequest/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/TransportationStatusRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- Why: ShippingOrderID is "A reference number for a shipping order". `LD-CS-26-0228` is the consignment (the same value is the Consignment ID of this document, and of 11, 12, 13). The shipping order/forwarding instruction is 11, `LD-TR-26-0227`. Same misuse as in 13.
- Condition: ShippingOrderID, if present, identifies the shipping order, not the consignment.
- Options: (a, preferred) `LD-TR-26-0227`; (b) drop it.
- Needs decision: no

### retail/14#F4 · Low · Requested status location without the goods-in GLN
- XPath: `/TransportationStatusRequest/cac:RequestedStatusLocation/cbc:Name` = `Brightmarket Stores, goods-in`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: The location for which status is requested is the store's goods-in, which the order identifies by GLN `9522610900019`; the request names it in free text only, which does not say which store.
- Condition: the requested status location identifies the goods-in (by its GLN).
- Options: add Location/ID `9522610900019`.
- Needs decision: no

## Checked and consistent
- Issue time 10:59 on 2026-04-29 is after the waybill (08:56) and before the answer 15 (11:49); TransportationStatusTypeCode `DELIVERY` and "When will the benches arrive?" agree with the requested period 2026-04-29 to 2026-04-30.
- Consignment `LD-CS-26-0228` and DocumentReference `BS-PO-26-0224` (order 08) resolve.
- "The promotion starts soon": the promotion starts 2026-05-11 (06).
