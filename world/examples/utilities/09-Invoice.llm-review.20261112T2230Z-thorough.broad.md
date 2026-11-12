# LLM review: 09-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/09-Invoice.xml`, Git blob `f578132e365ef70fff8b3b325066166662819a4a` (committed)
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

### utilities/09#F1 · High · Full amount billed and collected although the statement says the household pays on account every month
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- XPath: `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- Why: The utility statement that supplements this invoice states monthly payments on account by direct debit on the first working day, settled by the bill against the reading. This invoice has no PrepaidAmount ("The total prepaid amount") and collects the full 38.78 by direct debit on 2026-04-23. The two documents describe incompatible payment arrangements; with both, the household pays March twice.
- Condition: Invoice 09 and statement 08 describe the same arrangement: either the invoice deducts the payment on account (PrepaidAmount, PayableAmount = balance), or no payments on account exist.
- Options: (a, preferred) no payments on account (change 08), since the invoice is monthly on the reading; (b) deduct the prepayment here and adjust 10-Reminder.xml and 11-CreditNote.xml.
- Needs decision: yes

### utilities/09#F2 · High · Mandate limited to 12 instructions, but in use monthly since September 2024
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MaximumPaymentInstructionsNumeric` = `12`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:ValidityPeriod/cbc:StartDate` = `2024-09-02`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MandateTypeCode` = `RCUR`
- Why: MaximumPaymentInstructionsNumeric is "The maximum number of payment instructions allowed within the validity period". The mandate is recurring and valid from 2024-09-02 with no end date; monthly invoices (this one for March 2026) collected under it from autumn 2024 to April 2026 amount to about 19 instructions, more than the 12 allowed. If the household also pays on account monthly (08-UtilityStatement.xml), the count is higher still.
- Condition: The maximum number of instructions, the validity period and the collection frequency are compatible at the date of this collection.
- Options: (a, preferred) drop MaximumPaymentInstructionsNumeric (an open-ended recurring mandate rarely has one); (b) give the mandate a validity period of 12 months that contains April 2026 (then a renewed mandate).
- Needs decision: no

### utilities/09#F3 · Medium · PayerParty is the debtor
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: PaymentMandate/PayerParty is "The Party, if different from the debtor, that makes the Payment." The payer is the customer and debtor, so the condition is not met.
- Condition: PayerParty is present only when someone other than the debtor pays.
- Options: (a, preferred) leave it out (the PayerFinancialAccount suffices).
- Needs decision: no

### utilities/09#F4 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" from ISO 639 is the language, not a locale. 213 examples carry the pattern (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: LocaleCode is a locale or absent.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/09#F5 · Low · Exemption reason given for a levy outside the scope of tax
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- Why: TaxExemptionReasonCode is "The reason for tax being exempted"; category O (outside scope) is not an exemption. EN 16931 requires a reason for O, UBL's definition describes an exemption. Same as 06-Invoice.xml.
- Condition: No exemption reason for category O, or the deviation is recorded among the EN 16931 vs UBL findings.
- Options: (a) record and keep; (b) drop it.
- Needs decision: yes

### utilities/09#F6 · Low · Beneficiary repeats the party the levy is collected for
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: CollectedForParty already names the department; BeneficiaryParty repeats it without a different party.
- Condition: BeneficiaryParty only where it differs from CollectedForParty.
- Options: (a, preferred) drop BeneficiaryParty.
- Needs decision: no

## Checked and consistent
- Lines: 14 × 2.35 = 32.90; levy 14 × 0.42 = 5.88; total 38.78 = all monetary totals; tax 0.00.
- Terms: due date 2026-04-23 = 21 days after issue, as the note says; penalty 1.5 % of 38.78 = 0.58; penalty period from 2026-04-24; collection pre-notified more than five days ahead (invoice of 2026-04-02), as the mandate clause requires; single collection 38.78 below MaximumPaidAmount 150.00.
- Payer account XB64BLUM38010007251840 = the customer's account; 10-Reminder.xml (returned debit of 23 April, 38.78) and 11-CreditNote.xml (2 m³ credited) refer to this invoice and agree with its amounts and prices.
- Line 1 agrees with 08-UtilityStatement.xml (14 m³, meter CSW-W-71844, contract CSW-C-311790).
- check_ids.py: RF46CSWCINV260319 and both accounts correct.

## Outside this review
- 08-UtilityStatement.xml is issued (15:10) before this invoice (15:44) although it refers to it as its parent (that example's review).
