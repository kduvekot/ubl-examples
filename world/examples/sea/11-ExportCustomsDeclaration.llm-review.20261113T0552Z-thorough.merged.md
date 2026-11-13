# LLM review: 11-ExportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/11-ExportCustomsDeclaration.xml`, Git blob `6df68444b58544480345d9e469661ab775d8d16a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:FunctionCode` = `9`
- XPath: `/ExportCustomsDeclaration/cbc:VersionID` = `1`
- Why: `PreviousCustomsDeclaration` is "A reference to a previous version of this customs declaration". This declaration is version 1 and an original (`FunctionCode` 9, UN/EDIFACT 1225), so it has no previous version; the referenced document is another declaration altogether, Lumeway's import of the same 96 benches and 12 castings into Bayvarra in March (`road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`, issued 2026-03-24). The reference resolves to a document of the wrong kind and contradicts the version number (section 6: High). In addition, the previous declaration's `FunctionCode` ("A code describing the function of this customs declaration") holds `IMPORT` from the world's declaration-type list, a type, not a function, while the same element of the declaration itself uses UN/EDIFACT 1225. The link to the import (a "previous document" in customs terms, for the re-export of imported stock) is a real business fact; this element does not express it.
- Condition: no `PreviousCustomsDeclaration` unless a previous version of this export declaration exists (with a function code from the function list); the import declaration, if referenced, is referenced as an additional document typed as the import declaration / previous procedure.
- Options: (a) preferred: reference `LD-IM-26-0161` as `AdditionalDocumentReference` with a type that says it is the import declaration of the goods; (b) drop the reference.
- Needs decision: no
- From: context (F1, High), broad (F2, Medium), logistics (F2, Medium)

### sea/11#F2 · High · Emission value is not factor × base
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" on the base `ValueBaseMeasure`; 0.82 × 1 EA = 0.82, not 96 kg CO2e. 39 examples carry the triple (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`).
- Condition: factor × base = value, or factor and base are absent (or the emission is absent from the declaration, F12).
- Options: (a) preferred: drop factor and base, and the emission from the declaration (F12); (b) a factor on a base whose product is 96.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F2)

### sea/11#F3 · Medium · Shipment-level customs and statistical values add up goods of two tariff headings
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredCustomsValueAmount` = `50688.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredStatisticsValueAmount` = `50688.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `940179`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- Why: under Shipment, `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of those goods in this shipment that are subject to the same customs procedure and have the same tariff/statistical heading, country information, and duty regime", and `DeclaredStatisticsValueAmount` "The value, declared for statistical purposes, of those goods in this shipment that have the same statistical heading". 50,688.00 = 49,920.00 + 768.00 (recomputed) is the sum over two goods items under different headings (and stays so after the reclassification in F5: 9401.79 and 9401.99). The per-heading values are already on the goods items (`/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`, `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `768.00`). The Consignment-level element in the bill of lading has a definition that allows a total; the Shipment-level one does not.
- Condition: no Shipment-level customs or statistical value covers goods of more than one tariff/statistical heading.
- Options: (a) preferred: drop the two Shipment-level values and keep the per-goods-item values (with per-item statistical values if the export statistics need them); (b) a declaration total in an element whose definition allows one.
- Needs decision: no
- From: money (F1)

### sea/11#F4 · Medium · Export declaration without packages, container or means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:Quantity` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:Quantity` = `12`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: an export declaration identifies the goods so that the exit office can match them when they leave. The goods items have quantities and weights but no number or kind of packages and no marks; the shipment has no transport handling unit or container (`TWLU4120872` in the packing list and bill of lading); the only shipment stage names the customs agent but neither mode of transport nor vessel or voyage. These are core data of an export declaration (own knowledge of the WCO data model: packages, container identifier, mode and means of transport at the border). The 25 pallets and the container are known on the day (packing list `10-PackingList.xml` the same day; container `TWLU4120872`).
- Condition: the declaration states per goods item the number and kind of packages, the container in which the goods leave, and the mode of transport at the border (with vessel and voyage if known at lodging).
- Options: (a) preferred: packages per goods item (24 pallets / 1 pallet), the container as transport handling unit, and mode and planned vessel on the shipment stage; (b) at least the packages and the container.
- Needs decision: no
- From: logistics (F3)

