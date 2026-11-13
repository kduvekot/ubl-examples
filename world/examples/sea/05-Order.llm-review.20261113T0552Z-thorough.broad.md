# LLM review: 05-Order.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/05-Order.xml`, Git blob `f1e12ba8710e50edcc4d14d6820937dec2dde266` (committed)
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

### sea/05#F1 · High · Pallet said to hold 24 benches; the catalogue sells pallets of four
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:Quantity` = `24`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cbc:Quantity` = `96`
- Why: `Package/Quantity` is "The quantity of items contained in this package". The order says a pallet (`PX`) holds 24 benches, while the catalogue the order refers to sells the bench "per pallet of four benches" (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Package/cbc:Quantity` = `4`) and the bill of lading carries 4 packages per pallet (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`). 96 benches are 24 pallets of 4: the 24 is the number of pallets put where the content of one pallet belongs. Physically, 24 benches of 1800 × 620 × 780 mm and about 56 kg each (catalogue data) do not fit on one pallet.
- Condition: the ordered package states the content of one pallet (4 benches), and, if wanted, the number of pallets elsewhere (e.g. `Package/Quantity` = 4 with 24 such packages, or a `TotalPackageQuantity`-like statement in the shipment).
- Options: (a) preferred: `Package/Quantity` = 4 EA, and the number of pallets in the ordered shipment (e.g. `Shipment/TotalTransportHandlingUnitQuantity` = 24); (b) drop the package from the order.
- Needs decision: no

### sea/05#F2 · High · Emission value is not factor × base
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies"; 0.82 × 1 EA = 0.82, not 96 kg. The values are copied from the catalogue (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`). 39 examples carry the factor 0.82 (`grep -l "<cbc:ValueFactorNumeric>0.82" world/examples/*/*.xml`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a) preferred: factor 96 per 1 EA; (b) drop factor and base.
- Needs decision: no

### sea/05#F3 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; a product's cradle-to-gate boundary is not a load factor of transport equipment. 39 examples carry this code in this element (`grep -l 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"' world/examples/*/*.xml`).
- Condition: `FullnessIndicationCode` is absent from product emissions or holds a fullness code.
- Options: (a) preferred: drop it; the boundary is stated in `LifecycleStageDescription`.
- Needs decision: no

### sea/05#F4 · Medium · Spare side frame classified as a general cast article, not as a part of a seat
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: a side frame made for the Serra bench is a part of a seat (HS 9401.99); Section XV Note 1 excludes articles of Chapter 94 from heading 7325 (own knowledge of HS 2022). 22 examples carry 732599 (`grep -l 732599 world/examples/*/*.xml`).
- Condition: HS, national tariff and CPC codes classify the side frame as a part of a seat, or the item is a casting of general use.
- Options: (a) preferred: HS 940199 with the matching tariff and CPC codes.
- Needs decision: no

### sea/05#F5 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode` (`grep -c LocaleCode world/examples/*/*.xml`).
- Condition: `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/05#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in the seller's postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/05#F7 · Low · Anticipated total ignores the catalogue's full-container discount
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `49920.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `50688.00`
- Why: the catalogue line the order refers to grants 3 % off for a full container (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`), and the goods travel as a full container load (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`); 96 benches are within the catalogue's maximum of 192. The order anticipates 96 × 520 = 49,920 XBL without the discount (which would be 96 × 15.60 = 1,497.60 XBL). Either the discount applies and is missing, or its condition is not met and nothing says why.
- Condition: the order's line amount reflects the catalogue's allowance when its condition is met, or the documents make clear why it does not apply.
- Options: (a) add the 3 % allowance to line 1 (and follow it through order response and invoice); (b) state in the catalogue what "full container" requires, so that this shipment visibly does not qualify.
- Needs decision: yes (whether the discount applies to this order)

