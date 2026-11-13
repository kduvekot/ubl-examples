# LLM review: 26-CreditNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### sea/26#F1 · Medium · Seller "claims from the insurer" a 64.00 loss under a policy with a 250.00 deductible whose beneficiary is the buyer
- XPath: `/CreditNote/cbc:Note` = `Under CIF the risk was the buyer's on board; the distributor credits the frame as a goodwill gesture and claims from the insurer.`
- XPath: `/CreditNote/cac:Annotation/cbc:AnnotationContent` = `Claimed from Wavesure Cargo Insurance under policy WS-CP-26-4471.`
- XPath: `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `64.00`
- Why: Policy WS-CP-26-4471 has a deductible and an excess of 250.00 XBL (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:DeductibleAmount` = `250.00`) and names Velumi Trading as beneficiary (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Velumi Trading`). The loss is one frame at 64.00 XBL (insured at 110 %: 70.40 XBL), well below the deductible, so a claim recovers nothing. And under CIF the insurance is for the buyer's benefit; the seller can claim only if the buyer assigns its rights, which the credit note does not say. The note and the annotation give a recovery route the policy data in the flow rule out.
- Condition: The way the loss is recovered, as stated in the credit note, is possible under the policy data of the flow (deductible, beneficiary), or the credit note does not state a recovery.
- Options: (a) preferred: drop the claim from the note and the annotation; the goodwill credit stands on its own (the loss is below the deductible); (b) keep a claim and make it possible (e.g. the buyer assigns its claim and the policy has no deductible for partial loss), which changes the policy data in the bill of lading; (c) the buyer claims, and the seller does not credit.
- Needs decision: yes

### sea/26#F2 · Low · Credit on a factored invoice "settled against the next payment to the seller"
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: The invoice credited was assigned to Harbourline Factoring; payment to anyone but the factor does not discharge the buyer (`22-Invoice.xml:/Invoice/cac:PaymentMeans/cac:TradeFinancing/cac:Clause/cbc:Content` = `Payment to any other account does not discharge the buyer.`). There is no "next payment to the seller": the buyer's next payment is to the factor, and that is where the credit is in fact deducted (`27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalCreditAmount` = `64.00`, paid to Harbourline). The credit note does not mention the factor at all, although it reduces a receivable the factor holds.
- Condition: The settlement note of the credit note agrees with the factoring of the credited invoice and with how the remittance advice settles it.
- Options: (a) preferred: say the credit is deducted from the balance of LD-INV-26-0147 payable to Harbourline Factoring (and name Harbourline as payee or in a note); (b) Lumeway refunds the buyer itself and the remittance pays the full balance (changes the remittance).
- Needs decision: no

### sea/26#F3 · Low · Payment alternative currency and rate without any amount in that currency
- XPath: `/CreditNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`
- XPath: `/CreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The credit is settled by deduction, not paid, and the credit note gives no `PayableAlternativeAmount`; the alternative currency and its rate (without a date) have no amount to apply to.
- Condition: An alternative payment currency and its rate appear only with an amount in that currency, or not at all.
- Options: (a) preferred: drop both; (b) add the alternative amount (64.00 × 0.4 = 25.600 XLC) and the rate's date.
- Needs decision: no

## Checked and consistent
- Credit 1 × 64 = 64.00; taxable 64.00, tax 0.00, tax inclusive and payable 64.00; category G with EXP, as on the invoice line for the frames (`22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `64`).
- The quantity matches the receipt advice's rejection of one frame (`21-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`); the reason (UNCL 4465 code 17, transport damage) fits.
- The credit 64.00 is deducted in the remittance (43778.00 − 64.00 = 43714.00).
- The statement referenced (HF-ST-26-0151, 2026-06-13) is older than the credit note (2026-06-15).
