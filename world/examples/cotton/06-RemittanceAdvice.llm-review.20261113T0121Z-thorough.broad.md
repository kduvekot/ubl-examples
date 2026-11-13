# LLM review: 06-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/06-RemittanceAdvice.xml`, Git blob `e26eebc8bac0997744bbae65cf8d2aa86a65b428` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### cotton/06#F1 · Low · The payment reference the invoice asked for is not quoted
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF77SCGSBI260194`
- XPath: `18-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF46SCGINV260210`
- Why: the self-billed invoice asks for its creditor reference RF77SCGSBI260194 to be quoted. The remittance advice gives neither a `PaymentID` nor an `InvoicingPartyReference`, so the farm's bank statement line cannot be matched by reference. The mill's remittance advice in the same flow quotes the reference it was asked for.
- Condition: the remittance advice quotes the creditor reference requested in 04.
- Options: (preferred) `PaymentMeans/PaymentID` = RF77SCGSBI260194 (and, if wanted, `InvoicingPartyReference`).
- Needs decision: no

### cotton/06#F2 · Low · No date of the payment
- XPath: `/RemittanceAdvice/cbc:IssueDate` = `2026-02-16`
- Why: a remittance advice "specifies details of an actual payment", but nothing says when the transfer is executed or value-dated (the issue date is only the date of the advice). The farm needs the date to reconcile the 3141.070 on its account and to see that the 45-day term (due 2026-03-24) was met.
- Condition: the payment's execution or value date is stated, or the document says that it equals the issue date.
- Options: (preferred) a payment date in the payment means or in the remittance lines (where the model offers one); or a note.
- Needs decision: no

### cotton/06#F3 · Low · The ginnery's paying contact is its sales desk
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the ginnery pays the farm here; questions about the remittance go to its farm-payments / accounts-payable desk (04 routes to "Farm payments"), not to lint sales.
- Condition: the accounting customer's contact handles payments.
- Options: (preferred) a farm-payments contact; or none.
- Needs decision: no

## Checked and consistent
- 3210.320 (payable of 04) − 69.250 (payable of 05) = 3141.070 = total payment amount.
- Line 1 refers to 04 and line 2 to 05, both exist; debit for the invoice, credit for the credit note.
- Payer account `XL31BSEL0020004922263` is the ginnery's (the same account receives the mill's payment in 18); payee account `XL67BSEL0020004817534` is the farm's account from 01 and 04; both check digits pass.
- Paid on 2026-02-16, before the invoice's due date 2026-03-24 and on the credit note's due date 2026-02-16.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount`: debit used for an amount the payer pays — refuted: from the payer's ledger the invoice is a debit to settle, the credit note a credit; consistent with 18.
- `/RemittanceAdvice/cbc:TotalPaymentAmount`: early payment of a 45-day invoice — refuted: paying before the due date is allowed and explains the set-off date.
