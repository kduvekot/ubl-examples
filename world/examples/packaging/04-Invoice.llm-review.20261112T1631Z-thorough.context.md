# LLM review: 04-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/04#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats the language of `Language/ID` and names no locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/04#F2 · Low · Buyer's cost centre "Raw cotton" on an invoice for garment bags
- XPath: `/Invoice/cbc:AccountingCostCode` = `2200`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw cotton`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name` = `Garment bag`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole, expressed as text". The invoice bills polyethylene garment bags, not cotton; the value is the mill's constant cost centre, copied from `03-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton` and used on all its purchases (5 examples, `grep -rl --include='*.xml' '<cbc:AccountingCost>Raw cotton<'`).
- Condition: the invoice's cost centre is one for packaging material, the same as in the corrected order, or absent.
- Options: (a) preferred: the same packaging cost centre as the order; (b) leave it out.
- Needs decision: no

### packaging/04#F3 · Low · Invoice contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: The accounting customer's contact is the purchasing contact, placed in Sales as a customer service officer (name and department contradict each other); the accounting supplier's is the order desk. Neither is an invoicing contact (accounts payable / receivable). 89 examples have a `Purchasing` or `Buying office` contact in Sales (XPath count).
- Condition: the accounting parties' contacts have an accounting function, with name, title and department agreeing.
- Options: (a) preferred: accounts payable / receivable contacts; (b) leave the contacts out.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523` resolves to `03-Order.xml`; parties, item, 20000 EA at 0.08 XBL and the exemption agree.
- Arithmetic: 1600.00 throughout; penalty 1.5 % × 1600.00 = 24.00; due date 2026-06-02 is 30 days after 2026-05-03.
- `check_ids.py`: RF reference and IBAN-like account pass.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: `MPNS` here, `RTNS` in `02-Invoice.xml` from the same supplier — refuted because 02 is a cross-border payment (Trade Accord rail) and 04 a domestic one (LUMEPAY); the different channels fit.
