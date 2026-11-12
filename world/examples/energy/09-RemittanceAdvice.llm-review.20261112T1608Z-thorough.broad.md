# LLM review: 09-RemittanceAdvice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/09-RemittanceAdvice.xml`, Git blob `64ddc3389c441e3d1a8906ba4cb8cd22d97d45ce` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/09#F1 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` is the language. 362 occurrences in 213 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'`).
- Condition: LocaleCode holds a locale (e.g. `en-XB`) or is absent.
- Options: (a, preferred) `en-XB`; (b) omit.
- Needs decision: no

### energy/09#F2 · Medium · Province given in Region
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`). World convention; 219 occurrences in 104 of 250 XML examples.
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/09#F3 · Low · Contacts are trading and sales desks on a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Gas sales`
- Why: the remittance advice goes from the payer's accounts payable to the payee's receivables; the energy trader and the gas sales manager are the contract contacts copied from the invoices.
- Condition: the contacts are those who deal with the payment.
- Options: (a, preferred) payables / receivables contacts; (b) keep with a reason.
- Needs decision: no

## Checked and consistent
- Line 1: 132 480 000 XUF = 06-Invoice.xml PayableAmount; line 2: 1 987 200 XUF = 08-Reminder.xml line 2 (19 872 XBL × 100) = 06-Invoice.xml PenaltyAmount; TotalDebitAmount = TotalPaymentAmount = 134 467 200; LineCountNumeric 2.
- PaymentID RF41KGINV260157 = 06-Invoice.xml's; payer account = Montebrio's account in 03-Invoice.xml; payee account = Kelpstone's in 06/08; check digits OK (`check_ids.py`).
- Issued 2026-06-06, before the reminder's due date 2026-06-10; references KG-INV-26-0157 and KG-DOC-26-0159 resolve to 06 and 08.
- Montebrio's address here uses `en-XU`, as in 03 and 05.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:ExchangeRate/cbc:Date`: suspected a rate dated 2026-06-06 against the reminder's conversion of 2026-06-03 — refuted: both use 100 XUF per XBL, so the amounts agree; the date is when the payer established the rate.
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:DebitLineAmount`: suspected the line should carry the reminder's full total (1 344 672 XBL) — refuted: the invoice is paid on line 1, the reminder's line only adds the surcharge, so no amount is counted twice.
