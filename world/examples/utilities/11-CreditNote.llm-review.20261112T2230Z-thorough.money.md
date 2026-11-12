# LLM review: 11-CreditNote.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

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

### utilities/11#F1 · Medium · Drinking water classified as a supply of services
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The world's SupplyTypeCode list defines GOODS as "A supply of goods, including energy and water delivered through a network." (`world/codelists/gc/SupplyTypeCode.gc`). The credit repeats the classification of invoice 09, which has the same problem (09#F4).
- Condition: The water line's supply type is GOODS, the same as in the corrected invoice 09.
- Options: (a, preferred) GOODS.
- Needs decision: no

### utilities/11#F2 · Low · A 0 % rate on a levy outside the scope of tax
- XPath: `/CreditNote/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O has no rate. A rate of 0 % describes a zero-rated supply (category Z). Same as 06#F4 and 09#F5.
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no

## Checked and consistent
- 2 × 2.35 = 4.70 and 2 × 0.42 = 0.84 add up to 5.54, which is the TaxExclusive, TaxInclusive and Payable amount. The taxable amounts per category are 4.70 (E) and 0.84 (O).
- Prices, items and tax categories are those of invoice 09's lines. The credited 2 m³ do not exceed the invoiced 14 m³.
- The credit note refers to invoice 09 (CSWC-INV-26-0319, 2026-04-02), which exists in the flow.

## Considered and refuted
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID`: suspected of being copied master data. Refuted: the terms allow a refund ("unless refunded"), and a refund would go to this account.
- `/CreditNote/cac:PaymentTerms/cbc:Note`: "Settled against the next payment to the seller" while the invoice is still unpaid (reminder 10) was considered. It is not contradictory: the credit reduces what the household still owes.
