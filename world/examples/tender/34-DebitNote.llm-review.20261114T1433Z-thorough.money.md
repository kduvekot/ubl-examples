# LLM review: 34-DebitNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/34-DebitNote.xml`, Git blob `b6bf3671341fe2437750245b0f5de26efdc18dc0` (committed)
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

### tender/34#F1 · High · As encoded, the department owes the supplier the penalty: creditor and debtor are the wrong way round
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/DebitNote/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/DebitNote/cbc:Note` = `Penalty for late installation under the contract's clause PEN-1.`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `6.48`
- Why: a Debit Note is "a document used to specify debits due to the Creditor from the Debtor"; its accounting supplier party is the creditor, its accounting customer party the debtor, and `PayableAmount` is "the amount … to be paid" by the latter. The document is the department's (its number series, its penalty under its contract clause), and the money is owed by Valdara to the department. With Valdara as supplier and the department as customer the document says the opposite: the department owes Valdara a further 6.48 lume. The later documents read it the way the note means it, not the way it is encoded: `35-Reminder.xml:/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount` = `6.48` ("The department's penalty, set off.") and `36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount` = `6.48` both reduce what the department pays. A debit note raised by a buyer against its supplier is a known commercial practice; the UBL document type has no such reading.
- Condition: the party to whom the amount is owed is the creditor of the document and the party that owes it is the debtor, and the reminder and the remittance advice treat the amount accordingly.
- Options: (a, preferred) keep the document as the department's claim and make the department the accounting supplier (creditor) and Valdara the accounting customer (debtor); the reminder and remittance advice then keep their credit lines; (b) replace it by a credit note from Valdara for the penalty, which the two later documents reference as a credit note; (c) a self-billed credit note issued by the department, if the world has self-billing in this contract.
- Needs decision: yes

### tender/34#F2 · High · The line's withholding tax (1.08) is not the document's (0.72)
- XPath: `/DebitNote/cac:DebitNoteLine/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.08`
- XPath: `/DebitNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `0.72`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:WithholdingTaxTotalAmount` = `0.72`
- Why: the document has one line. Its withholding tax is 1.08, i.e. 10 % of the line amount 10.80; the document's withholding tax is 0.72, i.e. 10 % of the amount after the allowance (7.20). The total of the lines' withholding tax does not equal the document's. The amount used further on is the document's (10.80 − 3.60 − 0.72 = 6.48), and 0.72 is what reconciles with the tax office payment in the reminder (72.00 − 1.80 − 0.72 = 69.48).
- Condition: the sum of the lines' withholding tax equals the document's withholding tax total.
- Options: (a, preferred) apply the waiver on the line (2 days, or a line allowance) so that the line amount is 7.20 and its withholding 0.72; (b) remove the line-level withholding total.
- Needs decision: no

### tender/34#F3 · Low · Zero tax and a withholding tax without category, rate or scheme; withholding "on services of non-residents" applied to a penalty
- XPath: `/DebitNote/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/DebitNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `0.72`
- Why: `TaxAmount` is "the total tax amount for a particular taxation scheme"; neither total names its scheme, category, base or rate. For the 0.00 the reader cannot tell which tax was considered for a contractual penalty; for the 0.72 only the invoice shows that it is the 10 % withholding on a non-resident's services. That tax is deducted from a payment for a service; a penalty is not a service of the supplier. The figure makes sense only if the penalty is read as a reduction of the installation price already invoiced, whose withholding is then reduced in proportion; the document does not say so.
- Condition: each tax amount of the debit note has a subtotal with base, category, rate and scheme, or is absent; the document states that the penalty reduces the invoiced installation price if the withholding is to follow it.
- Options: (a, preferred) drop the zero tax total, give the withholding a subtotal (7.20, 10 %, the invoice's scheme) and add to the note that the penalty reduces the price of the installation; (b) charge the penalty without withholding (payable 7.20) and adjust 35 and 36.
- Needs decision: yes

### tender/34#F4 · Low · The penalty is calculated on the installation price before the credit note
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `10.80`
- Why: 10.80 = 3 × 0.5 % × 720.00, the installation line of the invoice. Two days before this debit note the supplier credited one installation (`33-CreditNote.xml:/CreditNote/cac:CreditNoteLine[2]/cbc:LineExtensionAmount` = `18.00`), so the installation price of the release stood at 702.00, and 3 × 0.5 % × 702.00 = 10.53. The contract's clause does not name the base at all (24#F4 of this part), so either figure can be defended, but the note's own wording ("the installation price of the release") points to the price as it stands.
- Condition: the base of the penalty is stated and equals an amount that can be found in the billing documents at the date of the debit note.
- Options: (a, preferred) keep 720.00 and word the note "of the installation price invoiced (720.00)"; (b) recalculate on 702.00 (line 10.53, allowance 3.51, withholding 0.70, payable 6.32) and adjust 35 and 36.
- Needs decision: no

### tender/34#F5 · Low · The supplier's tax representative on the department's penalty note
- XPath: `/DebitNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `TaxRepresentativeParty` is the party "authorized to act as the Tax Representative" for the document. Bayforth is described in the invoice as the manufacturer's tax representative in Bayvarra. This document is raised by the department for a contractual penalty and carries no tax of the manufacturer; see 32#F8 of this part.
- Condition: as 32#F8.
- Options: (a, preferred) remove the representative from the debit note; decided together with 32#F8.
- Needs decision: yes

## Checked and consistent
- Penalty: 0.5 % of 720.00 = 3.60 a day; 3 days = 10.80 (line and `LineExtensionAmount`); allowance "One day waived" 3.60 = `AllowanceTotalAmount`; 10.80 − 3.60 = 7.20 = `TaxExclusiveAmount`; withholding 10 % of 7.20 = 0.72; 7.20 − 0.72 = 6.48 = `PayableAmount`. The cap of the clause (10 % of 720.00 = 72.00) is not reached.
- The allowance: `ChargeIndicator` false, reason code 64 ("Special agreement") with the text "One day waived": indicator, code and text agree, and the amount is one day's penalty.
- The clause cited (PEN-1) is the one in the contract (24-TenderContract.xml); the invoice referenced exists and contains the installation line the penalty is based on.
- 6.48 is the amount the reminder and the remittance advice use.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/DebitNote/cac:AllowanceCharge/cbc:Amount`: a waiver expressed as a document allowance instead of charging two days — refuted as a money finding: the result is the same and the reason is stated; its effect on the line's withholding is F2.
- `/DebitNote/cac:OrderReference/cbc:ID`: the order referenced does not contain the installation the penalty is about — refuted as a finding of this document: the reference is to the release; the missing order line is 26#F1.
- `/DebitNote/cbc:DocumentCurrencyCode`: no payment means or terms for the 6.48 — refuted because the amount is set off against the invoice (35, 36), which needs no payment instruction.

## Outside this review
- Whether the installation was three days late, and against which date, cannot be checked: no document of the flow states the agreed or the actual installation date. This is a timeline question across 26, 29 and 34.
