# LLM review: 36-RemittanceAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/36-RemittanceAdvice.xml`, Git blob `0d67d6237dbe199fe762a5dccb67b4360d07c700` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/36#F1 · High · The debit note is deducted as a credit although, as issued, it is a debt of the payer
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount` = `6.48`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cac:BillingReference/cac:DebitNoteDocumentReference/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `521.68`
- Why: the line deducts 6.48 lume from the payment and gives a debit note as the reason. In the debit note referenced the supplier is the creditor and the department the debtor (`34-DebitNote.xml:/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`, payable amount 6.48), so by that document the department would have to add 6.48, not deduct it; the payment would be 12.96 lume higher. The remittance advice follows what the debit note means (the department's penalty against the supplier), which is not what it encodes. See 34#F1 of this part.
- Condition: the side of the line (debit or credit) agrees with who is creditor and debtor in the referenced document, and `TotalCreditAmount`/`TotalPaymentAmount` follow.
- Options: (a, preferred) correct the parties of the debit note (34#F1 option (a)); this line and the totals then stand; (b) if the penalty becomes the supplier's credit note, reference it as a credit note.
- Needs decision: yes

### tender/36#F2 · Medium · The payer pays interest for 1 to 5 May without objection, on a due date its own contract does not give
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cbc:DebitLineAmount` = `22.23`
- XPath: `/RemittanceAdvice/cbc:Note` = `Payment of the first release, with the interest.`
- Why: the department pays the reminder's interest in full. Its own contract sets the payment term at `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` and contains no interest clause; the release was installed late (the department's own penalty note of 6 April), so thirty days after acceptance end after 30 April, and the interest is described by the supplier as Urvania's statutory interest (35-Reminder.xml). A public authority paying, with a payment authorisation, interest that its contract neither provides nor makes due is a contradiction in the flow's story of payment; it follows from 32#F3, 32#F6 and 35#F2 of this part. Rated Medium here because the remittance advice reports the payment correctly; what it reports contradicts the contract.
- Condition: the amounts the remittance advice pays are due under the contract: the interest line exists only if the contract (after the decisions on 32#F3 and 32#F6) makes the balance overdue from 1 May and gives the supplier interest.
- Options: (a, preferred) decide with 32#F3/35#F2; if the contract term stays "after acceptance", drop the interest line (payment 20286.32) or recalculate it; (b) change the contract's term and add the interest clause, which makes this document right as it is.
- Needs decision: yes

### tender/36#F3 · Low · The advice does not state the amount in the currency in which the payment is made, nor when it is made
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `20308.55`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XUF`
- Why: a Remittance Advice "specifies details of an actual payment". The invoice and the reminder ask for payment in ferra (`35-Reminder.xml:/Reminder/cbc:PaymentCurrencyCode` = `XUF`) into a ferra account; the payer's account is in lume. What the payee needs in order to match the receipt is the amount credited in ferra (2030855 at the reminder's rate of 100) and the rate applied; the advice gives the lume amount only, with no payment currency, no exchange rate (although the flow cites a forward purchase of ferra made for this purpose in six other documents) and no date of the payment (only the document's issue date).
- Condition: the advice states the amount transferred in the currency of the payee's account, or the rate from which it follows, and the date of the payment.
- Options: (a, preferred) add the payment exchange rate (here is where the forward contract BL-FX-26-0091 belongs, see 26#F4) and say in the note that 2030855 ferra were transferred on 8 May; (b) none seen.
- Needs decision: no

## Checked and consistent
- Totals: debits 20808.00 + 22.23 = 20830.23 = `TotalDebitAmount`; credits 515.20 + 6.48 = 521.68 = `TotalCreditAmount`; 20830.23 − 521.68 = 20308.55 = `TotalPaymentAmount` = the reminder's payable amount (`35-Reminder.xml:/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20308.55`). Four lines = `LineCountNumeric`.
- Each line's amount equals the payable amount of the referenced document: invoice 20808.00 (after 72.00 withholding), credit note 515.20, debit note 6.48; line 4 is the interest charged by the reminder (22.23), whose issue date 2026-05-05 is quoted correctly.
- The payment is made on 8 May, before the reminder's new due date of 12 May; no further interest is claimed by any document.
- The settlement discount of the invoice (2 %, until 10 April) is rightly not taken.
- Payment reference RF48VIINV260221: check digits correct, and it is the reference the invoice asks to be quoted. Payer account XB73 BLUM 3801 0001 7803 93 and payee account XU79…9458: check digits correct (`check_ids.py`); the payee account, holder, branch and bank are those of the invoice and the reminder; payment means 30 (credit transfer) as requested. The bank identifiers BLUMXBLX and CREVXUFR carry the user-assigned country codes XB and XU and cannot collide with real BICs.
- ISIN XU0001042501: check digit correct.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cbc:DebitLineAmount`: the line references the reminder but pays only 22.23 of the reminder's 20308.55 — refuted because the other 20286.32 are paid under lines 1 to 3 against their own documents; counting the reminder's full amount would pay them twice.
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount`: the withholding tax (69.48 net) is not shown — refuted because the advice reports the payment to the supplier, and every amount in it is the payable amount after withholding of its document; the withholding is specified in 32, 33 and 34.
- `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID`: one structured reference for a payment that settles four documents — refuted: the reference identifies the payment for the payee, and the lines give the breakdown.
