# LLM review: 07-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/07-Invoice.xml`, Git blob `c9439fcedf37997f7173ad361e9246f5cc5439d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/07#F1 · High · Gas exported to Ferrano Energy is declared to customs as consigned to Montebrio Power, and no import by Ferrano Energy exists
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: this invoice bills Ferrano Energy for 2400 MWh of Kelpstone gas "measured at the border station" and zero-rates it as an export. The only export declaration of the flow declares 39200 MWh (= 36800 + 2400) with Montebrio Power as sole consignee, and the only import declaration imports Montebrio Power's 36800 MWh. Ferrano Energy's 2400 MWh are thus declared as delivered to another party on export and are not declared on import at all; the invoice cannot be linked to any customs document for its gas. Counted over `world/examples/*/*.xml`: no import declaration names Ferrano Energy (XU-R-105781) as importer.
- Condition: the 2400 MWh billed here are covered by customs documents that name Ferrano Energy as consignee and importer, or the story says how the gas reaches Ferrano Energy otherwise (e.g. imported by Montebrio Power and passed on), and the invoice agrees with it.
- Options: (a) preferred: split the export of `04-ExportCustomsDeclaration.xml` by buyer and add Ferrano Energy's import (a second goods item or consignment, or a separate import declaration), because it keeps the two direct sales; (b) let Montebrio Power import all 39200 MWh and resell 2400 MWh to Ferrano Energy (changes this invoice's seller and tax treatment); (c) state in the story that Ferrano Energy's share is delivered through Montebrio's import, with the documents saying so.
- Needs decision: yes

## Checked and consistent
- Quantity × price, calculated: 2400 × 3600 XUF per 1 MWh = 8 640 000 XUF; 3600 XUF = 36 XBL × 100 (pricing exchange rate), the same price per MWh as `06-Invoice.xml` and as the export value (1 411 200 XBL / 39200 MWh = 36 XBL).
- Weight implied by the customs declarations: 2400 MWh × 75 kg/MWh = 180 000 kg = 2 940 000 − 2 760 000 kg, the difference between `04-ExportCustomsDeclaration.xml` and `05-ImportCustomsDeclaration.xml`.
- Downstream use: Ferrano Energy resells 61 200 kWh = 61.2 MWh of gas to Valdara Industries in March (`01-UtilityStatement.xml`, `utilities/02-Invoice.xml`), within the 2400 MWh bought.
- Item and origin: the same item and field coordinates as `04-ExportCustomsDeclaration.xml` and `06-Invoice.xml`; HS 271121 and CPC 12020 fit natural gas.
- Dates: `InvoicePeriod` March 2026 before the issue date 2026-04-03; due date 2026-05-03.
- `check_ids.py`: RF14KGINV260158 and the payee account check digits OK.
