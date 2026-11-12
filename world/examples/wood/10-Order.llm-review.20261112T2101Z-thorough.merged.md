# LLM review: 10-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/10-Order.xml`, Git blob `9ace6d42e7deb8a74ae8c2e901f90885e501c883` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 83ce5da 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### wood/10#F1 · Medium · A language code in `Language/LocaleCode`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). The value `en` with `listID="ISO 639"` is the language itself and only repeats `Language/ID`, so the element carries a meaning other than its definition (section 6 names "a language code in `LocaleCode`" as Medium). The examples already use locale-like tags (`en-XB`, `en-XU`) in `languageID`. The same element and value occur 362 times in 213 examples (merge recount, `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cbc:LocaleCode` present holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: (a, preferred) drop `LocaleCode` where no locale matters; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47) and name that list in `listID`.
- Needs decision: no
- From: broad/F1, parties/F1, context/F1

### wood/10#F2 · Low · The buyer's contact is its trade sales desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in its role here. Brackenmere as buyer should be reached at purchasing or a buyer; its contact on the purchase order is the trade sales desk in Sales (a customer-service officer), the function that sells Brackenmere's furniture, not the one that buys timber. The parties carry the same contact in every example of the flow whatever their role; `Customer service officer` occurs 395 times in 229 examples (merge recount, `grep -rho --include='*.xml'`). The seller's sales office does fit its role here (parties part).
- Condition: The buyer's contact on the order is a purchasing contact whose name, job title and department agree.
- Options: (a, preferred) role-specific contacts per party in the world, picked per document; (b) drop job title and department where only a functional mailbox is known.
- Needs decision: no
- From: broad/F3, parties/F2, context/F2

### wood/10#F3 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Brackenmere Furniture Ltd and Marrowdale Sawmill Ltd, two different companies, both carry 1996-01-01; the date occurs 271 times in 181 examples (merge recount, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`) for about 25 companies of every kind in the registers of all three countries (parties part), while other dates are specific (Valdara: 1962-04-12). Counter-argument (context part, which refuted it): it plausibly is the date the federal business register of Bayvarra began; but the same date is also given in the Urvanian and Lisavan registers, and nothing in the examples says a register began then, so the merge cannot settle it.
- Condition: Each company's registration date is its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (a, preferred) its own date from the company's history; (b) record a 1996 (re-)registration in the story; (c) leave the date out.
- Needs decision: yes
- From: broad/F4, parties/F3; context considered and refuted it, carried here with its argument

### wood/10#F4 · Low · Ex-works order without a collection date
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `EXW`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Marrowdale Sawmill, timber yard`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- Why: Under EXW the seller delivers by making the goods available at its premises and the buyer collects them. The order names the place (as text only) and the despatch party, but `Delivery` has no `RequestedDeliveryPeriod` and `Despatch` no `RequestedDespatchPeriod`, although the aggregates are present, so it does not say when the 12 m³ are to be ready for collection. No other document of the flow records the collection (`11-Invoice.xml` follows the next morning without delivery data).
- Condition: The order states when the goods are to be made available for collection (date or period).
- Options: (a, preferred) add `Delivery/Despatch/RequestedDespatchPeriod` (or `Delivery/RequestedDeliveryPeriod`, under EXW the same moment); (b) state it in the line's `Delivery`.
- Needs decision: no
- From: broad/F2, logistics/F1

### wood/10#F5 · Low · Customs classification and origin in a domestic sale
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `440799`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- Why: UBL defines `CommodityCode` as "The harmonized international commodity code for cross border and regulatory (customs and trade statistics) purposes". This sale is between two companies in the same state of Bayvarra, collected ex works; no border is crossed, so the condition of the definition is not met, and the country of origin has no use either (no fillers).
- Condition: The domestic order carries only the classification its purpose uses (the CPC classification may stay), or the example states a domestic regulatory use of the HS code.
- Options: (a, preferred) drop the HS code and the origin country from the domestic order (and invoice); (b) keep them if a Bayvarran rule requires them, and say so in the world story.
- Needs decision: no
- From: context/F3

## Checked and consistent
- Arithmetic (recalculated): 12 m³ × 540 XBL/m³ = 6 480.00 = LineExtensionAmount = PayableAmount (broad, context).
- Tax: category E with reason RESALE ("Sale for resale or manufacture") under the Upland State sales tax fits a sale of timber to a furniture manufacturer in the same state (broad, context); whether the exemption is supported by a certificate is a finding of `11-Invoice.xml` (this merge).
- GLN 9523710900008 passes its check digit (`check_ids.py`, re-run by the merge); prefix 952 is reserved by GS1 for demonstrations (own knowledge of the parts) (broad, parties, context).
- `11-Invoice.xml` refers to this order (`BF-PO-26-0637`) and repeats quantity, price and tax (broad, logistics).
- No transport document exists for this order, consistent with EXW (the buyer carries); despatch party = seller, whose yard is the delivery location (logistics, context).
- Quantity 12 `MTQ` with price base quantity 1 `MTQ` fits sawn timber sold by volume; 12 m³ at 650–750 kg/m³ is 7.8–9.0 t, collectable in a few loads; no weight is stated to contradict (logistics).
- Price plausibility: 540 XBL/m³ for boards against about 1 108 XBL/m³ for the planed, cut-to-size slats of the Valdara order (7.2 / 0.006498 m³) (broad).
- Brackenmere is described identically in 10 and 11; identifiers, tax schemes and endpoints follow the country (parties).

## Considered and refuted
- `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty` with the seller as despatch party — refuted because under EXW the seller makes the goods available at its yard (from broad, parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales` as another default contact — refuted because a sales office is the right contact for the seller on an order (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9523710900008` as a real GLN — refuted because GS1 prefix 952 is for demonstrations and the check digit is correct (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` as a placeholder — refuted because it plausibly is the date the federal business register of Bayvarra began (from context). The merge keeps it as F3 with both arguments.

## Changed in the merge
- context's refuted registration-date candidate joined to broad/F4 and parties/F3 as F3, with its argument as counter-argument; "Needs decision: yes" kept.
- context/F2, parties/F2, broad/F3 → F2: limited to the buyer's contact, because the parties part found the seller's contact fitting.
- context/F1, parties/F1, broad/F1 → F1: preferred option is dropping `LocaleCode`.
