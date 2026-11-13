# LLM review: 01-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/01-SelfBilledInvoice.xml`, Git blob `aee01edf4f4e0c209dc01462389e7115dcceae7c` (committed)
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

### cotton/01#F1 · High · Payment due date of the advance contradicts "paid on issue"
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27`
- XPath: `/SelfBilledInvoice/cbc:DueDate` = `2026-01-13`
- XPath: `/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `Paid on issue by transfer. …`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-01-13`
- Why: PaymentMeans/PaymentDueDate is "The date on which payment is due for this means of payment".
  The only means of payment in this prepayment invoice is due on 2026-02-27, which is 45 days after
  issue (the farm's standard "45 days net" of `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `45 days net.`).
  The invoice's own DueDate, its payment terms ("Paid on issue by transfer") and the final
  self-billed invoice, which records the advance as paid on 2026-01-13, all say the advance was due
  and paid on the issue date. Two due dates in one document for the same payment contradict each
  other.
- Condition: every due date in the example (DueDate, PaymentMeans/PaymentDueDate) is the same date
  and agrees with the payment terms and with the PaidDate recorded in 04.
- Options: (a, preferred) set PaymentMeans/PaymentDueDate to the issue date, as everything else in
  the flow says the advance was paid on issue; (b) leave PaymentDueDate out, since DueDate already
  carries it.
- Needs decision: no

### cotton/01#F2 · Low · The farm's physical location (the cotton fields) in a prepayment invoice
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: Party/PhysicalLocation is "The physical location of this party". A prepayment invoice for an
  advance on a season agreement does nothing with where the fields are: no delivery takes place
  under it and no location-dependent tax or levy is computed (the payment terms say both fall on
  the delivery). The aggregate, with its coordinates and the farm's website as InformationURI,
  reads as copied from the party's master data. The same aggregate is in 03, 04, 05 and 06 of the
  flow (counted with `grep -c PhysicalLocation` over `world/examples/cotton/*.xml`); only in the
  delivery note 03, where the farm despatches the goods, does the document have a use for it.
- Condition: the supplier party in this example carries no PhysicalLocation, or the document states
  a purpose for it.
- Options: (a, preferred) leave PhysicalLocation out of the invoice; (b) keep it and give it a
  reason in the story (e.g. the advance is tied to a field).
- Needs decision: no

## Checked and consistent
- Price × quantity: 0.226 XLC/kg × 4,500 kg = 1,017.000 XLC = line, LineExtension, TaxExclusive,
  TaxInclusive and Payable amounts. Tax category O, 0 %, with TaxableAmount 1,017.000 and
  TaxAmount 0.000.
- InvoiceTypeCode 386 (prepayment invoice) fits the notes (an advance under the season agreement)
  and the self-billing customization; the advance is deducted in 04
  (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:PrepaidAmount` = `1017.000`,
  with `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BillingReference/cac:SelfBilledInvoiceDocumentReference/cbc:ID` = `SCG-SBI-26-0191`).
- The signatory is the ginnery, which writes self-billed invoices on the farm's behalf; buyer and
  seller roles (ginnery buys seed cotton, farm sells) fit a self-billed invoice.
- RF reference RF61SCGSBI260191 and the payee account XL67BSEL0020004817534 pass `check_ids.py`;
  the account is the farm's, as in 04.
- Industry codes: ISIC 0163 (post-harvest crop activities, which includes ginning) for the ginnery,
  0116 (growing of fibre crops) for the farm.
- HS 5201.00 and CPC 01921 for seed cotton: HS 5201 covers raw cotton, ginned or not (own knowledge
  of the HS explanatory notes).

## Considered and refuted
- `/SelfBilledInvoice/cac:PayeeParty`: payee equal to the seller suspected as redundant — refuted
  because the UBL definition ("The Party who receives the Payment") has no "if different from the
  seller" condition; stating the payee is not wrong.
- `/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `4500`: a quantity of goods on an
  advance invoice suspected as implying a delivery — refuted because a prepayment invoice commonly
  states the quantity the advance is for, and the note says the advance is deducted later.
- `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`: a tax total for a
  scheme that does not exist ("No general sales tax") suspected as a filler — refuted because it
  states positively that no sales tax applies, which IND6 (nothing implied by absence) asks for.
- `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: real-time gross settlement
  for a small farm payment suspected as implausible — refuted because "paid on issue" requires
  immediate settlement, which RTGS gives.
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.lisavufarm.example`:
  the farm's home page as "a document providing information about this location" — refuted as a
  separate finding; it is part of F2.
