# LLM review: 11-CreditNote.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/11-CreditNote.xml`, Git blob `831c5f12acb5889efdae887718f56b4fd27594fc` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/11#F1 · Medium · A language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. Recounted in the merge: 362 occurrences in 213 files over `world/examples/*/*.xml`.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale value such as `en-XB` with a list that defines it.
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### utilities/11#F2 · Medium · Drinking water classified as a supply of services
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The world's SupplyTypeCode list defines GOODS as "A supply of goods, including energy and water delivered through a network." (`world/codelists/gc/SupplyTypeCode.gc`). The credit repeats the classification of invoice 09, which has the same problem (09#F5).
- Condition: The water line's supply type is GOODS, the same as in the corrected invoice 09.
- Options: (a, preferred) GOODS.
- Needs decision: no
- From: money (F1)

### utilities/11#F3 · Low · Credit for a meter over-reading without the meter, the test, the period and the invoice lines it corrects
- XPath: `/CreditNote/cbc:Note` = `The meter test found the meter over-reading by two cubic metres.`
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `2`
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cbc:CreditedQuantity` = `2`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0319`
- Why: The credit rests on a meter test, but the credit note does not say which meter was tested (the flat's meter is `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterNumber` = `CSW-W-71844`), when, or over which period it over-read; the lines carry no invoice period and no reference to the invoice's line 1 (water) and line 2 (levy). A meter that over-reads does so on every reading since the fault began; crediting exactly 2 m³ against the March invoice implies that the whole error fell into March (2 of 14 m³, 14 % high in that month). If it accumulated over a longer time, the register reading 1844 of `08-UtilityStatement.xml` would also carry it into the next bill.
- Condition: The credit note identifies the meter (and the test) the credit rests on, the period of the over-reading and the invoice lines it corrects, and the credited quantity is consistent with that period's readings.
- Options: (a, preferred) add the invoice period 2026-03-01 to 2026-03-31, line-level references to invoice 09's lines 1 and 2, and the meter in the note, saying that the 2 m³ is March's over-reading; (b) if the fault covered several months, credit each billed month's share, referencing the invoices concerned; (c) a DiscrepancyResponse with a reason code for the meter error.
- Needs decision: no
- From: broad (F2), logistics (F1)

### utilities/11#F4 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible. 25 companies of the world are registered on 1 January 1996 (parties' count); recounted in the merge: 271 occurrences in 181 files over `world/examples/*/*.xml`. Both look like a default description (no fillers).
- Condition: Size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a, preferred) a size that fits a state water utility and a registration date of its own; (b) drop the two elements where the documents do not need them.
- Needs decision: yes
- From: parties (F2)

### utilities/11#F5 · Low · How the credit is settled against the still-open invoice, and the customer's account that no payment means names
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `5.54`
- XPath: `10-Reminder.xml:/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43.78`
- Why: The credited invoice `09-Invoice.xml` is unpaid: its debit was returned and `10-Reminder.xml` asks for 43.78 by 2026-05-11. The note offers a set-off against "the next payment" or a refund, but does not say which payment (the reminded 43.78, which would then be 38.24, or the next monthly debit) and has no PaymentMeans naming the refund account; the customer's account appears only under Person/FinancialAccount, which does not say it is the refund account. Broad, money and parties refuted the account as copied master data because a refund would go to it, and broad refuted the "next payment" as the payment of the reminded amount. Both readings are possible; the merge cannot settle whether the document says enough, so the finding stays Low with Needs decision yes (as context had it).
- Condition: The credit note states how the credit is settled (set-off against the open invoice, or refund to an account stated in PaymentMeans), and carries the customer's account only where it is used.
- Options: (a, preferred) a note that the credit reduces the open amount of invoice 09 (43.78 − 5.54 = 38.24 still due), and remove the unused account; (b) PaymentMeans with the customer's account as refund account.
- Needs decision: yes
- From: context (F2); account refuted by broad, money and parties (arguments above)

