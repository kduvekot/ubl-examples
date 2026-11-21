# LLM review: 04-ExportCustomsDeclaration.xml

Flow: modification (MDS-TX-26-0051) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/04-ExportCustomsDeclaration.xml`, Git blob `09ddb71b4b4602bafcd39426d68e91b7d8e6b483` (committed)
- Last commit changing the example: 1b71959a 2026-11-20 O260: every document belongs to the collaboration it is exchanged in
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### modification/04#F1 · Low · The export value does not reconcile with the import value in 05
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `11520.00`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1212000`
- Why: The same 2,400 blanks of the same shipment are declared at 11,520.00 lume for export (4.80 lume a blank) and at 1,212,000 ferra for import. At the rate the world uses elsewhere (the tax exchange rate `wood/08-Invoice.xml:/Invoice/cac:TaxExchangeRate/cbc:CalculationRate` = `100` ferra to the lume, 2026-02-26) the export value is 1,152,000 ferra, 60,000 ferra (5.2 %) less. An import value can legitimately include the transport to the border, but nothing in either declaration says so, and the sawmill carries the goods on its own truck.
- Condition: the two values reconcile at the rate of the day, or the difference is explained by a stated cost (transport to the border) in the declarations.
- Options: (a) preferred: derive both from the pro-forma MDS-PF-26-0113 and one rate; (b) keep the difference and state the added transport cost.
- Needs decision: yes (whether the difference is intended)

## Checked and consistent
- Shipment `MDS-SH-26-0051`, consignment `MDS-CS-26-0051`, 12 handling units, 14,448 kg and 2,400 blanks agree with 03 and 05.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`: the sawmill's own truck, as 01's note says.
- HS 440795 (sawn ash, over 6 mm) and CPC 31102 fit 51 mm ash blanks; origin Bayvarra.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference[1]/cbc:ID` = `MDS-PO-26-0047` resolves to 01; 05 refers back to this declaration by `MDS-EX-26-0011`.
- Issue time 08:20 after the despatch advice (08:10) on the day of despatch; note "declared before the goods leave".

## Considered and refuted
- `/ExportCustomsDeclaration/cbc:ExportTypeCode` = `PERMANENT` with `/ExportCustomsDeclaration/cbc:ExportReasonCode` = `PROCESSING`: processing abroad usually means temporary export (outward processing) — refuted because the processed slats do not come back: 07 sends them from Tostara to Valdara Industries in Urvania. A permanent export whose reason is processing abroad fits.
- `/ExportCustomsDeclaration/cbc:ProfileExecutionID` = `MDS-TX-26-0051` differs from `MDS-TX-26-0047` of the order documents — refuted: the export declaration is a separate collaboration with the customs authority, numbered after the shipment `MDS-SH-26-0051`.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference[2]/cbc:ID` = `MDS-PF-26-0113` is not an example of the flow — refuted as a broken reference: a pro-forma for goods sent free of charge is the usual basis of their customs value, and it need not be an example.
