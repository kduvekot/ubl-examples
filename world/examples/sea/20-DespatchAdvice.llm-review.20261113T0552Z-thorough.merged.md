# LLM review: 20-DespatchAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/20-DespatchAdvice.xml`, Git blob `48649a02a6dba4b51ed92b3c8c00d3a15724cd7a` (committed)
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

### sea/20#F1 · High · The bench's emission value, factor and base do not agree
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies". 0.82 × 1 EA = 0.82, not 96 kg CO2e; 96 / 0.82 = 117.1. The three values contradict each other. Added by the merge (no part raised it), aligned with sea merges a/d and the earlier flows.
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a) preferred: drop factor and base; (b) a factor and base whose product is 96 kg.
- Needs decision: no
- From: merge (no part raised it)

### sea/20#F2 · Medium · A language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the values repeat the ISO 639 code of `Language/cbc:ID` and name no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale from a list that defines locales.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` with a locale list.
- Needs decision: no
- From: parties (F2)

### sea/20#F3 · Medium · Gate number in AdditionalStreetName of the despatch party's postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." A business-park gate is a vehicle access point, not a street; where it matters for the despatch it belongs in a despatch (pickup) location. 79 occurrences in 76 files, always Lumeway's address (parties, grep over `*.xml`).
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop it from the postal address, giving it in a despatch location if the story needs it; (b) the park's internal road name.
- Needs decision: no
- From: broad (F2), parties (F1)

