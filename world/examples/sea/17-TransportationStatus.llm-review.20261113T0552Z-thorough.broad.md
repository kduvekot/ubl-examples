# LLM review: 17-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/17-TransportationStatus.xml`, Git blob `ca6268e2b075e6b8011b2c7aa08d386ab1c51391` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/17#F1 · High · Shipping order ID is the consignment ID; the bill of lading names another shipping order
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- Why: `ShippingOrderID` is "A reference number for a shipping order." The value is the consignment identifier of the same document (`Consignment/ID`), i.e. an identifier of another kind. The bill of lading referenced by this status (`TOL-BL-26-0139`) gives the shipping order of this consignment as `BF-FI-26-0137` (the forwarder's instructions, `12-ForwardingInstructions.xml`), so the two examples contradict each other on the shipping order. (`13-TransportationStatus.xml` uses the same consignment ID as shipping order.)
- Condition: `ShippingOrderID` holds the shipping order of the consignment, the same as in `14-BillOfLading.xml`, or is absent.
- Options: (a) preferred: `BF-FI-26-0137`, as on the bill of lading; (b) drop the element, the consignment and B/L reference already identify the shipment.
- Needs decision: no

### sea/17#F2 · Medium · Detention event of the transport means describes a pallet rule
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:OccurrenceTime` = `12:00:00`
- XPath: `28-DebitNote.xml:/DebitNote/cac:DiscrepancyResponse/cbc:Description` = `Heat-treatment mark illegible on pallet 095206101230000070.`
- Why: `DetentionTransportEvent` in a shipment stage is "The detention of a transport means during loading and unloading operations." What the flow tells (`28-DebitNote.xml`) is that one pallet's heat-treatment mark was illegible and the container was inspected by customs; the vessel was not detained. The description states a general import rule instead of what happened, and the event sits on the stage (the ship) rather than on the container, where the quarantine event already is.
- Condition: The event that holds the container is on the container (`TransportEquipment`) and its description states what happened (mark illegible on the named pallet, container held for inspection); no detention of the transport means is reported unless the ship was detained.
- Options: (a) preferred: drop the stage-level detention and give the container's event (quarantine or an additional event) a description of the illegible mark and the hold; (b) keep a detention event but move it to the equipment and describe the hold.
- Needs decision: no

### sea/17#F3 · Low · Container events without type, description or reason
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:OccurrenceTime` = `11:40:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: The additional container event at 11:40 has only a date and time: no type code, no description, no location, so the receiver cannot tell what happened. The quarantine event gives no reason or place; it can only be linked to the pallet problem through `28-DebitNote.xml`.
- Condition: Every event carries what it is (type or description) and the quarantine says why and where.
- Options: describe the 11:40 event (e.g. "moved to the customs inspection area") or drop it; give the quarantine a description and location.
- Needs decision: no

### sea/17#F4 · Low · Consignee contact named Purchasing, working in Sales as customer service officer
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Name, job title and department contradict one another (a purchasing function in a sales department), and for a consignee the contact should be the one who receives goods (goods inwards / import desk), not purchasing.
- Condition: Name, job title and department of the contact agree, and the consignee's contact fits receiving goods.
- Options: a goods-receiving contact of Velumi Trading; or make name, title and department agree (e.g. Purchasing / Buyer / Purchasing).
- Needs decision: no

## Checked and consistent
- Reference `TOL-BL-26-0139` resolves to `14-BillOfLading.xml`, same consignment `LD-CS-26-0133`, container `TWLU4120872` (ISO 6346 check digit OK), carrier Tidewell Ocean Lines and consignee Velumi Trading.
- Timeline within the document: arrival 06:30, discharge 11:20 (completed), container event 11:40, detention 12:00, quarantine 15:00 (completed), issue 16:36; all before the issue time. Arrival agrees with the requested arrival 06:00 at the fairway buoy in `16-CommonTransportationReport.xml`.
- Terminal handling charge `HD` 185.00 XBL "Terminal handling at Selanu" agrees with the bill of lading's charge of 185.00 XBL collect from the consignee.
- Port of Selanu's address, coordinates and UN/LOCODE `XLSEL` agree with `16-CommonTransportationReport.xml`.
- Notes in Lisavan (`qal`) and English (`en-XL`) are tagged.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount` = `185.00`: a Lisavu port charging in Bayvarra's Lume (XBL) rather than XLC — refuted because the bill of lading fixes the charge in XBL and the Trade Accord parties trade in Lume.
- `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`: the import-side status goes to the forwarder's export desk — refuted: Bayforth booked the export and follows the shipment to delivery; its export desk is its single shipment contact.
- `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Port of Selanu`: name without UN/LOCODE — refuted as a finding; the terminal operator's physical location in the same document carries `XLSEL`.
- `/TransportationStatus/cbc:Description` = `Container TWLU4120872 discharged and available for customs clearance.`: "available" despite quarantine — refuted: the quarantine event is completed (15:00) before the issue time.

## Outside this review
- `13-TransportationStatus.xml` also uses the consignment ID as `ShippingOrderID`; belongs to that example's review.