### sea/11#F5 · Medium · Spare side frame declared as a general cast article, not as a part of a seat
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:NatureCode` = `XV`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:ItemClassificationCode` = `42999`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: a side frame made for the Serra bench is a part of a seat (HS 9401.99, Section XX); Section XV Note 1 excludes articles of Chapter 94 from the base-metal chapters, so heading 7325 does not apply (own knowledge of HS 2022). In a customs declaration the classification is what is declared. Section, national tariff and CPC codes follow the same heading. 22 examples carry 732599.
- Condition: HS, section, national tariff and CPC codes classify the side frame as a part of a seat.
- Options: (a) preferred: HS 940199, section XX, matching tariff and CPC codes.
- Needs decision: no
- From: broad (F4)

### sea/11#F6 · Medium · Shipment gross weight without the transport equipment its definition includes
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 4,106.4 kg is goods plus pallets (goods items 3,984 + 122.4); with the container the shipment weighs 4,106.4 + 3,750 = 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`). Not High: this document names no container (see F4).
- Condition: the shipment's gross weight includes the transport equipment, or is absent (customs uses the goods items' gross weights).
- Options: (a) preferred: drop it; (b) 7,856.4 kg.
- Needs decision: no
- From: logistics (F4), context (F3)

### sea/11#F7 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: "A code signifying whether a piece of transport equipment is full, partially full, or empty"; a product footprint boundary is not a load factor. 39 examples.
- Condition: `FullnessIndicationCode` is absent from product emissions or holds a fullness code.
- Options: (a) preferred: drop it (or the whole emission, F12); TC write-up.
- Needs decision: no
- From: broad (F3), context (F4)

### sea/11#F8 · Medium · Lifecycle stage MANUFACTURING for a cradle-to-gate footprint
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- Why: "A code indicating the lifecycle stage to which this emission applies"; the description next to it (`From the ore at the mine to the bench leaving the factory gate.`) covers raw material supply, transport and manufacturing. Not raised by any part; added by the merge, aligned with retail, road and rail.
- Condition: the code covers the stages described, or the emission is absent from the declaration.
- Options: (a) preferred: drop the emission (F12); otherwise omit the code or one entry per stage.
- Needs decision: no
- From: merge

### sea/11#F9 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) repeats the language. 362 occurrences in 213 examples.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` (preferred by broad and context).
- Needs decision: no
- From: broad (F5), parties (F1), context (F5)

### sea/11#F10 · Medium · A gate in AdditionalStreetName of the exporter's postal address
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address"; a gate is not a street, and the exporter's postal address has no use for it. 79 occurrences in 76 examples.
- Condition: no street element of the postal address holds a gate.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (F6), parties (F2), context (F11, Low)

### sea/11#F11 · Medium · The Customs and Border Service of Bayvarra described as a company in a commercial register, with a liquidation status
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- Why: the national customs authority (ISIC `8411`, public administration) is placed in the federal business register as a commercial registration and given a liquidation status ("A code signifying the party's legal status"). A public body is not entered in a commercial register and cannot go into liquidation; the checklist names this case. The values carry a meaning that does not fit the party (Medium, as in all earlier flows).
- Condition: the authority's legal entity carries no commercial registration or liquidation status (a public-body register, only the registration name, or no legal entity).
- Options: (a) preferred: keep `RegistrationName`, drop the liquidation status and the commercial registration scheme; (b) drop `PartyLegalEntity`.
- Needs decision: no
- From: parties (F3, Medium), broad (F7, Low), context (F8, Low)

