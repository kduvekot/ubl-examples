# LLM review: 09-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/09-Invoice.xml`, Git blob `f578132e365ef70fff8b3b325066166662819a4a` (committed)
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

### utilities/09#F1 · High · Full amount billed and collected although the statement says the household pays on account every month
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- XPath: `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- Why: The utility statement that supplements this invoice states monthly payments on account by direct debit on the first working day, settled by the bill against the reading. This invoice has no PrepaidAmount ("The total prepaid amount"), settles nothing and collects the full 38.78 (14 × 2.35 + 14 × 0.42 = 32.90 + 5.88, recalculated in the merge) by a single direct debit on 2026-04-23. The two documents describe incompatible payment arrangements for the same consumption; with both, the household pays March twice. See 08#F1.
- Condition: Invoice 09 and statement 08 describe the same arrangement: either the invoice deducts the payment on account (PrepaidAmount, PayableAmount = balance), or no payments on account exist.
- Options: (a, preferred) keep this invoice as it is and remove the on-account scheme from 08 (the reminder 10 and the credit note 11 follow this invoice); (b) add a PrepaidAmount and a settlement amount here and adjust `10-Reminder.xml` and `11-CreditNote.xml`.
- Needs decision: yes
- From: broad (F1), money (F1), context (F1)

### utilities/09#F2 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. Recounted in the merge: 362 occurrences in 213 files over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale value such as `en-XB` with a list that defines it.
- Needs decision: no
- From: broad (F4), parties (F1), context (F3)

### utilities/09#F3 · Medium · Mandate limited to 12 instructions, open-ended and used for monthly collections since September 2024
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MaximumPaymentInstructionsNumeric` = `12`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:ValidityPeriod/cbc:StartDate` = `2024-09-02`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MandateTypeCode` = `RCUR`
- XPath: `/Invoice/cac:InvoicePeriod/cbc:DescriptionCode` = `MONTH`
- Why: MaximumPaymentInstructionsNumeric is "The maximum number of payment instructions allowed within the validity period". The mandate is recurring, valid from 2024-09-02 with no end date, and the bill is monthly (InvoicePeriod MONTH; statement 08 shows monthly bills for January and February 2026). Recalculated in the merge: monthly collections from October 2024 to this one on 2026-04-23 are 3 (Oct–Dec 2024) + 12 (2025) + 4 (Jan–Apr 2026) = 19 instructions, more than the 12 allowed, so this collection could not be made under the mandate. If the household also paid on account monthly (08#F1), the count is higher still. Refutation tried: no value states that every month since 2024 was collected under this mandate (the household could have paid otherwise for a time), so the contradiction rests on an inference from the monthly billing; that is why the merge keeps it at Medium (money's), not High (broad's).
- Condition: The instruction limit, the validity period and the collection frequency are compatible at the date of this collection.
- Options: (a, preferred) drop MaximumPaymentInstructionsNumeric (an open-ended recurring utility mandate rarely has one); (b) give the mandate a validity period of 12 months that contains April 2026 (a renewed mandate), or describe the limit as per year in the clause.
- Needs decision: no
- From: broad (F2, High), money (F3, Medium)

### utilities/09#F4 · Medium · PayerParty of the mandate is the debtor
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: UBL defines `PaymentMandate/PayerParty` as "The Party, if different from the debtor, that makes the Payment." The debtor of this invoice is its accounting customer Robin Ashdale, and the mandate's payer is the same person, debiting the debtor's own account. The condition of the definition is not met.
- Condition: `PayerParty` is present in the mandate only when someone other than the debtor pays.
- Options: (a, preferred) remove `PayerParty` (its absence means that the debtor pays; the payer account stays); (b) keep it only if the story has someone else pay Robin's water bill.
- Needs decision: no
- From: broad (F3), money (F2), parties (F2), context (F2)

### utilities/09#F5 · Medium · Drinking water classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The world's own SupplyTypeCode list defines GOODS as "A supply of goods, including energy and water delivered through a network." (`world/codelists/gc/SupplyTypeCode.gc`), and SERVICES as "A supply of services." A code exists in the list but is not the one the list assigns to water. The same problem is in 02, 06 and 11.
- Condition: The water line's supply type is GOODS.
- Options: (a, preferred) GOODS.
- Needs decision: no
- From: money (F4)

### utilities/09#F6 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: A water utility serving a state's capital, with its own meter network, is a large organisation; `SMALL` ("Small enterprise") is implausible. 25 companies of the world are registered on 1 January 1996 (parties' count); recounted in the merge: 271 occurrences in 181 files over `world/examples/*/*.xml`. Both look like a default description, not the company's story (no fillers).
- Condition: Size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a, preferred) a size that fits a state water utility and a registration date of its own; (b) drop the two elements where the documents do not need them.
- Needs decision: yes
- From: parties (F3)

