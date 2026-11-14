# LLM review: 32-Invoice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/32-Invoice.xml`, Git blob `670ec0ba9b4bae748393682c8030e3f46b70c018` (committed)
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

### tender/32#F1 · High · Forty installations are billed against an order that does not contain them
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Name[2]` = `Installation of a park bench`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `20880.00`
- Why: `OrderReference` is "A reference to the Order with which this Invoice is associated". That order has one line, 40 benches (`26-Order.xml:/Order/cbc:LineCountNumeric` = `1`), and after the colour change the seller accepted it at `28-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`. Invoice line 1 refers to order line 1; line 2, 40 installations, has no order line reference, and nothing in 26, 27 or 28 orders it. The invoice amount before withholding (20880.00) is 720.00 above the total the seller itself accepted six days earlier.
- Condition: Every invoice line corresponds to a line of the order as changed and accepted (with an order line reference), or to another ordering document of the flow that the invoice names; the amount before withholding equals what was ordered.
- Options: (a) add the installation as a second line to the order, its change and response, and give invoice line 2 its order line reference (preferred by money, context and logistics); (b) a separate order for the installation, referenced from line 2; (c) drop line 2 from this invoice and bill the installation later (preferred by broad). All change the story: 33 to 36 build on the invoiced installation.
- Needs decision: yes
- From: broad (F1), money (F1), logistics (F1), context (F4)

### tender/32#F2 · High · The installation is invoiced, with that day as tax point, before it can have been done
- XPath: `/Invoice/cbc:IssueTime` = `09:28:00`
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-03-31`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`
- Why: Line 2 bills the anchoring of 40 benches in Lumeport on the morning of 31 March. The benches left Urvania at 17:37 the evening before (`29-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `17:37:00`), their import was declared at 11:14 that day (`31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `11:14:00`), and four anchor sets were on back order (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderReason` = `The galvanising of the last batch is late; the sets follow within a week, before the installers need them.`). The debit note later charges a penalty for late installation (`34-DebitNote.xml:/DebitNote/cbc:Note` = `Penalty for late installation under the contract's clause PEN-1.`). The invoice has no delivery or invoice period that would say the service is billed in advance. Rated High (broad and logistics, who folded it into F1; context said Low as a timeline question): the tax point states the installation as supplied by 31 March, while 29 says the installers have not yet needed the anchors and 34 charges a delay of the same installation; a statement in this example that two other examples of the flow contradict (section 6). Kept apart from F1 because the condition differs (when, not whether, it was ordered).
- Condition: The installation is invoiced after it has been done (and accepted), or the invoice states that it is billed in advance and the contract allows that.
- Options: (a) bill the installation later, in its own invoice (preferred); (b) issue this invoice after installation and acceptance.
- Needs decision: yes
- From: context (F10), broad (F1), logistics (F1)

