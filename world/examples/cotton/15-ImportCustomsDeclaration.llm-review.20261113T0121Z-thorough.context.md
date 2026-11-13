# LLM review: 15-ImportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/15-ImportCustomsDeclaration.xml`, Git blob `243bca671cf988608608ddfeb177ea4ed50c7765` (committed)
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

### cotton/15#F1 · Medium · PackSizeNumeric carries the bale weight in kilograms, not a number of items
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: Item/PackSizeNumeric is "The number of items in a pack of this item"; 227 is the bale weight
  in kilograms. As in 02, 07, 08, 10, 11 and 16.
- Condition: no element meant for a count holds the bale weight.
- Options: (a, preferred) leave PackSizeNumeric out; give the bale weight, if needed, as an item
  property with a KGM quantity.
- Needs decision: no

### cotton/15#F2 · Low · The import declaration names the exporting country's exit office and its export declaration, but not the office of entry
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`
- XPath: `/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: The declaration applies in Bayvarra and is processed by the Customs and Border Service of
  Bayvarra. CustomsExitOfficeLocation ("Customs exit office of the goods being declared") names the
  Lisavu office at the port of Selanu, an office of another customs administration that plays no
  part in Bayvarra's release for free circulation; the office where the goods enter and are
  declared, at Lumeport, is not given. PreviousCustomsDeclaration ("A reference to a previously sent
  customs declaration") cites the Lisavu export declaration, which is a declaration of another
  declarant to another administration, not a previous declaration of this import (such as a
  summary or temporary storage declaration). Both values are real, but not the ones this document's
  elements are for.
- Condition: the offices and previous declarations in the import declaration are those of
  Bayvarra's procedure (entry at Lumeport), and the Lisavu export declaration, if cited, is cited as
  a supporting document.
- Options: (a, preferred) leave the exit office out, add the Lumeport customs office as the office of
  entry or declaration if the model offers one, and move SCG-CD-26-0204 to an
  AdditionalDocumentReference typed as the export declaration.
- Needs decision: no

### cotton/15#F3 · Low · The phytosanitary certificate made out for Bayvarra is not presented with the import
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0206`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cbc:Description` = `The ginned cotton is free of the pests named by Bayvarra's plant health rules.`
- Why: The phytosanitary certificate 10 exists because Bayvarra's plant health rules require it for
  this lint; it is valid for Bayvarra until 2026-03-14 and covers this shipment. The import
  declaration, which is where Bayvarra's border service would see it, references only the bill of
  lading. The item carries instead the commercial classing certificate, which no import control
  needs.
- Condition: the import declaration references the phytosanitary certificate SCC-GC-26-0202 (with
  its type), or the story says Bayvarra checks it elsewhere.
- Options: (a, preferred) add an AdditionalDocumentReference to SCC-GC-26-0202; consider leaving the
  classing certificate out of the item.
- Needs decision: no

### cotton/15#F4 · Low · Region of origin "North coast" is the farm's District elsewhere
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: The same area is a District in the farm's address and a Region here.
- Condition: North coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) use District in OriginAddress.
- Needs decision: no

## Checked and consistent
- Declared customs value 15,138.63 XBL = 6,055.452 XLC / 0.4 (the Lume–coral rate used elsewhere in
  the flow); gross 6,190.29 kg and net 6,129 kg as in 11 and 13.
- Importer, consignee and notifier are the mill; consignor the ginnery; type IMPORT, subtype
  release for free circulation and nature of transaction PURCHASE fit the sale of 08/16.
- AdditionalDocumentReference TOL-BL-26-0206 resolves to 13; issued 2026-03-06, after the B/L and
  the pre-arrival report 14.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `15138.63`:
  an FOB value as import customs value (no freight added) suspected — refuted for this lens because
  WTO valuation lets each member choose whether freight to the border is included (Art. 8.2), and the
  world's rule is not stated in the example; the money lens may look at it.
- `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`: a note on
  duties without duty amounts — refuted because the declaration states how duties are paid, not
  their assessment, which customs makes.
