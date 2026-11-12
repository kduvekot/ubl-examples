# LLM review: 04-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/04-RemittanceAdvice.xml`, Git blob `ed53a13de1ca0b9a4d9a62d8bc6c094c15743208` (committed)
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


### utilities/04#F1 · Medium · Province in Region
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division of the country (CountrySubentity). The Bayvarran addresses of the world use CountrySubentity. 219 occurrences in 104 files (recount over `*.xml`).
- Condition: Urvanian provinces are in CountrySubentity (with a code where the world has a list).
- Options: (a, preferred) CountrySubentity; (b) Region only if the story makes the province an economic or geographic region.
- Needs decision: no
- From: broad (F1), parties (F1)

### utilities/04#F2 · Low · Tax total: only the invoice's VAT, without scheme, unadjusted for the discount taken
- XPath: `/RemittanceAdvice/cac:TaxTotal/cbc:TaxAmount` = `2516028`
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `301923`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:Note` = `2 % discount taken: paid within the discount period of the invoice's terms.`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cbc:TaxAmount` = `2516028`
- Why: TaxTotal carries no subtotal or scheme, so the reader has to infer that 2516028 is the VAT of invoice 02; the invoice's other tax, the excise of 288840, is not mentioned. The 2 % discount of 301923 is taken on the gross amount; recalculated by the merge it contains 2 % of the VAT (50320.56) and of the excise (5776.80). Whether the remittance should state the invoice's tax or the tax in the amount paid depends on the world's rule for settlement discounts (in EU VAT the taxable amount is reduced when the discount is taken; own knowledge, money). Nothing in the advice uses the figure.
- Condition: The remittance carries no TaxTotal, or one per scheme with TaxSubtotal and TaxScheme, whose amount follows the world's stated rule for discounts taken.
- Options: (a, preferred) leave TaxTotal out: a remittance advice of one invoice needs no tax figure; (b) VAT and excise totals with their schemes, adjusted for the discount if the world's VAT law reduces the base.
- Needs decision: yes
- From: broad (F2), money (F1), context (F1, no)

### utilities/04#F3 · Low · Payment purpose "supplier payment" where the invoice names electricity and gas bills
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `ELEC`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:PaymentPurposeCode` = `GASB`
- Why: PaymentPurposeCode is "A code signifying the business purpose for this payment" (ISO 20022 ExternalPurpose1Code). The invoice gives its lines the specific purposes ElectricityBill and GasBill; the payer reports the generic SupplierPayment without saying why. The ISO list also has UBIL (utilities), which would cover both, but the world's subset does not contain it (money part, checked against `world/codelists/sources/iso20022/` and `world/codelists/gc/ISO20022PurposeCode.gc`). The same SUPP is used in 07 (water) and 14 (telephone).
- Condition: The remittance line's purpose code agrees with the purposes of the invoice it pays, or the difference is stated.
- Options: (a, preferred) ELEC, the larger part of the payment (or one line per purpose, or UBIL added to the world's subset); (b) keep SUPP with a note that one code covers a mixed bill; (c) leave the code out.
- Needs decision: no
- From: broad (F6), money (F2), context (F2)

### utilities/04#F4 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VI-BANK-26-04`
- Why: The reference has no type code, description or issuer, so Ferrano Energy cannot tell what VI-BANK-26-04 is (a bank statement, a payment batch?); no example carries it. The payment order itself is already referenced (PaymentOrderReference and InstructionID). A reference with only an ID says what it refers to where that is not obvious. Same pattern in 07 (BS-BANK-26-04) and 14 (VT-BANK-26-04).
- Condition: The reference states what kind of document it is (DocumentTypeCode and/or DocumentDescription), or is absent.
- Options: (a, preferred) add type and description saying why the payee needs it; (b) remove it.
- Needs decision: no
- From: broad (F5), logistics (F1), context (F3)

### utilities/04#F5 · Low · The line references the same invoice twice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0313`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `FE-INV-26-0313`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:DocumentTypeCode` = `Invoice`
- Why: The line's BillingReference already identifies the invoice ("A reference to a billing document"); the generic DocumentReference repeats it with type "Invoice" and adds nothing (no filler). The logistics part refuted it within its lens (both resolve to the same invoice and agree); that they agree is not in question, only that the second adds nothing.
- Condition: Each referenced document appears once per line, in the most specific element.
- Options: (a, preferred) keep BillingReference only.
- Needs decision: no
- From: broad (F7, part), context (F4)

### utilities/04#F6 · Low · Payer's master data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: A remittance advice tells the supplier which invoice a payment settles. Valdara's customs trader number, share listing and warehousing service provider play no part in it; the block is identical in all 75 examples with Valdara's full data (parties part). Copied master data (section 4.8).
- Condition: Every identifier, listing and service provider in the payer's party has a use in this advice, or is absent.
- Options: (a, preferred) drop them; (b) keep them only with a stated reason.
- Needs decision: no
- From: broad (F7, part), parties (F2), context (F5, part)

### utilities/04#F7 · Low · Payer's contact is its sales order desk, not someone who answers for the payment
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The supplier would turn to Valdara's accounts payable or treasury with questions about the payment and the discount taken; the contact given is Valdara's sales order desk, the same in all its examples.
- Condition: The payer's contact deals with payments, and name, job title and department agree.
- Options: (a, preferred) an accounts payable contact; (b) drop the contact.
- Needs decision: no
- From: broad (F7, part), parties (F3), context (F5, part)

