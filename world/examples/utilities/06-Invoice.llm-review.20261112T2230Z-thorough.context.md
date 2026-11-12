# LLM review: 06-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/06-Invoice.xml`, Git blob `a42ab090a50a199d6ef007b111b5c77252c9f943` (committed)
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

### utilities/06#F1 · High · "30 days net" contradicts the due date 21 days after issue
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- Why: 30 days net from 2026-04-02 gives 2026-05-02; every structured due date is 2026-04-23 (21 days), and the PenaltyPeriod starts on 2026-04-24, i.e. after 21 days. The note contradicts the structured terms.
- Condition: The net term in the note and the due dates agree.
- Options: (a, preferred) "21 days net" in the note, matching the penalty period and the flow's other invoices; (b) due dates and penalty start 30 days after issue.
- Needs decision: no

### utilities/06#F2 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" (ISO 639) is a language code repeating Language/ID. World-wide pattern (362 elements in 213 examples, counted with grep over `*.xml`).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a, preferred) remove; (b) a locale such as en-XB from a list that defines it.
- Needs decision: no

### utilities/06#F3 · Low · Supply type "services" on a levy that is no supply
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies". The sewage levy is collected for the city under category O ("Services outside scope of tax", reason "Levy collected for a public body"); it is not a supply of the water company at all, so a type of supply has nothing to describe.
- Condition: The levy line carries no supply type, or one the world's tax rules define for collected levies.
- Options: (a, preferred) remove SupplyTypeCode from the collection line.
- Needs decision: no

### utilities/06#F4 · Low · Buyer's cost centre "Garden department" for the shop's water
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- Why: The buyer's cost centre for the whole shop's drinking water and sewage levy is given as the garden department, Brightmarket's purchasing default (16 examples carry it, counted over `*.xml`).
- Condition: The cost centre fits the shop's utility costs, or is absent.
- Options: (a, preferred) a facilities/utilities cost centre.
- Needs decision: no

### utilities/06#F5 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:ID` = `10442197`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- Why: Logo, online shop and social media profile of the customer play no part in a water invoice, and the buying office is not the contact for utility bills.
- Condition: The customer carries what the invoice uses.
- Options: (a, preferred) remove; use accounts payable.
- Needs decision: no

## Checked and consistent
- Lines: 86 × 2.35 = 202.10; 86 × 0.42 = 36.12; total 238.22 = TaxExclusive = TaxInclusive = Payable; tax subtotals 202.10 (E) and 36.12 (O), tax 0.00.
- Penalty 1.5 % × 238.22 = 3.57; PenaltyPeriod from 2026-04-24 for one month.
- PaymentID RF03CSWCINV260317 check digits OK; paid in full by `07-RemittanceAdvice.xml` on 2026-04-19, before the due date.
- Statement `05-UtilityStatement.xml` matches line 1.

## Considered and refuted
- `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty`: same party as CollectedForParty — refuted because the city's public works department both receives the levy and benefits from it; the two roles coincide legitimately.
- `/Invoice/cac:BuyerCustomerParty`: repeats the accounting customer — refuted because "The buyer." has no "if different" condition.
- `/Invoice/cac:PurchaseReference/cbc:ID`: the supply contract as purchase reference — refuted because PurchaseReference names "a subscription number" as an example.
