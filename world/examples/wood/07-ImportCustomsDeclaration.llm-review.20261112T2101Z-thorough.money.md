# LLM review: 07-ImportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/07-ImportCustomsDeclaration.xml`, Git blob `45419bf3fd0c23bb1b64bfa1ca0140c26025be7e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### wood/07#F1 · Medium · Customs value leaves out the pallet charge the importer pays, and its delivery basis is not stated
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000`
- Why: DeclaredCustomsValueAmount is "the total declared value for customs purposes of the goods item". 3456000 XUF is the invoice line amount 34560.00 XBL × 100 (the XBL→XUF rate stated in other examples, e.g. energy/06-Invoice.xml). The 240.00 XBL (24000 XUF) charged to the importer for heat-treated export pallets (`08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`) is left out, although under the transaction-value method (WTO Customs Valuation Agreement Art. 8.1(a)(iii), from my own knowledge) packing costs borne by the buyer are added to the price paid. The declaration also does not state the delivery terms (DAP Ferrano, in the order) on which the value rests, which decides whether transport costs are in the value. The export declaration uses the same base (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00`).
- Condition: the declared customs value includes the packing charge (3480000 XUF at the rate 100) or the example states why not, and the delivery terms the value rests on can be read from the declaration.
- Options: (a) preferred: declare 3480000 XUF and state DAP on the shipment's delivery terms; (b) keep the value and give the story's reason (e.g. the Trade Accord's valuation rule) for leaving packing out. Which rule Urvanian customs applies is a story decision.
- Needs decision: yes

## Checked and consistent
- Conversion: 34560.00 XBL × 100 = 3456000 XUF, using the XBL→XUF rate of 100 stated in ExchangeRate aggregates of nine other examples (counted with grep over `*.xml` for `<cbc:CalculationRate>100</cbc:CalculationRate>`, e.g. tender/26-Order.xml).
- The note "Duties paid by the importer's account at customs." fits DAP, under which the buyer bears import duties and taxes; the importer is the buyer Valdara Industries.
- The declaration's currency XUF is the importing country's currency, as customs values are normally declared.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.`: suspected that the account the note mentions should be identified, and the duty amount stated — refuted because the UBL 2.5 ImportCustomsDeclaration has no element for a duty amount, a duty assessment or a customs deferment account (its children are parties, shipment, previous declaration and document references), so free text is the only place for this statement.
