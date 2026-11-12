# LLM review: 14-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/14-RemittanceAdvice.xml`, Git blob `13ca288b96ca5f33f56aefe8db004930ea15062a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1b44438 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/14#F1 · High · Document ID of Valdara Industries' remittance advice reused by Velumi Trading
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `07-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: the ID is "An identifier for this document, assigned by the sender". This remittance advice is sent by Velumi Trading, but its ID is that of Valdara Industries' remittance advice 04 ("VI" prefix, sequence 0316 of the Ferrano documents), also reused in 07 (Brightmarket Stores). Three documents of the same collaboration (UTILITIES-2026-01) share one ID, so a reference to it is ambiguous, and the prefix names another party. Velumi's other identifiers here use its own prefix (VT-PAY-…, VT-SIG-RA, VT-BANK-26-04).
- Condition: the document ID is unique in the flow and is one Velumi Trading assigns.
- Options: a Velumi number (e.g. VT-RM-26-…, sequence after 0323–0324); same fix in 07.
- Needs decision: no

### utilities/14#F2 · Low · Payment order references carry another invoice's number
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VT-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `ST-INV-26-0323`
- Why: the payer's references end in 0313, the number of Ferrano Energy's invoice to Valdara (paid in 04 with VI-PAY-26-0313 / VI-0313), not of Selanu Telecom's invoice 0323 paid here; they look copied from 04 (same pattern in 07).
- Condition: the payer's references are Velumi's own and do not borrow an unrelated invoice's number.
- Options: give Velumi's payment order its own number.
- Needs decision: no

### utilities/14#F3 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VT-BANK-26-04`
- Why: no type, description or issuer says what VT-BANK-26-04 is or why the payee needs it; same pattern in 04 and 07.
- Condition: the reference says what kind of document it is, or is absent.
- Options: add a type code or description (preferred), or remove it.
- Needs decision: no

## Checked and consistent
- BillingReference and line DocumentReference ST-INV-26-0323 (2026-04-02) resolve to 13-Invoice.xml, an invoice; amount 135.566 = its PayableAmount; balance 0.000.
- Payment reference RF26STINV260323 = the invoice's PaymentID; payee account XL18BSEL0010004293889 (with BlockchainID CORAL-NET-L1) = the invoice's payee account; payer account XL40BSEL0010003665515; check digits OK.
- Issued 2026-04-19, before the stated due date 2026-04-23 (and before 2026-05-17, the date "45 days net" would give, see utilities/13#F1).
