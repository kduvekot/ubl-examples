# LLM review: 02-OrderResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/02-OrderResponse.xml`, Git blob `4fa9a01f7c53c819946f93ff994818f91259d67f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### road/02#F1 · Medium · The party "who picks up the goods" is the 3PL that hands them over
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:ResponsibleParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Despatch/ResponsibleParty is defined as "the party who picks up the goods". Castrano Logistics is the seller's warehouse that loads and despatches the goods (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`); the goods are picked up by the buyer's carrier Trasvia Haulage, named in the order (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`) and recorded as performing the pickup in `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`.
- Condition: ResponsibleParty, if present, is the party that picks up the goods (the carrier Trasvia Haulage, XU-R-104822); the despatching 3PL is not given in that element.
- Options: (a) preferred: name Trasvia Haulage as ResponsibleParty, since the seller's confirmation of who collects is useful under FCA; (b) remove ResponsibleParty and, if the 3PL needs naming, use Despatch/DespatchParty as the order does.
- Needs decision: no

### road/02#F2 · Low · Promised delivery day earlier than the guaranteed despatch
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchDate` = `2026-03-24`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchTime` = `12:00:00`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:EstimatedDespatchPeriod/cbc:EndDate` = `2026-03-24`
- Why: Under the FCA terms of the order the seller's delivery is the hand-over to the carrier at despatch. The response promises delivery on 2026-03-23 only, but guarantees despatch (pickup) only by 2026-03-24 12:00 and estimates despatch over 23–24 March, so its own guarantee allows a despatch after the promised delivery period. Read as a target (promise) and a fallback (guarantee) the values can coexist, which is why this is Low; but then the promised period should not end before the guaranteed despatch.
- Condition: PromisedDeliveryPeriod covers the guaranteed despatch time, or the guaranteed despatch lies within the promised delivery period.
- Options: (a) preferred: extend PromisedDeliveryPeriod/EndDate to 2026-03-24 (matching the estimated despatch period); (b) set the guaranteed despatch to 2026-03-23.
- Needs decision: no

## Checked and consistent
- Estimated despatch 2026-03-23 14:00 equals the requested despatch in `01-Order.xml:/Order/cac:Delivery/cac:Despatch/cbc:RequestedDespatchTime` = `14:00:00`; actual despatch on 2026-03-23 (`04-DespatchAdvice.xml`) lies inside the estimated and guaranteed windows.
- Order line quantities 96 and 12 are repeated unchanged; OrderReference LD-PO-26-0149 resolves to `01-Order.xml`.
- NotifyParty Lumeway Distribution is the consignee in the transport documents.
