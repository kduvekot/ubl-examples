# LLM review: 31-ImportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/31#F1 · High · The declared goods are identified as the grey variant; the shipment is moss green
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- Why: The declaration covers shipment `CL-SH-26-0216`, which is `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.` The importer is the party that asked for the green benches (27); its own declaration describes grey ones.
- Condition: The item's variant and colour data describe the goods of the shipment, or the declaration carries no colour data.
- Options: (a) preferred: reduce the item to what customs needs; (b) the green variant's identification.
- Needs decision: no

### tender/31#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg CO2e; see `25-Catalogue.xml` (F4 of its review). 39 examples across flows carry these values (files containing `ValueFactorNumeric>0.82<`, grep over `world/examples/**/*.xml`).
- Condition: factor × base = value with the base in the factor's unit, or factor and base are absent.
- Options: as in 25.
- Needs decision: no

### tender/31#F3 · Medium · Goods imported into Bayvarra are classified with the Urvanian tariff
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: The national subdivision of the HS code is taken from `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, the customs tariff of Urvania, the country of export. This is a declaration for release for free circulation in Bayvarra (`/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XB`), lodged with the Customs and Border Service of Bayvarra, which assesses duty by its own tariff (or a common Trade Accord tariff, if there is one; the list name says XU). A code from the exporting country's list is not the classification this document needs. All 39 occurrences of the code in the examples use the XU list (grep for `CustomsTariffCode">94017910` over `world/examples/**/*.xml`); no XB tariff list occurs.
- Condition: The national tariff code of an import declaration comes from the tariff of the importing territory.
- Options: (a) a Bayvarran (or Trade Accord) tariff code; (b) only the six-digit HS code 940179 in the import declaration. Which exists in the world is for its owner to say.
- Needs decision: yes

### tender/31#F4 · Medium · The customs value leaves out the colour surcharge of the goods
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`
- Why: "The total declared value for customs purposes of the goods item." The importer was invoiced that morning (09:28, before this declaration at 11:14) and the price of the goods is 19960.00 plus the special-colour charge of 200.00: `32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`, the amount it had itself agreed in the order change. The declared value is the price of the standard bench (40 × 499). The note speaks of duties paid, so the value matters. (That customs value follows the price payable for the goods is my knowledge of customs valuation practice.)
- Condition: The declared customs value agrees with the price of the goods on the invoice, or a stated valuation rule explains the difference.
- Options: (a) preferred: 20160.00 XBL; (b) state the valuation basis.
- Needs decision: no

### tender/31#F5 · Low · Only the foreign exit office is named, by a description; no office of entry and no supporting documents
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: The only customs office in this import declaration is the Urvanian exit office, named by a description that does not identify the crossing (see 30, F4). The Bayvarran office where the goods enter and are cleared is not given (the customs party is the service as a whole), nor the carrier or vehicle presenting the goods (the export declaration names Trasvia Haulage), nor packages or net weight, nor the commercial invoice `VI-INV-26-0221`, which exists by then and on which value and origin rest. Missing details the document could carry.
- Condition: The declaration identifies the office of entry on the Bayvarran side and the supporting commercial document; the exit office, if kept, is a named place.
- Options: add the entry office as a location of the customs party or in a note, an `AdditionalDocumentReference` to the invoice, and packages (preferred); name the crossing.
- Needs decision: no

### tender/31#F6 · Low · Signature identifier carries the flow's name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LPWD-SIG-IM-tender`
- Why: "An identifier for this signature." "tender" is the name of the example flow; the department's other signature IDs name the document (PWD-SIG-CONTRACT, PWD-SIG-OC).
- Condition: The signature ID does not contain the flow name.
- Options: e.g. PWD-SIG-IM (preferred).
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no failures.
- Issue time 31 March 11:14 follows the export declaration (30 March 13:40), the despatch (30 March 17:37) and the invoice (31 March 09:28); validity 30 days from the issue date.
- `cac:PreviousCustomsDeclaration/cbc:ID` VI-CD-26-0219 is the ID of the customs declaration in `30-ExportCustomsDeclaration.xml`.
- Shipment CL-SH-26-0216, gross weight 1660 kg (shipment = goods item) and 40 EA agree with 29 and 30; 19960.00 XBL = 1996000 XUF at the flow's rate (the two declarations agree with each other).
- Importer and consignee the department, consignor Valdara: fits DAP (buyer clears import). Jurisdiction XB.
- TypeCode IMPORT, SubTypeCode FREECIRC, NatureOfTransactionCode PURCHASE: in their lists and fitting a purchase released for free circulation. HS 940179 fits; origin XU.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID`: a declaration of another party to another country's customs as "a previously sent customs declaration" — refuted: linking the import to the export declaration of the same movement is a reasonable use, and the ID resolves.
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation`: an exit office in an import declaration — refuted as to presence: the element is defined for this document ("Customs exit office of the goods being declared"); its content is F5.
