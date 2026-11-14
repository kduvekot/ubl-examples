# LLM review: 30-ExportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/30-ExportCustomsDeclaration.xml`, Git blob `badd401509d1f287a27ff308ccae49e844329ef6` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit e0e5001 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/30#F1 · High · Gross weight of the shipment is less than the materials of the benches
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `40`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- Why: the goods item states for one bench 34 kg of steel and 22.5 kg of hardwood, 56.5 kg together; 40 benches are 40 × 56.5 = 2260 kg net, before anchors, bolts, packaging and about ten pallets (pallets of 4, 15). The declared gross weight of 1660 kg is 41.5 kg per bench, 600 kg below the net weight of the benches. A gross weight below the net weight is impossible, and the weight is one of the figures customs checks at the border. The same 1660 kg is in the despatch advice (29) and the import declaration (31).
- Condition: gross weight ≥ 40 × weight of a bench plus accessories, packaging and pallets, consistently in 29, 30 and 31, and consistent with the per-bench material figures.
- Options: (a) a gross weight of about 2600 kg in all three documents (preferred); (b) lower material figures per bench everywhere the item appears.
- Needs decision: no

### tender/30#F2 · High · The declared goods are the grey variant, the goods despatched are green
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: the benches of this shipment (CL-SH-26-0216) were ordered in moss green by the order change, accepted by the seller, and despatched as such: `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.` The export declaration describes the same goods with the grey variant's identifier and colour. A declaration that describes goods differently from what is on the lorry is a discrepancy at the customs check.
- Condition: variant identifier and colour of the declared item are those of the goods despatched.
- Options: (a) the green variant (preferred); (b) leave colour out of the declaration altogether (item reduced to what customs needs).
- Needs decision: no

### tender/30#F3 · Medium · Emission factor that does not lead to the emission value
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × the base of 1 bench is not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state. Same block as in the catalogue (25).
- Condition: factor × the stated base or activity gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric (preferred); (b) state the activity.
- Needs decision: no

### tender/30#F4 · Medium · Language code in LocaleCode; provinces in Region
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; provinces are in CountrySubentity.
- Options: (a) a locale code, and move the provinces (preferred).
- Needs decision: no

### tender/30#F5 · Low · The customs value leaves out the colour surcharge
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000`
- Why: "The total declared value for customs purposes of the goods item." 1996000 XUF is 40 × 49900 XUF (19960.00 XBL). The price actually payable for these goods includes the special-colour charge of 200.00 XBL agreed on 2026-03-25 (27, 28) and invoiced with them (`32-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `200.00`), i.e. 2016000 XUF. A transaction value normally includes all charges for the goods themselves (my knowledge of customs valuation); the import declaration should be compared.
- Condition: the declared value is the price payable for the goods including the colour charge, or the declaration says why it is excluded.
- Options: (a) 2016000 XUF (preferred); (b) keep 1996000 and treat the charge as a service outside the goods' value, in 31 and 32 too.
- Needs decision: yes (customs valuation rule of the world)

### tender/30#F6 · Low · The exit office is a description, not an identified office; the customs authority is described as a company
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: the exit office is "The location of the exit office from where the goods will leave or have left the customs territory". The name describes a kind of place and does not say which border post; there is no office code or address, although the customs party's border office has an address (Valico di Confine 22). The Customs Administration of Urvania is a state authority (ISIC 8411) and is given a commercial-register entry with a liquidation status.
- Condition: the exit office is named or coded so that it identifies one office; the authority carries no liquidation status and no commercial-register type.
- Options: (a) name and ID of the border post (preferred); remove the company attributes.
- Needs decision: no

### tender/30#F7 · Low · A signature ID that contains the name of the examples' flow
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-tender`
- Why: "An identifier for this signature" in Valdara's numbering. Other signatures of the flow are named after the document (PWD-SIG-CAN, CL-SIG-26-DA); this one ends in "tender", the name of the example flow, which is not something the exporter's system would know. It reads as a technical leftover.
- Condition: the signature ID is a business identifier in the exporter's own style.
- Options: (a) e.g. VI-SIG-26-EX (preferred).
- Needs decision: no

### tender/30#F8 · Low · Catalogue content and seller master data in a customs declaration; consignee addressed at the procurement office
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: customs needs description, classification, origin, quantity, weight and value. The goods item also carries search keywords, warranty, test method, emissions, circularity profile and repairability score from the catalogue. The exporter's contact for customs questions is the sales order desk. The consignee, to whom the goods are consigned, is given with the room of the procurement office and a procurement contact, not the depot that receives the benches (26), and as a company with a liquidation status.
- Condition: the declaration carries what customs uses; the consignee's address and contact are those of the receiving place.
- Options: (a) reduce the item; use the depot's address for the consignee; a customs or shipping contact for the exporter (preferred).
- Needs decision: no

## Checked and consistent
- Value arithmetic: 40 × 49900 XUF = 1996000 XUF = 19960.00 XBL × 100 (rate of 26/32).
- Shipment CL-SH-26-0216, consignment CL-CS-26-0217 and carrier Trasvia Haulage are those of the despatch advice (29); quantity 40 EA as despatched.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LPWD-PO-26-0212` is the order (26); the invoice (2026-03-31) did not yet exist when the declaration was made.
- Classification: HS 9401.79 lies in chapter 94, section XX "Miscellaneous manufactured articles"; the national code 94017910 extends it; origin XU.
- Exporter = consignor Valdara; consignee the department; the declaration applies in Urvania and is processed by the Urvanian customs administration at its border office.
- Issue 2026-03-30 13:40 precedes the despatch advice (17:37), in line with the note "Declared electronically before the goods leave."; function code 9 (original), version 1; export type permanent, reason sale.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 90 days for an export of the same day — refuted, a declaration's validity for exit is a customs rule of the world.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox`: post box and street in one address — refuted, the address type is POSTAL and both can be printed.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[1]/cbc:CargoTypeCode`: general cargo next to the HS code — refuted, palletised benches are general cargo.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted, the warehouse that despatches is relevant to an export.

## Outside this review
- Which border post lies on the road from Ferrano to Lumeport is a location question.
