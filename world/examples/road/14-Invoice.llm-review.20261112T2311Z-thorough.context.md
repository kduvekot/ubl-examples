# LLM review: 14-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/14-Invoice.xml`, Git blob `1173f55bda6f9ffdefd8413a5ce62500697f236a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### road/14#F1 · Medium · Province given as Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/14#F2 · Medium · LocaleCode holds a language code
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/14#F3 · Low · The buyer's stock-purchase cost code on a freight invoice
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCostCode` is "The buyer's accounting code, applied to the Invoice as a whole". The carrier's invoice for road transport carries the same code and text as Lumeway's purchase order for the benches (`01-Order.xml:/Order/cbc:AccountingCostCode` = `4410`); nothing in the transport request gave Trasvia this code, and freight is a transport cost, not a purchase of stock. It looks copied from the goods order.
- Condition: the freight invoice carries the buyer's accounting code only if the buyer gave it for the transport (e.g. in the transport request), and it is a code for freight.
- Options: (a) drop both (preferred: the transport request has no cost code); (b) add a freight cost code to the transport request and repeat it here.
- Needs decision: no

### road/14#F4 · Low · Freight invoice refers to only one of the two receipt lines
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cbc:LineID` = `1`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `LD-RA-26-0164`
- Why: the invoice bills a full truck load for the whole consignment (`/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0152`), which carried both the benches and the side frames (`13-ReceiptAdvice.xml` lines 1 and 2). Its only goods item points to receipt line 1, the benches, so the reference suggests that the freight is for the benches only.
- Condition: the reference to the receipt covers what the freight is billed for (the whole receipt, or both lines), or is absent.
- Options: (a) refer to the receipt advice as a whole (document reference without line) (preferred: the freight is per consignment); (b) add a goods item for receipt line 2.
- Needs decision: no

### road/14#F5 · Low · Contacts and master data that do not fit an invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Planning desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: the accounting customer's contact receives and checks invoices (accounts payable), not Lumeway's customer service in Sales; the supplier's contact for an invoice is its accounts or billing function, not the operations planning desk. The carrier's operating permit plays no part in billing (section 4.8, IND5).
- Condition: the accounting contacts are the billing functions of both parties; the invoice carries no permit.
- Options: (a) accounts payable / accounts receivable contacts and no permit (preferred); (b) drop the contacts' job titles and departments.
- Needs decision: no

## Checked and consistent
- Waybill `TH-WB-26-0159`, consignment `LD-CS-26-0152` and receipt advice `LD-RA-26-0164` resolve to `08-Waybill.xml`, the consignment there, and the corrected `13-ReceiptAdvice.xml` (not the cancelled one).
- The actual delivery event 2026-03-25 09:40 equals the receipt advice's actual delivery; the invoice is issued afterwards (11:07).
- Accounting customer = buyer = Lumeway, who ordered and pays the transport under FCA (the waybill's collect note says the consignee pays the freight); accounting supplier = seller = carrier = Trasvia.
- The line describes a full truck load priced per kilometre, matching the transport request's service `FTL`.

## Considered and refuted
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TH-WB-26-0159` with ID only: suspected an unclear reference — refuted because the carrier refers to its own consignment note for the transport it bills; no other kind of document has this number.
- `/Invoice/cbc:DefaultLanguageCode` = `en` from an Urvanian carrier: suspected wrong — refuted because the invoice goes to an English-speaking Bayvarran customer and carries the Urvanian renderings with their own `languageID`.

## Outside this review
- Whether 186 km loaded (`/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `186`) fits the route from Ferrano to Marrowdale on the map, with a transit from 2026-03-23 to 2026-03-25, is a question for the cross-flow consistency review.
