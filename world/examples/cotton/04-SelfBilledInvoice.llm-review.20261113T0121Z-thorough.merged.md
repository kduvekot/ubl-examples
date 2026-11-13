# LLM review: 04-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/04-SelfBilledInvoice.xml`, Git blob `7ff28661ff5e42f702b07e4477e9454c7a6c7ebb` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### cotton/04#F1 · High · Pricing currency Lume, but every price is in coral
- XPath: `/SelfBilledInvoice/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.226`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.226`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for prices in the Invoice", and `PricingExchangeRate` "The exchange rate between the document currency and the pricing currency". The only price, 0.226 per kg, is stated with `currencyID` `XLC`, as is the per-unit haulage amount (0.010 XLC); no price is in Lume, and the Lume price the rate would imply (0.226 / 0.4 = 0.565 XBL/kg, recomputed) appears nowhere. The advance invoice 01, at the same price between the same parties, carries no pricing currency. The header contradicts the prices it describes. The same pair occurs in 05.
- Condition: either every price of the invoice is in the currency `PricingCurrencyCode` names, with the pricing exchange rate converting it to the document currency, or the invoice carries no pricing currency and no pricing exchange rate.
- Options: (a, preferred) drop `PricingCurrencyCode` and `PricingExchangeRate`: the farm's price is a coral price in 01, 04 and 05, so nothing in the story changes; (b) if the season agreement really fixes the price in Lume, state the line price in XBL and keep the rate, which changes how 01 and 05 state the price too (a story change, which would need a decision).
- Needs decision: no (for the preferred option; money said yes, context yes only for option b)
- From: broad (F2), money (F2), context (F1)

### cotton/04#F2 · High · The taxable amount leaves out the haulage charge of the same tax category
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:Amount` = `180.000`
- XPath: `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `4248.000`
- Why: `TaxableAmount` is "The net amount to which the tax percent (rate) is applied". The only tax subtotal is for category `O`, and both the seed-cotton line (4 068.000) and the document-level haulage charge (180.000) are in category `O` under the same scheme name. Recomputed: 4 068.000 + 180.000 = 4 248.000 = `TaxExclusiveAmount`, but the subtotal's taxable amount is 4 068.000, so the subtotals do not add up to the tax-exclusive amount and the charge is in a category whose subtotal does not contain it. The rate is 0, so no tax amount changes, but the arithmetic does not hold. Refutation tried: there is no second subtotal the charge could belong to.
- Condition: the sum of the taxable amounts of the tax subtotals equals `TaxExclusiveAmount` (4 248.000), each line and document-level charge counted in the subtotal of its own category.
- Options: (a, preferred) taxable amount 4 248.000 in the `O` subtotal; (b) if the haulage charge belongs to another category (or is not a supply), a second subtotal for it, or take it out of the tax-exclusive amount and say how it is settled (story change).
- Needs decision: no
- From: broad (F1), money (F1)

### cotton/04#F3 · Medium · The delivery note given as a despatch advice
- XPath: `/SelfBilledInvoice/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledInvoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cbc:ID` = `LCF-DN-26-0193`
- Why: `DespatchDocumentReference` is "A reference to a Despatch Advice associated with this document". `LCF-DN-26-0193` is the farm's Delivery Note (03), which the invoice already cites, correctly, with `DeliveryNoteDocumentReference` and in the line's `DeliveryNoteLineReference`. UBL 2.5 has distinct document types and references for the two; no despatch advice exists in the flow, so the element is used for a document of another kind and suggests a document that does not exist.
- Condition: `DespatchDocumentReference`, if present, refers to a despatch advice; the delivery note is cited only as a delivery note.
- Options: (a, preferred) drop `DespatchDocumentReference`; (b) add a despatch advice to the flow if the farm really sends one (story change).
- Needs decision: no
- From: broad (F3), logistics (F1), context (F4)

### cotton/04#F4 · Medium · The mill as originator and beneficiary of the ginnery's seed-cotton call-off, with a mill document as originator document
- XPath: `/SelfBilledInvoice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- XPath: `/SelfBilledInvoice/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- XPath: `08-Order.xml:/Order/cbc:ID` = `LTM-PO-26-0198`
- Why: in an invoice `OriginatorCustomerParty` is "The Party who originated the Order to which this Invoice is related"; `BeneficiaryParty` is "A Party for whom the associated transaction is ultimately intended or who derives benefit from it". The order is the ginnery's own call-off `SCG-SEASON-2026/03` under its season agreement with the farm; the mill buys lint from the ginnery under a separate order (08, issued 2026-02-24), and the ginnery gins the seed cotton and sells lint and seed for its own account. `LTM-SEASON-2026` exists in no example and says nothing about what it is; 01 names no originator or beneficiary. Unlike the delivery note (03#F10, Low), the invoice's definition ties the originator to the order, which the ginnery placed, so the element carries a meaning other than its definition (Medium, as broad and context; parties had Low). A reading in which the mill's season agreement drives the ginnery's purchases is possible, but the documents do not show it, hence the decision.
- Condition: originator, beneficiary and originator document are present only if the flow's documents show the mill originating this order or the seed cotton being bought for it, and then consistently in 01, 03, 04 and 05, with the originator document saying what it is.
- Options: (a, preferred) drop the three; (b) if the mill finances or pre-buys the farm's crop under `LTM-SEASON-2026`, state that in the story and the season agreement, give the reference a type, and name the roles the same way in 01, 03, 04 and 05.
- Needs decision: yes
- From: broad (F4), parties (F2), context (F3)

### cotton/04#F5 · Medium · A customs broker as tax representative of a domestic farm purchase
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID` = `IC41585`
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Self Billed Invoice". A tax (fiscal) representative acts for a party not established in the taxing country (own knowledge of tax practice). Farm and ginnery are both Lisavan, in the island companies register, neither carries a `PartyTaxScheme`, the supply is outside a general sales tax, and the presumptive tax is withheld by the ginnery itself; there is nothing a representative would account for. Tevaro Customs Brokers appears nowhere else in the flow; in the only other example that names it, it is an importer's customs agent. 01 has no tax representative. The same party is in 05.
- Condition: the self-billed invoice names a tax representative only if one of its parties needs one for a tax this invoice declares, the reason is visible in the document, and the party's role in the world is tax representation.
- Options: (a, preferred) drop `TaxRepresentativeParty`; (b) if Lisavan law requires farms to appoint an agent for the presumptive tax, record that rule in the world's tax story and name a fitting agent.
- Needs decision: yes
- From: broad (F5), money (F5, Low), parties (F1), context (F2)

