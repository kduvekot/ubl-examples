# LLM review: 03-ForwardingInstructions.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

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

### air/03#F1 · High · The referenced order does not exist
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0319`
- Why: No example has the ID `VT-PO-26-0319`, and `flow_index.py air` resolves it to nothing. The goods are the 8 side frames that order `VT-PO-26-0127` (`sea/05-Order.xml`) as changed by `VT-OC-26-0320` (`01-OrderChange.xml`) asks for. The reference has no DocumentTypeCode either, so it does not say it is an order. The same ID is the OrderReference of `06-DespatchAdvice.xml` and `08-DespatchAdvice.xml`.
- Condition: the reference resolves to the order or order change the goods belong to, and says what kind of document it is.
- Options: (a) `VT-OC-26-0320` (and/or `VT-PO-26-0127`) with a DocumentTypeCode (preferred); (b) add an order `VT-PO-26-0319` to the flow, which changes the story (a separate order instead of an order change).
- Needs decision: no

### air/03#F2 · High · The package is far smaller than the goods it is said to hold
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cbc:Quantity` = `8`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[1]/cbc:Measure` = `800`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[2]/cbc:Measure` = `300`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[3]/cbc:Measure` = `300`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetVolumeMeasure` = `0.42`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:GrossVolumeMeasure` = `0.576`
- Why: The one package "LD-AIR-BOX" holds 8 items (Package/Quantity is "The quantity of items contained in this package") and measures 0.8 × 0.3 × 0.3 m = 0.072 m³. The goods alone take 0.42 m³ net, almost six times the box. The waybill's gross volume, 0.576 m³, is exactly 8 × 0.072 m³, so the dimensions seem to describe one box per frame (8 boxes, each with one bagged frame of 0.0525 m³). As encoded, the consignment does not fit its package.
- Condition: the packages' number and dimensions can hold the stated net volume, and their total agrees with the waybill's gross volume.
- Options: (a) describe 8 boxes of one frame each (e.g. Package/Quantity 1 with the box repeated, or the box count on the handling unit) (preferred, because it matches 0.576 m³); (b) one box with dimensions that hold 0.42 m³.
- Needs decision: no

### air/03#F3 · Medium · Instruction to send a bill of lading in an air shipment
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `04-Waybill.xml:/Waybill/cbc:WaybillTypeCode` = `AWB`
- Why: Air cargo travels under an air waybill (`04-Waybill.xml`), not a bill of lading. The instruction is the same text as in the sea flow (`sea/09-ForwardingInstructions.xml`), and it is addressed to the forwarder, telling it to send a document to itself. As written, it asks for a document that does not exist in this flow.
- Condition: the instruction names the transport document of this shipment and a recipient other than the addressee, or is absent.
- Options: (a) remove it (preferred: the waybill goes to the forwarder anyway, see `04-Waybill.xml` ReceiverParty); (b) "Send the air waybill copy to the consignor".
- Needs decision: no

### air/03#F4 · Medium · The instructions do not say where the goods go
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the shipment to the island.`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-05-14`
- Why: A forwarding instruction tells the forwarder what to move, and from and to where. This one has a requested delivery date but no delivery place or address, no destination airport and no delivery terms. The consignee's postal address (Velumi Trading, Reef Street) is the only hint, and the goods actually go to Nalevi Warehousing (`01-OrderChange.xml` DeliveryParty, `06-DespatchAdvice.xml` DeliveryCustomerParty) or, under CPT, to Selanu airport cargo terminal (`01-OrderChange.xml`). The destination is left to be implied by absence.
- Condition: the document states the destination (delivery location or party, or the destination airport and the CPT place) that the forwarder is to deliver to.
- Options: (a) a Delivery with DeliveryLocation (Selanu airport cargo terminal, `XLSLA`) and the CPT term; (b) a Consignment/DeliveryTerms with the place. Either is fine.
- Needs decision: no

### air/03#F5 · Medium · LocaleCode holds a language code
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code. The same pattern occurs in 213 example files.
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/03#F6 · Low · Packaging weight too low for a skid, eight boxes and eight bags
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetNetWeightMeasure` = `76`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cbc:TransportHandlingUnitTypeCode` = `SI`
- Why: Shipment gross weight is "the weight of the goods plus packaging plus transport equipment". 81.6 − 76 = 5.6 kg is left for a skid, the boxes (8 boxes of 0.8 × 0.3 × 0.3 m if F2 is resolved that way) and 8 bags. From my own knowledge, a corrugated box of that size weighs about 0.5–0.7 kg (4–5.6 kg for eight), and a wooden skid that carries them weighs another 5–15 kg. The gross weight looks like goods plus boxes only.
- Condition: gross minus net weight covers the skid, boxes and bags at plausible tare weights, here and in the waybill (`04-Waybill.xml`, same 81.6 kg).
- Options: raise the gross weight (and the chargeable weight and invoice where they follow from it), or state a light skid explicitly.
- Needs decision: no

### air/03#F7 · Low · A transport event with no type and no place
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceTime` = `19:00:00`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:CompletionIndicator` = `false`
- Why: The event has a date, a time and "not completed", but no TransportEventTypeCode, description or location. A reader cannot tell whether 13 May 19:00 is a cut-off, a pickup or a flight. The flight in `04-Waybill.xml` is on 14 May 07:00, and the pickup and despatch are requested for 12 and 13 May.
- Condition: the event says what it is (type code or description) and where, or is absent.
- Options: (a) type it (e.g. the cargo acceptance cut-off at Lumeport airport) (preferred, if that is the intent); (b) remove it.
- Needs decision: no

### air/03#F8 · Low · Shipping order number is the shipment ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- Why: ShippingOrderID is a "Reference number to identify a Shipping Order", the order for transport, while Shipment/ID identifies the goods. Using one number for both is possible but makes the two indistinguishable. Later documents also put the consignment ID `LD-CS-26-0324` in ShippingOrderID (`04-Waybill.xml`, `05-TransportationStatus.xml`, `09-TransportationStatus.xml`), so the shipping order number of this shipment is not settled.
- Condition: the shipping order has one identifier that is not another object's ID, and the flow uses it consistently.
- Options: (a) a separate shipping order number (or this FI's own ID `LD-FI-26-0322`, which UBL's Waybill definition of ShippingOrderID allows: "Shipping Order or Forwarding Instruction"); (b) keep it and align the other documents to `LD-SH-26-0323`.
- Needs decision: no

### air/03#F9 · Low · Exchange rate without any amount in the target currency
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The document has amounts only in XBL (declared values 512.00). Nothing in it is converted to Coral, and the forwarder has no instruction that would need the rate (the import declaration, if any, belongs to the island side). It has no date either, so it does not say when the rate applies.
- Condition: the exchange rate is absent, or the document says what it is used for and carries its date.
- Options: (a) remove it (preferred); (b) keep it with a date and a stated use (e.g. customs value in XLC for the import).
- Needs decision: no

### air/03#F10 · Low · Distribution list names only the addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: DocumentDistribution is "A list of interested parties to whom this document is distributed". The only entry is the forwarder, who is the addressee already (FreightForwarderParty). The entry adds nothing.
- Condition: DocumentDistribution lists parties other than the addressee, or is absent.
- Options: remove it, or add a real copy recipient (e.g. the buyer, if it gets a copy).
- Needs decision: no

### air/03#F11 · Low · The consignee's contact does not fit receiving goods
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: A consignee's contact is the person who takes delivery or arranges it. Here it is "Purchasing", a customer service officer in Sales. Name, title and department contradict each other and the role (52 files carry this combination).
- Condition: the consignee's contact fits receiving goods, with name, title and department in agreement.
- Options: e.g. an import or goods-receiving contact.
- Needs decision: no

## Checked and consistent
- Shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross 81.6 kg, net 76 kg, net volume 0.42 m³ and declared value 512.00 XBL are the same in `02-OrderResponse.xml`, `04-Waybill.xml` and `06-DespatchAdvice.xml`. The declared value equals the goods value 8 × 64 = 512.00 of `01-OrderChange.xml`.
- SSCC `095206103190000015` (check digit OK) carries Lumeway's GS1 company prefix 9520610, the same as its GLN 9520610900008. The 952 prefix is GS1's demonstration range.
- Weight per frame 76 / 8 = 9.5 kg, i.e. about 1.3 dm³ of cast iron at 7.2 kg/dm³ (own knowledge). It fits inside an envelope of 0.0525 m³ per frame (0.42 / 8), as expected for an open frame casting.
- Pickup by Bayforth (earliest 12 May), despatch requested 13 May, delivery 14 May: in order, and the issue date (12 May) is not later than the earliest pickup.
- Parties: Lumeway (consignor), Bayforth (forwarder) and Velumi (consignee) have the same identifiers and legal data as in the other examples of the flow.

## Considered and refuted
- `/ForwardingInstructions/cbc:AdValoremIndicator` = `false`: suspected to contradict the declared value for carriage. Refuted because UBL defines the indicator by ad valorem *duties* ("levied on commodities at certain rates per centum on their value"), not by the carrier's valuation charge. See `04-Waybill.xml`, where the same indicator is `true`; that contradiction is recorded there.
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `false`: an air waybill is never to order. Refuted because `false` is correct, and stating it tells the forwarder that a straight consignment is wanted.
- `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`: against "the forwarder is booked" in `02-OrderResponse.xml`. Refuted because confirming a booking that was made on a quote is normal practice.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredStatisticsValueAmount` = `512.00`: a statistical value in a forwarding instruction. Refuted because the forwarder may lodge the export declaration and needs the value for it.
