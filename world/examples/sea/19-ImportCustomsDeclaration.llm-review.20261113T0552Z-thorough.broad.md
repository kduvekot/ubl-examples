# LLM review: 19-ImportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/19#F1 · Medium · Shipment gross weight leaves out the container
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: UBL defines Shipment/GrossWeightMeasure as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment." The value 4 106.4 kg is the sum of the two goods items (3 984 + 122.4), i.e. without the container; with the container's tare of 3 750 kg (manifest) the shipment weighs 7 856.4 kg, as the manifest gives for the container.
- Condition: The shipment gross weight includes the transport equipment (7 856.4 kg), or the goods-only weight is carried in an element meant for it (e.g. the goods items, or a consignment's gross weight).
- Options: (a) preferred: 7 856.4 kg, following the definition; (b) keep 4 106.4 only at goods-item / consignment level and leave the shipment weight out.
- Needs decision: no

### sea/19#F2 · Medium · The commercial invoice the customs value rests on is not referenced
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InvoiceLine/cbc:ID` = `1`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- XPath: `22-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `49920.00`
- Why: The declared customs value (19 968.000 XLC = 49 920.00 XBL × 0.4) is the invoice value of line 1 of Lumeway's invoice `LD-INV-26-0147` (`22-Invoice.xml`), and goods item 1 points to "invoice line 1", but the declaration nowhere says which invoice; its only document reference is the bill of lading. For a release for free circulation of a purchase, the commercial invoice is the basis of the customs value and is referenced in the declaration. Goods item 2 has no invoice line at all.
- Condition: The declaration references invoice `LD-INV-26-0147`, and each goods item points to its invoice line.
- Options: add an additional document reference to `LD-INV-26-0147` (with a type) and an invoice line `2` for goods item 2. Preferred: both.
- Needs decision: no

### sea/19#F3 · Medium · Gate number in AdditionalStreetName of the consignor's postal address
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`; the gate, if needed, is in a delivery or pickup location.
- Options: drop it from the postal address (preferred); keep it only where goods are collected.
- Needs decision: no

### sea/19#F4 · Low · Freight share given for the benches only
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:Amount` = `1162.121`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `307.200`
- Why: The ocean freight of 2 950 XBL (`14-BillOfLading.xml`: 2 700 + 250) is apportioned by value: 2 950 × 49 920 / 50 688 = 2 905.303 XBL × 0.4 = 1 162.121 XLC for the benches. The remaining share for the castings (2 950 × 768 / 50 688 = 44.697 XBL = 17.879 XLC) is not given, so the freight to be added to the customs value under CIF is incomplete.
- Condition: Each goods item carries its freight share, or the freight is given once for the shipment.
- Options: add a freight charge of 17.879 XLC to goods item 2 (preferred); or state the freight once at shipment level.
- Needs decision: no

### sea/19#F5 · Low · Urvanian national tariff used in a Lisavu import declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The national tariff codes carry the list `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, the tariff of Urvania (the country of origin). An import declaration lodged with the Island Customs Service classifies goods in the importing country's (or a common Accord) tariff. The same XU list is the only national tariff list in all examples (61 uses, `grep -o` of the listID over `*.xml`), also in Bayvarra's export declaration `11-ExportCustomsDeclaration.xml`.
- Condition: The national tariff code in the declaration is from the tariff that applies at Lisavu import, or the world states that the Urvanian tariff is the common tariff of the Accord.
- Options: introduce a Lisavu (or Accord) tariff list; or record that the XU tariff is common.
- Needs decision: yes

### sea/19#F6 · Low · Power of attorney: notarised by the chamber of commerce, witnessed by the warehouse, mandate reference without meaning
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:NotaryParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:WitnessParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:MandateDocumentReference/cbc:ID` = `MAND-2026-014`
- Why: A chamber of commerce is not a notary (it may certify origin or signatures, but `NotaryParty` is "The Party who notarises this Power of Attorney"). The witness is a company, Nalevi Warehousing, the consignee's warehouse; a witness is normally a person. The mandate reference `MAND-2026-014` occurs in no other example and gives no type, so it is unclear what mandate (customs representation, direct debit of duties) it is.
- Condition: The notary is a party that notarises; the witness, if any, is a person with a reason to witness; the mandate reference says what it is or is left out.
- Options: a notary as `NotaryParty` (or no notary), drop the company witness, give the mandate a document type or drop it.
- Needs decision: no

### sea/19#F7 · Low · Product master data copied into the customs declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- Why: Warranty, search keywords, the seller's trade conditions, maintenance and repairability data and the load test are catalogue data; customs does nothing with them in a release for free circulation. They look copied from the item's master data (the same blocks appear in `20-DespatchAdvice.xml`, `21-ReceiptAdvice.xml` and `22-Invoice.xml`).
- Condition: The item in the declaration carries what customs uses (description, identification, classification, origin, value) and data with a customs purpose only.
- Options: reduce the item to the customs-relevant data (preferred); keep any element only with a stated customs reason (e.g. emission data for a border carbon measure).
- Needs decision: no

### sea/19#F8 · Low · Customs authority described as a company; importer contact inconsistent
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The Island Customs Service is a public authority: it is not in the commercial companies register and has no liquidation status. The importer's contact is named Purchasing but is a customer service officer in Sales; for the importer of record, the contact customs needs is the one responsible for imports.
- Condition: The authority carries no commercial-register/liquidation data; the importer contact's name, title and department agree and fit the import.
- Options: drop those legal-entity elements for the authority; give Velumi an import/logistics contact.
- Needs decision: no

## Checked and consistent
- Values: 49 920.00 XBL × 0.4 = 19 968.000 XLC and 768.00 × 0.4 = 307.200 XLC, the rate of `22-Invoice.xml` (XBL→XLC 0.4); the same values in XBL in `11-ExportCustomsDeclaration.xml`. Insured value 59 155.80 XBL = 53 778 × 1.1 (CIF + 10 %), as on `14-BillOfLading.xml`, policy `WS-CP-26-4471`.
- Weights: 3 984 + 122.4 = 4 106.4 kg; 3 984 / 96 = 41.5 kg per bench including its share of 24 pallets; 122.4 / 12 = 10.2 kg per casting; 7 856.4 − 3 750 = 4 106.4 (manifest).
- Previous declaration `BF-CD-26-0136` resolves to the customs declaration inside `11-ExportCustomsDeclaration.xml`; B/L `TOL-BL-26-0139` resolves; shipment `LD-SH-26-0132`, consignor, consignee (Velumi, as on the B/L) and forwarder agree.
- Quantities 96 benches and 12 castings agree with invoice lines 1 and 2 of `22-Invoice.xml`.
- GTINs `9520610000012`, `9520610000029` and GLN `9520610900008` pass `check_ids.py`; HS 940179 / 732599 fit benches with metal frames and cast steel parts.
- Issue 2026-05-19 09:07 follows discharge (05-18 11:20) in `17-TransportationStatus.xml`.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.`: suspected contradiction with the B/L's "Island customs fees advanced by the broker and recharged to the consignee" and the power of attorney for paying duties — refuted: the B/L speaks of the broker's fees, the note of duties, and the broker can pay through the importer's account under the power of attorney.
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`: an exit office in an import declaration — refuted: it is the export exit office of the goods, which import declarations may record.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`: value without freight under CIF — refuted: the freight is given separately in the goods item's freight charge, from which customs builds the CIF value (but see F4).

## Outside this review
- `15-Manifest.xml` gives the same 4 106.4 kg as shipment gross weight; belongs to that example's review.
