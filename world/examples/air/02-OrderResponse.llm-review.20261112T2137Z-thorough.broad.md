# LLM review: 02-OrderResponse.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/02-OrderResponse.xml`, Git blob `7b81c0b8231d36020cf1c1f9d1fabe0d729ce771` (committed)
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

### air/02#F1 · High · Line 1 of the response is the bench line of the referenced order
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cbc:Quantity` = `8`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: The response refers to order `VT-PO-26-0127` and to its change `VT-OC-26-0320`. In the order, line 1 is 96 park benches, and the side frames are line 2. The response accepts "line 1" with 8 side frames, which says the bench line was changed into 8 frames. The response repeats the line-ID problem of `01-OrderChange.xml` (its F1) and cannot be matched to the order lines without ambiguity.
- Condition: the accepted line carries the same line identification as the changed or added line of the order change, and that identification does not collide with a different line of `VT-PO-26-0127`.
- Options: follow the fix of 01 (a new line 3 for the added frames is preferred there) and use the same ID here.
- Needs decision: no

### air/02#F2 · Medium · LocaleCode holds a language code
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code that only repeats Language/ID. The same pattern occurs in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639"'`).
- Condition: LocaleCode holds a locale (language and region) from a locale list, or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it (preferred unless the locale is used).
- Needs decision: no

### air/02#F3 · Low · A validity period on an acceptance
- XPath: `/OrderResponse/cac:ValidityPeriod/cbc:EndDate` = `2026-05-13`
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `AP`
- Why: ValidityPeriod is "The period for which the Order Response is valid". A validity period makes sense for a counter-offer, which lapses if the buyer does not accept. This response is a plain acceptance (AP), and the contract it closes does not expire on 13 May. If the date means "valid only if the cargo makes the booked flight", the document does not say so.
- Condition: the ValidityPeriod is absent, or the document states what lapses on that date.
- Options: (a) remove it (preferred); (b) explain it in the note (e.g. tied to the flight booking).
- Needs decision: no

### air/02#F4 · Low · The forwarder's quote is referenced by ID only and does not exist in the flow
- XPath: `/OrderResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-QUOTE-AIR-26-0611`
- Why: The reference has neither DocumentTypeCode nor DocumentDescription, and no example has this ID (`grep -rn --include='*.xml' BF-QUOTE world/examples` finds only this one). It is Bayforth's quote to Lumeway for the air freight. Under CPT the seller pays the freight, so this quote concerns the buyer only if the story says why it is passed on (e.g. as proof of booking).
- Condition: the reference says what kind of document it is, or it is absent.
- Options: (a) add DocumentTypeCode/DocumentDescription ("Forwarder's quotation for the air freight"); (b) remove it, since the buyer does not act on the seller's freight quote (preferred).
- Needs decision: no

### air/02#F5 · Low · The buyer's contact does not fit its role
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: A buyer's "Purchasing" contact is a customer service officer in Sales. Name, title and department contradict each other. The same combination occurs in 52 example files.
- Condition: job title and department fit the name and the buyer role.
- Options: e.g. buyer / Purchasing.
- Needs decision: no

## Checked and consistent
- `VT-PO-26-0127` resolves to `sea/05-Order.xml` and `VT-OC-26-0320` to `01-OrderChange.xml`. Seller, buyer and accounting codes (`500`, "Stock for municipal projects") match both.
- Net weight 76 kg and net volume 0.42 m³ are the same as `03-ForwardingInstructions.xml` (consignment) and agree with each other for 8 iron castings (9.5 kg each; see 03 for the packaging).
- The CPT line delivery term agrees with `01-OrderChange.xml`. The forwarder Bayforth Forwarding (`20411644`) is the same party as in 03, 04 and 10.
- GLN 9520610900008: check digit OK.

## Considered and refuted
- `/OrderResponse/cbc:Note` = `Accepted: the frames fly on the morning flight; the forwarder is booked.`: suspected to contradict `03-ForwardingInstructions.xml`, issued three hours later and asking "Please confirm the booking". Refuted because a booking made on the forwarder's quote and then confirmed against the written instructions is normal practice.
- `/OrderResponse/cbc:AccountingCostCode` = `500`: the buyer's accounting code in a seller's document. Refuted because echoing the buyer's cost code lets the buyer book the response, and the value matches the order.
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`: tagged `en-XB` here but `en-XL` in `01-OrderChange.xml`. Refuted because the tag consistently follows the English of the issuing party across the examples (Lumeway's documents use `en-XB`, island issuers `en-XL`). That is a legitimate reading of languageID, since the text is written in the sender's English.

## Outside this review
- Timeline: "the frames fly on the morning flight" (12 May) against the flight on 14 May 07:00 in `04-Waybill.xml` and the missed flight in `07-FulfilmentCancellation.xml`: which morning is meant is a question for the cross-flow timeline review.
