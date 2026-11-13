# LLM review: 11-ExportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/11-ExportCustomsDeclaration.xml`, Git blob `6a4c14a5a30406d882ebdc39fccad12bc46c7e0e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/11#F1 · Low · Consignee's Bayvarra sales-tax registration in the Lisavu export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: the declaration is made to the Island Customs Service for a permanent export from Lisavu,
  which has no general sales tax; the consignee's registration for the Coastal State sales tax of
  Bayvarra is assessed nowhere in it. It has its use at import (15), not at export (section 4.8,
  master data copied into a document that does not use it).
- Condition: the export declaration carries a party tax registration only if Lisavu customs uses it.
- Options: (a, preferred) drop the consignee's `PartyTaxScheme`.
- Needs decision: no

## Checked and consistent
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `6055.452` XLC: under FOB Port of Selanu (08) the export value at the exit office is the price of the goods, 6 129 kg × 0.988 = 6 055.452, as ordered (08) and invoiced (16); the currency is the invoice currency.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`: the customs value is supported by the order rather than by the commercial invoice 16 — refuted because the invoice is issued on 2026-03-02, after this declaration of 2026-03-01; the order states the same price and amount.
