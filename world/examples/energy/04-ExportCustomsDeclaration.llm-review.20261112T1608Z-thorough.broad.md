# LLM review: 04-ExportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/04-ExportCustomsDeclaration.xml`, Git blob `d23054c9c05d2dbe62a877d4d23f4891f2983d71` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/04#F1 · High · Export of both buyers' gas declared to one consignee, and the import declaration gives the same shipment another quantity
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `2940000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyIdentification/cbc:ID` = `XU-R-105918`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- Why: the declared 39 200 MWh is the sum of Kelpstone's March sales to Montebrio Power (36 800 MWh, 06-Invoice.xml) and to Ferrano Energy (2 400 MWh, 07-Invoice.xml); the value 1 411 200 XBL × 100 = 141 120 000 XUF is the sum of both invoices. But the only `ConsigneeParty` ("The Party who receives the goods") is Montebrio Power. And the import declaration 05-ImportCustomsDeclaration.xml declares the same shipment KG-SH-26-0154 with 36 800 MWh and 2 760 000 kg. One shipment, two different contents, and 2 400 MWh exported to a consignee that does not receive them.
- Condition: the consignee(s) of the exported gas agree with the quantity declared, and the shipment ID KG-SH-26-0154 has the same goods in the export and the import declaration (or the two quantities belong to different shipments/consignments).
- Options: (a, preferred) split the export into two consignments (Montebrio Power 36 800 MWh, Ferrano Energy 2 400 MWh), each with its consignee, quantity, weight and value, and let the import declaration cover Montebrio's consignment (a second import declaration for Ferrano Energy would complete the story); (b) declare only Montebrio's 36 800 MWh here and add a separate export for Ferrano Energy's gas.
- Needs decision: yes

### energy/04#F2 · Medium · Natural gas in gaseous state classified as dry bulk cargo
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: `CargoTypeCode` is "A mutually agreed code signifying the type of cargo for purposes of commodity classification"; the code means "Dry bulk". The goods are natural gas in gaseous state (HS 271121) moved by pipeline, which is neither dry nor bulk cargo in the transport sense. Same value in 05-ImportCustomsDeclaration.xml.
- Condition: the cargo type, if present, fits gas carried by pipeline.
- Options: (a, preferred) omit `CargoTypeCode`: pipeline gas has no cargo type in the shipping sense; (b) use a code of the world list for gas/liquid bulk if one exists or is added.
- Needs decision: no

### energy/04#F3 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language itself, already in `Language/ID`. A locale would be e.g. English as used in Bayvarra (`en-XB`, the tag the examples use elsewhere). The same value occurs 362 times in 213 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'`).
- Condition: LocaleCode holds a locale (language and region), from a list of locales, or is absent.
- Options: (a, preferred) `en-XB` with a locale list (BCP 47 style); (b) omit LocaleCode.
- Needs decision: no

### energy/04#F4 · Medium · Province given in Region
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`, as Bayvarra's addresses in the same document use). World convention via the XU address format; 219 occurrences in 104 of 250 XML examples.
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/04#F5 · Low · Urvanian address renderings tagged en-XB, elsewhere en-XU
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- Why: the same address of Montebrio Power carries `languageID="en-XU"` in 03-Invoice.xml, 05-ImportCustomsDeclaration.xml and 09-RemittanceAdvice.xml, and `en-XB` here (and in 06, 07, 08, all sent from Bayvarra). The rendering is the Urvanian English form of the name; tagging it as English of Bayvarra describes the sender, not the text.
- Condition: the renderings of one address carry the same language tag in every example.
- Options: (a, preferred) `en-XU`, the variety the name belongs to; (b) document that the tag follows the sender's locale.
- Needs decision: no

### energy/04#F6 · Low · Customs authority described as a company
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:ID` = `XB:FBR`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`
- Why: the Customs and Border Service of Bayvarra is a public authority (ISIC 8411). A liquidation status and a registration in the federal business register with type "Commercial register" describe a company. The contact "Public service officer" in "Public services" is generic for the office that handles a pipeline export. Public bodies carry a liquidation status in 90 parties of 75 XML examples (count of parties with IndustryClassificationCode 8411 and CompanyLiquidationStatusCode, over `*/*.xml` with lxml).
- Condition: the authority's legal-entity data fit a public body (no liquidation status; a register of public bodies, if any); its contact is the office that handles the declaration.
- Options: (a, preferred) drop the liquidation status and commercial-register type for public bodies; (b) keep, if the world registers authorities in the business register, but then without liquidation status.
- Needs decision: no

### energy/04#F7 · Low · Field coordinates about 6 km from the plant, text says 4 km
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `16.20`
- Why: plant at 39°52.80′S 15°18.00′W, origin at 39°49.80′S 15°16.20′W: Δlat 3.0′ = 5.56 km, Δlon 1.8′ × cos 39.85° = 2.56 km, distance ≈ 6.1 km, against "four kilometres out". The origin is a region (a map tile), so its coordinate may be the tile's centre, not the platform; hence Low.
- Condition: the origin coordinate and the description agree, or the origin is explicitly the tile and not the platform.
- Options: (a) bring the coordinates of the field nearer (≈ 4 km) or the text to "six kilometres"; (b) leave as tile centre.
- Needs decision: no

### energy/04#F8 · Low · Declaration does not say which period of pipeline flow it covers, nor which invoices
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: a pipeline export is declared for a period of flow; here the period (March 2026) can only be guessed from the journey ID, and the customs value is not linked to the commercial invoices 06/07 it is the sum of. Both matter for checking the declaration against the metered quantity and the invoices.
- Condition: the declaration states the period of flow and, where the value derives from them, the invoices.
- Options: (a, preferred) a shipment-stage period or transit period and `AdditionalDocumentReference`s to KG-INV-26-0157 / KG-INV-26-0158 if the element is available in this document; (b) a note.
- Needs decision: no

## Checked and consistent
- Value: 39 200 MWh × 36 XBL = 1 411 200 XBL; at 100 XUF per XBL (06-Invoice.xml exchange rate) = 141 120 000 XUF = 132 480 000 (06) + 8 640 000 (07).
- Weight: 2 940 000 kg / 39 200 MWh = 75 kg/MWh = 13.3 kWh/kg, close to the lower heating value of natural gas (methane about 13.9 kWh/kg, own knowledge), plausible for gas with some inerts; Shipment and GoodsItem gross weight agree.
- HS 271121 "Natural gas, in gaseous state", HS section V, CPC 12020, transport mode 7 and means type 71 (pipeline) agree with each other.
- Exporter data agree with 05, 06, 07, 08, 09; Kelpstone as carrier of its own pipeline is plausible.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID`: suspected a second document number besides `/ExportCustomsDeclaration/cbc:ID` — refuted: the definition is "An identifier associated with customs related procedures", a declaration reference distinct from the message ID is legitimate.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name`: suspected the exporter cannot be the carrier — refuted: a producer owning the export pipeline is the carrier of the gas through it.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID`: suspected a GTIN with a real GS1 prefix — refuted: its scheme is the world's own item scheme (`urn:ubl-examples:world:item`), not GS1.

