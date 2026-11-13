# LLM review: 15-ImportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/15-ImportCustomsDeclaration.xml`, Git blob `243bca671cf988608608ddfeb177ea4ed50c7765` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### cotton/15#F1 · Medium · Shipment gross weight without the container
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: as cotton/11#F1: the shipment's gross weight by definition includes the transport equipment, the goods item's excludes it; the same 6190.29 kg in both, for a shipment that arrived in a container with a verified gross mass of 9940.29 kg.
- Condition: the shipment gross weight includes the container, or only the goods-item gross weight is given.
- Options: (preferred) drop the shipment gross weight.
- Needs decision: no

### cotton/15#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/15#F3 · Low · Customs value is the FOB price; the sea freight paid by the importer is left out
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `15138.63`
- XPath: `16-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `2950.00`
- Why: 15138.63 XBL is exactly the FOB invoice value converted (6055.452 XLC × 2.5). Under the WTO valuation agreement most customs territories add the cost of transport to the place of importation (CIF basis); some use FOB (own knowledge). The mill paid 2950.00 XBL sea freight for this shipment (17). The declaration does not say on which basis the value is declared, and nothing in the world's customs story here tells which basis Bayvarra uses.
- Condition: the declared customs value follows a stated valuation basis of Bayvarra: if CIF, it includes the 2950.00 XBL freight (and insurance); if FOB, the basis is stated.
- Options: (preferred) decide Bayvarra's valuation basis in the world's customs story and apply it (CIF: 18088.63 XBL plus any insurance); or keep FOB and state it.
- Needs decision: yes

### cotton/15#F4 · Low · Import declaration with the exit office but no office of import
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs and Border Service of Bayvarra`
- Why: an import declaration is lodged at the office where the goods enter (Lumeport); the declaration names only the Lisavan exit office, which belongs to the export, not the Bayvarran office that releases the goods.
- Condition: the declaration names the Bayvarran office of import (or entry); the exit office appears only if Bayvarra's procedure needs it.
- Options: (preferred) add the office of import at the port of Lumeport (as a location of the shipment or the customs party's address), and keep the exit office only as information from the previous declaration.
- Needs decision: no

### cotton/15#F5 · Low · Neither the number of bales nor the phytosanitary certificate
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0206`
- Why: the declaration counts no packages and cites only the bill of lading, although the lint may enter Bayvarra only with the phytosanitary certificate issued for it (10: "free of the pests named by Bayvarra's plant health rules").
- Condition: the declaration states the number of bales and refers to the phytosanitary certificate SCC-GC-26-0202.
- Options: (preferred) package count 27 bales and an additional document reference to SCC-GC-26-0202 with its type.
- Needs decision: no

### cotton/15#F6 · Low · Classing results in the applicant's remarks
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: as cotton/02#F5.
- Condition: the result is not carried as an applicant's remark.
- Options: (preferred) drop the remark.
- Needs decision: no

### cotton/15#F7 · Low · Origin area in `Region`, in `District` in the farm's address
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- Why: as cotton/02#F6.
- Condition: the north coast in the same element everywhere.
- Options: (preferred) `District`.
- Needs decision: no

### cotton/15#F8 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: as cotton/02#F7.
- Condition: the bale weight is not carried as a count.
- Options: (preferred) drop the pack elements; count the bales (F5).
- Needs decision: no

### cotton/15#F9 · Low · The importer's contact is its purchasing desk in sales
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: as cotton/02#F3; customs questions go to the importer's import / customs desk.
- Condition: name, title and department agree and fit the importer role.
- Options: (preferred) an import desk contact.
- Needs decision: no

## Checked and consistent
- 6055.452 XLC × 2.5 (the coral-to-Lume rate used in 04/05) = 15138.63 XBL.
- Previous customs declaration SCG-CD-26-0204 is the export declaration's customs declaration in 11; the bill of lading reference resolves to 13.
- Issued 6 March, after the pre-arrival report (3 March); valid 30 days.
- Shipment ID, goods description, quantity and gross weight agree with 10, 11 and 13; importer, consignor and consignee agree with 09–13.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:NotifierParty`: the importer also as notifier — refuted: "the Party who is responsible for contact on master level" may be the importer itself.
- `/ImportCustomsDeclaration/cbc:Note`: duties paid but no duty amounts in the declaration — refuted: the declaration declares; the assessment and payment are the authority's documents.
