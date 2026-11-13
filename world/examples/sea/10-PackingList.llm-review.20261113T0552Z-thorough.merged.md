# LLM review: 10-PackingList.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/10-PackingList.xml`, Git blob `aef1ab21426bbd03022aba54b057f406aeb46b61` (committed)
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

### sea/10#F1 · High · Shipment gross weight smaller than the gross weight of its own container
- XPath: `/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:TareWeightMeasure` = `3750`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The same document gives the shipment's container `TWLU4120872` a gross weight of 7,856.4 kg with a tare of 3,750 kg (recomputed: 4,106.4 + 3,750 = 7,856.4). The shipment that contains that container cannot weigh 4,106.4 kg; 4,106.4 kg is goods plus pallets (the goods items, 3,984 + 122.4 = 4,106.4). Two values of this document contradict each other under the definition (section 6: High). The semantic-conformance rule applies the UBL definition even where practice reads the shipment weight without the box. The same 4,106.4 kg is in 09, 11, 12, 14 and 15.
- Condition: the shipment's gross weight includes the container (7,856.4 kg), or the 4,106.4 kg is given only in an element whose definition excludes transport equipment (goods items).
- Options: (a) preferred: 7,856.4 kg as the shipment's gross weight (the box is known here, and the goods items already carry the weight without it); (b) drop the shipment's gross weight.
- Needs decision: no
- From: context (F1, High), logistics (F3, Medium)

### sea/10#F2 · High · Emission value is not factor × base
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies"; 0.82 × 1 EA = 0.82, not 96 kg CO2e (96 / 0.82 = 117.1 would be the base). The same triple is in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent (or the emission is absent from the packing list, F9).
- Options: (a) preferred: drop factor and base (and, see F9, the emission from the packing list); (b) a factor on a base whose product is 96.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F2)

### sea/10#F3 · Medium · A packing list that does not say how the goods are packed
- XPath: `/PackingList/cbc:Note` = `25 pallets.`
- XPath: `/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- Why: a Packing List is "A document describing how goods are packed". It gives two goods items without packages and a single `TransportHandlingUnit` that holds only the container; the 25 pallets exist only as a note and a count. Which pallet holds what, the pallets' type, marks, SSCCs, weights or dimensions are missing from the one document whose purpose they are. The bill of lading, issued two days later by the carrier, has exactly this information (24 bench pallets with 4 each and one frames pallet with 12, SSCCs `095206101230000018` … `095206101230000254`, marks `VELUMI SELANU / 001 of 025` …: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`, `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`), data a carrier takes from the shipper's packing list. (Logistics also saw a mismatch between the count 25 and the one transport handling unit listed; `TotalTransportHandlingUnitQuantity` is "The number of pieces of transport handling equipment (pallets, boxes, cases, etc.) in this shipment", so 25 pallets is the right count; the problem is that the pallets are not described.)
- Condition: the packing list describes the 25 pallets (type, marks or SSCC, contents per pallet and which goods item each holds), consistent with the bill of lading.
- Options: (a) preferred: the 25 pallets as packaged handling units of the container (or two with counts), with SSCC, marks, goods item and package count, as later on the bill of lading; (b) at least per goods item the number and kind of packages.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F3)

### sea/10#F4 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; a product footprint's system boundary is not a load factor. In a packing list the container's fullness would even be meaningful, which makes the misuse more confusing. 39 examples carry the code (`grep -rl --include='*.xml' 'CRADLETOGATE'`).
- Condition: `FullnessIndicationCode` is absent from product emissions or holds a fullness code.
- Options: (a) preferred: drop it (or the whole emission, F9); the missing boundary element is a point for the TC write-up.
- Needs decision: no
- From: broad (F3), context (F4)

### sea/10#F5 · Medium · Lifecycle stage MANUFACTURING for a cradle-to-gate footprint
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies". The description and `Description` ("Mining, steel making, casting, galvanising, sawing and the transport between them") cover raw material supply, transport and manufacturing; the code names only manufacturing. Code and text disagree. Not raised by any part; added by the merge, aligned with retail, road and rail.
- Condition: the code covers the stages the description names, or the emission is absent from the packing list (F9).
- Options: (a) preferred: drop the emission from the packing list; otherwise omit the code or give one entry per stage.
- Needs decision: no
- From: merge

