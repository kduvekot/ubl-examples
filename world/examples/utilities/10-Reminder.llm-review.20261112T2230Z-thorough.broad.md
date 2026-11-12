# LLM review: 10-Reminder.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/10-Reminder.xml`, Git blob `11e7db92f151d2164c7a773e47dfe430253bad7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1b44438 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### utilities/10#F1 · Medium · The seller's own accounts in the buyer's accounting cost
- XPath: `/Reminder/cbc:AccountingCostCode` = `1210`
- XPath: `/Reminder/cbc:AccountingCost` = `Household receivables`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCostCode` = `8320`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCost` = `Reminder fees`
- Why: Reminder/AccountingCost is "The buyer's accounting code, applied to the Reminder as a whole", and on the line "The buyer's accounting cost centre for this reminder line". "Household receivables" and "Reminder fees" are accounts of the water company (a receivables account and a revenue account), not of the household Robin Ashdale, who has no cost accounts. The elements carry the seller's bookkeeping.
- Condition: The accounting cost elements are absent, or carry the buyer's own cost code.
- Options: (a, preferred) leave them out (a private household has no cost accounts).
- Needs decision: no

### utilities/10#F2 · Medium · Language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" from ISO 639 is the language, not a locale. 213 examples carry the pattern (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: LocaleCode is a locale or absent.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/10#F3 · Low · Fee for a returned direct debit described as compensation for late payment
- XPath: `/Reminder/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Compensation for late payment`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Note` = `The fee for the returned direct debit.`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:PenaltySurchargePercent` = `0`
- Why: The only taxable item is the 5.00 fee, which the line describes as the fee for the returned direct debit, i.e. a charge for the bank's return and its handling, not compensation for late payment; the tax reason text and the line note describe two different things. TaxExemptionReason ("The reason for tax being exempted") is also used for category O, which is not an exemption (as in 06-Invoice.xml). PenaltySurchargePercent ("The penalty for late payment, expressed as a percentage") with 0 on the fee line says nothing (rule "no fillers"); the invoice's late-payment surcharge of 1.5 % (`09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`) is simply not charged.
- Condition: The tax treatment text and the line describe the fee the same way; no zero penalty percentage without a reason.
- Options: (a, preferred) a tax reason that names the returned-debit fee (or none for O), and drop PenaltySurchargePercent; (b) if the 5.00 is meant as late-payment compensation, say so in the line note.
- Needs decision: yes

### utilities/10#F4 · Low · Signature without method or reason
- XPath: `/Reminder/cac:Signature/cbc:ID` = `CSWC-SIG-26-REM`
- Why: Only an ID and signatory; nothing says how or why the reminder is signed (rule "no fillers").
- Condition: A signature with a reason and the data that make it one, or none.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/10#F5 · Low · Line amount repeated
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Amount` = `5.00`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `5.00`
- Why: ReminderLine/Amount ("The amount on this reminder line") repeats the debit line amount; line 1 has only the debit amount. One of the two is redundant.
- Condition: Each line states its amount once, in the same way on both lines.
- Options: (a, preferred) drop Amount on line 2.
- Needs decision: no

## Checked and consistent
- Amounts: invoice 38.78 (`09-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`) + fee 5.00 = 43.78 = LineExtensionAmount = PayableAmount; LineCountNumeric 2.
- Story: debit due 2026-04-23 (09), bank return notice of 2026-04-24, reminder 2026-05-01, reminder period from the due date; new due date 2026-05-11 = ten days, as the payment terms say; credit transfer to the payee account of the invoice.
- Reference CSWC-INV-26-0319 of 2026-04-02 is 09-Invoice.xml.
- check_ids.py: both accounts correct.

## Considered and refuted
- `/Reminder/cac:PayeeParty/cac:PartyName/cbc:Name`: payee repeats the supplier — refuted, Reminder/PayeeParty ("The Party who receives the Payment") has no "if different" condition.
- `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount`: late-payment surcharge of the invoice not charged — refuted, the invoice says penalties "may apply" in the penalty period; waiving it is legitimate.

## Outside this review
- 11-CreditNote.xml (2026-05-05) credits 5.54 against invoice 09 four days after this reminder demanded the full 43.78; whether the reminder's demand still stands is a matter for that example and the flow's timeline.
