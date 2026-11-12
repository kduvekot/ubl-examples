# LLM review: 02-ForwardingInstructions.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/02-ForwardingInstructions.xml`, Git blob `2697645dcfc391cd36edbe8e8ed4c28f35be7a85` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/02#F1 · Medium · Forwarding instructions that do not say where, how or when to forward
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SE-SH-26-0715`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- Why: Forwarding Instructions is "a document issued to a forwarder, giving instructions regarding
  the action to be taken for the forwarding of goods described therein". Apart from the consignee
  party, the document gives no destination or delivery location, no mode or routing (no
  ShipmentStage, no transport mode; air only appears indirectly through "cargo aircraft only"), no
  requested pickup or delivery date, no Incoterms or freight payment instruction, and no reference
  to the order ST-PO-26-0713 it executes. The forwarder cannot act on it without asking.
- Condition: the instructions state at least the destination (place or airport), the mode or
  service wanted, the delivery terms or who pays the freight, and a date (pickup or wanted
  delivery).
- Options: (a, preferred) add a Delivery (or destination location) and a MainCarriageShipmentStage
  with mode 4 and the wanted dates, DeliveryTerms CPT as in the order, and a reference to the order;
  (b) at least destination and mode.
- Needs decision: no

### mast/02#F2 · Medium · Placard notation 7 on an excepted package that carries no label
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: UN 2911 excepted packages carry no class 7 label or placard (own knowledge: SSR-6, IATA DGR);
  the item's own text says so, the placard notation says otherwise.
- Condition: no placard notation for the UN 2911 item.
- Options: (a, preferred) drop it; the class is in HazardClassID.
- Needs decision: no

### mast/02#F3 · Medium · Language codes in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` with listID
  ISO 639 is the language again, not a locale. 213 examples carry it.
- Condition: LocaleCode is a locale (e.g. en-XB) from a locale list, or absent.
- Options: (a, preferred) `en-XB`; (b) drop it.
- Needs decision: no

### mast/02#F4 · Low · Each lithium-battery crate exceeds the cargo-aircraft limit of PI 965 IA
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:Quantity` = `6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:HazardousGoodsTransit/cbc:PackingCriteriaCode` = `PI965IA`
- Why: Six crates of one battery each, 348 kg gross: 58 kg per crate (52 kg net per 4.8 kWh pack,
  about 92 Wh/kg with a steel case, plausible). IATA Packing Instruction 965 Section IA allows at
  most 35 kg gross per package on cargo aircraft (own knowledge); heavier batteries need the
  approval of the State of Origin under special provision A99. The document gives neither a
  lighter packing nor an approval.
- Condition: either each package is within the limit of the packing instruction stated, or the
  approval that allows more is referenced.
- Options: (a, preferred) reference an A99 approval (e.g. as a document reference or in the
  transit description); (b) change weights or packing; (c) if the world's air rules differ, record
  that.
- Needs decision: yes (dangerous-goods story)

### mast/02#F5 · Low · Stowage positions on board in the shipper's instructions
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-2`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: PositionOnBoardStowage is "the place on board a transport means where the hazardous item is
  stowed". When the consignor instructs its forwarder (2026-06-03), no flight is booked and the
  stowage on the aircraft is decided later by the carrier's load planning; the instructions name no
  aircraft either.
- Condition: the forwarding instructions do not state the actual stowage position on board, or
  state only a requirement (e.g. "accessible").
- Options: (a, preferred) drop the positions here; keep them in the waybill or a load document if
  anywhere; (b) phrase a stowage requirement instead.
- Needs decision: no

### mast/02#F6 · Low · Road and sea data, and negatives without a reason, for an air shipment
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:TransportEmergencyCardCode` = `TEC9`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:InhalationToxicityZoneCode` = `NOTTOXIC`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AnimalFoodApprovedIndicator` = `false`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure` = `60`
- Why: Orange plates, ADR tunnel codes and road emergency cards apply to road (and rail) vehicles;
  the goods are packed in air ULDs for a cargo-aircraft flight. The inhalation-toxicity zone is
  defined only for substances toxic by inhalation; "not toxic" for a battery states nothing. Food
  approval of the container is irrelevant to batteries. An emergency temperature applies to
  temperature-controlled self-reactive substances and organic peroxides (own knowledge), not to
  lithium batteries. The same HazardousGoodsTransit block is repeated three times (equipment,
  loaded item, handling unit). These values have no business reason in the document (IND5).
