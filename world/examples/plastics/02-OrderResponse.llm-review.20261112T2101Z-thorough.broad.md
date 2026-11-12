# LLM review: 02-OrderResponse.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/02-OrderResponse.xml`, Git blob `ed508cac8f8d97787b90685b12c76dfda6ffaaa6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/02#F1 · Medium · Province of the seller's address in Region
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country", i.e. `CountrySubentity` (+ `CountrySubentityCode`), as the Bayvarran addresses of the same document do (`/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). The value has no `languageID`, unlike the other parts of the address. 219 occurrences in the world (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: no Urvanian province is carried in `cbc:Region`; it is in `cbc:CountrySubentity` (and its code, where a list exists).
- Options: (a) move the province to `CountrySubentity` (preferred, matches the definition and the Bayvarran addresses); (b) keep `Region` only if Ferrano is an economic region and not an administrative division, documented in the world data.
- Needs decision: no

### plastics/02#F2 · Medium · Language code in LocaleCode
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (with `listID` `ISO 639`) is a language, already given in `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`. The buyer's locale would be Bayvarran English (`en-XB`). 362 occurrences in 213 examples (`grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples`).
- Condition: `LocaleCode` carries a locale from a locale list named in `listID`, or is absent.
- Options: (a) `en-XB` with a BCP 47/CLDR list (preferred); (b) drop it.
- Needs decision: no

### plastics/02#F3 · Low · Buyer's contact is a sales/customer-service desk
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact, who receives the acceptance of its order, should be the buying function; a customer-service officer in Sales is the seller-side function. Same contact as in `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`.
- Condition: the buyer's contact is a purchasing contact, consistent across the ordering documents.
- Options: (a) a purchasing contact for Rivermouth as buyer (preferred); (b) a neutral general contact.
- Needs decision: no

### plastics/02#F4 · Low · Buyer's bank account in an Order Response
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: The Order Response only accepts the order (`/OrderResponse/cbc:OrderResponseCode` = `AP`); no payment is stated, so the buyer's account is master data the document does nothing with (section 4.8).
- Condition: no buyer account in the Order Response unless the response says something about payment that uses it.
- Options: (a) remove it (preferred); (b) keep it only with payment information that uses it.
- Needs decision: no

### plastics/02#F5 · Low · Both parties registered on 1 January 1996
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Companies in two different countries' registers share the same registration date, the most frequent one in the world (271 occurrences, `grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*' world/examples | sort | uniq -c`); it looks like a default value (IND5/IND6), unless the story explains it.
- Condition: each registration date is the company's own, or the shared date is explained by the world's history.
- Options: (a) individual dates (preferred); (b) document a general re-registration on that date.
- Needs decision: yes

## Checked and consistent
- `/OrderResponse/cac:OrderReference/cbc:ID` = `RP-PO-26-0882` resolves to `01-Order.xml`; buyer and seller are the same parties with the same identifiers; the response is issued the day after the order.
- Seller description: the same as in the Order, except that the texts are tagged `en-XU` (the seller's own English) instead of `en-XB` (the buyer's) and the legal form and certificate type are also given in `qau`; that follows the sender's languages and is not a contradiction.

## Considered and refuted
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode`: the waste-recovery authorisation looked copied into the response — refuted for the ordering documents: it backs the recycled-content claim of the ordered goods (see `01-Order.xml`).
- `/OrderResponse/cbc:OrderResponseCode`: an acceptance without lines or delivery date — refuted: `AP` accepts the order as placed, so no lines need to be repeated.

## Outside this review
- The transport request `03-TransportExecutionPlanRequest.xml` is issued on 2026-04-14 at 09:57, before this acceptance (15:39 the same day): the seller books the barge before it accepts the order. This is a timeline question across documents.
