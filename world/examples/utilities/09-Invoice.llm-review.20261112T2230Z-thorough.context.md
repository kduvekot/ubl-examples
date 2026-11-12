# LLM review: 09-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/09-Invoice.xml`, Git blob `f578132e365ef70fff8b3b325066166662819a4a` (committed)
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

### utilities/09#F1 · High · The invoice ignores the payments on account its statement describes
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- XPath: `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- Why: The statement that supplements this invoice says the household pays on account every month and that the bill settles those payments against the reading. This invoice charges the whole March consumption and levy, has no PrepaidAmount, and collects the full amount 21 days after the invoice date. The two documents describe different payment arrangements for the same consumption.
- Condition: Invoice and statement describe the same arrangement: either no payments on account, or a PrepaidAmount and a settlement of the difference here.
- Options: (a, preferred) remove the on-account data from the statement (the flow's reminder and credit note follow this invoice); (b) add the payments on account here.
- Needs decision: yes

### utilities/09#F2 · Medium · PayerParty equal to the debtor
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: PaymentMandate/PayerParty is "The Party, if different from the debtor, that makes the Payment." The debtor is Robin Ashdale and so is the payer.
- Condition: PayerParty is present only when someone other than the debtor pays.
- Options: (a, preferred) remove PayerParty.
- Needs decision: no

### utilities/09#F3 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" (ISO 639) is a language code. World-wide pattern (362 elements in 213 examples, grep over `*.xml`).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a, preferred) remove.
- Needs decision: no

### utilities/09#F4 · Low · The customer's account given twice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerFinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The direct debit uses the mandate's payer account; the same account under Person/FinancialAccount ("The financial account associated with this person") adds nothing the invoice uses.
- Condition: The account appears where the invoice uses it.
- Options: (a, preferred) remove Person/FinancialAccount.
- Needs decision: no

### utilities/09#F5 · Low · Supply type "services" on a levy that is no supply
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: As in `06-Invoice.xml`: the sewage levy, collected for the city and outside the scope of tax, is not a supply whose type could be given.
- Condition: The levy line carries no supply type, or one the world's rules define for levies.
- Options: (a, preferred) remove.
- Needs decision: no

## Checked and consistent
- Lines: 14 × 2.35 = 32.90; 14 × 0.42 = 5.88; total 38.78; tax 0.00 (E and O).
- Penalty 1.5 % × 38.78 = 0.58; due 2026-04-23 = 21 days after issue, matching the note.
- Mandate: recurring, 150.00 maximum per instruction, valid from 2024-09-02; the 2026-04-23 collection is announced more than five days before by this invoice (clause CSW-DD-T3).
- `10-Reminder.xml` reminds of 38.78 after the return of the 23 April debit; `11-CreditNote.xml` credits 2 m³ of it.

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent`: a late-payment surcharge on a direct debit — refuted because a returned debit makes the payment late, as `10-Reminder.xml` shows.
