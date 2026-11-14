# LLM review: 33-CreditNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/33-CreditNote.xml`, Git blob `fedb04ee2964c2e08e60565d54f4c570247bdfda` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 0199c78 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/33#F1 · High · The benches are described as grey although the release was changed to moss green
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The buyer changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), and the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`). This document concerns those same 40 benches, yet it identifies them as the grey variant: extended identifier `GRY` (the variant suffix of the seller's item number), colour attribute of the frame `GRY` "Frame in Ferro grey", and the property "Frame colour" = "Ferro grey". The credited bench is one of those 40.
- Condition: Every document about the benches of this release states the colour that was ordered after the change (moss green, RAL 6005) in the extended identifier, the colour attribute and the colour property, or states none.
- Options: (a) preferred: a variant for moss green (extended identifier, colour code and text; the colour list needs a code for it) in all documents from the despatch on; (b) remove the colour data where the document does not need it.
- Needs decision: no
### tender/33#F2 · High · Two different statements of how the credit is settled, and the flow follows neither literally
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PaymentTerms/cbc:Note` = `Set off against the next release's invoice.`
- Why: The document says the credit is settled against the next payment to the seller; line 1 says it is set off against the invoice of the next release. On 2026-04-04 the next payment to the seller is the payment of the still unpaid invoice `VI-INV-26-0221` of this release, not of a next release; and that is what happens: the reminder and the remittance advice both list the credit note next to that invoice (`36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:BillingReference/cac:CreditNoteDocumentReference/cbc:ID` = `VI-CN-26-0222`). The line's statement contradicts the document's and the settlement that follows; line 2 has no terms, so half of the credit would follow one rule and half the other.
- Condition: The credit note states one way of settlement, the same for the whole document, and it is the one the reminder and the remittance advice apply (set-off against invoice `VI-INV-26-0221`).
- Options: (a) preferred: keep the document-level terms, worded as set-off against the open invoice, and drop the line-level terms; (b) none seen.
- Needs decision: no

