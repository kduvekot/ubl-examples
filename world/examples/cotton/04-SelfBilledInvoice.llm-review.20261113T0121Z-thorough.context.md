# LLM review: 04-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/04-SelfBilledInvoice.xml`, Git blob `7ff28661ff5e42f702b07e4477e9454c7a6c7ebb` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### cotton/04#F1 · High · Pricing currency Lume, but every price is in coral
- XPath: `/SelfBilledInvoice/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount/@currencyID` = `XLC`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- Why: PricingCurrencyCode is "A code signifying the currency used for prices in the Invoice". The
  only price of the invoice is 0.226 XLC per kg, in coral, and the season price of seed cotton
  between a Lisavu farm and a Lisavu gin is the same coral price as in the advance invoice 01
  (`01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.226`).
  The header says prices are in Lume and gives a Lume-to-coral pricing exchange rate that no amount
  of the invoice uses. The header and the price contradict each other.
- Condition: PricingCurrencyCode, if present, is the currency of the prices in the invoice, and a
  PricingExchangeRate is present only if prices are stated in another currency than the document
  currency.
- Options: (a, preferred) leave PricingCurrencyCode and PricingExchangeRate out: prices are in
  coral, the document currency; (b) if the season agreement fixes the price in Lume (because the
  lint is sold to Bayvarra), state the price in XBL and keep the rate, and say so in a note.
- Needs decision: yes for option (b), which changes the story of the price; no for (a)

### cotton/04#F2 · Medium · Tax representative for a domestic purchase between two Lisavu parties, with no tax registration to represent
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: TaxRepresentativeParty is "The Party authorized to act as the Tax Representative for this
  Self Billed Invoice". A tax representative acts for a party that is not established in the
  taxing country (own knowledge of tax practice). Both the farm and the ginnery are Lisavu
  companies, Lisavu has no general sales tax (the tax category is O, "No general sales tax"), and
  neither party has a PartyTaxScheme in the invoice. The presumptive tax is withheld by the gin
  itself. A customs broker (in the other flows it acts as the importer's customs agent, e.g.
  `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`)
  has nothing to represent here. The same party is in the credit note 05.
- Condition: the self-billed invoice names a tax representative only if one of its parties needs
  one under the tax of the invoice, and the story says for whom it acts.
- Options: (a, preferred) leave TaxRepresentativeParty out; (b) give the story a reason (e.g. the
  farm being represented for the presumptive tax) and make it visible in the document.
- Needs decision: yes

### cotton/04#F3 · Medium · The textile mill as originator and beneficiary of the farm's seed cotton invoice, with the mill's season document as originator document
- XPath: `/SelfBilledInvoice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- XPath: `/SelfBilledInvoice/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- Why: OriginatorCustomerParty is "The Party who originated the Order to which this Invoice is
  related". The order of this invoice is the ginnery's call-off SCG-SEASON-2026/03 under its season
  agreement with the farm; the ginnery, not the mill, originated it. BeneficiaryParty ("for whom the
  associated transaction is ultimately intended") names the mill for a purchase of seed cotton that
  the ginnery buys and processes for its own account; the mill orders lint only later (08, issued
  2026-02-24) and is not a party to the farm–gin contract. LTM-SEASON-2026 as
  OriginatorDocumentReference ("a reference to an originator document") ties the farm's invoice to
  a mill document that no example contains and that the farm has no part in. The delivery note 03
  names the same two roles.
- Condition: originator and beneficiary roles and the originator document are present only if the
  flow's documents show the mill originating this order or the seed cotton being bought for it.
- Options: (a, preferred) leave the three out; (b) make the mill's role explicit in the story (a mill
  contract under which this lot is bought) and keep them.
- Needs decision: yes

