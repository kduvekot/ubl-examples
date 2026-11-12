# LLM review: 16-ApplicationResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/16-ApplicationResponse.xml`, Git blob `1e7f911b472f7aea92ee35fb380bd4e0c2647589` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit adfced0 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/16#F1 · High · Three-way match passed before the goods arrived and before any receipt advice
- XPath: `/ApplicationResponse/cbc:ResponseDate` = `2026-03-25`
- XPath: `/ApplicationResponse/cbc:ResponseTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:Description` = `Three-way match passed.`
- XPath: `/ApplicationResponse/cbc:IssueTime` = `12:55:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:Delivery/cbc:ActualDeliveryTime` = `09:40:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:Note` = `Counted and checked at goods-in: one bench short, one box of side frames over.`
- Why: A three-way match compares order, receipt and invoice. The response's information is created on 2026-03-25 at 06:12 ("The date/time on which the information in the response was created"), and the document is issued at 12:55. The goods arrive at 09:40 that day, the first receipt advice is issued at 15:40 and reports one bench short and one box over; it is corrected only on 2026-03-26. At 06:12 there was no receipt to match, and when a receipt existed it did not match.
- Condition: The invoice response is created and issued after the receipt it relies on, and its matching result agrees with that receipt (e.g. after `13-ReceiptAdvice.xml`, 2026-03-26 10:48, with a note on the oversupplied box).
- Options: (a, preferred) move the response after the corrected receipt advice (2026-03-26 after 10:48); (b) make it a two-way match (order and invoice) without the receipt.
- Needs decision: no

### road/16#F2 · Medium · Language code in LocaleCode
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/16#F3 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/ApplicationResponse/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/16#F4 · Medium · Province in Region instead of CountrySubentity
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/16#F5 · Low · Sender contact is the customer service desk
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: An invoice response comes from accounts payable; Lumeway's contact is its `Customer service` desk in `Sales`, which handles Lumeway's own customers.
- Condition: The sender's contact is an accounts payable contact.
- Options: (a, preferred) give Lumeway an accounts payable contact; (b) omit JobTitle/Department.
- Needs decision: no

### road/16#F6 · Low · Document reference with only an ID
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `VI-INV-26-0166`
- Why: A document reference that carries only an ID must say what it refers to where that is not obvious (no `DocumentTypeCode` or `DocumentType`, no issue date). The response's whole purpose is the referenced invoice; the reference does not say it is an invoice (the remittance advice in the same flow does, with a document type code).
- Condition: The reference states the kind of document it refers to (type code or type text).
- Options: (a, preferred) add `DocumentTypeCode` from the world's document type list (as the remittance advice does); (b) add `DocumentType` as text.
- Needs decision: no

### road/16#F7 · Low · Issuer and recipient of the responded-to document look swapped
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:IssuerParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:RecipientParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `VI-INV-26-0166`
- Why: Inside `DocumentResponse`, `IssuerParty` is "The Party who issues this Document" and `RecipientParty` "The Party who is the intended recipient of this Document", where the document is the one the response is about (the referenced invoice VI-INV-26-0166). The invoice is issued by Valdara to Lumeway, but the response names Lumeway as issuer and Valdara as recipient, i.e. the parties of the response itself, which `SenderParty` and `ReceiverParty` already give. The definition is ambiguous enough that the reading must be confirmed.
- Condition: Issuer and recipient in the document response describe the referenced invoice (issuer Valdara, recipient Lumeway), or are absent.
- Options: (a, preferred) swap them or remove them, since sender and receiver already identify the response's parties; (b) keep them if the world's billing profile defines them as the response's parties.
- Needs decision: yes

## Checked and consistent
- `DocumentReference` VI-INV-26-0166 resolves to `15-Invoice.xml`; response code AP (accepted) on the document and line 2; the note on line 2 agrees with the substitution in `02-OrderResponse.xml`.
