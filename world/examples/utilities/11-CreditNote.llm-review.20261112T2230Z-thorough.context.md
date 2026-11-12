# LLM review: 11-CreditNote.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/11-CreditNote.xml`, Git blob `831c5f12acb5889efdae887718f56b4fd27594fc` (committed)
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

### utilities/11#F1 · Medium · A language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" (ISO 639) is a language code repeating Language/ID. World-wide pattern (362 elements in 213 examples, grep over `*.xml`).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a, preferred) remove.
- Needs decision: no

### utilities/11#F2 · Low · The credit note does not say how the credit is settled; the customer's account stands unused
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `5.54`
- XPath: `10-Reminder.xml:/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43.78`
- Why: The credited invoice `09-Invoice.xml` is unpaid: its debit was returned and `10-Reminder.xml` asks for 43.78 by 2026-05-11. The credit of 5.54 can be set off against that open amount or refunded; the credit note has no PaymentMeans or note saying which. The customer's account appears only under Person/FinancialAccount, which does not say it is the refund account.
- Condition: The credit note states how the credit is settled (set-off against the open invoice, or refund to a stated account in PaymentMeans).
- Options: (a, preferred) a note that the credit reduces the open amount of the invoice, and remove the unused account; (b) PaymentMeans with the customer's account as refund account.
- Needs decision: yes

### utilities/11#F3 · Low · Supply type "services" on a credited levy
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: As in `09-Invoice.xml`: the levy collected for the city is not a supply of the water company, so a type of supply has nothing to describe.
- Condition: The levy line carries no supply type.
- Options: (a, preferred) remove.
- Needs decision: no

## Checked and consistent
- BillingReference CSWC-INV-26-0319 (2026-04-02) resolves to `09-Invoice.xml`; 2 m³ × 2.35 = 4.70; 2 m³ × 0.42 = 0.84; total 5.54; tax categories E and O as in the invoice.
- The note (meter over-reading by 2 m³) gives the reason for the credit; the credited quantity (2 of 14 m³) fits.
- CreditNoteTypeCode 381 fits a credit note.

## Considered and refuted
- `/CreditNote/cac:CollectionCreditNoteLine/cac:BeneficiaryParty`: no CollectedForParty as on the invoice — refuted because the beneficiary names the city's department, which suffices to show for whom the levy is credited.
