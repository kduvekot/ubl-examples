# LLM review: 19-ImportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/19-ImportCustomsDeclaration.xml`, Git blob `64061347e935665afd0ab08807b3400cadbb512f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### sea/19#F1 · Medium · Lisavu import declared with Urvania's national tariff codes
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: both codes carry listID urn:ubl-examples:world:XU:codelist:CustomsTariffCode, the list
  the world defines as "Urvania's national customs tariff … each country keeps its own tariff"
  (world/codelists/gc/XU-CustomsTariffCode.gc). The declaration is lodged with the Island Customs
  Service for release into free circulation in Lisavu (JurisdictionRegionAddress XL), so the
  national tariff line that matters is Lisavu's. The Urvanian line is the manufacturer's
  classification, carried over with the item description; the world has no Lisavu tariff list
  (only the XU list occurs, 61 times over `world/examples/*/*.xml`, counted with grep of the listID).
- Condition: the national tariff code in the import declaration is from Lisavu's tariff (or only
  the HS subheading is declared, if Lisavu declares at HS level).
- Options: (a, preferred) a Lisavu tariff list and its code; (b) declare only the six-digit HS code
  already present in CommodityClassification[1]; (c) state why Urvania's tariff applies.
- Needs decision: yes (whether Lisavu has its own tariff list)

### sea/19#F2 · Medium · Shipment gross weight without the container
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: Shipment/GrossWeightMeasure is "the total gross weight of a shipment; the weight of the
  goods plus packaging plus transport equipment". 4106.4 kg is the goods with their packaging
  (3984 + 122.4, the two goods items); the shipment travelled in container TWLU4120872 with a tare
  of 3750 kg, so by the definition the figure is 7856.4 kg (the container's gross weight in
  `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`).
  Customs practice declares gross mass without the container; under the semantic-conformance rule
  that does not change the element's meaning. The same value occurs in Shipment/GrossWeightMeasure
  of 8 examples of the flow (09, 10, 11, 12, 14, 15, 19, 20; XPath query over `sea/*.xml`).
- Condition: Shipment/GrossWeightMeasure includes the transport equipment, or the goods' gross
  weight is given in an element whose definition excludes it.
- Options: (a, preferred) leave the goods' weights on the goods items (they already sum to
  4106.4 kg) and give the shipment's gross weight with the container (7856.4 kg); (b) drop
  Shipment/GrossWeightMeasure here.
- Needs decision: no

### sea/19#F3 · Low · The import declaration does not say how the goods arrived
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: the declaration names an exit office ("customs exit office of the goods being declared")
  that belongs to Bayvarra's export, but neither the office of entry or of lodging in Selanu, nor
  the container (TWLU4120872), the vessel (Tidewell Harbour, voyage TH-26-19E), the mode of
  transport at the border or the arrival date. Only the bill of lading number, without a type,
  links the declaration to the transport. An import declaration is normally matched against the
  carrier's manifest (15-Manifest.xml) by exactly these data.
- Condition: the declaration identifies the transport by which the goods entered Lisavu (at least
  container or vessel/voyage, and the place of entry), and the bill of lading reference says it
  is one.
- Options: (a, preferred) a main-carriage ShipmentStage with mode, vessel and journey, the
  container on a TransportHandlingUnit, and the Selanu office as the location; (b) at least add
  the DocumentTypeCode to the reference and the Selanu office. The exit office may stay if
  Lisavu's customs ask for it.
- Needs decision: no

### sea/19#F4 · Low · The goods are not linked to the commercial invoice
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InvoiceLine/cbc:ID` = `1`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InvoiceLine/cbc:InvoicedQuantity` = `96`
- Why: GoodsItem[1] carries "information about an invoice line relating to this goods item", but
  the declaration does not say which invoice: the seller's invoice
  `22-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0147` (issued 2026-05-14, before this
  declaration) is not referenced anywhere. GoodsItem[2] (the 12 side frames) has no invoice line
  at all. The customs value is based on that invoice, so the link is what customs checks.
- Condition: the declaration refers to LD-INV-26-0147, and both goods items point to their lines
  in it.
- Options: an AdditionalDocumentReference to LD-INV-26-0147 (commercial invoice), and an
  InvoiceLine on GoodsItem[2] (line 2 of that invoice, if it is).
- Needs decision: no

### sea/19#F5 · Low · The insured value of the whole shipment is given on the benches only
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- Why: 59155.80 XBL is the insured value of the whole consignment (110 % of the CIF value
  53778.00, as in `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`).
  Here it is attached to goods item 1, the "insurance policies that apply to this goods item", so
  the benches appear insured for the full amount and the side frames (goods item 2) not at all.
- Condition: the shipment's insured value is not presented as the value of one goods item.
- Options: (a, preferred) move the policy to Shipment level (Shipment/InsurancePolicy or
  InsuranceValueAmount); (b) split the insured value per goods item.
- Needs decision: no

## Checked and consistent
- Weights: goods items 3984 + 122.4 = 4106.4 kg, equal to the packing list (10-PackingList.xml)
  and the bill of lading; quantities 96 benches and 12 side frames agree with both; 96 benches on
  24 pallets of 4 and 12 frames in one pallet of boxes (14-BillOfLading.xml) fit.
- Values: 19968.000 + 307.200 = 20275.200 XLC; at the bill of lading's rate 0.4 XLC per XBL this
  is 50688.00 XBL, the FOB value in 14-BillOfLading.xml (49920.00 + 768.00 XBL). The ocean freight
  share 1162.121 XLC = (2700 + 250) × 0.4 × 49920/50688 (freight split by value).
- References: shipment LD-SH-26-0132; PreviousCustomsDeclaration BF-CD-26-0136 is the declaration
  inside 11-ExportCustomsDeclaration.xml; TOL-BL-26-0139 is 14-BillOfLading.xml; consignor,
  consignee, forwarder and customs party match 14 and 15.
- Dates: issued 2026-05-19 09:07, after the discharge on 2026-05-18 (17-TransportationStatus.xml);
  validity from the issue date. GTINs 9520610000012 and 9520610000029 and GLN 9520610900008 pass
  their check digits.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `BF-CD-26-0136`: looked like a reference that does
  not resolve (the export declaration document is BF-EX-26-0135) — refuted because BF-CD-26-0136 is
  the ID of the CustomsDeclaration inside 11-ExportCustomsDeclaration.xml, and the element refers to
  a customs declaration, not to a document.
