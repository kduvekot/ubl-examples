# LLM review: 08-Waybill.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: money

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

### rail/08#F1 · Low · Freight charge stated for only one of the two containers
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason` = `Rail freight per container`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:ID` = `FRXU1044180`
- XPath: `10-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2`
- XPath: `10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `109200`
- Why: TransportEquipment/FreightAllowanceCharge is "a freight allowance charge associated with this
  piece of transport equipment", and its Amount is "the monetary amount of this allowance or charge
  to be applied". Container FRXU1044175 carries the rail freight of 54,600 XUF; container
  FRXU1044180, equal in type (45G1), load and weight and carried on the same train, carries none. The
  waybill therefore shows freight of 54,600 XUF for the consignment, while the freight invoice that
  references this waybill bills 2 × 54,600 = 109,200 XUF.
- Condition: either both containers carry their freight charge, or the waybill states the freight in
  one place that covers both containers; in either case the freight in the waybill adds up to what
  10-Invoice.xml bills.
- Options: (a) preferred: give the second container the same FreightAllowanceCharge, since the
  charge is per container; (b) state the freight once for the consignment (e.g. on the consignment
  or shipment) and remove it from the equipment.
- Needs decision: no

## Checked and consistent
- Rate 54,600 XUF per container equals the unit price of the freight invoice
  (`10-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `54600`); reason code FC
  ("Freight service", UN/EDIFACT 7161) fits a freight charge; ChargeIndicator true.
- PrepaidPaymentTerms ("Freight prepaid by the consignor under DAP") agrees with
  `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Freight prepaid by the consignor under DAP.`,
  with the DAP terms of `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`, and with the freight
  invoice addressed to the consignor Valdara Industries.
- AdValoremIndicator false agrees with a freight charged per container rather than on the value of
  the goods; no declared value for carriage is given, so nothing contradicts it.
- The waybill's issue date (2026-04-14) is the start date of the payment terms agreed in
  03-TransportExecutionPlan.xml; the conflict with the invoice's due date is a finding of the reviews
  of 03 and 10.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms`: "prepaid" although the freight is
  invoiced on 2026-04-17 with 30 days to pay — refuted because "prepaid" is the freight term (charges
  borne by the consignor at origin, not collect from the consignee), not a payment in advance.
