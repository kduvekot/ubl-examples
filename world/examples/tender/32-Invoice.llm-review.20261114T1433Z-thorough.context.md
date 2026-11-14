# LLM review: 32-Invoice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/32#F1 · High · The benches are described as grey although the release was changed to moss green
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The buyer changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), and the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`). This document concerns those same 40 benches, yet it identifies them as the grey variant: extended identifier `GRY` (the variant suffix of the seller's item number), colour attribute of the frame `GRY` "Frame in Ferro grey", and the property "Frame colour" = "Ferro grey". The invoice bills the charge for the special colour (`/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Special colour`) and at the same time describes the invoiced benches as the standard grey ones.
- Condition: Every document about the benches of this release states the colour that was ordered after the change (moss green, RAL 6005) in the extended identifier, the colour attribute and the colour property, or states none.
- Options: (a) preferred: a variant for moss green (extended identifier, colour code and text; the colour list needs a code for it) in all documents from the despatch on; (b) remove the colour data where the document does not need it.
- Needs decision: no
### tender/32#F2 · High · The seller's standard payment terms instead of the contract's
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentTermsDetailsURI` = `https://www.valdara.example/terms`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-30`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- Why: The invoice is issued under the framework contract it references (`/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`), whose payment terms are `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` The invoice applies Valdara's own standard terms (identifier `XU-STD`, details on Valdara's website): due 30 days after the invoice date, a 2 % discount within ten days and 8 % penalty interest, none of which the contract contains. The due date 2026-04-30 is counted from the invoice date (2026-03-31), the day after despatch, when the release was neither delivered nor accepted; under the contract no due date can be fixed before acceptance. A supplier cannot replace the payment terms of a public contract by its general terms on the invoice.
- Condition: The payment terms and due date of the invoice are those of the contract (30 days after acceptance of the release); a discount or penalty interest appears only if the contract provides for it.
- Options: (a) preferred: terms "30 days after acceptance of the release" with a due date derived from the acceptance (which then needs a date in the flow); (b) add discount and interest to the contract's terms and count from acceptance.
- Needs decision: yes (the reminder and the remittance advice build on the due date and the interest)

### tender/32#F3 · High · Pricing currency ferra, but the prices are in lume
- XPath: `/Invoice/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `18`
- Why: `PricingCurrencyCode` is the currency of the prices of the invoice. Both prices carry `currencyID="XBL"` and are the lume prices of the contract (499 and 18); in ferra they would be 49900 and 1800, as in the catalogue. The declared pricing currency and the currency of every price contradict each other.
- Condition: Every `PriceAmount` is in the currency `PricingCurrencyCode` names, or no pricing currency different from the document currency is declared.
- Options: (a) preferred: drop `PricingCurrencyCode` and the pricing exchange rates (F6, F9); (b) give the prices in ferra.
- Needs decision: yes (which currency the contract price is fixed in; same decision as for `26-Order.xml`)

### tender/32#F4 · High · An installation is billed against an order that does not contain one
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Name[2]` = `Installation of a park bench`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: The invoice is associated with order `LPWD-PO-26-0212`. That order has one line, the benches (`26-Order.xml:/Order/cbc:LineCountNumeric` = `1`), and neither the order change nor the order response adds an installation. Line 1 of the invoice refers to order line 1; line 2 has no order line reference, and nothing in the flow orders the 40 installations it bills.
- Condition: Every invoice line corresponds to something ordered under the referenced order (with an order line reference), or to another order the invoice names.
- Options: (a) preferred: add the installation as a second line to the order (and its change and response); (b) bill the installation in a separate invoice once it is ordered and done.
- Needs decision: yes (adds a line or a document to the flow)

### tender/32#F5 · High · "By the manufacturer's installers" although the installation is subcontracted
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The award and the contract say the installation is done by a subcontractor (`24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`). The invoice for that installation says the manufacturer's own installers did it. The text comes from the catalogue (`25-Catalogue.xml`), where the same contradiction is raised.
- Condition: The description of the installation service does not name installers other than those of the contract, in both language versions.
- Options: (a) preferred: "by the supplier's subcontractor" or no statement of who installs; (b) none seen.
- Needs decision: no

### tender/32#F6 · Medium · Line-level pricing exchange rates that do not differ from the document's
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- Why: A price's `PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". Both line rates equal the document's rate in currencies, rate and date, so the condition of the definition is not met; and the prices they sit on are in lume (F3), so no rate applies to them.
- Condition: A price carries its own pricing exchange rate only when that rate differs from the document's.
- Options: (a) preferred: remove the line-level rates; (b) none seen.
- Needs decision: no

