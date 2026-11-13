# LLM review: 06-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

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

### cotton/06#F1 · Low · The transfer's payment reference is not given
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentID` = `RF77SCGSBI260194`
- Why: a remittance advice "specifies details of an actual payment". The self-billed invoice asks
  for the transfer to quote `RF77SCGSBI260194`, and the farm's bank statement will show the
  transfer under some reference; the remittance advice names the transfer only by its means code,
  without the payment identifier that ties the 3 141.070 on the statement to this advice. The
  billing references tie the advice to the documents, but not to the transfer.
- Condition: the remittance advice identifies the transfer it describes by the reference the
  transfer carries.
- Options: (a, preferred) add `PaymentMeans/PaymentID` with the reference quoted on the transfer;
  (b) leave it, if the amount and date are considered enough for the farm's matching.
- Needs decision: no

## Checked and consistent
- Total: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `3210.320` (the payable amount of 04) − `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `69.250` (the payable amount of 05) = 3 141.070 = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `3141.070`, positive as the definition requires.
- Billing references: SCG-SBI-26-0194 is 04 and SCG-SBC-26-0195 is 05; 05's set-off note and payment means 97 agree with netting it here, and 05's `DueDate` 2026-02-16 is this advice's issue date.
- Accounts: the payee account `XL67BSEL0020004817534` is the farm's, the same as in 01 and 04; the payer account `XL31BSEL0020004922263` is the ginnery's; both pass `check_ids.py`, both are coral accounts as the document currency.
- The advance of 01 (1 017.000, paid on issue) is correctly not part of this payment: 04 already deducts it as prepaid.
- Payment on 2026-02-16 is before 04's due date 2026-03-24, so no penalty interest arises.
