# LLM review: 05-SelfBilledCreditNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/05-SelfBilledCreditNote.xml`, Git blob `ae986b70b136e1ac8647dd8051159b9d408be29a` (committed)
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

### cotton/05#F1 · High · Pricing currency Lume, but the credited price is in coral
- XPath: `/SelfBilledCreditNote/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Price/cbc:PriceAmount` = `0.03`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:PricingCurrencyCode` = `XBL`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for prices in the Self Billed Credit Note". The only price, the grade difference of 0.03 per kg, is in XLC (`currencyID`); no amount uses the Lume-to-coral pricing rate (a Lume price would be 0.075 XBL, recomputed, which appears nowhere). The header contradicts the price, as in the credited invoice 04 (04#F1).
- Condition: either every price is in the currency `PricingCurrencyCode` names, with the pricing rate converting it, or there is no pricing currency and no pricing exchange rate.
- Options: (a, preferred) drop `PricingCurrencyCode` and `PricingExchangeRate`, consistently with 04; (b) state the price in Lume if the season agreement fixes it in Lume (story change, would need a decision, together with 01 and 04).
- Needs decision: no (for the preferred option; money said yes, as for 04)
- From: broad (F3), money (F1), context (F2)

### cotton/05#F2 · High · The downgrade cites a certificate that says Middling and is signed six days later
- XPath: `/SelfBilledCreditNote/cac:AdditionalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/SelfBilledCreditNote/cbc:IssueDate` = `2026-02-14`
- XPath: `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:Description` = `2,500 kg classed Strict Low Middling instead of Middling.`
- XPath: `08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:EndDate` = `2026-02-22`
- Why: the credit note grants a price reduction because 2 500 kg were classed Strict Low Middling, and the only certificate it cites is `XL-CLS-2026-0042`. Wherever that certificate is described (02, 07, 08, 10, 11, 15, 16) it is the chamber's classing certificate of the lint sold to the mill, "Grade Middling", the contracted grade, signed on 2026-02-20, six days after this credit note; the ginning it would class ended only on 2026-02-22 (10). A certificate stating Middling cannot support a credit for Strict Low Middling, and cannot be cited before it was verified. The classing report `SCC-CLS-26-0311`, cited as work report, may be the document meant (broad, logistics, context). Logistics rated it Low; it is a contradiction with a referenced object in several examples, so High (broad, context).
- Condition: every certificate or report the credit note cites as the reason for the downgrade exists at its issue date and states the lower grade; or the reference makes clear it is not the basis of the downgrade.
- Options: (a, preferred) drop the reference to `XL-CLS-2026-0042` and let the classing report `SCC-CLS-26-0311` (with a type or description, see F11) carry the reason; (b) if `XL-CLS-2026-0042` is meant to be the classing of this farm's delivery, make the certificate in 02, 07, 08 and 10 describe that lot (with the SLM part) and date it before 2026-02-14.
- Needs decision: yes (which document records the classing of the farm's delivery is part of the story; logistics and context said yes, broad no)
- From: broad (F1), logistics (F2, Low), context (F1)

### cotton/05#F3 · High · The taxable amount ignores the allowance, which has no tax category
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `75.000`
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:Amount` = `5.000`
- XPath: `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `70.000`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `O`
- Why: recomputed: 2 500 × 0.03 = 75.000 line amount, less the 5.000 allowance = 70.000 = `TaxExclusiveAmount`; the only subtotal (category O) gives 75.000 as "The net amount to which the tax percent (rate) is applied". The subtotals do not add up to the tax-exclusive amount, and the allowance carries no `TaxCategory`, so the credit note does not say in which category it reduces the base; in 04 the document-level charge carries category O. Money rated it Medium; it is arithmetic that does not hold, as 04#F2, so High.
- Condition: the allowance has a tax category, and the subtotals' taxable amounts add up to `TaxExclusiveAmount`, each allowance counted in its category.
- Options: (a, preferred) give the allowance category O like the 04 charge and set the O subtotal to 70.000; (b) if the fee is not part of the supply, move it out of the tax-exclusive amount (see F21 on what the fee is).
- Needs decision: no
- From: broad (F2), money (F2, Medium)

### cotton/05#F4 · Medium · The delivery note given as a despatch advice
- XPath: `/SelfBilledCreditNote/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledCreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: `DespatchDocumentReference` is "A reference to a Despatch Advice associated with this document"; `LCF-DN-26-0193` is the farm's Delivery Note 03, already cited with `DeliveryNoteDocumentReference`. No despatch advice exists in the flow. Same as 04#F3.
- Condition: `DespatchDocumentReference`, if present, refers to a despatch advice.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: broad (F8), logistics (F1), context (F4)