### sea/10#F6 · Medium · Spare side frame classified as a general cast article, not as a part of a seat
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:NatureCode` = `XV`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[1]/cbc:ItemClassificationCode` = `42999`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the item is a "Spare side frame for the Serra bench", identifiable as made for one seat; the bench itself is classified 940179 (seats with metal frames). Parts of seats fall under HS 9401.99, and Section XV Note 1 excludes articles of Chapter 94 from the base-metal chapters, so heading 7325 ("other cast articles of iron or steel") does not apply (own knowledge of HS 2022). The section code `XV`, the national tariff code and the CPC code (42999, other fabricated metal products; parts of seats are CPC 3816x) follow the same wrong heading. 22 examples carry 732599 (`grep -rl --include='*.xml' '>732599<'`).
- Condition: HS, section, national tariff and CPC codes classify the side frame as a part of a seat, or the documents say why it is not one.
- Options: (a) preferred: HS 940199, section XX, matching tariff and CPC codes, in every example of the world.
- Needs decision: no
- From: broad (F4)

### sea/10#F7 · Medium · Language code in LocaleCode
- XPath: `/PackingList/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PackingList/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is the language itself and repeats `Language/ID`. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: each `LocaleCode` is absent or a locale code from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (preferred by broad and context).
- Needs decision: no
- From: broad (F5), parties (F1), context (F5)

### sea/10#F8 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/PackingList/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is an access point for vehicles, not a street, and a postal address has no use for it. 79 occurrences in 76 examples, 25 sea examples.
- Condition: no street element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address; where a truck needs it, in a location of the document that the truck uses.
- Needs decision: no
- From: broad (F6), parties (F2), context (F9, Low)

### sea/10#F9 · Low · Product sheet and customs values in a packing list
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:EmissionStandardReference` = `Greenhouse Gas Protocol Product Standard`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `768.00`
- Why: a packing list tells forwarder, carrier and receiver what is in which package and "Keep with the container's documents". Goods item 1 carries the catalogue's product sheet (keywords, warranty, sales conditions, load test, emissions, circularity profile, repairability), which nobody handling the container uses; goods item 2 shows the item without them. Both goods items carry a declared customs value (`DeclaredCustomsValueAmount`, "The total declared value for customs purposes of the goods item"), which is declared in the export declaration (`11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`). The context part refuted the customs values (packing lists accompany export declarations); that is a possible use, but this packing list does not state it, and it travels with the container. The values agree with the order (96 × 520.00, 12 × 64.00).
- Condition: goods items carry identification, description, quantities, weights, origin and classification, and the sales, product and customs data only if the packing list states a use for them.
- Options: (a) preferred: reduce goods item 1's item to the form of goods item 2 and drop the customs values; (b) keep the customs values and state that the packing list supports the export declaration.
- Needs decision: no
- From: broad (F7), money (F1), context (F6)

### sea/10#F10 · Low · Net volume and item dimensions do not describe the benches as shipped
- XPath: `/PackingList/cac:Shipment/cbc:NetVolumeMeasure` = `38.9`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[2]/cbc:Measure` = `620`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`
- Why: `NetVolumeMeasure` is "The total volume of the goods in this shipment, excluding packaging and transport equipment". One assembled bench of 1,800 × 620 × 780 mm has an envelope of 0.870 m³; 96 benches take 83.6 m³ (recomputed), more than twice the stated 38.9 m³ and more than the inside of a 40-foot general-purpose container (about 12.03 × 2.35 × 2.39 m = 67.6 m³, own knowledge). Four assembled benches stacked on one pallet would be 4 × 780 = 3.12 m high, above the 2.39 m inside height. The figures only work if the benches travel knocked down or nested, which no document says; the item dimensions describe the bench as installed ("Above the ground when anchored"), not as packed. The order response gives 41.5 m³ gross (`06-OrderResponse.xml`), consistent with 38.9 m³ net plus pallets, so the stated volume is consistent within the flow but not with the goods described.
- Condition: volume and dimensions describe the goods as shipped, and the documents say how the benches are packed if not assembled.
- Options: (a) preferred: state that the benches ship knocked down or nested (item or package description, packed dimensions) and keep the volume; (b) a volume that fits assembled benches, which then do not fit one 40-foot container.
- Needs decision: yes (how the benches are shipped)
- From: broad (F8)

