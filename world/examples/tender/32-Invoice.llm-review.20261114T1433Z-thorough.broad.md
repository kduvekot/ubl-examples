# LLM review: 32-Invoice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/32-Invoice.xml`, Git blob `670ec0ba9b4bae748393682c8030e3f46b70c018` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 20523a0 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/32#F1 · High · The installation of 40 benches is billed although it was not ordered and cannot yet have been done
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- XPath: `/Invoice/cbc:IssueTime` = `09:28:00`
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-03-31`
- Why: the invoice refers to order LPWD-PO-26-0212, which has one line, the benches (`26-Order.xml:/Order/cbc:LineCountNumeric` = `1`); neither it nor the order change orders an installation, and line 2 accordingly has no order line reference. The service also cannot have been supplied when it is billed: the benches left Ferrano on 2026-03-30 at 17:37 (29), the import declaration is lodged on 2026-03-31 at 11:14 (31), after this invoice, and the despatch advice says of four missing anchor sets `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderReason` = `The galvanising of the last batch is late; the sets follow within a week, before the installers need them.` Finally the description says the manufacturer's installers do the work, while the contract has Saltmere Engineering install as subcontractor (`24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description`).
- Condition: the invoice bills only what was ordered and supplied by its tax point; the installation is billed when done, against an order that covers it, and its description agrees with the contract on who installs.
- Options: (a) remove line 2 (with its withholding tax and tax subtotal) from this invoice and bill the installation later (preferred; totals in 33–36 follow); (b) add the installation to the order and move the invoice after the installation.
- Needs decision: yes (whether and when release 1 is installed)

### tender/32#F2 · High · A charge for the special colour on an item identified as the grey standard variant
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Special colour`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: the invoice charges 200.00 for the special colour (moss green RAL 6005, order change 27, despatched as such, 29) and in the same document identifies the invoiced benches as variant GRY with a grey frame. The charge and the item contradict each other.
- Condition: the invoiced item's variant and colour are those delivered, for which the charge is made.
- Options: (a) the green variant in ExtendedID, PhysicalAttribute and the colour property (preferred).
- Needs decision: no

