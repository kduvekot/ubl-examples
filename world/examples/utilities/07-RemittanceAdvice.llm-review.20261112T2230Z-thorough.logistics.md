# LLM review: 07-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/07#F1 · High · Document ID of Valdara Industries' remittance advice reused by Brightmarket Stores
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `14-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: the ID is "An identifier for this document, assigned by the sender". This remittance advice is sent by Brightmarket Stores (its signatory and AccountingCustomerParty), but carries the ID of Valdara Industries' remittance advice 04 ("VI" prefix, sequence number 0316, which follows Ferrano Energy's documents 0313–0315), and the same ID appears a third time in 14 (Velumi Trading). Three different documents of the same collaboration (ProfileExecutionID UTILITIES-2026-01) share one ID, so a reference to VI-RM-26-0316 cannot be resolved, and the prefix names the wrong party. The other identifiers of this document use Brightmarket's own prefix (BS-PAY-…, BS-SIG-RA, BS-BANK-26-04).
- Condition: the document ID is unique in the flow and is one Brightmarket Stores assigns (consistent with its other references).
- Options: give the document a Brightmarket number (e.g. BS-RM-26-…, with a sequence that fits the flow, after 0317–0320); same fix in 14.
- Needs decision: no

### utilities/07#F2 · Low · Payment order references carry another invoice's number
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `BS-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0317`
- Why: the payer's payment order and internal reference end in 0313, the number of Ferrano Energy's invoice to Valdara (FE-INV-26-0313, paid in 04 with VI-PAY-26-0313 and VI-0313). This payment settles Coastal State Water's invoice 0317. Brightmarket's own order numbering would not follow another company's invoice number; the values look copied from 04. (14 has the same pattern with VT-PAY-26-0313.)
- Condition: the payer's references are Brightmarket's own and do not borrow the number of an unrelated invoice.
- Options: give Brightmarket's payment order its own number (e.g. derived from this invoice or from Brightmarket's sequence).
- Needs decision: no

### utilities/07#F3 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BS-BANK-26-04`
- Why: no type, description or issuer says what BS-BANK-26-04 is or why the payee needs it; the payment order is already referenced. Same pattern as 04 (VI-BANK-26-04) and 14.
- Condition: the reference says what kind of document it is, or is absent.
- Options: add a type code or description (preferred), or remove it.
- Needs decision: no

## Checked and consistent
- BillingReference and line DocumentReference CSWC-INV-26-0317 (2026-04-02) resolve to 06-Invoice.xml, an invoice.
- Amount 238.22 = invoice PayableAmount; no discount in the invoice's terms, so TotalCreditAmount 0.00 is consistent; balance 0.00.
- Payment reference RF03CSWCINV260317 = the invoice's PaymentID; payee account XB21BLUM38010004189160 = the invoice's PayeeFinancialAccount; check digits OK (check_ids.py).
- Issued 2026-04-19, before the invoice's due date 2026-04-23, so no penalty applies.
