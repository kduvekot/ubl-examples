# LLM review: 12-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/12-ForwardingInstructions.xml`, Git blob `1f7cbe1f873685d1f9299ab7815123702e495ea9` (committed)
- Last commit changing the example: 62a1919 2026-11-12 sea/12 no longer declares a carriage value; emergency card on the secondary hazard decided
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/12#F1 · High · Shipping order given as the shipment ID, while the bill of lading names this document as the shipping order
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- XPath: `/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`
- Why: ShippingOrderID is a "reference number to identify a Shipping Order". These instructions are
  the shipping order the carrier works under: the bill of lading gives this document's ID,
  BF-FI-26-0137, as its shipping order. The instructions themselves name the shipment's own ID as
  the shipping order, and the port's status message names the consignment ID
  (`13-TransportationStatus.xml:/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`). One
  booking, three shipping order numbers.
- Condition: the shipping order of this booking has one number throughout the flow, and it is not
  the shipment's or consignment's ID.
- Options: (a) preferred: drop ShippingOrderID here (this document is the shipping order; its ID
  identifies it), and keep BF-FI-26-0137 in the bill of lading; (b) a separate shipping order number
  used in 12, 13 and 14.
- Needs decision: no

### sea/12#F2 · Medium · A booking request to the carrier that does not say what to carry or where
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: Forwarding Instructions give "instructions regarding the action to be taken for the
  forwarding of goods described therein". Bayforth asks the carrier to confirm a booking, but the
  shipment has no goods item, no container or equipment size (Lumeway asked for "a 40-foot
  container on the next sailing", `09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions`
  = `Book a 40-foot container on the next sailing to Selanu, arrange the truck to the port, declare the export and insure the cargo.`),
  no port of loading or discharge, no sailing and no cargo description. Only a weight and the
  consignee are given. The carrier cannot book on this.
- Condition: the instructions to the carrier state at least the goods (description, packages,
  weight), the equipment (one 40 ft container), the ports of loading and discharge and the sailing
  or date wanted.
- Options: (a) preferred: add a goods item or consignment summary, the requested equipment and a
  main-carriage stage Lumeport–Selanu with the 15 May sailing; (b) at least the equipment and ports.
- Needs decision: no

### sea/12#F3 · Medium · Gross weight of the shipment without its transport equipment
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: "the weight of the goods plus packaging plus transport equipment"; the loaded container
  weighs 7,856.4 kg (10-PackingList). 4,106.4 kg is goods plus pallets.
- Condition: the shipment's gross weight includes the container, or the goods' gross weight is given
  in an element that excludes it.
- Options: (a) preferred: give 4,106.4 kg as the goods' (consignment or goods item) gross weight.
- Needs decision: no

### sea/12#F4 · Medium · A language code in LocaleCode (three places)
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; each is the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/12#F5 · Low · Exchange rate the instructions do nothing with
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: there is no amount in the document at all; the rate has no use.
- Condition: no exchange rate without an amount that needs it.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/12#F6 · Low · Reference to the purchase order with only an ID
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: the carrier receives the buyer's order number with no type; it cannot tell what it is, nor
  does it need it for the carriage.
- Condition: the reference says what it is, or is absent from the carrier's instructions.
- Options: (a) preferred: drop it; (b) type it as the buyer's order.
- Needs decision: no

### sea/12#F7 · Low · Consignor's and consignee's contacts are sales customer service; consignor's legal data copied
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: the carrier needs the consignor's and consignee's shipping and receiving contacts, not sales
  customer service; the consignor's share capital, legal form and tax registration play no role in
  a booking.
- Condition: contacts with functions that fit, and parties reduced to what the carriage uses.
- Options: (a) preferred: shipping/goods-inwards contacts; drop legal and tax data.
- Needs decision: no

### sea/12#F8 · Low · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` agree with 09, 10, 11 and 14; consignor,
  carrier, forwarder and consignee are the parties of the bill of lading.
- The bill of lading refers to these instructions (`BF-FI-26-0137`) as a document reference.
- DocumentDistribution to the carrier and the forwarder's signature fit an instruction from
  Bayforth to Tidewell.

## Considered and refuted
- `/ForwardingInstructions/cbc:CarrierAssignedID`: the carrier's booking number `TWL-BK-26-55710`
  on instructions that still ask "Please confirm the booking" — refuted: a forwarder typically
  obtains the booking number first and then sends the shipping instructions for confirmation; the
  bill of lading carries the same number (`14-BillOfLading.xml:/BillOfLading/cbc:CarrierAssignedID`
  = `TWL-BK-26-55710`).
- `/ForwardingInstructions/cbc:OtherInstruction`: "Send the bill of lading to the forwarder" in the
  forwarder's own instructions — refuted: Bayforth asks the carrier to send the bill to Bayforth,
  which makes sense.
- `/ForwardingInstructions/cbc:Description`: the same name, description and note as Lumeway's
  instructions in 09 — refuted: the forwarder passing on the instructions in the same words is
  plausible.

## Outside this review
- These instructions (2026-05-10 09:15) are issued after the carrier's nomination deadline in
  08-TransportServiceDescription (2026-05-09 10:00) and before the packing list and export
  declaration they would rely on (2026-05-12); a timeline question across documents (see also the
  08 review).
