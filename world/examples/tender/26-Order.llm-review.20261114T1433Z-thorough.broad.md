# LLM review: 26-Order.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/26-Order.xml`, Git blob `6251abb7d11ec4be2651a2e8b809979afc7557fa` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/26#F1 · High · Pricing currency is ferra, but the price is given in lume
- XPath: `/Order/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `499`
- Why: PricingCurrencyCode is "A code signifying the currency used for all prices in the Order". The only price of the order carries `currencyID="XBL"` (499 lume; in ferra it would be 49900, as in the catalogue). The header thus says all prices are in XUF while the price is in XBL. The line's PricingExchangeRate (XUF to XBL, 0.01) shows that the price was converted from the catalogue's ferra price into the document currency, i.e. it is no longer in the pricing currency.
- Condition: every PriceAmount of the order is in the currency PricingCurrencyCode names, or PricingCurrencyCode is absent/equal to the currency the prices are in.
- Options: (a) PriceAmount 49900 XUF with the exchange rate explaining the line amount in XBL (preferred, matches the catalogue's contract price); (b) drop PricingCurrencyCode and the pricing exchange rates and price in XBL, as the tender did.
- Needs decision: no

### tender/26#F2 · High · The order has one line, but the invoice for it bills the installation as well
- XPath: `/Order/cbc:LineCountNumeric` = `1`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `19960.00`
- Why: the order asks for 40 benches and nothing else. The invoice that cites this order bills a second line, `32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00` for 40 times "Installation of a park bench" (lot 2 of the framework), which no order line and no order change line covers. Either the release includes the anchoring of the 40 benches, and then the order lacks the line and its amount is too low, or it does not, and the invoice bills an unordered service.
- Condition: what the invoice bills against this order is ordered by it (or by its order change), with matching quantities and amounts.
- Options: (a) add an order line for the installation of 40 benches at 18.00 (preferred: the framework awards both lots together and the delivery terms name the depot only for the goods); (b) bill the installation on a separate order of lot 2.
- Needs decision: yes (whether release 1 includes installation)

### tender/26#F3 · Medium · The seller's sales order number in the buyer's order
- XPath: `/Order/cbc:SalesOrderID` = `VI-SO-26-0058`
- Why: SalesOrderID is "An identifier for the Order, assigned by the seller". The order is the first message of the release, issued by the department; the seller can assign its number only after receiving it. The seller's own order response (28) carries no SalesOrderID, and no other example of the flow mentions VI-SO-26-0058 (searched tender/*.xml).
- Condition: a seller-assigned order number appears first in a document the seller issues (order response) and is repeated by the buyer only afterwards.
- Options: (a) move it to 28-OrderResponse.xml (preferred); (b) remove it.
- Needs decision: no

### tender/26#F4 · Medium · ReleaseID used as the number of the framework release
- XPath: `/Order/cac:Delivery/cbc:ReleaseID` = `1`
- Why: Delivery/ReleaseID is "An identifier used for approval of access to delivery locations (e.g., port terminals)", i.e. a gate or terminal release reference. The value 1 is evidently the first release (call-off) of the framework ("Releases every few months", 21), which is a different thing; the delivery place is the department's own depot, where no access release is needed.
- Condition: ReleaseID holds an access-approval reference of the delivery location, or is absent; the number of the framework release is given where it belongs (e.g. in the order's note or ID).
- Options: (a) remove ReleaseID and state "Release 1 of framework …" in a Note (preferred); (b) none other seen.
- Needs decision: no

### tender/26#F5 · Medium · Emission factor that does not lead to the emission value
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × the base of 1 bench is not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state (the materials are 34 kg steel and 22.5 kg hardwood). The block is the catalogue's (25), where the same holds.
- Condition: factor × the stated base or activity gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric (preferred); (b) state the activity.
- Needs decision: no

### tender/26#F6 · Medium · Language code in LocaleCode; province in Region
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; the province is in CountrySubentity.
- Options: (a) a locale code, and move the province (preferred).
- Needs decision: no

### tender/26#F7 · Low · The order says neither when nor exactly where to deliver
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Public works depot, Lumeport`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: the release is to be delivered DAP to a depot, but the order has no requested delivery date or period and no delivery address; the depot appears only as a description inside the delivery terms. The call required delivery within a lead time (10 days) from 2026-04-02; a seller cannot tell from the order when the 40 benches are wanted, and the despatch advice (29) later has to know the depot's address from elsewhere.
- Condition: the order states the requested delivery date or period and identifies the delivery location by address or identifier.
- Options: (a) add Delivery/RequestedDeliveryPeriod and Delivery/DeliveryLocation with the depot's address (preferred).
- Needs decision: no

