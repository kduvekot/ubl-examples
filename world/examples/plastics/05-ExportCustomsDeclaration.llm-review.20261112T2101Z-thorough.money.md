# LLM review: 05-ExportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/05-ExportCustomsDeclaration.xml`, Git blob `a5a3199bc1d430c4bdf148c1d2afa50b7ca50c54` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### plastics/05#F1 · Low · Export value includes the freight beyond the export border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9984000`
- Why: the declared value is the full `CPT` price of the goods invoice (`10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000`), which includes the barge freight all the way to the river quay in Lumeport (`07-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `179400`). Export values for customs and statistics are normally taken at the export border (FOB/FCA-type value: the price without the transport beyond the frontier; own knowledge of EU and WCO practice). The import side of the flow does split the freight off: `09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:FreeOnBoardValueAmount` = `98046.00` `XBL` = (9,984,000 − 179,400) / 100. The world's valuation rule for Urvanian exports is not visible in the examples.
- Condition: the export customs value follows a stated valuation basis, and it is consistent with the FOB value used in `09-ImportCustomsDeclaration.xml` (either the price at the border, or a documented rule that the full `CPT` price is declared).
- Options: (a, preferred) declare the value at the border (the price less the transport beyond the river border), because that is how real export declarations value goods; (b) keep the full price if the world's Urvanian customs rules say so, and record that rule.
- Needs decision: yes

### plastics/05#F2 · Low · Consignee's bank account in an export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". An export declaration by Rinova to the Urvanian customs makes no payment to or from the foreign consignee; the consignee's current account at a Bayvarran bank is master data copied into a document that does nothing with it. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`).
- Condition: the consignee party in the export declaration carries no financial account.
- Options: (a, preferred) drop it.
- Needs decision: no

## Checked and consistent
- Currency: the export declaration values in the exporter's currency `XUF`; the import declaration values the same goods in `XBL` at 100 `XUF` = 1 `XBL`, the rate used in the exchange-rate aggregates of the other examples (`grep -rh --include='*.xml' -A6 '<cac:\(Tax\|Pricing\|Payment\)ExchangeRate>' world/examples`: XUF→XBL 0.01, XBL→XUF 100 throughout).
- The export underpins the zero-rating of the goods invoice (`10-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`, defined in the Urvanian list as evidenced by the customs declaration); exporter and seller are the same party.
- The declaration references the order (`/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `RP-PO-26-0882`), not the invoice, which is correct because the invoice (`10-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-20`) is issued after the declaration.
