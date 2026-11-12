# LLM review: 01-OrderChange.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/01-OrderChange.xml`, Git blob `16f89e4161a30f6558c8105aa5b37873619d1f2c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/01#F1 · High · The changed line reuses line ID 1, which is the bench line of the order being changed
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cbc:ID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cbc:ID` = `2`
- Why: An Order Change carries "(changed) Order Lines" of the Order it references (`VT-PO-26-0127`). In that order, line 1 is 96 park benches and line 2 is 12 side frames. This change carries a line 1 holding 8 side frames, so it reads as a change of the bench line into 8 side frames. The note says eight side frames are *added* ("the rest of the order is unchanged"). That fits neither line 1 (benches) nor a change of line 2, which would show a quantity of 20.
- Condition: the change line can be matched to the order without ambiguity: either a new line ID not used in `VT-PO-26-0127` (e.g. 3) for the added frames, or line 2 with its new total quantity; the totals (F2) and the follow-up documents (02, 06, 08) use the same line identification.
- Options: (a) new line ID 3 for the added air frames (preferred: matches the note, and the sea part of line 2 stays as it was); (b) change line 2 to 20 frames, with a split delivery.
- Needs decision: no

### air/01#F2 · Medium · The anticipated total is the new order total, not the amount of change, and the document's line does not add up to it
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `51200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `51200.00`
- XPath: `/OrderChange/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `51200.00`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `512.00`
- XPath: `sea/05-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`
- Why: UBL defines OrderChange/AnticipatedMonetaryTotal as "The amount of change to the total cost of the order anticipated by the buyer". 51200.00 = 50688.00 (the original order) + 512.00 (8 × 64), so it is the new total, not the change. The only line in this document is 512.00, so neither the line extension total nor the taxable amount can be recalculated from the document's lines.
- Condition: the AnticipatedMonetaryTotal and TaxSubtotal amounts equal the sum of the lines this Order Change carries (512.00), or the document carries every line of the changed order so that the totals add up.
- Options: (a) totals of 512.00, the amount of change, as the definition says (preferred); (b) repeat the unchanged lines so that 51200.00 adds up.
- Needs decision: no

### air/01#F3 · Medium · LocaleCode holds a language code
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used", i.e. a language plus a region (e.g. en-XB). The value `en` with listID ISO 639 only repeats the language already in Language/ID. The same `LocaleCode listID="ISO 639"` occurs in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: LocaleCode holds a locale (language and region) from a list of locales, or is absent.
- Options: (a) a locale such as `en-XB` with a suitable listID (preferred, if the party's locale matters); (b) remove LocaleCode.
- Needs decision: no

### air/01#F4 · Low · Contacts do not fit their roles
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact is called "Purchasing" but is a customer service officer in Sales. The receiving warehouse's "Goods inwards" contact is also a customer service officer in Sales. Name, job title and department contradict each other, and neither title fits the role (buying; receiving goods). The pair Purchasing / Customer service officer occurs in 52 example files (counted with `grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'`, all followed by this title and department).
- Condition: each contact's job title and department fit its name and the party's role in this document.
- Options: e.g. Purchasing → buyer / Purchasing; Goods inwards → goods receiving clerk / Warehouse.
- Needs decision: no

### air/01#F5 · Low · Two Delivery Terms for one change; the document-level CPT reads as applying to the whole order
- XPath: `/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:SpecialTerms` = `The rest of the order stays CIF by sea.`
- Why: The same CPT term appears twice. The document-level set has the place and the delivery-level set has the remark. The document-level DeliveryTerms is "A set of delivery terms associated with this document", so CPT reads as replacing the order's CIF terms (`sea/05-Order.xml`), which the special terms then contradict. The CPT term only concerns the added air frames.
- Condition: CPT and its place are stated once, where they apply only to the air delivery, and the remark about CIF for the rest is next to it.
- Options: (a) one DeliveryTerms on the Delivery (or on the line) with place and remark (preferred); (b) keep the document level, without the duplicate.
- Needs decision: no

### air/01#F6 · Low · The buyer names the air carrier before the seller has booked the transport
- XPath: `/OrderChange/cac:Delivery/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: Under CPT the seller contracts the carriage. In this flow the seller books a forwarder (`02-OrderResponse.xml` refers to a forwarder quote and names Bayforth Forwarding), and the forwarder books Kelaro (`04-Waybill.xml`). A buyer's order change that names the airline a day earlier needs a reason in the story (the buyer asks for this airline), or the carrier does not belong here.
- Condition: the CarrierParty in the order change has a stated reason (a buyer's carrier request) or is absent.
- Options: (a) remove it (preferred: the seller chooses the carrier under CPT); (b) keep it and state the buyer's request in a note or SpecialTerms.
- Needs decision: yes

### air/01#F7 · Low · SalesOrderID is the seller's number of the original order, not of the Order Change
- XPath: `/OrderChange/cbc:SalesOrderID` = `LD-SO-26-0123`
- XPath: `sea/06-OrderResponse.xml:/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`
- Why: OrderChange/SalesOrderID is defined as "An identifier for the Order Change, assigned by the seller". The buyer issues this document, so the seller cannot have numbered the change yet. The value is the seller's number for the original order (`sea/06-OrderResponse.xml`). Quoting the seller's order number is a legitimate business need, but the definition does not name it.
- Condition: SalesOrderID holds a seller-assigned identifier of this Order Change, or the seller's order number is carried where UBL means it (e.g. a reference to the order).
- Options: (a) move the value to `OrderReference/SalesOrderID` ("An identifier for this order reference, assigned by the seller"), which is exactly what it is (preferred); (b) keep it and accept the reading "seller's number of the order being changed".
- Needs decision: no

## Checked and consistent
- References: `VT-PO-26-0127` is `sea/05-Order.xml`, an Order with the same buyer, seller, originator, beneficiary, CustomerReference, AccountingCostCode/AccountingCost and currency; `LD-DAG-26-0125` is `sea/03-DigitalAgreement.xml` between Lumeway and Velumi.
- Line: 8 × 64 = 512.00; price, item identifiers (GTIN 9520610000029, check digit OK), seller's and manufacturer's item IDs, HS and CPC codes and manufacturer are the same as order line 2 of `sea/05-Order.xml`.
- 50688.00 + 512.00 = 51200.00 (see F2 for what that sum means).
- Tax: category G with exemption EXP fits an export from Bayvarra to Lisavu and matches the original order.
- GLN 9520610900008: check digit OK; the 952 prefix is GS1's range for demonstrations, so it cannot be mistaken for a real GLN.
- Parties: buyer, seller and the Nalevi delivery party have the same identifiers, addresses and legal data as in `sea/05-Order.xml`.

## Considered and refuted
- `/OrderChange/cac:Delivery/cac:NotifyParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: notify party equal to the delivery party, suspected redundant. Refuted because notifying the receiving warehouse of the air arrival is a legitimate role, and the airline's arrival notice goes to that party.
- `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`: an Urvanian national tariff code in a trade from Bayvarra to Lisavu. Refuted because it is the only national tariff list in the examples (61 occurrences, all `XU:codelist:CustomsTariffCode`, counted over `*.xml`), it is the item's country of origin, and the original order carries the same classification.
- `/OrderChange/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`: originator and beneficiary in an order change. Refuted because the original order has them too, and the change concerns the same project ("Harbour parks Selanu").
