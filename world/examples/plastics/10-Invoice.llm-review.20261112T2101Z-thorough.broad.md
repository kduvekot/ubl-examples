# LLM review: 10-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/10-Invoice.xml`, Git blob `1e3f9e5ae5dac5d74b0e7b9130b9a13721e9ec83` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### plastics/10#F1 · Medium · Province of Urvanian addresses in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`, as the Bayvarran addresses of the same invoice do. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/10#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/10#F3 · Low · Customer's bank account in a credit-transfer invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Payment is by credit transfer to the payee account (`/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`); the invoice does nothing with the customer's own account (it would matter only for a direct debit). Master data copied into the invoice.
- Condition: the customer's account is absent, or the payment means uses it.
- Options: remove it (preferred).
- Needs decision: no

### plastics/10#F4 · Low · Contacts are sales functions, not accounts
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: The accounting customer's contact handles payables; Rivermouth's contact is a sales order desk with the job title customer service officer. The supplier's contact for billing questions is sales customer service rather than accounts receivable.
- Condition: the accounting parties' contacts are accounting functions.
- Options: accounting contacts in billing documents (preferred).
- Needs decision: no

### plastics/10#F5 · Low · Waste-recovery permit in the goods invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The invoice bills a product; the supplier's waste-recovery permit is not needed for it (the recycled-content certificate on the item already carries the claim).
- Condition: no permit in the invoice, unless the invoice uses it.
- Options: remove it (preferred).
- Needs decision: no

### plastics/10#F6 · Low · Both companies registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for two companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

### plastics/10#F7 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8) in the GTIN-12 (UPC) range; it could be taken for a real GTIN (see `01-Order.xml`).
- Condition: the number cannot be mistaken for a real GTIN, or it is verified as unassigned and documented.
- Options: (a) a non-GTIN format (preferred); (b) document the verification.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 120 t × 83 200 = 9 984 000 XUF = line extension = tax-exclusive = tax-inclusive = payable; tax 0; settlement discount 2 % × 9 984 000 = 199 680; settlement period 2026-04-20 to 2026-04-30 (10 days); due 2026-05-20 = 30 days.
- References: order `RP-PO-26-0882` line 1 (`01-Order.xml`) and despatch advice `RR-DA-26-0892` (`08-DespatchAdvice.xml`) exist; quantity, price and item agree with them.
- Tax: category `G`, exemption `EXP`, supply type goods, consistent with the export declaration `05-ExportCustomsDeclaration.xml`; tax point 2026-04-20, after despatch (2026-04-19).
- The note on CPT agrees with the order's delivery terms (carriage to the river quay included in the price).
- Payment: RF reference `RF89RRINV260894` and payee account `XU700351041620000000418916` pass their checks (`check_ids.py`); the remittance `11-RemittanceAdvice.xml` uses the same reference and account and pays 9 984 000 after the discount period, so without discount.

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:ID`: `XU-STD` also appears in the freight invoice of another supplier (`07-Invoice.xml`) — refuted for this invoice: these are Rinova's own standard terms; the conflict with the agreed transport terms is recorded in the review of `07`.
- `/Invoice/cac:PaymentMeans/cbc:PaymentRailID`: a Trade Accord payment rail for a cross-border payment in XUF — refuted: fits a payment from Bayvarra to Urvania.
