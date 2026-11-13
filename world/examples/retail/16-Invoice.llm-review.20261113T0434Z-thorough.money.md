# LLM review: 16-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/16-Invoice.xml`, Git blob `e1ce518ac0f84644902623e83922648f889ca0d0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/16#F1 · Low · Outbound delivery freight booked to the buyer's "Stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCost` is "the buyer's accounting code, applied to the Invoice as a whole". The buyer here is Lumeway, and what it buys is the road transport of goods it sold to Brightmarket under DDP from its own warehouse to the customer's store (`/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Truck load within Bayvarra, price per kilometre driven loaded.`; `08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DDP`). Delivering sold goods is a distribution cost of the seller, not a purchase of stock (own knowledge of cost accounting); freight on inbound goods could be capitalised into stock, but this leg carries goods out of stock. No other document of the flow states Lumeway's cost code, so the value cannot be checked against one.
- Condition: The buyer's accounting cost names a cost centre or account for outbound freight or distribution, or is left out.
- Options: (a) preferred: a distribution or outbound freight account (e.g. "Outbound freight"), because that is what the service is to Lumeway; (b) omit both elements, as no other document gives Lumeway's code.
- Needs decision: no

### retail/16#F2 · Low · The transport invoice cannot be matched to the transport order or contract
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `BF-WB-26-0231`
- Why: The service was ordered by Lumeway's transport execution plan request under a framework contract (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`; `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-BF-FW-2026`). The invoice refers only to the carrier's own waybill, and gives neither the request (as the order the buyer matches the invoice against) nor the contract that would justify the rate of 2.85 per loaded kilometre. Matching the invoice to the purchase is what the buyer does with it; the consignment ID in the delivery helps, but it is not the buyer's purchase reference.
- Condition: The invoice refers to the buyer's transport request LD-TR-26-0227 or to the contract LD-BF-FW-2026 under which the rate applies.
- Options: (a) preferred: `OrderReference` with LD-TR-26-0227, because it is Lumeway's own reference for the purchase of the service; (b) `ContractDocumentReference` with LD-BF-FW-2026, which also explains the price.
- Needs decision: no

## Checked and consistent
- Line: 38 km × 2.85 = 108.30; totals 108.30 throughout, tax 0.00.
- Penalty: 1.5 % of 108.30 = 1.6245, rounded 1.62 (`/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `1.62`), per month from 2026-05-31, the day after the due date 2026-05-30 (30 days after the issue date 2026-04-30).
- Tax: E, exemption SVCB2B "Service to a business" under the state sales tax, supply type SERVICES; a transaction-based exemption, not a party status.
- Bill-to: the invoice goes to Lumeway, the bill-to party of the request (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`).
- Payee account XB40BLUM38020502618225 (check digits valid by `check_ids.py`) is held in the name of the seller's registered name Bayforth Forwarding Ltd, in XBL; the RF creditor reference RF66BFINV260234 is valid and repeated in the instruction note.
- The waybill is not ad valorem (`13-Waybill.xml:/Waybill/cbc:AdValoremIndicator` = `false`), consistent with a freight charge per kilometre and no value-based charge.