### sea/11#F12 · Low · Product sheet in an export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:EmissionStandardReference` = `Greenhouse Gas Protocol Product Standard`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`
- Why: customs needs the goods described, classified, valued, weighed and their origin. Goods item 1 also carries the catalogue's product data (keywords, warranty, sales conditions, emissions, circularity profile, item properties, dimensions, specification and repair documents); the declaration does nothing with them. Goods item 2 shows the item without them.
- Condition: goods item 1 carries what the export declaration uses, as goods item 2 does, unless the declaration states a use for more.
- Options: (a) preferred: reduce it to description, identifiers, origin and classification.
- Needs decision: no
- From: broad (F8), context (F7)

### sea/11#F13 · Low · Ocean freight and insured value in an export declaration valued free on board
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:FreightAllowanceCharge/cbc:Amount` = `2950.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:InsuranceValueAmount` = `59155.80`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:FreeOnBoardValueAmount` = `50688.00`
- Why: customs, statistical and FOB values are all 50,688.00, the value on board at Lumeport. The ocean freight to Selanu (`FreightAllowanceCharge`, "A cost incurred by the shipper in moving goods … under the terms of the contract of carriage") and the insured value for the voyage enter none of the declared values; Bayvarra's customs does nothing with them here. They are used at import in Lisavu (`19-ImportCustomsDeclaration.xml`). The context part refuted the freight (declaring freight beyond the border for statistics is legitimate); that use would show in a CIF-based statistical value, which this declaration does not have.
- Condition: the export declaration carries the post-export freight and the insured value only if Bayvarra's export procedure uses them, and then the declared values reflect that use.
- Options: (a) preferred: remove both; (b) a CIF-based statistical value (53,778.00) with freight and insurance as its components.
- Needs decision: no
- From: money (F2)

### sea/11#F14 · Low · A shipment stage that holds only the customs agent
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `ShipmentStage` is "A stage in the transport movement of this shipment". This one has no mode, means, place or time; it exists only to carry the customs agent, who is also the declarant and signatory. The broad part refuted it because `CustomsAgentParty` is "The Customs Agent who is associated with this Shipment Stage"; the agent's place is legitimate, but a stage that describes no movement says nothing about any stage. Resolved together with F4 (mode and vessel on the stage).
- Condition: a shipment stage present describes a stage of the movement, with the customs agent attached where it acts, or the agent is given elsewhere.
- Options: (a) preferred: describe the main-carriage stage (sea, vessel, departure from Lumeport) and keep the agent in it (F4); (b) drop the stage.
- Needs decision: no
- From: context (F6)

### sea/11#F15 · Low · Customs offices named but not identified
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExitLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExportLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`
- Why: customs offices are identified by an office code; the three office locations have a name only, and the port has the UN/LOCODE `XBLMP` used in the flow. A declaration routed to an office needs its identifier.
- Condition: the office locations carry an identifier (an office code, or at least the port's LOCODE).
- Options: (a) preferred: an office ID in Bayvarra's customs office scheme, if the world has one; (b) the LOCODE `XBLMP`.
- Needs decision: no
- From: broad (F9), logistics (F5)

### sea/11#F16 · Low · The customs authority given with its inland border office, while the declaration is made and the goods exit at the port
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName` = `Border Crossing Road`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CityName` = `Marrowdale`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExportLocation/cbc:Name` = `Customs office, port of Lumeport`
- Why: `CustomsParty` is "The Authority who processes this Customs Declaration". The declaration is made and the goods exit at the port office of Lumeport, but the authority is given with the address and contact of a border office on Border Crossing Road in Marrowdale, the exporter's inland town. The contact a declarant or carrier would reach for these goods is the port office.
- Condition: the authority's address and contact are those of the office that processes this declaration, or of the authority's head office, consistent with the office locations.
- Options: (a) preferred: the port office's contact and address in Lumeport; (b) the head office.
- Needs decision: no
- From: parties (F5)

