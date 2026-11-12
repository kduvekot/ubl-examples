# LLM review: 07-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/07-Invoice.xml`, Git blob `0e28c5a596e22d95a0c87b535ac9b772716f3863` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### ore/07#F1 · Low · Moisture deduction without any moisture value or agreement it can be checked against
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Moisture deduction`
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.015`
- Why: the line deducts 1.5 % of the value (14 414 504 × 0.015 = 216 217.56 → 216 218) for moisture, under reason code 64 "Special agreement". No XML example of the flow states a moisture content, a moisture limit or the agreement: the item carries only `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty/cbc:Name` = `Iron content`, the order (`01-Order.xml`) has no quality or moisture clause, and the assay referenced elsewhere in the flow (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID` = `SM-ASSAY-26-11`) is not referenced by the invoice and does not exist as an example. The buyer cannot verify the deduction from the documents, and "special agreement" points to an agreement nobody references. (In ore trade, by my own knowledge, moisture is usually settled by converting wet to dry tonnes against a measured moisture; a value deduction is a legitimate simplification if the basis is stated.)
- Condition: the invoice states the basis of the moisture deduction: the measured moisture (e.g. as an AdditionalItemProperty of the item) and/or a reference to the assay or agreement that fixes the 1.5 %.
- Options: (a) preferred: add the measured moisture as an item property and reference the assay certificate (AdditionalDocumentReference) from the invoice, keeping the allowance; (b) state the contractual rule in the allowance's reason text and reference the order or contract clause; (c) drop the deduction if the story has no moisture agreement.
- Needs decision: no

## Checked and consistent
- Price extension: 1788.4 × 8060 = 14 414 504 = `/Invoice/cac:InvoiceLine/cac:ItemPriceExtension/cbc:Amount` = `14414504` = `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:BaseAmount` = `14414504`; price and base quantity equal the order (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `8060` per tonne); quantity equals the despatched quantity of 04-DespatchAdvice.xml (1788.4 t).
- Allowance: 14 414 504 × 0.015 = 216 217.56 → `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:Amount` = `216218`; 14 414 504 − 216 218 = 14 198 286 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `14198286` = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `14198286`.
- Tax: 20 % of 14 198 286 = 2 839 657.2 → `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `2839657` = `/Invoice/cac:InvoiceLine/cac:TaxTotal/cbc:TaxAmount` = `2839657`; total 17 037 943 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `17037943` = `/Invoice/cac:InvoiceLine/cbc:TaxInclusiveLineExtensionAmount` = `17037943`. Price-extension tax 20 % of 14 414 504 = 2 882 900.8 → `2882901`, and 14 414 504 + 2 882 901 = `17297405`.
- Settlement discount: 2 % of 17 037 943 = 340 758.86 → `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `340759`; settlement period 11–21 March (10 days); due date 2026-04-10 = 30 days after issue, the same in DueDate, PaymentMeans and PaymentTerms.
- Payee account `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU420351041700000000104729` passes the IBAN-style check, is the seller's, and is the payee account in `08-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU420351041700000000104729`. RF reference `RF73SMINV260312` passes and is quoted back in the remittance advice.
- The remittance advice pays the full payable amount on 9 April, after the discount period and before the due date — consistent with no discount being taken.
- Supply type GOODS, category S 20 %, domestic sale within Urvania — consistent.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: suspected that a quality deduction needs another UNCL 5189 code — refuted: UNCL 5189 has no moisture or quality code, and "Special agreement" is a legitimate reading for a contractual deduction (the missing agreement is F1).
- `/Invoice/cbc:TaxPointDate` = `2026-03-11`: the goods were handed to the carrier on 10 March (FCA) — refuted as a finding: the element is defined as "The date of the Invoice, used to indicate the point at which tax becomes applicable"; the world's tax-point rule is outside what this review may consult.
- `/Invoice/cbc:AccountingCostCode` = `3100`: equal to the buyer's ISIC code — refuted, see the review of 01-Order.xml: it is Valdara's cost account in all 12 XML examples that carry it.
