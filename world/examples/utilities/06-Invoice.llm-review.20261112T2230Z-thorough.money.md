# LLM review: 06-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/06-Invoice.xml`, Git blob `a42ab090a50a199d6ef007b111b5c77252c9f943` (committed)
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

### utilities/06#F1 · High · Due date is 21 days after the invoice date; the terms say 30 days net
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-04-24`
- Why: Issued 2026-04-02, 30 days net gives 2026-05-02; the due dates and the start of the penalty period follow a 21-day term. The note and the structured dates contradict each other; a surcharge from 2026-04-24 would be charged on a payment the note says is not yet due. Same in 02 ("30 days net") and 13 ("45 days net").
- Condition: Note, due dates and penalty period start agree.
- Options: (a) due date 2026-05-02 and penalty from 2026-05-03; (b, preferred if 21 days is the world's utility term, as in 09) note "21 days net".
- Needs decision: no

### utilities/06#F2 · Medium · Drinking water classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The world's SupplyTypeCode list defines GOODS as "A supply of goods, including energy and water delivered through a network." (`world/codelists/gc/SupplyTypeCode.gc`), so water through the mains is GOODS by the list's own definition. SERVICES on the sewage levy (the collection line) is not affected. Same in 02 (electricity, gas), 09 and 11 (water).
- Condition: The supply type of the drinking water line is GOODS.
- Options: (a, preferred) GOODS.
- Needs decision: no

### utilities/06#F3 · Low · Penalty period of one month for a surcharge "per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`
- Why: `PenaltyPeriod` is "the period during which penalties may apply". A period of one month limits the surcharge to the first month of delay, while the note says 1.5 % per month late, i.e. recurring. PenaltyAmount 3.57 is the surcharge of one month.
- Condition: The penalty period and the note describe the same rule.
- Options: (a, preferred) a penalty period without an end (StartDate only), with the note saying the amount is per month; (b) keep one month and say "1.5 % surcharge if paid late".
- Needs decision: no

### utilities/06#F4 · Low · A tax rate of 0 % on a supply outside the scope of tax
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: `Percent` is "the tax rate for this category, expressed as a percentage". Category O (services outside scope of tax) has no rate; stating 0 % describes it as zero-rated, which is category Z. EN 16931 forbids a rate for O (BR-O-05); the point here is the UBL meaning. For category E (exempt) the 0 % is equally a statement about a rate that does not apply, though less misleading.
- Condition: The category O of the levy carries no Percent.
- Options: (a, preferred) leave Percent out for O (and consider the same for E).
- Needs decision: no

## Checked and consistent
- 86 × 2.35 = 202.10; 86 × 0.42 = 36.12; total 238.22 = TaxExclusive = TaxInclusive = Payable; taxable amounts per category 202.10 (E) and 36.12 (O); tax 0.00.
- PenaltyAmount 3.57 = 1.5 % × 238.22 (3.5733).
- PaymentID RF03CSWCINV260317 passes the ISO 11649 check; payee account XB21BLUM38010004189160 passes the IBAN-like check and is the account paid in 07.
- The levy line names Lumeport Public Works Department as the party it is collected for; the amount is in the payable total, which the remittance 07 pays in full.

## Considered and refuted
- `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount`: including the collected levy in the line extension total was suspected — refuted: UBL 2.5 has no separate total for collection lines, and the levy is part of what the customer pays.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: MPNS (mass payment net system) with rail LUMEPAY for a monthly bill — plausible, contradicts nothing.