### sea/11#F17 · Low · Supporting document: the buyer's order by ID only
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: `AdditionalDocumentReference` is "A reference to additional documents relevant or related to this customs declaration"; the only one is the buyer's order number, without a type saying it is an order. An export declaration normally rests on the commercial (or pro-forma) invoice and the packing list; the order is the weakest evidence of the sale and its value.
- Condition: the supporting documents are referenced with their document type, and the declaration references the documents it rests on.
- Options: (a) preferred: a type code on the order reference, and a reference to the packing list (`LD-PL-26-0134`, though issued later that day, see "Outside this review").
- Needs decision: no
- From: broad (F10), context (F9)

### sea/11#F18 · Low · Contacts whose function does not fit the role
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: customs reaches the exporter about the declared goods (export or shipping function), but the contact is Sales' customer service; the consignee's contact is called Purchasing with the job title and department of a seller's customer service. Name, title, department and role do not agree.
- Condition: contacts with agreeing name, title and department that fit the role, or none.
- Options: (a) preferred: an export/shipping contact for Lumeway and a goods-in or import contact for the consignee.
- Needs decision: no
- From: broad (F11), parties (F4, F7), context (F10)

### sea/11#F19 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: tagged `en-XB` here (issued by Bayforth), `en-XL` in the order Velumi sent (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`); the tag follows the issuer across the flow, a convention no document records.
- Condition: the same `languageID` in every example, or the issuer rule recorded.
- Options: (a) preferred: `en-XL` everywhere; (b) record the rule.
- Needs decision: yes (one rule for the world)
- From: broad (F12), parties (F6, address part)

### sea/11#F20 · Low · Velumi's legal form given once, in English, without its Lisavan form
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: the order gives it in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); here only the English, untagged.
- Condition: the same renderings in every example.
- Options: (a) preferred: both renderings, tagged.
- Needs decision: no
- From: parties (F6, legal-form part; split by the merge)

### sea/11#F21 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Bayforth Forwarding (Bayvarra) and Velumi Trading (Lisavu) share New Year's Day 1996; 271 occurrences in 181 examples; a default value, not a fact of the world.
- Condition: own dates, or absent.
- Options: (a) preferred: own dates; (b) leave the element out.
- Needs decision: yes
- From: parties (F8)

### sea/11#F22 · Low · GTINs in the distributor's company prefix for the manufacturer's branded items
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: the GTINs are in the prefix of Lumeway's GLN (9520610900008), while the items are Valdara's brand; the brand owner allocates GTINs (GS1 rules). Not raised by any part; added by the merge, aligned with retail.
- Condition: the GTINs are in the brand owner's prefix, or the story explains the distributor's numbering.
- Options: (a) preferred: Valdara's own prefix.
- Needs decision: yes
- From: merge

### sea/11#F23 · Low · World item number shaped like a valid GTIN-12
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: both carry a valid GS1 check digit (recomputed), so they read as real GTIN-12 numbers. Not raised by any part; added by the merge, aligned with retail, road, rail and plastics.
- Condition: the world item number cannot be mistaken for a GTIN, or is documented as GS1-based.
- Options: (a) preferred: a format that is not a GTIN shape.
- Needs decision: yes
- From: merge

### sea/11#F24 · Low · Party data the declaration does nothing with
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: the exporter's share capital and the customs agent's state sales-tax registration play no part in an export declaration; they look copied from master data (section 4.8). The exporter's tax registration (`UL-1230822`) and the customs-trader numbers are left out of this finding: an export declaration may use the exporter's tax and trader identifiers. Not raised by any part; added by the merge, as in the earlier flows.
- Condition: the parties carry only what the declaration uses.
- Options: (a) preferred: drop them.
- Needs decision: no
- From: merge

