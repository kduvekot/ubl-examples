# LLM review: 05-Order.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/05-Order.xml`, Git blob `f1e12ba8710e50edcc4d14d6820937dec2dde266` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3f5c37 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/05#F1 · High · Ordered pallet said to hold 24 benches; pallets hold four
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:Quantity` = `24`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:PackagingTypeCode` = `PX`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cbc:Quantity` = `96`
- Why: `Package/Quantity` is "The quantity of items contained in this package". The order says one pallet (`PX`) contains 24 benches, while the same line's transaction conditions sell "per pallet of four benches", the catalogue packs four per pallet (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Package/cbc:Quantity` = `4`) and the bill of lading carries pallets of four (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`). Recalculated: 96 / 4 = 24, so 24 is the number of pallets, put in the element for the content of one. Physically, 24 benches of 1800 × 620 × 780 mm and about 56.5 kg of material each (catalogue data) cannot be one pallet (about 1.36 t, and 24 × 0.78 m stacked would be 18.7 m high).
- Condition: the ordered package states four benches per pallet; the number of pallets, if the order states it, is in an element for a count of packages or handling units.
- Options: (a) preferred: `Package/Quantity` 4, and the pallet count, if wanted, on the ordered shipment (e.g. `TotalTransportHandlingUnitQuantity` 24) or left to the despatch documents; (b) drop the ordered package, since the transaction conditions fix the packing.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### sea/05#F2 · High · Emission value is not factor × base
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: as in 02#F2: `ValueFactorNumeric` × `ValueBaseMeasure` = 0.82 × 1 EA = 0.82, not 96 kg CO2e (recalculated; 96 / 0.82 = 117.1). Copied from the catalogue (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`); 39 examples carry the triple (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>' world/examples`).
- Condition: factor × base = value in the stated units, or factor and base are absent (or the order carries no footprint, F16).
- Options: (a) preferred: drop factor and base, as in all earlier flows; (b) a factor on a base whose product is 96; (c) factor 96 per 1 EA (broad).
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### sea/05#F3 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 such elements in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: `LocaleCode` is absent or a locale from a locale list.
- Options: (a) preferred: drop it; (b) `en-XB` from a list of language tags.
- Needs decision: no
- From: broad (F5), parties (F1), context (F4)

### sea/05#F4 · Medium · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate is not a street name, and the order arranges no pickup. 79 occurrences in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street-name element of Lumeway's postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no
- From: broad (F6), parties (F2), context (F8, Low)

### sea/05#F5 · Medium · LifecycleStageCode MANUFACTURING for a footprint from the ore at the mine
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: as in 02#F9: the code names manufacturing only, the description covers raw-material extraction, transport and manufacturing (EN 15804 A1–A3, own knowledge); code and text disagree. No part raised it in 05; added in the merge, aligned with 02 and the earlier flows.
- Condition: the lifecycle stage code covers what the description says, or the description is limited to manufacturing (or the order carries no footprint, F16).
- Options: (a) preferred: a product-stage / cradle-to-gate code; (b) a description saying that upstream supply is included.
- Needs decision: no
- From: merge (no part; broad refuted it in 02)

### sea/05#F6 · Medium · An emission boundary code in FullnessIndicationCode
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; cradle-to-gate is a footprint boundary from the world's `EmissionBoundaryCode` list, and an ordered bench has no transport equipment.
- Condition: no `FullnessIndicationCode` on the item's emission, or a fullness code of transport equipment.
- Options: (a) preferred: drop it (the boundary is in `LifecycleStageDescription`).
- Needs decision: no
- From: broad (F3), context (F3)

### sea/05#F7 · Medium · The spare side frame classified as a general cast article, not as a part of a seat
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: as in 02#F11: a side frame made for the Serra bench (`/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cbc:Description` = `Spare side frame for the Serra bench.`) is an identifiable part of a seat (HS 9401.99); Section XV Note 1 excludes articles of Chapter 94 from heading 7325 (own knowledge of HS 2022). 22 examples carry 732599 (`grep -l 732599 world/examples/*/*.xml`).
- Condition: HS, national tariff and CPC codes classify the side frame as a part of a seat, or the item is a casting of general use.
- Options: (a) preferred: HS 940199 with the matching tariff and CPC codes.
- Needs decision: no
- From: broad (F4)

### sea/05#F8 · Low · Velumi Trading and Nalevi Warehousing described differently from the documents that answer this order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: here both Lisavan parties carry `en-XL` renderings and their legal form in Lisavan and English; the order response to this order describes the buyer with `en-XB` and the legal form once, in English (`06-OrderResponse.xml:/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`), and the bill of lading does the same for Nalevi (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`). The flow splits along the issuer (Lisavan issuers 05, 17, 19, 21, 24, 27–29 use this form). This example has the fuller, Lisavu-appropriate description; the finding is the inconsistency with the documents it is linked to.
- Condition: Velumi and Nalevi carry the same address renderings, `languageID` values and legal-form renderings in every example, following one documented rule.
- Options: (a) preferred: this example's description everywhere (`en-XL`, legal form in both languages), so nothing changes here; (b) a documented issuer-variety rule, with the Lisavan legal form everywhere.
- Needs decision: yes
- From: parties (F3)

### sea/05#F9 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID"; Velumi Trading and Nalevi Warehousing share the New Year's Day date with companies in all three registers (271 times in 181 examples, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while Lumeway has `1988-10-03`.
- Condition: every `RegistrationDate` is the party's date in the world, or absent.
- Options: (a) preferred: an own date per company; (b) drop it.
- Needs decision: yes
- From: parties (F5)

### sea/05#F10 · Low · Contacts of the buyer and the delivery party carry a seller's title and department
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's contact buys and the warehouse's goods-inwards contact receives goods (checklist); both carry the job title and department of a seller's customer service, the same as Lumeway's.
- Condition: each contact's title and department fit its name and role (purchasing; goods receipt), or are absent.
- Options: (a) preferred: e.g. procurement officer / Purchasing for Velumi, goods-in supervisor / Warehouse operations for Nalevi; (b) functional names only.
- Needs decision: no
- From: broad (F9), parties (F4, F7), context (F6)

### sea/05#F11 · Low · Delivery places only as text, not linkable to the follow-up documents
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Lanoro warehouse, Selanu`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Port of Selanu`
- Why: the delivery location is a description naming a "Lanoro warehouse", which occurs in no other example (`grep -rl --include='*.xml' Lanoro world/examples` finds only this file), while the delivery party Nalevi has its address at Lagoon Road 9 and the despatch advice delivers there (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `95940358`); nothing says Lanoro is Nalevi's site. The Incoterms place is given as text, while the order response identifies it as UN/LOCODE `XLSEL` (`06-OrderResponse.xml:/OrderResponse/cac:DeliveryTerms/cac:DeliveryLocation/cbc:ID` = `XLSEL`). The checklist asks that a location carry the identifier by which the same place is identified elsewhere.
- Condition: the delivery location is identified (address or delivery-point ID) the same way as in the despatch advice, and the delivery terms' place carries the port's identifier.
- Options: (a) preferred: Nalevi's warehouse address or delivery-point ID in `DeliveryLocation` (keeping the name, if Lanoro is its name), and `XLSEL` in the terms' location; (b) drop `DeliveryLocation` and let the delivery party's address stand.
- Needs decision: no
- From: broad (F10), parties (F6), logistics (F3), context (F7)

### sea/05#F12 · Low · CIF for goods in a container
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: Incoterms 2020 reserve CIF for goods placed on board the vessel and recommend CIP for containerised goods handed to the carrier at a terminal (own knowledge); the goods travel as a full container load (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`). CIF is common in practice for containers, and the context part found it fitting; a plausibility remark about the deal's terms.
- Condition: the delivery term fits the way the goods are handed over, or the choice of CIF is deliberate.
- Options: (a) CIP with the named place; (b) keep CIF (common practice).
- Needs decision: yes (the trade terms of the deal)
- From: broad (F12); context (Checked and consistent) disagreed

### sea/05#F13 · Low · CIF order's anticipated total leaves out the freight and insurance the seller bills later
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `50688.00`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: `AnticipatedMonetaryTotal` is "The total amount for the Order anticipated by the buyer". Under CIF the seller contracts and pays carriage and insurance to Selanu. The buyer anticipates the goods value only (recalculated: 96 × 520 = 49,920.00 + 12 × 64 = 768.00 → 50,688.00), while the invoice for this order adds sea freight and insurance (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`, `22-Invoice.xml:/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`; 50,688.00 + 2,950.00 + 140.00 = 53,778.00 = `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`). Either the CIF price includes freight and insurance (then the invoice charges them twice) or the seller passes them on (then the order and the order response would show it). The order alone cannot tell; the choice changes the money story of the flow.
- Condition: the order's anticipated total and the way the flow bills freight and insurance under CIF tell the same story.
- Options: (a) preferred: treat 520 as a CIF price and stop billing freight and insurance separately in the invoice (nothing changes here; aligned with 06#F1 and sea merger c); (b) keep the goods value here and make the surcharge explicit in the order response (money part's preference, the catalogue price being a trade price); (c) anticipated freight and insurance charges in the order.
- Needs decision: yes
- From: money (F1)

### sea/05#F14 · Low · The catalogue's full-container discount is not applied, without a reason
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `49920.00`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`
- Why: the catalogue line the order refers to grants 3 % for "Full container" on the range 4–192 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`), 96 benches lie in that range, and they travel as FCL. The order prices them at 520 without it (recalculated: 96 × 15.60 = 1,497.60 XBL would be the allowance). The money part refuted this for the order: the catalogue does not say when a "full container" is reached, the problem is the catalogue's encoding (02#F6), and the order's price is consistent with the discount not being earned (41.5 m³ for 96 benches is far from a full 40-foot box). Both readings hold until 02#F6 is resolved.
- Condition: the order's line amount reflects the catalogue's allowance when its condition is met, or the documents make clear why it does not apply.
- Options: (a) preferred: resolve 02#F6 so that 96 benches visibly do not qualify (nothing changes here); (b) add the 3 % allowance and follow it through order response and invoice.
- Needs decision: yes (whether the discount applies)
- From: broad (F7); money (Considered and refuted, carried as counter-argument)

### sea/05#F15 · Low · Originator and beneficiary repeated on every line
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: the header already names the Port of Selanu as originator and beneficiary of the whole order (`/Order/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`); line-level parties serve to name a different party for a line. Repeating the same party says nothing (no fillers). The parties part checked the header and lines as consistent; the merge keeps the remark, since it concerns redundancy, not consistency.
- Condition: line-level originator and beneficiary appear only where they differ from the header.
- Options: (a) preferred: drop them from the lines.
- Needs decision: no
- From: broad (F11)

### sea/05#F16 · Low · The seller's catalogue description copied into the order
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:EmissionStandardReference` = `Greenhouse Gas Protocol Product Standard`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: an Order is "used to order goods and services"; the item is identified by buyer's, seller's, manufacturer's and standard identifiers and the catalogue reference. Keywords ("assigned by the seller party"), warranty, test method, emission calculation, circularity profile and the Urvanian national tariff code (a Bayvarra → Lisavu trade, Urvania only the origin) are catalogue content the buyer orders nothing by; line 2, from the same catalogue, carries none of it. Section 4.8.
- Condition: the ordered item carries what identifies and specifies the order (identifiers, catalogue reference, chosen colour, any property the buyer requires), not a copy of the catalogue description.
- Options: (a) preferred: reduce line 1's item to the form of line 2 plus the colour variant; (b) keep only properties the buyer requires (e.g. load capacity as a requirement).
- Needs decision: no
- From: broad (F8), context (F5); the XU tariff code added in the merge (as air)

### sea/05#F17 · Low · GTINs of the maker's Valdara items in Lumeway's GS1 company prefix
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: as in 02#F16: both GTINs are in `9520610`, the prefix of Lumeway's GLN (`/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`), while the brand is Valdara's. Added in the merge, aligned with retail and sea b/d.
- Condition: the GTINs come from the brand owner's company prefix, or the brand owner is Lumeway.
- Options: (a) preferred: a Valdara company prefix; (b) a story in which Lumeway owns the brand.
- Needs decision: yes
- From: merge (no part)

### sea/05#F18 · Low · World item numbers that are valid GTIN-12s
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: as in 02#F20: 12 digits with a valid GS1 check digit (recalculated) in a range of GS1 US company prefixes (own knowledge); they could be mistaken for real GTIN-12s. Added in the merge.
- Condition: world item numbers cannot be read as valid GTINs, or are verified as unassigned.
- Options: (a) preferred: change the world's item-number format; (b) record a verification.
- Needs decision: yes
- From: merge (no part)

## Checked and consistent
- Arithmetic recalculated: 96 × 520.00 = 49,920.00 (`/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount`); 12 × 64.00 = 768.00 (`/Order/cac:OrderLine[2]/cac:LineItem/cbc:LineExtensionAmount` = `768.00`); sum 50,688.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `50688.00` = taxable amount; tax 0 % → `/Order/cac:TaxTotal/cbc:TaxAmount` = `0.00`; the same totals in `06-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00`.
- Prices, items, identifiers and classification agree with `02-Catalogue.xml` (reference `LD-CAT-26-0124`, issued 2026-05-04, valid from that day); 96 lies in 4–192 and is a multiple of the delivery unit 4; 12 frames ≥ minimum 1.
- Tax category G, 0 %, EXP under STT agrees with the catalogue, order response and invoice.
- Quantities 96 benches and 12 frames are the same in order response, packing list, export declaration and bill of lading (24 pallets × 4 + 1 pallet of 12).
- Buyer = accounting customer = Velumi (`IC41859`), invoiced in 22; originator and beneficiary the Port of Selanu (`IC41037`), consistent with `CustomerReference` "Harbour parks Selanu" and with 06's originator document `PS-REQ-26-0031`.
- CIF with cargo insurance agrees with the bill of lading's insurance certificate `WS-CERT-26-0884`. Check digits of GLN and both GTINs correct (`check_ids.py`).

## Considered and refuted
- `/Order/cbc:AccountingCost` = `Stock for municipal projects` next to a port as originator — refuted: Velumi's own cost allocation; the port's parks can be a municipal project (from broad, parties, context).
- `/Order/cac:AccountingCustomerParty` equal to the buyer — refuted: the element has no "if different" condition in an order, and the buyer is the party invoiced (from broad, parties).
- `/Order/cbc:AccountingCostCode` = `500` as a seller-side code — refuted: "the buyer's accounting code", issued by the buyer (from money).
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason`: the buyer stating the seller's export exemption — refuted: the anticipated tax of an order may follow the catalogue's tax category (from context).
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`: discount not applied — refuted by money; carried into F14 as counter-argument.

## Changed in the merge
- broad/F2, logistics/F2, context/F2 → F2: preferred option drop factor and base (broad preferred factor 96).
- broad/F5, parties/F1, context/F4 → F3: preferred option drop, aligned.
- context/F8 → F4: Low raised to Medium, aligned.
- F5 (MANUFACTURING), F17 (GTIN prefix), F18 (world item numbers) added in the merge, aligned with 02 and earlier flows.
- broad/F9, parties/F4 and F7, context/F6 → F10: grouped (one contacts finding per example).
- broad/F10, parties/F6, logistics/F3, context/F7 → F11: grouped.
- broad/F7 → F14: kept as Low/yes with money's refutation; preferred option changed to resolving 02#F6 (the cause lies in the catalogue's encoding).
- broad/F8 + context/F5 → F16: grouped; the XU national tariff code added (as air/01#F10).
- money/F1 → F13: preferred option changed to the CIF-price reading (money preferred (b)), aligned with 06#F1 and sea merger c.
