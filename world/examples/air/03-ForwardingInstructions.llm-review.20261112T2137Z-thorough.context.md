# LLM review: 03-ForwardingInstructions.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### air/03#F1 · High · Reference to an order that does not exist
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0319`
- Why: No example has the document ID VT-PO-26-0319 (searched over `world/examples/*/*.xml`). The order is VT-PO-26-0127 (sea/05-Order.xml), changed by VT-OC-26-0320 (01-OrderChange.xml), confirmed by LD-OR-26-0321 (02-OrderResponse.xml). The reference also carries no DocumentTypeCode, so even its kind is not stated. The same ID is used in 06/08-DespatchAdvice.xml.
- Condition: the reference resolves to the order or order change these instructions execute, and says what kind of document it is.
- Options: (preferred) VT-OC-26-0320, the change that asked for the air delivery, with a document type; or VT-PO-26-0127 if the instructions are to point to the order itself.
- Needs decision: no

### air/03#F2 · Medium · An instruction about a bill of lading in air freight instructions to the forwarder
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- Why: OtherInstruction holds "other free-text instructions to the forwarders or carriers related to the shipment". The shipment goes by air (04-Waybill.xml is an air waybill, WaybillTypeCode `AWB`); there is no bill of lading. And the instructions are addressed to the forwarder itself (FreightForwarderParty and DocumentDistribution are Bayforth Forwarding), so "send … to the forwarder" has no one to act on it.
- Condition: the instruction refers to the transport document of this mode and to a party other than its own addressee, or is absent.
- Options: (preferred) an instruction that fits, e.g. "Send the air waybill copy to the consignor"; or drop it.
- Needs decision: no

### air/03#F3 · Medium · A transport event with no type and no place
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceTime` = `19:00:00`
- Why: Consignment/TransportEvent is "any additional significant occurrences … not specified elsewhere in this Consignment". This one has only a date, a time and CompletionIndicator false: no TransportEventTypeCode, no description, no location. A forwarder cannot tell whether 13 May 19:00 is a cut-off, a pickup, an acceptance or a departure. UBL has dedicated events for the likely meanings (Consignment/RequestedPickupTransportEvent, ShipmentStage/AcceptanceTransportEvent).
- Condition: the event says what happens and where, preferably in the dedicated element for it, or it is absent.
- Options: (preferred) the dedicated element for what is meant (e.g. a requested pickup or the acceptance cut-off for the 14 May flight) with its location; or a TransportEventTypeCode and Location on the generic event.
- Needs decision: no

### air/03#F4 · Medium · AdValoremIndicator false while a value for carriage is declared, and true in the waybill
- XPath: `/ForwardingInstructions/cbc:AdValoremIndicator` = `false`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount` = `512.00`
- XPath: `04-Waybill.xml:/Waybill/cbc:AdValoremIndicator` = `true`
- Why: The instructions declare 512.00 XBL "solely for the purpose of varying the carrier's level of liability"; in air freight a declared value for carriage is what triggers the ad valorem (valuation) charge, and the air waybill for the same consignment says AdValoremIndicator `true` with the same 512.00. The instructions and the waybill thus disagree about the same consignment. (UBL's own definition of AdValoremIndicator speaks of ad valorem duties, which adds to the doubt about what the indicator means here; resting on knowledge of air-freight practice.)
- Condition: the instructions and the waybill agree on whether an ad valorem rate applies, and that agrees with whether a value for carriage is declared.
- Options: (preferred) `true` here, as the shipper declares a value; or no declared value and `false` in both documents if no higher liability is wanted.
- Needs decision: yes (whether the shipper wants higher carrier liability)

### air/03#F5 · Medium · LocaleCode holds a language code
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/03#F6 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street. Here a gate would matter, because the forwarder picks the goods up (Package/Pickup BF-PU-26-0611), but then it belongs to the pickup location, not to the consignor's postal address.
- Condition: no gate in a street-name element of the postal address; if the forwarder needs the gate, it is given with the pickup.
- Options: (preferred) move it to a pickup location (Package/Pickup/cac:PickupLocation) with the address of the dispatch area; or drop it.
- Needs decision: no

### air/03#F7 · Low · Shipping order ID equal to the shipment ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "Reference number to identify a Shipping Order"; the value is the shipment's own ID. No shipping order exists in the flow, and the later documents use yet another value as the shipping order (the consignment ID LD-CS-26-0324 in 04, 05 and 09), so the shipping order reference has no stable meaning.
- Condition: ShippingOrderID identifies a shipping order (or these instructions as the order to ship), and the waybill and status reports quote the same value; or it is absent.
- Options: (preferred) drop ShippingOrderID here and let the later documents quote these instructions (LD-FI-26-0322) as their shipping order or forwarding instruction; or a real shipping order number used consistently.
- Needs decision: no

### air/03#F8 · Low · An exchange rate the instructions do nothing with
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: Every amount in the instructions is in XBL (declared values 512.00); no amount, charge or payment in Coral appears, and no instruction asks for conversion (e.g. charges collect at destination). The exchange rate has no date, so it is not even clear when it applies.
- Condition: the exchange rate is absent, or the document uses it (an amount or charge in XLC, or collect charges at Selanu) and dates it.
- Options: (preferred) drop it; or add the purpose (charges collect at destination) with its date.
- Needs decision: no

### air/03#F9 · Low · Document distribution to the document's own addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: DocumentDistribution is "A list of interested parties to whom this document is distributed". Bayforth Forwarding is the forwarder to whom the instructions are issued; listing it again as an interested party adds nothing. A real copy recipient (the carrier, the consignee) is not listed.
- Condition: DocumentDistribution lists only parties other than the addressee that receive a copy, or is absent.
- Options: (preferred) drop it; or distribute to a party that needs a copy.
- Needs decision: no

### air/03#F10 · Low · Signature aggregate without a signature
- XPath: `/ForwardingInstructions/cac:Signature/cbc:ID` = `LD-SIG-FI-03`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension that could be verified. 131 of 133 Signature aggregates over `world/examples/*/*.xml` are like this (lxml count).
- Condition: either a verifiable signature (method and attachment) is present, or no Signature aggregate.
- Options: (preferred) drop it; or add signature data where the story needs a signed instruction.
- Needs decision: yes (a convention across many examples)

## Checked and consistent
- Consignment LD-CS-26-0324, shipment LD-SH-26-0323, gross weight 81.6 kg and the parties agree with 04-Waybill.xml and 06-DespatchAdvice.xml.
- Declared values 512.00 XBL equal the value of the change line in 01-OrderChange.xml (8 × 64).
- Pickup by Bayforth Forwarding (earliest 12 May) and requested despatch 13 May are after the order response (12 May 10:46) and fit a flight on 14 May.
- SSCC `095206103190000015` passes the check digit (check_ids.py).

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `false`: suspected filler, as air waybills are never to order — refuted: stating that the transport document is not consigned to order is a true, explicit statement and not implied by absence.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:SplitConsignmentIndicator` = `false`: suspected a state ("has been split in transit") that cannot be known before transport — refuted: at issue time the consignment has not been split, and the statement is true.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredStatisticsValueAmount` = `512.00`: suspected data the forwarder does not use — refuted: the forwarder lodges the export declaration for goods leaving Bayvarra and needs the statistical value.
- `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`: suspected contradiction with the order response's "the forwarder is booked" — refuted: a written confirmation of an agreed booking is normal.

