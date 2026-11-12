# LLM review: 04-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

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

### packaging/04#F1 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/04#F2 · Low · Cost centre "Raw cotton" for garment bags
- XPath: `/Invoice/cbc:AccountingCostCode` = `2200`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw cotton`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole, expressed
  as text". The garment bags billed here are booked to the mill's raw-cotton account, the account of
  its cotton purchases (`cotton/08-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`); taken over
  from `03-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`.
- Condition: the cost centre fits a packaging purchase, or is absent (and agrees with the order).
- Options: (a) a packaging/consumables cost centre in order and invoice (preferred); (b) omit.
- Needs decision: no

### packaging/04#F3 · Low · Contacts do not fit invoicing roles
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: The accounting customer's contact should handle the invoice (accounts payable); the mill's
  contact is "Purchasing" with the job title and department of a sales customer-service desk, which
  also disagree with each other. The supplier's contact for a payment request is its order desk, not
  accounts receivable.
- Condition: each accounting party's contact is a function that handles the invoice, with name, job
  title and department that agree.
- Options: (a) accounts payable / receivable contacts (preferred); (b) at least consistent purchasing
  values for the mill.
- Needs decision: no

### packaging/04#F4 · Low · No delivery information on the invoice
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523`
- Why: The invoice bills 20 000 bags delivered DAP to the mill but has no Delivery (date, place) and
  no despatch reference; the order names no date either. Which delivery the invoice covers, and when
  the supply took place, cannot be read from it (IND6).
- Condition: the invoice states the actual delivery date (and place), or references the delivery
  document.
- Options: (a) Delivery/ActualDeliveryDate (preferred); (b) a DespatchDocumentReference.
- Needs decision: no

### packaging/04#F5 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000110`
- Why: A valid GTIN-12 (GS1 US prefix 077, own knowledge); all world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/04#F6 · Low · Default-looking registration date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: 25 companies in all three countries carry 1 January 1996 (271 occurrences in 181 files,
  counted over `*.xml`); it reads as a default (IND5).
- Condition: each date is the company's own, or absent.
- Options: (a) dates from the company histories (preferred); (b) omit.
- Needs decision: yes

## Checked and consistent
- Order reference `LTM-PO-26-0523` resolves to `03-Order.xml`; parties, item, 20 000 EA × 0.08 =
  1600.00 and tax E/RESALE agree.
- Totals 1600.00 throughout, tax 0.00. Due date 2026-05-03 + 30 days = 2026-06-02 (three places agree);
  penalty 1.5 % × 1600.00 = 24.00; penalty period from 2026-06-03.
- Domestic credit transfer over LUMEPAY (MPNS) to the seller's account; RF72RPINV260524 and the
  account pass check_ids.py.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
  repeated next to the payee account — refuted: the supplier is paid under this invoice.
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE` without
  a resale-certificate reference — refuted: the exemption reason is stated; a certificate reference is
  optional in UBL and not required for the story.
