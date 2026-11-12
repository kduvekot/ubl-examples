# LLM review: 10-Reminder.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/10-Reminder.xml`, Git blob `11e7db92f151d2164c7a773e47dfe430253bad7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/10#F1 · Medium · The seller's ledger accounts are given as the buyer's accounting codes
- XPath: `/Reminder/cbc:AccountingCostCode` = `1210`
- XPath: `/Reminder/cbc:AccountingCost` = `Household receivables`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCostCode` = `8320`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCost` = `Reminder fees`
- Why: In a Reminder, UBL defines these as "The buyer's accounting code, applied to the Reminder as a whole" and "The buyer's accounting cost centre for this reminder line". Here the buyer is a private household, Robin Ashdale. "Household receivables" and "Reminder fees" are the water company's own accounts: a receivables account and a fee income account. The values therefore carry the seller's bookkeeping in the buyer's elements.
- Condition: The Reminder carries no accounting cost, or it carries a code of the buyer's.
- Options: (a, preferred) remove both pairs; a household has no cost accounts.
- Needs decision: no

### utilities/10#F2 · Low · The invoice's late-payment surcharge is neither charged nor waived; a 0 % surcharge is stated on the fee line
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:PenaltySurchargePercent` = `0`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `38.78`
- Why: Invoice 09 sets a surcharge of 1.5 % for payment after 2026-04-23 (`09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`, PenaltyAmount 0.58). The reminder of 2026-05-01 claims the overdue 38.78 without the surcharge and says nothing about waiving it. Instead it puts a surcharge of 0 % on the line for the return fee, where no lateness applies.
- Condition: The reminder either charges the invoice's surcharge on the overdue line or states that it is waived, and the fee line carries no surcharge percent.
- Options: (a) add 0.58 as a surcharge on line 1; (b, preferred if the company waives it for a first reminder) remove PenaltySurchargePercent from line 2 and add a note that the surcharge is waived.
- Needs decision: yes

### utilities/10#F3 · Low · The tax exemption reason calls the fee compensation for late payment; the line calls it a returned-debit fee
- XPath: `/Reminder/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Compensation for late payment`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Note` = `The fee for the returned direct debit.`
- Why: The 5.00 is the cost of the debit the bank returned (notice BLUM-RTN-26-04-0193), not compensation for lateness. The fee and the surcharge (F2) are different charges, and the tax text describes the one that is not charged.
- Condition: The exemption reason describes the fee actually charged.
- Options: (a, preferred) for example "Fee for a returned direct debit, outside the scope of tax".
- Needs decision: no

### utilities/10#F4 · Low · Credit transfer requested without the payment reference
- XPath: `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `/Reminder/cac:PaymentTerms/cbc:Note` = `Please pay within ten days by credit transfer; the next collection will be by direct debit again.`
- Why: The reminder asks the household to pay by credit transfer to the company's account, but it gives no PaymentID or instruction note. The invoice's creditor reference RF46CSWCINV260319 is not repeated, so the company cannot match the incoming 43.78 automatically. That matching is what the reminder's payment means are for.
- Condition: The reminder's payment means carry the reference the payer is to quote.
- Options: (a, preferred) PaymentID with RF46CSWCINV260319 (or a new RF reference for the 43.78).
- Needs decision: no

### utilities/10#F5 · Low · The household's bank account is repeated in a reminder that asks for a credit transfer
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The reminder asks the household to transfer the money. The household's own account plays no part in that, and it reads as copied master data.
- Condition: The account is present only if the reminder uses it.
- Options: (a, preferred) remove it.
- Needs decision: no

## Checked and consistent
- 38.78 + 5.00 = 43.78 = LineExtensionAmount = PayableAmount. Line 1's 38.78 is invoice 09's PayableAmount.
- The due date 2026-05-11 is 10 days after 2026-05-01, as the note says. The reminder period starts on the invoice's due date, 2026-04-23. The bank's return notice is dated 2026-04-24, after the collection on 2026-04-23.
- The payee account XB21BLUM38010004189160 is the company's account, as in 06 and 09.
- The fee is out of scope of tax (O): taxable 5.00, tax 0.00.

## Outside this review
- Credit note 11 (2026-05-05) credits 5.54 against "the next payment" while this reminder's 43.78 is still open until 2026-05-11. That is a question about the order of documents in the flow, not about this reminder's values.
