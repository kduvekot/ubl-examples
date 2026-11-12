# LLM review: 07-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/07#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats the language of `Language/ID` and names no locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/07#F2 · Low · Buyer's cost centre "Garden department" on an invoice for shirts
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name` = `Cotton shirt`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole, expressed as text". Men's shirts, sold in the store's clothing department (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`), are booked to the garden department, copied from `05-Order.xml:/Order/cbc:AccountingCost` = `Garden department`; the pair is Brightmarket's constant on 12 examples (`grep -rl --include='*.xml' '<cbc:AccountingCost>Garden department<'`).
- Condition: the invoice carries the same clothing (or general merchandise) cost centre as the corrected order, or none.
- Options: (a) preferred: the clothing cost centre of the order; (b) leave it out.
- Needs decision: no

### packaging/07#F3 · Low · Invoice contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The mill, as supplier, gives its purchasing contact for queries on its own sales invoice; the store, as accounting customer, its buying office, placed in Sales as customer service officer. Neither is an invoicing contact (accounts receivable / payable), and the names contradict the departments. 89 examples have a `Purchasing` or `Buying office` contact in Sales (XPath count).
- Condition: the accounting parties' contacts have an accounting function fitting their role, with agreeing name, title and department.
- Options: (a) preferred: accounts receivable for the mill, accounts payable for the store; (b) leave the contacts out.
- Needs decision: no

### packaging/07#F4 · Low · Customer's marketing data on an invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The customer's logo reference, online shop and photo-sharing profile have no use in a supplier's invoice to it; they are Brightmarket's master data copied into the document (section 4.8).
- Condition: the invoice carries none of these, or a reason to.
- Options: (a) preferred: leave them out.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml`; 600 EA × 14.5 = 8700.00 agrees with the order and with the 600 EA of `06-DespatchAdvice.xml`.
- Penalty 1.5 % × 8700.00 = 130.50; due 2026-06-11 is 30 days after 2026-05-12.
- `check_ids.py`: GLN, RF reference and IBAN-like account pass; the payee account is the mill's own (`Lumeport Textile Mill Ltd`).

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item`: no `BuyersItemIdentification` although order and despatch advice carry `BM-778120` — refuted because absence is not a finding and the seller's and standard identifiers suffice to match the line.
