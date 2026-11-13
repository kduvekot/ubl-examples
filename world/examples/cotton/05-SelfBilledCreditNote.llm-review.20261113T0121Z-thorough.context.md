# LLM review: 05-SelfBilledCreditNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/05-SelfBilledCreditNote.xml`, Git blob `ae986b70b136e1ac8647dd8051159b9d408be29a` (committed)
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

### cotton/05#F1 · High · The cited classing certificate says Middling, and is verified after the credit note, which credits a downgrade to Strict Low Middling
- XPath: `/SelfBilledCreditNote/cac:AdditionalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:Description` = `2,500 kg classed Strict Low Middling instead of Middling.`
- XPath: `/SelfBilledCreditNote/cbc:IssueDate` = `2026-02-14`
- XPath: `08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- XPath: `08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- Why: The credit note exists because 2,500 kg were classed below the contracted grade. The only
  certificate it cites, XL-CLS-2026-0042, is the cotton classing certificate that the forecast 02,
  the revision 07 and the order 08 describe as "Grade Middling", i.e. the contracted grade, and whose
  signature those documents give as verified on 2026-02-20, six days after this credit note was
  issued. A certificate stating Middling cannot support a credit for cotton classed Strict Low
  Middling, and it cannot be cited as a basis before it was verified. The classing result that
  supports the downgrade is the work report SCC-CLS-26-0311, which the note also cites.
- Condition: every certificate or report the credit note cites as the reason for the downgrade
  states the lower grade and exists at the credit note's issue date; or the reference makes clear
  that it is not the basis of the downgrade.
- Options: (a, preferred) leave the reference to XL-CLS-2026-0042 out and let the classing report
  SCC-CLS-26-0311 carry the reason; (b) if XL-CLS-2026-0042 is meant to be the classing of this
  farm's delivery, make the certificate in 02, 07, 08 and 10 describe that lot (with the 2,500 kg at
  Strict Low Middling) and date it before 2026-02-14.