### sea/20#F4 · Medium · Shipment gross weight leaves out the container
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- XPath: `10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment." 4106.4 kg is benches 3984 kg + side frames 122.4 kg with packaging (`10-PackingList.xml`); merge recalculation with the 3750 kg container tare: 4106.4 + 3750 = 7856.4 kg, the container's gross weight in the packing list and the bill of lading. Same value in 8 examples of the flow (logistics, XPath query over `sea/*.xml`).
- Condition: `Shipment/GrossWeightMeasure` includes the container, or the goods' weight is given in an element whose definition excludes it.
- Options: (a) preferred: 7856.4 kg with the container stated (see F5); (b) drop the shipment weight.
- Needs decision: no
- From: broad (F1), logistics (F2)

### sea/20#F5 · Medium · The despatch advice does not say when, or in what container and pallets, the goods are despatched
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `One 40-foot container: 24 pallets of 4 benches.`
- XPath: `/DespatchAdvice/cbc:IssueTime` = `08:52:00`
- Why: A despatch advice is "a document used to describe the despatch or delivery of goods". This one gives items and quantities but no despatch date or expected delivery (no `Shipment/Delivery` or `Despatch` with dates or delivery location), no container and no handling units: container `TWLU4120872` and the 25 SSCC-labelled pallets (`14-BillOfLading.xml`) appear only in the free-text line note, although `DespatchLine/Note` is for information "not contained explicitly in other structures". The receiving 3PL, Nalevi Warehousing, needs exactly these data to plan and check the receipt (its receipt advice `21-ReceiptAdvice.xml` refers to this document). The order names the delivery place (`05-Order.xml`), and the container was handed to the carrier at 10:15 the same day (`14-BillOfLading.xml`).
- Condition: The despatch advice states the despatch date and the expected delivery (date or period), and identifies the container and the pallets the lines are packed in.
- Options: (a) preferred: `Shipment/Delivery` with despatch date 2026-05-13 and the estimated delivery period at Nalevi's warehouse, `Shipment/TransportHandlingUnit` with the container and the 25 pallets, lines linked to them; (b) at least the dates and the container ID, the pallet detail left to the referenced packing list.
- Needs decision: no
- From: logistics (F1), broad (F5, Low)

### sea/20#F6 · Medium · Lifecycle stage "Manufacturing" for an emission described from the mine to the factory gate
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: The code names one stage, the description covers raw material extraction, transport and manufacturing (cradle to gate, EN 15804 A1–A3, own knowledge). Code and its text equivalent disagree. Added by the merge, as in 19 and the earlier flows.
- Condition: The lifecycle stage code and description name the same scope.
- Options: (a) preferred: a product-stage code if the list has one, or drop the code; (b) narrow the description (changes the value).
- Needs decision: no
- From: merge (no part raised it)

### sea/20#F7 · Medium · "Cradle to gate" in an element that says whether transport equipment is full
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty …". A product-footprint system boundary is not a fullness indication; the code comes from a list meant for another concept. Added by the merge (Medium/no, TC write-up), as in 19 and the earlier flows.
- Condition: `FullnessIndicationCode` is absent from the item's footprint, or holds a fullness indication.
- Options: (a) preferred: drop it; (b) record the missing boundary element for the UBL TC.
- Needs decision: no
- From: merge (no part raised it)

### sea/20#F8 · Low · Document and line status "no status"
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:LineStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` / `LineStatusCode` signify the status "with respect to its original state". "No status" conveys what absence conveys; under "no fillers, nothing implied by absence" the values have no reason (26 `DocumentStatusCode` = `NoStatus` in the examples, context, grep over `*.xml`).
- Condition: Status codes are present only where the document or line has a status worth stating.
- Options: (a) preferred: drop them; (b) keep them only by a recorded project decision.
- Needs decision: no
- From: context (F3)

### sea/20#F9 · Low · Damage to be reported "on the consignment note" for a sea shipment under a bill of lading
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods travel by sea under bill of lading `TOL-BL-26-0139` and reach Nalevi via the Selanu terminal; a consignment note is the road or rail transport document (CMR, CIM; own knowledge), and none exists in this flow. The warehouse in fact reports the damaged side frame in its receipt advice (`21-ReceiptAdvice.xml`). The note names a document the receiver does not have.
- Condition: The note names the document or channel the receiver actually uses, or is absent.
- Options: (a) preferred: "… report any damage in the receipt advice"; (b) name the bill of lading or the haulier's delivery receipt of the last leg.
- Needs decision: no
- From: context (F1), logistics (F3)

### sea/20#F10 · Low · Contacts whose name, job title and department disagree
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Nalevi's goods-inwards contact fits the role by name, but is a customer service officer in Sales; Velumi's Purchasing contact is also in Sales. Name, title and department of each contact contradict each other; both are master-data contacts recurring in every example that describes the parties in full.
- Condition: Each contact's name, job title and department describe the same function (goods receipt at the warehouse, purchasing at the buyer).
- Options: (a) preferred: matching titles and departments (e.g. receiving clerk / Warehouse; buyer / Purchasing); (b) drop title and department.
- Needs decision: no
- From: broad (F4), parties (F3)

### sea/20#F11 · Low · Lisavu addresses tagged as Bayvarran English, legal forms in English only
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `21-ReceiptAdvice.xml:/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: The English renderings of Nalevi's and Velumi's Lisavu addresses carry `languageID="en-XB"`, and their legal forms are in English only, untagged; the receipt advice describes the same parties with `en-XL` and the legal form in Lisavan and English. The tag follows the issuer, not the place. Over `*.xml`: English street/town renderings in Lisavu addresses `en-XL` 188, `en-XB` 141, `en-XU` 9 (parties, lxml).
- Condition: The same rendering of the same address carries the same `languageID` everywhere, under one documented rule, and legal forms are given in the same languages.
- Options: (a) preferred: `en-XL` and the legal form in Lisavan and English everywhere; (b) keep the issuer's locale and record the convention.
- Needs decision: yes (one world rule; parties said no, aligned with 16 and sea a/d, air, wood, plastics)
- From: parties (F4)

### sea/20#F12 · Low · Tax registrations and share capital in a despatch advice
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- Why: A despatch advice states no prices or taxes; the despatch party's and carrier's Bayvarran sales-tax registrations and share capital play no part (copied master data, section 4.8). Buyer and delivery recipient carry no tax scheme here.
- Condition: The despatch party and the carrier carry only the party data a despatch advice uses.
- Options: (a) preferred: drop their `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator`; (b) keep them with a reason.
- Needs decision: no
- From: parties (F5), money (F1)

### sea/20#F13 · Low · Catalogue and product-passport data copied into the despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: A despatch advice tells the delivery party what is coming so it can receive and check it. The bench's item carries the catalogue's keywords, warranty, sales conditions, load test, emissions (see F1, F6, F7), circularity profile and product documentation; the receiving warehouse does nothing with them. The side-frame line does without them.
- Condition: The despatch lines carry what the delivery party needs to receive and identify the goods (identifiers, description, lots and instances, handling-relevant dimensions), other data only with a stated reason.
- Options: (a) preferred: reduce the item to identification, description, lot and handling data; (b) keep a product-passport reference only if the world wants it to travel with the goods.
- Needs decision: no
- From: broad (F6), context (F2)

### sea/20#F14 · Low · GTINs in the distributor's GS1 company prefix, not the manufacturer's
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: The GTINs of Valdara Industries' bench and side frame begin with `9520610`, the company prefix of Lumeway Distribution's GLN `9520610900008`. Under GS1 rules the brand owner allocates the GTIN (own knowledge); nothing makes these Lumeway private-label products. Check digits valid (`check_ids.py`). Added by the merge, as in 19, sea d and the retail merges.
- Condition: The GTINs are in the brand owner's prefix, or the world states that Lumeway is the brand owner.
- Options: (a) preferred: GTINs in Valdara's own prefix; (b) record Lumeway as brand owner.
- Needs decision: yes
- From: merge (no part raised it)

### sea/20#F15 · Low · World item numbers with valid GS1 check digits
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: Both 12-digit world item numbers carry a valid GTIN-12 check digit (merge recalculated: 7 and 4), and read as GTIN-12 they fall in prefix 077 (GS1 US range; own knowledge), so they can be mistaken for real GTINs. Added by the merge, as in 19 and the earlier flows.
- Condition: The world item numbers cannot be read as valid GTINs, or the convention is recorded.
- Options: (a) preferred: a non-GTIN format; (b) record the convention.
- Needs decision: yes
- From: merge (no part raised it)

### sea/20#F16 · Low · Benches "from the distributor's stock" made three days before despatch
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- Why: The benches are said to come from Lumeway's stock in Bayvarra, but the lot and all 12 castings were made on 2026-05-10 (a Sunday) by Valdara in Urvania, after the order of 2026-05-07, two days before the container was weighed in Bayvarra (2026-05-12) and three days before this despatch. Goods made after the order in another country are not stock held by the distributor; the description and the manufacture date in the same document disagree. Context and logistics put the question under "Outside this review" as a timeline question; the merge follows broad, since the contradiction is within this example (the cross-flow feasibility stays outside).
- Condition: The manufacture dates fit goods held in Lumeway's stock before the order, or the description no longer says "from the distributor's stock".
- Options: (a) preferred: manufacture dates (and lot) before the order, keeping the stock story; (b) change the description.
- Needs decision: no
- From: broad (F3); context and logistics under "Outside this review"

## Checked and consistent
- References: order `VT-PO-26-0127` with lines 1 and 2 (`05-Order.xml`) and packing list `LD-PL-26-0134` (`10-PackingList.xml`, issued 2026-05-12 15:59, before this advice) exist; shipment and consignment IDs are those of the bill of lading (broad, context, logistics).
- Quantities: 24 pallets × 4 = 96 benches; 12 side frames with 12 item instances, serials VI-SF-01230 to VI-SF-01241 without gaps, one melt; equal to order, packing list, bill of lading (24 pallets + 1 pallet of 12 boxes = 25), import declaration, invoice and receipt advice (96 and 11 + 1 rejected) (broad, context, logistics).
- Timing: issued 2026-05-13 08:52, after the VGM weighing (2026-05-12 15:30) and before the drop-off at the Lumeport terminal (10:15) in `14-BillOfLading.xml` (broad, logistics).
- Parties: despatch party, seller and signatory Lumeway (`20410274`); buyer Velumi (`IC41859`); originator and beneficiary Port of Selanu as in the order; Nalevi (`IC41722`, ISIC 5210) is the order's delivery party, the B/L's notify party and the party that confirms receipt in 21; carrier Tidewell as in 14; manufacturer Valdara consistent; Lumeway's and Tidewell's descriptions identical across the flow (parties).
- GTINs and GLN pass `check_ids.py`; accounting cost `500` "Stock for municipal projects" as in the order and `22-Invoice.xml` (broad, logistics, parties).

## Considered and refuted
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: the B/L names Velumi as final delivery party — refuted: Nalevi receives physically on Velumi's behalf (from broad).
- `/DespatchAdvice/cbc:AccountingCostCode` = `500`: the buyer's cost centre on the seller's document — refuted: carried over from the order so the receiver can book; the definition does not name whose (from broad, money).
- `/DespatchAdvice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`: originator and beneficiary in a despatch advice — refuted: the order was placed for the port's project, the advice repeats the order's parties, and the warehouse keeps the goods apart for it (from broad, context, parties).
- `/DespatchAdvice/cbc:IssueDate` = `2026-05-13`: before the bill of lading (05-14) — refuted: the advice is sent when the goods leave the seller (from context).
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`: the seller's customer service as despatch contact — refuted: it is where a recipient reports delivery problems (from parties).
- `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`: the buyer's customs trader number — refuted: the goods cross a customs border to the importer's warehouse (from parties).

## Changed in the merge
- Added by the merge: F1 (emission triple, High), F6 (MANUFACTURING), F7 (CRADLETOGATE), F14 (GTIN prefix, Low/yes), F15 (world item numbers, Low/yes), aligned with 19, sea d and the earlier flows.
- broad/F5 (Low) and logistics/F1 (Medium) → F5 (Medium): a despatch advice without despatch date and container lacks what its purpose depends on.
- context/F3 Needs decision yes → no (F8), aligned with all flows.
- parties/F4 Needs decision no → yes (F11), aligned with the earlier flows' en-XB/en-XL row.
- broad/F3 kept as F16 although context and logistics put it under "Outside": the contradiction is inside this example.
- Combined: broad/F1 + logistics/F2 → F4; broad/F2 + parties/F1 → F3; context/F1 + logistics/F3 → F9; broad/F4 + parties/F3 → F10; parties/F5 + money/F1 → F12; broad/F6 + context/F2 → F13.

## Outside this review
- Whether the castings and benches could be made on 2026-05-10 in Urvania, moved to Bayvarra and packed by 2026-05-12 is a timeline question across flows (from context, logistics).
- The same 4106.4 kg shipment weight occurs in other examples of the flow; each belongs to its own review (from logistics).
