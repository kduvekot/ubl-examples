# LLM review: 03-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/03-Invoice.xml`, Git blob `80f13e4ce6ede50f2dc64b8d628230f6cf1de513` (committed)
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

### energy/03#F1 · Medium · Electricity sold as a commodity classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture". The line sells 18400 MWh of electricity fed into the grid ("Electricity, wholesale"), i.e. the energy itself, not the use of a network (which energy/02 rightly classifies as services). In the same flow, the other energy commodity, natural gas, is classified as goods (energy/06 and energy/07). VAT practice treats electricity and gas alike, as goods (EU VAT Directive Art. 15(1), own knowledge); a world in which gas is goods but electricity is services would need a stated reason. The same commodity at retail level is also classified as services in utilities/02-Invoice.xml (lines 1–3), so the question is wider than this example: counted with `grep -rh --include=*.xml SupplyTypeCode world/examples | sort | uniq -c`, SERVICES occurs 29 times and GOODS 32 times; the energy-commodity lines (electricity or gas sold by kWh/MWh) are 03-Invoice line 1 and utilities/02-Invoice lines 1–3 (SERVICES) against 06-Invoice and 07-Invoice (GOODS).
- Condition: the supply type of electricity and of gas sold as energy is the same throughout the world, and it is the one the world's tax rules give them; network use stays services.
- Options: (a) preferred: GOODS for the electricity line here (and for the energy lines in utilities/02), consistent with 06/07 and with VAT practice; (b) keep SERVICES only if the world's VAT law treats electricity as a service, and then say so in the world's tax rules and explain why gas differs.
- Needs decision: yes (tax treatment)

## Checked and consistent
- Line arithmetic: 18400 × 9800 = 180320000 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `180320000` = LineExtensionAmount, TaxExclusiveAmount and TaxableAmount of the totals.
- Tax: 20 % of 180320000 = 36064000 = `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `36064000`; 180320000 + 36064000 = 216384000 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `216384000`.
- Settlement discount: 2 % of 216384000 = 4327680 = `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4327680`; settlement period 2026-04-03 to 2026-04-13 (10 days) and due date 2026-05-03 (30 days) match the note.
- Payment: RF32MPINV260151 passes its check digits; Montebrio Power's account XU720351041700000005021992 passes the IBAN-like check and is the same account that pays Kelpstone in `09-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XU720351041700000005021992`.
- Physics and price against the gas bought: Montebrio Power buys 36800 MWh of gas in March (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`) and sells 18400 MWh of electricity, an efficiency of 50 %, plausible for a combined-cycle gas plant (own knowledge: about 50–60 %). Fuel cost per MWh of electricity 2 × 3600 = 7200 XUF against a selling price of 9800 XUF: a plausible margin.

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S`: wholesale electricity between two registered traders is often reverse-charged in real practice — refuted: that is an option of the EU directive (Art. 199a), not a rule a fictional national VAT must follow; the standard rate is a legitimate treatment.
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4327680`: discount on the amount including VAT — refuted as in 02-Invoice: a legitimate reading of the element.
