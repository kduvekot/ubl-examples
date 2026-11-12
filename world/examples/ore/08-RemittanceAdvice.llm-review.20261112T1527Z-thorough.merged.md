# LLM review: 08-RemittanceAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/08-RemittanceAdvice.xml`, Git blob `ba4a236a16cc3b9d330f7fd945ee82d84e44ac69` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
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
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located" and Address/CountrySubentity as "The territorial
  division of a country, such as a county or state, expressed as text". A province is a territorial
  division of Urvania; Bayvarran addresses put their states in CountrySubentity.
  `<cbc:Region>Province of` occurs 219 times in 104 XML examples (`grep -rl --include='*.xml'` and
  `grep -rh … | wc -l` over `world/examples`, recounted in the merge).
- Condition: the province of every Urvanian address in this example is in `cbc:CountrySubentity`
  and not in `cbc:Region`, or the world states why Region is used on purpose.
- Options: (a, preferred) move the province to CountrySubentity for all Urvanian addresses, as for
  Bayvarra; (b) keep Region and record in the world why.
- Needs decision: yes (it changes the Urvanian address format in every flow and may be deliberate)
- From: broad (F1), parties (F1), context (F1)

### ore/08#F2 · Low · Two different values for the payer's payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0304`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VI-0304`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VI-PAY-26-0304`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to
  the payer's bank" and PayerReference "An internal reference to the payer's order for payment".
  Both name the payer's own order for this payment, yet they carry two different values; the
  instruction ID agrees with the first. `VI-0304` refers to nothing else in the flow (it resembles
  the order number `VI-PO-26-0304`), so a reader cannot tell what it identifies that
  `VI-PAY-26-0304` does not.
- Condition: each payer-side reference identifies a distinguishable object the reader can tell
  apart, or the two that mean the same carry the same value, or one is left out.
