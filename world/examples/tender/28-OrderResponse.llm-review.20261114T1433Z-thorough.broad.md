# LLM review: 28-OrderResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/28-OrderResponse.xml`, Git blob `3ed78b3450611e60a961e71c98db29842ff2963f` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 1ae0e51 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/28#F1 · High · Reference to an order that does not exist
- XPath: `/OrderResponse/cac:OrderDocumentReference/cbc:ID` = `PWD-PO-26-0212`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: OrderDocumentReference is "A reference to an Order other than the one being responded to". No example has the ID PWD-PO-26-0212 (searched `PWD-PO-26-0212` over world/examples/*/*.xml: apart from this element it occurs only as part of LPWD-PO-26-0212). It differs from the order being responded to only by the missing first letter, so it is either a mistyped duplicate of the same order, which the element's definition excludes, or a reference to nothing.
- Condition: OrderDocumentReference is absent, or identifies an existing order other than LPWD-PO-26-0212.
- Options: (a) remove it (preferred); (b) none other seen.
- Needs decision: no

### tender/28#F2 · Medium · Pricing currency without any price
- XPath: `/OrderResponse/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: PricingCurrencyCode names the currency of the prices of the document. The response has no lines and no prices; its only amounts (charge and totals) are in XBL. The code and the pricing exchange rate therefore describe nothing in this document.
- Condition: PricingCurrencyCode is present only when the document has prices, and they are in that currency.
- Options: (a) remove PricingCurrencyCode and PricingExchangeRate (preferred).
- Needs decision: no

### tender/28#F3 · Medium · Language code in LocaleCode; province in Region
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; the province is in CountrySubentity.
- Options: (a) a locale code, and move the province (preferred).
- Needs decision: no

### tender/28#F4 · Low · The seller quotes the buyer's forward exchange contract
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- Why: a forward purchase of ferra is a contract of the party that has to pay in ferra, the department, with its bank (the ID has the prefix of the Bank of Lumeport's documents, BL). In the seller's response it is the seller who states it, as the basis of the pricing rate. The seller is not a party to that contract; and as in 26 and 27 the contract fixes a payment rate, not a pricing rate, and predates the procedure (2026-01-02).
- Condition: a foreign exchange contract is stated by a party to it, on the rate it fixes.
- Options: (a) remove the contract (and the pricing rate) from the seller's response (preferred).
- Needs decision: yes (whether and when the department hedges)

### tender/28#F5 · Low · The acceptance promises no delivery date and gives no sales order number
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `AP`
- XPath: `/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`
- Why: neither the order nor the change stated a delivery date, and the acceptance does not promise one, so the release has no agreed date in any document until the despatch advice. The seller's order number, which the order already quoted (`26-Order.xml:/Order/cbc:SalesOrderID` = `VI-SO-26-0058`), is absent from the one document in which the seller would assign it.
- Condition: the accepted release has a delivery date or period in the order or its response; the seller's order number is in the seller's response if it is used at all.
- Options: (a) add SalesOrderID VI-SO-26-0058 and a promised delivery period (preferred).
- Needs decision: no

### tender/28#F6 · Low · The department described as a company in a commercial register
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: a municipal department (ISIC 8411) is not a company in a commercial register and has no liquidation status.
- Condition: no liquidation status and no commercial-register type on the department.
- Options: (a) remove them (preferred).
- Needs decision: no

## Checked and consistent
- `/OrderResponse/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212` is the order (26) and `/OrderResponse/cac:OrderChangeDocumentReference/cbc:ID` = `LPWD-OC-26-0213` the order change (27); the response (2026-03-25 16:15) lies within the change's validity (to 2026-03-27).
- Totals equal those of the order change: 19960.00 + 200.00 = 20160.00; charge reason CAT (special colour service, UNTDID 7161) as in 27.
- Response code AP (accepted, UNTDID 4343) agrees with the note; the note is given in Urvanian and English with matching tags.
- Exchange rates 100 and 0.01 are reciprocal.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted here, the seller tells the buyer who will despatch the goods (Castrano Logistics issues the despatch advice, 29).
- `/OrderResponse/cbc:TaxCurrencyCode`: XUF without a tax total — refuted, it announces the tax currency of the invoice.
- `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount`: no order lines to carry the amounts — refuted, a simple acceptance may confirm totals only.
