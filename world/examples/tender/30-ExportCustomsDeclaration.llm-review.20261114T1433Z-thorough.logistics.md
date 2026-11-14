# LLM review: 30-ExportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/30#F1 · High · The declared goods are identified as the grey variant; the shipment is moss green
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- Why: The declaration covers shipment `CL-SH-26-0216`, which according to `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.` consists of the green variant ordered by the change of 24 March and accepted on 25 March, five days before this declaration. The item variant, the colour code GRY and the property "Frame colour: Ferro grey" describe goods that are not in the lorry.
- Condition: The item's variant and colour data describe the goods of the shipment (moss green), or the declaration carries no colour data.
- Options: (a) preferred: reduce the item to what customs needs (description, classification, origin), without variant and colour; (b) the green variant's identification, as in the corrected despatch advice.
- Needs decision: no

### tender/30#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg CO2e; see `25-Catalogue.xml` (F4 of its review). 39 examples across flows carry these values (files containing `ValueFactorNumeric>0.82<`, grep over `world/examples/**/*.xml`).
- Condition: factor × base = value with the base in the factor's unit, or factor and base are absent.
- Options: as in 25.
- Needs decision: no

### tender/30#F3 · Medium · The customs value leaves out the colour surcharge of the goods
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000`
- Why: "The total declared value for customs purposes of the goods item." 1996000 XUF is 40 × 49900, the catalogue price of the standard bench. The price agreed for these goods since 25 March includes the special-colour charge (`28-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00` XBL = 2016000 XUF), and the invoice treats that total as the value of the exported goods (`32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`, category "Export of goods outside Urvania"). The value declared at export is 20000 XUF lower than the value the same exporter claims the export exemption on. (That customs value follows the price actually payable for the goods is my knowledge of customs valuation practice; under other valuation rules of the fictional countries the figure could differ, but not between the exporter's own two documents.)
- Condition: The declared customs value agrees with the price of the goods in the order response and the invoice, or a stated valuation rule explains the difference.
- Options: (a) preferred: 2016000 XUF; (b) state the valuation basis.
- Needs decision: no

### tender/30#F4 · Low · Exit office named by a description, not as a place
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: "The location of the exit office from where the goods will leave or have left the customs territory"; a location's name is "the name of this location". The value describes the kind of office but does not say which border crossing it is; it has no identifier and no address, so the office cannot be told from any other post on that border. The same text is the exit office in `31-ImportCustomsDeclaration.xml`.
- Condition: The exit office is identified by the name of the crossing (and an office identifier where the world has one).
- Options: name the border crossing on the Ferrano–Lumeport road as the map knows it (preferred), with an office ID.
- Needs decision: no

### tender/30#F5 · Low · No packages, net weight or means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem`
- Why: The goods item gives description, value, gross weight (1660 kg) and quantity (40 EA). Number and kind of packages (ten pallets), the net weight and the means of transport crossing the border (the lorry of Trasvia Haulage) are absent; from my knowledge of customs declarations these are standard particulars, and the exit office needs at least the packages and the vehicle to match the goods presented to the declaration. Missing details the document could carry.
- Condition: The declaration states the packages and net weight of the goods item and identifies the border-crossing means of transport.
- Options: `cac:GoodsItem/cac:Package` (10 pallets) and `cbc:NetWeightMeasure`; a shipment stage with the lorry (preferred).
- Needs decision: no

### tender/30#F6 · Low · Supporting document with only an ID
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: "A reference to additional documents relevant or related to this customs declaration." The ID resolves to the buyer's order (`26-Order.xml`), but the reference does not say that it is an order; customs cannot know the buyer's numbering.
- Condition: The reference states the kind of document (type code or type).
- Options: add `cbc:DocumentTypeCode`/`cbc:DocumentType` for a purchase order (preferred).
- Needs decision: no

### tender/30#F7 · Low · Signature identifier carries the flow's name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-tender`
- Why: "An identifier for this signature." The suffix "tender" is the name of the example flow, not something Valdara would put in the identifier of its signature on an export declaration; its other signature IDs are business-like (`32-Invoice.xml:/Invoice/cac:Signature/cbc:ID` = `VI-SIG-26-0078`).
- Condition: The signature ID does not contain the flow name.
- Options: a numbered ID like the invoice's (preferred).
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no failures.
- Issue time 30 March 13:40 precedes the despatch advice (17:37), in line with the note "Declared electronically before the goods leave"; validity 90 days from 30 March.
- Shipment CL-SH-26-0216, consignment CL-CS-26-0217, carrier and permit, gross weight 1660 kg (shipment = goods item) and quantity 40 EA agree with `29-DespatchAdvice.xml`. (The plausibility of 1660 kg is questioned in the review of 29, F6.)
- Declaration ID VI-CD-26-0219 is the one the import declaration cites as previous declaration.
- Exporter and consignor Valdara, consignee the department: fits DAP. Territory XU is the customs territory left.
- Classification: HS 940179, national code 94017910 ("Benches for parks and gardens…") of the Urvanian tariff, the right tariff for an Urvanian export; origin XU.
- FunctionCode 9 = Original (UNCL 1225); ExportTypeCode PERMANENT and ExportReasonCode SALE fit a sale.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID`: the order instead of the commercial invoice — refuted: the invoice is issued only on 31 March, after the declaration.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 90 days for goods leaving the same day — refuted: a validity of the declaration, not a transport time.
