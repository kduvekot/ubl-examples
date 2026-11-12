# LLM review: 03-ForwardingInstructions.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/03-ForwardingInstructions.xml`, Git blob `0b8c1e57de771a3aa28a4f5ad2687ce72817a1ac` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/03#F1 · High · AdValoremIndicator false here, true in the air waybill for the same shipment
- XPath: `/ForwardingInstructions/cbc:AdValoremIndicator` = `false`
- XPath: `04-Waybill.xml:/Waybill/cbc:AdValoremIndicator` = `true`
- Why: The UBL definition is "a term used in commerce in reference to certain duties, called ad
  valorem duties, which are levied on commodities at certain rates per centum on their value". The
  goods, the shipment `LD-SH-26-0323` and the declared value (512.00 XBL in both documents) are the
  same, so whether ad valorem duties apply cannot change between the shipper's instructions and the
  carrier's waybill. (In transport practice the flag is also read as freight or a valuation charge
  on declared value; under that reading too the two documents disagree about the same shipment.)
- Condition: both documents carry the same AdValoremIndicator for this shipment, and the value
  chosen fits the definition (duties levied on value in Lisavu, or not).
- Options: (a) set both according to whether Lisavu's import duty on HS 7325.99 is ad valorem
  (preferred: the definition is about duties, and the tariff is the source of truth); (b) leave the
  indicator out of both documents if no party acts on it.
- Needs decision: no

### air/03#F2 · Low · Exchange rate without date and with nothing in the target currency
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: Every amount in the instructions is in XBL (declared values 512.00); no amount, charge or
  collect instruction is in XLC, and the rate has no Date ("the date on which the exchange rate was
  established"), so the forwarder cannot tell which day's rate is meant if it were used, e.g. for a
  value in Lisavu's currency at import. The rate 0.4 agrees with the other XBL→XLC rates in the
  world (e.g. `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`).
- Condition: either the exchange rate is used by something in the document (an amount or
  instruction in XLC) and dated, or it is absent.
- Options: (a) preferred: remove it (nothing in forwarding instructions for a CPT shipment is
  settled in XLC); (b) keep it with a Date and a stated use (e.g. the value for Lisavu import in
  XLC).
- Needs decision: no

## Checked and consistent
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount` = `512.00`
  equals the goods value (8 × 64 XBL,
  `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `512.00`)
  and the waybill's declared values (`04-Waybill.xml:/Waybill/cbc:DeclaredCarriageValueAmount` = `512.00`).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredStatisticsValueAmount` = `512.00`:
  one goods item under one statistical heading (HS 732599), so the statistical value is the value of
  all goods; consistent.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredStatisticsValueAmount`: under
  CPT the statistical value might have to include freight to the border — refuted because the price
  is unchanged by the change of terms (64 XBL each, the seller absorbs the freight), so the invoice
  value of the goods is 512.00 either way, and the world's statistical valuation rule is not stated.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount`: a declared
  value only makes sense above the carrier's statutory limit (Montreal Convention, own knowledge:
  26 SDR/kg, 81.6 kg) — refuted because XBL is fictional with no SDR conversion in the world, so the
  comparison cannot be made.
