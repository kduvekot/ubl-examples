# LLM review: 11-Invoice.xml

Flow: air (26-0416) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/air/11-Invoice.xml`, Git blob `115ce5628d025f15f6631b042a93127cf72e584a` (committed)
- Last commit changing the example: 771277df 2026-11-21 Rail lots per container, mast order DG identification, air timing and origin statement, sawmill buys its logs
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 1d8c94f3 2026-11-21 Reviews of the examples added since the November run (quick run 20261121T1048Z), first files
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### air/11#F1 · High · The air part of the order is exempt as "in transit", the sea part of the same order as an export
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `TRANSIT`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `TRANSIT`
- XPath: `/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `TRANSIT`
- XPath: `sea/22-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- Why: Both invoices are Lumeway Distribution's, to Velumi Trading, for the same order 26-0417 (`sea/22-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `26-0417`), and both sets of goods are despatched by Lumeway from Bayvarra to Lisavu (here by air, 08-DespatchAdvice.xml, despatch supplier Lumeway). The sea invoice exempts the state sales tax as "Export outside Bayvarra"; this one as "Goods in transit through Bayvarra". Goods that Lumeway sells and despatches itself are exported from Bayvarra; nothing in the air flow says the side frames pass through Bayvarra without entering Lumeway's stock (no transit declaration, and 08 is despatched by Lumeway). One of the two reasons is wrong for the same kind of supply, or the difference is unexplained. The order change `01-OrderChange.xml` carries `TRANSIT` as well.
- Condition: the exemption reason of the side frames agrees with how they move (export from Lumeway's stock, or transit under a customs procedure stated in the flow), and the two invoices of order 26-0417 use the same reason for the same kind of supply, or state why they differ.
- Options: (a) preferred: `EXP` "Export outside Bayvarra", as in sea/22, here and in 01-OrderChange — the side frames leave from Lumeway's own despatch; (b) keep `TRANSIT` and make the transit real in the flow (the frames come from Valdara under a transit procedure and are only routed through Lumeport airport), which changes the story.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 8 × 64 = 512.00; 512.00 + 714.00 = 1226.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1226.00`; 1.5 % of 1226.00 = 18.39 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `18.39`.
- The freight charge 714.00 is Bayforth's invoice to Lumeway at cost: 10-Invoice.xml, 105 kg chargeable × 6.8 = 714.00, as the note and 01's "we pay the air freight as a surcharge at cost" say.
- Line 4, 8 side frames at 64 lume, item identifiers, accounting cost `500` "Stock for municipal projects" and CPT Selanu airport agree with 01-OrderChange.xml; `/Invoice/cac:DespatchDocumentReference/cbc:ID` = `LMW-DA-26-1018` is the replacement despatch advice 08 (after the cancellation 07 of 06), with 8 units.
- ProfileExecutionID `26-0416` is that of the order sea/05-Order.xml and of 01.
- GLN, GTIN, RF reference and the payee account pass `check_ids.py`; due date 30 days after the issue date; penalty period starts the day after.
- Contacts fit the roles (accounts receivable / accounts payable).
- Criterion S ("sufficiently processed") fits iron castings made in Urvania by the manufacturer of `VI-C180`.

## Considered and refuted
- `/Invoice/cac:OrderReference/cbc:ID` = `26-0417` while line 4 was added by the order change 26-0065 — refuted: the change amends that order, and the order line reference `4` is the added line.
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5` is per month only in the note — refuted: the element has no time basis, and the amount is one month's surcharge.
