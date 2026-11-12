# LLM review: 08-RemittanceAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

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

### ore/08#F1 · Medium · A province is given in `Region`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries"; a province is "the political or administrative division of a country" (`CountrySubentity`), as for Bayvarra's states. 104 XML examples carry "Province of Ferrano" (`grep -rl --include='*.xml'`).
- Condition: the province is in `CountrySubentity` in every address.
- Options: (a) preferred: move it; (b) rename it if it is an economic region.
- Needs decision: no

### ore/08#F2 · Low · Two references to the payer's payment order with different values
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0304`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VI-0304`
- Why: PaymentOrderReference is "an internal reference to the order for payment from the payer to the payer's bank"; PayerReference is "an internal reference to the payer's order for payment". Both name the same thing, the payer's payment order (whose ID `VI-PAY-26-0304` is also the PaymentMeans/InstructionID), yet carry two different values; "VI-0304" refers to nothing else in the flow (it resembles the order number VI-PO-26-0304).
- Condition: each reference has a distinct meaning in this document, and a reader can tell what PayerReference identifies.
- Options: (a) preferred: drop PayerReference (the payment order is identified by PaymentOrderReference and InstructionID); (b) give it a value that is a different payer reference the story explains (e.g. the payment run).
- Needs decision: no

### ore/08#F3 · Low · The line repeats the invoice and the parties
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SM-INV-26-0312`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SM-INV-26-0312`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Serravona Mining`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: the invoice paid is referenced twice in the same line, once as a billing reference and once as a generic document reference with type "Invoice"; and the line-level accounting parties ("related to the remittance information reported on this line") are the same as the document's. With one line and one invoice, the second invoice reference and the line parties add nothing the document uses.
- Condition: the invoice is referenced once in the line, and line-level parties are present only where they differ from the header.
- Options: (a) preferred: keep BillingReference/InvoiceDocumentReference only and drop the line parties; (b) keep the DocumentReference only if it refers to another document (e.g. the order).
- Needs decision: no

### ore/08#F4 · Low · The payer's contact is its sales order desk
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the sender of a remittance advice is the payer; its contact answers questions about the payment (accounts payable/treasury). Valdara's sales order desk ("Customer service officer") is given, copied from master data; the payee's contact is likewise its sales office.
- Condition: the payer's contact is a function that deals with payments.
- Options: (a) preferred: Valdara's accounts-payable contact; (b) omit.
- Needs decision: no

### ore/08#F5 · Low · Party master data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: the payer's stock-exchange listing and warehousing provider (in no role in the flow), and the payee's mine location with its road conditions, have no use in an advice of payment. Same master data in 75 XML examples each (SecurityListing, service provider).
- Condition: every aggregate of the parties has a use in this remittance advice.
- Options: (a) preferred: leave them out.
- Needs decision: no

## Checked and consistent
- InvoiceDocumentReference `SM-INV-26-0312` with issue date 2026-03-11 resolves to 07; amount paid 17 037 943 = PayableAmount of 07; balance 0.
- Payee account `XU420351041700000000104729` and RF reference `RF73SMINV260312` are those of 07 (check digits OK per check_ids.py); payer account is Valdara's.
- Dates: issued 2026-04-09, one day before the due date 2026-04-10 of 07; the 2 % discount (until 2026-03-21) was not taken, consistent with paying the full amount.
- Totals: TotalDebitAmount = DebitLineAmount = TotalPaymentAmount = 17 037 943, TotalCreditAmount 0.

## Considered and refuted
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF73SMINV260312`: an RF creditor reference in an element for "an internal reference to the order for payment by the invoicing party" — refuted because the definition adds "This may have been requested of the payer by the payee to accompany the payer's remittance", which is exactly what 07 asks ("Quote RF73SMINV260312").
- `/RemittanceAdvice/cbc:TotalCreditAmount` = `0`: a zero total as filler — refuted, it states that no credit notes are offset, a real statement in a remittance.
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`: refuted, a supplier payment for goods.
- The carrier's invoice `06-Invoice.xml` has no remittance advice in the flow — refuted as a finding of this example: nothing requires one, and this advice is explicitly about the ore invoice.