### cotton/05#F5 · Medium · The farm as payee of a credit that flows to the ginnery
- XPath: `/SelfBilledCreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`
- XPath: `/SelfBilledCreditNote/cac:PaymentTerms/cbc:Note` = `Set off against the payment of the self-billed invoice.`
- Why: `PayeeParty` is "The Party who receives the Payment." A self-billed credit note reduces what the ginnery owes the farm: the 69.250 credited flows from the farm to the ginnery, here by clearing between partners (code 97) against the payment of 04, which 06 shows as a credit line. The farm receives nothing under this credit note, so naming it as payee reverses the role; the value is apparently carried over from 04. (Unlike 01 and 04, where the farm does receive the payment and parties' payee finding was refuted in the merge.)
- Condition: the credit note names no payee, or names the party that receives the credited amount.
- Options: (a, preferred) drop `PayeeParty`, since the amount is set off and nothing is paid; (b) name the ginnery.
- Needs decision: no
- From: broad (F5), parties (F2)

### cotton/05#F6 · Medium · A customs broker as tax representative of a domestic farm credit
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID` = `IC41585`
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Self Billed Credit Note." Both parties are Lisavan, there is no general sales tax, neither has a tax registration in the document, and the presumptive tax is withheld by the ginnery itself; a customs broker (elsewhere an importer's customs agent) has nothing to represent. Same as 04#F5.
- Condition: a tax representative is named only if one of the parties needs one for a tax this document declares, with the reason visible, and then a party whose role is tax representation.
- Options: (a, preferred) drop it, consistently with 04; (b) record the rule that requires it in the world's tax story.
- Needs decision: yes
- From: broad (F6), money (F5, Low), parties (F1), context (F3)

### cotton/05#F7 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: as 01#F2: 5305 `O` is "Services outside scope of tax"; the line credits goods. 17 files use `O`, 5 with `GOODS` (merge count; broad's "17 examples" counted every use).
- Condition: the goods line and its subtotal carry a code whose meaning covers goods outside the scope of tax, or the deviation is recorded.
- Options: (a, preferred) one world-wide decision; (b) keep `O` as a recorded deviation.
- Needs decision: yes
- From: broad (F7)

### cotton/05#F8 · Low · Tax and payment currency repeat the document currency, with identity exchange rates
- XPath: `/SelfBilledCreditNote/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledCreditNote/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledCreditNote/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledCreditNote/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- Why: XLC to XLC at 1; nothing is converted, and the credit is not even paid but set off (code 97). No business reason (IND5). Same as 04#F7.
- Condition: tax or payment currency and rate only where they differ from the document currency.
- Options: (a, preferred) drop the four elements.
- Needs decision: no
- From: broad (F9), money (F6), context (F6, rates part)

### cotton/05#F9 · Low · Alternative payment currency for a credit that is set off
- XPath: `/SelfBilledCreditNote/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- XPath: `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`
- Why: the credit is "set off against the payment of the self-billed invoice", and 06 nets it in coral; no payment in Lume can take place, and no payable alternative amount is given. Same as 04#F8.
- Condition: no alternative payment currency unless a payment in it can occur under this document.
- Options: (a, preferred) drop both elements.
- Needs decision: no
- From: broad (F9), money (F7), context (F6, alternative-currency part)

### cotton/05#F10 · Low · Invoice period starts two days before the only delivery
- XPath: `/SelfBilledCreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`
- XPath: `/SelfBilledCreditNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- Why: the credit note repeats the invoice period of 04 (2026-02-03 to 05) for a delivery that 03 and its own `Delivery` date to 2026-02-05 only. Context refuted it (the period of the credited invoice, does no harm); it is the same question as 04#F9 and must be resolved the same way, so it stays Low.
- Condition: the period and the delivery dates of 03, 04 and 05 describe the same deliveries.
- Options: (a, preferred) align with the fix of 04 (period from 2026-02-05, or a delivery period in 03).
- Needs decision: no
- From: logistics (F4); context (considered and refuted, argument carried)

### cotton/05#F11 · Low · The classing report that carries the downgrade is cited by ID only
- XPath: `/SelfBilledCreditNote/cac:WorkReportDocumentReference/cbc:ID` = `SCC-CLS-26-0311`
- Why: the classing report is the basis of the credit (broad, logistics, context), but it is filed as a "work report" with only an ID, no type or description, and exists in no example; the reader has to infer from the prefix that it is the chamber's classing report. Context refuted the element choice (a report of classing work is a work report); that is accepted, so only the missing description remains, Low.
- Condition: the reference says what the report is (classing report of the farm's delivery).
- Options: (a, preferred) add a document type or description; (b) cite it as an `AdditionalDocumentReference` with a type.
- Needs decision: no
- From: broad (F12, work-report part); context (considered and refuted the element, carried)

### cotton/05#F12 · Low · Weighbridge ticket cited as a receipt advice
- XPath: `/SelfBilledCreditNote/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: `ReceiptDocumentReference` is "A reference to a Receipt Advice associated with this document"; the ID is the gin's weighbridge ticket, cited by 03 as an additional document. No receipt advice is in the flow, and the credit is for grade, not weight. Same as 04#F11.
- Condition: the document is cited as the same kind in 03, 04 and 05, matching the element, and only where the credit note uses it.
- Options: (a, preferred) drop it here (the credit does not rest on the weighing); (b) cite it as an additional document with type "Weighbridge ticket".
- Needs decision: no
- From: logistics (F3), context (F5, receipt part)

### cotton/05#F13 · Low · Statement reference before the statement can exist
- XPath: `/SelfBilledCreditNote/cac:StatementDocumentReference/cbc:ID` = `SCG-ACC-LCF-26-02`
- Why: `StatementDocumentReference` ("A reference to a Statement") cites what reads as the farm's February account statement from a credit note issued on 14 February, without type or description; the credit note does nothing with it. Same as 04#F12; the reading as a monthly statement is an inference.
- Condition: the reference points to a document that exists at the issue date and has a role here, or it is absent.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: broad (F12), context (F5, statement part)

### cotton/05#F14 · Low · The mill's season document as originator document of a farm credit
- XPath: `/SelfBilledCreditNote/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- Why: `OriginatorDocumentReference` ties a quality credit between ginnery and farm to a mill document the farm is not a party to, which exists in no example, and, unlike 04, without any originator party (parties noted the missing roles as an inconsistency belonging to 03 and 04). It belongs to the same story question as 03#F10 and 04#F4.
- Condition: the credit note carries an originator document only if the story makes the mill originate the purchase, consistently with 03 and 04.
- Options: (a, preferred) drop it, with the roles in 03/04; (b) keep it with the story of 04#F4 option (b) and a type.
- Needs decision: yes
- From: broad (F12, originator part), context (F5, originator part)

### cotton/05#F15 · Low · Project reference to a chamber of commerce quality project
- XPath: `/SelfBilledCreditNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: a chamber project no document of the flow describes; nothing says what it has to do with this credit (a quality credit might be the one place where a quality project matters, but nothing says so). Same as 03#F3, 04#F13.
- Condition: a project reference only if the story has a project this credit belongs to, described.
- Options: (a, preferred) leave it out; (b) give the project a role in the story.
- Needs decision: yes
- From: broad (F12, project part), context (F5, project part)

### cotton/05#F16 · Low · Annotation repeats the note
- XPath: `/SelfBilledCreditNote/cac:Annotation/cbc:AnnotationContent` = `Written by the gin on the farm's behalf under the self-billing agreement.`
- XPath: `/SelfBilledCreditNote/cbc:Note[2]` = `Self-billed credit note under the season agreement.`
- Why: the annotation repeats in substance what the note says and adds no structure or information (IND5). Same as 04#F14.
- Condition: the annotation adds information the note does not carry, or is absent.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: context (F6, annotation part)

### cotton/05#F17 · Low · The ginnery's customs-trader number and the farm's fields in a domestic credit note
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: section 4.8. A credit for below-grade domestic seed cotton involves neither customs nor the place of the fields; both read as copied master data (IND5).
- Condition: every identifier and location of the parties is one the document has a use for.
- Options: (a, preferred) leave both out.
- Needs decision: no
- From: parties (F6), context (F6, physical-location part)

### cotton/05#F18 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`); reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from the company's history; (b) drop it; (c) record a register-wide date.
- Needs decision: yes
- From: parties (F5)

### cotton/05#F19 · Low · Contacts do not fit the role or the party
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledCreditNote/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- Why: the document routes to "Farm payments", but the ginnery's contact is its lint sales desk; the farm is a one-person micro sole proprietorship with a "Customer service officer" in "Sales". Same as 04#F17.
- Condition: the ginnery's contact handles farm payments or seed-cotton purchasing (or is absent), and the farm's contact fits a one-person farm.
- Options: (a, preferred) role-specific contacts; (b) drop them.
- Needs decision: no
- From: broad (F13), parties (F3, F4)

### cotton/05#F20 · Low · Delivery terms carried into a quality credit
- XPath: `/SelfBilledCreditNote/cac:DeliveryTerms/cbc:ID` = `DAP`
- Why: the credit note credits a grade difference and is set off; delivery terms do not bear on it and read as copied from 04 (IND5), where they are themselves questioned (04#F18).
- Condition: the credit note carries delivery terms only if the credit depends on them.
- Options: (a, preferred) leave them out.
- Needs decision: no
- From: context (F6, delivery-terms part)

### cotton/05#F21 · Low · Who bears the classing fee is unclear from the allowance's direction
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:ChargeIndicator` = `false`
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Classing fee`
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`
- XPath: `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount` = `5.000`
- Why: in a credit note an allowance reduces the amount credited: the ginnery credits itself 75.000 and reduces that by a 5.000 "classing fee", so the farm ends up 5.000 better off, i.e. the ginnery bears the fee. A classing fee is normally a cost of the party having its cotton classed; if the farm bears it, it would be a charge raising the credit to 80.000. The text and code 64 ("special agreement") do not say which is meant. Broad read the indicator and reason as pointing in opposite directions (Medium); since the ginnery refunding the fee is a possible reading the document does not exclude, the merge keeps money's Low with a decision.
- Condition: the direction of the classing-fee amount matches the party that bears the fee, and the credit note says who that is.
- Options: (a, preferred) say in `AllowanceChargeReason` that the ginnery refunds/bears the farm's classing fee, if that is the story; (b) if the farm bears it, make it a charge, credit 80.000 and adjust 06.
- Needs decision: yes
- From: broad (F4, Medium), money (F3)

### cotton/05#F22 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: as 01#F8: the zero tax total names the absence of a tax as a scheme, without ID.
- Condition: the zero tax total names a real Lisavan scheme with ID, or is absent.
- Options: (a, preferred) one decision for the 9 files with this name.
- Needs decision: yes
- From: broad (F11)

### cotton/05#F23 · Low · A 0 % rate on tax category O
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: `Percent` is "The tax rate for this category, expressed as a percentage"; a supply outside the scope of tax has no rate, and 0 % reads as zero-rating. Added by the merge, as 01#F9 and 04#F22.
- Condition: a category stating the supply is outside the scope of tax carries no `Percent`.
- Options: (a, preferred) drop `Percent` in both places.
- Needs decision: no
- From: merge

### cotton/05#F24 · Low · Withholding tax reversed without scheme, basis or rate
- XPath: `/SelfBilledCreditNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.500`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:WithholdingTaxTotal/cac:TaxSubtotal[2]/cbc:Percent` = `2`
- Why: the withholding in 04 is tiered (1 % up to 2 000, 2 % above) with subtotals; here only 1.500 is given. Recomputed: it is 2 % of 75.000, correct because the credited value falls entirely in the upper tier (20.000 + 41.360 = 61.360 on 4 068.000 before, 20.000 + 39.860 = 59.860 on 3 993.000 after, difference 1.500), but the credit note gives no subtotal, taxable amount, rate or tax scheme, so the tax the 1.500 belongs to is not even named.
- Condition: the withholding tax total names its scheme and gives the taxable amount and rate from which 1.500 follows.
- Options: (a, preferred) one subtotal: taxable 75.000, 2 %, the OTH "Presumptive tax on farm produce" as in 04.
- Needs decision: no
- From: broad (F10), money (F4)

### cotton/05#F25 · Low · A lint grade applied to seed cotton, and the downgraded lint not visible
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cbc:Name[2]` = `Seed cotton`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `2500`
- XPath: `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:Description` = `2,500 kg classed Strict Low Middling instead of Middling.`
- Why: Middling and Strict Low Middling are lint grades, assigned by classing samples of ginned bales (own knowledge). The line credits 2 500 kg of seed cotton at 0.03 per kg. That works if the season agreement prices seed cotton by the grade of its lint, but the text does not say whether 2 500 kg of seed cotton or of lint was downgraded. What became of the lower-grade lint is not visible either: the 6 129 kg shipped to the mill are all Middling (logistics).
- Condition: the credit note says whether the quantity is seed cotton or the lint ginned from it, and how the lint grade applies to the farm's seed cotton.
- Options: (a, preferred) word the discrepancy as "lint ginned from 2,500 kg of seed cotton classed Strict Low Middling"; (b) credit by the lint weight with a corresponding item.
- Needs decision: yes
- From: context (F7), logistics (F2, part on the material)

### cotton/05#F26 · Low · Address lines repeat the farm's structured address and mix languages
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the same four lines as in 01 and 03 repeat `StreetName`, `Description`, `District` and `CityName`, and lines 1 and 4 combine the Lisavan and English forms in one text without `languageID`, although `Line` "may be repeated only to provide the same content in multiple natural languages". No part raised it here; added by the merge (appended, without renumbering) so the farm's address is treated as in 01#F6 and 03#F5, where parties' counter-argument (a Lisavan print format) is recorded.
- Condition: the farm's postal address states each part once, and language-specific renderings carry `languageID`.
- Options: (a, preferred) drop the address lines; (b) keep only lines with information not in the structured parts.
- Needs decision: no
- From: merge

### cotton/05#F27 · Low · Expiry date on the farm's commercial-register entry
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: `RegistrationExpirationDate` is "The date upon which a registration expires (e.g., registration for an import/export license)"; the registration described is the farm's entry in the island companies register, which normally does not expire. Parties (in 01) read it as a seasonal farm registration (`XL-FARM-REG-0412` in 04); possible, but that is not the company registration described. No part raised it here; added by the merge (appended, without renumbering) for consistency with 01#F7 and 03#F6.
- Condition: the expiry date belongs to a registration that expires and is the one described.
- Options: (a, preferred) drop it; (b) make the world's register rules say that sole proprietorships register yearly.
- Needs decision: yes
- From: merge

## Checked and consistent
- Arithmetic (redone): 2 500 KGM × 0.03 per 1 KGM = 75.000; less 5.000 allowance = 70.000 tax-exclusive = tax-inclusive (tax 0.000); `AllowanceTotalAmount` 5.000; withholding 1.500 (see F24); levy `/SelfBilledCreditNote/cac:CollectionCreditNoteLine/cbc:LineExtensionAmount` = `0.750` = 1 % of 75.000, as 40.680 is 1 % of 4 068.000 in 04; payable 70.000 − 1.500 + 0.750 = 69.250 = `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `69.250` (the farm keeps the tax no longer withheld and is relieved of the levy).
- 06 nets the credit: `06-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `69.250`; 3 210.320 − 69.250 = 3 141.070 = `06-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `3141.070`, on 2026-02-16, this credit note's `DueDate`.
- Billing reference `SCG-SBI-26-0194` with issue date 2026-02-07 resolves to 04; same order, contract, delivery note, buyer and seller; 2 500 kg is part of the 18 000 kg billed there.
- Discrepancy code 2 of 4465 "Below specification goods" fits a downgrade; reference ID 1 points to line 1; type 261 "Self billed credit note"; the ginnery signs; set-off by code 97 fits the terms note.
- Rates 0.4 and 2.5 are inverse and the same as in 04. Item `LCF-SC`, HS 520100, CPC 01921 as in 01, 03, 04.
- The levy's beneficiary is the Selanu Chamber of Commerce (`IC42133`), as in 04; farm and ginnery identified as in 01, 03, 04 (parties).

## Considered and refuted
- `/SelfBilledCreditNote/cbc:DueDate` = `2026-02-16`: a due date on a credit settled by set-off — refuted: it tells when the set-off takes place, and 06 does it on that date. (from broad)
- `/SelfBilledCreditNote/cac:CollectionCreditNoteLine`: reversal of a share of the levy — refuted: consistent with the levy collected in 04 (1 % of the credited value). (from broad)
- `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: from the right list? / does not name the reason — refuted: 5189 is the allowance reason list (matches `ChargeIndicator` false), it has no classing code, and the fee is set by the season agreement; the open question of who bears the fee is F21. (from money, context)
- `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`: clearing between partners against the credit transfer in 06 — refuted: the credit is deducted from the transfer that pays 04, as 06 shows. (from money)
- Missing originator and beneficiary (04 names the mill): not a finding here — recorded in 03 and 04 where the roles are present; the originator document here is F14. (from parties)
- `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:ResponseCode` = `2`: "Below specification goods" from the wrong list — refuted: 4465 is the adjustment reason list, and the code fits. (from logistics, context)
- `/SelfBilledCreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-02-03`: context refuted (repeats 04, no harm); kept by the merge as F10 with logistics. (from context)
- `/SelfBilledCreditNote/cac:WorkReportDocumentReference/cbc:ID` = `SCC-CLS-26-0311`: a classing report as a work report — refuted: a report of classing work is a work report, and it is the basis of the credit; its missing description is F11. (from context)

## Changed in the merge
- broad/F3, money/F1, context/F2 → F1: High; needs decision no for the preferred option (money said yes), as 04#F1.
- broad/F1 (High), logistics/F2 (Low), context/F1 (High) → F2: High/yes; logistics' material point moved to F25.
- broad/F2 (High), money/F2 (Medium) → F3: High, as 04#F2.
- broad/F9, money/F6 + F7, context/F6 (rates and alternative-currency parts) → F8 and F9, split as in 04.
- broad/F12 split by reference into F11 (work report, ID only), F13 (statement), F14 (originator document, Low/yes), F15 (project, Low/yes); context/F5 split into F12–F15 accordingly (its "yes for originator and project, no for the rest" kept per finding).
- context/F6 split into F8, F9, F16 (annotation), F17 (physical location, with parties/F6), F20 (delivery terms).
- broad/F13 + parties/F3 + parties/F4 → F19: grouped (contacts).
- broad/F4 (Medium/yes), money/F3 (Low/yes) → F21: Low/yes.
- broad/F10 + money/F4 → F24: combined, tier arithmetic redone.
- context/F7 + logistics/F2 (material part) → F25.
- F23: added by the merge (O with 0 %).
- F26: added by the merge (farm address lines), for consistency with 01 and 03.
- F27: added by the merge (farm registration expiry date), for consistency with 01 and 03.