### tender/26#F8 · Low · A forward exchange contract of 2 January attached to the pricing rate
- XPath: `/Order/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/Order/cac:PaymentExchangeRate/cbc:Date` = `2026-03-23`
- Why: PricingExchangeRate is "The exchange rate between the document currency and the pricing currency"; a forward purchase of ferra hedges a payment, and the rate it fixes would be the payment rate, yet PaymentExchangeRate carries a rate "established" on the order date with no contract. The forward was concluded on 2026-01-02, ten days before the prior information notice (2026-01-12) and two months before the award, when neither the supplier nor the currency of the purchase was known. The order also gives a payment exchange rate without naming a payment currency (the invoice names XUF).
- Condition: a foreign exchange contract is attached to the rate it fixes and is dated when the need for ferra was known; the payment currency is stated where a payment rate is given.
- Options: (a) move the contract to PaymentExchangeRate with a date after the award and add PaymentCurrencyCode XUF (preferred); (b) drop the forward contract.
- Needs decision: yes (whether the department hedges at all, and when)

### tender/26#F9 · Low · OriginatorDocumentReference repeats the contract number
- XPath: `/Order/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Order/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- Why: the originator document is "an originator document associated with this document", e.g. the internal requisition that led to the order. Here it has the same identifier as the contract (which is also the procurement file's number), without a document type, so it adds nothing and leaves open what it points to. The signed contract itself is identified as LPWD-DOC-26-0210 / PWD-CONTRACT-2026-PARKS in 24.
- Condition: the originator reference names a document other than the contract and says what it is, or is absent; the contract reference uses the contract's identifier.
- Options: (a) remove OriginatorDocumentReference (preferred); (b) reference a requisition.
- Needs decision: no

### tender/26#F10 · Low · The full catalogue record of the item and seller master data in the order; department as a company
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ResourceOriginDescription` = `Steel made from Serravona ore in Urvania`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the order line identifies the item by the seller's number, the standard number and the catalogue reference; it then repeats the catalogue's whole record (emissions, circularity profile, repairability, test method, waste per bench), which are the seller's statements and which the buyer neither orders nor can vouch for. The steel is described as made from ore although the contract requires at least 30 % recycled steel (see 25). The buyer also tells the seller who the seller's logistics provider is. The buyer, a municipal department, carries a company liquidation status and a commercial-register type.
- Condition: the order identifies the item and states what the buyer requires; seller statements and seller master data are absent; the department carries no liquidation status.
- Options: (a) reduce the item to identification, name, description and required properties (colour) (preferred).
- Needs decision: no

## Checked and consistent
- Arithmetic: 40 × 499 = 19960.00 = line amount = LineExtensionAmount = PayableAmount = TaxableAmount; tax 0.00.
- Exchange rates: 49900 XUF × 0.01 = 499 XBL (catalogue 25); 100 and 0.01 are reciprocal; the operator is Multiply in each direction.
- Quantity 40 fits the tender's ordering terms (minimum 20, increments of 4, maximum 96; 15) and is one sixth of 240, the average release of the notices (19960.00 for lot 1).
- References: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CatalogueDocumentReference/cbc:ID` = `VI-CAT-26-0211` is the catalogue (25), issued 2026-03-21 before the order; the item data equal the catalogue line 1 (English texts tagged en-XB instead of en-XU).
- Issue date 2026-03-23 is the first day of the contract's validity.
- DAP (Incoterms) with the buyer as importer agrees with the import declaration lodged by the department (31).
- Order type 220 (order) from UNTDID 1001.
- Tax category G with the Urvanian export reason is what the invoice (32) applies.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/Order/cbc:OrderTypeCode`: a release under a framework could be 226 (call off order) — refuted because 226 refers to a blanket order message; a release under a contract is an ordinary order with a contract reference.
- `/Order/cbc:TaxCurrencyCode`: XUF while the tax total is in XBL — refuted because the code is "the currency requested for tax amounts in Invoices related to this Order", not the currency of this order's tax total.
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID`: a Bayvarran buyer stating Urvanian export VAT — refuted because the order anticipates the tax of the invoice, and the buyer's own exemption from state sales tax needs no line here.
- `/Order/cac:PricingExchangeRate/cbc:ExchangeMarketID`: XLMX could be a real MIC — refuted, it is in the world's market list (Lumeport Exchange) and I know no ISO 10383 MIC XLMX.
- `/Order/cbc:AccountingCostCode`: code without listID, equal to the project reference — refuted, a buyer-internal accounting code.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name`: order desk — fits the role here.
