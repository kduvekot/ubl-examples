# LLM review: 27-OrderChange.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/27-OrderChange.xml`, Git blob `e43fb0041dc6f797ab80a2e9f8efb406a7c4464c` (committed)
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

### tender/27#F1 · High · Payment terms "as the contract says" that the contract does not say
- XPath: `/OrderChange/cac:PaymentTerms/cbc:Note` = `30 days after the invoice, as the contract says.`
- Why: the contract's payment terms are `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` (the same in the notices and the call). The order change counts the 30 days from the invoice and claims the contract as its source. The two starting points differ: the invoice of this release is dated 2026-03-31, while the release can only be accepted after delivery and inspection.
- Condition: payment terms that cite the contract repeat the contract's terms.
- Options: (a) "30 days after each accepted release" (preferred); (b) change the contract's terms in 02, 03, 21, 24 to 30 days after the invoice.
- Needs decision: yes (which term is the world's; the invoice and the reminder depend on it)

### tender/27#F2 · Medium · Pricing currency without any price
- XPath: `/OrderChange/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderChange/cac:AllowanceCharge/cbc:Amount` = `200.00`
- Why: PricingCurrencyCode is the currency "used for all prices" of the document. The order change contains no price: the line has a quantity and an amount in XBL, and the new charge is in XBL. If the code is taken to cover the amounts that price the change, they contradict it (as in the order, 26, where the unit price is in XBL under a pricing currency XUF).
- Condition: PricingCurrencyCode is present only when the document has prices, and they are in that currency.
- Options: (a) remove PricingCurrencyCode and PricingExchangeRate from the order change (preferred); (b) give the line's price in XUF.
- Needs decision: no

### tender/27#F3 · Medium · Language code in LocaleCode; provinces in Region
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; provinces are in CountrySubentity.
- Options: (a) a locale code, and move the provinces (preferred).
- Needs decision: no

### tender/27#F4 · Low · The change of colour is only in free text; the item is not identified
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Park bench Serra 180, frame in moss green RAL 6005`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`
- Why: the order identified the bench as VI-B180 with ExtendedID GRY, a PhysicalAttribute COLOUR/FRM/GRY and a property "Frame colour" = Ferro grey (26). The revised line carries no item identification at all and states the new colour only in the description, although the same structures exist to say it (ExtendedID, PhysicalAttribute with a colour code). A receiving system cannot match the revised line to the article or see which attribute changed.
- Condition: the revised line identifies the same item as the order line and states the new colour in the structure the order used for the old one.
- Options: (a) SellersItemIdentification VI-B180 with the green variant's ExtendedID and PhysicalAttribute (preferred); (b) at least the item identification.
- Needs decision: no

### tender/27#F5 · Low · Payment means, payment terms and a freight forwarder appear for the first time in a change of colour
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458`
- XPath: `/OrderChange/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/OrderChange/cac:TransactionConditions/cbc:Description` = `The framework contract's conditions apply.`
- Why: the change asks for another colour and accepts a charge of 200 lume. It also introduces the seller's bank account, payment terms, general conditions and a freight forwarder, none of which the order (26) had and none of which the note presents as a change. Under the order's DAP terms the seller arranges the carriage, so a forwarder named by the buyer has no task; in the invoice the same company is the seller's tax representative (32), and the goods are in fact despatched by Castrano Logistics (29). The forwarder is not explained by anything in the flow.
- Condition: an order change carries what it changes (and what is needed to understand the change); a freight forwarder is named only if it carries or forwards the goods of this order.
- Options: (a) remove FreightForwarderParty, PaymentMeans, PaymentTerms and TransactionConditions here; put payment terms in the order if wanted (preferred); (b) explain the forwarder's task in the story.
- Needs decision: yes (what Bayforth Forwarding does for this order)

### tender/27#F6 · Low · A forward exchange contract of 2 January attached to the pricing rate
- XPath: `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/OrderChange/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- Why: as in the order (26): a forward purchase of ferra fixes a payment rate, not a pricing rate, and it is dated ten days before the prior information notice, when no supplier or currency was known. The payment rate given here has no contract and no payment currency.
- Condition: the foreign exchange contract is attached to the rate it fixes and dated when the need was known.
- Options: (a) move it to PaymentExchangeRate with a plausible date (preferred); (b) drop it.
- Needs decision: yes (whether and when the department hedges)

### tender/27#F7 · Low · OriginatorDocumentReference repeats the contract number; department as a company; seller master data
- XPath: `/OrderChange/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/OrderChange/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the originator reference has the contract's (and the procurement file's) identifier and no type, so it adds nothing. The department carries a company liquidation status and a commercial-register type. The buyer repeats the seller's logistics provider.
- Condition: the originator reference names a distinct document or is absent; the department has no liquidation status; seller master data is absent.
- Options: (a) remove them (preferred).
- Needs decision: no

## Checked and consistent
- `/OrderChange/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212` is the order (26), issued the day before; line 1, quantity 40 and amount 19960.00 are unchanged and the line status is Revised.
- Arithmetic: 19960.00 + charge 200.00 = 20160.00 payable; the order response (28) and the invoice (32) carry the same charge with the same reason code.
- Charge reason CAT is "Special colour service" in UNTDID 7161 and agrees with the text; RAL 6005 is moss green in the real RAL Classic collection.
- The change is answered within its validity (to 2026-03-27) by the order response of 2026-03-25, which accepts "moss green, at the quoted charge"; the despatch advice confirms forty benches in RAL 6005.
- Payment means 30 (credit transfer) to Valdara's account; branch ID 03510-41600 is contained in the account number; check_ids.py: IBAN-like XU790351041600000000209458 and ISIN XU0001042501 correct.
- Exchange rates 100 and 0.01 are reciprocal; requested invoice currency XBL equals the invoice's document currency.

## Considered and refuted
- `/OrderChange/cac:QuotationDocumentReference/cbc:ID`: VI-QT-26-0071 is no example of the flow, and a quotation would have had to arrive between the order (2026-03-23 14:40) and this change (2026-03-24 08:06) — refuted because a quotation for a colour surcharge can be given the same afternoon and need not be a UBL document of the flow.
- `/OrderChange/cac:AdditionalDocumentReference/cbc:ID`: only an ID — refuted, the identifier names the colour specification.
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: CREVXUFR could be a real BIC — refuted, country part XU is not an assigned ISO 3166 code.
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]`: Italian-looking name tagged en-XB — refuted, the world's English names for Urvanian places are Italianate.
- `/OrderChange/cac:AllowanceCharge/cbc:Amount`: no tax category on the charge — refuted, an order change need not state tax.
