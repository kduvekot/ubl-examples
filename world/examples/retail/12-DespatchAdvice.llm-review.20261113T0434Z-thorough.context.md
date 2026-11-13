# LLM review: 12-DespatchAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/12-DespatchAdvice.xml`, Git blob `d93dffcfbe79b292ad495776e25413987734c7cc` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/12#F1 · High · Emission factor times base does not give the emission
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor (see F6).
- Options: drop the emission from the despatch advice (preferred), or correct the factor.
- Needs decision: no

### retail/12#F2 · Medium · The pallet is listed as a package inside itself, holding one item
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:Quantity` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:DeliveredQuantity` = `4`
- Why: ActualPackage is "A package contained in this transport handling unit", and its Quantity "The
  quantity of items contained in this package". The handling unit is a pallet; the one package said to
  be contained in it is also a pallet (with the pallet's returnable GRAI), holding one item. The pallet
  carries four benches, and TotalPackageQuantity says four packages. The returnable pallet is the
  handling unit itself, not a package in it. The same holds for all six handling units
  (`TransportHandlingUnit[2]` … `[6]`).
- Condition: the packages in each handling unit are what the pallet carries (four bench packages, or
  none), and the returnable pallet is described as the handling unit (or its equipment), not as a
  package inside it.
- Options: (a) preferred: four ActualPackages (or one with quantity 4) for the benches, and the GRAI
  on the handling unit's returnable-pallet description (e.g. as a TransportEquipment of type pallet,
  if a fitting element is used elsewhere in the world); (b) drop ActualPackage and keep
  TotalPackageQuantity.
- Needs decision: no

### retail/12#F3 · Medium · A language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/12#F4 · Medium · A system-boundary code in the fullness indication
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty". In a despatch advice with a truck the element could carry a real
  fullness, but here it carries the product footprint's life-cycle boundary (39 examples use this
  list in this element, `grep -l` over `*.xml`).
- Condition: no boundary code in FullnessIndicationCode.
- Options: drop it (preferred).
- Needs decision: no

### retail/12#F5 · Low · Handling-unit despatch lines repeat the despatch line, with clashing IDs
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `24`
- Why: the six HandlingUnitDespatchLines (IDs 1 to 6, four benches each) and the one DespatchLine (ID
  1, 24 benches) describe the same 24 benches twice; despatch line `1` is once four and once 24
  benches. A receiver matching lines by ID gets two different lines `1`.
- Condition: each despatch line ID identifies one line; the handling units refer to the despatch line
  rather than repeating it under the same ID.
- Options: give the handling-unit lines their own IDs (e.g. `1-1` … `1-6`) or replace them by a
  reference to the despatch line (preferred).
- Needs decision: no

### retail/12#F6 · Low · Transport means and a shipping-document reference on one pallet only, and an empty goods item
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `BV LP 2203`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ShipmentDocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:GoodsItem/cbc:ID` = `1`
- Why: the truck carries all six pallets, but TransportMeans ("A means of transport associated with
  this transport handling unit") is given on the first pallet only. ShipmentDocumentReference ("A
  reference to a shipping document associated with this transport handling unit") on that pallet
  points to the booking request 11-TransportExecutionPlanRequest.xml, not to the shipping document,
  the waybill `BF-WB-26-0231` (13-Waybill.xml) issued that morning. The goods item has only an ID.
- Condition: data that concern the whole shipment are given once for the shipment (or for every
  pallet), the shipping-document reference names the waybill, and no aggregate is empty.
- Options: move the truck to the shipment's delivery or consignment transport data and reference the
  waybill there (preferred); drop the empty goods item.
- Needs decision: no

### retail/12#F7 · Low · "No status" codes on the document and the line
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "the status of the Despatch Advice with respect to its original state"
  and LineStatusCode "the status of this despatch line with respect to its original state". An
  original despatch advice has no status to report; `NoStatus` states nothing (IND5/IND6).
- Condition: status codes only for a revised, cancelled or disputed document or line.
- Options: drop both.
- Needs decision: no

### retail/12#F8 · Low · The despatch advice carries the item's full catalogue description and the parties' master data
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: a domestic despatch advice uses the item's identification, lot and quantity; the seller's
  sales conditions, the footprint, circularity, load test and customs codes, and the parties' share
  capital, social media and customs trader number play no part in it (IND5/IND6).
- Condition: the item and parties carry what despatch and receipt use.
- Options: reduce them.
- Needs decision: no

## Checked and consistent
- OrderReference `BS-PO-26-0224` and OrderLineReference `1` resolve to 08-Order.xml; 24 benches
  delivered = 24 ordered = 6 pallets × 4.
- The consignment `LD-CS-26-0228` and gross weight 996 kg are those of
  11-TransportExecutionPlanRequest.xml; the carrier is Bayforth, the provider booked there.
- DespatchSupplierParty Lumeway, DeliveryCustomerParty Brightmarket, buyer and seller as in the order.
- Shipping marks "001 of 006" … "006 of 006" and six SSCCs match six pallets.
- Buyer's item ID `BM-551210` is the one of 08-Order.xml; the grey variant `GRY` is the ordered one,
  not the proposed moss green substitute.
- check_ids.py: all SSCCs, GRAIs, GLNs and the GTIN have valid check digits.

## Considered and refuted
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: `DELIVERY` for a despatch advice — refuted because
  the world's list distinguishes despatch types and a delivery to the customer is the intended type.
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure`: the shipment's gross weight "plus transport
  equipment" equals the consignment's weight without the carrier's equipment in 11 — refuted as
  outside this lens's certainty: with pallets counted as packaging and no other equipment the figures
  can coincide.

## Outside this review
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-04-26`:
  benches made by Valdara in Urvania on a Sunday, three days before they leave Lumeway's stock in
  Marrowdale, while the item is described as "from the distributor's stock"
  — a timeline question across the import and this flow.
