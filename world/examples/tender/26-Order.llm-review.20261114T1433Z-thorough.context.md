# LLM review: 26-Order.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/26-Order.xml`, Git blob `6251abb7d11ec4be2651a2e8b809979afc7557fa` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/26#F1 · High · Pricing currency ferra, but the price is in lume
- XPath: `/Order/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `499`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for all prices in the Order". The only price of the order, 499, carries `currencyID="XBL"` (lume), the document currency, and that is the contract price of the tender (499.00 lume a bench); in ferra the price would be 49900, as in the catalogue. The declared pricing currency and the currency of the price contradict each other.
- Condition: Every `PriceAmount` of the order is in the currency `PricingCurrencyCode` names, or the pricing currency is not declared as different from the document currency.
- Options: (a) preferred: drop `PricingCurrencyCode` (and the pricing exchange rates, F3), since the contract and the order are in lume; (b) give the price in ferra (49900) with the rate to the document currency, if the contract price is the catalogue's ferra price.
- Needs decision: yes (which currency the contract price is fixed in)

### tender/26#F2 · Medium · The seller's sales order number in the buyer's order
- XPath: `/Order/cbc:SalesOrderID` = `VI-SO-26-0058`
- Why: `SalesOrderID` is "An identifier for the Order, assigned by the seller". The order is issued by the buyer (`/Order/cbc:ID` = `LPWD-PO-26-0212`) and is the first document of the purchase: the seller receives it afterwards and only then assigns its own number. The buyer cannot know it when it writes the order. (The element has a use when the order follows a quotation or a sales order of the seller; nothing of that kind precedes this order.)
- Condition: The order carries a sales order identifier only if the seller issued one before the order; otherwise the identifier first appears in the seller's response.
- Options: (a) preferred: remove it here and let the order response carry it; (b) none seen.
- Needs decision: no

### tender/26#F3 · Medium · An approval identifier for access to the delivery location used as release number
- XPath: `/Order/cac:Delivery/cbc:ReleaseID` = `1`
- Why: `ReleaseID` of a delivery is "An identifier used for approval of access to delivery locations (e.g., port terminals)": a release or gate-pass number that lets a carrier into a terminal. The delivery goes to the public works depot, which has no such approval, and the value `1` reads as "first release of the framework" (the contract speaks of releases). That is a different meaning of "release".
- Condition: `Delivery/ReleaseID` holds an access approval for the delivery location or is absent; the number of the framework release is stated elsewhere.
- Options: (a) preferred: remove it and state the release in the order's note or its identifier; (b) none seen in the model for a call-off number at this place.
- Needs decision: no

### tender/26#F4 · Medium · A line-level pricing exchange rate that does not differ from the document's
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Order/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- Why: The price's `PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". It is the same rate, between the same currencies, of the same date as the document's pricing exchange rate, so the condition of the definition is not met. In addition the price it sits on is in lume (F1), so no rate applies to it at all.
- Condition: A price carries its own pricing exchange rate only when that rate differs from the document's.
- Options: (a) preferred: remove the line-level rate; (b) none seen.
- Needs decision: no

### tender/26#F5 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in the sibling lifecycle stage description. (Semantic conformance asks for the UBL definition even where another use seems handy.) The same value comes with every copy of the item in the flow, from `25-Catalogue.xml` on.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element and keep the boundary in the lifecycle stage description; (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision)
### tender/26#F6 · Medium · A province in `Region`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/26#F7 · Medium · A language code as locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/26#F8 · Low · Three exchange rates and a forward contract in an order whose amounts are all in lume
- XPath: `/Order/cac:TaxExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/Order/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- Why: Every amount of the order is in lume: price, line amount, taxable amount, tax and totals. The order nevertheless carries a tax exchange rate, a pricing exchange rate and a payment exchange rate (`PaymentExchangeRate` is "The exchange rate between the document currency and the payment currency"; the order declares no payment currency). The pricing rate rests on a forward purchase of ferra concluded on 2026-01-02, ten days before the prior information notice of the procedure (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:IssueDate` = `2026-01-12`) and more than two months before the award, when the department could not know that it would buy from an Urvanian supplier, nor at what price; and a buyer that pays a lume price has no ferra to buy. The document does nothing with these rates.
- Condition: The order carries an exchange rate only for a currency in which it states or will settle amounts, and a foreign exchange contract only if it was concluded for this purchase (after the award).
- Options: (a) preferred: remove the rates and the forward contract from the order; (b) if the contract price is in ferra and paid in ferra, state price and payment currency accordingly and date the forward contract after the award.
- Needs decision: yes (follows the decision of F1)

