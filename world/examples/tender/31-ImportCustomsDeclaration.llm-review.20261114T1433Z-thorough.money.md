# LLM review: 31-ImportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/31-ImportCustomsDeclaration.xml`, Git blob `f995e80c478f86074b7bfa4eca588151c5ee7767` (committed)
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

### tender/31#F1 · Medium · The declared value leaves out the colour charge that is part of the price of the imported goods
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`
- Why: `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods item". The importer declares 40 × 499 lume. The price it owes for these goods is higher: the benches are the moss-green ones for which it agreed a charge of 200.00 lume itself (`27-OrderChange.xml:/OrderChange/cac:AllowanceCharge/cbc:Amount` = `200.00`), and the invoice, issued at 09:28 on the day of this declaration (11:14), bills goods of `32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`. The declared value is thus 200.00 lume below the price payable for the goods, on the document on which any duty is assessed. Rated Medium because the world's customs valuation rules are not in the examples; by the usual transaction-value rule (my knowledge: WTO Valuation Agreement, price actually paid or payable) a charge for the colour of the goods belongs to their value. The export declaration has the same value (30#F1 of this part).
- Condition: the declared customs value equals the goods amount of the invoice for the same shipment, or the difference is explained in the declaration.
- Options: (a, preferred) declare 20160.00; (b) bill the colour separately from the goods in the invoice and keep 19960.00.
- Needs decision: no

### tender/31#F2 · Low · "Duties paid" without a duty, a rate or an amount, by an importer that is exempt from the only Bayvarran tax the flow names
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- Why: the note states a payment. The declaration contains no duty or tax amount, no rate and no tariff treatment, and no other example of the flow shows a duty on this import (the invoice, the reminder and the remittance advice carry Urvanian VAT at 0 % and a Bayvarran withholding tax only). The importer's own tax data says it is exempt from the state sales tax (`/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`), and the goods originate in a partner country of the Trade Accord. The reader cannot tell whether any duty was due, which one, or how much; the note may be a general remark on how this importer settles duties, but as worded it asserts that duties were paid on this declaration. The identical sentence is in six import declarations of the examples (counted with `grep -l "Duties paid by the importer" */*.xml` over `world/examples`: cotton, plastics, road, sea, tender and wood), so it is not specific to this import.
- Condition: a statement about duties in the declaration agrees with what is due on this import: either the duty (kind and amount) is stated, or the note says that none is due and why, or it describes the means of settlement without asserting a payment.
- Options: (a, preferred) reword to what applies here, e.g. "No customs duty under the Trade Accord; the importer is exempt from state sales tax as a public body."; (b) "Any duties are settled through the importer's deferment account at customs." if the world has such accounts.
- Needs decision: yes

## Checked and consistent
- 40 × 499 = 19960.00 lume; equal to the export declaration's 1996000 ferra at 100 ferra to the lume (`30-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000`), and to the order line.
- The value is in lume, the currency of the importing country. The installation is rightly not part of the customs value.
- The importer is the buyer, which fits the delivery term DAP of the order (import clearance by the buyer); nature of transaction PURCHASE and release for free circulation fit an outright purchase.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: an exemption from sales tax worded as a sale ("Sale to a public body") on an importer — refuted for the money lens: it is the party's standing data and identical in all examples; whether the wording describes a status or a transaction belongs to the review of the party.