### tender/32#F7 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in the sibling lifecycle stage description. (Semantic conformance asks for the UBL definition even where another use seems handy.) The same value comes with every copy of the item in the flow, from `25-Catalogue.xml` on.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element and keep the boundary in the lifecycle stage description; (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision)
### tender/32#F8 · Medium · A province in `Region`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/32#F9 · Medium · A language code as locale
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/32#F10 · Low · The installation is invoiced before the benches have arrived
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-31`
- XPath: `/Invoice/cbc:IssueTime` = `09:28:00`
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-03-31`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`
- Why: An invoice requests payment for what was supplied. Line 2 bills the anchoring of 40 benches in the ground at Lumeport on the morning of 2026-03-31. The benches were despatched from Urvania at 17:37 the evening before (`29-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `17:37:00`), their import was declared only at 11:14 that day (`31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `11:14:00`), and four of the anchor sets were still on back order, to "follow within a week, before the installers need them" (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderReason`). No bench can have been installed when the invoice was written; the invoice has no delivery or invoice period that would say otherwise.
- Condition: The installation is invoiced after it has been carried out (and, under the contract, accepted), or the invoice states that it is billed in advance and the contract allows that.
- Options: (a) preferred: bill the installation later, in its own invoice or after the installation dates; (b) keep one invoice and issue it after installation and acceptance.
- Needs decision: yes (changes the timeline of the flow)

### tender/32#F11 · Low · The buyer's forward contract and a pricing rate of January in the seller's invoice
- XPath: `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:ExchangeMarketID` = `XLMX`
- XPath: `/Invoice/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- Why: The pricing exchange rate (ferra to lume) rests on a foreign exchange contract that is, in the order, the buyer's "Forward purchase of ferra" of 2026-01-02 (`26-Order.xml:/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`). In the seller's invoice it has no place: the seller is not party to the buyer's hedge, and it dates from before the procedure was even announced. The invoice does need the tax rate (the Urvanian tax total is in ferra) and the payment rate (payment currency ferra); a pricing rate has nothing to convert, since prices and totals are in the document currency.
- Condition: The invoice carries the exchange rates it uses (tax, payment) and no foreign exchange contract of the buyer.
- Options: (a) preferred: remove the pricing exchange rate with its contract; (b) none seen.
- Needs decision: yes (follows the currency decision, F3)

### tender/32#F12 · Low · A tax representative in an invoice on which no tax of the representative's country is charged
- XPath: `/Invoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Invoice/cbc:Note[2]` = `Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra.`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Invoice", a party that accounts for tax on the supplier's behalf where the supplier is not established. The taxes on this invoice are Urvanian value added tax, not charged (export; service abroad), and a Bayvarran withholding tax that the buyer withholds and pays itself. No Bayvarran sales tax is charged, the buyer being exempt, and the buyer is its own importer under DAP. There is nothing for a representative in Bayvarra to account for on this invoice; the party and the note explain a role the document does not use. (Bayforth Forwarding is also named as freight forwarder in the order change and does no forwarding in the flow.)
- Condition: A tax representative is named only where the invoice charges, or reports, a tax that the representative accounts for; otherwise party and note are absent.
- Options: (a) preferred: remove the representative and the note; (b) keep them if the state sales tax law of the world requires a representative for every non-resident supplier even on exempt sales, and say so.
- Needs decision: yes (a tax rule of the world)

### tender/32#F13 · Low · Buyer, seller and originator document repeat what is already there
- XPath: `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Invoice/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/Invoice/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: The buyer is the accounting customer and the seller the accounting supplier; the separate buyer and seller parties repeat them with name and identifier only and tell the reader nothing. The originator document reference ("A reference to an originator document associated with this document") carries the contract's identifier, which `ContractDocumentReference` already gives. Under the rule "no fillers" each needs a reason of its own.
- Condition: `BuyerCustomerParty` and `SellerSupplierParty` are present only when they differ from the accounting parties; the originator document reference points to a document other than the contract, or is absent.
- Options: (a) preferred: remove the three; (b) keep buyer and seller if the world's invoice rule asks for all four roles.
- Needs decision: no

