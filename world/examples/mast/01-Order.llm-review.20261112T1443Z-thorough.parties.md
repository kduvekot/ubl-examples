# LLM review: 01-Order.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/01-Order.xml`, Git blob `a15e986388f03b87c705a9a004911992c536b517` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/01#F1 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "a code signifying the locale in which this language is used". A locale is a language as used in a region (the examples themselves use `en-XB`, `en-XL`, `en-XU` as `languageID`); `en` with `listID="ISO 639"` is the language code again, repeating `Language/ID`. The same value occurs in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">' world/examples | wc -l`), always `en`.
- Condition: `LocaleCode` is absent, or holds a locale (language and country/region) from a locale list, with a matching `listID`.
- Options: (a, preferred) a locale such as `en-XB` with a listID naming BCP 47 / the world's locale list, since Saltmere uses Bayvarran English; (b) drop `LocaleCode`.
- Needs decision: no

### mast/01#F2 · Low · Buyer's and seller's contacts look swapped
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: In an order the buyer's contact is the one who buys and the seller's contact the one who sells. Here the buyer, Selanu Telecom, is represented by its sales "Business accounts" desk (which serves Selanu Telecom's own business customers), and the seller, Saltmere Engineering, by a "Bids office" staffed by a procurement officer of the procurement department. Each contact fits the opposite role. The same contacts are used for these parties throughout the flow (02–05).
- Condition: the buyer's contact is a purchasing person or desk of Selanu Telecom, and the seller's contact a sales or order-handling person or desk of Saltmere Engineering.
- Options: (a, preferred) give each party a contact for its role in the document (purchasing for Selanu Telecom as buyer; sales/order desk for Saltmere as seller); (b) if the "Bids office" is Saltmere's tendering (sales) office, make its job title and department say so.
- Needs decision: no

### mast/01#F3 · Low · Registration date 1 January 1996
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `1996-01-01` is the registration date of about 25 different companies across the examples (Selanu Telecom, Bayforth Forwarding, Kelaro Air Cargo, Velumi Trading, Brackenmere Furniture, …), in 181 examples (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`). A shared New Year's Day date for so many companies reads as a default value, not as each company's own history (IND5/IND6: no fillers).
- Condition: each company's registration date is its own (from the company's history in the world), or absent.
- Options: (a, preferred) give each company the date of its history; (b) drop the date where the world has none.
- Needs decision: yes (company histories)

### mast/01#F4 · Low · Delivery place named by the company, not the place
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu Telecom, mast site`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Selanu Telecom`
- Why: The CPT place of the delivery terms is described only by the buyer's name and "mast site"; Selanu Telecom presumably has more than one mast, and neither the location nor the DeliveryParty carries an address or identifier. A location's name or description should be the place.
- Condition: the delivery location identifies the place (which mast site, with its address or identifier).
- Options: (a, preferred) give the location the mast site's name and address; (b) if delivery is to the business address on Mast Hill Road, say so.
- Needs decision: no

### mast/01#F5 · Low · The island's telecom operator described as a small entity
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: Selanu Telecom (ISIC 6110, wired telecommunications) runs the island's mast network and orders back-up power for it; a network operator is usually at least medium-sized. In a small island economy it could still be small, so this needs a decision.
- Condition: the size code matches the company's description in the world.
- Options: (a) `MEDIUM` or `LARGE` if the world describes it as the island's operator; (b) keep `SMALL` if the world says so.
- Needs decision: yes

## Checked and consistent
- Parties: Selanu Telecom `IC42407` (XL register) is BuyerCustomerParty and DeliveryParty; Saltmere Engineering `20410685` (XB register) SellerSupplierParty; the same identifiers, names, address IDs, tax ID, contacts and endpoints are used in 02–05.
- Saltmere's tax registration: state sales tax (`STT`) of Upland State, `TaxLevelCode` STATE, matching its address in Upland State (`XB-UL`).

## Considered and refuted
- `/Order/cac:SellerSupplierParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 4290 (construction of other civil engineering projects) for a supplier of batteries and detectors — refuted because an engineering firm that builds and equips telecom masts supplies their equipment; the class fits.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName`: no legal form for Saltmere Engineering, unlike the other companies — refuted because a firm without a company suffix (a partnership or sole trader) is a legitimate reading, and its name is the same in every example.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress`: no PostalZone — refuted because no Lisavan address in the examples has one.