### tender/33#F3 · High · Pricing currency ferra, but the prices are in lume
- XPath: `/CreditNote/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Price/cbc:PriceAmount` = `18`
- Why: The pricing currency is the currency of the prices of the document. Both prices carry `currencyID="XBL"`; the ferra price of the bench appears separately as an alternative condition price (`/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount` = `49900`). Declared pricing currency and the currency of the prices contradict each other, as in the invoice.
- Condition: Every `PriceAmount` under `Price` is in the currency `PricingCurrencyCode` names, or no pricing currency different from the document currency is declared.
- Options: (a) preferred: drop `PricingCurrencyCode` and the pricing exchange rate with its foreign exchange contract (`BL-FX-26-0091`, the buyer's forward purchase of 2026-01-02, which the seller has no reason to cite); (b) give the prices in ferra.
- Needs decision: yes (same currency decision as for `26-Order.xml` and `32-Invoice.xml`)

### tender/33#F4 · High · "By the manufacturer's installers" although the installation is subcontracted
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The contract says `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.` The credited installation is described as done by the manufacturer's own installers. The text comes from the catalogue, where the same contradiction is raised.
- Condition: The description of the installation service does not name installers other than those of the contract.
- Options: (a) preferred: "by the supplier's subcontractor" or no statement of who installs; (b) none seen.
- Needs decision: no

### tender/33#F5 · Medium · Invoice periods on a credit for one damaged bench of one invoice
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-03-31`
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:EndDate` = `2026-04-04`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:InvoicePeriod/cbc:StartDate` = `2026-04-02`
- Why: At document level `InvoicePeriod` "Associates the Credit Note with Invoicing Periods rather than with a specific Invoice". This credit note is associated with a specific invoice (`/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221`), so the condition of the definition is not met; the period given runs from the invoice's date to the credit note's date, which is not an invoicing period of anything (the sale is not billed by period). On line 1, "An invoice period to which this credit note line applies" holds a single start date, 2026-04-02, with no end: the credited object is a bench, not a period; the date seems to be the day the damage was found or the bench delivered.
- Condition: `InvoicePeriod` is absent from a credit note that corrects one invoice of goods; a date of delivery or of the damage is stated where it is said what it is (the damage report reference, a note).
- Options: (a) preferred: remove both periods and state the date of the damage in a note or in the reference to the damage report (its issue date); (b) none seen.
- Needs decision: no

### tender/33#F6 · Medium · The credited installation "collected for" the tax representative
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `CollectedForParty` is "The Party on whose behalf this item or amount is collected": a third party for whom the supplier bills an amount it will pass on. Line 2 credits the installation of the damaged bench (18.00). The installation is performed by the subcontractor Saltmere Engineering and billed by Valdara in its own name; Bayforth Forwarding is, in this same document, the tax representative, and neither installs nor is owed the installation price. The invoice's installation line names no such party (`32-Invoice.xml` has no `CollectedForParty`). The element states that the 18.00 was collected on Bayforth's behalf, which nothing in the flow supports.
- Condition: `CollectedForParty` is absent from the installation line, or names a party for whom the invoiced amount was in fact collected, consistently in invoice and credit note.
- Options: (a) preferred: remove it; (b) if the withheld tax is what is meant, it is not "collected for" a forwarder either; none seen that keeps the element.
- Needs decision: yes (who Bayforth Forwarding is in this flow: forwarder, tax representative, collecting agent)

### tender/33#F7 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in the sibling lifecycle stage description. (Semantic conformance asks for the UBL definition even where another use seems handy.) The same value comes with every copy of the item in the flow, from `25-Catalogue.xml` on.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element and keep the boundary in the lifecycle stage description; (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision)
### tender/33#F8 · Medium · A province in `Region`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/33#F9 · Medium · A language code as locale
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/33#F10 · Low · The credit note does not say why it credits
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:DocumentReference/cbc:ID` = `PWD-DMG-26-0081`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cac:Item/cbc:Name` = `Side frames of the bench`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cbc:LineExtensionAmount` = `180.00`
- Why: A credit note is "A document used to specify credits due to the Debtor from the Creditor". It credits one bench and one installation in full, but has no note and no discrepancy response; that a bench was damaged can only be guessed from the letters "DMG" in an untyped document reference. The one sub-line names the side frames with 180.00, without saying how that relates to the 499.00 credited on the line (the damaged part and its value? a part to be replaced?); a single detail line that covers 180.00 of 499.00 explains nothing.
- Condition: The credit note states the reason for the credit in text (and/or a typed reference to the damage report), and a sub-line either accounts for the line amount together with its siblings or says what it is.
- Options: (a) preferred: a note or `DiscrepancyResponse` "Bench 17 of Harbour park damaged in transport; bench and its installation credited", a document type on the reference, and either sub-lines that sum to 499.00 or none; (b) at least the note.
- Needs decision: no

### tender/33#F11 · Low · Fillers on line 1: "not free of charge", originator and beneficiary
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cbc:FreeOfChargeIndicator` = `false`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `FreeOfChargeIndicator` is "An indicator that this credit note line is free of charge (true) or not (false). The default is false": stating the default says nothing (rule: nothing implied by absence). `OriginatorParty` ("The Party who originates the Order to which the Credit Note is related") and `BeneficiaryParty` both repeat the accounting customer, who ordered and who uses the benches; they would matter only if another unit had originated the order or benefited.
- Condition: The indicator is absent unless true; originator and beneficiary of a line are present only when they differ from the customer.
- Options: (a) preferred: remove the three; (b) name the parks service as beneficiary if the world has it as a separate body.
- Needs decision: no

### tender/33#F12 · Low · A tax representative in a credit note on which no tax of the representative's country is reversed
- XPath: `/CreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: As in the invoice: the taxes of the document are Urvanian value added tax (not charged) and a Bayvarran withholding tax the buyer handles itself; there is nothing for a tax representative in Bayvarra to account for.
- Condition: A tax representative is named only where the document charges or reverses a tax the representative accounts for.
- Options: (a) preferred: remove it; (b) keep it under a recorded rule of the world's sales tax law.
- Needs decision: yes (same decision as for `32-Invoice.xml`)

### tender/33#F13 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/33#F14 · Low · Master data of a party that the document does not use
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). A credit note identifies the supplier for accounting and tax; its share capital, stock-exchange listing and warehouse provider are not used. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
### tender/33#F15 · Low · The whole catalogue description of the item repeated in a document that does not use it
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:Dimension[4]`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:CircularityProfile`
- Why: The item is identified by the seller's and the standard item identification. Beyond that the line repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the test method of the load capacity, the range of the seat height, the greenhouse-gas emission of manufacturing with its calculation method and measurement period, and the circularity profile (maintenance frequency, resource consumption, packaging waste, repairability score, repair manual). A credit note line needs to say which invoiced item is credited, in what quantity and at what price; the full catalogue description of the bench, with emissions and repairability, is not credited. It reads as item master data copied into the document; the remarks made on these values in the catalogue's review (lifecycle stage code against its description, no recycled steel shown, two keywords in one element) come along with every copy.
- Condition: The item of this document carries the identification and those properties the document's purpose uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) preferred: reduce the item to identification, name, description and the properties this document needs; (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision.
- Needs decision: yes (a design decision for all documents that carry the item)
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- `BillingReference` `VI-INV-26-0221` is the invoice; `DeliveryNoteDocumentReference` `CL-DA-26-0215` the despatch advice, whose note asked to report damage on arrival.
- Arithmetic: 1 × 499 = 499.00; 1 × 18 = 18.00; total 517.00; withholding 10 % of 18.00 = 1.80; payable 517.00 − 1.80 = 515.20; taxable amounts 499.00 and 18.00; the unit prices are the invoice's.
- The alternative condition price 49900 ferra is the catalogue's price of the bench, the same price in other terms (499 lume at 100).
- Purchase references: `PARK-HB` at document level and `PARK-HB-B17` on line 1 read as the park and the bench position the credit relates to, an "object … to which this Credit Note relates" in the sense of the definition.
- Type 381 credit note; `LineCountNumeric` 2 with two lines; accounting cost as in the order; the credit note is issued by the seller, who bears the transport risk under DAP.

## Considered and refuted
- `/CreditNote/cac:WorkReportDocumentReference/cbc:ID`: a work report for a credit on goods — refuted because the installation is a work, and the installers' report of the bench they could not install is a plausible basis for crediting it (line 1 refers to its line 1).
- `/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice`: the same price twice — refuted, the definition is "The price expressed in terms other than the actual price", here in the catalogue's currency.
- `/CreditNote/cac:CreditNoteLine[2]/cbc:CreditedQuantity`: the installation of the damaged bench credited although installations were invoiced before they took place — refuted here: crediting an installation that will not be done is consistent; the early invoicing is raised in the invoice's review.
- `/CreditNote/cac:CreditNoteLine[1]/cbc:TaxPointDate`: repeats the document's — refuted, legitimate at line level.

## Outside this review
- Whether a damaged bench is credited or replaced, and what happens to bench 17 afterwards, is a story question across later releases.
- Tax categories and the withholding reversal: money part. Emission factor arithmetic of the item: logistics part.
