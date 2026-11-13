# LLM review: 20-DespatchAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/20-DespatchAdvice.xml`, Git blob `48649a02a6dba4b51ed92b3c8c00d3a15724cd7a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/20#F1 · Low · Sales-tax registrations and share capital of the despatching party and the carrier in a despatch advice
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- Why: A despatch advice describes what was despatched to the delivery party (Nalevi Warehousing). It carries no amounts, prices or taxes, so the Bayvarran state sales-tax registrations of Lumeway and Tidewell and their share capital have no use in it (section 4.8: master data copied into a document that does not use it).
- Condition: Despatch supplier and carrier carry tax schemes and capital data only if the despatch advice has a stated use for them.
- Options: (a) preferred: leave them out, keeping identification, name, address and contact; (b) keep them with a stated reason.
- Needs decision: no

## Checked and consistent
- The despatch advice carries no monetary amounts apart from the share capital of the two parties; the currencies of those (XBL) match the parties' country.
- The tax schemes quoted match the descriptions of Lumeway (`UL-1230822`, Upland State) and Tidewell (`CO-1235754`, Coastal State) in the other examples of the flow.

## Considered and refuted
- `/DespatchAdvice/cbc:AccountingCost` = `Stock for municipal projects`: suspected the code is the buyer's (Velumi's, from the order `05-Order.xml:/Order/cbc:AccountingCost` = `Stock for municipal projects`) while the despatch advice is issued by the seller — refuted because the definition here is the cost centre "applied to the Despatch Advice as a whole", without naming whose; passing the buyer's cost centre from the order on to goods-in is a legitimate use.
