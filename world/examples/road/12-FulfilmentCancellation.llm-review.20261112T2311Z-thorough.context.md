# LLM review: 12-FulfilmentCancellation.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/12-FulfilmentCancellation.xml`, Git blob `e80b06a59cdefc8b05210e1023501fad527985dd` (committed)
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

### road/12#F1 · Medium · Cancellation refers to the despatch advice as well as the receipt advice it cancels
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`
- XPath: `/FulfilmentCancellation/cac:ReceiptDocumentReference/cbc:ID` = `LD-RA-26-0162`
- XPath: `/FulfilmentCancellation/cbc:CancellationNote` = `The recount found the bench reported short; the shortage did not exist.`
- Why: a Fulfilment Cancellation is "A document used to cancel an entire fulfilment document (Despatch Advice or Receipt Advice)", and the document references are how it names the document it cancels. Here it refers to both the despatch advice and the receipt advice, so a receiver can read it as cancelling both; only the receipt advice is meant (the cancellation note is about the count at goods-in, and the despatch advice stays valid: the corrected receipt advice still refers to it, `13-ReceiptAdvice.xml:/ReceiptAdvice/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`).
- Condition: the cancellation names only the document it cancels, the receipt advice `LD-RA-26-0162`; the despatch advice is not referenced as if it were cancelled.
- Options: (a) drop `DespatchDocumentReference` (preferred: the receipt advice already refers to the despatch advice); (b) keep it and say in the note that the despatch advice stands.
- Needs decision: no

### road/12#F2 · Medium · Province given as Region
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/12#F3 · Medium · LocaleCode holds a language code
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/12#F4 · Low · Contacts that do not fit the cancellation of a receipt advice
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the receipt advice is cancelled by Lumeway's goods-in after its recount, not by its customer service in Sales; the despatch supplier's contact is named "Warehouse office" but has a sales customer-service job title and department.
- Condition: Lumeway's contact is the goods-in function that recounted; Castrano's contact has a name, job title and department that agree.
- Options: (a) goods-in for Lumeway, a warehouse job title for Castrano (preferred); (b) drop the job titles and departments that do not fit.
- Needs decision: no

### road/12#F5 · Low · Party master data the cancellation does nothing with
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- Why: a cancellation identifies the cancelled document and the parties to it; the seller's stock-exchange listing and the despatch supplier's shareholder play no part (section 4.8, IND5).
- Condition: the cancellation carries no party data without a use in it.
- Options: drop them (preferred).
- Needs decision: no

## Checked and consistent
- `ReceiptDocumentReference` `LD-RA-26-0162` resolves to `11-ReceiptAdvice.xml`; the cancellation note (the shortage did not exist) matches the corrected receipt advice `13-ReceiptAdvice.xml` (96 benches received); the note "A corrected receipt advice follows" matches its issue two minutes later.
- Order reference `LD-PO-26-0149` resolves to `01-Order.xml`; buyer, seller and despatch supplier are the parties of the cancelled receipt advice.
- Issued 2026-03-26 10:46, after the receipt advice it cancels (2026-03-25 15:40).
