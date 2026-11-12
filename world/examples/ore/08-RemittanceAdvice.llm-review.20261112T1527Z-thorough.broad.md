# LLM review: 08-RemittanceAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/08-RemittanceAdvice.xml`, Git blob `ba4a236a16cc3b9d330f7fd945ee82d84e44ac69` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/08#F1 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province
  belongs in `CountrySubentity`. 104 `*.xml` files do the same
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/08#F2 · Low · The paid invoice is referenced twice in the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SM-INV-26-0312`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SM-INV-26-0312`
- Why: the BillingReference/InvoiceDocumentReference is the dedicated reference to the invoice being
  paid; the line's DocumentReference ("A reference to a document associated with this remittance
  advice line") repeats the same invoice with the same date and only adds a type code. The second
  reference carries no information the first does not, and a reader may wonder which other document
  is meant.
- Condition: each document is referenced once per line, in the element made for it.
- Options: (a, preferred) keep the billing reference and drop the duplicate; (b) use the
  DocumentReference for a different associated document (e.g. the order) if the story needs one.
- Needs decision: no

### ore/08#F3 · Low · Contacts do not fit the payment roles
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the payer's contact in a remittance advice answers questions about the payment (accounts
  payable or treasury), the payee's about allocating it (accounts receivable). Both are sales
  customer-service desks; Valdara's is a sales desk although Valdara is the paying customer.
- Condition: both contacts belong to the accounting functions of the parties.
- Options: (a, preferred) accounts-payable / accounts-receivable contacts; (b) drop job title and
  department.
- Needs decision: no

### ore/08#F4 · Low · Data without use in a remittance: service provider and the mine's site conditions
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: a remittance advice "specifies details of an actual payment". Valdara's logistics service
  provider (Castrano Logistics, warehousing and despatch) and the access conditions of Serravona's
  mine and rail siding do nothing in it; they are copied from master data (section 4.8). The service
  provider is in 75 `*.xml` files (`grep -rl --include='*.xml' 'VI-SP-2026-01'`); the mine's
  physical location also appears in the ore invoice
  (`07-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions`).
- Condition: the remittance carries no party data that the payment does not use.
- Options: (a, preferred) leave both out of the remittance; (b) keep only what identifies the parties
  for allocation of the payment.
- Needs decision: no

## Checked and consistent
- The invoice reference resolves to `07-Invoice.xml` (ID and issue date 11 March); the amount paid
  17 037 943 XUF equals its PayableAmount; balance 0; total debit = total payment, total credit 0.
- Paid on 9 April: after the discount period (11–21 March), so no discount is due; before the due
  date 10 April, so no penalty interest.
- Payee account and branch equal the invoice's payee account; payment ID and invoicing-party
  reference quote the invoice's RF reference `RF73SMINV260312`; the payer's account
  `XU790351041600000000209458` is Valdara's at the Ferrano main branch (bank 03510, branch 41600,
  matching the branch ID `03510-41600`).
- PaymentOrderReference and InstructionID both `VI-PAY-26-0304`; payment purpose `SUPP`
  (SupplierPayment) fits a payment to the ore supplier.
- `check_ids.py`: RF references and both accounts OK.

## Considered and refuted
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF73SMINV260312`: suspected the RF creditor
  reference is not "an internal reference to the order for payment by the invoicing party" —
  refuted because the definition continues "This may have been requested of the payer by the payee
  to accompany the payer's remittance", which is exactly what an RF reference is.
- `/RemittanceAdvice/cbc:PayerReference` = `VI-0304`: suspected a duplicate of the payment order
  reference — refuted because the payer's own reference and its payment order to the bank are
  different identifiers.

## Outside this review
- The freight invoice `FRC-INV-26-0311` (`06-Invoice.xml`) is not remitted in the flow; whether its
  payment belongs in the flow is a question of the flow's composition.
