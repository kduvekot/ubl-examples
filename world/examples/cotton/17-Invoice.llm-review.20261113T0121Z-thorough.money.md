# LLM review: 17-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/17-Invoice.xml`, Git blob `7bc3532e1225094de3f9e7a64900c767d56742c2` (committed)
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

### cotton/17#F1 · Low · The ocean carrier's tax registration in the forwarder's invoice
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- Why: the invoice is between Bayforth (supplier) and the mill (customer); their tax registrations
  are rightly present. The carrier Tidewell is named to identify the consignment's carriage, but it
  is not a party to the supply and nothing in the invoice is taxed for it; its Coastal State
  sales-tax registration has no use here (section 4.8, master data copied into a document that does
  not use it).
- Condition: the carrier is described in the invoice without a tax registration, unless the invoice
  does something with it.
- Options: (a, preferred) drop the carrier's `PartyTaxScheme`.
- Needs decision: no

## Checked and consistent
- Line: 1 service unit × 2 950 = 2 950.00 = line extension = tax-exclusive = tax-inclusive = payable; tax 0.00 on the E subtotal of 2 950.00, which equals the tax-exclusive amount.
- Terms: 2026-03-04 + 30 days = 2026-04-03 = `DueDate` = `PaymentTerms/PaymentDueDate` = `PaymentMeans/PaymentDueDate`, matching "30 days net".
- Penalty: `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5` of 2 950.00 = 44.25 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `44.25`, for the penalty period of one month starting `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-04-04`, the day after the due date; agrees with "1.5 % surcharge per month late".
- Tax: exemption E with the reason code and text "Service to a business", the same in the subtotal category and the line's classified category, scheme STT, supply type SERVICES.
- Payment: `check_ids.py` passes `RF08BFINV260211` and `XB40BLUM38020502618225`; the payee account is Bayforth's own, a Lume account for a Lume invoice; domestic payment on the Lume mass-payment rail.
- Freight billed to the mill fits FOB Port of Selanu (08) and "Freight collect" in 13.

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCB2B`: an exemption reason that reads like a reverse-charge or place-of-supply rule was checked against "the party's own status, not a transaction" — refuted because the reason belongs to the tax category of the supply (the element's parent), where a transaction-based reason is correct; it is the party tax scheme's exemption reason that must be the party's status.
- `/Invoice/cbc:AccountingCost` = `Raw cotton`: the mill's cost centre for raw cotton on a freight invoice — refuted because freight to the mill is part of the landed cost of the cotton, and it is the same buyer's code as in 08 and 16.
