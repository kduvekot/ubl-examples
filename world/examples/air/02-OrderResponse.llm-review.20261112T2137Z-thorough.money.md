# LLM review: 02-OrderResponse.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/02-OrderResponse.xml`, Git blob `7b81c0b8231d36020cf1c1f9d1fabe0d729ce771` (committed)
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

### air/02#F1 · Low · The forwarder's freight quotation is referenced in the seller's response to the buyer
- XPath: `/OrderResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-QUOTE-AIR-26-0611`
- Why: The ID reads as Bayforth Forwarding's quotation for the air freight. Under CPT
  (`/OrderResponse/cac:OrderLine/cac:LineItem/cac:DeliveryTerms/cbc:ID` = `CPT`) the freight is the
  seller's cost, agreed between the seller and the forwarder and billed to the seller
  (`10-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`);
  the buyer does nothing with that quotation, and the reference carries no DocumentTypeCode or
  description saying what it is. No example of the flow (or any other, counted with
  `grep -rn --include='*.xml' BF-QUOTE world/examples`: 1 hit, this one) has this ID, so the freight
  price it would fix cannot be checked against the invoice (6.8 XBL/kg).
- Condition: every document reference in the response is to a document the buyer uses under this
  order change, or says what it is and why the buyer receives it.
- Options: (a) preferred: drop the reference from the order response (the forwarder's price is the
  seller's business under CPT); (b) keep it with a DocumentTypeCode/DocumentDescription saying it is
  the forwarder's booking confirmation the buyer may track the shipment by.
- Needs decision: no

## Checked and consistent
- No prices or totals are restated: an acceptance (`AP`) of the order change needs none; quantity 8
  and seller's item LD-10443 agree with
  `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:Quantity` = `8`.
- Delivery terms CPT on the line agree with the order change.

## Considered and refuted
- `/OrderResponse/cbc:AccountingCostCode` = `500`: the buyer's accounting code in a document issued
  by the seller — refuted because the definition here is "an accounting cost code applied to the
  order as a whole", and echoing the buyer's code from the order change (same code and text) lets
  the buyer post the response.
