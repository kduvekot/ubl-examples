# LLM review: 08-Order.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/08-Order.xml`, Git blob `71ce9b04ed217222f38cfab91ff0f8de0f9cd595` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### cotton/08#F1 · Low · "No general sales tax" typed as a consumption tax, unlike the invoice for the same supply
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode` = `CONSUMPTION`
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `16-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `TaxTypeCode` is "a code signifying the type of tax". The scheme here is the absence of a
  sales tax in Lisavu; giving it the type "tax on consumption" describes a tax that does not
  exist. The invoice for the same order line (16) describes the same scheme without a type, and so
  do the self-billed documents 01, 04 and 05. The scheme with this name occurs in 9 examples
  (`grep -rl --include='*.xml' 'No general sales tax' world/examples`); this order is the only one
  with a `TaxTypeCode` on it.
- Condition: the order and the invoice describe the tax scheme of the same supply in the same way,
  and the scheme carries a tax type only if that type is the type of a tax that applies.
- Options: (a, preferred) drop the `TaxTypeCode` here, as in the other eight; (b) if the type is
  meant to say which kind of tax is absent, give it the same way in every document of the flow.
- Needs decision: no

## Checked and consistent
- Line: 6 129 kg × 0.988 per 1 kg = 6 055.452 = line extension = anticipated line extension = anticipated payable amount = taxable amount of the O subtotal; tax 0.000. 6 129 kg is 27 bales of 227 kg.
- The invoice 16 bills the same line (6 129 kg at 0.988, 6 055.452, order line 1) in the requested invoice currency XLC, with the same tax category O.
- `/Order/cac:DeliveryTerms/cbc:ID` = `FOB` at the Port of Selanu agrees with the mill's own forwarder (Bayforth) billing the sea freight to the mill in 17 rather than the ginnery including it in its price.
- Buyer's accounting cost `2200` "Raw cotton" is the code the invoice 16 repeats.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`: the buyer's Bayvarra sales-tax registration in an order whose supply is outside the scope of tax was suspected of being master data copied in — refuted because the goods are imported into Bayvarra, where the mill's registration matters for the import (15) and is quoted on the invoice (16); an order that announces the tax treatment may name the buyer's registration.
- `/Order/cac:TaxTotal/cbc:TaxAmount` = `0.000`: a tax total in an order suspected of being a filler — refuted because the order states the anticipated tax treatment of the supply (outside scope), which the invoice confirms.
