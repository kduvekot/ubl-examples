# LLM review: 13-BillOfLading.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/13-BillOfLading.xml`, Git blob `c90a3571519a90b3221ab1bd12b871dc2751864d` (committed)
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

### cotton/13#F1 · Low · Ad valorem bill of lading with a declared value, but the freight billed is flat
- XPath: `/BillOfLading/cbc:AdValoremIndicator` = `true`
- XPath: `/BillOfLading/cbc:DeclaredCarriageValueAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `2950`
- Why: the carrier accepts a value "declared … solely for the purpose of varying the carrier's
  level of liability" and marks the bill ad valorem ("levied … at certain rates per centum on
  their value"). A carrier that accepts higher liability on a declared value charges for it on
  the value (own knowledge of carriage practice); the sea freight billed for this container is a
  flat 2 950.00 XBL with no value-based part (17), and no duty rate appears in the flow either. The
  same pair is in the forwarding instructions 09.
- Condition: if the bill is ad valorem with a declared value, the value-based charge appears where
  the freight is billed; otherwise the indicator is false or absent and no value is declared.
- Options: (a, preferred) drop the indicator and the declared value unless the mill wants the
  higher liability; (b) keep them and add the ad valorem charge to 17.
- Needs decision: yes

### cotton/13#F2 · Low · Freight terms only as a note, no freight stated
- XPath: `/BillOfLading/cbc:Note` = `Freight collect.`
- Why: the bill of lading states "the details of the transportation, charges, and terms and
  conditions under which the transportation service is provided". Who pays the freight is given
  only as free text, and the freight itself not at all, although the consignment has dedicated
  structures for both (`FreightAllowanceCharge`, the consignment's payment terms). For "freight
  collect" the amount to be collected from the consignee side is what the carrier's agent at
  Lumeport needs; it is the 2 950.00 XBL the forwarder passes on in 17.
- Condition: the bill of lading states, in structured form, which freight is due and whether it is
  prepaid or collect, or states explicitly that the freight is "as arranged".
- Options: (a, preferred) add the sea freight as the consignment's freight charge and the collect
  terms as its payment terms; (b) keep the note, if a bill "freight collect, as arranged" without
  an amount is intended.
- Needs decision: no

### cotton/13#F3 · Low · Exchange rate without any amount to convert
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the only amount in the bill is the declared value in XLC; nothing is stated in Lume, so the
  XBL→XLC rate converts nothing here (rule "no fillers"). The rate itself agrees with 04, 09 and 15.
- Condition: an exchange rate is present only if the bill states an amount that must be converted.
- Options: (a, preferred) drop it; (b) state the declared value or the freight in both currencies.
- Needs decision: no

### cotton/13#F4 · Low · Tax registrations and share capital copied into the bill of lading
- XPath: `/BillOfLading/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/BillOfLading/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: the bill of lading bills no tax; the Coastal State sales-tax registrations of carrier,
  forwarder and consignee and the carrier's share capital have no use in the contract of carriage
  (section 4.8, master data copied into a document that does not use it).
- Condition: no party tax registration or share capital unless the bill does something with it.
- Options: (a, preferred) drop the three `PartyTaxScheme` blocks and the carrier's
  `CorporateStockAmount` and `FullyPaidSharesIndicator`.
- Needs decision: no

## Checked and consistent
- 6 055.452 XLC declared is the invoice value of the goods (16) and the value in the forwarding instructions (09).
- "Freight collect" agrees with FOB Port of Selanu (08): the buyer's side pays the main carriage, and 17 bills it to the mill.

## Considered and refuted
- `/BillOfLading/cbc:Note` = `Freight collect.` against 17, where the forwarder bills the mill for sea freight "booked with the ocean carrier": suspected contradiction (collect means payable to the carrier at destination, not through the forwarder) — refuted because the forwarder, established in Lumeport, can pay the collect freight at destination on the mill's behalf and pass it on; both say the mill's side pays.
