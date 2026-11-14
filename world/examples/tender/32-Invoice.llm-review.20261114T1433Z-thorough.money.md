# LLM review: 32-Invoice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/32-Invoice.xml`, Git blob `670ec0ba9b4bae748393682c8030e3f46b70c018` (committed)
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

### tender/32#F1 · High · The invoice bills 720.00 lume of installation that the order it refers to does not contain
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `20880.00`
- Why: the invoice's only order reference is the first release. That order has one line, 40 benches (`26-Order.xml:/Order/cbc:LineCountNumeric` = `1`), and after the colour change the seller itself accepted it at `28-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`. The invoice's first line refers to order line 1; its second line, 40 installations, has no order line reference and nothing in 26, 27 or 28 orders it. The seller therefore invoices 720.00 lume more than the total it accepted for this order six days earlier.
- Condition: every invoice line that falls under the order reference corresponds to a line of the order as changed and accepted, and the invoice's amount before withholding equals the accepted total; or the second line refers to another order that exists in the flow.
- Options: (a, preferred) add the installation to the order (26#F1 of this part) and give the invoice's second line its order line reference; (b) a separate order for the installation, referenced from line 2.
- Needs decision: yes

### tender/32#F2 · High · In the tax currency the whole invoice, installation included, is declared as export of goods
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `2088000`
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `720.00`
- Why: the tax total in lume splits the invoice into 20160.00 under category G (export of goods) and 720.00 under category O (service outside the scope). The tax total in ferra, the declared tax currency and the one the Urvanian tax return uses, has a single subtotal: 2088000 ferra = 20880.00 lume × 100, all under category G with reason "Export of goods outside Urvania". At the invoice's own rate the two subtotals should be 2016000 and 72000 ferra. As written, 72000 ferra of installation service are reported as exported goods, and the two tax totals of one invoice contradict each other.
- Condition: the tax total in the tax currency has the same subtotals (category, reason) as the one in the document currency, each taxable amount being the document-currency amount converted with `TaxExchangeRate`.
- Options: (a, preferred) two subtotals in ferra: 2016000 (G, EXP) and 72000 (O, SVCABROAD); (b) none seen.
- Needs decision: no

### tender/32#F3 · High · The due date runs from the invoice date; the contract the invoice refers to lets it run from the acceptance of the release
- XPath: `/Invoice/cbc:DueDate` = `2026-04-30`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: the invoice applies the seller's standard terms (ID XU-STD, details at the seller's website): 30 days from the invoice date, 31 March + 30 = 30 April. The contract it cites says `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` On 31 March the release was not accepted: the goods had been despatched the evening before and were cleared for import two hours after the invoice, four anchor sets were on back order (29-DespatchAdvice.xml) and the installation was finished late (34-DebitNote.xml, 6 April, "3 days"). Under the contract the due date lies thirty days after an acceptance in April, i.e. in May, not on 30 April. The difference has consequences in the flow: the reminder charges interest from 1 May (35-Reminder.xml). The buyer's order change words the term a third way ("30 days after the invoice, as the contract says.", 27#F1 of this part).
- Condition: the invoice's due date (in all three places it is stated) is the date the contract's payment term yields, and the term text in the invoice is the contract's; a settlement discount may be offered in addition.
- Options: (a, preferred) record the acceptance of the release (a date in the invoice note or a receipt advice in the flow) and set the due date to acceptance + 30 days, moving the reminder accordingly; (b) change the contract's term to "30 days after the invoice" in 01–03 and 24, which makes 27 and this invoice right.
- Needs decision: yes

