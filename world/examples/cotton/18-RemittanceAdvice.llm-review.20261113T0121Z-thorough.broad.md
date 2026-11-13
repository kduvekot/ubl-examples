# LLM review: 18-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/18-RemittanceAdvice.xml`, Git blob `47eb48a5adfeabc95404a79c9aab2a6843d04e46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit c959f36 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/18#F1 · Medium · Language code in `LocaleCode`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2: an ISO 639 language code in an element for a locale, repeating `Language/ID`.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/18#F2 · Low · The invoice referenced twice in the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SCG-INV-26-0210`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SCG-INV-26-0210`
- Why: the line already refers to the invoice through the dedicated `BillingReference/InvoiceDocumentReference`; the generic `DocumentReference` ("A reference to a document associated with this remittance advice line") repeats the same invoice with the same date and adds only a type code.
- Condition: each referenced document appears once per line, in the element meant for it.
- Options: (preferred) drop the generic document reference.
- Needs decision: no

### cotton/18#F3 · Low · The payer's contact is its purchasing desk in sales
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: as cotton/02#F3; questions about a payment go to the mill's accounts payable.
- Condition: the payer's contact handles payments, with name and department that agree.
- Options: (preferred) an accounts-payable contact.
- Needs decision: no

### cotton/18#F4 · Low · The ginnery's and its bank's English addresses tagged as Bayvarran English
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Reef Street`
- Why: as cotton/02#F4: the same renderings of Lisavan addresses carry `en-XL` in 01, 04, 06 and 16 and `en-XB` here.
- Condition: the same rendering carries the same tag in every example.
- Options: (preferred) `en-XL`.
- Needs decision: no

## Checked and consistent
- Total debit 6055.452 − total credit 0.000 = total payment 6055.452 XLC = payable amount of 16; balance 0.000.
- Paid on 29 March, before the due date in 16; the creditor reference `RF46SCGINV260210` requested in 16 is quoted (payment ID and invoicing-party reference; check digits pass).
- Payer account `XB35BLUM38020504608076` (mill, Bank of Lumeport) and payee account `XL31BSEL0020004922263` (ginnery, the account of 06 and 16) pass their check digits; payment purpose SUPP fits a supplier payment.
- Payment order reference and instruction ID are the same (LTM-PAY-26-0191), as expected for one transfer.

## Considered and refuted
- `/RemittanceAdvice/cbc:TotalCreditAmount`: a zero credit total as filler — refuted: it states explicitly that no credit is set off, which the reader could otherwise not tell (IND6).
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode`: a Lume account paying a coral amount — refuted: the bank converts; the invoice asked for payment in coral.