- Options: (a, preferred) drop PayerReference, since PaymentOrderReference and InstructionID already
  identify the payment order; (b) give PayerReference a value that is clearly another payer-side
  object the story explains (e.g. the payer's payment run).
- Needs decision: no
- From: money (F1), context (F2); broad had refuted it (see "Changed in the merge")

### ore/08#F3 · Low · The paid invoice is referenced twice on the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SM-INV-26-0312`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SM-INV-26-0312`
- Why: BillingReference/InvoiceDocumentReference ("A reference to an invoice") is the dedicated
  reference to the invoice being paid; the line's DocumentReference ("A reference to a document
  associated with this remittance advice line") repeats the same invoice with the same issue date and
  adds only the type code `Invoice`. It tells the payee nothing more, and a reader may wonder which
  other document is meant. The logistics part counted the same double reference in 9 remittance
  advices (lxml over `*/*RemittanceAdvice*.xml`; not recounted in the merge).
- Condition: each document is referenced once on the line, in the element meant for it.
- Options: (a, preferred) keep the billing reference and drop the DocumentReference; (b) use the
  DocumentReference only for another associated document (e.g. the order) if the story needs one.
- Needs decision: no
- From: broad (F2), money (F2), logistics (F1), context (F3, first half)

### ore/08#F4 · Low · Line-level parties repeat the document-level parties
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104137`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Serravona Mining`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: the line parties are "The Accounting Supplier Party related to the remittance information
  reported on this Remittance Advice Line" (and likewise for the customer); they serve a remittance
  covering invoices of several suppliers or customers. Here the only line pays one invoice between
  the same two parties as the document level
  (`/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` =
  `XU-R-104137`, `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID`
  = `XU-R-104274`), so they add nothing (IND5).
- Condition: the line carries its own parties only where they differ from the document level.
- Options: (a, preferred) leave them out of this line; (b) keep them if the story makes the
  remittance cover more than one supplier, and show that.
- Needs decision: no
- From: parties (F4), context (F3, second half)

### ore/08#F5 · Low · Contacts do not fit the payment roles
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party". A remittance advice goes from the payer's
  accounts payable (or treasury) to the payee's accounts receivable, which matches the payment to
  its open items. Valdara Industries, the payer and sender, gives its sales order desk, the wrong side
  of the transaction; Serravona Mining, the payee, is given its sales office, not the function that
  allocates payments. Both are copied from master data (Valdara's contact in 75 XML examples,
  Serravona's in 7, per the parties part).
- Condition: the accounting customer's contact belongs to accounts payable or treasury and the
  accounting supplier's to accounts receivable, or each is left out.
- Options: (a, preferred) a contact per function, using the one that fits; (b) leave the contacts
  (or job title and department) out.
- Needs decision: no
- From: broad (F3), parties (F2), context (F4)

### ore/08#F6 · Low · Party master data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: a remittance advice is "A document that specifies details of an actual payment". Valdara's
  share listing and its warehousing provider Castrano Logistics (in no role in the flow), and the
  mine's physical location with its road-access conditions and coordinates, do nothing in it
  (section 4.8, IND5). SecurityListing and Castrano Logistics are in 75 XML examples each
  (`grep -rl --include='*.xml'`, recounted); the mine's physical location also appears in
  `07-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions`.
- Condition: every aggregate of the parties has a use in this remittance advice, or the document
  says why it carries it.
- Options: (a, preferred) leave them out, keeping only what identifies the parties for allocating the
  payment; (b) give them a role in the story and show it in the flow.
- Needs decision: no
- From: broad (F4), parties (F3), context (F5)

## Checked and consistent
- Totals (redone in the merge): TotalDebitAmount = DebitLineAmount = TotalPaymentAmount = 17 037 943
  = `07-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `17037943`; TotalCreditAmount
  0; balance 0.
- The invoice reference `SM-INV-26-0312` with issue date 2026-03-11 resolves to `07-Invoice.xml`.
- Issued 2026-04-09 12:10: after the discount period (ends
  `07-Invoice.xml:/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-03-21`), so no
  discount is due, and before the due date 2026-04-10, so no penalty interest.
- Payee account `XU420351041700000000104729` and branch equal the invoice's; PaymentID and
  InvoicingPartyReference quote the invoice's RF reference `RF73SMINV260312` (check digits valid).
  Payer account `XU790351041600000000209458` passes the IBAN-style check, is in XUF, named
  `Valdara Industries SUA`, at the Ferrano main branch `03510-41600` embedded in the account, and is
  Valdara's account in all 10 XML examples that carry it (per the money part).
- PaymentMeansCode 30 (credit transfer) and purpose `SUPP` fit the payment of a supplier invoice.
- Parties described identically in all eight ore examples; roles as in `07-Invoice.xml`;
  `check_ids.py` passes.

## Considered and refuted
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF73SMINV260312`: suspected misuse of an element
  for "an internal reference to the order for payment by the invoicing party" — refuted because the
  definition continues "This may have been requested of the payer by the payee to accompany the
  payer's remittance", which is what the RF creditor reference of `07-Invoice.xml` is (from broad,
  money, context).
- `/RemittanceAdvice/cbc:TotalCreditAmount` = `0` as filler — refuted: it states that no credit notes
  are offset (from context).
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP` — refuted, a supplier
  payment for goods (from context).
- No remittance advice for the freight invoice `06-Invoice.xml` — refuted as a finding of this
  example: nothing requires one, and this advice is about the ore invoice (from money, context; also
  under "Outside this review").
- English renderings in Italian form, `+999` telephone numbers, `0990:10427` under ISO 6523 (not
  checked against the ICD register), `CREVXUFR` as a possible real BIC — refuted as in the other ore
  examples: proper names, E.164 code 999 unassigned, ICD 0990 not assigned to own knowledge, `XU`
  user-assigned (from parties).

## Changed in the merge
- broad, "Considered and refuted" on `/RemittanceAdvice/cbc:PayerReference` = `VI-0304` ("the payer's
  own reference and its payment order to the bank are different identifiers") → F2 with money/F1 and
  context/F2: the merge disagrees, because the two definitions both describe the payer's order for
  payment, and nothing in the document or the flow says what else `VI-0304` would identify.
- broad/F1, context/F1 (Needs decision: no) + parties/F1 (yes) → F1 Needs decision: yes, because the
  change touches the Urvanian address format in every flow and may be deliberate.
- context/F3 (double invoice reference and line parties in one finding) split into F3 and F4, as two
  different problems with different conditions; F3 combined with broad/F2, money/F2, logistics/F1,
  F4 with parties/F4.
- broad/F3, parties/F2, context/F4 → F5: combined; context had made it for the payer only, mentioning
  the payee in passing.
- broad/F4, parties/F3, context/F5 → F6: combined.

## Outside this review
- The freight invoice `FRC-INV-26-0311` (`06-Invoice.xml`) is not remitted in the flow; whether its
  payment belongs in the flow is a question of the flow's composition (from broad, logistics).