### utilities/09#F7 · Low · The customer's bank account given twice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerFinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The account to be debited is stated where the invoice uses it, in the mandate ("The payer's financial account"). The same account, with its full bank and branch description, is repeated under the customer's Person ("The financial account associated with this person"), where the invoice does nothing with it; it is the person's master data, repeated in every example that carries Robin Ashdale. The money part refuted it as "the debtor's account that the direct debit uses"; that is true of the mandate's PayerFinancialAccount, not of the second copy under Person.
- Condition: The debtor's account appears in this invoice only where the payment uses it.
- Options: (a, preferred) drop the account from Person; (b) keep it only with a reason the mandate does not cover.
- Needs decision: no
- From: parties (F4), context (F4); refuted by money (argument above)

### utilities/09#F8 · Low · A 0 % rate on a levy outside the scope of tax
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O (outside the scope of tax) has no rate; a rate of 0 % describes a zero-rated supply (category Z). Same as 06.
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no
- From: money (F5)

### utilities/09#F9 · Low · Exemption reason given for a levy outside the scope of tax
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- Why: TaxExemptionReasonCode is "The reason for tax being exempted"; category O is not an exemption. EN 16931 requires a reason for O, while UBL's definition describes an exemption (semantic conformance: the UBL definition governs, the practice is context). Same as 06.
- Condition: No exemption reason for category O, or the deviation is recorded among the EN 16931 vs UBL findings.
- Options: (a) record the deviation and keep it; (b) drop the reason code and text.
- Needs decision: yes
- From: broad (F5)

### utilities/09#F10 · Low · BeneficiaryParty repeats the party the levy is collected for
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: CollectedForParty ("The Party on whose behalf this item or amount is collected") already names the department (`20410548`); BeneficiaryParty repeats it without a different party. The credit note `11-CreditNote.xml` keeps only BeneficiaryParty, so the two documents describe the third party differently (11#F8).
- Condition: BeneficiaryParty only where it differs from CollectedForParty, and invoice and credit note use the same role(s).
- Options: (a, preferred) drop BeneficiaryParty here and use CollectedForParty in 11.
- Needs decision: no
- From: broad (F6)

### utilities/09#F11 · Low · Supply type "services" on a levy that is no supply
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The sewage levy, collected for the city and outside the scope of tax, is not a supply of the water company whose type could be given; as in `06-Invoice.xml`.
- Condition: The levy line carries no supply type, or one the world's rules define for levies.
- Options: (a, preferred) remove it.
- Needs decision: no
- From: context (F5)

## Checked and consistent
- Lines (redone in the merge): 14 × 2.35 = 32.90; 14 × 0.42 = 5.88; 32.90 + 5.88 = 38.78 = LineExtension, TaxExclusive, TaxInclusive and Payable amounts; tax 0.00 (E 32.90, O 5.88); LineCountNumeric 2.
- Terms: due date 2026-04-23 = 2026-04-02 + 21 days, as the note says (the only invoice of the flow where note and date agree); PenaltyAmount 0.58 = 1.5 % × 38.78 (0.5817); penalty period from 2026-04-24.
- Mandate: the collection on 2026-04-23 is announced more than five days before by this invoice of 2026-04-02 (clause CSW-DD-T3); a single collection of 38.78 is below MaximumPaidAmount 150.00 ("the maximum amount to be paid within a single instruction").
- Accounts: payer account XB64BLUM38010007251840 is named after Robin Ashdale; payee account XB21BLUM38010004189160 is "Coastal State Water Company Ltd", the supplier's account in 06, 07 and 10.
- `10-Reminder.xml` (returned debit of 23 April, 38.78) and `11-CreditNote.xml` (2 m³ of each line at the same prices) refer to this invoice and agree with its amounts and prices. Line 1 agrees with `08-UtilityStatement.xml` (14 m³, meter CSW-W-71844, contract CSW-C-311790).
- Supplier and customer are described as in 08, 10 and 11; Lumeport Public Works Department (`20410548`) as in 06.
- check_ids.py: RF46CSWCINV260319 and both accounts correct.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MandateTypeCode`: SequenceType3Code RCUR as a mandate type, from another element's list — refuted, whether a mandate is recurring or one-off is its type, and the world chose this list on purpose (from money).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`: a private person as accounting customer without tax or register identifiers — refuted, a household has none to give (from parties).
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent`: a late-payment surcharge on a direct debit — refuted, a returned debit makes the payment late, as `10-Reminder.xml` shows (from context).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID`: refuted by money as the account the direct debit uses — the merge disagrees for the copy under Person and keeps it as F7 (from money).

## Changed in the merge
- broad/F2 (High) and money/F3 (Medium) → F3: Medium. The contradiction depends on the inference that the mandate was used monthly since 2024; no value states it. Count of instructions recalculated (19).
- broad/F5 → F9 and money/F5 → F8: kept as two findings (same TaxCategory, different elements and decision status).
- money/F4 (water line) and context/F5 (levy line) → F5 and F11: separate problems (water is GOODS by the world list; a levy is no supply).
- parties/F3 → F6: count recalculated (271 in 181 files).
- broad/F4, parties/F1, context/F3 → F2: count re-made.

## Outside this review
- `08-UtilityStatement.xml` is issued (15:10) before this invoice (15:44) although it refers to it as its parent (08#F8).