### tender/26#F9 · Low · The first release does not say when the benches are wanted
- XPath: `/Order/cac:Delivery`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Public works depot, Lumeport`
- Why: An order is "A document used to order goods and services". The delivery of the order names who receives the goods and, in the delivery terms, the place as text, but neither the delivery nor the line has a requested delivery date or period, and no delivery address. The call for tenders asked for a first delivery on 2026-04-02 and a lead time of at most 10 days; the supplier cannot tell from the order which date applies to this release.
- Condition: The order states the requested delivery date or period of the release (and the delivery address, if it is not the buyer's postal address).
- Options: (a) preferred: add `RequestedDeliveryPeriod` to the delivery (e.g. the 2026-04-02 of the call for tenders) and the depot's address; (b) state in a note that the contract's lead time applies.
- Needs decision: no

### tender/26#F10 · Low · The contract referenced twice, once as "originator document"
- XPath: `/Order/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Order/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- Why: `OriginatorDocumentReference` is "A reference to an originator document associated with this document", i.e. a document of the originator of the need (a requisition, an internal request). Its identifier is the contract's, which the order already references in `Contract`; the reference gives no document type and adds nothing.
- Condition: The originator document reference points to a document of the originator other than the contract (with its type), or is absent.
- Options: (a) preferred: remove it; (b) refer to the department's internal requisition for the release, if the world has one.
- Needs decision: no

### tender/26#F11 · Low · The installation that is later invoiced against this order is not ordered
- XPath: `/Order/cbc:LineCountNumeric` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-B180`
- Why: The order has one line, 40 benches. The contract covers the benches (lot 1) and their installation (lot 2, 18.00 lume a bench), and the invoice that names this order bills the installation as well (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-INST-B`). Neither this order nor its change or response orders an installation (searched `VI-INST` and "Installation" in `26-Order.xml`, `27-OrderChange.xml`, `28-OrderResponse.xml`: none). The average release value of the framework, 20680.00, is 40 benches with installation (40 × 517.00); the order totals 19960.00, benches only.
- Condition: What is invoiced against the order was ordered: the release contains a line for the installation of the 40 benches, or the invoice does not bill it under this order.
- Options: (a) preferred: add a second order line for 40 installations at 18.00; (b) order the installation with a separate release and reference that in the invoice.
- Needs decision: yes (adds a line, or a document, to the flow)

### tender/26#F12 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/26#F13 · Low · Master data of a party that the document does not use
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). An order tells the seller what the buyer wants; the buyer has no reason to restate the seller's share capital, stock-exchange listing and warehouse provider to the seller. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
### tender/26#F14 · Low · The whole catalogue description of the item repeated in a document that does not use it
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Dimension[4]`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile`
- Why: The item is identified by the seller's and the standard item identification and the catalogue reference. Beyond that the line repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the test method of the load capacity, the range of the seat height, the greenhouse-gas emission of manufacturing with its calculation method and measurement period, and the circularity profile (maintenance frequency, resource consumption, packaging waste, repairability score, repair manual). An order needs to say which item is wanted, in which variant and quantity, at which price; the seller knows its own product's emissions, test methods and repair manual. It reads as item master data copied into the document; the remarks made on these values in the catalogue's review (lifecycle stage code against its description, no recycled steel shown, two keywords in one element) come along with every copy.
- Condition: The item of this document carries the identification and those properties the document's purpose uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) preferred: reduce the item to identification, name, description and the properties this document needs; (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision.
- Needs decision: yes (a design decision for all documents that carry the item)
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- Arithmetic: 40 × 499 = 19960.00 = line amount = taxable amount = `LineExtensionAmount` = `PayableAmount`; tax 0.00.
- Quantity 40 against the awarded tender's order constraints (pallet of 4, steps of 4, 20 to 96 per order): 40 is a multiple of 4 within the range.
- `Contract` `PWD-2026-PARKS` is the framework contract; the order is issued on 2026-03-23, the day the contract starts, after the catalogue (2026-03-21); `CatalogueDocumentReference` `VI-CAT-26-0211` is the catalogue, and `CatalogueIndicator` true fits an order from it.
- Price 499 lume = the awarded tender's unit price; item `VI-B180`, variant `GRY`, as in the catalogue.
- `LineCountNumeric` 1 with one order line; `OrderTypeCode` 220 (order); delivery terms DAP with a named place; delivery party = buyer.
- Tax and payment exchange rates (lume → ferra, 100) are the inverse of the pricing rate (ferra → lume, 0.01).

## Considered and refuted
- `/Order/cbc:OrderTypeCode`: 220 "Order" for a release under a framework, where UN/EDIFACT 1001 also has a call-off order — refuted because 220 is a correct, more general type and the contract is referenced.
- `/Order/cbc:TaxCurrencyCode`: ferra as the currency requested for tax amounts although the buyer is in Bayvarra — refuted for this lens because the tax in question is the seller's Urvanian value added tax (export exemption); the money part judges the tax treatment.
- `/Order/cbc:AccountingCostCode`: the same value as the project reference `PWD-PARKS-26` — refuted, a cost code named after the programme it books to is plausible.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:WarrantyInformation[2]`: the ten-year coating warranty is missing — refuted here because the text is the catalogue's; raised in the catalogue's review.

## Outside this review
- The tax category of the order's tax total (export out of Urvania, in a tax total in lume) is the money part's lens.
- The emission factor arithmetic of the item (0.82 × 1 against 96 kg) is the logistics part's lens.
