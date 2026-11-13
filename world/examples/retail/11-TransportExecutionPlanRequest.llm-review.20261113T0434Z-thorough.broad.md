# LLM review: 11-TransportExecutionPlanRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/11-TransportExecutionPlanRequest.xml`, Git blob `43f5b79071571e3db0185c905bab61bd7c25ec4c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### retail/11#F1 · Medium · Transport request that does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `996`
- Why: a Transport Execution Plan Request asks a transport service provider to plan a transport; the provider needs to know what it carries. The consignment gives only its ID, a gross weight and the consignee and consignor: no goods description, no number of pallets or packages, no dimensions or loading metres. That the load is six pallets of four park benches (24 benches, 1.8 m long) is only known from 12-DespatchAdvice, which Bayforth does not receive. The full truck load service (`FTL`) does not replace it.
- Condition: the request states what is carried: at least the number and type of handling units (six pallets) and a goods description, with the gross weight already given.
- Options: (a, preferred) add the handling units (e.g. `TotalTransportHandlingUnitQuantity` and a `TransportHandlingUnit` or `GoodsItem` with description and package count) to the consignment; (b) a consignment-level description and package quantity at least.
- Needs decision: no

### retail/11#F2 · Medium · Language codes in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/11#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- Why: In the pick-up location (`FromLocation`) the gate is useful information for the truck, but still not a street name. `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/11#F4 · Low · Locations named after the companies, and the delivery point of the order not used
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Lumeway Distribution`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Brightmarket Stores`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: a `Location` name is the place, not the company. The delivery place of this transport is the store's goods-in of the garden department, which the order identifies by GLN `9522610900019` and calls "Goods-in, garden department"; the request sends the truck to the store's postal address only. The pick-up place is Lumeway's distribution centre (as the note says), not "Lumeway Distribution".
- Condition: from and to locations name the places (distribution centre, goods-in), and the delivery place carries the identifier the order uses for it.
- Options: (a, preferred) names such as "Distribution centre Marrowdale" and "Goods-in, garden department", with the goods-in GLN on the to-location; (b) keep the names and add the GLN.
- Needs decision: no

### retail/11#F5 · Low · Contacts that do not fit the transport roles
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Operations`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: in a transport request the transport user's contact is the one who arranges transport, the provider's contact the one who plans it, and the consignee's contact the one who receives the goods. Here Lumeway is represented by its customer service in sales, Bayforth by its "Export desk" for a domestic haul within Bayvarra (Marrowdale to Lumeport), and the consignee Brightmarket by its buying office, whose job title and department (customer service officer, sales) also contradict its name. The order 08 names a goods-in contact for Brightmarket (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`) and a dispatch office for Lumeway (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`). The same party contacts are used in every retail example.
- Condition: each party's contact in this document fits its role in the transport, and name, job title and department agree with each other.
- Options: (a, preferred) Lumeway's dispatch office, Bayforth's road or domestic operations desk, Brightmarket's goods-in; (b) drop the contacts where they are only master data.
- Needs decision: no

## Checked and consistent
- Parties: Lumeway is sender, transport user and bill-to party (it sells delivered duty paid, so it pays the carriage, consistent with 02-Catalogue's trading terms and 08-Order's `DDP`); Bayforth is receiver and transport service provider; consignor and consignee are Lumeway and Brightmarket.
- Dates: issued 2026-04-25, response deadline 2026-04-26, service from 2026-04-29 to 2026-05-02; 12-DespatchAdvice, 13-Waybill and 15-TransportationStatus are all dated 2026-04-29, and 17-ReceiptAdvice receives on 2026-04-30, within the service period.
- Consignment `LD-CS-26-0228` and gross weight 996 kg are the same in 12-DespatchAdvice and 13-Waybill.
- From and to addresses equal the parties' postal addresses as described in every retail example.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: suspected implausible for six pallets of about one tonne — refuted: a dedicated truck for a promotion delivery is a commercial choice, and the despatch advice shows a 13.6 m trailer was used.
- `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`: suspected filler — refuted: an explicit "no special status" (UBL default code list) is a statement, not a filler.