- Condition: every dangerous-goods element present applies to the mode and the goods of this
  shipment.
- Options: (a, preferred) drop the road-only and negative values and keep the transit data once,
  where it applies; (b) keep the pre-carriage by road, if there is one, in its own stage with its
  road data.
- Needs decision: yes (affects coverage)

### mast/02#F7 · Low · Two ULDs of the same kind coded differently
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `AM`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- Why: RKN41207K0 is, by its IATA ULD type code RKN, a temperature-controlled LD3-size air
  container; AKE20514K0 is an LD3. Both are ULDs; one is coded "Refrigerated container" (a code used
  for sea/land reefers), the other "ULD". The RKN's air-flow and humidity settings belong to
  ventilated reefers rather than to an RKN.
- Condition: both ULDs are coded as ULDs (the temperature control given by the refrigeration
  elements), or the choice of AM is explained.
- Options: (a, preferred) UL for both, with RefrigeratedIndicator for the RKN; (b) keep AM.
- Needs decision: no

### mast/02#F8 · Low · Activity of the americium sources: per detector or for the set?
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: 37 kBq is the typical activity of one detector; the item is a set of ten (370 kBq). The
  parent's UBL definition (fission chain reaction) does not fit Am-241 detectors at all (model
  defect).
- Condition: the activity is that of the set, or the text says per detector.
- Options: (a, preferred) 370 kBq; (b) a note.
- Needs decision: no

### mast/02#F9 · Low · Contacts that do not fit the roles
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Business accounts`
- Why: The consignor's contact for a dangerous-goods shipment is its procurement office; the
  consignee's is a sales desk. A consignor's contact ships goods, a consignee's contact receives
  them (and for dangerous goods should be reachable when they arrive).
- Condition: consignor and consignee contacts are shipping and goods-receiving functions.
- Options: (a, preferred) role-specific contacts; (b) drop them.
- Needs decision: no

### mast/02#F10 · Low · Lisavan address renderings tagged en-XB
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- Why: The same address of Selanu Telecom is tagged `en-XB` here (the issuer's country) and `en-XL`
  in 01 and 03.
- Condition: the same address carries the same language tags in every example.
- Options: (a, preferred) tag by the address's own country (en-XL).
- Needs decision: yes (the world's language convention)

### mast/02#F11 · Low · A mast operator classified as a wired telecom
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120); see the review of 01.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes

## Checked and consistent
- Shipment gross weight 376 kg = 348 (batteries) + 3 (detectors) + 25 (stripper), the same in 03
  and 04.
- Stripper: 20 L at about 0.95 kg/L = 19 kg plus four 5-L cans ≈ 1–1.5 kg each gives 23–25 kg;
  5 L per inner can is within the cargo-aircraft limit for UN 2920 PG II (30 L), not the passenger
  limit (1 L), which matches the cargo-aircraft flight of 03 (own knowledge).
- Batteries: 312 kg net / 6 = 52 kg; 0.24 m³ / 6 = 0.04 m³ per pack (≈ 1300 kg/m³), plausible for
  a 4.8 kWh pack in a steel case. State of charge ≤ 30 % as PI 965 requires.
- Segregation: the class 8 (3) cans and the lithium batteries are in different ULDs at different
  positions, as IATA segregation between UN 3480 and class 3 requires (own knowledge).
- Shipment and consignment IDs agree with 03 and 04; items and DG data agree with 01.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode`:
  temperature control for batteries suspected pointless — refuted: keeping lithium batteries
  between 5 and 35 °C on a flight to a warm island is a plausible reason; the coding is F7.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty`: the
  consignor as party to notify — refuted: the shipper is the usual emergency contact.

## Outside this review
- Whether an RKN and an AKE fit the ATR 72 freighter named in 03, and at main-deck positions MD-2
  and MD-6, is a capacity question.
