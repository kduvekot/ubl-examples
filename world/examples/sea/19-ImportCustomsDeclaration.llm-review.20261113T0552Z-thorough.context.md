# LLM review: 19-ImportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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

### sea/19#F1 · Medium · Urvania's national tariff used in an import declaration lodged in Lisavu
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- XPath: `/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XL`
- Why: `CommodityCode` is "The harmonized international commodity code for cross border and regulatory (customs and trade statistics) purposes". In an import declaration the national subdivision that matters is the tariff of the importing country, which determines the duty; the declaration applies in Lisavu (`JurisdictionRegionAddress` XL) and is lodged with the Island Customs Service. Both goods items carry, as their 8-digit code, an entry of the list `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, Urvania's national tariff (Urvania is the country of origin and manufacture, but is neither exporting nor importing country here). The code is valid in its list, but it is not the one the importing customs applies. The same list is used 61 times in the examples (counted with `grep -rho --include='*.xml' 'listID="urn:ubl-examples:world:X[A-Z]:codelist:CustomsTariffCode"'`); no Lisavan or Trade Accord tariff list occurs at all.
- Condition: The national commodity code in this import declaration is from the tariff the Island Customs Service applies (a Lisavan or common Trade Accord tariff), or the declaration carries only the HS code.
- Options: (a) preferred: a Lisavan (or common Accord) tariff list with the corresponding codes; (b) if the world decides the Trade Accord uses one common tariff, give that list an Accord-level listID instead of an Urvanian one; (c) keep only the 6-digit HS code.
- Needs decision: yes

### sea/19#F2 · Low · Sales and product-passport data copied into the customs declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: The goods item's item carries the complete catalogue description of the bench: search keywords "assigned by the seller", warranty, the seller's sales conditions ("Sold to trade customers only"), the load test method, colour options with importance codes, emissions, circularity profile (maintenance, repairability, packaging waste) and product documentation. An import declaration needs what identifies and classifies the goods for duty and statistics (description, codes, origin, value, weight). None of these elements is used by customs or by the broker who lodges it; they are master data copied from the catalogue. The second goods item, the side frame, is declared without them, which shows the declaration does not need them.
- Condition: The declared items carry only what customs uses to identify, classify, value and check the goods (and any data a stated customs rule asks for).
- Options: (a) preferred: reduce the bench's item to identification, classification, origin and the properties relevant to classification; (b) if a product passport is part of the Lisavan import rules in the world, keep the circularity data and state that rule, and drop the sales data.
- Needs decision: no

### sea/19#F3 · Low · A validity period for an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:StartDate` = `2026-05-19`
- XPath: `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `30`
- Why: `ValidityPeriod` is "A period, assigned by the issuer, during which the information in the declaration is valid". A declaration for release for free circulation (`SubTypeCode` FREECIRC) is accepted or not and the goods are then released; it does not lapse after 30 days. Nothing in the flow uses the period. The value has no business reason here (rule: no fillers).
- Condition: A validity period is present only where the declaration's procedure gives it a validity (e.g. a pre-lodged declaration that lapses if the goods are not presented).
- Options: (a) preferred: remove it; (b) make the declaration a pre-lodged one with a stated reason for the period, which changes the story.
- Needs decision: no

### sea/19#F4 · Low · The customs broker in four roles, one of them in a shipment stage that has nothing else
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: Tevaro is the importer's agent, holder of the power of attorney, notifier ("The Party who is responsible for contact on master level"), customs agent of a shipment stage and signatory. The shipment stage contains nothing but the customs agent: no mode, means, place or time, so it is not a stage of the transport movement ("A stage in the transport movement of this shipment") but a container for a role already stated in `ImporterParty/AgentParty`. The repetition adds no information and the stage misuses its aggregate.
- Condition: Each role of the broker appears where the document needs it, and a shipment stage is present only to describe a stage of the transport.
- Options: (a) preferred: keep the agent of the importer (with the power of attorney) and the signatory; drop the empty stage; keep the notifier only if it means something different here; (b) give the stage its transport content (the sea leg into Selanu) if the customs agent must be stated per stage.
- Needs decision: no

### sea/19#F5 · Low · The warehouse that receives the goods witnesses the importer's power of attorney
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:WitnessParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: `WitnessParty` is "A Witness to this Power of Attorney". The power of attorney was issued on 2026-01-05 and notarised by the Selanu Chamber of Commerce. Nalevi Warehousing is the delivery party of this shipment (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`); nothing explains why a logistics provider would have witnessed a power of attorney between Velumi and its broker months before this shipment. A witness of a power of attorney is normally a natural person present at the signing.
- Condition: The witness is a party the world gives a reason to witness the signing (typically a person), or no witness is given.
- Options: (a) preferred: remove the witness, as the notary already attests the power; (b) a named person (e.g. an employee of the notary) as witness.
- Needs decision: yes

## Checked and consistent
- Quantities agree with the flow: 96 benches and 12 side frames, as ordered (`05-Order.xml`), despatched (`20-DespatchAdvice.xml`) and invoiced (`22-Invoice.xml`).
- The declaration is issued on 2026-05-19, after the discharge on 2026-05-18 (`17-TransportationStatus.xml`), for release for free circulation, under an outright purchase, which agrees with the sale in the flow.
- The note "Duties paid by the importer's account at customs" agrees with the power of attorney's scope (lodging declarations and paying duties on behalf of Velumi Trading).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: an exit office in an import declaration suspected to be the wrong office — refuted because it is the only customs office element the UBL 2.5 Import Customs Declaration has ("Customs exit office of the goods being declared"), and the office at Lumeport where the goods left Bayvarra is a true and usable reference for the importing customs.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason`: a freight charge in an import declaration suspected as data the document does nothing with — refuted because freight to the place of entry is part of the customs value (CIF-based valuation, own knowledge), so customs needs it.
