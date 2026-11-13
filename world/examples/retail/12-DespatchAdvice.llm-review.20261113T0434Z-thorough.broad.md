# LLM review: 12-DespatchAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/12-DespatchAdvice.xml`, Git blob `d93dffcfbe79b292ad495776e25413987734c7cc` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/12#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/12#F2 · Medium · The first pallet contains a pallet with one item, while it holds four benches
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:Quantity` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:ID` = `095206100000122217`
- Why: `ActualPackage` is "A package contained in this transport handling unit", and its `Quantity` "The quantity of items contained in this package". The handling unit is itself a pallet (`PX`, SSCC `095206102170000014`) with four packages (four benches, `HandlingUnitDespatchLine` 4 each). The only package listed inside it is again a pallet, identified by a GRAI (the returnable pallet itself) and containing one item. Read as UBL defines it, the pallet contains one other pallet with one bench, which contradicts the four packages and four benches. The returnable pallet is the handling unit's own equipment, not a package in it. Pallets 2 to 6 carry no such package, so the six identical pallets are described differently.
- Condition: the packages listed in a handling unit are the packages it contains, consistent with `TotalPackageQuantity` and the despatched quantity; the returnable pallet, if identified, is identified as the handling unit's own equipment, the same way on all six pallets.
- Options: (a, preferred) drop the `ActualPackage` and, if the GRAI matters (returnable pallet), carry it on the handling unit in a way that identifies the pallet itself (e.g. as `TransportEquipment` or a second identifier of the handling unit), on every pallet; (b) list the four benches as the actual packages.
- Needs decision: no

### retail/12#F3 · Medium · Language codes in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/12#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/12#F5 · Low · Shipping document reference points to the transport request, not to the consignment note
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ShipmentDocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- XPath: `13-Waybill.xml:/Waybill/cbc:ID` = `BF-WB-26-0231`
- Why: `ShipmentDocumentReference` is "A reference to a shipping document associated with this transport handling unit". The referenced document is 11-TransportExecutionPlanRequest, Lumeway's booking request to the forwarder, which Brightmarket never receives. The shipping document that travels with the goods, and that the note asks Brightmarket to use, is the consignment note 13-Waybill (`BF-WB-26-0231`). The reference is also given on one of six pallets only.
- Condition: the shipping document reference, if present, refers to the document that accompanies the goods, at shipment level or on every handling unit it applies to.
- Options: (a, preferred) reference `BF-WB-26-0231` (on the shipment or consignment, which covers all six pallets); (b) drop it and let the note name the consignment note's number.
- Needs decision: no

### retail/12#F6 · Low · Truck and goods item attached to one of six pallets
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `BV LP 2203`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:GoodsItem/cbc:ID` = `1`
- Why: the truck carries all six pallets, but the transport means is given on the first handling unit only, as is a goods item that consists of an ID and nothing else, while all six pallets state `TotalGoodsItemQuantity` 1. The reader cannot tell whether pallets 2 to 6 travel on the same truck or what their goods item is.
- Condition: data that applies to the whole shipment is given once for the shipment (or on every handling unit), and a goods item is described or absent.
- Options: (a, preferred) move the transport means to the shipment's delivery or the consignment and drop the empty goods item; (b) repeat both on every pallet, with a description in the goods item.
- Needs decision: no

### retail/12#F7 · Low · Handling unit despatch lines reuse the despatch line's ID with another quantity
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:DeliveredQuantity` = `4`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `24`
- Why: both are despatch lines ("An identifier for this despatch line"). The document-level despatch line 1 covers 24 benches; the handling unit despatch lines are numbered 1 to 6 with 4 benches each, so "despatch line 1" means two different lines with different quantities. A receipt advice referring to despatch line 1 (as 17-ReceiptAdvice does) is ambiguous.
- Condition: despatch line IDs are unique within the document, or the handling unit lines are clearly the breakdown of line 1.
- Options: (a, preferred) IDs such as `1.1` to `1.6` for the per-pallet lines; (b) drop the per-pallet lines, since the pallets are identical and the despatch line gives the total.
- Needs decision: no

### retail/12#F8 · Low · Delivery customer's contact is the buying office, not goods-in
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the delivery customer's contact is the one who receives the goods and checks them, as the note asks. The order named that contact (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`); here Brightmarket's buying office is given, with a job title and department (customer service officer, sales) that also contradict its name. The same contact is used for Brightmarket in all 19 retail examples that describe it.
- Condition: the delivery customer's contact is goods-in, with name, job title and department that agree.
- Options: (a, preferred) the goods-in contact of the order.
- Needs decision: no

### retail/12#F9 · Low · Whole item master data copied into the despatch line
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a despatch advice identifies what is shipped; the lot and manufacture date (`ItemInstance`) belong here. The catalogue data (emissions, circularity, load test, dimensions, Urvania's customs tariff code in a domestic Bayvarran delivery) does not, and nothing in the despatch uses it.
- Condition: the despatched item carries its identifiers, the lot data and what the despatch depends on.
- Options: (a, preferred) drop the catalogue data from the item.
- Needs decision: no

## Checked and consistent
- 6 pallets × 4 benches = 24 benches = `DeliveredQuantity` of the despatch line = the ordered quantity of 08-Order (order line 1); shipping marks number the pallets 001 to 006 of 006.
- SSCCs `095206102170000014` to `095206102170000069` and the GRAI pass the check digit (check_ids.py); they use GS1 prefix 952 (demonstration range).
- Shipment `LD-SH-26-0230`, consignment `LD-CS-26-0228` and gross weight 996 kg agree with 11-TransportExecutionPlanRequest and 13-Waybill; the carrier is Bayforth, as in 11 and 13.
- Weight: 996 kg / 6 pallets = 166 kg per pallet; with a wooden pallet of about 25 kg (own knowledge) that leaves about 35 kg per bench, which fits a bench made from 34 kg of steel and 22.5 kg of hardwood consumed, after casting and sawing losses (consumption figures from `CircularityProfile`; yields of about 70 % and 50 % are own assumptions).
- A 13.6 m trailer (`TransportMeansTypeCode` 395, truck with trailer) has room for six pallets.
- Order reference `BS-PO-26-0224` resolves to 08-Order; buyer and seller, despatch supplier and delivery customer are the right parties.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TraceID` = `095206102170000014`: suspected a filler that repeats the SSCC — refuted: the SSCC is the trace identifier GS1 logistics labels carry; repeating it as the trace ID is legitimate.
- `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`: suspected filler — refuted: an explicit default status from UBL's own list.

## Outside this review
- Timeline: this despatch advice is issued on 2026-04-29 at 15:34, after the consignment note (08:56), after the truck was reported on its way (15-TransportationStatus, 11:49) and after the expected arrival at the store at 14:00 (`15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime`); 17-ReceiptAdvice receives the goods on 2026-04-30. A despatch advice is normally sent at despatch, before arrival.
- Timeline: the benches' lot was manufactured on 2026-04-26 by Valdara in Urvania (`ItemInstance`), three days before despatch from Lumeway's stock in Marrowdale, while the item is described as "from the distributor's stock"; whether the goods could have been imported in that time is a cross-flow question.
