# LLM review: 09-ImportCustomsDeclaration.xml

Flow: reefer (26-0249) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/09-ImportCustomsDeclaration.xml`, Git blob `e49987a730caf7630b84001f67fd322e654aba81` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### reefer/09#F1 · Low · The importer's language differs from every other example of the flow
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:ID` = `qal`
- Why: Party/Language is "the language associated with this party", a property of the party, not of the document. Hafefo Fresh Produce is given English in every other example that states its language (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`, with locale `en-XL`; likewise `02-OrderResponse.xml`, `10-TransportationStatus.xml`, `11-ReceiptAdvice.xml`, `12-RemittanceAdvice.xml`). The bilingual note of this declaration explains why a Lisavan text is present, but not why the party's own language changes.
- Condition: Hafefo's Language is the same in every example of the flow, or the difference has a stated reason (e.g. a language the island's customs requires, carried somewhere other than the party's own language).
- Options: (a) give Hafefo the same language here as elsewhere and keep the Lisavan note for the island's customs (preferred); (b) if Hafefo's language is Lisavan, change the other examples.
- Needs decision: no

## Checked and consistent
- Customs values: 6,988.800 + 2,744.000 + 1,814.400 = 11,547.200 XLC, the "landed value" of the note; each is 0.4 × the invoice line (17,472.00, 6,860.00, 4,536.00 XBL), the XBL→XLC rate used elsewhere in the examples (e.g. a CalculationRate of 0.4 dated 2026-05-14); the CIP invoice value includes freight and insurance to Selanu, so it is the landed value. 10 % of 11,547.200 = 1,154.720, as the note says.
- Preference criterion P (wholly obtained) agrees with the origin statement in `08-Invoice.xml`; origin Bayvarra on every item; the note's "no duty: goods of Accord origin" fits.
- Weights and quantities agree with `04-GoodsCertificate.xml` and `05-ExportCustomsDeclaration.xml`; 20 handling units.
- The four additional references resolve to `07-BillOfLading.xml`, `04-GoodsCertificate.xml`, `05-ExportCustomsDeclaration.xml` and `08-Invoice.xml`, each with the matching document type code. Issued 24 April, after the sailing and before arrival on 26 April; customs release on 26 April is stated in `10-TransportationStatus.xml`.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `6988.800`: the declaration does not state the rate used to convert the XBL invoice — refuted: ImportCustomsDeclaration has no exchange-rate element in UBL 2.5, and the rate applied is the one other examples state.
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Purchasing`: a customs desk in the purchasing department — refuted: in a small importer the import clerk working with purchasing is plausible.
