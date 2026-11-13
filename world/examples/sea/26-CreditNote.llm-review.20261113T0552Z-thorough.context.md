# LLM review: 26-CreditNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/26-CreditNote.xml`, Git blob `27ef7cc12dad5d613bda5ae257e7fc61371126be` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/26#F1 · Low · "Settled against the next payment to the seller", but the credit is deducted from this invoice's payment to the factor
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: The receivable the credit reduces (`LD-INV-26-0147`) was assigned to Harbourline Factoring; the invoice instructs that only payment to the factor's account discharges the buyer. The credit is in fact set off against that same invoice in Velumi's payment to the factor: `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00` (43778.00 − 64.00). The note speaks of "the next payment to the seller", which is neither the party paid nor (for this invoice) a later payment. The free text does not describe what the flow does.
- Condition: The credit note's settlement text describes the settlement the flow carries out (set off against the payment of `LD-INV-26-0147` to the factor), or is absent.
- Options: (a) preferred: say that the credit is deducted from the payment of the invoice to Harbourline Factoring; (b) remove the note and rely on the billing reference.
- Needs decision: no

### sea/26#F2 · Low · The electronic-trading agreement cited as the contract of a goodwill credit
- XPath: `/CreditNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`
- Why: `ContractDocumentReference` is "A reference to a contract associated with this document". `LD-DAG-26-0125` is the Digital Agreement between Lumeway and Velumi (`03-DigitalAgreement.xml`), the agreement on exchanging electronic documents under the Trade Accord's certified procedures. The credit is, by the credit note's own note, a goodwill gesture outside the sale's terms (risk under CIF passed to the buyer on board); the agreement on electronic exchange is not the contract under which the credit is granted. The reference is valid but does not have a reason in this document.
- Condition: The contract reference names the contract that governs the credit (the sale, or a goodwill or claims agreement), or is absent.
- Options: (a) preferred: remove it, since the credit is goodwill; (b) reference the sale's general terms (`LD-GTC-2026`) if a clause there covers transport damage.
- Needs decision: no

### sea/26#F3 · Low · A buyer project that appears nowhere before the claim
- XPath: `/CreditNote/cac:ProjectReference/cbc:ID` = `VT-PRJ-26-07`
- Why: `ProjectReference` is "A reference to a project associated with this document". The project `VT-PRJ-26-07` occurs only in this credit note and in `28-DebitNote.xml` (counted with `grep -l VT-PRJ-26-07 world/examples/*/*.xml`); neither the order nor the invoice it credits refers to a project. If the purchase belonged to a project of Velumi, the order would carry it; as it stands, the project has no reason in the flow.
- Condition: The project reference occurs from the order onwards, or not at all.
- Options: (a) preferred: remove it here; (b) add it to the order and invoice if the world wants the purchase tied to a Velumi project (e.g. the Port of Selanu's benches).
- Needs decision: no

## Checked and consistent
- Amount: 1 side frame × 64.00 = 64.00, the invoice's unit price (768.00 / 12 in `22-Invoice.xml`); tax category and exemption as on the invoice.
- References: the invoice `LD-INV-26-0147` (with its issue date), the receipt advice `NW-RA-26-0146` that reports the cracked frame, the statement `HF-ST-26-0151` and the order exist and precede the credit note.
- The discrepancy code 17 "Transport damage" and the line note agree with the receipt advice ("One box crushed at the port").
- The note on CIF risk agrees with the bill of lading's delivery terms (risk passes on board in Lumeport), and the insurer claim agrees with the insurance policy `WS-CP-26-4471` on the goods in `19-ImportCustomsDeclaration.xml`.

## Considered and refuted
- `/CreditNote/cac:StatementDocumentReference/cbc:ID`: a reference to the factor's statement suspected as without reason — refuted because the credit reduces the balance that statement reported, and pointing the factor and the buyer to it is a real use.
- `/CreditNote/cbc:PaymentAlternativeCurrencyCode`: an alternative payment currency on a credit note suspected as a filler — refuted because the invoice it corrects offers payment in Coral at the same rate, so stating the credit's equivalent for a buyer paying in Coral has a reason.