### utilities/11#F6 · Low · A 0 % rate on a levy outside the scope of tax
- XPath: `/CreditNote/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O has no rate; a rate of 0 % describes a zero-rated supply (category Z). Same as 06 and 09 (09#F8).
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no
- From: money (F2)

### utilities/11#F7 · Low · Exemption reason given for a levy outside the scope of tax
- XPath: `/CreditNote/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- Why: TaxExemptionReasonCode is "The reason for tax being exempted"; category O is not an exemption. EN 16931 requires a reason for O; the UBL definition governs (semantic conformance). Same as 06 and 09 (09#F9). The line-level place was added in the merge (same value).
- Condition: No exemption reason for O, or the deviation is recorded among the EN 16931 vs UBL findings.
- Options: (a) record and keep; (b) drop it.
- Needs decision: yes
- From: broad (F4)

### utilities/11#F8 · Low · Levy credited for a beneficiary, without the party it was collected for
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `09-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The credit note corrects the collection line of `09-Invoice.xml`, which names the department both as CollectedForParty ("The Party on whose behalf this item or amount is collected") and as BeneficiaryParty. The credit line keeps only BeneficiaryParty, although its note says the levy is "credited for the city" and the line also has CollectedForParty. It reverses an amount collected on behalf of the department, so CollectedForParty is the element that fits, and the two documents describe the third party differently. Context refuted this (the beneficiary suffices to show for whom the levy is credited); that covers who receives the money, not on whose behalf it had been collected, and does not remove the difference from invoice 09.
- Condition: The collection credit line names the third party in the same role(s) as the invoice line it corrects.
- Options: (a, preferred) CollectedForParty (Lumeport Public Works Department, `20410548`), as in the invoice, and drop BeneficiaryParty in both (09#F10); (b) if only one role is wanted, use the same one in invoice and credit note.
- Needs decision: no
- From: broad (F3), parties (F3); refuted by context (argument above)

### utilities/11#F9 · Low · Supply type "services" on a credited levy
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: As in `09-Invoice.xml` (09#F11): the levy collected for the city is not a supply of the water company, so a type of supply has nothing to describe.
- Condition: The levy line carries no supply type.
- Options: (a, preferred) remove it.
- Needs decision: no
- From: context (F3)

## Checked and consistent
- Amounts (redone in the merge): 2 × 2.35 = 4.70; 2 × 0.42 = 0.84; total 5.54 = LineExtension, TaxExclusive, TaxInclusive and Payable amounts; taxable 4.70 (E) and 0.84 (O), tax 0.00; prices, items and tax categories those of invoice 09.
- BillingReference CSWC-INV-26-0319 (2026-04-02) resolves to `09-Invoice.xml`; the 2 m³ credited do not exceed the 14 m³ billed. CreditNoteTypeCode 381 fits.
- Issued 2026-05-05, after the invoice and after `10-Reminder.xml` (2026-05-01).
- Supplier and customer as in `09-Invoice.xml`; the beneficiary has the same register number `20410548` as in 06 and 09.
- check_ids.py: account XB64BLUM38010007251840 correct.

## Considered and refuted
- `/CreditNote/cac:PaymentTerms/cbc:Note`: credit settled against the "next payment" while invoice 09 is still open — refuted by broad and money, the next payment is the payment of the reminded amount, against which the credit can be set off (from broad, money; context's finding on the same note is F5).
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID`: customer's bank account as copied master data — refuted by broad, money and parties, it is the account for a possible refund ("unless refunded"); carried into F5 as the counter-argument (from broad, money, parties).
- `/CreditNote/cbc:Note`: an over-reading of 2 m³ in 14 m³ (14 %) against accuracy class 1 and the 2024 calibration in `08-UtilityStatement.xml` — refuted, a meter test is done when a meter is suspected of failing (from logistics).
- `/CreditNote/cac:CollectionCreditNoteLine/cac:BeneficiaryParty`: no CollectedForParty as on the invoice — refuted by context; the merge disagrees and keeps it as F8 (from context).

## Changed in the merge
- broad/F2 and logistics/F1 → F3: combined; options from both.
- context/F2 → F5: kept Low/yes, with the refutations of broad, money and parties as the counter-argument; the remaining amount 38.24 calculated.
- broad/F4 → F7: the CollectionCreditNoteLine's LEVY code added as a second place (same value).
- broad/F3, parties/F3 → F8: combined; context's refutation answered.
- broad (Outside this review): the amount still due after the credit corrected from 38.22 to 38.24 (43.78 − 5.54).
- parties/F2 → F4: count recalculated (271 in 181 files).

## Outside this review
- `10-Reminder.xml` demands 43.78 by 2026-05-11; after this credit note of 2026-05-05 the amount actually due is 38.24 (43.78 − 5.54). Whether a corrected reminder was needed, and whether the meter test was already pending when the reminder was sent, is a timeline question of the flow (broad, logistics).
