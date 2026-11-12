# LLM review: 06-TransitCustomsDeclaration.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/06-TransitCustomsDeclaration.xml`, Git blob `3619a51519aa158336a9817cd911b99963ad4351` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/06#F1 · Low · Declared value includes the carriage inside Bayvarra
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9580800`
- XPath: `11-Invoice.xml:/Invoice/cbc:Note[2]` = `Delivered at place: the price includes the carriage to the siding.`
- XPath: `11-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9580800`
- XPath: `10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `109200`
- Why: DeclaredCustomsValueAmount is "the total declared value for customs purposes of the goods
  item". The declared value is exactly the DAP sale price, which by the sales invoice includes the
  carriage to Lumeway's siding in Marrowdale, i.e. carriage beyond the Urvanian border and inside
  Bayvarra. Under the usual customs valuation rules (own knowledge: WTO Valuation Agreement, value at
  the border; export statistical value at the frontier of the exporting country), carriage after the
  goods cross the border is not part of the customs value when it is known separately, and here it is
  known: the whole rail freight was bought for 109,200 XUF excluding VAT (10-Invoice.xml), of which
  only the part beyond the border would be deducted. The difference is small (at most 1.1 % of the
  value), and the world may have its own rule.
- Condition: the declared customs value is the value at the basis the world's customs rules require,
  or the example states why the DAP price is the right value.
- Options: (a) keep the DAP price if the world's transit rules use the invoice price for the
  guarantee (then nothing to change); (b) deduct the share of the carriage beyond the border.
  No preference: it depends on the world's customs rules.
- Needs decision: yes (customs valuation rule)

## Checked and consistent
- 9,580,800 XUF = 192 × 49,900 XUF, the same as the order
  (`01-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `9580800`) and the sales
  invoice; the currency (XUF) is that of the sale and of the declaring country.
- NatureOfTransactionCode PURCHASE ("Outright purchase or sale") fits the sale of 01 and 11.
- The tax registrations of Valdara (XU007299291, VAT), Lumeway (UL-1230822, STT) and Ferrano Rail
  Cargo (XU007328060, VAT) agree with the other examples of the flow.
