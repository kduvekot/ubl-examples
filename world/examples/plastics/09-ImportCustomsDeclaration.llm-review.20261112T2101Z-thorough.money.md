# LLM review: 09-ImportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/09-ImportCustomsDeclaration.xml`, Git blob `f2d4fcae7f399f23e32926db94e2eab6ad1dd2dc` (committed)
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

### plastics/09#F1 · Low · Customs value includes the river freight after the border
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99840.00`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredStatisticsValueAmount` = `99840.00`
- Why: 99,840 `XBL` is the full `CPT` price (`10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000` `XUF` at 100 `XUF` = 1 `XBL`), i.e. including all of the barge freight (179,400 `XUF`, `07-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `179400`). The goods enter Bayvarra at the river border (`/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`) and the barge then continues to the river quay in Lumeport. Under the WTO valuation agreement (own knowledge: interpretative note to Art. 1, transport after importation is excluded when it is distinguished from the price; Art. 8.2 lets members include transport only up to the place of importation), the share of the freight inside Bayvarra would not be part of the customs value, and statistical values are normally taken at the border. The freight is distinguished here: this very declaration splits it off for the FOB value (`/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:FreeOnBoardValueAmount` = `98046.00` = (9,984,000 − 179,400) / 100). The world's valuation rule for Bayvarra is not visible in the examples.
- Condition: the customs and statistical values follow a stated valuation basis (price at the border, or a documented Bayvarran rule that the delivered price is declared), consistent with the FOB value and with `05-ExportCustomsDeclaration.xml`.
- Options: (a, preferred) declare the value at the border (FOB value plus the freight share up to the river border), because the freight is known and distinguished; (b) keep the delivered price if the world's Bayvarran rules say so, and record that rule.
- Needs decision: yes

### plastics/09#F2 · Low · "Duties paid by the importer's account at customs" without duties or customs account
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: the note says duties are paid from the importer's account at customs, i.e. an account held with the customs authority (cash or deferment account). The only account in the declaration is the importer's current account at a commercial bank (`/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:Name` = `Bank of Lumeport`, account type `CACC` "Current"), and the declaration states no duty or tax at all, nor any value "on which a duty, tax, or fee will be assessed" (the goods item has no ValueAmount). Whether any duty is due is also open: the goods claim preferential origin (`/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P`, wholly obtained), and Bayvarra's state sales tax has an exemption for goods used in manufacture (`RESALE` in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`, read for code meanings), which fits a packaging maker.
- Condition: the note and the structured data agree: either the account the duties are paid from is identified as such (and duties or taxes are actually due), or the note says what is really paid (e.g. no duty under the preference, sales tax not due for manufacturing input).
- Options: (a, preferred) word the note after what the importer pays and from where, and drop the bank account if it is not the account debited; (b) keep the account as the debit account and say so in the note ("debited to the importer's bank account").
- Needs decision: yes

## Checked and consistent
- Currency conversion: 9,984,000 `XUF` / 100 = 99,840.00 `XBL`, the rate used in all exchange-rate aggregates of the examples (`grep -rh --include='*.xml' -A6 '<cac:\(Tax\|Pricing\|Payment\)ExchangeRate>' world/examples`: XUF→XBL 0.01, XBL→XUF 100).
- FOB value 98,046.00 `XBL` = (9,984,000 − 179,400) / 100: price less the freight billed in `07-Invoice.xml` and charged in `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`.
- Statistical value equals customs value, as expected for one goods item under one heading.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:InsuranceValueAmount` = `0.00` — suspected as a filler (an explicit zero); refuted: under `CPT` the seller has no duty to insure, an explicit "uninsured" is a meaningful customs statement (no insurance cost in the value), and it is consistent with the value declared for carriage in `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:DeclaredForCarriageValueAmount` = `9984000`.
- Two decimals here (`99840.00`) against none in the `XUF` documents — refuted: different currencies may have different minor units; nothing contradicts.