### cotton/04#F6 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: in UN/EDIFACT 5305 `O` is "Services outside scope of tax"; the line is seed cotton, a supply of goods, as `SupplyTypeCode` says. EN 16931 uses `O` for any out-of-scope supply; under semantic conformance that is context, not a lower severity. For the haulage charge, a service, `O` fits (broad). Counted (merge, lxml): 17 files use 5305 `O`, 5 with `O` and `GOODS` in one category (cotton 01, 04, 05, 16, sea/29). Same as 01#F2.
- Condition: the goods line and the subtotal that covers it carry a code whose meaning covers goods outside the scope of tax, or the deviation is recorded as a deliberate choice.
- Options: (a, preferred) one world-wide decision on how goods outside any sales tax are coded; (b) keep `O` and record it as a deliberate EN 16931-style deviation.
- Needs decision: yes
- From: broad (F6)

### cotton/04#F7 · Low · Tax and payment currency repeat the document currency, with identity exchange rates
- XPath: `/SelfBilledInvoice/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledInvoice/cac:TaxExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledInvoice/cac:PaymentExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- Why: `TaxExchangeRate` is "The exchange rate between the document currency and the tax currency", `PaymentExchangeRate` the same for the payment currency; both convert coral into coral at 1, and the two currency codes repeat the document currency. Nothing is converted (IND5). 01 between the same parties has none of them. The same occurs in 05.
- Condition: a tax or payment currency and its exchange rate are present only where they differ from the document currency.
- Options: (a, preferred) drop the four elements.
- Needs decision: no
- From: broad (F7), money (F6), context (F8)

### cotton/04#F8 · Low · Alternative payment currency Lume without a reason or an amount
- XPath: `/SelfBilledInvoice/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: the farm is paid by RTGS in coral into a coral account, and 06 pays it in coral; nothing offers payment in Lume, and `LegalMonetaryTotal` has no `PayableAlternativeAmount`. A Lisavan micro farm offered settlement in Bayvarra's currency has no reason in the document (IND5). (1 XLC = 2.5 XBL is the inverse of the pricing rate 0.4, recomputed, so the rates agree with each other.) The same occurs in 05.
- Condition: an alternative payment currency is present only if the payee can actually be paid in it under this invoice, and then the amount in that currency follows from the rate.
- Options: (a, preferred) drop both elements; (b) keep them with a reason in the payment terms and a payable alternative amount (a story addition).
- Needs decision: no (money said yes; dropping changes nothing in the story, and broad and context said no)
- From: broad (F7), money (F7), context (F8)

