# LLM review: 10-ImportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/10-ImportCustomsDeclaration.xml`, Git blob `e4f412380312e36eb2dbbc9f243cbc69a0fee18e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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
- Currency conversion: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00` is 4 790 400 XUF × 0.01, and `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `717.60` is 71 760 XUF × 0.01, the rate of `15-Invoice.xml:/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01` (same date, 2026-03-24) and of the energy flow (`energy/09-RemittanceAdvice.xml` uses 100 XUF per XBL). Both amounts are in XBL, the importing country's currency, which is right for a value on which Bayvarran duties are assessed.
- The XUF values converted are those of the export declaration (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400`) and of the invoice lines.
- The certificate of origin that gives the Trade Accord preference is referenced (`/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`: suspected that an import customs value must include the transport to the place of entry (CIF-type), while this is the FCA price without any part of the haulage invoiced in `14-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `44733` — refuted because the WTO Valuation Agreement (Art. 8.2) leaves it to each member whether transport to the place of importation is included (the EU includes it, the United States does not; own knowledge), and the example gives no Bayvarran rule that would require it.
- `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`: suspected that the declaration should state the duties it says are paid — refuted because the UBL 2.5 Import Customs Declaration has no element for duty or tax amounts (checked in UBL-Entities-2.5.gc: the document, Shipment and Goods Item offer only values, no tax total), so the note is the only place for it.

## Outside this review
- The declaration is issued 2026-03-24 09:54 (`/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`), before the commercial invoice on which a customs value is normally based (`15-Invoice.xml:/Invoice/cbc:IssueTime` = `11:41:00`, same day); the values therefore rest on the order. A question of the order of documents across the flow.
