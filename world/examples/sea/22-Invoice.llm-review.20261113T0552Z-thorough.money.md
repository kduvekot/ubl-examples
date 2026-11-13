# LLM review: 22-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/22-Invoice.xml`, Git blob `4c08d1557efc54cdc92ff08f70f42ccd45fd61e0` (committed)
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

### sea/22#F1 · High · Freight and insurance charged on top of a price agreed CIF; invoice total exceeds the confirmed order total
- XPath: `/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`
- XPath: `/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `53778.00`
- XPath: `/Invoice/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: Under CIF (Incoterms, own knowledge) the seller contracts and pays for carriage and insurance to the named port, and the agreed price includes them. The order and the order response, both CIF Port of Selanu at the same unit prices (520 and 64), agree a total payable of 50688.00 (`05-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `50688.00`, `06-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00`). The invoice then adds the seller's own freight and insurance costs (billed to Lumeway by its forwarder, `18-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3175.00`) as charges to the buyer, raising the total to 53778.00. The CIF term on the invoice and the confirmed order total contradict the charges. The rest of the flow follows the invoice (statement, remittance, the bill of lading's CIF value 53778.00), so the question is which story is meant.
- Condition: The invoice total agrees with the price confirmed in the order response for the agreed delivery term: either a CIF price that already contains freight and insurance (no separate charges, total 50688.00), or a term under which freight and insurance are for the buyer's account and were agreed as extra charges in the order/order response.
- Options: (a) preferred: keep CIF and the confirmed prices, drop the two charges (taxable and payable amounts, percentages, deposit split and the follow-up documents adjust); this matches the order and the meaning of CIF; (b) keep the charges and make the order and order response say that freight and insurance are recharged at cost (e.g. as anticipated charges in the order response), or change the term (e.g. FOB/FCA with freight prepaid and added, "CFR/CIF" only as a delivery point); (c) treat 50688.00 as an ex-works/FOB price and change the delivery term throughout the flow.
- Needs decision: yes

### sea/22#F2 · High · Balance due date does not follow from "30 days net" after shipment
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:ReferenceEventCode` = `81`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:InstallmentDueDate` = `2026-06-28`
- XPath: `/Invoice/cbc:DueDate` = `2026-06-28`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-06-28`
- Why: Reference event 81 is "Date of shipment as evidenced by the transport document(s)". The bill of lading is dated 2026-05-14 (`14-BillOfLading.xml:/BillOfLading/cbc:IssueDate` = `2026-05-14`); the vessel left Lumeport on 2026-05-14 and arrived at Selanu on 2026-05-18. 30 days after shipment is 2026-06-13 (after arrival: 2026-06-17); 2026-06-28 is 45 days after shipment and invoice date. The due date and the penalty period starting 2026-06-29 therefore contradict the stated terms. The statement repeats 2026-06-28 (`25-Statement.xml:/Statement/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-06-28`).
- Condition: The balance due date equals the reference event date plus the stated term, and the penalty period starts the day after it; the same date appears in the payment means, the invoice due date and the statement.
- Options: (a) preferred: keep "30 days net" from shipment and make the due date 2026-06-13 (penalty from 2026-06-14), checking that the remittance of 2026-06-25 then becomes a late payment, or adjust that too; (b) keep 2026-06-28 and state the term that yields it (e.g. "45 days net from shipment").
- Needs decision: yes

### sea/22#F3 · High · Exchange rate and terms validity dated after the invoice was issued; two dates for the same rate
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ExchangeRate/cbc:Date` = `2026-05-18`
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ValidityPeriod/cbc:StartDate` = `2026-05-18`
- XPath: `/Invoice/cac:PaymentAlternativeExchangeRate/cbc:Date` = `2026-05-14`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-14`
- Why: `ExchangeRate/Date` is "the date on which the exchange rate was established". An invoice issued on 2026-05-14 cannot state a rate established on 2026-05-18. The same pair XBL→XLC at 0.4 is stated twice, once dated 2026-05-14 (payment alternative rate) and once 2026-05-18 (terms rate). The validity of the balance terms also begins on 2026-05-18, four days after issue and with no stated reason, and ends on 2026-07-02, after the due date and inside the penalty period, which leaves open what applies to a payment between 2026-05-14 and 2026-05-17.
- Condition: No date in the invoice that records something already established (rate date) lies after the issue date; the invoice states the XBL→XLC rate once, or both statements carry the same date; the terms' validity period, if present, covers the period from issue to due date in a way the terms explain.
- Options: (a) preferred: drop the exchange rate from the payment terms (the payment alternative rate already serves the XLC amount) and drop the validity period, or date both 2026-05-14; (b) keep a separate terms rate only if the terms say the rate is fixed on a future event (then not as an established rate).
- Needs decision: no

## Checked and consistent
- Lines: 96 × 520 = 49920.00 and 12 × 64 = 768.00; line total 50688.00; charges 2950.00 + 140.00 = 3090.00; tax exclusive 53778.00; tax 0.00; prepaid 10000.00; payable 43778.00; alternative 43778.00 × 0.4 = 17511.200 XLC.
- Prices equal the catalogue's XLC prices at 0.4 (208 XLC / 0.4 = 520 XBL, 25.6 XLC / 0.4 = 64 XBL).
- Payment percentages: 10000.00 / 53778.00 = 18.59 %, 43778.00 / 53778.00 = 81.41 %, together 100.00 %; penalty 1.5 % × 43778.00 = 656.67.
- Deposit: due 2026-05-09, the day after the order response (reference event 8, "Date of confirmation of order received"; `06-OrderResponse.xml:/OrderResponse/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-09`); paid 2026-05-08, received 2026-05-09, 10000.00 as in the order response.
- Tax: category G (free export item) with reason EXP on both lines, both charges and the subtotal; taxable amount 53778.00 includes the charges.
- Factoring: type 393 (factored invoice), note, payee Harbourline Factoring, payee account and financing account `XB51BLUM38020502304038` in Harbourline's name, financing party Harbourline, clause on discharge, remittance advice routed to Harbourline; the same account is used by the statement and the remittance advice.
- RF reference `RF20LDINV260147` valid, quoted identically in the payment means, terms, statement and remittance advice.

## Considered and refuted
- `/Invoice/cac:AllowanceCharge[2]/cbc:AllowanceChargeReasonCode` = `96`: suspected a code from the allowance list (UNCL 5189) used for a charge while the freight charge uses UNCL 7161 — refuted because UNCL 5189 is "Allowance or charge identification" and code 96 is Insurance in the D22A source, so it fits the element; the mixed lists are a style question.
- `/Invoice/cac:PaymentMeans/cac:CreditAccount/cbc:AccountID` = `HF-CL-VT-001`: suspected a credit account with no use in a credit transfer — refuted because a credit account is one "for sales on account", and the factor's ledger account of the debtor Velumi is such an account, useful for the payer's reference.
- `/Invoice/cac:PaymentMeans/cbc:ServiceLevelCode` = `NURG`: suspected a conflict with the real-time channel RTNS — refuted because a non-urgent service level on a real-time net settlement rail is a valid combination (the urgency concerns priority, not settlement mode).
