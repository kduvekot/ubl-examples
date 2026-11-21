# LLM review: 01-Order.xml

Flow: lpg (9924528384) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/lpg/01-Order.xml`, Git blob `283933755f383e2a11d65182e2b3a00ac376e0d9` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### lpg/01#F1 · Low · The buyer's contact is the water company's customer service
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the Contact of `BuyerCustomerParty` is "the primary contact for this party" in its role as buyer: the person or function who placed the order for 20 t of propane and answers the seller's questions about it. A water company's customer service serves the company's own water and heat customers; it is not who buys fuel for the district heating plant. The same contact is used in every role of this party in the flow (`02-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name`, `03-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name`, `04-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name`), which suggests it is master data rather than a role contact.
- Condition: the buyer's contact is a purchasing (fuel procurement) function of the Coastal State Water Company.
- Options: (a, preferred) a purchasing contact for the order; the consignee, delivery and accounts-payable roles get their own contacts in the other documents; (b) leave out the contact if the party has none for purchasing.
- Needs decision: no

### lpg/01#F2 · Low · Telephone prefix "38522" of Gullhaven numbers overlaps Lumeport's prefix "38"
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38522 68330`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 9310 7518`
- Why: Kelpstone Gas sits in Gullhaven, Northern Territory (postal zone 90540); its number begins with `38522`. Lumeport numbers begin with `38` followed by an eight-digit subscriber number (236 telephone elements in `world/examples/*/*.xml` begin with `+999 2 38 `, counted with `grep -rho --include='*.xml' '<cbc:Telephone>+999 2 [0-9]* '`). An area code "38" and an area code "38522" cannot both exist in a closed numbering plan (codes must be prefix-free, ITU-T E.164 practice; own knowledge), and Gullhaven's postal zone does not suggest a Lumeport-area code. The bank branch code `385220` of the Gullhaven branch in `04-Invoice.xml` follows the same "38522" pattern, so it may be a deliberate scheme I cannot see.
- Condition: telephone numbers of Gullhaven and Lumeport follow one prefix-free numbering plan, and the Gullhaven prefix is not a longer form of the Lumeport one.
- Options: (a, preferred) a Gullhaven area code of its own in the world's numbering plan; (b) confirm that "38" is not an area code but the start of longer ones, and write Lumeport numbers accordingly.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 20 TNE × 560 XBL per 1 TNE = 11200.00; 6.5 % of 11200.00 = 728.00; 11200.00 + 728.00 = 11928.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount`.
- DPU with the delivery location "into the propane storage of the district heating plant" fits a delivery pumped into the buyer's storage; the requested delivery date 2026-06-10 matches the delivery in `02-DespatchAdvice.xml` and `04-Invoice.xml`.
- The item (seller's ID `KG-LPG`, standard ID `KXU19676LPG`, name and description) is the same in all four examples of the flow; `HazardousRiskIndicator` true is right for UN 1965 (own knowledge).
- The parties' identifiers, addresses and electronic addresses agree with the other three examples.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description`: "hydrocarbon gas mixture C" next to the name "Propane, commercial" suspected as a contradiction (UN 1978 is propane) — refuted because commercial propane is commonly classified as UN 1965 Mixture C, and the despatch advice and waybill use UN 1965 consistently.
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent`: a state sales tax in an order — refuted, an anticipated tax total in an order is allowed and the rate matches the invoice.