### tender/32#F14 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/32#F15 · Low · Master data of a party that the document does not use
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). An invoice identifies the supplier for accounting and tax; its share capital, stock-exchange listing and warehouse provider are not used by a request for payment. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
### tender/32#F16 · Low · The whole catalogue description of the item repeated in a document that does not use it
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:Dimension[4]`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile`
- Why: The item is identified by the seller's and the standard item identification. Beyond that the line repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the test method of the load capacity, the range of the seat height, the greenhouse-gas emission of manufacturing with its calculation method and measurement period, and the circularity profile (maintenance frequency, resource consumption, packaging waste, repairability score, repair manual). An invoice line needs the item's identification, description, quantity, price and tax category; emissions, test methods, seat-height range and repairability score are not billed. It reads as item master data copied into the document; the remarks made on these values in the catalogue's review (lifecycle stage code against its description, no recycled steel shown, two keywords in one element) come along with every copy.
- Condition: The item of this document carries the identification and those properties the document's purpose uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) preferred: reduce the item to identification, name, description and the properties this document needs; (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision.
- Needs decision: yes (a design decision for all documents that carry the item)
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example (creditor reference `RF48VIINV260221`, account number).
- Arithmetic: 40 × 499 = 19960.00; 40 × 18 = 720.00; lines 20680.00; + charge 200.00 = 20880.00 (tax exclusive = tax inclusive, tax 0); withholding 10 % of 720.00 = 72.00; payable 20880.00 − 72.00 = 20808.00; taxable 19960.00 + 200.00 = 20160.00 and 720.00; ferra tax total 2088000 = 20880.00 × 100; settlement discount 2 % of 20880.00 = 417.60, settlement period ten days from the invoice date.
- The charge "Special colour" 200.00 with reason code `CAT` is the one of the order change and the order response.
- `OrderReference` `LPWD-PO-26-0212` is the order; line 1 refers to its line 1; contract `PWD-2026-PARKS`; project `PWD-PARKS-26` as in the order.
- `LineCountNumeric` 2 with two lines; type 380 commercial invoice; payment currency ferra with a ferra account of the payee and a payment exchange rate; payment means reference in the instruction note equals `PaymentID`.
- Supply type codes: goods on the bench, services on the installation, matching their tax categories.
- The annotation "First release: 40 benches; 200 remain." agrees with the framework's 240 benches.
- Notes and item texts are given in Urvanian and English, tagged `qau` and `en-XU`; default language `en`.

## Considered and refuted
- `/Invoice/cac:Annotation/cbc:AnnotationContent`: "200 remain" although the remaining benches are not ordered — refuted because an annotation is informative text about the framework and, unlike an outstanding quantity, claims nothing about this order.
- `/Invoice/cac:WithholdingTaxTotal`: a withholding on the installation billed by a non-resident — refuted for this lens: it fits the scheme's name ("Withholding tax on services of non-residents"); whether the rate and the base are right is the money part's.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: a clearing channel code — refuted for this lens; the list is one the repository decided on for this element (`CLAUDE.md` mentions the decision on the payment channel).
- `/Invoice/cac:BuyerAssignedReference`: an accounts-payable routing reference — refuted, that is what the element is for.
- `/Invoice/cbc:TaxPointDate`: equal to the issue date — refuted, legitimate.

## Outside this review
- The invoice has no reference to the despatch advice `CL-DA-26-0215` although the credit note refers to it; references are the logistics part's lens.
- The tax categories (export of goods, service to a business abroad for a public body) and the tax currency: money part.
- The emission factor arithmetic of the item: logistics part.
