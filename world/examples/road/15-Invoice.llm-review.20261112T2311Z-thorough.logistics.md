# LLM review: 15-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/15-Invoice.xml`, Git blob `8fdcb4b50214e654097ed80dd7c97b81f9267569` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/15#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated. No other reading fits: 96 / 0.82 = 117.1, which is neither a count in the flow, nor the bench's materials (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg net). The same three values are in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) preferred: relate the factor to the activity it really measures (e.g. per kg of steel, base in KGM), so the value can be recalculated; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep the total.
- Needs decision: no

## Checked and consistent
- Invoiced quantities 96 and 12 equal the despatched quantities (`04-DespatchAdvice.xml`) and the order; the oversupplied 13th side frame received (`13-ReceiptAdvice.xml`) is not invoiced, which is consistent with invoicing what was ordered and despatched.
- OrderReference and DespatchDocumentReference resolve to `01-Order.xml` and `04-DespatchAdvice.xml`.

## Considered and refuted
- `/Invoice/cbc:IssueDate`: goods invoiced on 2026-03-24, before their arrival at the buyer on 2026-03-25 — refuted because under FCA the seller delivers on handing the goods to the buyer's carrier on 2026-03-23 (`04-DespatchAdvice.xml`), so the invoice follows the delivery.
- `/Invoice/cac:Delivery/cac:DeliveryParty`: a delivery without date or place — refuted because the despatch advice reference carries the delivery details and an invoice needs no more.