### tender/32#F3 · High · Pricing currency is ferra, but the prices are in lume
- XPath: `/Invoice/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `18`
- Why: PricingCurrencyCode is "A code signifying the currency used for prices in the Invoice". Both prices carry `currencyID="XBL"`; in ferra they are 49900 and 1800 (catalogue 25). The line-level exchange rates (XUF to XBL, 0.01) show the prices were converted out of the pricing currency.
- Condition: every PriceAmount is in the currency PricingCurrencyCode names, or the code is absent.
- Options: (a) prices 49900 and 1800 XUF, with the exchange rate explaining the line amounts (preferred); (b) drop PricingCurrencyCode and the pricing exchange rates.
- Needs decision: no

### tender/32#F4 · High · The tax total in ferra declares everything as export of goods
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `2088000`
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `720.00`
- Why: the tax total in the document currency splits the base into 20160.00 export of goods (category G) and 720.00 service outside scope (category O). The tax total in the tax currency has one subtotal, category G "Export of goods outside Urvania", with a base of 2088000 XUF = 20880.00 XBL, i.e. it includes the 72000 XUF of the installation service. The same invoice thus reports the service once as outside scope and once as exported goods; the ferra total is the one meant for the Urvanian tax authority.
- Condition: the subtotals of the tax-currency total have the same categories and (converted) bases as those of the document-currency total: 2016000 XUF in G and 72000 XUF in O.
- Options: (a) two subtotals in TaxTotal[2] (preferred); (b) none other seen.
- Needs decision: no

### tender/32#F5 · High · The seller's standard payment terms instead of the contract's
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-30`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- Why: the invoice is under the framework contract (`/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`), whose payment terms are `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` and whose order change adds "The framework contract's conditions apply." The invoice applies Valdara's standard terms (ID XU-STD, with a link to its general terms): 30 days from the invoice date, a 2 % discount and 8 % penalty interest, none of which the contract contains. The due date 2026-04-30 is counted from the invoice date, issued before the goods had even been imported, not from the acceptance of the release. The reminder (35) then claims interest from this due date.
- Condition: payment terms, due date and penalty of the invoice are those of the contract (or the contract is changed to contain them).
- Options: (a) terms "30 days after acceptance of the release", due date from the acceptance, no discount and no contractual interest beyond what the contract or law gives (preferred; 35 and 36 follow); (b) put the seller's terms into the contract documents.
- Needs decision: yes (which payment terms the world's contract has; same question as in 27)

### tender/32#F6 · Medium · Emission factor that does not lead to the emission value
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × the base of 1 bench is not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state. Same block as in the catalogue (25).
- Condition: factor × the stated base or activity gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric (preferred); (b) state the activity.
- Needs decision: no

### tender/32#F7 · Medium · Language code in LocaleCode; provinces in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; provinces are in CountrySubentity.
- Options: (a) a locale code, and move the provinces (preferred).
- Needs decision: no

### tender/32#F8 · Low · A tax representative with no tax registration and no tax to represent
- XPath: `/Invoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Invoice/cbc:Note[2]` = `Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra.`
- Why: the tax representative is "The Party authorized to act as the Tax Representative for this Invoice". It is given by register number and name only: no tax registration number, no tax scheme, no address, which is what identifies a representative to a tax authority. The invoice charges no Bayvarran tax at all (only Urvanian VAT categories G and O at 0 %); the one Bayvarran tax in it, the withholding tax on the service, is withheld by the customer. What the representative represents is not visible; in the order change (27) the same company is the freight forwarder.
- Condition: a tax representative is present only where a tax of its country is declared through it, and carries its tax registration there.
- Options: (a) remove the tax representative and the note (preferred, also in 33–35); (b) give Bayforth's STT registration and show the Bayvarran tax it accounts for.
- Needs decision: yes (what Bayforth Forwarding does for Valdara)

### tender/32#F9 · Low · The seller quotes the buyer's forward exchange contract as pricing rate
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:Date` = `2026-03-31`
- Why: as in 26–28: a forward purchase of ferra is the paying department's contract with its bank and fixes a payment rate; it is attached to the pricing rate, stated by the seller, and dated before the procedure began. The payment rate (XBL to XUF, the payment currency) is given as a spot rate of the invoice date without the contract.
- Condition: a foreign exchange contract is stated by a party to it on the rate it fixes, with a plausible date.
- Options: (a) remove it from the seller's invoice (preferred); (b) attach it to the payment rate in the buyer's documents.
- Needs decision: yes (whether and when the department hedges)

### tender/32#F10 · Low · No reference to the despatch, no delivery; contract and originator carry the same ambiguous number; a buyer reference no buyer document gave
- XPath: `/Invoice/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `PWD-PARKS-26-AP`
- Why: the invoice does not cite the despatch advice CL-DA-26-0215 or say when and where the goods were delivered, although the credit note later cites that advice. The contract reference uses the number that is also the procurement file and project (24 identifies the contract document as LPWD-DOC-26-0210 / PWD-CONTRACT-2026-PARKS), and the originator reference repeats it without a type. BuyerAssignedReference is "A reference provided by the buyer used for internal routing"; the order and order change give only the cost code PWD-PARKS-26, never this accounts-payable code.
- Condition: the invoice cites the despatch advice; the contract reference uses the contract's identifier; a buyer reference is one the buyer provided in the order.
- Options: (a) add DespatchDocumentReference, drop the originator reference, and give the buyer reference in the order (preferred).
- Needs decision: no

### tender/32#F11 · Low · Catalogue content on the invoice line; the department as a company
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: the invoice line repeats the catalogue's keywords, test method, dimensions, emissions and circularity profile, which billing does not use. The customer, a municipal department, carries a company liquidation status and a commercial-register type.
- Condition: the invoiced item is identified and described; catalogue content is absent; no liquidation status on the department.
- Options: (a) reduce the item; correct the department's legal entity (preferred).
- Needs decision: no

## Checked and consistent
- Arithmetic: 40 × 499 = 19960.00; 40 × 18 = 720.00; lines 20680.00; + charge 200.00 = 20880.00 tax exclusive = tax inclusive (tax 0.00); withholding 10 % × 720.00 = 72.00; payable 20880.00 − 72.00 = 20808.00. Tax bases: 19960.00 + 200.00 = 20160.00 (G), 720.00 (O). 20880.00 × 100 = 2088000 XUF.
- Settlement discount 2 % × 20880.00 = 417.60; settlement period 2026-03-31 to 2026-04-10 is "within 10 days"; due date 2026-04-30 = issue date + 30 days, the same in DueDate, PaymentMeans and PaymentTerms.
- Order reference LPWD-PO-26-0212 (26), line 1, 40 benches at the contract price; charge 200.00 with reason CAT as agreed in 27 and 28.
- Payment: credit transfer (30) to Valdara's ferra account, the account of the order change; payment currency XUF equals the account's currency; RF48VIINV260221 is a valid ISO 11649 reference built from the invoice number; channel RTNS and charge bearer SHAR are ISO 20022 codes.
- Tax: export of goods from Urvania at 0 % (G) with the supply type GOODS, service outside scope (O) with SERVICES; reasons in Urvanian and English; the withholding tax is on the service line only and repeated at line level.
- Annotation "First release: 40 benches; 200 remain." agrees with the framework's 240.
- Supplier and customer as in the order; check_ids.py: ISIN, RF reference and IBAN-like account correct.

## Considered and refuted
- `/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID`: OTH for a withholding tax — refuted, UNTDID 5153 has no code for a withholding tax on services and the scheme is named.
- `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode`: "Service to a business" for a public body — refuted as undecidable from the examples (see 25); the Urvanian rule turns on the customer being abroad.
- `/Invoice/cac:TaxTotal[1]/cbc:TaxAmount`: no Bayvarran state sales tax shown — refuted, the seller is not registered in Bayvarra and the customer is exempt (PartyTaxScheme PUBLIC).
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: computed on 20880.00, not on the payable 20808.00 — refuted, a discount on the invoice total before withholding is a legitimate convention.
- `/Invoice/cbc:DefaultLanguageCode`: en while the supplier's language is Urvanian — refuted, untagged texts of the invoice are English.
- `/Invoice/cac:PaymentMeans/cbc:PaymentRailID`: fictional rail — accepted as the world's.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType`: master data — the seller's own statement about itself; left.

## Outside this review
- The invoice is issued (2026-03-31 09:28) before the import declaration (11:14) and before any acceptance of the release; whether the benches had arrived is a timeline question.
