# LLM review: 30-ExportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/30-ExportCustomsDeclaration.xml`, Git blob `badd401509d1f287a27ff308ccae49e844329ef6` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/30#F1 · Medium · The declared value leaves out the colour charge that the invoice exempts as part of the exported goods
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000`
- Why: `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods item". 1996000 ferra is 40 × 49900, the list price of 40 benches (19960.00 lume at 100 ferra to the lume). The benches exported are the moss-green ones of the order change, for which the seller accepted a charge of 200.00 lume five days before this declaration (28-OrderResponse.xml, 25 March). The invoice treats that charge as part of the exported goods: its export-exempt taxable amount is `32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00` (19960.00 + 200.00) under reason EXP, which the world's code list defines as "the export is evidenced by the customs declaration". The declaration evidences 19960.00 only, so 200.00 lume (20000 ferra) of the exemption claimed on the invoice have no export evidence, and the price actually payable for the goods is higher than the value declared. Rated Medium because the world's customs valuation rules are not in the examples; by the usual transaction-value rule (my knowledge: WTO Valuation Agreement, price actually paid or payable) a charge for the colour of the goods belongs to their value.
- Condition: the declared customs value equals the amount the invoice of the same goods treats as the value of the exported goods (in the declaration's currency at the stated rate), or the difference is explained in the declaration.
- Options: (a, preferred) declare 2016000 ferra; (b) bill the colour as a service outside the goods' value in the invoice, with its own tax category, and keep 1996000.
- Needs decision: no

## Checked and consistent
- 40 × 49900 = 1996000 ferra = 19960.00 lume × 100: the value agrees with the catalogue price, the order line and with the import declaration (`31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`) at the flow's rate.
- The value is in ferra, the currency of the exporting country; the installation (a service performed in Bayvarra) is rightly not part of it.
- Quantity 40 EA = despatch advice, order and invoice. Export type PERMANENT and reason SALE fit a sale invoiced with an export exemption.
- The declaration carries no tax or duty amount; none is expected on an export.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount`: under DAP the seller's price includes the carriage to Lumeport, so an export value at the Urvanian border could be lower than the invoice price — refuted as a finding because no document of the flow separates a freight amount from the price; the value used is consistently the goods price.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount`: the amount has no decimals while lume amounts have two — refuted: the ferra is used without decimals everywhere in the flow (catalogue prices, the invoice's tax total in XUF).
