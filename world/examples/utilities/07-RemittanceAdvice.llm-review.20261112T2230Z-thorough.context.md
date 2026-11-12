# LLM review: 07-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

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

### utilities/07#F1 · High · Document ID of another payer's remittance advice
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `14-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: ID is "An identifier for this document, assigned by the sender." This advice is sent by Brightmarket Stores, whose other references use the prefix BS (BS-PAY-…, BS-BANK-…, BS-SIG-RA). VI-RM-26-0316 carries Valdara Industries' prefix and is the ID of Valdara's advice `04-RemittanceAdvice.xml` (and again of `14-RemittanceAdvice.xml`). Three different remittance advices of the same flow share one document ID, and a reference to VI-RM-26-0316 cannot be resolved to one of them.
- Condition: The advice has an ID of Brightmarket's own numbering, unique in the flow.
- Options: (a, preferred) a BS-RM-… number.
- Needs decision: no

### utilities/07#F2 · Low · Payment order and payer references numbered after Valdara's invoice
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `BS-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `BS-PAY-26-0313`
- Why: In `04-RemittanceAdvice.xml` the suffix 0313 follows the paid invoice FE-INV-26-0313. Here Brightmarket pays CSWC-INV-26-0317, but its references carry the same 0313, which looks taken over from Valdara's advice rather than from Brightmarket's own numbering or the paid invoice.
- Condition: The payer's references follow Brightmarket's own numbering (or the paid invoice), not another payer's.
- Options: (a, preferred) BS-PAY-26-0317 / BS-0317 or a Brightmarket sequence.
- Needs decision: no

### utilities/07#F3 · Medium · A language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" (ISO 639) is a language code. World-wide pattern (362 elements in 213 examples, grep over `*.xml`).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a, preferred) remove; (b) a locale code from a locale list.
- Needs decision: no

### utilities/07#F4 · Low · Payment purpose "supplier payment" where the invoice names a water bill
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:PaymentPurposeCode` = `WTER`
- Why: The invoice gives the ISO 20022 purpose WTER (WaterBill); the payer reports the generic SUPP.
- Condition: The purpose code agrees with the invoice's, or is absent.
- Options: (a, preferred) WTER.
- Needs decision: no

### utilities/07#F5 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BS-BANK-26-04`
- Why: No type or description says what BS-BANK-26-04 is, and no example carries it.
- Condition: The reference says what it is, or is removed.
- Options: (a, preferred) add DocumentTypeCode / DocumentDescription.
- Needs decision: no

### utilities/07#F6 · Low · The line references the same invoice twice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- Why: The generic DocumentReference repeats the billing reference to the same invoice.
- Condition: One reference per document per line.
- Options: (a, preferred) keep BillingReference only.
- Needs decision: no

### utilities/07#F7 · Low · Payer master data the remittance does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:ID` = `10442197`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- Why: Logo and social media profile have no role in a payment advice; the buying office is not the contact for payments.
- Condition: The payer carries what the advice uses.
- Options: (a, preferred) remove; accounts payable contact.
- Needs decision: no

## Checked and consistent
- References CSWC-INV-26-0317 resolve to `06-Invoice.xml` (issue date agrees); 238.22 paid in full, balance 0.00, on 2026-04-19 before the due date 2026-04-23.
- PaymentID / InvoicingPartyReference RF03CSWCINV260317 and the payee account equal the invoice's.

## Considered and refuted
- `/RemittanceAdvice/cbc:TotalCreditAmount`: 0.00 stated — refuted because a total of credits of zero is a real statement of a debit-only advice, not an implied value.