### cotton/04#F4 · Medium · Despatch Advice reference pointing to a delivery note
- XPath: `/SelfBilledInvoice/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledInvoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: DespatchDocumentReference is "A reference to a Despatch Advice associated with this
  document". LCF-DN-26-0193 is the farm's DeliveryNote (03), which the invoice already references,
  correctly, as DeliveryNoteDocumentReference. UBL 2.5 has distinct document types and references for
  the two; the same delivery note given as a despatch advice uses the element for a document of
  another kind, and suggests a despatch advice exists that the flow does not contain.
- Condition: DespatchDocumentReference, if present, points to a Despatch Advice.
- Options: (a, preferred) leave DespatchDocumentReference out; the delivery note reference covers it.
- Needs decision: no

### cotton/04#F5 · Low · Document references whose kind does not match the document behind the ID, or that say nothing about it
- XPath: `/SelfBilledInvoice/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `/SelfBilledInvoice/cac:WorkReportDocumentReference/cbc:ID` = `SCG-OUT-26-0311`
- XPath: `/SelfBilledInvoice/cac:StatementDocumentReference/cbc:ID` = `SCG-ACC-LCF-26-02`
- XPath: `/SelfBilledInvoice/cac:AdditionalDocumentReference/cbc:ID` = `XL-FARM-REG-0412`
- Why: ReceiptDocumentReference is "A reference to a Receipt Advice"; SCG-WB-26-0311 is cited by the
  delivery note as an additional document of the weighing at the gin
  (`03-DeliveryNote.xml:/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`),
  i.e. a weighbridge ticket, not a Receipt Advice. WorkReportDocumentReference is "A reference to a
  Work Report": the invoice prices seed cotton per kilogram delivered, so a gin outturn report
  (SCG-OUT) has no bearing on the amount; the credit note 05 cites a different work report
  (SCC-CLS-26-0311) for the same delivery. StatementDocumentReference ("A reference to a
  Statement") cites what reads as the farm's February account statement from an invoice issued on
  7 February, before such a statement can exist. XL-FARM-REG-0412 is given without DocumentTypeCode
  or description. None of these documents is in the flow, so the kind must come from the
  reference itself.
- Condition: each reference uses the element for the kind of document it points to, points to a
  document that can exist at the issue date, and states its kind where the ID does not.
- Options: (a, preferred) keep only the references the invoice needs (contract, order, delivery
  note, the advance), and give the weighbridge ticket and farm registration, if kept, an
  AdditionalDocumentReference with a DocumentTypeCode or description; (b) keep them all and add
  types and descriptions that justify the elements.
- Needs decision: no

### cotton/04#F6 · Low · Project reference to a chamber of commerce quality project in a seed cotton invoice
- XPath: `/SelfBilledInvoice/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: ProjectReference is "A reference to a project associated with this document". The ID is the
  Selanu Chamber of Commerce's; the purchase of seed cotton under a season agreement is not part of
  a project in any document of the flow, and nothing says what the project does with this invoice.
  Also in 03 and 05.
- Condition: the invoice carries a project reference only if the story has a project this purchase
  belongs to, and says what it is.
- Options: (a, preferred) leave it out; (b) give the project a role in the story.
- Needs decision: yes (whether such a project exists in the world)

### cotton/04#F7 · Low · DAP delivery terms with a haulage charge paid by the buyer, described as an allowance
- XPath: `/SelfBilledInvoice/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:ChargeIndicator` = `true`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Haulage allowance`
- Why: Under DAP the seller delivers at the named place and bears the cost of carriage to it (own
  knowledge of Incoterms 2020). Here the gin, as buyer, pays the farm a cartage charge of 180 XLC on
  top of the price. That is a common arrangement for seed cotton, but it is not what DAP says, and
  the reason text calls a charge (ChargeIndicator true) an "allowance", which in UBL is the opposite
  of a charge. A reader cannot tell which party bears the haulage.
- Condition: the delivery terms and the haulage charge agree on who bears the cost of carriage to
  the gin, and the reason text matches the charge indicator.
- Options: (a, preferred) keep the charge and use delivery terms under which the buyer pays the
  carriage (e.g. FCA farm), with a reason such as "Haulage to the gin"; (b) keep DAP and drop the
  charge, with the haulage in the price.
- Needs decision: yes (who bears the haulage is part of the season agreement)

### cotton/04#F8 · Low · Exchange rates and currencies that change nothing
- XPath: `/SelfBilledInvoice/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledInvoice/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledInvoice/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- Why: TaxExchangeRate is "The exchange rate between the document currency and the tax currency"
  and PaymentExchangeRate "between the document currency and the payment currency"; both convert
  coral into coral at rate 1. The tax and payment currency codes repeat the document currency. A
  Lume alternative payment currency for a payment between two Lisavu parties into a coral account
  (`/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`) has no
  use in the story. The values carry no information for this invoice (UBL IND5).
- Condition: currency codes and exchange rates other than the document currency appear only where
  an amount of the invoice is in, or may be paid in, that other currency.
- Options: (a, preferred) leave the tax, payment and alternative payment currencies and their rates
  out; (b) give the Lume alternative a reason in the story.
- Needs decision: no

### cotton/04#F9 · Low · Allowance/charge details that the single haulage charge does not use
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:PrepaidIndicator` = `false`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:SequenceNumeric` = `1`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:BaseAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: SequenceNumeric orders "the sequence of calculations applied when there are multiple
  allowances or charges"; there is one. BaseAmount is "The monetary amount to which the multiplier
  factor is applied"; there is no multiplier factor, and the charge is 0.010 XLC per kg × 18,000 kg
  = 180.000 XLC, not derived from 4,068.000. AllowanceCharge/PaymentMeans ("A means of payment for
  this allowance or charge") repeats the invoice's credit transfer: the charge is paid together with
  the invoice. These elements are present without a business reason (UBL IND5).
- Condition: the allowance/charge carries only elements that its calculation or settlement uses.
- Options: (a, preferred) leave SequenceNumeric, BaseAmount and the charge's PaymentMeans out (keep
  PerUnitAmount, which the amount is calculated from).
- Needs decision: no

### cotton/04#F10 · Low · Annotation repeats the note; line status "NoStatus" and the farm's physical location carry nothing
- XPath: `/SelfBilledInvoice/cac:Annotation/cbc:AnnotationContent` = `Written by the gin on the farm's behalf under the self-billing agreement.`
- XPath: `/SelfBilledInvoice/cbc:Note[2]` = `Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Delivery/cac:DeliveryNoteLineReference/cbc:LineStatusCode` = `NoStatus`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: The annotation ("structured annotation providing contextual or explanatory information")
  says in English only what Note[2] already says. LineStatusCode "No status" gives no status of the
  referenced line. Party/PhysicalLocation (the farm's fields with coordinates) is not used by the
  invoice: the delivery location is the gin's weighbridge. All three read as fillers or copied
  master data (UBL IND5).
- Condition: each of these elements either says something the invoice does not say elsewhere and
  uses, or is absent.
- Options: (a, preferred) leave the annotation, the line status code and the supplier's physical
  location out.
- Needs decision: no

## Checked and consistent
- The advance: `/SelfBilledInvoice/cac:BillingReference/cac:SelfBilledInvoiceDocumentReference/cbc:ID` = `SCG-SBI-26-0191`
  and PrepaidPayment 1,017.000 XLC paid on 2026-01-13 agree with 01 (amount and issue date).
- Delivery note reference and line reference (line 1 of LCF-DN-26-0193) resolve to 03; 18,000 kg on
  both.
- Self-billing context: InvoiceTypeCode 389, customer (ginnery) as signatory, payee the farm with its
  own account, BuyerAssignedReference for the ginnery's internal routing.
- Presumptive tax tiers: 1 % of 2,000.000 = 20.000; 2 % of 2,068.000 = 41.360; total 61.360 =
  WithholdingTaxTotalAmount; the tier ranges fit the rates.
- Haulage charge: 0.010 × 18,000 = 180.000 = ChargeTotalAmount.
- RF77SCGSBI260194 and XL67BSEL0020004817534 pass `check_ids.py`.

## Considered and refuted
- `/SelfBilledInvoice/cac:InvoiceLine/cac:Delivery/cac:DeliveryNoteLineReference/cbc:UUID` = `6d32dd14-dac3-5c83-91e2-8c40cef6875b`:
  a UUID that matches no line in 03 — refuted because LineReference/UUID is "A universally unique
  identifier for this line reference", the reference's own identifier, not the referenced line's.
- `/SelfBilledInvoice/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`: a three-day invoice period
  for a delivery on 2026-02-05 — refuted because the three trailer loads may have been harvested and
  hauled over those days; the period is what the invoice covers.
- `/SelfBilledInvoice/cac:PurchaseReference/cbc:ID` = `LCF-FIELD-07`: suspected as unrelated —
  refuted because PurchaseReference names "an object … to which this Invoice relates", and a field
  the seed cotton was picked from is such an object.
- `/SelfBilledInvoice/cac:CollectionInvoiceLine/cbc:Note` = `Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.`:
  a collection line in a self-billed invoice suspected as misplaced — refuted for this lens because
  the definition ("an item or amount collected on behalf of a third party") fits a levy for the
  chamber's cotton fund, with the chamber as BeneficiaryParty of the line.
- `/SelfBilledInvoice/cac:PayeeParty`: payee equal to the seller — refuted because the UBL
  definition has no "if different" condition.

