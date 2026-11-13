# LLM review: 12-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/12-ForwardingInstructions.xml`, Git blob `1f7cbe1f873685d1f9299ab7815123702e495ea9` (committed)
- Last commit changing the example: 62a1919 2026-11-12 sea/12 no longer declares a carriage value; emergency card on the secondary hazard decided
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8f7babd 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/12#F1 · Medium · Booking instructions to the carrier without goods, equipment or route
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: the forwarder instructs the carrier ("giving instructions regarding the action to be taken for the forwarding of goods described therein") and asks for a booking, but the instructions describe no goods (no goods item, description, packages, commodity code), request no equipment (the consignor asked for "a 40-foot container", `09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions`), and name no port of loading, port of discharge or sailing. Only the gross weight and the consignee are given. A carrier cannot book space from this.
- Condition: the instructions state what is to be carried (goods items, packages, weight), in what equipment (a 42G1 container), and from where to where (Lumeport to Selanu, the sailing), consistent with the bill of lading.
- Options: (a) preferred: add goods items, the requested equipment and the main-carriage stage with load and discharge ports; (b) none better seen.
- Needs decision: no

### sea/12#F2 · Medium · Shipment ID given as shipping order ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- Why: `ShippingOrderID` is "Reference number to identify a Shipping Order"; the value is Lumeway's shipment ID (same in `09-ForwardingInstructions.xml` and `10-PackingList.xml`). An identifier of one kind is given as another. In the forwarder's instructions to the carrier the shipping order, if any, would be the forwarder's.
- Condition: `ShippingOrderID` identifies a shipping order distinct from the shipment, or is absent.
- Options: (a) preferred: drop it, or give Lumeway's instructions `LD-FI-26-0131` as a document reference if the link is wanted; (b) a shipping order number of its own.
- Needs decision: no

### sea/12#F3 · Medium · Language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/12#F4 · Medium · A gate in AdditionalStreetName
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/12#F5 · Low · Carrier's booking number in a request to confirm the booking
- XPath: `/ForwardingInstructions/cbc:CarrierAssignedID` = `TWL-BK-26-55710`
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: `CarrierAssignedID` is the "Reference number assigned by a carrier or its agent to identify a specific shipment, such as a booking reference number when cargo space is reserved". If the carrier has already assigned the booking number, the space is reserved; if the booking still awaits confirmation, the carrier has not assigned a number yet. Both cannot be true when the instructions are issued. No earlier document of the flow shows the booking (the service description only offered the service, `08-TransportServiceDescription.xml`).
- Condition: either the instructions follow a booking the flow shows (and the note does not ask for confirmation), or they request the booking and carry no carrier-assigned number.
- Options: (a) preferred: drop the note's request and keep the number (booking made by phone or portal beforehand, which could be said in a note); (b) drop the number here and let the bill of lading carry it.
- Needs decision: no

### sea/12#F6 · Low · Text copied from the consignor's instructions
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the shipment to the island.`
- Why: name, description, note and other instruction are word for word those of Lumeway's instructions to Bayforth (`09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`). From Bayforth to the carrier, "send the bill of lading to the forwarder" means to Bayforth itself, which is plausible but reads as copied; the consignor's service instructions to the forwarder (book, truck, declare, insure) are rightly not repeated, yet nothing replaces them with what the carrier must do.
- Condition: the free texts are those of the forwarder's instructions to the carrier.
- Options: (a) preferred: e.g. "Release the bill of lading to Bayforth Forwarding" and carrier-related instructions (load at Lumeport, stow castings at the doors).
- Needs decision: no

### sea/12#F7 · Low · Exchange rate the document does not use
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the instructions state no amount at all; nothing is converted to coral. The rate looks copied from master data (same in `09-ForwardingInstructions.xml`).
- Condition: an exchange rate appears only where an amount of the document is converted with it.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/12#F8 · Low · Distribution of the instructions to their own addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Tidewell Ocean Lines`
- Why: the distribution list names the carrier, the party the instructions are addressed to (`CarrierParty`), for this very document; it adds no interested party.
- Condition: document distribution names parties other than the addressee, or is absent.
- Options: (a) preferred: drop it; (b) name a real copy recipient (e.g. Lumeway as consignor).
- Needs decision: no

### sea/12#F9 · Low · Contacts whose function does not fit
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the consignor's contact for transport is Sales' customer service; the consignee's contact is purchasing with the job title of a seller's customer service.
- Condition: each contact's name, job title and department agree with each other and fit the party's role.
- Options: (a) preferred: a shipping contact for Lumeway; a goods-in contact for the consignee.
- Needs decision: no

### sea/12#F10 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the order Velumi sent tags the same renderings `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); across the flow the tag follows the sender's country (16 × `en-XB`, 8 × `en-XL`).
- Condition: Velumi's address renderings carry the same `languageID` in every example.
- Options: (a) preferred: `en-XL` everywhere.
- Needs decision: no

## Checked and consistent
- The booking number is the one the bill of lading carries (`TWL-BK-26-55710`, twice in `14-BillOfLading.xml`), and the bill of lading references these instructions (`BF-FI-26-0137`).
- Consignor Lumeway, forwarder Bayforth (issuer and signatory), carrier Tidewell, consignee Velumi agree with `09-ForwardingInstructions.xml` and the bill of lading; shipment and consignment IDs and the gross weight (4,106.4 kg) agree with the packing list.
- Issued on 2026-05-10, the day after Lumeway's instructions (2026-05-09 16:45), and before the cargo acceptance at the port (bill of lading, 2026-05-13).
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- Forwarding instructions sent by the forwarder (`FreightForwarderParty` = issuer) to the carrier — refuted because UBL defines the document as used "by any party who gives instructions for the transportation services … to any party who is contracted to provide the transportation services", carriers included.
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `true` with a named consignee — refuted, as in `09-ForwardingInstructions.xml`: "to the order of" a named consignee is a common form.

## Outside this review
- Timeline: issued on a Sunday (2026-05-10), while the parties' contacts work "Weekdays 08:00–17:00"; and after the service's nomination deadline of 2026-05-09 10:00 (`08-TransportServiceDescription.xml`, see its review).
