# LLM review: 11-ExportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/11-ExportCustomsDeclaration.xml`, Git blob `6a4c14a5a30406d882ebdc39fccad12bc46c7e0e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### cotton/11#F1 · Medium · PackSizeNumeric carries the bale weight in kilograms, not a number of items
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: Item/PackSizeNumeric is "The number of items in a pack of this item"; 227 is the bale weight
  in kilograms ("compressed bales of about 227 kg"). As in 02, 07, 08, 10, 15 and 16.
- Condition: no element meant for a count holds the bale weight.
- Options: (a, preferred) leave PackSizeNumeric out; give the bale weight, if needed, as an item
  property with a KGM quantity.
- Needs decision: no

### cotton/11#F2 · Low · The export declaration does not cite the phytosanitary certificate issued for the shipment, nor the number of bales
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: A customs declaration for exporting plant products lists the supporting documents presented
  with it (own knowledge of customs practice); the phytosanitary certificate SCC-GC-26-0202, issued
  the day before for this very shipment, is not referenced, while the buyer's order is. The goods
  item states the net quantity in kilograms but not the number of bales (packages), which customs
  checks at exit. The declaration is complete enough to be read, but leaves out data its purpose
  usually depends on.
- Condition: the declaration references the plant health certificate of the shipment and states the
  number of packages, or the story says why neither is needed in Lisavu.
- Options: (a, preferred) add an AdditionalDocumentReference to SCC-GC-26-0202 with its type, and the
  27 bales as package quantity of the goods item.
- Needs decision: no

### cotton/11#F3 · Low · Region of origin "North coast" is the farm's District elsewhere
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: The same area is a District in the farm's address and a Region here.
- Condition: North coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) use District in OriginAddress.
- Needs decision: no

## Checked and consistent
- Exporter, consignor (ginnery), consignee (mill), customs (Island Customs Service) and the exit
  office at the port of Selanu fit an export from Lisavu under FOB Port of Selanu.
- Declared customs value 6,055.452 XLC is the order value of 08 (FOB value, the usual basis of an
  export value); gross 6,190.29 kg and net 6,129 kg agree with 09, 10, 13 and 15.
- The customs declaration ID SCG-CD-26-0204 is the one the import declaration cites as previous
  declaration
  (`15-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`).
- Issued 2026-03-01, before the bill of lading (2026-03-02, shipped on board), as the note
  ("Declared electronically before the goods leave") says.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`:
  a commercial classing certificate in a customs declaration suspected as unused — refuted because
  the grade affects the export value and cotton exports are commonly declared with their class.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:FunctionCode` = `9`: a message function code
  (UNTDID 1225) for a declaration — refuted because "Original" is the function of a first
  declaration, which is what the element asks.
