# LLM review: 28-OrderResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/28-OrderResponse.xml`, Git blob `3ed78b3450611e60a961e71c98db29842ff2963f` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit e0e5001 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/28#F1 · High · A second order reference to an order that does not exist
- XPath: `/OrderResponse/cac:OrderDocumentReference/cbc:ID` = `PWD-PO-26-0212`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: `OrderDocumentReference` is "A reference to an Order other than the one being responded to". The flow has one order, `LPWD-PO-26-0212`, which the response already names in `OrderReference` as the order responded to. `PWD-PO-26-0212` is the identifier of no document (as an exact value it occurs only here; searched `>PWD-PO-26-0212<` over `world/examples/*/*.xml`); it is the order's own number without its first letter. Either it is meant as the same order, which the definition excludes, or it points to an order that does not exist.
- Condition: `OrderDocumentReference` is absent, or names an existing order other than `LPWD-PO-26-0212` that the response has a reason to mention.
- Options: (a) preferred: remove it; (b) none seen, there is no other order.
- Needs decision: no

### tender/28#F2 · Medium · A province in `Region`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/28#F3 · Medium · A language code as locale
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/28#F4 · Low · The acceptance says neither the seller's order number nor when it delivers
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `AP`
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: An order response is "A document used to indicate detailed acceptance or rejection of an Order or to make a counter-offer". The response accepts the order and its change and confirms the total; it has no sales order identifier, although the buyer's order quotes one (`26-Order.xml:/Order/cbc:SalesOrderID` = `VI-SO-26-0058`), no order line and no promised delivery date, although the order gave no date either and the colour was changed to a special one. The seller's own number belongs in the seller's document, and the acceptance is where the buyer would learn when the green benches come.
- Condition: The order response carries the seller's sales order identifier (and the buyer's order does not), and states the promised delivery date or period of the release.
- Options: (a) preferred: add `SalesOrderID` and a promised delivery period; (b) at least the sales order identifier.
- Needs decision: no

### tender/28#F5 · Low · Exchange rates, a pricing currency and the buyer's forward contract in a response whose amounts are all in lume
- XPath: `/OrderResponse/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderResponse/cac:TaxExchangeRate`
- XPath: `/OrderResponse/cac:PricingExchangeRate`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/OrderResponse/cac:PaymentExchangeRate`
- Why: The response contains no price, and its charge and totals are in lume, the document currency; a pricing currency "used for all prices" and three exchange rates have nothing to apply to. The foreign exchange contract is a forward purchase of ferra, i.e. a contract of the party that holds lume and needs ferra, the buyer (its identifier is the one in the buyer's order and order change); the seller, who issues this document, has no part in it and no reason to restate it. Its date, 2026-01-02, precedes the whole procedure.
- Condition: The order response carries an exchange rate only for a currency in which it states amounts or will be settled, and no foreign exchange contract of the other party.
- Options: (a) preferred: remove pricing currency, rates and contract; (b) keep one rate if the response states the ferra equivalent of the total.
- Needs decision: yes (follows the currency decision of the order, `26-Order.xml`)

### tender/28#F6 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/28#F7 · Low · Master data of a party that the document does not use
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The response accepts an order; the seller's share capital, listing and warehouse provider play no part in the acceptance. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- `OrderReference` `LPWD-PO-26-0212` is the order, `OrderChangeDocumentReference` `LPWD-OC-26-0213` the order change; the response is issued on 2026-03-25, after both and within the change's validity (to 2026-03-27).
- `OrderResponseCode` `AP` (accepted) with the note "Accepted: moss green, at the quoted charge."; charge 200.00 with reason `CAT`, as in the order change.
- Totals: 19960.00 + 200.00 = 20160.00, equal to the order change's total.
- The note is given in Urvanian and English, tagged `qau` and `en-XU`; the seller is Urvanian.
- Seller and buyer are in their roles (seller first, as sender).

## Considered and refuted
- `/OrderResponse/cac:LegalMonetaryTotal`: a total without order lines — refuted because a response of type "accepted" may confirm the order as a whole, and the total equals the changed order's.
- `/OrderResponse/cac:AllowanceCharge`: the charge repeated from the change — refuted because it is the part of the change that costs money and the seller confirms it.