### tender/32#F3 · High · A special-colour charge on benches identified as the standard grey variant
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Special colour`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The charge (code CAT, "Special colour service") is for the moss green of the order change (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), accepted in 28 and despatched so (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`). In the same invoice the benches are the grey variant, the default colour for which no charge is due. The invoice contradicts itself and the despatch.
- Condition: The invoiced item's variant and colour are those delivered and charged for (moss green, RAL 6005).
- Options: (a) the green variant in ExtendedID, PhysicalAttribute and the colour property (preferred, all parts); (b) remove colour data from the line (context's alternative), which leaves the charge without its object, so not preferred here.
- Needs decision: no
- From: broad (F2), money (F10), logistics (F2), context (F1)

### tender/32#F4 · High · In the tax currency the whole invoice, installation included, is declared as export of goods
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `2088000`
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`
- XPath: `/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `720.00`
- Why: The tax total in lume splits the base into 20160.00 in category G (export of goods) and 720.00 in category O (service outside scope, SVCABROAD). The tax total in ferra, the tax currency the Urvanian return uses, has a single subtotal of 2088000 XUF = 20880.00 × 100, all in G with reason "Export of goods outside Urvania". Recomputed: at the invoice's tax rate of 100 the subtotals would be 2016000 (G) and 72000 (O). The same invoice reports the installation once as outside scope and once as exported goods.
- Condition: The tax-currency total has the same subtotals (category, reason) as the document-currency total, each taxable amount converted with `TaxExchangeRate`.
- Options: two subtotals in ferra, 2016000 (G, EXP) and 72000 (O, SVCABROAD) (preferred; no other seen).
- Needs decision: no
- From: broad (F4), money (F2)

### tender/32#F5 · High · The seller's standard payment terms and interest instead of the contract's
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentTermsDetailsURI` = `https://www.valdara.example/terms`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-30`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- XPath: `/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: The invoice is issued under the framework contract, whose term is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` (the same in `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.`). It applies instead Valdara's standard terms (ID XU-STD, details on Valdara's website): 30 days from the invoice date (31 March + 30 = 30 April, in DueDate, PaymentMeans and PaymentTerms), a 2 % discount and 8 % a year penalty interest, none of which the contract contains. On 31 March the release was neither delivered nor accepted (despatched the evening before, cleared for import at 11:14, four anchor sets on back order, installation late per 34), so under the contract the due date lies 30 days after an acceptance in April. The order change words the term a third way (`27-OrderChange.xml:/OrderChange/cac:PaymentTerms/cbc:Note` = `30 days after the invoice, as the contract says.`). The interest has consequences: the reminder charges it from 1 May as "Urvania's statutory interest" (35), and the buyer pays it (36); the contract, concluded under Bayvarran procurement law, names no interest against the buyer, so neither the seller's terms nor Urvanian law obviously apply (money F6, own knowledge: an authority's contract terms prevail over a tenderer's standard terms).
- Condition: The invoice's payment terms, due date (in all three places) and penalty interest are those the contract yields, or the contract states the seller's terms; a discount may be offered in addition.
- Options: (a) contract terms "30 days after acceptance of the release", with the acceptance recorded in the flow (a date in a note or a receipt advice) and the due date derived from it; 35 and 36 follow (preferred by broad, money, context); (b) change the contract's term to "30 days after the invoice" (01–03, 24) and add the late-payment interest to it, which makes 27 and this invoice right (money's alternative for both the term and the interest); (c) base the interest on a stated Bayvarran statutory rate.
- Needs decision: yes
- From: broad (F5), money (F3, F6), context (F2); logistics left it to money

### tender/32#F6 · High · The pricing currency is the ferra; both prices are in lume
- XPath: `/Invoice/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `18`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for prices in the Invoice". Both prices carry `currencyID="XBL"`; in ferra they would be 49900 and 1800 (as in 25). Two values of the same document contradict each other (section 6 High). The tendered and contracted prices are in lume (499 and 18, money), so the pricing currency is in fact the document currency, and neither the code nor the pricing exchange rates (F9, F14) have anything to convert.
- Condition: Every `PriceAmount` is in the currency `PricingCurrencyCode` names; if that is the document currency, there is no `PricingCurrencyCode` or `PricingExchangeRate`.
- Options: (a) drop `PricingCurrencyCode` and the pricing exchange rates (preferred by money and context: the contract is in lume, as tendered); (b) state the prices in ferra, 49900 and 1800 XUF (broad).
- Needs decision: no
- From: broad (F3), money (F4), context (F3)

### tender/32#F7 · High · Emission factor × base does not give the emission value
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg; 96 / 0.82 = 117.07 of an unstated activity. 39 files carry factor 0.82.
- Condition: factor × base = value, or factor and base are absent.
- Options: (a) drop factor and base (preferred); (b) a real factor and its activity.
- Needs decision: no
- From: broad (F6), logistics (F3)

### tender/32#F8 · Medium · "By the manufacturer's installers" although the award has a subcontractor install
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The award and the contract say `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`, and the tender names the subcontractor (`15-Tender.xml:/Tender/cac:SubcontractorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`, a Bayvarran company). The invoice bills the same 18 lume a bench as work "by the manufacturer's installers". Context rated it High (a statement another example contradicts), parties Medium, money Low. The merge takes Medium: the phrase can be read loosely as "installers engaged by the manufacturer", so it is not a hard contradiction, but as written it names the wrong party for the work the document bills. The withholding on "services of non-residents" can stand, since the non-resident seller invoices the service (money). The text comes from the catalogue (25).
- Condition: The description of the installation does not attribute the work to a party other than the one the tender and award name, in both language versions.
- Options: (a) "by the supplier's installation subcontractor", or no statement of who installs (preferred); (b) remove the subcontractor from the tender and award documents, if the manufacturer's own staff install (changes the story).
- Needs decision: no
- From: parties (F3), context (F5), money (F12), broad (F1)

### tender/32#F9 · Medium · Each price repeats the document's pricing exchange rate, with base rates of 1
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyBaseRate` = `1`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:TargetCurrencyBaseRate` = `1`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- Why: `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". Both line rates have the document's currencies, rate (0.01) and date (2026-01-02): the definition's condition is not met. The base rates ("In the case of a source currency with denominations of small value, the unit base") are 1, the default. And the prices are in lume (F6), so no rate applies to them. Medium, as the sea merge D decided for exchange rates whose own condition is not met.
- Condition: A price-level exchange rate is present only where it differs from the document's; base rates only with a value the rate refers to.
- Options: remove the price-level exchange rates (preferred; no other seen).
- Needs decision: no
- From: money (F5), context (F6)