### tender/32#F4 · Medium · The pricing currency is the ferra, both prices are stated in lume
- XPath: `/Invoice/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `18`
- Why: `PricingCurrencyCode` is "a code signifying the currency used for prices in the Invoice". Both `PriceAmount`s carry `currencyID="XBL"`. If prices are in ferra they are 49900 and 1800 (as in 25-Catalogue.xml) and the pricing exchange rate turns them into the line amounts; if they are in lume, the pricing currency is the document currency and neither the code nor the pricing exchange rate has a function.
- Condition: every `PriceAmount` is in the currency named by `PricingCurrencyCode`; if that is the document currency, there is no `PricingCurrencyCode`/`PricingExchangeRate`.
- Options: (a) prices 49900 and 1800 XUF; (b) drop the pricing currency and rate. The choice follows the decision on the contract's price currency (25#F2 of this part); (b) is preferred if the contract is in lume, as tendered.
- Needs decision: no

### tender/32#F5 · Medium · Each price repeats the document's pricing exchange rate, with base rates that say nothing
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyBaseRate` = `1`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:TargetCurrencyBaseRate` = `1`
- Why: `Price/PricingExchangeRate` is "the exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". On both lines it has the document's currencies, rate (0.01) and date (2026-01-02); the condition is not met. The base rates ("in the case of a … currency with denominations of small value, the unit base") are 1 on both sides, the default, on both lines.
- Condition: a price-level exchange rate is present only where it differs from the document's; base rates only with a value other than 1 that the rate refers to.
- Options: (a, preferred) remove the price-level exchange rates; (b) none seen.
- Needs decision: no

### tender/32#F6 · Low · Late-payment interest of the seller's home law on a contract under Bayvarran procurement law that names no interest
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentTermsDetailsURI` = `https://www.valdara.example/terms`
- Why: `PenaltyInterestRate` is "an interest rate to be applied in case of late payment". The 8 % a year comes from the seller's standard terms; the reminder calls it "Urvania's statutory interest" (35-Reminder.xml). The contract, concluded by a Bayvarran authority under "Bayvarra public procurement" (`24-TenderContract.xml:/TenderContract/cbc:RegulatoryDomain`), states payment terms and a penalty against the seller but no interest against the buyer, and a tenderer's standard terms do not normally override the authority's contract. Whether Urvanian statutory interest can be charged to the department is not settled by any document of the flow, yet the buyer pays it (36-RemittanceAdvice.xml).
- Condition: the interest rate on the invoice is one the contract (or the law the contract names) gives the seller; the contract or the notices state it, or the invoice carries none.
- Options: (a, preferred) add the late-payment interest (8 % a year, simple) to the contract's payment terms in 01–03 and 24 and call it contractual in the reminder; (b) base it on a Bayvarran statutory rate and say so.
- Needs decision: yes

### tender/32#F7 · Low · The buyer's forward purchase of ferra, dated before the procedure began, is given as the source of the seller's pricing rate; the payment rate is a rate of the invoice date
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:ExchangeMarketID` = `XLMX`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:Date` = `2026-03-31`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- Why: as in 26#F4 of this part. A forward purchase of ferra is the hedge of the party that must pay in ferra, the buyer, and fixes the conversion of the payment; here the seller cites it for the conversion of its prices, together with an exchange market as the source of the same rate (a rate is either a market fixing or a contract rate). It is dated 2 January 2026, ten days before the prior information notice and two months before it was known that the supplier would be Urvanian. `PaymentExchangeRate` instead carries a rate established on the invoice date for a payment due a month later (and made on 8 May). All rates of the flow are exactly 100, on every date.
- Condition: the foreign exchange contract sits on the rate it fixes and is dated when its need could be known; each exchange rate names one source; the payment rate is one that applies to the payment.
- Options: (a, preferred) move the forward contract to `PaymentExchangeRate`, date it after the award, and keep the market fixing (without contract) for the pricing or tax rate; (b) if the two currencies are pegged at 100, remove the forward contract.
- Needs decision: yes

