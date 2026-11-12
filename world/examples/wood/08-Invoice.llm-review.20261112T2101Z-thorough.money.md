# LLM review: 08-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/08-Invoice.xml`, Git blob `cc18be7786d6372f4c7794e335c9b6d55250ba96` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### wood/08#F1 · Low · Export exemption claimed without anything in the invoice that shows the goods leave Bayvarra
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `G`
- Why: the invoice charges no state sales tax because the goods are exported (category G, reason EXP). Apart from the buyer's Urvanian address, the invoice carries nothing that supports the export: no Delivery (delivery location or country, actual delivery date), no delivery terms (DAP Ferrano, in the order) and no reference to the export declaration MS-EX-26-0630 (05-ExportCustomsDeclaration.xml) or the despatch advice MS-DA-26-0633 (06-DespatchAdvice.xml). In sales-tax and VAT practice (my own knowledge) the export exemption rests on the goods being shipped out, which the invoice usually shows by the place of delivery or a reference to the export evidence; the buyer's address alone does not establish where the goods go.
- Condition: the invoice states where the goods are delivered (country XU) or references the export evidence (export declaration or despatch advice), so the exemption can be checked from the invoice and its references.
- Options: (a) preferred: add a Delivery with the delivery location in Ferrano (XU) and the actual delivery date, and an AdditionalDocumentReference to MS-EX-26-0630; (b) only the DespatchDocumentReference to MS-DA-26-0633.
- Needs decision: no

### wood/08#F2 · Low · The charged pallets appear in no document that describes the goods
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`
- Why: the invoice charges 240.00 XBL for heat-treated export pallets, but none of the documents that describe the shipment (04-TransportExecutionPlanRequest.xml, 05-ExportCustomsDeclaration.xml, 06-DespatchAdvice.xml, 07-ImportCustomsDeclaration.xml) has a pallet, package or transport handling unit (searched over `wood/*.xml` for pallet, Package, HandlingUnit: only the charge itself in 02, 03 and 08). The object of the charge cannot be linked to the goods shipped.
- Condition: the pallets that the charge is for are visible in the despatch advice (or another shipment document of the flow), with a count that makes 240.00 XBL plausible.
- Options: (a) preferred: describe the pallets as transport handling units in the despatch advice (and the transport request), e.g. a number of pallets of 50-slat bundles; (b) drop the charge if the slats are not shipped on charged pallets.
- Needs decision: no

## Checked and consistent
- Arithmetic: 4800 EA × 7.2 XBL / 1 EA = 34560.00 LineExtensionAmount; + 240.00 ChargeTotalAmount = 34800.00 TaxExclusiveAmount; tax 0.00; TaxInclusiveAmount = PayableAmount = 34800.00.
- Tax: the one subtotal's TaxableAmount 34800.00 = line 34560.00 (ClassifiedTaxCategory G) + charge 240.00 (TaxCategory G); G/0 %/EXP under STT fits a sale from Upland State (XB) to Urvania; tax scheme currency XBL = document currency, so no tax currency is needed.
- Price, quantity, charge and currency agree with the order `03-Order.xml` (VI-PO-26-0627) and the quotation.
- Terms: DueDate 2026-03-28 = issue date 2026-02-26 + 30 days ("30 days net"); PaymentDueDate the same in PaymentMeans and PaymentTerms; PenaltySurchargePercent 1.5 × 34800.00 = 522.00 PenaltyAmount for the one-month PenaltyPeriod starting 2026-03-29, the day after the due date; PaymentTerms/PaymentMeansID 1 resolves to PaymentMeans/ID 1.
- Payment means: RF83MSINV260635 has a valid ISO 11649 check (check_ids.py) and is quoted in the instruction note and used by the remittance advice; the payee account XB78BLUM38712004398618 has a valid check, its bank code BLUM and branch 387120 agree with the BIC-like BLUMXBLX and the branch ID; account name = the seller's registration name; account currency XBL = payment currency.
- ChargeBearerCode SHAR and channel RTNS with rail TRADE-ACCORD-PAY fit a cross-border credit transfer XU→XB; the domestic invoice 11-Invoice.xml uses MPNS/LUMEPAY, consistently.
- Paid in full: 09-RemittanceAdvice.xml pays 34800.00 XBL on 2026-03-26, before the due date, balance 0.00.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR`: suspected that shared charges would leave the payee with less than 34800.00, contradicting the remittance's full payment — refuted because SHAR means each party bears its own bank's charges; the remittance states what the payer sends, and the payee's own charges do not change the amount paid.

## Outside this review
- 06-DespatchAdvice.xml and 04-TransportExecutionPlanRequest.xml describe no packaging or handling units at all; whether they should (for the shipment's own sake) belongs to their reviews (see F2 for the link to the charge).
