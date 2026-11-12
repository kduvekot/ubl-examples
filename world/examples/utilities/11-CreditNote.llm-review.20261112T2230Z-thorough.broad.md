# LLM review: 11-CreditNote.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/11-CreditNote.xml`, Git blob `831c5f12acb5889efdae887718f56b4fd27594fc` (committed)
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

### utilities/11#F1 · Medium · Language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" from ISO 639 is the language, not a locale. 213 examples carry the pattern (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: LocaleCode is a locale or absent.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/11#F2 · Low · Credit for a meter error without the period and the invoice lines it corrects
- XPath: `/CreditNote/cbc:Note` = `The meter test found the meter over-reading by two cubic metres.`
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `2`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0319`
- Why: The credit note corrects 2 m³ of invoice 09, but gives no invoice period and no reference to the invoice lines it corrects (no DiscrepancyResponse, no line-level BillingReference), and does not name the meter (CSW-W-71844) or the test. A reader cannot tell whether the 2 m³ belong to March (14 m³ billed) or accumulated over a longer time, which matters because the register reading 1844 of 08-UtilityStatement.xml would then also be 2 m³ too high for the next bill.
- Condition: The credit note states the period (or reading) the correction applies to and which invoice lines it corrects.
- Options: (a, preferred) InvoicePeriod March 2026, BillingReferenceLine or line-level references to invoice lines 1 and 2, and the meter as PurchaseReference-equivalent in a line note; (b) a DiscrepancyResponse with a reason code for the meter error.
- Needs decision: no

### utilities/11#F3 · Low · Levy credited for a beneficiary, without the party it was collected for
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `09-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The invoice names the department as CollectedForParty ("The Party on whose behalf this item or amount is collected") and repeats it as BeneficiaryParty; the credit note keeps only BeneficiaryParty. The collection line of the credit note reverses an amount collected on behalf of the department, so CollectedForParty is the element that fits, and the two documents should describe the third party the same way.
- Condition: The collection line of the credit note names the department in the same role as invoice 09.
- Options: (a, preferred) CollectedForParty, as in the invoice (and drop BeneficiaryParty in both).
- Needs decision: no

### utilities/11#F4 · Low · Exemption reason given for a levy outside the scope of tax
- XPath: `/CreditNote/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- Why: TaxExemptionReasonCode is "The reason for tax being exempted"; category O is not an exemption. Same as 06 and 09.
- Condition: No exemption reason for O, or the deviation is recorded among the EN 16931 vs UBL findings.
- Options: (a) record and keep; (b) drop it.
- Needs decision: yes

## Checked and consistent
- Amounts: 2 × 2.35 = 4.70; levy 2 × 0.42 = 0.84; total 5.54 = all monetary totals; tax 0.00 (E 4.70, O 0.84); prices equal invoice 09's.
- Reference CSWC-INV-26-0319 of 2026-04-02 is 09-Invoice.xml; 2 m³ credited is less than 14 m³ billed.
- Payment terms "settled against the next payment ... unless refunded" fit the situation of 10-Reminder.xml (invoice still unpaid after the returned debit).
- check_ids.py: account XB64BLUM38010007251840 correct.

## Considered and refuted
- `/CreditNote/cac:PaymentTerms/cbc:Note`: credit settled against the "next payment" while invoice 09 is still open — refuted, the next payment is the payment of the reminded amount, against which the credit can be set off.
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID`: customer's bank account in a credit note — refuted, it is the account for a possible refund ("unless refunded").

## Outside this review
- 10-Reminder.xml demands 43.78 by 2026-05-11; after this credit note of 2026-05-05 the amount actually due is 38.22. Whether a corrected reminder or a note is needed is a timeline question of the flow.
