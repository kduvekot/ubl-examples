# LLM review: 02-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/02-Invoice.xml`, Git blob `ca1ffa8a13476757483bcb761f1e9079132080e5` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/02#F1 · Low · Two identical electricity lines that nothing distinguishes
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `412800`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- Why: lines 1 and 2 bill the same item (electricity network use, FG-NET-E) at the same price (6.2 XUF per kWh), the same tax category and the same period (the invoice period, March 2026). Nothing on either line says which connection or consumption point it is for: no note, no delivery location, no reference to a meter or a utility statement. For the gas line there is a utility statement (energy/01) that carries the consumption point and meter; for the two electricity lines there is none in the flow. The buyer, a retailer that passes these charges on to its customers, cannot tell from the invoice which customer's network use each amount is, and so cannot check the 2559360 and 115320 XUF against its own billing.
- Condition: each electricity line identifies what it is for (consumption point, meter or connection, e.g. in a line note, `Delivery/DeliveryLocation`, a document reference to a utility statement), or the two lines are merged into one if the split has no meaning.
- Options: (a) preferred: give each line the identifier of its consumption point (a line note or a document reference to the metering data), as the gas line has through its utility statement; (b) one line of 431400 kWh if the retailer needs no split.
- Needs decision: no

## Checked and consistent
- Line arithmetic: 412800 × 6.2 = 2559360; 18600 × 6.2 = 115320; 61200 × 1.9 = 116280 (`/Invoice/cac:InvoiceLine[3]/cbc:LineExtensionAmount` = `116280`).
- Totals: 2559360 + 115320 + 116280 = 2790960 = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `2790960` = TaxExclusiveAmount = TaxableAmount; 20 % of 2790960 = 558192 = `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `558192`; 2790960 + 558192 = 3349152 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3349152`.
- Settlement discount: 2 % of 3349152 = 66983.04 → `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `66983`; settlement period 2026-04-03 to 2026-04-13 = 10 days, as the note says; due date 2026-05-03 = 30 days after issue, the same in DueDate, PaymentMeans and PaymentTerms.
- Tax: standard rate 20 % VAT on network use classified as services (`/Invoice/cac:InvoiceLine[3]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`): use of a distribution network is a service, also under real VAT practice (own knowledge).
- Payment: RF reference RF13FGINV260150 passes its check digits (check_ids.py) and is quoted in the instruction note; the payee account of Ferrano Grid passes the IBAN-like check and is held in XUF, the document currency.
- The quantity of line 3 agrees with the utility statement energy/01 (61200 kWh).

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `66983`: suspected to be computed on the wrong base — refuted: 2 % of the payable amount including VAT is a legitimate reading of "the amount of a settlement discount offered for payment"; the net base (55819) would be the other reading, but nothing in the document asks for it.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: real-time gross settlement for a domestic invoice payment — refuted: plausible for a payment of over 3 million XUF between two utilities, and consistent with 03-Invoice.
- `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`: penalty interest not mentioned in the payment terms note — refuted: the note only summarises net days and discount; the structured penalty does not contradict it.

## Outside this review
- The same consumption (61200 kWh gas, meter FG-G-20417) is billed onward in utilities/02-Invoice.xml; whether the retailer's price (8.4 XUF/kWh, "network charges included") covers the 1.9 XUF/kWh network charge billed here is a question across flows.
