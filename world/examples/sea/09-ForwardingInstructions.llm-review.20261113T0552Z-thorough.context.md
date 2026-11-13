# LLM review: 09-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/09-ForwardingInstructions.xml`, Git blob `ba67389d2ddd1ff0fe54f4614822678c58b812b2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/09#F1 · High · The shipment ID given as shipping order, while the flow uses other shipping order numbers
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- Why: ShippingOrderID is a "reference number to identify a Shipping Order", the booking order
  under which the carrier accepts the cargo. Here it repeats the shipment's own identifier, which
  is "an identifier for this shipment", not an order. The same shipment's shipping order is
  `BF-FI-26-0137` in the bill of lading (the forwarder's instructions to the carrier) and the
  consignment ID `LD-CS-26-0133` in the port's status message; the three documents name three
  different shipping orders for one booking.
- Condition: one shipping order number identifies the booking for this shipment in every document
  of the flow that carries a ShippingOrderID, and it is not the shipment's or the consignment's ID;
  where no shipping order exists yet (Lumeway's instruction to its forwarder precedes the booking),
  the element is absent.
- Options: (a) preferred: drop ShippingOrderID here (the booking with the carrier does not exist
  yet when Lumeway instructs Bayforth), and let the booking number of 12 / 14 be the shipping order;
  (b) give the shipping order a number of its own and use it consistently.
- Needs decision: no

### sea/09#F2 · Medium · Gross weight of the shipment without its transport equipment
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: In Shipment, GrossWeightMeasure is "the total gross weight of a shipment; the weight of the
  goods plus packaging plus transport equipment". The value is goods plus pallets; the 40 ft
  container the instructions ask to book weighs 3,750 kg tare, and the loaded container is
  7,856.4 kg in the packing list
  (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure`
  = `7856.4`).
- Condition: the shipment's gross weight includes the transport equipment, or the weight of goods
  and packaging is given in an element that means that (e.g. the consignment's or goods item's
  gross weight).
- Options: (a) preferred: carry 4,106.4 kg as the consignment's gross weight of goods and leave the
  shipment's gross weight to the documents that know the container; (b) 7,856.4 kg here, if the
  container is known.
- Needs decision: no

### sea/09#F3 · Low · The insurer as the party that holds the insurance
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:InsuranceParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: InsuranceParty is "the Party who holds the insurance for this Consignment"; the insurer is
  already the policy's InsurerParty ("the Party providing the insurance"). Under CIF the seller
  takes out the insurance for the buyer, so the holder is Lumeway (or the buyer as beneficiary), not
  the insurer.
- Condition: InsuranceParty is the holder of the insurance (policyholder), or absent.
- Options: (a) preferred: Lumeway Distribution as InsuranceParty; (b) drop it, the policy already
  names the insurer.
- Needs decision: yes (who holds the cover in the story)

### sea/09#F4 · Low · Final delivery to the 3PL in the seller's instructions under CIF
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:FinalDeliveryTransportationService/cbc:Name` = `Truck from the port of Selanu to the 3PL`
- Why: FinalDeliveryTransportationService is "the service for delivery to the consignee under the
  transport contract for this consignment". The sale is CIF Port of Selanu
  (`05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`): the seller's contract of carriage ends
  in the port, and the truck to the warehouse is the buyer's affair. The forwarder's instruction
  from the seller (`ForwarderServiceInstructions`) asks for the truck to the port, the booking,
  export and insurance, not for on-carriage on the island; the final delivery service has no
  instruction behind it.
- Condition: the instructions describe only services under Lumeway's transport contract, or they
  state that Lumeway also arranges on-carriage on behalf of the buyer.
- Options: (a) preferred: drop FinalDeliveryTransportationService here; (b) add the on-carriage to
  the forwarder's instructions if Lumeway arranges it.
- Needs decision: yes (who arranges the on-carriage in Selanu)

### sea/09#F5 · Low · Exchange rate the instructions do nothing with
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: ExchangeRate is "information about the rate of exchange … between two currencies". The only
  amount in the document is the insured value in XBL; nothing is stated in corals, and nothing
  asks the forwarder to convert. The rate has no use here.
- Condition: an exchange rate is present only where an amount in the target currency is given or
  required.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/09#F6 · Low · Reference to the purchase order with only an ID
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: A DocumentReference is "a reference to another document associated with this document"; the
  forwarder receives a buyer's order number without a type code or description and cannot tell what
  it is (it is the order in 05-Order).
- Condition: the reference says it is the buyer's purchase order (type code or description).
- Options: (a) preferred: DocumentTypeCode for an order, or a description.
- Needs decision: no

### sea/09#F7 · Low · Consignor's and consignee's contacts are sales customer service
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The consignor's contact for a shipment is the one who hands over the goods and answers the
  forwarder (shipping, despatch); the consignee's contact receives the goods. Both are given as a
  sales customer-service officer, the consignee's under the name Purchasing.
- Condition: the consignor's contact is a shipping/despatch function and the consignee's a goods
  receiving function, or the contacts are absent.
- Options: (a) preferred: shipping and goods-inwards contacts.
- Needs decision: no

### sea/09#F8 · Medium · A language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; each holds the
  ISO 639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/09#F9 · Low · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name": a gate is not a street. Here the gate matters (the truck picks
  up at Lumeway), but then as the pickup location of the pre-carriage, not in the postal address.
- Condition: no gate in the postal address; if the truck must use Gate 3, it is in the pickup
  location.
- Options: (a) preferred: move it to the pickup/despatch location of the pre-carriage.
- Needs decision: no

## Checked and consistent
- Insured value 59,155.80 XBL = 110 % of the CIF value 53,778.00 given in the bill of lading
  (`14-BillOfLading.xml`, DeliveryTerms Amount), as usual for CIF cover.
- Consignment `LD-CS-26-0133` and shipment `LD-SH-26-0132` are the same in 10, 11, 12 and 14.
- ExporterParty Lumeway and ImporterParty Velumi agree with the sale; ConsolidatableIndicator false
  fits a full 40 ft container.
- "Load the castings last, behind the doors" agrees with the 12 side frames being a separate small
  lot.

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator`: a to-order bill of lading with a named consignee
  — refuted: "to the order of" the named consignee is common, and the bill of lading
  (14-BillOfLading) has the same indicator.
- `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name`: distribution
  to the forwarder who is the addressee — refuted: a distribution list may name the main addressee.
- `/ForwardingInstructions/cbc:AdValoremIndicator`: an explicit false — refuted: it states that no
  ad valorem freight is asked for, a real statement in a forwarding instruction.

## Outside this review
- These instructions (2026-05-09 16:45) and the forwarder's instructions to the carrier
  (12-ForwardingInstructions, 2026-05-10 09:15) precede the packing list (10, 2026-05-12) and the
  export declaration (11, 2026-05-12); the numbering of IDs (0131, 0134, 0135, 0137) does not follow
  the issue order. A timeline question across documents.
