# LLM review: 11-ExportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/11-ExportCustomsDeclaration.xml`, Git blob `6df68444b58544480345d9e469661ab775d8d16a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 01cf804 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/11#F1 · High · An import declaration given as the previous version of this export declaration, which is version 1
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `IMPORT`
- XPath: `/ExportCustomsDeclaration/cbc:VersionID` = `1`
- Why: PreviousCustomsDeclaration is "a reference to a previous version of this customs
  declaration". The declaration is version 1, so it has no previous version, and the referenced
  declaration is another declaration altogether: the import of the goods into Bayvarra
  (`road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`). Its
  FunctionCode, "a code describing the function of this customs declaration" (the main declaration
  uses EDIFACT 1225, `9` original), holds a declaration type from another list.
- Condition: no PreviousCustomsDeclaration unless a previous version of this export declaration
  exists; the earlier import declaration, if referenced, is referenced as an additional/related
  document with a type that says it is the import declaration.
- Options: (a) preferred: reference LD-IM-26-0161 as an AdditionalDocumentReference typed as the
  previous customs procedure (the import that brought the goods into Bayvarra); (b) drop it.
- Needs decision: no

### sea/11#F2 · High · Emission value does not follow from its factor and base
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: 0.82 × a base of 1 each = 0.82, not 96 kg CO2e.
- Condition: factor × base = value, or factor and base absent.
- Options: (a) preferred: drop factor and base (see F7).
- Needs decision: no

### sea/11#F3 · Medium · Gross weight of the shipment without its transport equipment
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: In Shipment, GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment"; 4,106.4 kg is goods plus pallets (3,984 + 122.4, the goods items), the loaded
  container weighs 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure`
  = `7856.4`). For customs the goods' gross weight is the relevant one, and it is already on the goods
  items.
- Condition: the shipment's gross weight includes the container, or is absent.
- Options: (a) preferred: drop it (the goods items carry the weights customs needs); (b) 7,856.4 kg.
- Needs decision: no

### sea/11#F4 · Medium · An emission boundary code in FullnessIndicationCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: "A code signifying whether a piece of transport equipment is full, partially full, or empty";
  the value is a footprint boundary.
- Condition: no boundary code in FullnessIndicationCode.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/11#F5 · Medium · A language code in LocaleCode (three places)
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; each is the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/11#F6 · Low · A shipment stage that holds only the customs agent
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: ShipmentStage is "a stage in the transport movement of this shipment". This one has no
  mode, transport means, place or time; it exists only to carry the customs agent, who is also the
  declarant (signature `BF-SIG-EX-sea`) and the FreightForwarderParty. A reader learns nothing about
  any stage of the movement.
- Condition: a ShipmentStage present describes a stage of the movement (e.g. the main carriage from
  Lumeport with mode and vessel, which an export declaration typically states), with the customs
  agent attached where it acts, or the stage is absent.
- Options: (a) preferred: describe the main-carriage stage (sea, the vessel, departure from
  Lumeport) and keep the customs agent in it; (b) drop the stage.
- Needs decision: no

### sea/11#F7 · Low · Catalogue content and the product footprint in a customs declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:EmissionStandardReference` = `Greenhouse Gas Protocol Product Standard`
- Why: An export declaration declares goods to customs: description, classification, origin, value,
  weight. Keywords, warranty, the seller's sales conditions, the product footprint, item properties,
  dimensions and the circularity profile are catalogue content customs does nothing with. Goods
  item 2 shows the item without them.
- Condition: goods item 1's Item carries what customs uses, as goods item 2 does.
- Options: (a) preferred: reduce it to the form of goods item 2.
- Needs decision: no

### sea/11#F8 · Low · The customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: CustomsParty is "the Authority who processes this Customs Declaration"; a federal authority
  is neither registered in the commercial register nor subject to liquidation.
- Condition: no company-only data for the authority.
- Options: (a) preferred: drop its PartyLegalEntity, or describe it as a public body.
- Needs decision: no

### sea/11#F9 · Low · Reference to the purchase order with only an ID
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: "A reference to additional documents relevant or related to this customs declaration"; it
  does not say what the document is (an order, not the commercial invoice customs usually expects).
- Condition: the reference states its type.
- Options: (a) preferred: a DocumentTypeCode for an order.
- Needs decision: no

### sea/11#F10 · Low · Exporter's and consignee's contacts are sales customer service
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- Why: Customs reaches the exporter about the declared goods (export or shipping function) and the
  consignee about their receipt; both are a sales customer-service officer.
- Condition: contacts with functions that fit, or none.
- Options: (a) preferred: export/shipping and goods-inwards contacts.
- Needs decision: no

### sea/11#F11 · Low · A gate in AdditionalStreetName of the exporter's postal address
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- Declared values 49,920.00 + 768.00 = 50,688.00 = shipment DeclaredCustomsValue, statistics value
  and FOB value; equal to the order total.
- Goods items' weights and quantities equal those of 10-PackingList; consignment and shipment IDs
  agree with 09, 10, 12 and 14.
- Insurance value 59,155.80 equals the insured value in 09.
- Exporter Lumeway, consignee Velumi, declarant Bayforth (signature and customs agent), customs
  authority of Bayvarra and office of export/exit Lumeport fit an export by sea from Lumeport.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: the
  exit office repeated at declaration and consignment level — refuted: both levels exist in UBL and
  agree.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:FreightAllowanceCharge/cbc:Amount`:
  ocean freight in an export declaration with an FOB value — refuted for this lens: declaring the
  freight beyond the border for statistics is legitimate; the amounts are for the money lens.
