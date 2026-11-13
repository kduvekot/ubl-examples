# LLM review: 18-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/18-RemittanceAdvice.xml`, Git blob `47eb48a5adfeabc95404a79c9aab2a6843d04e46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/18#F1 · Low · Two different references for the same payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `LTM-PAY-26-0191`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `LTM-0191`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `LTM-PAY-26-0191`
- Why: `PaymentOrderReference` is "an internal reference to the order for payment from the payer
  to the payer's bank", `PayerReference` "an internal reference to the payer's order for payment".
  Both name the mill's own payment order, and the payment means confirms that order as
  LTM-PAY-26-0191; `LTM-0191` is a second, shorter number for the same order that nothing explains.
  A remittance advice exists so that the payee can match the payment; two numbers for one order
  invite a mismatch.
- Condition: the mill's payment order is identified by one reference, or the two references
  visibly identify two different things.
- Options: (a, preferred) drop `PayerReference`, which repeats what `PaymentOrderReference` says;
  (b) give it a different meaning (e.g. the mill's payment-run number) and a value that fits it.
- Needs decision: no

### cotton/18#F2 · Low · Zero total of credits in an advice without credit lines
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `0.000`
- Why: "the totals of all credit amounts" is 0.000 because no line carries a credit amount; a zero
  total of something absent carries no information (rule "nothing implied by absence"). The other
  remittance advice of the flow (06), which does have a credit line, carries no totals of debits
  and credits at all.
- Condition: the advice carries a credit total only when it has credit amounts.
- Options: (a, preferred) drop `TotalCreditAmount` (and keep `TotalDebitAmount`, which has a
  value, or drop both as in 06).
- Needs decision: no

### cotton/18#F3 · Low · The invoice is referenced twice on the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SCG-INV-26-0210`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SCG-INV-26-0210`
- Why: the billing reference already identifies the paid invoice with its issue date; the generic
  `DocumentReference` ("a reference to a document associated with this remittance advice line")
  names the same invoice again with the same date and adds only the type "Invoice", which the
  billing reference's element already says. No second document is associated with the line.
- Condition: each document associated with the line is referenced once.
- Options: (a, preferred) drop the line's `DocumentReference`.
- Needs decision: no

### cotton/18#F4 · Low · Customer's sales-tax registration in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: the remittance advice reports a payment; it declares no tax and the paid invoice carries no
  tax. The mill's Coastal State sales-tax registration has no use here (section 4.8); the
  ginnery's own remittance advice 06 carries no party tax data.
- Condition: no party tax registration in the remittance advice unless it does something with it.
- Options: (a, preferred) drop the customer's `PartyTaxScheme`.
- Needs decision: no

## Checked and consistent
- Amounts: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `6055.452` is the payable amount of 16; `TotalDebitAmount` and `TotalPaymentAmount` 6 055.452; balance 0.000, i.e. the invoice is paid in full.
- References: the RF reference `RF46SCGINV260210` (valid check digits) is the one 16 asks to quote, given as `PaymentID` and as the invoicing party's reference; the invoice number and issue date 2026-03-02 match 16.
- Accounts: the payee account `XL31BSEL0020004922263` is the ginnery's coral account from 16; the payer pays from its own Lume account `XB35BLUM38020504608076` (valid check digits), which fits a coral invoice paid by a Bayvarra buyer through currency conversion at its bank.
- Timing: issued 2026-03-29, before the due date of 16, so no penalty interest arises (whichever of the due dates discussed for 16 applies).
- Payment purpose `SUPP` (supplier payment) fits a payment for goods.
