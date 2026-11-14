# LLM review: 31-ImportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/31-ImportCustomsDeclaration.xml`, Git blob `f995e80c478f86074b7bfa4eca588151c5ee7767` (committed)
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

### tender/31#F1 · High · Gross weight of the shipment is less than the materials of the benches
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `40`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- Why: one bench contains 34 kg of steel and 22.5 kg of hardwood according to the same goods item, 56.5 kg; 40 benches are 2260 kg net, before anchors, bolts, packaging and pallets. The declared gross weight of 1660 kg (41.5 kg per bench) is 600 kg below that. Gross cannot be below net. Same figure in 29 and 30.
- Condition: gross weight ≥ 40 × weight of a bench plus accessories, packaging and pallets, consistently in 29, 30 and 31 and with the material figures.
- Options: (a) about 2600 kg in all three documents (preferred); (b) lower material figures per bench wherever the item appears.
- Needs decision: no

### tender/31#F2 · High · The declared goods are the grey variant, the goods despatched are green
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: the importer itself changed the order to moss green (27), and the shipment CL-SH-26-0216 was despatched as `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.` The importer's declaration describes the grey variant.
- Condition: variant identifier and colour of the declared item are those of the goods despatched, or colour is not stated.
- Options: (a) the green variant (preferred); (b) reduce the item to what customs needs.
- Needs decision: no

### tender/31#F3 · Medium · Urvania's national tariff code in an import declaration to Bayvarra
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: the declaration applies in Bayvarra and is processed by the Customs and Border Service of Bayvarra. The eight-digit code carries the list `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, the national tariff of Urvania, the exporting country. An import is classified in the tariff of the importing territory; beyond the six HS digits (940179, also given) national subdivisions differ by country. The code was carried over with the seller's item data.
- Condition: a national tariff code in the import declaration is from Bayvarra's tariff (or a common Trade Accord tariff), or only the HS code is given.
- Options: (a) Bayvarra's tariff code with its own list (preferred); (b) drop the national code and keep HS 940179; (c) if the Accord has a common tariff, name the list accordingly in both declarations.
- Needs decision: yes (whether the Trade Accord countries share a tariff)

### tender/31#F4 · Medium · Emission factor that does not lead to the emission value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × the base of 1 bench is not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state. Same block as in the catalogue (25).
- Condition: factor × the stated base or activity gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric (preferred); (b) state the activity.
- Needs decision: no

### tender/31#F5 · Medium · Language code in LocaleCode; province in Region
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; the province is in CountrySubentity.
- Options: (a) a locale code, and move the province (preferred).
- Needs decision: no

### tender/31#F6 · Low · The declaration cites no commercial document, and its value leaves out the colour surcharge
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0219`
- XPath: `/ImportCustomsDeclaration/cbc:NatureOfTransactionCode` = `PURCHASE`
- Why: the declaration is for a purchase, but refers neither to the invoice (VI-INV-26-0221, issued 2026-03-31 09:28, before this declaration at 11:14) nor to the order or contract; its only reference is the export declaration. The declared value is 40 × 499.00; the price payable for the goods includes the special-colour charge of 200.00 (`32-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `200.00`), and under the order's DAP terms the price includes carriage to Lumeport. Customs can verify the value only against the invoice.
- Condition: the import declaration refers to the commercial invoice, and the declared value is the invoice's price for the goods (including the colour charge) or says why it differs.
- Options: (a) add a reference to VI-INV-26-0221 and declare 20160.00 (preferred); (b) keep 19960.00 and treat the charge as outside the goods' value in 30 and 32 too.
- Needs decision: yes (customs valuation rule of the world)

### tender/31#F7 · Low · Only the foreign exit office is named, and by a description
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: "Customs exit office of the goods being declared." The name does not identify a particular office (no code, no place name). It is the Urvanian office; the Bayvarran office where the goods are presented appears only through the customs party's address (Border Crossing Road 36, Marrowdale).
- Condition: the office is named or coded so that it identifies one office.
- Options: (a) name and ID of the border post, the same as in 30 (preferred).
- Needs decision: no

### tender/31#F8 · Low · A signature ID that contains the name of the examples' flow
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LPWD-SIG-IM-tender`
- Why: the department's other signatures are named after the document (PWD-SIG-CAN, PWD-SIG-OC). "tender" is the name of the example flow, not part of a business identifier; and the prefix LPWD differs from the PWD prefix of the department's other signature IDs.
- Condition: the signature ID is a business identifier in the department's own style.
- Options: (a) e.g. PWD-SIG-IM (preferred).
- Needs decision: no

### tender/31#F9 · Low · Catalogue content in a customs declaration; public bodies as companies; importer addressed at the procurement office
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the goods item carries the catalogue's keywords, warranty, test method, emissions, circularity profile and repairability score, none of which an import declaration uses. The importing department and the customs service are public bodies (ISIC 8411) described as companies in a commercial register with a liquidation status. The consignor is given with its logistics provider, stock listing and order desk.
- Condition: the declaration carries what customs uses; public bodies carry no liquidation status and no commercial-register type.
- Options: (a) reduce the item and the parties (preferred).
- Needs decision: no

## Checked and consistent
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0219` is the customs declaration inside the export declaration (30); shipment CL-SH-26-0216, quantity 40 EA and weight are the same as there and in 29.
- Value: 19960.00 XBL = 1996000 XUF of the export declaration at 100 XUF per XBL.
- Importer = consignee = notifier: the department, which buys DAP and therefore clears the import itself; note "Duties paid by the importer's account at customs." agrees with DAP. The importer's customs trader number XB-TR-410548 is given.
- Customs party: the Bayvarran service at a border address in Marrowdale, Upland State; jurisdiction XB; contact "Border office".
- Issue 2026-03-31 11:14 follows the despatch (2026-03-30 17:37) and the export declaration; type import, free circulation, purchase.
- HS 940179 in section XX; origin XU.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID`: "previously sent" declaration, but the export declaration was sent by another party to another authority — refuted, it is the preceding declaration of the same movement.
- `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name`: the importer as its own notifier — refuted, the definition ("responsible for contact on master level") fits the declarant.
- `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 30 days here, 90 in the export declaration — refuted, two authorities with their own rules.
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name`: procurement office as customs contact — refuted, the department's buying office lodges the declaration; the goods' receiving place is not this document's concern.
