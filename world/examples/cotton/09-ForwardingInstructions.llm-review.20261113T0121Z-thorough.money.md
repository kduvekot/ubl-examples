# LLM review: 09-ForwardingInstructions.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/09-ForwardingInstructions.xml`, Git blob `f8e65d13a83ffc42dbb2cdb364ae14e78a2f0b46` (committed)
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

### cotton/09#F1 · Low · Ad valorem indicator and declared carriage value without an ad valorem charge anywhere
- XPath: `/ForwardingInstructions/cbc:AdValoremIndicator` = `true`
- XPath: `/ForwardingInstructions/cbc:DeclaredCarriageValueAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `2950`
- Why: `AdValoremIndicator` is defined as "a term used in commerce in reference to certain duties,
  called ad valorem duties, which are levied on commodities at certain rates per centum on their
  value"; in a forwarding instruction it is commonly read (own knowledge of carriage practice) as
  "freight or a liability surcharge is charged on the declared value". The declared carriage value
  is "declared … solely for the purpose of varying the carrier's level of liability", which carriers
  price with an ad valorem surcharge. Yet the freight the forwarder bills for this consignment is a
  flat 2 950.00 XBL per 40-foot container with no value-based part (17), and no duty rate or duty
  amount appears in the flow (the import declaration 15 only says "Duties paid by the importer's
  account at customs"). With either reading, nothing in the flow is levied "per centum" on the
  value, so the indicator and the declared value are not reflected in any amount.
- Condition: if the indicator is true, the value-based charge or duty it announces appears where
  it is billed or assessed (the freight invoice 17, or the import); otherwise the indicator is
  false or absent, and the declared carriage value is present only if the mill wants the higher
  liability and pays for it.
- Options: (a, preferred) drop the indicator (and decide whether the mill declares a value at
  all); (b) keep both and add the ad valorem surcharge to the freight invoice 17.
- Needs decision: yes

### cotton/09#F2 · Low · Exchange rate without any amount to convert
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the forwarding instructions contain exactly one amount, the declared carriage value in XLC;
  nothing is stated in Lume, so "the rate of exchange (conversion) between two currencies" converts
  nothing in this document. The rate agrees with 04 and with the import value in 15
  (6 055.452 / 0.4 = 15 138.63 XBL), so it is correct, but it has no use here (rule "no fillers").
  The same rate occurs in the bill of lading 13.
- Condition: the exchange rate is present only if the document states an amount in one of its two
  currencies that the receiver must convert, and says which.
- Options: (a, preferred) drop it; (b) state the declared value also in XBL (the forwarder's and
  carrier's currency) and keep the rate as the conversion used.
- Needs decision: no

### cotton/09#F3 · Low · Tax registrations of forwarder and consignee in a document that does nothing with tax
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: forwarding instructions give "instructions regarding the action to be taken for the
  forwarding of goods"; they bill nothing and declare nothing for tax. The Coastal State sales-tax
  registrations of Bayforth and of the mill are master data with no use here (section 4.8).
- Condition: no party tax registration unless the instructions do something with it.
- Options: (a, preferred) drop both `PartyTaxScheme` blocks.
- Needs decision: no

## Checked and consistent
- The declared carriage value 6 055.452 XLC is the order and invoice value of the 6 129 kg of lint (08, 16).
- FOB Port of Selanu (08) makes the mill the party that contracts the main carriage, which is why the mill instructs its own forwarder here and the forwarder bills the mill in 17.
