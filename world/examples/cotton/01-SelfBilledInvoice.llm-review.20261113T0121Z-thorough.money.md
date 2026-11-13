# LLM review: 01-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/01-SelfBilledInvoice.xml`, Git blob `aee01edf4f4e0c209dc01462389e7115dcceae7c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/01#F1 · High · Payment due date of the means contradicts "paid on issue"
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27`
- XPath: `/SelfBilledInvoice/cbc:DueDate` = `2026-01-13`
- XPath: `/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `Paid on issue by transfer. No presumptive tax is withheld…`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-01-13`
- Why: `PaymentMeans/PaymentDueDate` is "the date on which payment is due for this means of
  payment". The only means of payment is the credit transfer, so the advance is due by transfer on
  2026-02-27, while the invoice's `DueDate` ("the date on which Invoice is due") is the issue date,
  the payment terms say the advance is paid on issue, and the final self-billed invoice records the
  advance as paid on 2026-01-13. 2026-02-27 is exactly 45 days after the issue date, i.e. the
  standard "45 days net" terms of `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentTerms/cbc:Note`
  = `45 days net.` appear to have been applied to an advance that is paid at once.
- Condition: every due date in the document (`DueDate`, `PaymentMeans/PaymentDueDate`, and any
  other) is the same date, the one on which the advance is paid, and agrees with the payment terms
  and with the paid date recorded in 04.
- Options: (a, preferred) set `PaymentMeans/PaymentDueDate` to 2026-01-13, which matches the note
  and 04; (b) drop `PaymentMeans/PaymentDueDate`, since `DueDate` already says it.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `4500` kg × `/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.226` per 1 kg = 1017.000 = line extension, tax exclusive, tax inclusive and payable amount; tax 0.000 on the O subtotal of 1017.000.
- The advance is 4 500 kg, a quarter of the 18 000 kg delivered and billed in `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `18000`, at the same price 0.226; 04 deducts it as `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:PrepaidAmount` = `1017.000` and cites this invoice with its issue date in `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BillingReference/cac:SelfBilledInvoiceDocumentReference/cbc:IssueDate` = `2026-01-13`.
- The payment terms note (no presumptive tax and no cotton fund levy on the advance) agrees with 04, which withholds the tax and adds the levy on the delivery only; no `WithholdingTaxTotal` is present here.
- `check_ids.py`: RF reference `RF61SCGSBI260191` and account `XL67BSEL0020004817534` have valid check digits; the account is the farm's (payee = seller in this self-billing relation) and is the same account as in 04.
- Tax category O ("outside scope of tax") with the scheme named "No general sales tax" is the same treatment the flow uses for the farm's supplies in 04 and 05; neither Lisavu party carries a `PartyTaxScheme`, which agrees with a country without a general sales tax.

## Considered and refuted
- `/SelfBilledInvoice/cbc:InvoiceTypeCode` = `386`: a prepayment invoice type in a SelfBilledInvoice document was suspected of conflicting with the self-billed type 389 — refuted because the document type already states self-billing and 386 states what this invoice is (an advance), which 04 then deducts.
- `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: real-time gross settlement for a small advance to a micro farm was suspected of being implausible — refuted because the island's interbank rail (`CORAL-NET`) is the world's given rail and the advance is said to be paid on issue, which a real-time channel supports.
- `/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice SCG-SBI-26-0191`: suspected duplicate of the remittance information — refuted because the definition ("free-form text applying to the Payment for the owner of this account") fits a note for the farm's statement, and it names this document correctly.