### sea/10#F11 · Low · Reference to the purchase order with only an ID
- XPath: `/PackingList/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: a plain `DocumentReference` with only an ID; carrier and forwarder cannot tell that it is the buyer's purchase order (`05-Order.xml`).
- Condition: the reference states its document type.
- Options: (a) preferred: a `DocumentTypeCode` for an order (e.g. `220`).
- Needs decision: no
- From: logistics (F4), context (F7)

### sea/10#F12 · Low · Contacts whose function does not fit the role
- XPath: `/PackingList/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/PackingList/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: the consignor that packed the container is reached through Sales' customer service rather than its warehouse or shipping; the consignee's contact, who receives the goods, is called Purchasing, with the job title and department of a seller's customer service. Name, job title, department and role do not agree.
- Condition: each contact's name, job title and department agree with each other and fit the party's role, or the contact is absent.
- Options: (a) preferred: a warehouse/despatch contact for Lumeway and a goods-in contact for the consignee.
- Needs decision: no
- From: broad (F9), parties (F3, F5), context (F8)

### sea/10#F13 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: the English renderings carry `languageID="en-XB"`; the order Velumi sent tags them `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`). The tag follows the issuer's country across the flow, a convention no document records.
- Condition: Velumi's renderings carry the same `languageID` in every example, or the world records the issuer rule.
- Options: (a) preferred: `en-XL` everywhere; (b) record the issuer rule.
- Needs decision: yes (one rule for the world)
- From: broad (F10), parties (F4, address part)

### sea/10#F14 · Low · Velumi's legal form given once, in English, without its Lisavan form
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: in the order Velumi issued, the legal form is given in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); here only the English one, untagged.
- Condition: Velumi's legal form is given the same way in every example.
- Options: (a) preferred: both renderings, tagged, as in the order.
- Needs decision: no
- From: parties (F4, legal-form part; split by the merge)

### sea/10#F15 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/PackingList/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID": Bayforth Forwarding (Bayvarra) and Velumi Trading (Lisavu) share New Year's Day 1996; 271 occurrences in 181 examples. A default value, not a fact of the world.
- Condition: every `RegistrationDate` is that party's date in the world, or absent.
- Options: (a) preferred: own dates; (b) leave the element out.
- Needs decision: yes
- From: parties (F6)

### sea/10#F16 · Low · Party master data the packing list does nothing with
- XPath: `/PackingList/cac:ConsignorParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/PackingList/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/PackingList/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/PackingList/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/PackingList/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: a packing list has no tax, capital or customs content; the customs-trader numbers, share capital and sales-tax registrations look copied from the parties' master data (section 4.8). Not raised by any part; added by the merge for consistency with the earlier flows.
- Condition: the parties carry only what the packing list uses.
- Options: (a) preferred: drop them.
- Needs decision: no
- From: merge

### sea/10#F17 · Low · GTINs in the distributor's company prefix for the manufacturer's branded items
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- XPath: `/PackingList/cac:ConsignorParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- Why: the GTINs start with the GS1 company prefix of Lumeway's GLN (9520610), while the items are Valdara's brand (`BrandName` `Valdara`) made by Valdara Industries; under GS1 rules the brand owner allocates the GTIN. Check digits are valid (recomputed). Not raised by any part; added by the merge, aligned with retail.
- Condition: the GTINs are in the brand owner's prefix, or the story says why the distributor allocates them.
- Options: (a) preferred: Valdara's own prefix; (b) story (Lumeway's own-label numbering).
- Needs decision: yes
- From: merge

### sea/10#F18 · Low · World item number shaped like a valid GTIN-12
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: both 12-digit numbers carry a valid GS1 check digit (recomputed: 7 and 4), so they read as GTIN-12 (UPC) numbers in a real prefix range, against the rule that fictional values must not be mistaken for real ones. Not raised by any part; added by the merge, aligned with retail, road, rail and plastics.
- Condition: the world item number cannot be mistaken for a GTIN (other length, letters, or an invalid check digit by design), or is documented as a GS1-based scheme.
- Options: (a) preferred: a scheme format that is not a GTIN shape.
- Needs decision: yes
- From: merge

