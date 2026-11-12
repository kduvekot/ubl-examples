# LLM review: 12-FulfilmentCancellation.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/12-FulfilmentCancellation.xml`, Git blob `e80b06a59cdefc8b05210e1023501fad527985dd` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5c0d61b 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/12#F1 · Medium · Language code in LocaleCode
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/12#F2 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/12#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/12#F4 · Low · Contacts that do not fit the role
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The cancellation of a receipt advice comes from the receiving warehouse; Lumeway's contact is its `Customer service` desk in `Sales`. Castrano's contact is named `Warehouse office` but titled `Customer service officer` in `Sales`, which contradicts its name.
- Condition: Contact name, job title and department agree with each other and with the role (goods-in for the receiver, warehouse for the despatcher).
- Options: (a, preferred) give Lumeway a goods-in contact and Castrano a warehouse title and department; (b) omit JobTitle/Department.
- Needs decision: no

## Checked and consistent
- `ReceiptDocumentReference` LD-RA-26-0162 resolves to `11-ReceiptAdvice.xml`; despatch CL-DA-26-0153 and order LD-PO-26-0149 resolve to `04` and `01`.
- Issued 2026-03-26 10:46, after the receipt advice it cancels (2026-03-25 15:40) and two minutes before the corrected receipt advice `13-ReceiptAdvice.xml` (10:48), as the note announces.
- The cancellation note (the reported shortage did not exist) agrees with `13-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedQuantity` = `96`.

## Considered and refuted
- `/FulfilmentCancellation/cbc:ID` = `LD-DOC-26-0163`: a generic `DOC` prefix looked unlike the other Lumeway numbers — refuted: any sender-assigned identifier is valid, and the running number fits the flow.
