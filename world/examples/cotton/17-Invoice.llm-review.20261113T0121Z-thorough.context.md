# LLM review: 17-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/17-Invoice.xml`, Git blob `7bc3532e1225094de3f9e7a64900c767d56742c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/17#F1 · Low · The ocean carrier's tax registration and master data in the forwarder's freight invoice
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Tidewell Ocean Lines`
- Why: The invoice is Bayforth's bill to the mill for sea freight. Naming the carrier the freight
  was booked with is useful (the item says "booked with the ocean carrier"), but the carrier party
  also carries its state sales tax registration and the rest of its party record. The carrier is
  not a party to this invoice's tax: the tax treatment (exempt, service to a business) is the
  forwarder's supply to the mill. The carrier's tax data reads as copied master data that the
  invoice does nothing with (UBL IND5).
- Condition: the carrier party in the invoice carries only what identifies the carrier.
- Options: (a, preferred) reduce the carrier to its identification and name.
- Needs decision: no

## Checked and consistent
- 1 service unit × 2,950 XBL = 2,950.00 XBL = all totals; tax exempt (E) with a transaction exemption
  reason, tax 0.00.
- Due date 2026-04-03 is 30 days after issue, as "30 days net" says; penalty 1.5 % of 2,950.00 =
  44.25 XBL; the penalty period starts the day after the due date.
- Freight is billed by the buyer's forwarder to the buyer (mill), which fits FOB (08) and "Freight
  collect" (13); one 40-foot container fits the container of the VGM 12 (tare 3,750 kg).
- AdditionalDocumentReference TOL-BL-26-0206 resolves to 13; consignment LTM-CS-26-0201 is the one
  of 09, 11 and 13; the carrier is the B/L's carrier.
- RF08BFINV260211 and XB40BLUM38020502618225 pass `check_ids.py`.

## Considered and refuted
- `/Invoice/cbc:AccountingCost` = `Raw cotton`: the buyer's raw cotton cost centre on a freight
  invoice suspected as wrong — refuted because freight to the mill is part of the landed cost of the
  raw cotton, which a buyer commonly books to the same cost centre.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `MPNS`: a mass payment net system for a
  single business payment — refuted because domestic B2B credit transfers commonly run through such
  (ACH-type) systems.
