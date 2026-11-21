# LLM review: 05-ImportCustomsDeclaration.xml

Flow: modification (26-0015) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/05-ImportCustomsDeclaration.xml`, Git blob `362b4f90c54856bcf8a90fbd5dd03e8ef8d15bfb` (committed)
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

### modification/05#F1 · Low · The import value does not reconcile with the export value in 04
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1212000`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:DeclaredStatisticsValueAmount` = `1212000`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `11520.00`
- Why: See 04#F1: at 100 ferra to the lume (`wood/08-Invoice.xml:/Invoice/cac:TaxExchangeRate/cbc:CalculationRate` = `100`) the export value is 1,152,000 ferra; the import value is 60,000 ferra higher with no stated reason. Both cite the same pro-forma `MDS-PF-26-0113`.
- Condition: the values reconcile, or the declarations state what makes the difference.
- Options: as 04#F1.
- Needs decision: yes

### modification/05#F2 · Low · The release of the processed slats in Urvania has no document in the flow
- XPath: `/ImportCustomsDeclaration/cbc:Note[2]` = `Inward processing: no duty and no import value added tax while the goods are worked under the procedure. The goods are of Accord origin; the import value added tax of 20 % …`
- XPath: `07-OrderChange.xml:/OrderChange/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The goods enter under inward processing; the note says import VAT is due "only when the processed products are released for free circulation". 07 delivers all 96 bundles to Valdara Industries in Ferrano, Urvania, so the procedure has to be discharged by a release for free circulation (with the 20 % import VAT on the stated value), but no example of the flow does that, and none says who declares it (the owner Marrowdale, Tostara as holder, or Valdara). The reader of the flow cannot tell how the goods leave the procedure.
- Condition: the flow shows, or its documents state, how the inward-processing procedure is discharged for the slats delivered to Valdara.
- Options: (a) a release declaration for the slats as a further example; (b) preferred, if no document is wanted: a statement in 07 or 08 of who declares the release (the cheaper change); (c) re-export, which 07 contradicts.
- Needs decision: yes

## Checked and consistent
- `/ImportCustomsDeclaration/cac:AdditionalDocumentReference[3]/cbc:ID` = `MDS-EX-26-0011` resolves to 04-ExportCustomsDeclaration.xml; shipment, consignment, 12 units, 14,448 kg and 2,400 blanks agree with 03 and 04.
- Inward processing (SubTypeCode `INWARDPROC`, nature `PROCESSING`) agrees with 01 (the customer's own ash, which stays its property) and with the authorisation `XU-IP-AUT-0217`; validity of six months covers the job.
- The two language versions of the note agree (both state 20 % and 1,212,000 ferra).
- `/ImportCustomsDeclaration/cbc:IssueTime` = `10:30:00-01:00`: after the export declaration (08:20) and the despatch (08:10), on the day of the crossing.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyName/cbc:Name` = `Tostara Wood Modification`: the definition asks for the owner "or [the party with] similar right of disposal", and the note says the sawmill owns the goods — refuted: the holder of an inward-processing authorisation declares the goods and has the right of disposal under the procedure; the note names the owner.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `S` with 20 % while no VAT is charged — refuted: it is the category that applies at release, which the note explains.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P` (wholly obtained) for sawn timber — refuted: sawn wood from trees felled in the country is usually wholly obtained under preferential origin rules (own knowledge).
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyIdentification/cbc:ID` = `xu_k4r7`: a format unlike Bayvarra's public-body numbers — refuted: the same identifier is used for this authority throughout (27 occurrences, `grep -o` over `*.xml`).
- `/ImportCustomsDeclaration/cbc:ProfileExecutionID` = `26-0015` differs from the order collaboration — refuted: the import declaration is Tostara's own collaboration with its customs authority.
