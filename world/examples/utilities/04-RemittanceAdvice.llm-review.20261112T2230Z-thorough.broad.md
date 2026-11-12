# LLM review: 04-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/04-RemittanceAdvice.xml`, Git blob `ed53a13de1ca0b9a4d9a62d8bc6c094c15743208` (committed)
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

### utilities/04#F1 · Medium · Province in Region
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country (CountrySubentity). Same value in Region in 104 examples (`grep -l --include='*.xml' -r '<cbc:Region>Province of'`).
- Condition: Urvanian provinces are in CountrySubentity.
- Options: (a, preferred) CountrySubentity.
- Needs decision: no

### utilities/04#F2 · Low · Tax total without its tax and unchanged by the discount taken
- XPath: `/RemittanceAdvice/cac:TaxTotal/cbc:TaxAmount` = `2516028`
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `301923`
- Why: The invoice has two tax totals, excise (288840) and VAT (`02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cbc:TaxAmount` = `2516028`). The remittance advice gives one TaxTotal with the VAT amount but no subtotal, so it does not say which tax it is. The payer has taken a 2 % settlement discount on the gross amount (including VAT); depending on the world's VAT rules this reduces the VAT due (2 % of 2516028 ≈ 50321), which the tax total does not reflect, and nothing in the remittance advice uses the tax total.
- Condition: The tax total either names its tax scheme and states the tax actually settled by this payment, or is absent.
- Options: (a, preferred) leave the TaxTotal out, since the remittance advice settles the invoice and does not report tax; (b) give it a subtotal with VAT, and decide whether the discount reduces it.
- Needs decision: yes

### utilities/04#F3 · Low · Two different references for the payer's payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VI-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VI-PAY-26-0313`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank" and PayerReference "An internal reference to the payer's order for payment". Both denote the payer's payment order, which is VI-PAY-26-0313 (also the InstructionID). The second value VI-0313 is a different identifier for the same thing, without explanation.
- Condition: Each reference has a distinct meaning in this payment, or only one is given.
- Options: (a, preferred) drop PayerReference, or give it a distinct real reference (e.g. the payer's internal payables voucher, then say so).
- Needs decision: no

### utilities/04#F4 · Low · Signature with nothing signed or no method
- XPath: `/RemittanceAdvice/cac:Signature/cbc:ID` = `VI-SIG-RA`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: Signature is "A signature applied to this document". It carries only an ID and the signatory; there is no signature method, no digital signature attachment and no reason in the remittance advice why it is signed. As it stands it implies a signature without describing one (rule "no fillers, nothing implied by absence").
- Condition: A signature is present only with a business reason and the information that makes it one (method, validation or attachment), or is absent.
- Options: (a, preferred) leave it out; (b) describe the signature (SignatureMethod, DigitalSignatureAttachment) if remittance advices are signed in this world.
- Needs decision: no

### utilities/04#F5 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VI-BANK-26-04`
- Why: The reference does not say what VI-BANK-26-04 is (a bank statement, a payment file, a bank order?); the document is not an example of the flow (flow_index: `-> ?`). The skill's rule is that a reference with only an ID says what it refers to where that is not obvious.
- Condition: The reference states its document type (code or description), or is absent.
- Options: (a, preferred) add DocumentTypeCode or DocumentDescription (e.g. the payment batch sent to the bank).
- Needs decision: no

### utilities/04#F6 · Low · Payment purpose differs from the purposes the invoice gave
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `ELEC`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:PaymentPurposeCode` = `GASB`
- Why: The invoice asks for the payment purposes ElectricityBill and GasBill; the remittance advice reports the generic SupplierPayment. Both are valid ISO 20022 purpose codes, but the payer did not use the purpose the payee asked for, and nothing explains why.
- Condition: The remittance advice uses the purpose the invoice gave (ELEC for the bulk of the amount), or the difference is deliberate and stated.
- Options: (a, preferred) ELEC; (b) keep SUPP and note that one purpose code covers a mixed electricity-and-gas invoice.
- Needs decision: no

### utilities/04#F7 · Low · The invoice is referenced twice in the line, and payer master data the advice does not use
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `FE-INV-26-0313`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0313`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: The line's BillingReference already identifies the invoice ("A reference to a billing document"); the DocumentReference repeats it with a type code "Invoice" and adds nothing. The payer's customs trader number, its logistics service provider and its order desk (in Sales) have nothing to do with a payment; the payer's contact for a remittance advice is accounts payable.
- Condition: Each reference and party detail serves the remittance advice; the payer's contact is the one that handles payments.
- Options: (a, preferred) drop the DocumentReference and the master data, and give an accounts-payable contact.
- Needs decision: no

## Checked and consistent
- Amounts: invoice payable 15096168 (`02-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `15096168`) − discount 301923 (= 2 % of 15096168, the invoice's SettlementDiscountAmount) = 14794245 = TotalPaymentAmount; debit and credit totals equal the line amounts; balance 0.
- Timing: issued 2026-04-10, within the invoice's settlement period 2026-04-02 to 2026-04-12, so the discount could be taken.
- References: FE-INV-26-0313 of 2026-04-02 is 02-Invoice.xml; period March 2026 agrees; payment ID and InvoicingPartyReference RF58FEINV260313 are the invoice's creditor reference; payee account XU080351041600000004084431 is the invoice's PayeeFinancialAccount.
- check_ids.py: RF references, both IBAN-like accounts and the ISIN have correct check digits.
- LineCountNumeric 1 = number of lines.

## Outside this review
- The same document ID VI-RM-26-0316 is used by 07-RemittanceAdvice.xml (sent by Brightmarket Stores) and 14-RemittanceAdvice.xml (sent by Velumi Trading); the prefix VI fits only this example (Valdara Industries). The problem lies in those two examples.