### sea/05#F8 · Low · Product data of the catalogue copied into the order
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- Why: the order line repeats the whole product description of the catalogue: emissions with their calculation method, circularity profile, load test, dimensions. An order needs the item identified (it is, by seller's, buyer's, manufacturer's and GTIN identifiers and the catalogue reference); the buyer does nothing with the seller's LCA or test method in its order.
- Condition: the order line carries what the order needs to identify and specify the ordered item (identifiers, colour variant), not the catalogue's product sheet, unless the order has a reason (e.g. a required property) stated in it.
- Options: (a) preferred: keep identifiers, catalogue reference and the colour variant; drop emissions, circularity, test method and dimensions; (b) none better seen.
- Needs decision: no

### sea/05#F9 · Low · Contacts whose job title and department do not fit their names
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's contact is `Purchasing` and the delivery party's contact is `Goods inwards` (a consignee's contact receives goods); both carry the job title and department of a seller's customer service.
- Condition: job title and department of each contact agree with its name and the party's role.
- Options: (a) preferred: purchasing officer / Purchasing for Velumi; goods-in supervisor / Warehouse for Nalevi.
- Needs decision: no

### sea/05#F10 · Low · Delivery location given only as text
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Lanoro warehouse, Selanu`
- Why: the location to deliver to is named in free text only; neither an address nor an identifier links it to the delivery party's address (`/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`), and "Lanoro" appears in no address of the party. A carrier cannot tell from the order whether the warehouse is at the party's address.
- Condition: the delivery location has an address or identifier, or is the delivery party's address in an evident way.
- Options: (a) preferred: give the warehouse's address (or its location ID) in `DeliveryLocation`; (b) drop `DeliveryLocation` and rely on the delivery party's address.
- Needs decision: no

### sea/05#F11 · Low · Originator and beneficiary repeated on every line
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: the header already names the Port of Selanu as originator and beneficiary of the whole order (`/Order/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`); line-level parties serve to name a different party for a line. Repeating the same party on every line says nothing.
- Condition: line-level originator and beneficiary appear only where they differ from the header.
- Options: (a) preferred: drop them from the lines.
- Needs decision: no

### sea/05#F12 · Low · CIF for goods in a container
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: Incoterms 2020 reserve CIF for goods placed on board the vessel and recommend CIP for containerised goods handed to the carrier at a terminal (own knowledge of Incoterms 2020). The goods travel as a full container load (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`). CIF is common in practice for containers, so this is a plausibility remark.
- Condition: the delivery term fits the mode in which the goods are handed over, or the choice of CIF is deliberate.
- Options: (a) CIP with the named place; (b) keep CIF (common practice).
- Needs decision: yes (the trade terms of the deal)

## Checked and consistent
- Arithmetic: 96 × 520 = 49,920.00; 12 × 64 = 768.00; 49,920 + 768 = 50,688.00 = line extension, taxable amount and payable amount; tax 0.00 at 0 %.
- Prices, items, identifiers and classification of both lines agree with the catalogue (`02-Catalogue.xml`); 96 is within the catalogue's 4–192 and a multiple of 4; line 2's 12 is above its minimum of 1.
- Export tax category `G` fits a Bayvarran seller delivering to Lisavu.
- Velumi's address is tagged `en-XL` here, which fits a Lisavu address (the other examples differ; see their reviews).
- CIF with cargo insurance agrees with the flow: the bill of lading references an insurance certificate (`14-BillOfLading.xml`, `PolicyDocumentReference` `WS-CERT-26-0884`).
- Check digits of GLN and both GTINs correct (`check_ids.py`).

## Considered and refuted
- `/Order/cbc:AccountingCost` = `Stock for municipal projects`: stock for projects next to an originator that is a port — refuted because Velumi buys for its stock and names the port's park project in `CustomerReference`; the port is a public body that can run municipal projects.
- `/Order/cac:AccountingCustomerParty`: equal to the buyer — refuted because the element is not conditional on differing from the buyer.
