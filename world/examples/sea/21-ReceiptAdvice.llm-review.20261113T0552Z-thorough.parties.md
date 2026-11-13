# LLM review: 21-ReceiptAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/21-ReceiptAdvice.xml`, Git blob `11d4ca627fbbda4c36b71ae5b97e59794bcbb9ae` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/21#F1 · Medium · A gate in the despatch party's AdditionalStreetName
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no place in the postal address of the party a receipt advice is sent to. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/21#F2 · Medium · A language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/21#F3 · Low · Contact name, job title and department disagree for the issuer and the buyer
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The receipt advice is issued by the warehouse's goods-in ("Counted and checked at goods-in"), and its contact is named Goods inwards, but job title and department make it a customer service officer in Sales. The buyer's contact is named Purchasing, but is again a customer service officer in Sales. Name, title and department of each contact contradict each other.
- Condition: Each contact's name, job title and department describe the same function: goods receipt at the warehouse, purchasing at the buyer.
- Options: (a) matching job titles and departments (preferred); (b) drop job title and department and keep the functional name.
- Needs decision: no

### sea/21#F4 · Low · Tax registration and share capital of the despatch party in a receipt advice
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The warehouse reports quantities received and rejected; it does nothing with Lumeway's sales-tax registration or its share capital. They are copied from master data (section 4.8 of the review rules); the other parties of the receipt advice carry no tax scheme.
- Condition: The despatch party carries only the party data a receipt advice uses.
- Options: (a) drop `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator` from the despatch party (preferred); (b) keep them with a reason.
- Needs decision: no

## Checked and consistent
- Issuer and signatory are Nalevi Warehousing (`IC41722`), the delivery recipient of the despatch advice `20-DespatchAdvice.xml` and the delivery party of the order `05-Order.xml`; despatch party and seller are Lumeway Distribution (`20410274`), buyer Velumi Trading (`IC41859`), as in both.
- Nalevi's and Velumi's Lisavu addresses and legal forms carry `en-XL` and the Lisavan renderings, like the order and the other examples issued on the island; the despatch advice differs (reviewed there).
- Lumeway's GLN and the items' GTINs pass their check digits (check_ids.py).
- Industry classifications fit: 5210 warehousing, 4649 wholesale.

## Considered and refuted
- `/ReceiptAdvice/cbc:RejectActionCode`: the warehouse, not the buyer, asking the seller for a credit — refuted because `RejectActionCode` is the action "the delivery party wishes the despatch party to take", the delivery party is the warehouse, and it reports for the buyer whose goods it receives; the credit note `26-CreditNote.xml` is then issued to the buyer.
- `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: the buyer's customs trader number in a receipt advice — refuted because the goods were imported for that trader, and the warehouse receives them after clearance.