### cotton/04#F9 · Low · Invoice period starts two days before the only delivery
- XPath: `/SelfBilledInvoice/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`
- XPath: `/SelfBilledInvoice/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- Why: the invoice bills one delivery note with one actual delivery date, 2026-02-05, which its own `Delivery` repeats. A period from 2026-02-03 implies deliveries over three days (three trailer loads, per 03's note), which neither document records. Context refuted it: the loads may have been harvested and hauled over those days, and the period is what the invoice covers. That reading needs 03 to record the loads on those days, which it does not, so the finding stays Low. The same period is in 05.
- Condition: the invoice period and the delivery date(s) of the invoice and of 03 describe the same deliveries.
- Options: (a, preferred) start the period on 2026-02-05; (b) if the loads came on 2026-02-03 to 05, give 03 a delivery period (or one delivery per load) and the invoice matching dates.
- Needs decision: no
- From: logistics (F2); context (considered and refuted, argument carried)

### cotton/04#F10 · Low · Ginning outturn report cited on the day ginning began, for a price that does not depend on it
- XPath: `/SelfBilledInvoice/cac:WorkReportDocumentReference/cbc:ID` = `SCG-OUT-26-0311`
- XPath: `/SelfBilledInvoice/cbc:IssueDate` = `2026-02-07`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:StartDate` = `2026-02-07`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:EndDate` = `2026-02-22`
- XPath: `05-SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:WorkReportDocumentReference/cbc:ID` = `SCC-CLS-26-0311`
- Why: `WorkReportDocumentReference` is "A reference to a Work Report associated with this document". The ID reads as the gin's outturn report (`OUT`), the report of what ginning yielded. Ginning ran from 2026-02-07 to 2026-02-22 (10), so on the invoice's issue day (15:50) it had just begun. The invoice is priced per kilogram of seed cotton delivered (18 000 × 0.226), not on outturn, so it does not rest on such a report; the credit note 05 cites a different work report for the same delivery. The reference has only an ID. The reading of `OUT` as outturn is an inference from the ID, which keeps this Low.
- Condition: every work report the invoice cites exists at its issue time, is something the invoice is based on, and says what kind of report it is.
- Options: (a, preferred) drop the reference (the weighbridge ticket is already cited); (b) if the price depends on outturn, issue the invoice after it (story change).
- Needs decision: no
- From: logistics (F3), context (F5, work-report part), broad (F11, work-report part)

### cotton/04#F11 · Low · Weighbridge ticket cited as a receipt advice
- XPath: `/SelfBilledInvoice/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: `ReceiptDocumentReference` is "A reference to a Receipt Advice associated with this document". The ID is the gin's weighbridge ticket (03: "weighed at the gin"; prefix `WB`), which 03 cites as an additional document. No receipt advice is in the flow, and nothing says the ticket is the gin's receipt advice; a reader of 03 and 04 sees one document as two kinds (see 03#F4).
- Condition: the document is cited as the same kind in 03, 04 and 05, and that kind matches the reference element used.
- Options: (a, preferred) cite it as an `AdditionalDocumentReference` with a document type "Weighbridge ticket" in 03, 04 and 05; (b) if the ticket is meant as the gin's receipt advice, say so with a document type and keep `ReceiptDocumentReference`.
- Needs decision: no
- From: logistics (F4), context (F5, receipt part), broad (F11, receipt part)

### cotton/04#F12 · Low · Statement and farm-registration references that say nothing about themselves
- XPath: `/SelfBilledInvoice/cac:StatementDocumentReference/cbc:ID` = `SCG-ACC-LCF-26-02`
- XPath: `/SelfBilledInvoice/cac:AdditionalDocumentReference/cbc:ID` = `XL-FARM-REG-0412`
- Why: `StatementDocumentReference` ("A reference to a Statement") cites what reads as the farm's February account statement from an invoice issued on 7 February, before such a statement can be complete; the farm registration is given without `DocumentTypeCode` or description, and the invoice does nothing with it. Neither document is in the flow, so the kind must come from the reference itself (context, broad). The reading of the statement ID as a monthly statement is an inference.
- Condition: each reference points to a document that can exist at the issue date, has a role in this invoice, and states its kind where the ID does not.
- Options: (a, preferred) drop both unless the invoice needs them; (b) keep them with a type or description that justifies them (e.g. the farm registration as evidence for the presumptive tax tier, if the story says so).
- Needs decision: no
- From: context (F5, statement and registration parts), broad (F11)

### cotton/04#F13 · Low · Project reference to a chamber of commerce quality project
- XPath: `/SelfBilledInvoice/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: `ProjectReference` is "A reference to a project associated with this document". The ID is the Selanu Chamber of Commerce's; the purchase of seed cotton under a season agreement is not part of a project in any document of the flow, and nothing says what the project does with this invoice. Also in 03 (03#F3) and 05.
- Condition: the invoice carries a project reference only if the story has a project this purchase belongs to, and says what it is.
- Options: (a, preferred) leave it out; (b) give the project a role in the story.
- Needs decision: yes (whether such a project exists in the world)
- From: context (F6), broad (F11, project part)

### cotton/04#F14 · Low · Annotation repeats the note
- XPath: `/SelfBilledInvoice/cac:Annotation/cbc:AnnotationContent` = `Written by the gin on the farm's behalf under the self-billing agreement.`
- XPath: `/SelfBilledInvoice/cbc:Note[2]` = `Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.`
- Why: `Annotation` is "A structured annotation providing contextual or explanatory information"; here it repeats `Note[2]` in other words, in English only, and adds no structure or information (IND5).
- Condition: the annotation adds information the note does not carry, or it is absent.
- Options: (a, preferred) drop the annotation; (b) use it for something the note does not say (e.g. the self-billing agreement's reference and acceptance date).
- Needs decision: no
- From: broad (F14), context (F10, annotation part)

### cotton/04#F15 · Low · The ginnery's customs-trader number and the farm's fields in a domestic self-billed invoice
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- XPath: `/SelfBilledInvoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu Cotton Ginnery, weighbridge`
- Why: section 4.8. The purchase is domestic (no customs), and the delivery place is the gin's weighbridge; the farm's `PhysicalLocation` (the fields, with coordinates and the home page as `InformationURI`) and the ginnery's customs-trader number are not used by the invoice and read as copied master data (IND5). (The field is referenced separately in `PurchaseReference` `LCF-FIELD-07`, which logistics and context accepted.)
- Condition: every identifier and location of the parties is one the document has a use for.
- Options: (a, preferred) leave both out of the invoice; (b) keep one only where the story gives it a role here.
- Needs decision: no
- From: parties (F7), context (F10, physical-location part)

### cotton/04#F16 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Shared by the ginnery, the mill, Bayforth Forwarding and both ports; 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`). Reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the date on which that party was registered in the world's story, or absent.
- Options: (a, preferred) a date from the company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F6)

### cotton/04#F17 · Low · Contacts do not fit the role or the party
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- Why: the document itself routes the invoice to "Farm payments", but the accounting customer's contact is the lint sales desk; the ginnery here buys seed cotton and writes and pays the invoice. The farm is a one-person micro sole proprietorship; "Customer service officer" in "Sales" describes a sales organisation it does not have.
- Condition: the ginnery's contact in this role handles farm payments or seed-cotton purchasing (or is absent), and the farm's contact has no job title/department, or ones that fit a one-person farm.
- Options: (a, preferred) a farm-payments contact for the ginnery; no job title/department (or "Owner") for the farm; (b) drop the contacts.
- Needs decision: no
- From: broad (F13), parties (F4, F5)

### cotton/04#F18 · Low · DAP without a named place, and a haulage charge paid by the buyer
- XPath: `/SelfBilledInvoice/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/SelfBilledInvoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu Cotton Ginnery, weighbridge`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `CAB`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AccountingCost` = `Seed cotton haulage`
- XPath: `05-SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:DeliveryTerms/cbc:ID` = `DAP`
- Why: under Incoterms DAP the seller delivers at the named place and bears the cost of carriage to it, and every Incoterms rule is used with a named place (own knowledge of Incoterms 2020). `DeliveryTerms` names no place; only the separate `Delivery` names the gin's weighbridge. The ginnery nevertheless pays the farm a cartage charge of 0.010 per kg (180.000) on top of the price. A haulage payment to growers is a common arrangement, but then DAP no longer says who bears the carriage; with a delivered price the charge would not exist.
- Condition: the delivery terms name their place, and the terms and the haulage charge give the same answer to who bears the cost of carrying the seed cotton to the gin.
- Options: (a, preferred) keep the charge and use a rule under which the buyer bears the carriage (e.g. FCA at the farm), or describe the arrangement in `DeliveryTerms` without an Incoterm; (b) keep DAP with the gin as named place and drop the charge (and the 180.000 in the totals and in 06), or describe the payment as a delivery premium agreed in the season contract.
- Needs decision: yes (who bears the haulage is part of the season agreement)
- From: broad (F10), money (F4), logistics (F5), context (F7, terms part)

### cotton/04#F19 · Low · A charge whose reason text calls it an allowance
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:ChargeIndicator` = `true`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Haulage allowance`
- Why: `ChargeIndicator` true makes this a charge, which adds 180.000 to what the ginnery owes the farm, as a payment for the farm's own haulage should. The reason text calls it an allowance, which in UBL's allowance/charge terms is the opposite (a deduction). Money refuted it: "haulage allowance" is the growers' term for a payment towards haulage, and `CAB` (cartage) is a charge reason. The business meaning is indeed consistent; the text still reads against the indicator in a UBL allowance/charge, so it stays a Low remark.
- Condition: the reason text does not describe the charge as an allowance in the UBL sense, or makes clear it is a payment to the farm.
- Options: (a, preferred) reason text such as "Haulage paid to the farm" or "Haulage to the gin"; (b) keep the trade term and add that it is paid to the farm.
- Needs decision: no
- From: broad (F8), context (F7, text part); money (considered and refuted, argument carried)

### cotton/04#F20 · Low · Charge details the single per-kilogram haulage charge does not use
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:BaseAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:PerUnitAmount` = `0.010`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:PrepaidIndicator` = `false`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:SequenceNumeric` = `1`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: `BaseAmount` is "The monetary amount to which the multiplier factor is applied in calculating the amount of this allowance or charge"; there is no `MultiplierFactorNumeric`, and the charge is not a share of 4 068.000 (180 / 4 068 = 4.42 %, recomputed, no agreed rate): it is 0.010 × 18 000 kg = 180.000, as `PerUnitAmount` says. The base amount suggests a percentage calculation that did not take place (money rated this Medium). `SequenceNumeric` orders calculations "when there are multiple allowances or charges"; there is one. The charge's own `PaymentMeans` ("A means of payment for this allowance or charge") repeats the invoice's credit transfer; 06 pays the full 3 210.320 at once. `PrepaidIndicator` false repeats what the absence of a prepayment for the charge says (context). The merge keeps Low: the definition of `BaseAmount` describes its use with a factor, but an unused base contradicts no other value.
- Condition: the charge carries only elements its calculation or settlement uses; a per-kilogram charge is described by its per-unit amount.
- Options: (a, preferred) drop `BaseAmount`, `SequenceNumeric`, the charge's `PaymentMeans` and `PrepaidIndicator`; (b) if the haulage is a percentage, use `MultiplierFactorNumeric` with the base amount instead of the per-unit amount (changes the agreed rate).
- Needs decision: no
- From: broad (F9), money (F3, Medium; F9), context (F9)

### cotton/04#F21 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `TaxTotal` is "The total amount of a specific type of tax"; a tax total for "No general sales tax" totals a tax that does not exist, and the scheme has no `ID`. Same as 01#F8 and utilities/13#F8; one decision for the 9 files that use this name.
- Condition: the zero tax total names a real Lisavan scheme with an ID, or is absent, consistently with the world's rules for Lisavu.
- Options: (a, preferred) decide once for all Lisavan examples (scheme with ID, or no tax total).
- Needs decision: yes
- From: broad (F12)

### cotton/04#F22 · Low · A 0 % rate on tax category O
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: `Percent` is "The tax rate for this category, expressed as a percentage". A supply outside the scope of tax has no rate; 0 % reads as zero-rating, another category. No part raised it; added by the merge, as in 01#F9 and the utilities and road merges.
- Condition: a category stating the supply is outside the scope of tax carries no `Percent`.
- Options: (a, preferred) drop `Percent` in the three places.
- Needs decision: no
- From: merge

### cotton/04#F23 · Low · Zero total of allowances in an invoice without allowances
- XPath: `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:AllowanceTotalTaxInclusiveAmount` = `0.000`
- Why: "the total monetary amount of all allowances, inclusive of all taxes" is 0.000 because there are none, and there is no `AllowanceTotalAmount` either. A zero total of something absent carries no information (IND5).
- Condition: the monetary total carries allowance totals only when the invoice has allowances.
- Options: (a, preferred) drop the element.
- Needs decision: no
- From: money (F8)

### cotton/04#F24 · Low · Line status "NoStatus" in the delivery-note line reference
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Delivery/cac:DeliveryNoteLineReference/cbc:LineStatusCode` = `NoStatus`
- Why: `LineStatusCode` "No status" gives no status of the referenced line (IND5). Same treatment as `NoStatus` in the earlier flows' merges and in 03#F1.
- Condition: the line reference carries no `LineStatusCode`, or one that states a status the story has.
- Options: (a, preferred) leave it out.
- Needs decision: no
- From: context (F10, line-status part)

### cotton/04#F25 · Low · Address lines repeat the farm's structured address and mix languages
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the same four lines as in 01 and 03 repeat `StreetName`, `Description`, `District` and `CityName`, and lines 1 and 4 combine the Lisavan and English forms in one text without `languageID`, although `Line` "may be repeated only to provide the same content in multiple natural languages". No part raised it here; added by the merge (appended, without renumbering) so the farm's address is treated as in 01#F6 and 03#F5, where parties' counter-argument (a Lisavan print format) is recorded.
- Condition: the farm's postal address states each part once, and language-specific renderings carry `languageID`.
- Options: (a, preferred) drop the address lines; (b) keep only lines with information not in the structured parts.
- Needs decision: no
- From: merge

### cotton/04#F26 · Low · Expiry date on the farm's commercial-register entry
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: `RegistrationExpirationDate` is "The date upon which a registration expires (e.g., registration for an import/export license)"; the registration described is the farm's entry in the island companies register, which normally does not expire. Parties (in 01) read it as a seasonal farm registration (`XL-FARM-REG-0412` in 04); possible, but that is not the company registration described. No part raised it here; added by the merge (appended, without renumbering) for consistency with 01#F7 and 03#F6.
- Condition: the expiry date belongs to a registration that expires and is the one described.
- Options: (a, preferred) drop it; (b) make the world's register rules say that sole proprietorships register yearly.
- Needs decision: yes
- From: merge

## Checked and consistent
- Arithmetic (redone): 18 000 KGM × 0.226 per 1 KGM = 4 068.000 = line and `LineExtensionAmount`; charge 0.010 × 18 000 = 180.000 = `ChargeTotalAmount` = `ChargeTotalTaxInclusiveAmount`; tax-exclusive 4 248.000; tax 0.000; tax-inclusive 4 248.000.
- Withholding (redone): 1 % × 2 000.000 = 20.000; 2 % × 2 068.000 = 41.360; tiers 2 000 + 2 068 = 4 068.000, the line value ("of the delivery's value"); total 61.360 = `WithholdingTaxTotalAmount`.
- Cotton fund levy (redone): 1 % × 4 068.000 = 40.680 = `/SelfBilledInvoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `40.680`; 01 announced the levy on the delivery.
- Payable (redone): 4 248.000 − 1 017.000 − 61.360 + 40.680 = 3 210.320 = `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3210.320`; 06 remits it (`06-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `3210.320`).
- Prepayment: 1 017.000 paid 2026-01-13 and the billing reference `SCG-SBI-26-0191` with issue date 2026-01-13 match 01.
- Due date (redone): 2026-02-07 + 45 days = 2026-03-24 (21 days to 28 February + 24) = `DueDate` = `PaymentTerms/PaymentDueDate` = `PaymentMeans/PaymentDueDate`; penalty interest 6 % a year, simple.
- 1 XBL = 0.4 XLC and 1 XLC = 2.5 XBL are each other's inverse.
- `check_ids.py`: RF reference `RF77SCGSBI260194` and account `XL67BSEL0020004817534` valid; the payee account is the farm's, as in 01 and 06.
- Delivery note 03: same 18 000 kg, item, delivery date and order reference; `DeliveryNoteLineReference` line 1 of `LCF-DN-26-0193` resolves to its only line.
- The levy's beneficiary is the Selanu Chamber of Commerce (`IC42133`), as the line note says; a collection line with a beneficiary fits "an item or amount collected on behalf of a third party" (parties).
- Accounting parties, buyer, seller and signatory agree with 01, 03 and 05; self-billing context (389, ginnery as signatory, payee the farm, `BuyerAssignedReference` for internal routing) consistent (context).

## Considered and refuted
- `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `4248.000`: the definition says "the sum of payable amount and prepaid amount", 3 210.320 + 1 017.000 = 4 227.320 — refuted: the difference 61.360 − 40.680 = 20.680 (recomputed) is exactly the withholding less the collected levy, which UBL 2.5 places between the tax-inclusive and the payable amount; the older definition text does not cover them. (from broad, money)
- `/SelfBilledInvoice/cac:CollectionInvoiceLine`: a levy added to what the ginnery pays the farm / counted in no other total / misplaced in a self-billed invoice — refuted: an amount collected by the farm on behalf of a third party (the chamber), not the farm's supply, and paid to the farm for passing on; the definition fits also when the customer writes the invoice. (from broad, money, parties, context)
- `/SelfBilledInvoice/cac:WithholdingTaxTotal/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:ID` = `S`: standard-rate code for a tiered presumptive tax — refuted: the category describes the normal rate of each band within the OTH scheme, and the tiers are explicit. (from broad, money)
- `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `O`: for the haulage — refuted: haulage is a service, which `O` covers. (from broad)
- `/SelfBilledInvoice/cac:AllowanceCharge/cbc:ChargeIndicator` = `true` against "Haulage allowance": money refuted (growers' term, `CAB` is a charge reason); kept as a Low remark, F19. (from money)
- `/SelfBilledInvoice/cac:PrepaidPayment/cbc:ID` = `SCG-ADV-26-0012`: an ID occurring nowhere else — refuted: the ginnery's own payment number; the link to the advance is the billing reference. (from money)
- `/SelfBilledInvoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu Cotton Ginnery, weighbridge`: a company name in a location name — refuted: it names a facility by its operator, which identifies the place. (from parties)
- `/SelfBilledInvoice/cac:PurchaseReference/cbc:ID` = `LCF-FIELD-07`: a field number as purchase reference — refuted: "a reference to an object … to which this Invoice relates"; the field the cotton grew on is such an object. (from logistics, context)
- `/SelfBilledInvoice/cac:ContractDocumentReference/cbc:ID` = `SCG-SEASON-2026`: no target in the flow — refuted: an external season agreement, and the element says what it is. (from logistics)
- `/SelfBilledInvoice/cac:InvoiceLine/cac:Delivery/cac:DeliveryNoteLineReference/cbc:UUID` = `6d32dd14-dac3-5c83-91e2-8c40cef6875b`: matches no line in 03 — refuted: the line reference's own identifier, not the referenced line's. (from context)
- `/SelfBilledInvoice/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`: context refuted (loads over three days); the merge kept logistics' finding, F9. (from context)

## Refuted in the merge
### parties/F3 · Low · Payee named although it is the seller itself
- XPath: `/SelfBilledInvoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- Why (parties): `PayeeParty` is "The Party who receives the Payment." It is the farm, already the accounting supplier and seller, and the payee account names the farm; a separate payee carries information only when someone else is paid. Condition: `PayeeParty` present only if a party other than the accounting supplier receives the payment. Options: (a, preferred) drop it; (b) keep it only if the story has a different payee. Needs decision: no.
- Refuted because: the definition has no "if different from the supplier" condition, and in a self-billed invoice written by the customer, naming who receives the money states it rather than implying it by absence (IND6). Broad and context refuted it on the same grounds; same as 01.

## Changed in the merge
- broad/F2, money/F2, context/F1 → F1: High kept; needs decision set to no for the preferred option (money said yes), option (b) marked as a story change.
- broad/F1, money/F1 → F2: combined, arithmetic redone.
- broad/F3, logistics/F1, context/F4 → F3: combined.
- broad/F4 (Medium), parties/F2 (Low), context/F3 (Medium) → F4: Medium/yes; 03's equivalent stays Low (its definition does not tie the originator to the order).
- broad/F5, money/F5 (Low), parties/F1, context/F2 → F5: Medium/yes.
- broad/F7, money/F6 + F7, context/F8 → split into F7 (identity rates) and F8 (alternative currency); F8 needs decision no (money said yes).
- context/F5 and broad/F11 split by reference: F10 (work report, with logistics/F3), F11 (receipt, with logistics/F4), F12 (statement and farm registration), F13 (project, with context/F6).
- broad/F14 + context/F10 (annotation part) → F14; parties/F7 + context/F10 (physical-location part) → F15; context/F10 (line-status part) → F24: context/F10 split into three because the three parts have different conditions.
- broad/F13 + parties/F4 + parties/F5 → F17: grouped (contacts).
- broad/F10, money/F4, logistics/F5, context/F7 (terms part) → F18: combined, logistics' missing named place included.
- broad/F8 + context/F7 (text part) → F19; money's refutation carried.
- broad/F9, money/F3 (Medium) + F9, context/F9 → F20: Low (money's Medium lowered: an unused base contradicts no other value).
- F22: added by the merge (O with 0 %).
- parties/F3 → Refuted in the merge.
- F25: added by the merge (farm address lines), for consistency with 01 and 03.
- F26: added by the merge (farm registration expiry date), for consistency with 01 and 03.