### tender/32#F8 · Low · A tax representative in Bayvarra, and no Bayvarran tax of the seller on the invoice
- XPath: `/Invoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Invoice/cbc:Note[2]` = `Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra.`
- Why: `TaxRepresentativeParty` is "the Party authorized to act as the Tax Representative for this Invoice". A representative acts for a seller that owes tax in a country where it is not established. The taxes on this invoice are Urvanian VAT (the seller's home tax, categories G and O at 0 %) and a withholding tax that the customer deducts and pays (see 35-Reminder.xml, `PrepaidPayment`); the import is declared by the buyer itself (31-ImportCustomsDeclaration.xml); no Bayvarran sales tax is charged, the buyer being exempt. There is nothing on the invoice for which the seller needs a representative in Bayvarra. The same party appears in 33, 34 and 35.
- Condition: a tax representative is present only on a document that carries a tax the represented party owes in the representative's country, and that tax is identifiable in the document.
- Options: (a, preferred) remove the representative and the note unless the world's rules make the non-resident seller liable for a Bayvarran tax; in that case (b) show that tax (e.g. the state sales tax on the installation, category E, reason PUBLIC) in a tax subtotal.
- Needs decision: yes

### tender/32#F9 · Low · Forty benches are billed at the full price while four of the forty anchor sets that belong to them were not delivered
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `40`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:AdditionalInformation[2]` = `Supplied with four ground anchors and the bolts to fix them.`
- Why: the price of 499 lume is for a bench "supplied with four ground anchors" (the call's line includes the anchor set as a sub-line). The despatch advice of the day before records `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderQuantity` = `4`: four anchor sets follow later. The invoice bills all forty benches as complete, without a note, a retention or a later billing of the four incomplete ones.
- Condition: the invoice either bills only what was delivered complete, or states that the four anchor sets follow at no charge and that the price is unaffected.
- Options: (a, preferred) a note on line 1 that four anchor sets follow within a week at no further charge; (b) bill 36 benches now and four after the back order.
- Needs decision: no

### tender/32#F10 · Low · A charge for a special colour on a line that describes the bench in the default grey
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Special colour`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- Why: the charge (code CAT, "providing a colour which is different from the default colour") is justified only if the benches billed are not in the default colour. The invoice's goods line identifies and describes the bench in Ferro grey, the colour of the original order, not the moss green that was ordered by the change, delivered (29-DespatchAdvice.xml: "Forty benches in moss green, RAL 6005") and charged for. Read on its own, the invoice charges 200.00 lume for a special colour and bills grey benches.
- Condition: the item of the line to which the colour charge belongs is described in the colour charged for.
- Options: (a, preferred) describe the invoiced item as moss green RAL 6005 (variant and physical attribute); (b) none seen.
- Needs decision: no

### tender/32#F11 · Low · The installation is taxed as a service to a business; it is work on land for a public body
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: `SupplyTypeCode` is "a code signifying the type of supply to which this tax category applies"; the world's list has, next to SERVICES, the code WORKS, "construction or installation work on immovable property", which is what anchoring a bench in the ground is. The exemption reason is defined as a "service to a business established outside Urvania"; the customer is a public authority (see 25#F5 of this part). The category O itself (outside the scope of Urvanian VAT) is plausible for work performed in Bayvarra.
- Condition: supply type and exemption reason of the installation line are the codes whose definitions describe installation on land abroad for this kind of customer.
- Options: (a, preferred) supply type WORKS and a reason that covers work on immovable property abroad; (b) keep SERVICES and widen the definition of SVCABROAD to any customer abroad.
- Needs decision: yes

### tender/32#F12 · Low · The installation is said to be done by the manufacturer's installers; the award says a Bayvarran subcontractor does it
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- XPath: `/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `Withholding tax on services of non-residents`
- Why: the award and the contract state `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`, and Saltmere is registered in Bayvarra (15-Tender.xml, subcontractor party). The invoice bills the same 18 lume a bench as work "by the manufacturer's installers". The point matters for the money because the 10 % withholding rests on the service being one of a non-resident: it is invoiced by the non-resident seller, so the withholding can stand, but the description contradicts who performs the work.
- Condition: the description of the installation agrees with the subcontract terms of the award, and the withholding is consistent with who supplies the service to the buyer.
- Options: (a, preferred) reword to "by the manufacturer's subcontractor"; (b) none seen.
- Needs decision: no

## Checked and consistent
- Lines: 40 × 499 = 19960.00; 40 × 18 = 720.00; sum 20680.00 = `LineExtensionAmount`. Charge 200.00 = `ChargeTotalAmount`; 20680.00 + 200.00 = 20880.00 = `TaxExclusiveAmount`; tax 0.00, so `TaxInclusiveAmount` 20880.00; withholding 10 % of 720.00 = 72.00 (document, line 2 and monetary total agree); 20880.00 − 72.00 = 20808.00 = `PayableAmount`.
- Tax total in lume: G 19960.00 + 200.00 = 20160.00, O 720.00, together 20880.00; tax amounts 0.00.
- Settlement discount: 2 % of 20880.00 = 417.60; settlement period 31 March to 10 April = the note's ten days; 31 March + 30 days = 30 April, the same date in `DueDate`, `PaymentMeans/PaymentDueDate` and `PaymentTerms/PaymentDueDate`.
- Prices 499 and 18 lume = winning tender (119760.00 / 240, 4320.00 / 240) = catalogue at 0.01; the colour charge 200.00 with code CAT = 27 and 28. The amount 20680.00 of the lines is the notices' average release.
- Exchange rates: XUF → XBL × 0.01 and XBL → XUF × 100 are inverse; tax rate dated on the tax point date.
- Payment means: credit transfer; reference RF48VIINV260221 has correct check digits (ISO 11649) and is the one the remittance advice quotes; account XU79…9458 has correct check digits, is in ferra like the payment currency, and is the same account, holder, branch and bank in 27, 35 and 36; `PaymentTerms/PaymentMeansID` 1 = `PaymentMeans/ID`.
- Later documents use the payable amount 20808.00 unchanged (35-Reminder.xml line 1, 36-RemittanceAdvice.xml line 1).
- Tax category G with reason EXP, scheme VAT, 0 %, supply type GOODS on line 1 and on the charge: consistent with the export declaration of the same goods (30).
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount`: defined as "the sum of payable amount and prepaid amount", which would be 20808.00 — refuted because the difference is the withholding tax, which UBL totals separately (`WithholdingTaxTotalAmount`); 20880.00 − 72.00 = 20808.00 holds.
- `/Invoice/cbc:PaymentCurrencyCode`: payment in ferra, but no amount in ferra is stated — refuted because the payment exchange rate is given and the amount follows (2080800 ferra); whether that rate is the right one is F7.
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: the discount is calculated on the amount before withholding — refuted: the note names no base, and the gross amount is a legitimate one; the discount was not taken.
- `/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID`: category S ("Standard rate") and scheme OTH ("Other taxes") for a withholding tax — refuted because the scheme is named in text, the rate is its standard rate, and UN/EDIFACT 5153 has no code for withholding on services that the world would have to prefer.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: a real-time net settlement channel for a payment between two currencies — refuted: the rail named is the Trade Accord's, a regional scheme of the fictional world, and nothing in the flow contradicts it.
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: CREVXUFR has the shape of a BIC — refuted as a clash with a real register because its country part is the user-assigned code XU.
- `/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID`: the colour charge under the export category — refuted because the colour is a property of the exported goods; that the customs value leaves it out is a finding of 30 and 31.

## Outside this review
- Timeline: the invoice is issued at 09:28 on 31 March, the morning after the despatch and before the import clearance (11:14) and the installation, and bills the installation of all forty benches; its tax point is the same day. Whether a release can be invoiced before it is installed and accepted is a question of the timeline across 29, 31, 32 and 34.
