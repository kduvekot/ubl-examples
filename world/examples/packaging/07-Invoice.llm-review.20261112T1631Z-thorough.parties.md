# LLM review: 07-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/07-Invoice.xml`, Git blob `0345a2bca9a5957f58f15a04460ca368ab893cee` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/07#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already in Language/ID, not a locale. The same value occurs 362 times in 213 examples (Grep over `*.xml`).
- Condition: LocaleCode names a locale (language and region) or is absent.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/07#F2 · Low · The contacts of the accounting parties are a purchasing mailbox and a buying office
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party". The invoicing supplier's contact is its purchasing mailbox, which has nothing to do with selling or billing; the accounting customer's contact is its buying office with a sales department, neither of which is accounts payable. Both are the parties' single contacts used in every role (52 and 41 such contacts across the examples, lxml count over `*.xml`).
- Condition: the contacts of the accounting parties belong to billing or payment, and name, job title and department agree.
- Options: (a) preferred: accounts contacts for both parties; (b) omit the contacts where not needed.
- Needs decision: no

### packaging/07#F3 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". 25 companies in three countries' registers share exactly this date (271 occurrences in 181 examples, lxml count over `*.xml`), which looks like a default (IND5).
- Condition: Lumeport Textile Mill's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: an individual date; (b) remove; (c) confirm as a story fact.
- Needs decision: yes

### packaging/07#F4 · Low · Marketing and customs data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: the customer's logo, web shop and social media profile have no role in a supplier's invoice; the supplier's customs trader ID has none in a domestic supply taxed under the Coastal State sales tax. They look copied from master data (the logo reference is in 41 examples, Grep over `*.xml`).
- Condition: every party detail in the invoice has a role in invoicing, payment or tax.
- Options: (a) preferred: leave them out here; (b) state in the example why they are needed.
- Needs decision: no

## Checked and consistent
- OrderReference `BS-PO-26-0525` resolves to `05-Order.xml`; the accounting supplier and customer blocks are identical to the seller and buyer blocks there (compared line by line), and BuyerCustomerParty/SellerSupplierParty repeat them by ID and name.
- Payee account `XB35BLUM38020504608076` is named after Lumeport Textile Mill Ltd, the supplier, at the Harbour branch `380205` of the Bank of Lumeport (the branch code is also in the account number); check digits valid (check_ids.py), RF reference `RF18LTMINV260529` valid.
- Parties agree with `06-DespatchAdvice.xml` (despatch supplier and delivery customer).
