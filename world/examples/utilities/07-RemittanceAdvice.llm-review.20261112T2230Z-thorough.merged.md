# LLM review: 07-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/07-RemittanceAdvice.xml`, Git blob `ff1d21cc9e8ef3dfbfbdbfde835f54314d67116b` (committed)
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


### utilities/07#F1 · High · Document ID of another payer's remittance advice, shared by three advices of the flow
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `14-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BS-BANK-26-04`
- Why: ID is "An identifier for this document, assigned by the sender." The sender is Brightmarket Stores (signatory and AccountingCustomerParty), whose own references carry the prefix BS (BS-PAY-…, BS-BANK-26-04, BS-SIG-RA). VI-RM-26-0316 carries Valdara Industries' prefix and is the ID of Valdara's advice 04; Velumi Trading's advice 14 has it a third time (verified by the merge: `grep -rl --include='*.xml' '<cbc:ID>VI-RM-26-0316'` finds exactly 04, 07 and 14), all in the same profile execution UTILITIES-2026-01. A reference to VI-RM-26-0316 cannot be resolved to one of them, and the prefix names the wrong party. Refutation attempted: a payer may number freely, but not with another company's prefix and the very number of another document of the same collaboration. Money and parties rated it Medium (grouped with the references of F3); broad, logistics and context High; the merge keeps High (a document of this example and another example of the flow carry one identity; section 6).
- Condition: The document ID is one Brightmarket Stores assigns (consistent with its other references) and unique in the flow.
- Options: (a, preferred) a Brightmarket number (e.g. BS-RM-26-…, with a sequence that fits the flow); the same fix in 14.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1), money (F1, part, Medium), parties (F1, part, Medium)

### utilities/07#F2 · Medium · A language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language, repeating Language/ID. Recounted: 364 occurrences in 213 files (parts: 362).
- Condition: LocaleCode holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) remove; (b) a locale such as en-XB with a fitting list.
- Needs decision: no
- From: broad (F2), parties (F2), context (F3)

### utilities/07#F3 · Low · Payment order references numbered after another payer's invoice, and two references for one order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `BS-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank". Brightmarket's payment-order references end in 0313, the number of Ferrano Energy's invoice FE-INV-26-0313 that Valdara pays in 04 (VI-PAY-26-0313, VI-0313), while this advice pays CSWC-INV-26-0317; they look copied from 04 with the prefix changed (14 has VT-PAY-26-0313 too). In addition PayerReference ("An internal reference to the payer's order for payment") gives a second value for what looks like the same order (broad); whether it may be a distinct internal voucher is open (utilities/04#F8). No amount depends on these references, hence Low.
- Condition: The payer's references are Brightmarket's own (its sequence, or derived from the paid invoice), do not echo another payer's invoice number, and the two elements carry one reference or two distinct, explained ones.
- Options: (a, preferred) one Brightmarket payment-order number (e.g. BS-PAY-26-0317) in PaymentOrderReference and InstructionID, PayerReference dropped; (b) a distinct, explained PayerReference.
- Needs decision: no
- From: broad (F3), logistics (F2), context (F2), money (F1, part), parties (F1, part)

### utilities/07#F4 · Low · Payment purpose "supplier payment" where the invoice names a water bill
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:PaymentPurposeCode` = `WTER`
- Why: PaymentPurposeCode is "A code signifying the business purpose for this payment" (ISO 20022 ExternalPurpose1Code). Invoice 06 gives both lines WTER (WaterBill); the payer reports the generic SUPP (SupplierPayment) without explanation. Same in 04 and 14.
- Condition: The purpose code agrees with the invoice's, or the difference is stated.
- Options: (a, preferred) WTER; (b) leave the code out.
- Needs decision: no
- From: broad (F6), money (F2), context (F4)

### utilities/07#F5 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BS-BANK-26-04`
- Why: No type, description or issuer says what BS-BANK-26-04 is (bank statement, payment batch?) or why the payee needs it; no example carries it, and the payment order is already referenced. Same pattern as 04 and 14.
- Condition: The reference says what kind of document it is, or is absent.
- Options: (a, preferred) add DocumentTypeCode / DocumentDescription; (b) remove it.
- Needs decision: no
- From: broad (F5), logistics (F3), context (F5)

