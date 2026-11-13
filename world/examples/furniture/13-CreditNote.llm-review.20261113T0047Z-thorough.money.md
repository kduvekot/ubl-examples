# LLM review: 13-CreditNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/13-CreditNote.xml`, Git blob `62fa2031ce86b8f92b5eb82929f1d00df2904665` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/13#F1 · Low · Restocking deduction on a return the maker asked for
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Restocking deduction`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`
- Why: A restocking deduction compensates a seller for taking back goods the buyer chose to return. In this flow the return is the maker's initiative: `12-InstructionForReturns.xml:/InstructionForReturns/cbc:Note` = `The maker takes back six sets to free the store's shelf.` and `14-DebitNote.xml:/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.` The maker thus asks for the goods back, then charges the store 5 % for restocking them, while the store charges the maker for the transport. The code 64 "Special agreement" could mean the deduction was agreed, but no document of the flow (quotation 02, contract reference, instruction for returns 12) states such an agreement.
- Condition: The flow makes clear why the store bears a restocking deduction for a return the maker requested (an agreement it can be traced to), or the credit note credits the returned sets without it.
- Options: (preferred) state the agreed return terms where the return is arranged (12-InstructionForReturns, or the quotation's terms) so the deduction rests on them; or remove the deduction and credit 3660.00; or change the story so the store asks to return the sets.
- Needs decision: yes

### furniture/13#F2 · Low · Payment terms describe a set-off the document note rules out
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cbc:Note` = `The store paid the invoice; the credit is refunded.`
- Why: The document note says the credit is refunded, and the payment means give a due date and the store's account for the refund. The payment terms instead state set-off against the next payment as the rule and refund as the exception. Read together, the terms add a settlement route the document has already excluded; a reader cannot tell from the terms alone how the credit is settled.
- Condition: The payment terms and the note state the same way of settling the credit.
- Options: (preferred) let the payment terms say the credit is refunded by credit transfer by the due date; or drop the terms note, since the payment means already say it.
- Needs decision: no

### furniture/13#F3 · Low · Creditor reference built from the refunding party's own number
- XPath: `/CreditNote/cac:PaymentMeans/cbc:PaymentID` = `RF63BFCN260579`
- XPath: `/CreditNote/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF63BFCN260579`
- Why: An ISO 11649 reference is a structured *creditor* reference: the creditor creates it so it can match the incoming payment (own knowledge). For this refund the creditor is the store (the payee account is `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Brightmarket Stores Corp`), but the reference is built from the maker's credit note number, and the instruction "Quote …" addresses the payer, which is the maker itself. In 09-Invoice and 14-DebitNote the RF reference is built by the party that receives the money.
- Condition: The payment identifier of the refund is one the payee can match, and the instruction note addresses the party that makes the payment.
- Options: (preferred) keep the credit note number as an unstructured remittance identifier (a `PaymentID` without the ISO 11649 scheme) and drop the "Quote" instruction; or use a reference the store assigned.
- Needs decision: no

### furniture/13#F4 · Low · Payment note calls the credit note an invoice
- XPath: `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-CN-26-0579`
- Why: `PaymentNote` is "Free-form text applying to the Payment for the owner of this account". The document is a credit note (`/CreditNote/cbc:CreditNoteTypeCode` = `381`); the text calls it an invoice, which misleads the store when it matches the refund.
- Condition: The payment note names the document as a credit note (or refund).
- Options: (preferred) "Credit note BF-CN-26-0579" or "Refund of credit note BF-CN-26-0579".
- Needs decision: no

## Checked and consistent
- Line: `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `6` sets × 610 = 3660.00 = `/CreditNote/cac:CreditNoteLine/cac:ItemPriceExtension/cbc:Amount` = `3660.00` = `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:BaseAmount` = `3660.00`; 0.05 × 3660.00 = 183.00; 3660.00 − 183.00 = 3477.00 = `/CreditNote/cac:CreditNoteLine/cbc:LineExtensionAmount` = `3477.00`.
- Totals: line extension, tax exclusive, tax inclusive and payable amounts all 3477.00; taxable amount 3477.00 with tax 0.00.
- Against the invoice: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate` = `2026-03-22` is the issue date of 09-Invoice; the price 610 per set and the exempt STT/RESALE treatment are the invoice's; 6 of the 20 invoiced sets are credited, the quantity of `12-InstructionForReturns.xml:/InstructionForReturns/cac:InstructionForReturnsLine/cbc:Quantity` = `6`.
- Against the debit note: 14-DebitNote refers to this credit note with line amount 3477.00 and the 183.00 deduction, matching this document.
- Refund account: `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB48BLUM38010001570935` passes the IBAN-style check, is held by the store at the Bank of Lumeport main branch (branch code 380100 inside the account number) and is the store's account in 14-DebitNote as well. Due date 2026-05-13 is ten days after issue.
- `/CreditNote/cac:PaymentMeans/cbc:PaymentID` = `RF63BFCN260579` passes the ISO 11649 check digit test (check_ids.py).

## Considered and refuted
- `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:ChargeIndicator` = `false`: suspected that a restocking fee, which the seller charges the buyer, is wrongly encoded as an allowance ("a discount (false)"). Refuted because in a credit note the line amount is what is credited; the deduction reduces the credit, i.e. it is an allowance on the credited amount, and the arithmetic (3660.00 − 183.00 = 3477.00) follows that reading. Encoding it as a charge would increase the credit.
- `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: suspected that "Special agreement" does not match the text "Restocking deduction". Refuted as a code/text mismatch: the code names the basis (an agreement), the text the nature; whether such an agreement exists is F1.
