# LLM review: 16-ApplicationResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/16-ApplicationResponse.xml`, Git blob `1e7f911b472f7aea92ee35fb380bd4e0c2647589` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/16#F1 · High · Three-way match reported before the goods were received
- XPath: `/ApplicationResponse/cbc:ResponseDate` = `2026-03-25`
- XPath: `/ApplicationResponse/cbc:ResponseTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:Description` = `Three-way match passed.`
- Why: `ResponseDate`/`ResponseTime` are "The date/time on which the information in the response was created". A three-way match compares invoice, order and goods receipt; at 06:12 on 2026-03-25 the goods had not arrived (`11-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:Delivery/cbc:ActualDeliveryTime` = `09:40:00`) and no receipt advice existed (the first is issued at 15:40 that day and reports a bench short, `11-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ShortQuantity` = `1`; the corrected one follows on 2026-03-26). The match cannot have passed when the response says.
- Condition: the response's creation and effective times lie after the receipt against which the invoice was matched (the corrected receipt advice, 2026-03-26 10:48), or the status does not claim a three-way match.
- Options: (a) date the response after the corrected receipt advice, e.g. 2026-03-26 afternoon, and keep "three-way match passed" (preferred: matches the story of the recount); (b) keep the date and replace the status by a two-way match against the order.
- Needs decision: no

### road/16#F2 · Medium · Province given as Region
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/16#F3 · Medium · LocaleCode holds a language code
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/16#F4 · Low · Contacts that do not fit an invoice response
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the response to an invoice comes from the buyer's accounts payable, which matched it, and goes to the seller's accounts receivable; neither Lumeway's customer service in Sales nor Valdara's order desk handles invoices.
- Condition: the contacts are the parties' invoice-handling functions, or absent.
- Options: (a) accounts payable / receivable contacts (preferred); (b) drop the contacts.
- Needs decision: no

### road/16#F5 · Low · Master data and a signature ID the response does nothing with
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ApplicationResponse/cac:Signature/cbc:ID` = `LD-SIG-26-AR`
- Why: the seller's stock-exchange listing and its logistics provider play no part in accepting an invoice (section 4.8, IND5). The signature ID ends in `AR`, the abbreviation of the document type's name (ApplicationResponse), rather than a number in Lumeway's own scheme, and the signature carries nothing but ID and signer.
- Condition: the response carries no party data without a use in it; the signature ID follows the signer's numbering or the signature is absent.
- Options: (a) drop listing and service provider, number the signature after the response ID (preferred); (b) drop the signature.
- Needs decision: no

## Checked and consistent
- The referenced invoice `VI-INV-26-0166` resolves to `15-Invoice.xml`; issuer (Lumeway) and recipient (Valdara) of the response are that invoice's customer and supplier.
- `ResponseCode` `AP` (accepted) on document and line 2, the status `MATCHED` and the notes ("Accepted for payment; line 2 matched the substituted casting") agree; line 2 is the side-frame line that was substituted in `02-OrderResponse.xml`.
- `CustomizationID` for an invoice response fits an application response to an invoice.

## Considered and refuted
- `/ApplicationResponse/cbc:IssueTime` = `12:55:00` later than the response time 06:12: suspected a contradiction — refuted because the definitions allow the information to be created before the document is issued; the problem is the 06:12 itself (F1).
