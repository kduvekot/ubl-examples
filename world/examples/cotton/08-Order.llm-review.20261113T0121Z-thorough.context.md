# LLM review: 08-Order.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### cotton/08#F1 · Medium · PackSizeNumeric carries the bale weight in kilograms, not a number of items
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- Why: Item/PackSizeNumeric is "The number of items in a pack of this item". 227 is the bale weight
  in kilograms (the order is for 6,129 kg = 27 bales × 227 kg). A count element without unit holds
  a weight. As in 02 and 07.
- Condition: no element meant for a count holds the bale weight.
- Options: (a, preferred) leave PackSizeNumeric out and state the bale weight, if needed, as an item
  property with a KGM quantity.
- Needs decision: no

### cotton/08#F2 · Low · The order says nothing about when the lint is wanted
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: An Order is "A document used to order goods and services". Under FOB Port of Selanu the
  seller must have the bales on board the vessel the buyer's forwarder books, so the time of loading
  is a term the seller needs; the forecast 02 and its revision 07 spread the season's quantity over
  periods, which the order does not pick up. The Delivery carries only the delivery party, no
  requested delivery period, and neither the order header nor its line refers to the forecast or
  the season agreement under which it is placed.
- Condition: the order states the requested delivery or loading period (header or line Delivery),
  or refers to the agreement or forecast that fixes it.
- Options: (a, preferred) add a RequestedDeliveryPeriod for loading at the port of Selanu that fits
  the later documents of the flow; (b) refer to the season agreement as the source of the dates.
- Needs decision: no

### cotton/08#F3 · Low · Region of origin "North coast" is the farm's District elsewhere
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: The same area is a District ("district or geographical division of a country or region") in
  the farm's address and a Region ("recognized geographic or economic region or group of countries")
  here.
- Condition: North coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) use District in OriginAddress.
- Needs decision: no

## Checked and consistent
- 27 bales × 227 kg = 6,129 kg; 6,129 kg × 0.988 XLC = 6,055.452 XLC = line, LineExtension,
  TaxableAmount and PayableAmount.
- FOB Port of Selanu with the buyer's forwarder (Bayforth Forwarding, Bayvarra) as
  FreightForwarderParty fits: under FOB the buyer arranges the main carriage. DestinationCountry XB
  and the mill as delivery party fit the import into Bayvarra.
- The classing certificate in the line (validated 2026-02-20) is dated before the order (2026-02-24)
  and states the grade the line asks for (Middling, 28.6 mm = 1-1/8 inch).
- Buyer's and seller's item identifiers are both present and distinct.

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode` = `CONSUMPTION`:
  a tax type for a scheme named "No general sales tax" suspected as contradictory — refuted because
  the absent tax is a consumption tax; the code names the kind of tax that does not apply.
- `/Order/cbc:RequestedInvoiceCurrencyCode` = `XLC`: the same as the document currency, suspected as
  redundant — refuted because it states a buyer's request (to be invoiced in the seller's currency)
  that a Bayvarran buyer would otherwise not be assumed to make.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`: the
  ordered 6,129 kg of lint is about 34 % of the farm's 18,000 kg of seed cotton (a usual ginning
  outturn), so the certificate stating Middling for the whole lot was suspected of contradicting the
  downgrade of part of that delivery in 05 — refuted for this example, since nothing in the order
  links the lot to the farm's delivery; the contradiction is recorded in the review of 05.
