# LLM review: 11-ExportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/11-ExportCustomsDeclaration.xml`, Git blob `6df68444b58544480345d9e469661ab775d8d16a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/11#F1 · High · Emission value is not factor × base
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies"; 0.82 × 1 EA = 0.82, not 96 kg. 39 examples carry the factor 0.82 (`grep -l "<cbc:ValueFactorNumeric>0.82" world/examples/*/*.xml`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent (or the emission is absent from the declaration, F8).
- Options: (a) preferred: drop the emission from the declaration (F8); (b) factor 96 per 1 EA.
- Needs decision: no

### sea/11#F2 · Medium · Lumeway's earlier import declaration given as a previous version of this export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `IMPORT`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:FunctionCode` = `9`
- Why: `PreviousCustomsDeclaration` is "A reference to a previous version of this customs declaration". The referenced document is Lumeway's import declaration of the same 96 benches and 12 castings in March (`road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`, issued 2026-03-24): an earlier, different declaration, not a version of this one, which is itself an original (`FunctionCode` 9). In addition, `FunctionCode` is "A code describing the function of this customs declaration" (original, replacement …, UN/EDIFACT 1225 as in this declaration's own `FunctionCode`); `IMPORT` is a declaration type from another list. The link to the import (a "previous document" in customs terms) is a real business fact, but this element does not express it.
- Condition: `PreviousCustomsDeclaration` refers only to an earlier version of this export declaration, with a function code from the function list; the import declaration, if referenced, is referenced as an additional document of its kind.
- Options: (a) preferred: reference the import declaration as `AdditionalDocumentReference` with a document type code for an import declaration; (b) drop the reference.
- Needs decision: no

### sea/11#F3 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; a product LCA boundary is not a load factor. 39 examples carry this code in this element.
- Condition: `FullnessIndicationCode` is absent from product emissions or holds a fullness code.
- Options: (a) preferred: drop it (or the whole emission, F8).
- Needs decision: no

### sea/11#F4 · Medium · Spare side frame declared as a general cast article, not as a part of a seat
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:NatureCode` = `XV`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: a side frame made for the Serra bench is a part of a seat (HS 9401.99, Section XX); Section XV Note 1 excludes articles of Chapter 94 from heading 7325 (own knowledge of HS 2022). In a customs declaration the classification is what is declared. 22 examples carry 732599.
- Condition: HS, section, national tariff and CPC codes classify the side frame as a part of a seat.
- Options: (a) preferred: HS 940199, section XX, matching tariff and CPC codes.
- Needs decision: no

### sea/11#F5 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/11#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in the exporter's postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/11#F7 · Low · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Customs and Border Service of Bayvarra is a public authority; it is not registered in the federal business register as a commercial entity and has no liquidation status (section 5: "a public body … is not a company in a commercial register and has no liquidation status").
- Condition: the authority's legal entity carries no commercial registration or liquidation status (or no legal entity at all).
- Options: (a) preferred: drop `PartyLegalEntity` (or keep only the registration name); (b) a public-body register, if the world has one.
- Needs decision: no

### sea/11#F8 · Low · Product sheet in an export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`
- Why: customs needs the goods described, classified, valued, weighed and their origin; the bench's goods item also carries the catalogue's product data (emissions with calculation method, circularity profile, item properties, dimensions, sales conditions, specification and repair documents). The declaration does nothing with them.
- Condition: the goods items carry what the export declaration uses, unless the declaration states a use for more.
- Options: (a) preferred: keep description, identifiers, origin and classification; drop emissions, circularity, properties, dimensions and sales conditions.
- Needs decision: no

### sea/11#F9 · Low · Customs offices by name only, and the exit office twice
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExitLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExportLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`
- Why: customs offices are identified by an office code in a declaration; here they have names only. The exit office is stated twice, once for the consignment and once for the declaration, with no difference. Lumeway is in Marrowdale, inland, and declares at the port; that the office of export is the port office is possible, but nothing identifies it.
- Condition: each customs office is identified (an office code or at least a location ID such as the port's UN/LOCODE), and the exit office is stated once unless the two places differ.
- Options: (a) preferred: an office identifier for each office and one exit office; (b) none better seen.
- Needs decision: no

### sea/11#F10 · Low · Commercial document reference: the buyer's order by ID only
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: the only supporting document is the buyer's order number, without a type code saying it is an order. An export declaration normally rests on the commercial invoice and the transport document; the order is the weakest evidence of the sale and the declared value. The reference does not say what it is.
- Condition: the supporting documents are referenced with their document type, and the declaration references the documents it rests on (at least the commercial or pro-forma invoice or the packing list).
- Options: (a) preferred: add a type code to the order reference and reference the packing list (`LD-PL-26-0134`, though it is issued later that day, see "Outside this review"); (b) none better seen.
- Needs decision: no

### sea/11#F11 · Low · Contacts whose function does not fit
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the exporter's contact for customs is Sales' customer service; the consignee's contact is purchasing with the job title of a seller's customer service.
- Condition: each contact's name, job title and department agree with each other and fit the party's role.
- Options: (a) preferred: an export/shipping contact for Lumeway; a goods-in or customs contact for the consignee.
- Needs decision: no

### sea/11#F12 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the order Velumi sent tags the same renderings `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); across the flow the tag follows the sender's country (16 × `en-XB`, 8 × `en-XL`).
- Condition: Velumi's address renderings carry the same `languageID` in every example.
- Options: (a) preferred: `en-XL` everywhere.
- Needs decision: no

## Checked and consistent
- Values: goods items 49,920.00 + 768.00 = 50,688.00 = declared customs, statistical and FOB value, as in the order; insured value 59,155.80 = 110 % of the CIF value 53,778.00 (goods + 2,950.00 freight + 140.00 insurance); ocean freight 2,950.00 agrees with the invoice's freight charge (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`).
- Weights 3,984 + 122.4 = 4,106.4 kg and quantities 96 and 12 agree with the packing list; shipment and consignment IDs agree with the forwarding instructions and the packing list.
- The import declaration referenced is of the same goods (96 and 12 units, origin Urvania), which fits the story of goods from Lumeway's stock re-exported.
- Exporter Lumeway, declarant Bayforth as customs agent (signatory), authority of Bayvarra and territory XB fit an export from Bayvarra.
- GTINs and GLN check digits correct (`check_ids.py`).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty`: a shipment stage that holds only the customs agent — refuted because the element is defined as "The Customs Agent who is associated with this Shipment Stage", and the agent is associated with the export stage.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:FreeOnBoardValueAmount` = `50688.00`: FOB equal to the goods value, without the pre-carriage to the port — refuted because the pre-carriage is the forwarder's charge to Lumeway, not part of the price to the buyer; the FOB value of the sale is the goods price.

## Outside this review
- Timeline: this declaration is issued on 2026-05-12 at 14:25, before the packing list (`10-PackingList.xml`, 15:59 the same day).
