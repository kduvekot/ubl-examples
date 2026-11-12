# LLM review: 14-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/14-Invoice.xml`, Git blob `1173f55bda6f9ffdefd8413a5ce62500697f236a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit adfced0 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/14#F1 · High · Invoice refers to a receipt advice issued the day after the invoice
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-25`
- XPath: `/Invoice/cbc:IssueTime` = `11:07:00`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `LD-RA-26-0164`
- XPath: `13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueDate` = `2026-03-26`
- XPath: `13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `10:48:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00`
- Why: The freight invoice is issued on 2026-03-25 at 11:07 and refers to receipt advice LD-RA-26-0164, which Lumeway issues only on 2026-03-26 at 10:48 (the corrected advice after the cancellation). At 11:07 on 2026-03-25 no receipt advice existed at all; even the first one (`11-ReceiptAdvice.xml`) is issued at 15:40 that day. A document cannot refer to one that is issued later.
- Condition: Every document the invoice refers to exists at the invoice's issue time: either the invoice is issued after LD-RA-26-0164, or it refers to no receipt advice (e.g. only to the waybill and the delivery event).
- Options: (a, preferred) issue the freight invoice after 2026-03-26 10:48, keeping the reference; (b) drop the receipt line reference and rely on the waybill and the actual delivery event.
- Needs decision: no

### road/14#F2 · Medium · Province in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/14#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/14#F4 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/14#F5 · Low · Document reference with only an ID
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TH-WB-26-0159`
- Why: A document reference that carries only an ID must say what it refers to where that is not obvious (no `DocumentTypeCode` or `DocumentType`, no issue date). TH-WB-26-0159 is the CMR waybill (`08-Waybill.xml`); an untyped additional document on an invoice is not recognisable as the transport document the freight is billed for.
- Condition: The reference states the kind of document it refers to (type code or type text).
- Options: (a, preferred) add `DocumentTypeCode` from the world's document type list (as the remittance advice does); (b) add `DocumentType` as text.
- Needs decision: no

### road/14#F6 · Low · Contacts that do not fit the role
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Planning desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: On an invoice the supplier's contact answers billing questions and the customer's contact receives and checks invoices (accounts payable). Trasvia gives its `Planning desk` in `Operations`; Lumeway its `Customer service` desk in `Sales`.
- Condition: The accounting parties' contacts are billing/accounts contacts.
- Options: (a, preferred) give both parties accounts contacts; (b) omit JobTitle/Department.
- Needs decision: no

### road/14#F7 · Low · Freight for the whole consignment linked to the bench line only
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cbc:LineID` = `1`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `186`
- Why: The invoice bills the full truck load (186 km loaded) for the whole consignment of benches and side frames, but its goods item refers only to receipt line 1 (the benches); the side frames on receipt line 2 travelled on the same truck.
- Condition: The receipt reference covers the whole consignment (both lines, or the receipt advice as a whole), or is absent.
- Options: (a, preferred) reference the receipt advice without a line, or both lines; (b) drop the receipt line reference.
- Needs decision: no

## Checked and consistent
- Arithmetic: 186 km × 240.5 = 44 733 XUF = line amount = taxable amount = payable amount; tax 0; settlement discount 2 % of 44 733 = 894.66, rounded 895; settlement period 2026-03-25 to 2026-04-04 (10 days) and due date 2026-04-24 (30 days) match the note.
- Payment reference RF49THINV260165 (ISO 11649) and the IBAN-like account XU32… pass their check digits (`check_ids.py`); the account belongs to the same branch 03510-41600 as in the account number.
- Parties: supplier Trasvia, customer Lumeway, consistent with the transport request's bill-to party and the FCA freight terms; actual delivery 2026-03-25 09:40 = `11-ReceiptAdvice.xml`.
- Distance and fuel: 186 km against 61 l diesel in the waybill is about 33 l/100 km, plausible (own knowledge).

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O` with the reason "Service to a business established outside Urvania" — refuted as a finding: under the general B2B rule the place of supply of a transport service to a foreign business is the customer's country, so the service is outside the scope of Urvanian VAT; whether international freight should instead be zero-rated (exempt with credit) is a choice of the world's tax rules, which the examples do not settle.
- `/Invoice/cbc:AccountingCost` = `Stock purchases` for a freight invoice — refuted: inbound freight is part of the cost of stock (landed cost), so the buyer's stock account is a legitimate choice.