### utilities/07#F6 · Low · The line references the same invoice twice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- Why: The generic DocumentReference repeats the line's BillingReference to the same invoice and adds nothing (no filler). Same as utilities/04#F5.
- Condition: One reference per document per line, in the most specific element.
- Options: (a, preferred) keep BillingReference only.
- Needs decision: no
- From: broad (F7, part), context (F6)

### utilities/07#F7 · Low · Payer's marketing data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Logo, online shop and social media profile play no part in telling the water company which invoice a payment settles; they are part of the block repeated in all 41 examples with Brightmarket's full data. Copied master data.
- Condition: They appear only with a use in this advice.
- Options: (a, preferred) drop them; (b) keep them only with a stated reason.
- Needs decision: no
- From: broad (F7, part), parties (F3), context (F7, part)

### utilities/07#F8 · Low · Payer's contact: buying office with a sales job title and department
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name and job title/department contradict each other, and the payer's contact on a remittance advice answers for the payment (accounts payable, treasury), not the buying office or sales.
- Condition: Name, job title and department agree, and the function deals with payments.
- Options: (a, preferred) an accounts payable contact; (b) drop title and department.
- Needs decision: no
- From: broad (F7, part), parties (F4), context (F7, part)

### utilities/07#F9 · Low · The water company described as a small enterprise registered on the world's default date
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: As utilities/05#F8: a water utility serving a state's capital is not plausibly small (parties; broad refuted the size in 05), and 1996-01-01 is shared by 25 companies (271 occurrences in 181 files, recount).
- Condition: Size and registration date are values of the company's own story, the same in every example, or absent.
- Options: (a, preferred) a fitting size and a date of its own; (b) drop them where unused; (c) record a 1996 event in the story.
- Needs decision: yes
- From: parties (F5)

### utilities/07#F10 · Low · Signature without method or reason
- XPath: `/RemittanceAdvice/cac:Signature/cbc:ID` = `BS-SIG-RA`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: Signature is "A signature applied to this document"; only an ID and the signatory are given, nothing says how or why the advice is signed (no fillers, nothing implied by absence). 137 of the 147 Signature aggregates over `world/examples/*/*.xml` hold only ID and SignatoryParty (lxml, recount), so it is a world convention; aligned with the air merges and utilities/04#F9 (Low, Needs decision: yes; in 04 the context part refuted it as a legitimate element).
- Condition: A signature is present only with the data that make it one and a reason, or absent; or the convention is recorded.
- Options: (a, preferred) leave it out; (b) describe the signature; (c) record the convention.
- Needs decision: yes
- From: broad (F4, no)

## Checked and consistent
- Amounts: debit 238.22 = invoice 06's PayableAmount (`06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `238.22`), including the city's sewage levy of 36.12; no discount in the invoice's terms, so TotalCreditAmount 0.00; payment 238.22; balance 0.00.
- Timing: issued 2026-04-19, before the due date 2026-04-23 (and 2026-05-02 under the note's 30 days), so no penalty applies and none is taken.
- References: CSWC-INV-26-0317 of 2026-04-02 is `06-Invoice.xml`; PaymentID and InvoicingPartyReference RF03CSWCINV260317 are the invoice's PaymentID; payee account XB21BLUM38010004189160 is the invoice's PayeeFinancialAccount.
- Payer account XB48BLUM38010001570935, named "Brightmarket Stores Corp", is Brightmarket's account in the furniture flow; both accounts at Bank of Lumeport branch 380100, as the digits say.
- Payer and payee are the invoice's accounting parties, described as in 05 and 06; the signatory is the issuer.
- check_ids.py: RF reference, both IBAN-like accounts and the GLN correct.

## Considered and refuted
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: a real GLN — refuted, GS1 prefix 952 is reserved for demonstrations and examples; check digit valid (from parties).
- `/RemittanceAdvice/cbc:TotalCreditAmount`: 0.00 stated — refuted, a total of credits of zero is a real statement of a debit-only advice, not an implied value (from context).

## Changed in the merge
- money/F1 and parties/F1 (Medium, ID and references together) → F1 High (ID) and F3 Low (references): split as broad, logistics and context had them; the ID clash with 04 and 14 is a contradiction between examples (section 6 High), the references only borrowed numbering.
- broad/F7 and context/F7 → F6, F7, F8: duplicate reference, marketing data and contact split.
- broad/F4 (no) → F10, Needs decision: yes: aligned with the air merges and 04.
- F2: count corrected to 364 occurrences in 213 files.
