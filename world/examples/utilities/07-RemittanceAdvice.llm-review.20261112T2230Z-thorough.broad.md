# LLM review: 07-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/07-RemittanceAdvice.xml`, Git blob `ff1d21cc9e8ef3dfbfbdbfde835f54314d67116b` (committed)
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

### utilities/07#F1 · High · Document ID belongs to another sender and is used by two other remittance advices
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `14-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- Why: The document ID is "An identifier for this document, assigned by the sender." The sender here is Brightmarket Stores, whose own references all carry the prefix BS (`/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`, `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BS-BANK-26-04`, `/RemittanceAdvice/cac:Signature/cbc:ID` = `BS-SIG-RA`). The prefix VI is Valdara Industries', and exactly this ID is the ID of Valdara's remittance advice 04-RemittanceAdvice.xml for Ferrano's invoice, and of Velumi Trading's 14-RemittanceAdvice.xml, all in the same profile execution UTILITIES-2026-01. Three different documents of three senders cannot be told apart by their ID.
- Condition: The document ID is Brightmarket's own and unique within the flow.
- Options: (a, preferred) a Brightmarket number with prefix BS (e.g. BS-RM-26-…) and its own sequence number.
- Needs decision: no

### utilities/07#F2 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" from ISO 639 is the language, not a locale. 213 examples carry the same pattern (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: LocaleCode is a locale or absent.
- Options: (a, preferred) leave it out; (b) a real locale.
- Needs decision: no

### utilities/07#F3 · Low · Payment order references numbered after another party's invoice, and two references for one order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `BS-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `BS-PAY-26-0313`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank", PayerReference "An internal reference to the payer's order for payment": the same thing, given two different values. Both end in 0313, the number of Ferrano Energy's invoice FE-INV-26-0313 paid by Valdara in 04-RemittanceAdvice.xml (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`), not of the invoice paid here (CSWC-INV-26-0317). The values look derived from the other remittance advice rather than from Brightmarket's own payment order.
- Condition: The payer's payment-order reference is Brightmarket's own, given once (or the two elements carry two distinct, explained references).
- Options: (a, preferred) one Brightmarket payment-order number in PaymentOrderReference and InstructionID; drop PayerReference.
- Needs decision: no

### utilities/07#F4 · Low · Signature without method or reason
- XPath: `/RemittanceAdvice/cac:Signature/cbc:ID` = `BS-SIG-RA`
- Why: Signature is "A signature applied to this document". It has only an ID and the signatory; nothing says how or why the remittance advice is signed (rule "no fillers, nothing implied by absence").
- Condition: A signature is present only with a reason and the data that make it one, or absent.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/07#F5 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BS-BANK-26-04`
- Why: The reference does not say what BS-BANK-26-04 is (bank statement, payment batch?), and it is not an example of the flow.
- Condition: The reference states its document type, or is absent.
- Options: (a, preferred) add DocumentTypeCode or DocumentDescription.
- Needs decision: no

### utilities/07#F6 · Low · Payment purpose differs from the purpose the invoice gave
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:PaymentPurposeCode` = `WTER`
- Why: The invoice asks for the purpose WaterBill on both lines; the remittance advice reports the generic SupplierPayment without explanation.
- Condition: The purpose agrees with the invoice, or the difference is explained.
- Options: (a, preferred) WTER.
- Needs decision: no

### utilities/07#F7 · Low · The invoice is referenced twice in the line, and payer master data the advice does not use
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- Why: The line's BillingReference already identifies the invoice; the DocumentReference repeats it. Logo, online shop and social media profile have nothing to do with a payment; the payer's contact for a remittance advice is accounts payable, not the buying office.
- Condition: Each reference and party detail serves the remittance advice; the payer's contact handles payments.
- Options: (a, preferred) drop the DocumentReference and the master data; give an accounts-payable contact.
- Needs decision: no

## Checked and consistent
- Amounts: invoice payable 238.22 (`06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `238.22`) = debit = payment; no credit; balance 0.00.
- Timing: issued 2026-04-19, before the due date 2026-04-23, so no penalty applies.
- References: CSWC-INV-26-0317 of 2026-04-02 is 06-Invoice.xml; PaymentID and InvoicingPartyReference RF03CSWCINV260317 are the invoice's creditor reference; payee account is the invoice's PayeeFinancialAccount.
- check_ids.py: RF references, both IBAN-like accounts and the GLN correct.