### tender/32#F10 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: "A code signifying whether a piece of transport equipment is full, partially full, or empty. …" The value is a footprint system boundary for a bench.
- Condition: The element holds a fullness of transport equipment or is absent.
- Options: (a) remove it, keep the boundary in the lifecycle stage description (preferred); (b) in addition, record the missing boundary element for the TC write-up.
- Needs decision: no
- From: context (F7)

### tender/32#F11 · Medium · A province in `Region`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity`. 219 occurrences in 104 files.
- Condition: The province is in `CountrySubentity`; `Region` is absent or holds a region in the sense of the definition.
- Options: move it to `CountrySubentity` (preferred); or record a postal-region convention (parties' alternative).
- Needs decision: no
- From: broad (F7), parties (F1), context (F8)

### tender/32#F12 · Medium · A language code as locale
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code. 362 occurrences in 213 files.
- Condition: No `LocaleCode` holds a bare language code.
- Options: (a) remove it (preferred by parties and context); (b) a real locale from a locale list (broad).
- Needs decision: no
- From: broad (F7), parties (F2), context (F9)

### tender/32#F13 · Medium · The department described as a company in a commercial register, with a liquidation status
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The customer is a municipal department (ISIC 8411). A liquidation status ("A code signifying the party's liquidation status") and a register typed "Commercial register" do not fit a public body; the register number itself is not questioned.
- Condition: The department carries no liquidation status, and its register is not typed as commercial.
- Options: (a) drop the status and type the register neutrally (preferred); (b) reduce the legal entity to name and identifier.
- Needs decision: no
- From: parties (F8), context (F14), broad (F11)

### tender/32#F14 · Low · The buyer's forward exchange contract on the seller's pricing rate, dated before the procedure
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:ExchangeMarketID` = `XLMX`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:Date` = `2026-03-31`
- Why: A forward purchase of ferra is the hedge of the party that must pay in ferra, the buyer, with its bank; it fixes a payment rate. Here the seller cites it as the source of its pricing rate, next to an exchange market as source of the same rate (a rate is either a market fixing or a contract rate), dated 2 January 2026, before the prior information notice and before it was known that the supplier would be Urvanian. The payment rate (XBL to XUF, the payment currency) is a spot rate of the invoice date without the contract, for a payment made on 8 May (36). Same block as in 26–28.
- Condition: A foreign exchange contract is stated by a party to it, on the rate it fixes, dated when its need could be known; each rate names one source.
- Options: (a) remove it from the seller's invoice with the pricing rate (F6) (preferred by broad and context); (b) attach it to the payment rate in the buyer's documents, dated after the award (money); (c) if XUF and XBL are pegged at 100, remove the forward contract.
- Needs decision: yes
- From: broad (F9), money (F7), context (F11)

### tender/32#F15 · Low · A tax representative with no registration and no Bayvarran tax to represent
- XPath: `/Invoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Invoice/cbc:Note[2]` = `Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra.`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Invoice", a party accounting for tax on behalf of a supplier not established where the tax is due. It is given by register number and name only: no tax scheme, no registration, no address. The taxes on the invoice are Urvanian VAT (not charged: export, service abroad) and a Bayvarran withholding tax that the customer withholds itself (`/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `Withholding tax on services of non-residents`); no state sales tax is charged (the customer is exempt) and the buyer is its own importer (31). Nothing on the invoice needs a representative. The same party is freight forwarder in 27 and does no forwarding in the flow; that a forwarder acts as fiscal representative is common practice (parties), so the choice of party is not questioned. The same in 33, 34 and 35.
- Condition: A tax representative appears only where the document carries a tax it accounts for, with its tax registration; otherwise party and note are absent.
- Options: (a) remove the representative and the note (preferred by broad, money, context); (b) give Bayforth's STT registration and show the Bayvarran tax it accounts for (e.g. state sales tax on the installation, category E, reason PUBLIC), if the world's rules make the non-resident seller liable (parties' preference if the representation is part of the story).
- Needs decision: yes
- From: broad (F8), money (F8), parties (F9), context (F12)

### tender/32#F16 · Low · The installation is taxed as a service to a business; it is work on land for a public body
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- Why: `SupplyTypeCode` is "A code signifying the type of supply to which this tax category applies"; the world's list has WORKS, "Construction or installation work on immovable property." (`world/codelists/world-codes.json`), which is what anchoring a bench in the ground is. SVCABROAD is "Service to a business established outside Urvania"; the customer is a public authority. Category O itself is plausible for work performed in Bayvarra. Counter-argument (broad): whether SVCABROAD covers a public body is undecidable from the examples; the Urvanian rule turns on the customer being abroad.
- Condition: Supply type and exemption reason are the codes whose definitions describe installation on land abroad for this kind of customer.
- Options: (a) WORKS and a reason that covers work on immovable property abroad (preferred); (b) keep SERVICES and widen the definition of SVCABROAD to any customer abroad.
- Needs decision: yes
- From: money (F11); broad's refutation of the exemption reason carried as counter-argument

### tender/32#F17 · Low · Forty benches billed complete while four anchor sets are on back order
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `40`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:AdditionalInformation[2]` = `Supplied with four ground anchors and the bolts to fix them.`
- Why: The price is for a bench "supplied with four ground anchors". The despatch advice of the day before records `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderQuantity` = `4`. The invoice bills all forty as complete without a note or retention.
- Condition: The invoice bills only what was delivered complete, or states that the four anchor sets follow at no charge.
- Options: (a) a note on line 1 that four anchor sets follow within a week at no further charge (preferred); (b) bill 36 benches now and four after the back order.
- Needs decision: no
- From: money (F9)

### tender/32#F18 · Low · No despatch reference and no delivery date
- XPath: `/Invoice/cac:OrderReference`
- Why: The invoice cites order, contract and project but not the despatch advice CL-DA-26-0215 under which the benches travel, and has no `cac:Delivery` with an actual delivery date, although the contract's payment term counts from "each accepted release" (F5) and the credit note (33) cites the despatch advice. Missing details the document could carry.
- Condition: The invoice references the despatch advice and states the delivery date.
- Options: `cac:DespatchDocumentReference` CL-DA-26-0215 and `cac:Delivery/cbc:ActualDeliveryDate` (preferred).
- Needs decision: no
- From: logistics (F4), broad (F10)

### tender/32#F19 · Low · Contract cited by the procurement file number, repeated as "originator document"; a buyer reference no buyer document gave; programme code differs from the procurement documents
- XPath: `/Invoice/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `PWD-PARKS-26-AP`
- XPath: `/Invoice/cac:ProjectReference/cbc:ID` = `PWD-PARKS-26`
- XPath: `/Invoice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- Why: PWD-2026-PARKS is the procurement file (`24-TenderContract.xml:/TenderContract/cbc:ContractFolderID` = `PWD-2026-PARKS`); the contract document is `24-TenderContract.xml:/TenderContract/cbc:ID` = `LPWD-DOC-26-0210` with the contract reference `24-TenderContract.xml:/TenderContract/cac:ContractDocumentReference/cbc:ID` = `PWD-CONTRACT-2026-PARKS`. The originator reference ("A reference to an originator document associated with this document") repeats the same number without a type. `BuyerAssignedReference` is "A reference provided by the buyer used for internal routing of the document"; the order and order change give no such code. The programme is coded `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` in the procurement documents, here PWD-PARKS-26, used both as project ID and accounting code.
- Condition: The contract reference uses the contract's identifier; the originator reference names another document with its type, or is absent; the buyer reference is one the buyer provided; one code for the programme throughout the flow.
- Options: (a) contract reference PWD-CONTRACT-2026-PARKS, drop the originator reference, give the buyer reference in the order, one programme code (preferred); (b) keep PWD-2026-PARKS and type the reference as the procurement file.
- Needs decision: no
- From: broad (F10), logistics (F5, F6), context (F13)

### tender/32#F20 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: Here (issued in Urvania) the English renderings are tagged `en-XU` and the legal form is in `qau` and `en-XU`; in the Bayvarran-issued examples the same texts are tagged `en-XB` and the legal form appears once, untagged (`03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`). The tag follows the issuer, not the text. Could not be settled.
- Condition: The same rendering carries the same `languageID` in every example, or the rule is stated.
- Options: (a) `en-XU` everywhere (preferred); (b) the issuer-dependent tag, applied uniformly and documented.
- Needs decision: yes
- From: parties (F4)

### tender/32#F21 · Low · Accounting parties described with their procurement and sales contacts
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: For a billing document the people concerned book and pay; the invoice itself names the department's unit for that (`/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`), yet the customer is addressed to the head of procurement and the supplier's contact is the sales order desk, as in the tender and order documents.
- Condition: In billing documents the accounting customer's contact and attention are those of the unit that handles invoices, and the supplier's contact handles receivables (or they are absent).
- Options: (a) accounts contacts (preferred); (b) drop `Contact`, `Department` and `MarkAttention`.
- Needs decision: no
- From: parties (F5)

### tender/32#F22 · Low · Supplier's master data that an invoice does not use
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: An invoice identifies the supplier for accounting and tax. The warehouse provider (with a contact that has a name and no means of contact), the listing and whether shares are fully paid are not used (section 4.8). The issuer's own share capital on its own invoice is accepted by earlier merges (analysis/review-merge-decisions.md), so it is listed for completeness only. Counter-arguments: parties refuted the listing as part of a listed company's legal description; broad left the service provider as "the seller's own statement about itself".
- Condition: Listing and service provider appear only in documents whose purpose uses them.
- Options: (a) remove them here (preferred; share capital may stay as the issuer's own); (b) keep those for which a use can be stated.
- Needs decision: no
- From: parties (F6), context (F15)

### tender/32#F23 · Low · Party tax exemption reason worded as a transaction
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` these are "A reason for the party's exemption from tax"; code and text describe a sale. Only the second half of the text is the party's status.
- Condition: The party-level reason states the party's status, in code and text.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F7)

### tender/32#F24 · Low · The whole catalogue description of the item on the invoice line
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:Dimension[4]`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: An invoice line needs identification, description, quantity, price and tax category; the line repeats the full catalogue entry of `25-Catalogue.xml` (keywords, load test, seat-height range, emissions, circularity profile). F7 and F10 come along with it.
- Condition: The item carries what the invoice uses.
- Options: (a) reduce the item (preferred); (b) keep the full copy everywhere and record that decision (context's alternative).
- Needs decision: no
- From: context (F16), broad (F11)

## Checked and consistent
- Arithmetic (re-done in the merge): 40 × 499 = 19960.00; 40 × 18 = 720.00; lines 20680.00; + charge 200.00 = 20880.00 = tax exclusive = tax inclusive (tax 0.00); withholding 10 % × 720.00 = 72.00 (document, line 2, total); 20880.00 − 72.00 = 20808.00 payable. Lume tax bases 19960.00 + 200.00 = 20160.00 (G) and 720.00 (O). Ferra total 20880.00 × 100 = 2088000 (its split is F3).
- Settlement discount 2 % × 20880.00 = 417.60; settlement period 31 March–10 April = ten days; 31 March + 30 = 30 April in DueDate, PaymentMeans and PaymentTerms (whether that is the right term is F4).
- Prices 499 and 18 = winning tender (money); charge 200.00, code CAT, as in 27 and 28; annotation "First release: 40 benches; 200 remain." = 240 − 40.
- Exchange rates XUF→XBL × 0.01 and XBL→XUF × 100 are inverse; tax rate dated on the tax point.
- Payment: credit transfer (30) to Valdara's ferra account, the same account, holder, branch and bank in 27, 35 and 36; payment currency = account currency; `PaymentTerms/PaymentMeansID` 1 = `PaymentMeans/ID`. `check_ids.py` (re-run): ISIN, RF48VIINV260221 (ISO 11649) and the IBAN-like account correct.
- Later documents use the payable amount 20808.00 unchanged (35 line 1, 36 line 1).
- Category G, reason EXP, VAT 0 %, supply type GOODS on line 1 and the charge: consistent with the export declaration's goods (30; its value is 30/F4).
- `OrderReference` and line 1's order line reference resolve to the order and its bench line. Type 380; `LineCountNumeric` 2 = two lines; PaymentMeansCode 30; CAT for the colour charge.
- Parties: supplier/seller Valdara (signs), customer/buyer the department; identifiers the same in every example of the flow (parties, by script); Bayforth's identifier 20411644 the same in all five examples that carry it.

## Considered and refuted
- `/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID`: OTH and category S for a withholding tax — refuted, UNTDID 5153 has no code for withholding on services and the scheme is named; S is its standard rate (from broad, money).
- `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode`: "Service to a business" for a public body — refuted by broad as undecidable; money raised it with the supply type: F16, with broad's argument.
- `/Invoice/cac:TaxTotal[1]/cbc:TaxAmount`: no Bayvarran state sales tax — refuted, the seller is not registered in Bayvarra and the customer is exempt (from broad).
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: computed on 20880.00, not 20808.00 — refuted, the note names no base and the gross amount is a legitimate one (from broad, money).
- `/Invoice/cbc:DefaultLanguageCode`: en while the supplier is Urvanian — refuted, untagged texts are English (from broad).
- `/Invoice/cac:PaymentMeans/cbc:PaymentRailID`: fictional rail — accepted as the world's (from broad).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType`: master data — left by broad as the seller's own statement; the merge keeps it in F22 with parties and context.
- `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount`: "the sum of payable amount and prepaid amount" would be 20808.00 — refuted, the difference is the withholding, totalled separately (from money).
- `/Invoice/cbc:PaymentCurrencyCode`: no amount in ferra — refuted, the payment rate gives 2080800 ferra (from money).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTNS for a cross-currency payment — refuted, the Trade Accord rail is regional and nothing contradicts it; the list is the repository's decision (from money, context).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: shape of a BIC — refuted, country part XU is user-assigned (from money, parties).
- `/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID`: the colour charge under the export category — refuted, the colour is a property of the exported goods (from money; the customs value is 30/F4, 31/F6).
- `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: forward contract before the procedure — logistics raised it only in 26; money, broad and context raised it here: F14 (from logistics).
- `/Invoice/cbc:IssueTime`: invoice before the import (11:14) — refuted for the goods, invoicing at despatch is usual and the tax point of an export is the despatch; it holds only for the installation, F2 (from logistics).
- `/Invoice/cac:PaymentTerms/cbc:Note`: terms from the invoice date — left by logistics to money: F5 (from logistics).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` (`-1`): malformed — refuted, text offset used throughout (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`: real country code — refuted, +999 not assigned (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: master data — refuted by parties as part of the legal entity; kept in F22; check digit and fictional prefix confirmed.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: real ICD — refuted (from parties).
- `/Invoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name`: a forwarder as tax representative — refuted, forwarders commonly act as fiscal representatives; what is missing is F15 (from parties).
- `/Invoice/cac:Annotation/cbc:AnnotationContent`: "200 remain" although not ordered — refuted, informative text about the framework (from context).
- `/Invoice/cac:WithholdingTaxTotal`: withholding on a service billed by a non-resident — refuted, fits the scheme's name (from context; money confirms the withholding can stand, see F8).
- `/Invoice/cac:BuyerAssignedReference`: an accounts-payable routing reference — refuted as to presence, that is what the element is for (from context); where the code comes from is F19.
- `/Invoice/cbc:TaxPointDate`: equal to the issue date — refuted, legitimate (from context); for the installation see F2.

## Refuted in the merge
### context/F13 (part) · Low · Buyer and seller repeat the accounting parties
- XPath: `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Invoice/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- The part's finding: the buyer is the accounting customer and the seller the accounting supplier; the separate parties repeat them with name and identifier only (no fillers). Condition: present only when they differ. Options: remove them, or keep if the world's invoice rule asks for all four roles. Needs decision: no. (The originator-reference part of context/F13 is in F19.)
- Refuted because: UBL defines `BuyerCustomerParty` and `SellerSupplierParty` as "The buyer" and "The seller", without an "if different" condition (parties checked the same and refuted it); the accounting roles and the trade roles are distinct roles, and the repository's rule "nothing implied by absence" (IND6) means that leaving them out would leave the reader to infer that buyer and accounting customer coincide. Stating them, as here, is the explicit form, and they tie the invoice to the parties of the order.

## Changed in the merge
- broad/F1 split: "not ordered" → F1 (High, with money/F1, logistics/F1, context/F4); "not yet performed" → F2 (High, with context/F10, which said Low: the tax point is contradicted by 29 and 34); "by the manufacturer's installers" → F8.
- money/F10 (Low) → F3: High with broad/F2, logistics/F2, context/F1 (two values of the same invoice contradict each other).
- broad/F4 + money/F2 → F4: combined.
- broad/F5 + money/F3 + context/F2 + money/F6 → F5: combined, since the interest condition is the same (terms from the contract); money/F6's legal-basis argument and options kept.
- money/F4 (Medium) + broad/F3 (High) + context/F3 (High, yes) → F6: High (contradiction between two values of the document), Needs decision no: the tendered prices are in lume, so dropping the pricing currency is encoding.
- broad/F6 (Medium) + logistics/F3 (High) → F7: High, as analysis/review-merge-decisions.md.
- parties/F3 (Medium) + context/F5 (High) + money/F12 (Low) → F8: Medium; the reason is in Why.
- money/F5 + context/F6 → F9: combined.
- context/F7 (Medium, yes) → F10: Needs decision no, as analysis.
- parties/F8 + context/F14 (Low) + broad/F11 (department part) → F13: Medium, as analysis ("public bodies as companies").
- broad/F9 + money/F7 + context/F11 → F14: combined; all three options kept.
- broad/F8 + money/F8 + parties/F9 + context/F12 → F15: combined.
- broad/F10 + logistics/F4–F6 + context/F13 (originator part) → F18 (despatch, delivery) and F19 (references, programme code).
- context/F16 (Low, yes) + broad/F11 (catalogue part) → F24: Needs decision no, as analysis.
- context/F13 (buyer/seller part) → "Refuted in the merge".
- parties/F7 → F23: preferred option changed to keeping the code and rewording the text, because the code's list definition names a buyer that is a public body; aligned with the other tender merges.

## Outside this review
- Timeline: the invoice is issued at 09:28 on 31 March, the morning after the despatch and before the import clearance and the installation; whether a release can be invoiced before it is installed and accepted belongs to the consistency review across 29, 31, 32 and 34 (money, broad). Its contradiction with this invoice's own tax point is F2.