- Needs decision: yes (which document records the classing of the farm's delivery is part of the story)

### cotton/05#F2 · High · Pricing currency Lume, but the credited price is in coral
- XPath: `/SelfBilledCreditNote/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Price/cbc:PriceAmount/@currencyID` = `XLC`
- XPath: `/SelfBilledCreditNote/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- Why: PricingCurrencyCode is "A code signifying the currency used for prices in the Self Billed
  Credit Note". The only price, the grade difference of 0.03 per kg, is in coral; no amount uses the
  Lume-to-coral pricing rate. The header contradicts the price, as in the invoice 04.
- Condition: PricingCurrencyCode, if present, is the currency of the prices in the credit note.
- Options: (a, preferred) leave PricingCurrencyCode and PricingExchangeRate out.
- Needs decision: no

### cotton/05#F3 · Medium · Tax representative in a domestic credit note between two Lisavu parties
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: TaxRepresentativeParty is "The Party authorized to act as the Tax Representative for this
  Self Billed Credit Note". Both parties are established in Lisavu, there is no general sales tax
  (category O), neither party has a tax registration in the document, and the presumptive tax is
  withheld by the gin itself. A customs broker has nothing to represent here (same as 04).
- Condition: the credit note names a tax representative only if one of its parties needs one, and
  the story says for whom it acts.
- Options: (a, preferred) leave it out; (b) give it a reason in the story, consistently with 04.
- Needs decision: yes

### cotton/05#F4 · Medium · Despatch Advice reference pointing to a delivery note
- XPath: `/SelfBilledCreditNote/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledCreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: DespatchDocumentReference is "A reference to a Despatch Advice associated with this
  document"; LCF-DN-26-0193 is the delivery note 03, already referenced correctly as
  DeliveryNoteDocumentReference.
- Condition: DespatchDocumentReference, if present, points to a Despatch Advice.
- Options: (a, preferred) leave DespatchDocumentReference out.
- Needs decision: no

### cotton/05#F5 · Low · Originator document of the mill, a project, a statement and a receipt advice that the credit note does nothing with
- XPath: `/SelfBilledCreditNote/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- XPath: `/SelfBilledCreditNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- XPath: `/SelfBilledCreditNote/cac:StatementDocumentReference/cbc:ID` = `SCG-ACC-LCF-26-02`
- XPath: `/SelfBilledCreditNote/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: OriginatorDocumentReference ties a quality credit between gin and farm to a mill document
  the farm is not a party to (and, unlike 04, without any originator party). ProjectReference names
  a chamber of commerce project no document of the flow describes. StatementDocumentReference ("A
  reference to a Statement") cites the farm's February account statement from a credit note issued
  in mid-February, before the statement can exist. ReceiptDocumentReference ("A reference to a
  Receipt Advice") points to what the delivery note 03 cites as the weighing at the gin
  (`03-DeliveryNote.xml:/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`),
  a weighbridge ticket, not a Receipt Advice; the credit is for grade, not weight. None carries a
  type or description.
- Condition: the credit note references only documents that bear on the credit and exist at its
  issue date, each in the element for its kind.
- Options: (a, preferred) keep the self-billed invoice, the order, the contract, the delivery note
  and the classing report; leave the others out.
- Needs decision: yes for the originator document and project (they belong to the story of 04 and
  03); no for the rest

### cotton/05#F6 · Low · Delivery terms, exchange rates to the same currency, an alternative Lume payment and the farm's fields carried into a quality credit
- XPath: `/SelfBilledCreditNote/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/SelfBilledCreditNote/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledCreditNote/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledCreditNote/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- XPath: `/SelfBilledCreditNote/cac:Annotation/cbc:AnnotationContent` = `Written by the gin on the farm's behalf under the self-billing agreement.`
- Why: The credit note credits a grade difference and is settled by set-off (PaymentMeansCode 97,
  "Set off against the payment of the self-billed invoice"). Delivery terms do not bear on a grade
  credit; coral-to-coral exchange rates at 1 and a Lume alternative payment currency are
  meaningless for an amount that is never paid but set off in coral; the farm's physical location
  is not used; the annotation repeats in substance what the note says. These read as copied from the
  invoice (UBL IND5).
- Condition: the credit note carries only data that its purpose (a grade credit set off against 04)
  uses.
- Options: (a, preferred) leave them out.
- Needs decision: no

### cotton/05#F7 · Low · Lint classing grade applied to seed cotton
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cbc:Name[2]` = `Seed cotton`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `2500`
- Why: Grades such as Middling and Strict Low Middling are lint grades, assigned by classing samples
  of ginned bales (own knowledge of cotton classing). The credit line credits 2,500 kg of seed
  cotton, the farm's delivered product, at 0.03 per kg. That works if the season agreement prices
  seed cotton by the grade of the lint ginned from it, but then 2,500 kg is a seed cotton quantity
  while the classing speaks of lint, and the note ("2,500 kg classed Strict Low Middling") does not
  say which. The reader cannot tell whether 2,500 kg of seed cotton or of lint was downgraded.
- Condition: the credit note says whether the quantity is seed cotton or the lint ginned from it,
  and how the grade of the lint applies to the farm's seed cotton.
- Options: (a, preferred) word the discrepancy as "lint ginned from 2,500 kg of seed cotton classed
  Strict Low Middling"; (b) credit by the lint weight with a corresponding item.
- Needs decision: yes

## Checked and consistent
- Billing reference SCG-SBI-26-0194 of 2026-02-07 resolves to 04; same order, contract, delivery
  note, buyer and seller.
- Credit note type 261 (self-billed credit note), the ginnery as signatory and set-off by
  PaymentMeansCode 97 fit the self-billing arrangement and the payment terms note.
- Line: 0.03 × 2,500 kg = 75.000; collection line 0.750 = 1 % of 75.000, the cotton fund levy rate
  of 04 (40.680 on 4,068.000).
- DueDate 2026-02-16 is the date of the remittance advice 06 that settles invoice and credit note.

## Considered and refuted
- `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:ResponseCode` = `2`: a code of UN/EDIFACT 4465
  ("Below specification goods") in a response suspected as from the wrong list — refuted because
  4465 is the adjustment reason list, which is what the reason for a credit note is.
- `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: "Special
  agreement" for a classing fee suspected as a code that does not name the reason — refuted because
  UNTDID 5189 has no classing code and the fee is set by the season agreement.
- `/SelfBilledCreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`: InvoicePeriod is "A period
  (rather than a specific Invoice)" while a specific invoice is referenced — refuted as a finding;
  the period is the delivery period of the credited invoice and does no harm, though it repeats 04.
- `/SelfBilledCreditNote/cac:WorkReportDocumentReference/cbc:ID` = `SCC-CLS-26-0311`: a classing
  report as a work report — refuted because a report of classing work done on the farm's cotton is a
  report of work, and it is the basis of the credit.
