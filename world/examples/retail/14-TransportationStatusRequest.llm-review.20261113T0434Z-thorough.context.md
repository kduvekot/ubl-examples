# LLM review: 14-TransportationStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/14#F1 · High · Three different carrier references for the same shipment
- XPath: `/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: CarrierAssignedID is "A reference number assigned by a carrier or its agent to identify a
  specific shipment, such as a booking reference number". For the one shipment (consignment
  `LD-CS-26-0228`) the carrier's reference is `BF-CMR-26-0217` on the waybill, `BF-WB-26-0231` here
  (which is the waybill's document ID, not a shipment reference) and `BF-ROAD-26-0231` in the carrier's
  own status answer. The carrier cannot find the shipment by a reference it did not assign.
- Condition: the request and the status carry the carrier's shipment reference as given on the
  waybill (or all three agree on one reference); a document number is not used as a shipment
  reference.
- Options: `BF-CMR-26-0217` here and in 15 (preferred); the waybill, if it is to be referenced, goes in
  a DocumentReference.
- Needs decision: no

### retail/14#F2 · High · Reference to a transport execution plan that the flow does not have
- XPath: `/TransportationStatusRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `BF-TEP-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: TransportExecutionPlanDocumentReference is "A reference to the Transport Execution Plan
  associated with the transport service for which status is requested". No example has the ID
  `BF-TEP-26-0227`; the flow has only Lumeway's request `LD-TR-26-0227`, and Bayforth's plan in answer
  to it is never issued. 10-DocumentStatus.xml reports the transport request as accepted, but by no
  document.
- Condition: the referenced plan exists in the flow, or the request refers to what does exist.
- Options: (a) add Bayforth's TransportExecutionPlan `BF-TEP-26-0227` to the flow (it would also
  settle 10's "booked"); (b) drop the reference and rely on the consignment ID.
- Needs decision: yes

### retail/14#F3 · Medium · The consignment ID given as the shipping order number
- XPath: `/TransportationStatusRequest/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/TransportationStatusRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- Why: ShippingOrderID is "A reference number for a shipping order". `LD-CS-26-0228` is the
  consignment's ID, carried in the same document as Consignment/ID; the shipping order (forwarding
  instruction) is the transport request `LD-TR-26-0227`.
- Condition: ShippingOrderID is the forwarding instruction's ID, or absent.
- Options: `LD-TR-26-0227` (preferred), or drop it.
- Needs decision: no

### retail/14#F4 · Medium · A language code in LocaleCode
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/14#F5 · Low · The buyer's order number in a request to the carrier
- XPath: `/TransportationStatusRequest/cac:DocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: the carrier's contract is with Lumeway; Brightmarket's purchase order appears in none of the
  carrier's documents (11, 13) and the carrier cannot look anything up by it. Without a document type
  the reference also does not say what it is.
- Condition: references in the request are to documents the carrier knows, or are typed and have a
  reason.
- Options: drop it (preferred).
- Needs decision: no

### retail/14#F6 · Low · Requested status location without identification
- XPath: `/TransportationStatusRequest/cac:RequestedStatusLocation/cbc:Name` = `Brightmarket Stores, goods-in`
- Why: RequestedStatusLocation is "A location for which status is requested". The name combines the
  company and the goods-in; the order identifies the goods-in by GLN `9522610900019`
  (`08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`).
- Condition: the location is identified as in the order (GLN or address).
- Options: add the GLN (preferred).
- Needs decision: no

### retail/14#F7 · Low · Signature and master data without use
- XPath: `/TransportationStatusRequest/cac:Signature/cbc:ID` = `LD-SIG-26-TSR`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: a status question needs no signature (here only an ID and a signatory), customs trader number
  or share capital (IND5/IND6).
- Condition: everything present has a use.
- Options: drop them.
- Needs decision: no

## Checked and consistent
- Sender Lumeway and receiver Bayforth are the transport user and provider of 11; the consignment
  `LD-CS-26-0228` is the one in 11, 12 and 13.
- TransportationStatusTypeCode "Status of delivery", the description "When will the benches arrive?"
  and the instruction "Answer with the expected delivery time." agree.
- 15-TransportationStatus.xml answers this request (its request reference is `LD-DOC-26-0232`) 50
  minutes later.

## Considered and refuted
- `/TransportationStatusRequest/cac:RequestedStatusPeriod/cbc:EndDate`: a status period that ends
  the day after the request — refuted because the truck may arrive the next day; the period covers the
  expected delivery window.
