# LLM review: 02-OrderResponse.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### air/02#F1 · High · Response line 1 is the bench line of the referenced order
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `VT-PO-26-0127`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: LineItem/ID is "An identifier for this line item, assigned by the buyer". The response
  refers to order VT-PO-26-0127 (sea/05-Order.xml), whose line 1 is 96 Serra 180 benches; it
  accepts line 1 as 8 side frames (LD-10443). The value comes from the order change air/01, which
  adds the frames under the already used ID 1 (air/01#F1). As it stands the acceptance reads as a
  change of the bench line.
- Condition: the response line carries the ID that the added side-frame line has in the order change,
  and that ID is not one of the existing lines of VT-PO-26-0127.
- Options: follow the fix of air/01#F1 (preferred: new line ID 3); the response follows the order change.
- Needs decision: no

### air/02#F2 · Low · Reference to the forwarder's quotation without saying what it is
- XPath: `/OrderResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-QUOTE-AIR-26-0611`
- Why: The reference has only an ID; no DocumentTypeCode or DocumentDescription says that it is
  Bayforth Forwarding's air-freight quotation to the seller. The document is not in the flow, and the
  buyer, who receives this response, is not a party to that quotation; under CPT the freight is the
  seller's cost. The same number 0611 reappears as the pickup ID BF-PU-26-0611 in air/03.
- Condition: either the reference says what the document is (type or description) and why the buyer
  receives it, or it is not in the response.
- Options: drop the reference from the response (preferred: the buyer does nothing with the
  seller's freight quotation); or add a DocumentTypeCode/DocumentDescription.
- Needs decision: no

### air/02#F3 · Low · "The forwarder is booked" before the booking is instructed; the flight has no date
- XPath: `/OrderResponse/cbc:Note` = `Accepted: the frames fly on the morning flight; the forwarder is booked.`
- XPath: `/OrderResponse/cbc:IssueTime` = `10:46:00`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:IssueTime` = `13:44:00`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: The response (2026-05-12 10:46) says the forwarder is booked; the forwarding instructions that
  book it are sent the same day at 13:44 and ask the forwarder to confirm the booking. "The morning
  flight" has no date; the structured line has delivery terms but no delivery date, so the buyer cannot
  tell when the frames arrive (the waybill air/04 later plans 2026-05-14 07:00).
- Condition: the note does not state a booking that has not yet been made, and the response gives the
  promised delivery or flight date in a structured element (e.g. the line's Delivery/PromisedDeliveryPeriod)
  or in the note.
- Options: reword the note ("the forwarder has quoted; booking follows") and add the promised delivery
  date on the line (preferred); or move the response after the booking.
- Needs decision: no

## Checked and consistent
- `OrderReference/ID` VT-PO-26-0127 resolves to sea/05-Order.xml; `OrderChangeDocumentReference/ID`
  VT-OC-26-0320 resolves to air/01-OrderChange.xml (issued 2026-05-11 07:50, before this response).
- Quantity 8 EA and the item LD-10443 agree with air/01.
- Physics: NetNetWeightMeasure 76 kg for 8 frames = 9.5 kg each; sea/10-PackingList.xml gives
  122.4 kg gross for 12 frames (10.2 kg each) and 3762 kg net for 96 benches and 12 frames, which
  is 96 × 38 + 12 × 9.5 = 3648 + 114 = 3762 kg, so 9.5 kg net per frame is the flow's own figure.
  9.5 kg of cast iron (about 7.2 t/m³, own knowledge) is about 1.3 dm³ of metal, plausible for a
  bench end frame. NetVolumeMeasure 0.42 m³ = 0.0525 m³ per frame, about 181 kg/m³ as envelope
  density, plausible for an open casting. Both agree with air/03 (76 kg, 0.42 m³).
- Line-level DeliveryTerms CPT agrees with the air delivery of air/01.

## Considered and refuted
- `/OrderResponse/cac:FreightForwarderParty/cac:PartyName/cbc:Name`: a forwarder in a response to the
  buyer — refuted because UBL defines FreightForwarderParty here as "A freight forwarder or carrier"
  and the seller tells the buyer who handles the CPT carriage, which matters for the delivery party
  that has to collect the goods.
