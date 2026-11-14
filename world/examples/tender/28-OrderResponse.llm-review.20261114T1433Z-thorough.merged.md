# LLM review: 28-OrderResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/28-OrderResponse.xml`, Git blob `3ed78b3450611e60a961e71c98db29842ff2963f` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/28#F1 · High · Reference to "another order" that does not exist
- XPath: `/OrderResponse/cac:OrderDocumentReference/cbc:ID` = `PWD-PO-26-0212`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: `OrderDocumentReference` is "A reference to an Order other than the one being responded to". The flow has one order, `LPWD-PO-26-0212`, already named in `OrderReference`. `PWD-PO-26-0212` is the identifier of no document (`grep -rho --include='*.xml' '>PWD-PO-26-0212<' world/examples | wc -l`: 1, this element); it is the order's own number without its first letter. Either it means the same order, which the definition excludes, or an order that does not exist.
- Condition: `OrderDocumentReference` is absent, or names an existing order other than `LPWD-PO-26-0212`.
- Options: (a) remove it (preferred; there is no other order).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### tender/28#F2 · High · The accepted total of the release does not contain the installation that the seller then invoices for the same order
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: `LegalMonetaryTotal` is "The total amount of the Order (or counter-offer)". The seller accepts the order as changed at 20160.00 lume: 40 benches and the colour charge. Six days later the same seller invoices the same order with a second line for the installation (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`), for `32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `20880.00`. Recalculated: 20880.00 − 20160.00 = 720.00. Two totals of one release, both stated by the seller, differ, and no document orders or accepts the installation. Same problem as 26#F3 and 27#F2.
- Condition: the total the seller accepts equals what it invoices for the order before withholding, line by line.
- Options: (a) once the installation is ordered (26#F3), accept 20880.00 here (preferred); (b) a separate order and response for the installation.
- Needs decision: yes
- From: money (F1, Medium)

### tender/28#F3 · Medium · A province in `Region`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries"; a province is `CountrySubentity`, as the Bayvarran addresses use. 219 in 104 files.
- Condition: the province is in `CountrySubentity`; `Region` is absent or holds a region.
- Options: (a) move it to `CountrySubentity` (preferred).
- Needs decision: no
- From: broad (F3, part), parties (F1), context (F2)

### tender/28#F4 · Medium · Language code in `LocaleCode`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 code. 362 in 213 files.
- Condition: `LocaleCode` is absent or names a locale from a locale list.
- Options: (a) remove it (preferred); (b) `en-XB` from a locale list.
- Needs decision: no
- From: broad (F3, part), parties (F2), context (F3)

### tender/28#F5 · Medium · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The buyer is a municipal department (ISIC 8411); a liquidation status and a "Commercial register" type do not fit a body that is not a company.
- Condition: neither on the public body.
- Options: (a) drop both (preferred); (b) reduce the legal entity to name and CompanyID.
- Needs decision: no
- From: broad (F6, Low), parties (F6, Low), context (F6, Low)

### tender/28#F6 · Low · The acceptance gives neither the seller's order number nor a delivery date
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `AP`
- XPath: `/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: The buyer's order quotes a seller's order number (`26-Order.xml:/Order/cbc:SalesOrderID` = `VI-SO-26-0058`), which only the seller can assign; the seller's own response, its natural first place, does not have it. Neither the order nor the change stated a delivery date, and the acceptance promises none, although the colour was changed to a special one and the contract's penalty clause counts days late; no document fixes the release's date before the despatch advice.
- Condition: the seller's order number is in the seller's response (and not first in the order), and the release has a requested or promised delivery date or period.
- Options: (a) `SalesOrderID` VI-SO-26-0058 here and a `Delivery/PromisedDeliveryPeriod` (preferred); (b) leave the response minimal and fix the date in the order (26#F12).
- Needs decision: no
- From: broad (F5), logistics (F2), context (F4)

### tender/28#F7 · Low · Currency codes, three exchange rates and the buyer's forward contract in a response whose amounts are all in lume
- XPath: `/OrderResponse/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderResponse/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/OrderResponse/cac:TaxExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/OrderResponse/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- Why: `PricingCurrencyCode` is "the currency that is used for all prices in the Order Response" and `TaxCurrencyCode` "the currency that is used for all tax amounts in the Order Response". The response has no line, no price and no tax amount; its charge and totals are in lume, and it names no payment currency, so none of the rates converts anything. The forward purchase of ferra is a contract of the party that needs ferra, the buyer (the ID is the one in the buyer's 26 and 27, with the prefix of the Bank of Lumeport); the seller who issues this response is no party to it, and it dates from before the procedure (26#F13). Broad refuted `TaxCurrencyCode` as an announcement of the invoice's tax currency; in the order response the definition speaks of the response's own tax amounts.
- Condition: a currency code and exchange rate are present only where the response has an amount in, or a conversion into, that currency, and no foreign exchange contract of the other party is stated.
- Options: (a) remove the currency codes, the rates and the contract (preferred); (b) keep only what the currency decision of 25#F17 requires.
- Needs decision: yes (follows 26#F13 and 25#F17)
- From: broad (F2, Medium; F4, Low, yes), money (F2), context (F5)

### tender/28#F8 · Low · Party tax exemption reason worded as a transaction
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the text begins with a kind of sale; only its second half is the party's status.
- Condition: the party-level reason states the party's status.
- Options: (a) reword, e.g. "Public body: exempt from the state sales tax" (preferred).
- Needs decision: no
- From: parties (F5)

### tender/28#F9 · Low · Master data of the parties that the response does nothing with
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketName` = `Ferrano Stock Exchange`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: The response accepts an order; share capital, listing, the warehouse provider (whose contact has no means of contact) and both customs-trader numbers play no part in it. Counter-arguments carried: broad held that the seller tells the buyer who will despatch (Castrano issues 29); parties held that the listing is part of a listed company's description. A seller announcing its despatcher would do so in the delivery terms or the despatch advice, not as master data of itself.
- Condition: the parties carry what the response uses.
- Options: (a) leave these out (preferred); (b) keep those with a stated use, with a reachable contact.
- Needs decision: no
- From: parties (F4), context (F7); customs-trader numbers added in the merge

### tender/28#F10 · Low · Same Urvanian party tagged `en-XU` here and `en-XB` (with a single untagged legal form) in the Bayvarran-issued examples
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: This Valdara-issued response tags the English renderings `en-XU` and gives the legal form twice; the Bayvarran-issued examples tag the same texts `en-XB` and give the legal form once, untagged (`03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). This example is the `en-XU` side; the finding is the inconsistency across the flow. The renderings are moreover Italian names and an Italian legal form tagged as English, the second Low/yes question of the earlier flows. Neither can be settled from the XML.
- Condition: the same text carries the same `languageID` in every example, and the tag names the language of the text, or the convention is documented.
- Options: (a) `en-XU` everywhere, as here, and the convention recorded (preferred); (b) document the issuer rule.
- Needs decision: yes
- From: parties (F3); the Italian-name question added by the merge, as in 24–27

## Checked and consistent
- `OrderReference` `LPWD-PO-26-0212` is 26 and `OrderChangeDocumentReference` `LPWD-OC-26-0213` is 27; the response (2026-03-25 16:15) follows both and lies within the change's validity (to 2026-03-27).
- Totals (recalculated): 19960.00 + 200.00 = 20160.00 = the anticipated total of 27; charge CAT "Special colour" 200.00 as in 27 and 32.
- `OrderResponseCode` AP (Accepted, UNCL 4343) agrees with the note; the change is referenced, so the amended order is accepted without amendment by the seller.
- The note in `qau` and `en-XU`; the seller is Urvanian. Seller and buyer as in 26 and 27; seller's order-desk contact fits the acceptance of orders (from parties).
- `check_ids.py`: ISIN XU0001042501 correct.

## Considered and refuted
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted by broad (the seller tells who despatches); the merge keeps it in F9 (from broad).
- `/OrderResponse/cbc:TaxCurrencyCode`: XUF without a tax total — refuted by broad as an announcement of the invoice's tax currency; the merge keeps it in F7 because the order-response definition concerns the response's own tax amounts (from broad).
- `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount`: totals without order lines — refuted: an unconditional acceptance may confirm totals only (from broad, context).
- `/OrderResponse/cac:AllowanceCharge/cbc:Amount`: no tax category on the charge — refuted: no tax totals in the response; the category follows from the goods (from money).
- `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount`: no payment terms or due date — refuted: the terms are the contract's and the response accepts without change (from money).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` — refuted: text element, same everywhere (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 — refuted, not assigned in E.164 (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: unused master data — refuted by parties; the merge keeps it in F9 (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990` a real ICD — refuted (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name`: order desk unsuitable — refuted: it accepts orders and changes (from parties).
- `/OrderResponse/cac:PricingExchangeRate/cbc:Date`: 2026-01-02 in a document of 25 March — refuted here as the date of the forward contract the rate comes from; the contract itself is in F7 (from logistics).
- `/OrderResponse/cbc:OrderResponseCode`: AP although the order was changed — refuted: the change is referenced and accepted (from logistics).
- `/OrderResponse/cac:AllowanceCharge`: the charge repeated from the change — refuted: it is the costed part of the change, confirmed by the seller (from context).

## Changed in the merge
- money/F1 (Medium) → F2: High, aligned with 26#F3 and 27#F2.
- broad/F3 → F3 and F4: split.
- broad/F6, parties/F6, context/F6 (Low) → F5: Medium, aligned with the decisions file.
- broad/F5, logistics/F2, context/F4 → F6: combined.
- broad/F2 (Medium), broad/F4, money/F2, context/F5 → F7: combined, Low (nothing to convert), Needs decision yes for the forward contract.
- parties/F4, context/F7 → F9: combined; customs-trader numbers added.
- parties/F3 → F10: the Italian-name question added.
