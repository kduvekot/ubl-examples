# LLM review: 09-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/09-Invoice.xml`, Git blob `f578132e365ef70fff8b3b325066166662819a4a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/09#F1 · High · The invoice ignores the monthly payments on account that its statement describes
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- Why: Statement 08, which explains this invoice, says the household pays on account each month by direct debit on the first working day, and that "the next bill settles it against the reading" (`08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`). This invoice has no PrepaidAmount and settles nothing. It bills the full month and collects it once, 21 days after the invoice date. See 08#F1.
- Condition: Invoice 09 and statement 08 describe the same payment arrangement. If payments on account exist, the invoice deducts them.
- Options: (a, preferred) keep this invoice as it is and remove the on-account scheme from 08; (b) add a PrepaidAmount and a settlement amount here.
- Needs decision: yes

### utilities/09#F2 · Medium · The mandate's PayerParty is the debtor
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: UBL defines `PayerParty` in a payment mandate as "The Party, if different from the debtor, that makes the Payment." Robin Ashdale is the AccountingCustomerParty (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`), so the definition's condition is not met.
- Condition: The mandate has no PayerParty, or names a party other than the debtor.
- Options: (a, preferred) remove PayerParty; the payer account is enough.
- Needs decision: no

### utilities/09#F3 · Medium · A limit of 12 instructions in an open-ended mandate used for monthly collections since 2024
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MaximumPaymentInstructionsNumeric` = `12`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:ValidityPeriod/cbc:StartDate` = `2024-09-02`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MandateTypeCode` = `RCUR`
- Why: UBL defines the element as "the number of maximum payment instructions allowed within the validity period". The validity period has no end, and the bill is monthly (`/Invoice/cac:InvoicePeriod/cbc:DescriptionCode` = `MONTH`). From September 2024 to this collection on 2026-04-23 there would have been about 20 monthly collections, so a limit of 12 within the validity period would already be used up and this collection could not be made under the mandate.
- Condition: The instruction limit, the validity period and the monthly frequency allow this collection.
- Options: (a, preferred) remove the limit, which is unusual for a recurring utility mandate; (b) end the validity period, or describe the limit as per year in the clause.
- Needs decision: no

### utilities/09#F4 · Medium · Drinking water classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The world's SupplyTypeCode list defines GOODS as "A supply of goods, including energy and water delivered through a network." (`world/codelists/gc/SupplyTypeCode.gc`). The same problem is in 02, 06 and 11.
- Condition: The water line's supply type is GOODS.
- Options: (a, preferred) GOODS.
- Needs decision: no

### utilities/09#F5 · Low · A 0 % rate on a levy outside the scope of tax
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O has no rate. A rate of 0 % describes a zero-rated supply (category Z). Same as 06#F4.
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no

## Checked and consistent
- 14 × 2.35 = 32.90 and 14 × 0.42 = 5.88 add up to 38.78, which is the TaxExclusive, TaxInclusive and Payable amount. Tax 0.00.
- The due date 2026-04-23 is 21 days after 2026-04-02, as the terms note says (the only invoice in the flow where note and date agree).
- PenaltyAmount 0.58 = 1.5 % × 38.78 (0.5817). The penalty period starts 2026-04-24.
- Payment means 49 (direct debit) with a mandate. The mandate's MaximumPaidAmount of 150.00, "the maximum amount to be paid within a single instruction", is above 38.78.
- The payer account XB64BLUM38010007251840 and the payee account XB21BLUM38010004189160 pass the IBAN-like check. RF46CSWCINV260319 passes the ISO 11649 check.
- Credit note 11 credits 2 m³ of each line at the same prices; reminder 10 claims the full 38.78.

## Considered and refuted
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID`: suspected of being master data copied into the invoice. Refuted: it is the debtor's account that the direct debit of this invoice uses.
- `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MandateTypeCode`: SequenceType3Code RCUR as a mandate type was suspected of coming from another element's list. Refuted: whether a mandate is recurring or one-off is its type, and the world chose this list on purpose.
