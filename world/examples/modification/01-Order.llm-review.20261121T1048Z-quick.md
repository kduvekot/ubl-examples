# LLM review: 01-Order.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/01-Order.xml`, Git blob `58c2d773cfc4f1c4e019d9b08befe2862bc7ba2e` (committed)
- Last commit changing the example: fd97400c 2026-11-20 O255: wood and modification, story and XML brought into line
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### modification/01#F1 · Medium · The customer's own blank carries the sawmill's code as the seller's item identification
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `MDS-BL-1830`
- Why: Item/SellersItemIdentification is "Identifying information for this item, assigned by the seller". The seller of this order is Tostara Wood Modification (`/Order/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Tostara Wood Modification`), but `MDS-BL-1830` is Marrowdale Sawmill's own code (the MDS- prefix of all the sawmill's numbers, its slat `MDS-SL-1800` in the note; the sub-line note says the blank is "the sawmill's own kiln-dried ash"). The buyer's code belongs in BuyersItemIdentification. The same code sits in `03-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `MDS-BL-1830`, where the sawmill is the despatch party but not a seller.
- Condition: the identifier assigned by Marrowdale Sawmill to the blank is in the element for the buyer's identification (or the identification of the party that assigned it), in this order and in 03-DespatchAdvice.
- Options: (a) preferred: move it to `cac:BuyersItemIdentification`, since the sawmill is the buyer and the owner of the blank; (b) use ManufacturersItemIdentification, the sawmill having sawn and dried the blank (also true, but less direct for an order).
- Needs decision: no

### modification/01#F2 · Low · The buyer's contact is the sawmill's sales office
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Sales coordinator`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact handles the purchase of the processing job; a sales office and sales coordinator sell the sawmill's products. The sawmill has a despatch office (03) and a customs desk (04), so it is not a one-desk business. The same contact is used for Marrowdale as buyer in 02 and 07 and as accounting customer (payer) in 08 and 09 (counted over `*.xml` of the flow by the address `sales@marrowdalesawmill.example`).
- Condition: the contact of Marrowdale Sawmill as buyer is the desk that buys services (purchasing, or production planning that books the kiln slots), or the story says why the sales office does.
- Options: (a) preferred: a purchasing or production-planning contact, since the job is the sawmill's own season stock; (b) keep the sales office and say in the order why (it books the job for its customer Valdara).
- Needs decision: no

## Checked and consistent
- Arithmetic: 96 × 13250 = 1272000 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `1272000`, equal to the line extension and payable totals and to the taxable amount.
- Quantities: 96 bundles × 50 = 4800 slats = `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem/cbc:Quantity` = `4800` blanks = 2 × 2,400 per the note; 02, 06 (48 + 48 bundles), 07 and 08 agree with 96.
- Dates: LatestDeliveryDate 2026-02-06 after the "ready in store on 4 February" of 02 and the AvailabilityDate of 06.
- References: SalesOrderID `TWM-J-2526-014` is repeated in 02, 07 and 08; the contract `TWM-SA-2526-MS` matches 08; the contract is not an example of the flow, which is fine for a season agreement.
- Party identifiers, addresses and electronic addresses of both parties are the same in every example of the flow.

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`: suspected that work on goods physically in Urvania is taxable there — refuted because the customer is a business in Bayvarra (which has a state sales tax, not VAT: 08's customer tax scheme `STT`), and treating B2B work on movable goods as supplied where the customer is established is a legitimate rule; the exemption reason states the world's rule.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]`: tagged `en-XB` here and `en-XU` in 08 for the same text — refuted as a finding: the order is written by the Bayvarran buyer, the invoice by the Urvanian seller; each tags its own variety.
- `/Order/cac:DeliveryTerms/cbc:ID` = `EXW`: delivery terms for a service — refuted: the processed goods are handed back at the processor's plant; the call-off in 07 changes this to FCA.
