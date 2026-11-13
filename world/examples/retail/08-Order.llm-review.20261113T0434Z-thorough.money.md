# LLM review: 08-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/08-Order.xml`, Git blob `4b9ab738473f9a4b2d8102ca056f226654c8875b` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/08#F1 · High · Taxable amount ignores the order's own allowance
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12480.00`
- XPath: `/Order/cac:AllowanceCharge/cbc:Amount` = `624.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11856.00`
- Why: `TaxableAmount` is "the net amount to which the tax percent (rate) is applied to calculate the tax amount". The order deducts a document-level promotion support of 624.00 (5 % of 12480.00), so the net amount of the order is 12480.00 − 624.00 = 11856.00, which is also its payable amount. The tax subtotal uses the gross line total instead. The invoice for the same order and the same allowance uses the net amount (`18-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `11856.00`), so order and invoice disagree on the tax base. The tax amount is not affected only because the rate is 0 %.
- Condition: The order's taxable amount equals the line extension amount minus the document-level allowance (11856.00), as in the invoice.
- Options: (a) preferred: 11856.00, because the allowance is applied at document level before tax; optionally give the allowance its tax category (E, RESALE) as the invoice does, so the allocation is explicit.
- Needs decision: no

### retail/08#F2 · Medium · Data sending capability describes the e-invoicing channel, not purchase card data
- XPath: `/Order/cac:SellerSupplierParty/cbc:DataSendingCapability` = `UBL 2.5 over the trade accord network`
- Why: `SupplierParty/DataSendingCapability` is "text describing the supplier's ability to send invoice data via a purchase card provider (e.g., VISA, MasterCard, American Express)". Nothing in the flow is paid by purchase card: the order and the invoice ask for credit transfer (`/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`; `18-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`). The value describes the electronic channel over which the supplier sends UBL documents, a meaning the element does not have. The element occurs in this example only (counted with `grep -rl --include='*.xml' DataSendingCapability world/examples/`).
- Condition: `DataSendingCapability` is absent, or describes the supplier's ability to pass invoice data through a purchase card provider in a flow where a purchase card is used.
- Options: (a) preferred: remove it, because the flow has no purchase card; the electronic channel is already visible from the parties' electronic addresses; (b) introduce a purchase card payment in a flow where it has a real reason.
- Needs decision: no

## Checked and consistent
- Line: 24 × 520 = 12480.00, at the catalogue's trade price (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`), inside the price band 4–192 and the price validity.
- Allowance: 12480.00 × 0.05 = 624.00; totals 12480.00 − 624.00 = 11856.00; the invoice bills the same (`18-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `11856.00`).
- Tax category E with exemption RESALE under STT, as in the catalogue, invoice and credit note.
- Payment terms "30 days net" match the catalogue's trading terms and the invoice's due date 2026-05-30.
- The buyer's accounting code 6120 "Garden department" is the one the invoice and credit note carry (`18-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `6120`).
- Delivery terms DDP match the catalogue and the invoice line (`18-Invoice.xml:/Invoice/cac:InvoiceLine/cac:DeliveryTerms/cbc:ID` = `DDP`).

## Considered and refuted
- `/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Promotion support`: suspected that the 5 % has no basis, since the catalogue offers only a 3 % discount and the retail event mentions no supplier contribution — refuted because an order may carry an allowance agreed for a promotion it refers to (`/Order/cac:AdditionalDocumentReference/cbc:ID` = `BS-RE-26-0222`), and the seller's invoice confirms the same 5 %.
- The catalogue's 3 % "Full container" discount (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`) is not applied to the 24 benches: suspected an omission — refuted for this example because six pallets on a truck are not a full container; the unclear condition is a finding of the catalogue's review (retail/02).
