# LLM review: 04-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/04-Invoice.xml`, Git blob `b7615e989edc233d99c6d2b1a77b5e429b9d95e3` (committed)
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

### packaging/04#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already in Language/ID. The same value occurs 362 times in 213 examples (Grep over `*.xml`).
- Condition: LocaleCode names a locale (language and region) or is absent.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/04#F2 · Low · The contacts of the accounting parties do not fit invoicing; the customer's contradicts itself
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: Party/Contact is "The primary contact for this party"; for the accounting customer of an invoice it is whom the supplier contacts about the invoice and its payment. Lumeport Textile Mill's contact is named purchasing but has a sales job title and department (the same contradiction as in `03-Order.xml`; 52 such contacts across the examples, lxml count over `*.xml`), and neither is accounts payable. Rivermouth's accounting contact is its order desk.
- Condition: the contacts of the accounting parties belong to invoicing or payment, and name, job title and department agree.
- Options: (a) preferred: accounts contacts for both accounting parties; (b) omit the Contact where not needed.
- Needs decision: no

### packaging/04#F3 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". 25 companies in three countries' registers share exactly this date (271 occurrences in 181 examples, lxml count over `*.xml`), which looks like a default (IND5).
- Condition: each company's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: individual dates; (b) remove; (c) confirm as a story fact.
- Needs decision: yes

### packaging/04#F4 · Low · Customs trader identifiers in a domestic invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-412740`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: the customs trader identifiers identify the parties to customs; supplier and customer are both in Lumeport, the supply is taxed domestically (exempt for resale or manufacture under the Coastal State sales tax), and no customs formality is involved. They look copied from master data.
- Condition: the invoice carries customs identifiers only where the supply involves customs.
- Options: (a) preferred: leave them out here; (b) keep them only with a reason stated in the example.
- Needs decision: no

## Checked and consistent
- OrderReference `LTM-PO-26-0523` resolves to `03-Order.xml`; buyer and seller there are the accounting customer and supplier here with the same IDs, tax IDs, legal entities, addresses and endpoints. BuyerCustomerParty and SellerSupplierParty repeat them by ID and name.
- The supplier block is identical to the one in `02-Invoice.xml` (compared line by line).
- Payee account `XB96BLUM38020504712805` is Rivermouth's own account, named after Rivermouth Packaging Ltd; check digits valid (check_ids.py), RF reference `RF72RPINV260524` valid.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`: party account next to the payee account — refuted because the invoice is paid to it; the two agree.