### sea/11#F25 · Low · A signature with an ID and the signatory only, its ID carrying the flow name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `BF-SIG-EX-sea`
- XPath: `/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: the signature has no method, date, attachment or signing person, and its ID ends in `sea`, the name of the example flow, not a number of Bayforth's (noticed by context in F6). Not raised as a finding by any part; added by the merge, aligned with retail/air/utilities (empty signature) and cotton/road (flow name in the ID).
- Condition: a signature, where present, says how and when the document was signed, and its ID is the signer's own reference.
- Options: (a) preferred: drop it; (b) complete it with an ID of Bayforth's numbering.
- Needs decision: yes (whether the world's documents are signed at all)
- From: merge

## Checked and consistent
- Values (recomputed): goods items 96 × 520.00 = 49,920.00 and 12 × 64.00 = 768.00; sum 50,688.00 = FOB value = the invoice's goods total (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`); insured value 59,155.80 = 110 % of the CIF value 53,778.00; freight 2,950.00 = ocean freight 2,700.00 + bunker surcharge 250.00 on the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `2700.00`, `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:ExtraAllowanceCharge/cbc:Amount` = `250.00`) and the invoice's freight charge.
- Weights 3,984 + 122.4 = 4,106.4 kg, quantities 96 and 12, HS 940179 for the bench and origin Urvania agree with the packing list; shipment and consignment IDs agree with 09, 10, 12 and 14.
- The previous import declaration `LD-IM-26-0161` exists (`road/10-ImportCustomsDeclaration.xml`, 2026-03-24) and covers the same goods, so the re-export of imported stock is traceable (only the element is wrong, F1).
- Declarant Bayforth (customs agent and signatory) on behalf of exporter Lumeway with its customs trader number `XB-TR-410274`, as instructed in `09-ForwardingInstructions.xml` ("declare the export"); Bayforth described identically to 09, 10, 12 and 14. Lodged 2026-05-12 14:25, before the sailing on 2026-05-14: "Declared electronically before the goods leave." holds. Bayforth bills the lodging in `18-Invoice.xml`.
- GTIN and GLN check digits valid (`check_ids.py`).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:FreeOnBoardValueAmount` = `50688.00`: FOB equal to the goods value, without the pre-carriage to the port (310.00 in `14-BillOfLading.xml`) — refuted because under CIF the seller bears that cost and does not bill it to the buyer; the goods price is the price at which the seller delivers on board (from broad, money).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:DeclaredCustomsValueAmount` = `50688.00` against `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`: two customs values for the same consignment — refuted for this example: export (FOB) and import (CIF) value the same goods differently; the difference is freight and insurance (2,950.00 + 140.00) (from money). Whether the bill of lading's value is right is a finding of `14-BillOfLading.xml`.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: the exit office stated at declaration and consignment level — refuted: both levels exist in UBL and agree (from context; broad had folded the duplication into its F9, the merge kept only the identification part in F15).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:FreightAllowanceCharge/cbc:Amount`: ocean freight in an export declaration with an FOB value — refuted by context for its lens (freight beyond the border may be declared for statistics). Not followed: money's finding F13 kept, with this argument in it.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty`: a stage that holds only the customs agent — refuted by broad (the agent is associated with the export stage). Not followed: kept as F14, with the argument.

## Changed in the merge
- context/F1 (High), broad/F2 and logistics/F2 (Medium) → F1: High, because the reference contradicts the declaration's own version number and resolves to a document of another kind; the function-code misuse folded in.
- parties/F3 (Medium), broad/F7 and context/F8 (Low) → F11: Medium, aligned with all earlier flows (customs authority as a company).
- context/F11 (Low) → F10: Medium, aligned.
- broad/F9 and logistics/F5 → F15: the "exit office twice" part dropped, following context's refutation (carried under Considered and refuted).
- parties/F6 → F19 and F20: split (tag rule Low/yes; legal form Low/no); broad/F12 (no) aligned to yes.
- LocaleCode: preferred option set to drop.
- F8, F22, F23, F24, F25 added by the merge (no part raised them), for consistency with the earlier flows' merges.

## Outside this review
- Timeline: this declaration is issued on 2026-05-12 at 14:25, before the packing list (`10-PackingList.xml`, 15:59 the same day) (from broad).
