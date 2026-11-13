# LLM review: 12-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/12-ForwardingInstructions.xml`, Git blob `1f7cbe1f873685d1f9299ab7815123702e495ea9` (committed)
- Last commit changing the example: 62a1919 2026-11-12 sea/12 no longer declares a carriage value; emergency card on the secondary hazard decided
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/12#F1 · Low · Exchange rate that no amount in the instructions uses, and without a date
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: `ExchangeRate` is "information about the rate of exchange (conversion) between two currencies". The forwarder's instructions to the ocean carrier contain no monetary amount at all apart from the parties' share capital, and nothing to be converted into or paid in coral; the freight is prepaid in lume by the shipper (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Ocean freight and bunker surcharge prepaid by the shipper.`). Without a `Date` the rate also does not say when it applied. The element has no business reason here (no fillers); the same unused rate is in the shipper's instructions `09-ForwardingInstructions.xml`.
- Condition: the forwarding instructions carry an exchange rate only if an amount in them is in, or must be converted to, the target currency, and then with the date the rate applies to.
- Options: (a) preferred: remove the exchange rate; (b) keep it only with an amount that needs it (e.g. charges collect at Selanu in coral) and give it a date.
- Needs decision: no
