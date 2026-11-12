# LLM review: 11-RemittanceAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/11-RemittanceAdvice.xml`, Git blob `d0c26e7bbd846569482f83cb92b801d665bd1d34` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/11#F1 · Medium · Province of Urvanian addresses in Region
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`, as the Bayvarran addresses of the same document do. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/11#F2 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/11#F3 · Low · The invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `RR-INV-26-0894`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `RR-INV-26-0894`
- Why: The billing reference already identifies the paid invoice; the general document reference repeats the same invoice with the same date and adds only a type code. Nothing in the document uses the second reference (IND5/IND6).
- Condition: the paid invoice is referenced once (in the billing reference), unless the second reference carries information the first cannot.
- Options: remove the duplicate document reference (preferred).
- Needs decision: no

### plastics/11#F4 · Low · Payer's contact is a sales order desk
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The sender of a remittance advice is the payer's accounts payable; Rivermouth's contact is a sales order desk. The payee's contact (`/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`) is sales customer service rather than accounts receivable.
- Condition: the accounting parties' contacts are accounting functions.
- Options: accounting contacts in payment documents (preferred).
- Needs decision: no

### plastics/11#F5 · Low · Waste-recovery permit in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The payee's waste-recovery permit plays no part in a payment notice; master data copied into a document that does not use it.
- Condition: no permit in the remittance advice.
- Options: remove it (preferred).
- Needs decision: no

### plastics/11#F6 · Low · Both companies registered on 1 January 1996
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for two companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

## Checked and consistent
- `RR-INV-26-0894` of 2026-04-20 resolves to `10-Invoice.xml`; amount paid 9 984 000 XUF = the invoice's payable amount; balance 0; payment on 2026-05-19, after the discount period (ended 2026-04-30) and before the due date (2026-05-20), so no discount is taken, which is correct.
- Totals: debit 9 984 000, credit 0, payment 9 984 000 = line debit.
- Payee account `XU700351041620000000418916` and RF reference `RF89RRINV260894` are those of the invoice; payer account `XB96BLUM38020504712805` is Rivermouth's (checks pass, `check_ids.py`).
- `PaymentOrderReference` = `InstructionID` (`RP-PAY-26-0882`), consistent.

## Considered and refuted
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID`: the customer's bank account copied into the party — refuted: it is the account the payment was made from (same as the payer account), so it is relevant in a remittance advice.
- `/RemittanceAdvice/cbc:InvoicingPartyReference`: an RF creditor reference in an element for "an internal reference to the order for payment by the invoicing party" — refuted: the definition goes on "This may have been requested of the payer by the payee to accompany the payer's remittance", which is exactly the RF reference the invoice asked to be quoted.
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]`: Urvanian bank address tagged `en-XB` here but `en-XU` in the invoice — refuted: each sender renders the address in its own English (Rivermouth is Bayvarran), as in the order.
