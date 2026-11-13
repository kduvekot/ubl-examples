# LLM review: 02-Quotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/02-Quotation.xml`, Git blob `6e768c2e81f270872df5b742e223f22c2e4950bf` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

## Checked and consistent
- Reference: `/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `BS-DOC-26-0567` resolves to `01-RequestForQuotation.xml`, a Request for Quotation; buyer, seller, item (BF-GS-01, GTIN 9523710000012) and quantity (20 sets) agree with it.
- Dates: issued 2026-03-06 08:58, before the request's submission due date 2026-03-07. Validity end `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-05-05` is 60 days after the issue date, as the request asked (60 DAY).
- Quantity and price: 20 × 610 = 12200.00 = line extension = payable amount.
- Codes: SET, HS 940169, CPC 38112 fit the item; GS1 check digits pass (`check_ids.py`).

## Considered and refuted
- `/Quotation`: suspected missing delivery terms, since the request asked for DAP to the store's goods-in — refuted because a Quotation need not repeat the requested delivery terms; the order (`08-Order.xml`) carries DAP, and nothing in the quotation departs from the request.
