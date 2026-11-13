# LLM review: 26-CreditNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/26-CreditNote.xml`, Git blob `27ef7cc12dad5d613bda5ae257e7fc61371126be` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2d5178e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/26#F1 · Medium · Gate number in AdditionalStreetName of the supplier's postal address
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/26#F2 · Low · Credit on an assigned receivable without the factor
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `22-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `22-Invoice.xml:/Invoice/cac:PaymentMeans/cac:TradeFinancing/cac:Clause/cbc:Content` = `Payment to any other account does not discharge the buyer.`
- Why: The credited invoice `LD-INV-26-0147` was assigned to Harbourline Factoring, and the buyer pays only to the factor. The credit note says the credit is "settled against the next payment to the seller", but the next payment for this invoice goes to the factor (`27-RemittanceAdvice.xml` deducts the 64.00 from the payment to Harbourline). The credit note does not mention the assignment or the factor, so the buyer's set-off against the factored payment is not covered by the credit note's own terms.
- Condition: The credit note's settlement terms agree with how it is settled in the flow (deducted from the payment to the factor, with the factor named or the assignment referenced).
- Options: name the factor in the settlement note (e.g. "deducted from the payment of LD-INV-26-0147 to Harbourline Factoring") and reference the assignment; or settle by refund from Lumeway. Preferred: the first, as the remittance advice does.
- Needs decision: no

### sea/26#F3 · Low · Contract reference points to the digital agreement, credit line not linked to the invoice line
- XPath: `/CreditNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:ID` = `1`
- Why: `LD-DAG-26-0125` is `03-DigitalAgreement.xml`, the agreement on electronic exchange between the parties, not the sales contract under which the goodwill credit is given (the sales terms are `LD-GTC-2026`). The credit note line credits one casting but does not point to invoice line 2 or receipt line 2, which it corrects.
- Condition: The contract reference is to the contract the credit is given under, and the credit line references the invoice line it credits.
- Options: reference the general terms (or drop the contract reference); add a line-level billing reference to `LD-INV-26-0147` line 2.
- Needs decision: no

### sea/26#F4 · Low · Contacts do not fit the billing roles
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting parties' contacts are Lumeway's customer service in Sales and Velumi's "Purchasing" in Sales; a credit note's contacts are receivables/claims and payables. The buyer routes the document to `VT-CLAIMS` (its buyer-assigned reference), which its contact does not reflect; name and department also contradict each other.
- Condition: The contacts handle the credit note, and each contact's name and department agree.
- Options: Lumeway receivables/claims, Velumi claims or accounts payable.
- Needs decision: no

## Checked and consistent
- 1 × 64.00 = 64.00 = line extension = tax exclusive = inclusive = payable; tax 0 at G/EXP like the invoice; price 64 = invoice line 2's price (`22-Invoice.xml`).
- References resolve: invoice `LD-INV-26-0147` (issued 2026-05-14), order `VT-PO-26-0127`, receipt advice `NW-RA-26-0146` (one casting rejected, credit requested), statement `HF-ST-26-0151` (issued 06-13, before this credit note), digital agreement `LD-DAG-26-0125`.
- Actual delivery 2026-05-21 = receipt date in `21-ReceiptAdvice.xml`; discrepancy code 17 "Transport damage" and the line note agree with the receipt advice.
- The note's statement that the risk was the buyer's under CIF agrees with `14-BillOfLading.xml`; the insurer claim under policy `WS-CP-26-4471` agrees with the B/L's policy.
- The 64.00 is deducted in `27-RemittanceAdvice.xml` (credit line `LD-CN-26-0152`, 43 778 − 64 = 43 714).
- GTIN and GLN pass `check_ids.py`.

## Considered and refuted
- `/CreditNote/cbc:Note` = `Under CIF the risk was the buyer's on board; the distributor credits the frame as a goodwill gesture and claims from the insurer.`: the seller claiming from an insurance taken out for the buyer's benefit — refuted: under CIF the seller takes out the policy; having compensated the buyer, it can claim under it.
- `/CreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `0.4`: an alternative currency rate without an alternative amount — refuted as a finding: the rate tells the Lisavan buyer the XLC equivalent at the invoice's rate; no contradiction.
