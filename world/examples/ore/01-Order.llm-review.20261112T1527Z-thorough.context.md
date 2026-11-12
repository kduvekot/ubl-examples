# LLM review: 01-Order.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/01-Order.xml`, Git blob `af435c2882d01f0ca686e44a410c2da3f745d496` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/01#F1 · Medium · A province is given in `Region`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("the political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The world itself does this for Bayvarra (`CountrySubentity` = "Coastal State"/"Upland State" with a `CountrySubentityCode`), but uses `Region` for the Urvanian province: "Province of Ferrano" is in `Region` in 104 XML examples (`grep -rl --include='*.xml' 'Province of Ferrano' world/examples | wc -l`).
- Condition: the Urvanian province is carried in `CountrySubentity` (optionally with a `CountrySubentityCode` from an Urvanian list), and `Region` holds a value only where an address really lies in a named geographic or economic region.
- Options: (a) preferred: move the value to `CountrySubentity` in all three addresses (and every other Urvanian address), as for Bayvarra; (b) if "Province of Ferrano" is meant as an economic region and not an administrative unit, say so in the world's story and give it a name that does not read as a province.
- Needs decision: no

### ore/01#F2 · Low · The buyer's contact is a sales/customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact of the `BuyerCustomerParty` in an Order is the person or function that buys and answers questions about the purchase. Valdara's contact is its "Order desk" in the Sales department with the job title "Customer service officer", the function that takes Valdara's own customers' orders; the seller's contact has exactly the same job title and department (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`). For an ore purchase a purchasing/raw-materials buyer would be expected. The same Valdara contact is used in every ore example, in every role (buyer, transport user, consignee, accounting customer, payer).
- Condition: the buyer's contact in this Order is a purchasing function of Valdara (name, job title and department agreeing with each other and with the buyer role).
- Options: (a) preferred: a purchasing contact (e.g. raw-materials purchasing, Department "Purchasing"); (b) omit the contact if the world has no purchasing contact for Valdara.
- Needs decision: no

### ore/01#F3 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: the buyer's share listing on the Ferrano Stock Exchange and its warehousing-and-despatch provider play no part in an order for a train of iron ore delivered FCA at the mine siding and carried by Ferrano Rail Cargo to Valdara's own works: Castrano Logistics appears in no other role in any ore example (it only occurs inside this `ServiceProviderParty` in all eight). They look copied from Valdara's master data. The same SecurityListing (ISIN `XU0001042501`) occurs in 75 XML examples and the same service provider (`VI-SP-2026-01`) in 75 (`grep -rl --include='*.xml'`, counted over world/examples).
- Condition: every aggregate of the buyer party has a use in this Order; the security listing and the service provider are present only where a document of the flow does something with them.
- Options: (a) preferred: leave both out of this Order; (b) keep the service provider only if the story gives Castrano a part in receiving or storing the ore.
- Needs decision: no

## Checked and consistent
- Arithmetic: 1800 TNE × 8060 XUF = 14 508 000 (line, LineExtensionAmount, TaxableAmount); 20 % of 14 508 000 = 2 901 600; 14 508 000 + 2 901 600 = 17 409 600 (PayableAmount).
- The Delivery/Despatch/CarrierParty (Ferrano Rail Cargo) fits FCA: under FCA the buyer contracts the carriage and names the carrier to the seller; it is the carrier of 02, 03 and 05.
- DeliveryTerms FCA at "Mine siding, Serravona" matches the Order note, the TEP FromLocation (mine) and the despatch from the mine siding in 04/05.
- RequestedDeliveryPeriod 2026-03-09 to 2026-03-13 contains the transport window of 02/03 (2026-03-10 to 2026-03-13).
- Item description "loose in rail wagons", HS 260111 and CPC 14100 agree with each other and with the item name "Iron ore, lump" and the property "Iron content" 62 %.
- Codes: OrderTypeCode 220 (Order), ISIC 0710 (mining of iron ores) for Serravona, 4912 (freight rail transport) for Ferrano Rail Cargo.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`: a furniture manufacturer buying 1800 t of iron ore a month looked implausible — refuted because the world gives Valdara a steelworks (rail flow: `rail/01-Order.xml` carries the emission factor source "The steelworks' and sawmill's measured energy use of 2025" with reference `VI-LCA-2025`); the code names Valdara's main activity, the ore feeds its steelworks.
- `/Order/cbc:AccountingCostCode` = `3100`: same digits as Valdara's ISIC code, suspected to be a copied classification code — refuted because the pair "3100"/"Raw materials and parts" is Valdara's cost centre used consistently in 12 XML examples, and raw materials is the right cost centre for ore.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: suspected master data without use — refuted because stating the share capital on commercial documents is a legal requirement in several real jurisdictions (e.g. Italy, on which the Urvanian legal forms are modelled; own knowledge), so it can have a reason in an order.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`: road-access conditions in a rail delivery — refuted for this document because the PhysicalLocation is the FCA delivery place (the mine and its siding), which the buyer's carrier has to reach; the condition informs the buyer about the place.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `260111`: an HS code ("for cross border and regulatory (customs and trade statistics) purposes") in a domestic order — refuted because the code also serves statistics and the HS is used for national purposes; it is not a misuse.
- `/Order/cbc:Note[2]` = `Monthly call-off, one train.`: a call-off without a reference to the framework purchase agreement — refuted because the order's purpose does not depend on it; a missing optional reference is not a finding.