### sea/10#F19 · Low · A signature with an ID and the signatory only
- XPath: `/PackingList/cac:Signature/cbc:ID` = `LD-SIG-PL`
- XPath: `/PackingList/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: the signature has no method, date, attachment or signing person; it states nothing beyond the issuer, and its ID is formed from the document type. Not raised by any part; added by the merge, aligned with retail, air and utilities.
- Condition: a signature, where present, says how and when the document was signed.
- Options: (a) preferred: drop it; (b) complete it.
- Needs decision: yes (whether the world's documents are signed at all)
- From: merge

## Checked and consistent
- Weights (recomputed): goods items 3,984 + 122.4 = 4,106.4 kg; + tare 3,750 kg = 7,856.4 kg = the container's gross weight here and the verified gross mass on the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:VerifiedGrossMass/cbc:GrossMassMeasure` = `7856.4`). Tare 3,750 kg is typical for a 40-foot GP box (about 3,700–3,900 kg, own knowledge). Gross − net = 344.4 kg of packaging for 25 pallets = 13.8 kg per pallet incl. film, plausible. 3,984 / 96 = 41.5 kg gross per bench; 122.4 / 12 = 10.2 kg per side frame; about 38 kg net per bench, plausible for cast steel with hardwood slats.
- Quantities 96 and 12 and values 49,920.00 (96 × 520.00) and 768.00 (12 × 64.00) agree with the order, the export declaration and the invoice; 25 pallets = 24 × 4 benches + 1 castings pallet, as on the bill of lading.
- `check_ids.py`: ISO 6346 check digit of `TWLU4120872` valid; GTINs and GLN valid. The container is the bill of lading's.
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` are those of the forwarding instructions; the delivery instruction to Nalevi agrees with the order's delivery party and the bill of lading's on-carrier; "Castings pallet at the doors." agrees with the forwarding instructions.
- Parties: consignor, carrier, forwarder and consignee have the same identifiers as in 09 and 14; manufacturer Valdara Industries and property issuer Codana as in the catalogue (from parties).

## Considered and refuted
- `/PackingList/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`: distribution to the forwarder — refuted because a packing list has no addressee element, and the electronic copy to the forwarder who books and declares is a real use (from broad).
- `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID/@schemeID` = `ISO6346`: spelled without the space used in `listID="ISO 6346"` elsewhere — refuted because the repository keeps schemeIDs in their current style (`CLAUDE.md`) (from broad).
- `/PackingList/cac:Shipment/cbc:DeliveryInstructions`: Nalevi Warehousing named only in free text, not as a party — refuted: the delivery party is identified in the order and the bill of lading, and the instruction agrees with them (from parties).
- Floor space of 25 pallets in a 40-foot box: with pallets as long as a bench (about 1.85 m) one tier holds 18 (3 across × 6 along in 12.03 × 2.35 m), so 25 need two tiers; gross volume per pallet 41.5 / 25 ≈ 1.66 m³, on a footprint of about 1.85 × 0.77 m about 1.17 m high, two tiers 2.34 m under 2.39 m — refuted: the load fits, tightly, if the benches are nested on narrow pallets (from logistics). The merge notes that this rests on the stated volume, which F10 questions; it does not refute F10.
- Net weight per bench (about 38 kg) against the catalogue's material input of 56.5 kg (34 kg steel + 22.5 kg hardwood) — refuted: the input is consumed material including casting and sawing losses (from logistics, context).
- `/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount`: a customs value in a packing list — refuted because packing lists accompany export declarations (from context). Not followed: kept inside F9 as its weakest part, with this argument as option (b).

## Changed in the merge
- context/F1 (High), logistics/F3 (Medium) → F1: High kept, because the same document states the container's gross weight and tare (contradiction under the definition); logistics' Medium raised.
- broad/F7, money/F1, context/F6 → F9: grouped (product sheet and customs values are the same kind of copied data); context's refutation of the customs value carried as option (b).
- logistics/F2's count mismatch (25 vs one handling unit) → F3: not kept as a separate point; the definition of `TotalTransportHandlingUnitQuantity` counts pallets.
- context/F9 (Low) → F8: Medium, aligned with broad, parties and all earlier flows.
- parties/F4 → F13 and F14: split (tag rule Low/yes; legal form Low/no); broad/F10 (no) aligned to yes.
- LocaleCode: preferred option set to drop.
- F5, F16, F17, F18, F19 added by the merge (no part raised them), for consistency with the earlier flows' merges.

## Outside this review
- Timeline: the export declaration (`11-ExportCustomsDeclaration.xml`) is issued on 2026-05-12 at 14:25, before this packing list (15:59 the same day); whether the declarant could declare before the packing list existed is a cross-document timeline question (from broad).
