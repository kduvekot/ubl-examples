# LLM review: 10-PackingList.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/10-PackingList.xml`, Git blob `aef1ab21426bbd03022aba54b057f406aeb46b61` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/10#F1 · High · Emission value is not factor × base
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies"; 0.82 × 1 EA = 0.82, not 96 kg. 39 examples carry the factor 0.82 (`grep -l "<cbc:ValueFactorNumeric>0.82" world/examples/*/*.xml`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent (or, see F7, the emission is absent from the packing list).
- Options: (a) preferred: drop the emission from the packing list (F7); (b) factor 96 per 1 EA.
- Needs decision: no

### sea/10#F2 · Medium · A packing list that does not say how the goods are packed
- XPath: `/PackingList/cbc:Note` = `25 pallets.`
- XPath: `/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- Why: the document is "describing how goods are packed". It gives the goods items and the container, and the number of pallets in a note and a total, but no pallet: not their type, marks, contents, packages per pallet or weights. That 24 pallets hold four benches each and one pallet holds the twelve castings appears only in the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`, `…/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`) and the handling instruction "Castings pallet at the doors."
- Condition: the packing list describes the handling units (pallets) with their packaging type and contents (which goods item, how many packages), consistent with the bill of lading.
- Options: (a) preferred: 25 transport handling units (or one per pallet type with a quantity) inside the container, each with its packages and goods item reference; (b) none better seen.
- Needs decision: no

### sea/10#F3 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; a product LCA boundary is not a load factor. 39 examples carry this code in this element.
- Condition: `FullnessIndicationCode` is absent from product emissions or holds a fullness code.
- Options: (a) preferred: drop it (or the whole emission, F7).
- Needs decision: no

### sea/10#F4 · Medium · Spare side frame classified as a general cast article, not as a part of a seat
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:NatureCode` = `XV`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: a side frame made for the Serra bench is a part of a seat (HS 9401.99, Section XX); Section XV Note 1 excludes articles of Chapter 94 from heading 7325 (own knowledge of HS 2022). The HS section code follows the same wrong heading. 22 examples carry 732599.
- Condition: HS, section, national tariff and CPC codes classify the side frame as a part of a seat.
- Options: (a) preferred: HS 940199, section XX, matching tariff and CPC codes.
- Needs decision: no

### sea/10#F5 · Medium · Language code in LocaleCode
- XPath: `/PackingList/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PackingList/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/10#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/PackingList/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/10#F7 · Low · Product sheet and customs values in a packing list
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `768.00`
- Why: a packing list tells the forwarder, carrier and receiver what is in which package. The bench's goods item carries the catalogue's product sheet (emissions, circularity profile, load test, sales conditions, warranty) and both goods items a declared customs value; the packing list does nothing with them, and the customs value belongs to the declaration (`11-ExportCustomsDeclaration.xml`), where it is declared.
- Condition: goods items of the packing list carry identification, description, quantities, weights and classification, not the sales and product data, unless the packing list states a use.
- Options: (a) preferred: drop emissions, circularity, item properties, transaction conditions, warranty and customs values; (b) none better seen.
- Needs decision: no

### sea/10#F8 · Low · Net volume far below the benches' size
- XPath: `/PackingList/cac:Shipment/cbc:NetVolumeMeasure` = `38.9`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[2]/cbc:Measure` = `620`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`
- Why: `NetVolumeMeasure` is "The total volume of the goods in this shipment, excluding packaging". One bench of 1800 × 620 × 780 mm has an envelope of 0.87 m³; 96 benches take 83.6 m³, plus the castings, more than twice the stated 38.9 m³ and more than the inside of a 40-foot general-purpose container (about 12.0 × 2.35 × 2.39 m = 67 m³, own knowledge). Four assembled benches stacked on a pallet would also be 3.1 m high (4 × 780 mm), above the container's 2.39 m inside height. The figures only work if the benches travel knocked down or nested, which no document says.
- Condition: volume and dimensions describe the goods as shipped, and the documents say how the benches are packed if not assembled.
- Options: (a) state that the benches ship knocked down (item or package description, with packed dimensions) and keep the volume; (b) a volume that fits assembled benches (which then do not fit one container).
- Needs decision: yes (how the benches are shipped)

### sea/10#F9 · Low · Contacts whose function does not fit
- XPath: `/PackingList/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the consignor of a packing list is reached through Sales' customer service rather than its warehouse or shipping; the consignee's contact (who receives goods) is purchasing, with the job title of a seller's customer service.
- Condition: each contact's name, job title and department agree with each other and fit the party's role.
- Options: (a) preferred: a warehouse/shipping contact for Lumeway; a goods-in contact for the consignee.
- Needs decision: no

### sea/10#F10 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the order Velumi sent tags the same renderings `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); across the flow the tag follows the sender's country (16 × `en-XB`, 8 × `en-XL`).
- Condition: Velumi's address renderings carry the same `languageID` in every example.
- Options: (a) preferred: `en-XL` everywhere.
- Needs decision: no

## Checked and consistent
- Weights: goods items 3,984 + 122.4 = 4,106.4 kg = shipment gross weight; container gross 4,106.4 + tare 3,750 = 7,856.4 kg; 3,750 kg is a typical tare of a 40-foot GP container (own knowledge). Gross − net = 344.4 kg of packaging for 25 pallets = 13.8 kg per pallet incl. film: plausible. Per bench about 38 kg net ((3,984 − 24 × 13.8) / 96), plausible for cast steel with hardwood slats.
- Quantities 96 and 12 and customs values 49,920.00 and 768.00 agree with the order (`05-Order.xml`); 25 pallets = 24 × 4 benches + 1 castings pallet, as in the bill of lading.
- Container `TWLU4120872` has a valid ISO 6346 check digit (`check_ids.py`) and is the container of the bill of lading; GTINs and GLN check digits correct.
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` are the ones of the forwarding instructions (`09-ForwardingInstructions.xml`); delivery instruction to Nalevi agrees with the order's delivery party.

## Considered and refuted
- `/PackingList/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`: distribution to the forwarder — refuted because a packing list has no addressee element, and the electronic copy to the forwarder who books and declares is a real use.
- `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID/@schemeID` = `ISO6346`: spelled without the space used in `listID="ISO 6346"` elsewhere — refuted because the repository keeps schemeIDs in their current style (`CLAUDE.md`).

## Outside this review
- Timeline: the export declaration `11-ExportCustomsDeclaration.xml` is issued on 2026-05-12 at 14:25, before this packing list (15:59 the same day); whether the declarant could declare before the packing list existed is a question for the cross-document timeline.