### utilities/04#F8 · Low · Two different references for the payer's payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VI-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VI-PAY-26-0313`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank", PayerReference "An internal reference to the payer's order for payment". Both definitions denote the payer's payment order, which is VI-PAY-26-0313 (also the InstructionID), and the second carries another value without explanation (broad). Against it (logistics, which refuted it): PayerReference may be the payer's own internal reference, e.g. a payables voucher, distinct from the order to its bank. The definitions do not settle it, so the merge keeps it Low with Needs decision: yes.
- Condition: Each reference has a distinct, stated meaning in this payment, or only one is given.
- Options: (a, preferred) drop PayerReference; (b) give it a distinct reference (e.g. the payables voucher) and say so.
- Needs decision: yes
- From: broad (F3, no); logistics refuted it

### utilities/04#F9 · Low · Signature without method or attachment
- XPath: `/RemittanceAdvice/cac:Signature/cbc:ID` = `VI-SIG-RA`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: Signature is "A signature applied to this document"; it carries only an ID and the signatory, with no SignatureMethod, DigitalSignatureAttachment or reason why the advice is signed (broad: no fillers, nothing implied by absence). The context part refuted it as a legitimate business element that nothing contradicts. Recounted by the merge: 137 of the 147 Signature aggregates in `world/examples/*/*.xml` hold only ID and SignatoryParty (lxml), so it is a world convention; aligned with the air merges (Low, Needs decision: yes).
- Condition: A signature is present only with the information that makes it one (method, attachment) and a reason, or is absent; or the convention is recorded.
- Options: (a, preferred) drop it; (b) describe the signature if remittance advices are signed in this world; (c) record the convention.
- Needs decision: yes
- From: broad (F4, no); context refuted it

### utilities/04#F10 · Low · Italian text tagged as English (street and legal form)
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Added by the merge for alignment with utilities/01#F16 and the wood, plastics and rail merges: en-XU renderings in Italian; proper names may keep their form, the legal form is a description, and no convention is recorded. Cannot be settled.
- Condition: Either the convention is recorded in the world's story, or the en-XU renderings are English.
- Options: (a, preferred) record the convention for proper names, render legal forms in English; (b) English renderings throughout.
- Needs decision: yes
- From: merge

## Checked and consistent
- Amounts (redone by the merge): invoice payable 15096168 (`02-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `15096168`) − discount 301923 (2 % = 301923.36, the invoice's SettlementDiscountAmount) = 14794245 = TotalPaymentAmount; line debit 15096168, credit 301923, balance 0; LineCountNumeric 1.
- Timing: issued 2026-04-10, within the settlement period 2026-04-02 to 2026-04-12, so the discount could be taken; and before the due date 2026-04-23 (and 2026-05-02 under the note's 30 days).
- References: FE-INV-26-0313 of 2026-04-02 is `02-Invoice.xml`; invoice period March 2026 agrees; PaymentID and InvoicingPartyReference RF58FEINV260313 are the invoice's PaymentID; payee account XU080351041600000004084431 is the invoice's PayeeFinancialAccount; payment means 30 as requested.
- Payer account XU790351041600000000209458, named Valdara Industries SUA, is Valdara's account in other flows; both accounts at Crevalto Bank's Ferrano main branch 03510-41600, matching the account digits.
- check_ids.py: RF reference, both IBAN-like accounts and the ISIN have correct check digits.
- Signatory and line parties are Valdara and Ferrano Energy, the invoice's accounting parties, described as in 01–03.

## Considered and refuted
- `/RemittanceAdvice/cbc:PaymentOrderReference`: equals PaymentMeans/InstructionID — refuted, the payment order and the instruction are the same object seen from two sides; the number 0313 follows the invoice number (from money, context).
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name`: account holder name — matches the legal entity's RegistrationName (from parties).
- `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name`: supplier's customer service as contact — a usual addressee for the supplier side of a payment notice (from parties, "Checked").
- `/RemittanceAdvice/cbc:PayerReference`: second reference for the same payment order — refuted by logistics (possibly the payer's own voucher). The merge cannot settle it: kept as F8, Low, yes (from logistics).
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID`: invoice referenced twice — refuted by logistics within its lens (both resolve and agree); the presence question is F5 (from logistics).
- `/RemittanceAdvice/cac:Signature`: signature with only ID and party — refuted by context (legitimate, nothing contradicts it). The merge keeps F9 for alignment with the air merges (from context).

## Changed in the merge
- broad/F7 → F5, F6, F7: split into the duplicate reference, the master data and the contact, as context and parties had them.
- context/F1 (no) → F2, Needs decision: yes: the answer depends on the world's VAT rule for discounts (broad, money).
- broad/F3 (no) → F8, Needs decision: yes: logistics' reading is defensible; cannot be settled.
- broad/F4 (no) → F9, Needs decision: yes: aligned with the air merges (convention across 137 of 147 signatures).
- F10 added for alignment.

## Outside this review
- The same document ID VI-RM-26-0316 is used by `07-RemittanceAdvice.xml` (sent by Brightmarket Stores) and `14-RemittanceAdvice.xml` (sent by Velumi Trading); the prefix VI fits only this example (Valdara Industries), so the problem lies in those two examples (broad, context; utilities/07#F1).
- The logistics part noted that VI-RM-26-0316 "follows the flow's sequence" after Ferrano Energy's 0313–0315; the numbers 0313–0324 run across senders throughout the flow, which looks like one generator sequence rather than each sender's own numbering. Not a contradiction within this example.
