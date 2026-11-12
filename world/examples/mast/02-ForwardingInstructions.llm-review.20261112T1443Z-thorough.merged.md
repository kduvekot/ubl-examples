# LLM review: 02-ForwardingInstructions.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/02-ForwardingInstructions.xml`, Git blob `2697645dcfc391cd36edbe8e8ed4c28f35be7a85` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8533627 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all five parts
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/02#F1 · High · The hazardous item's package holds six batteries, the handling unit six crates of one
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:Quantity` = `6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:PackagingTypeCode` = `CR`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[1]/cbc:Quantity` = `1`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[6]/cbc:Quantity` = `1`
- Why: Package/Quantity is "The quantity of items contained in this package", and the hazardous item
  has at most one Package ("The Package details for this Hazardous Item", 0..1). Under the loaded
  hazardous item it thus says one crate containing six batteries; the handling unit lists six crates
  SE-CR-1 to SE-CR-6 with one battery each. Both cannot be true. The physics favour one battery per
  crate: one battery weighs 312 / 6 = 52 kg net, so a single crate with six would weigh 348 kg, far
  above the per-package limit (F5). The same pair occurs in the waybill (03).
- Condition: the package description under the hazardous item agrees with the handling unit's
  packages (six crates of one battery each).
- Options: (a, preferred) describe the hazardous item's package as one battery per crate (Quantity 1)
  and leave the six crates to LoadedHazardousItem/Quantity and the handling unit; (b) drop the
  Package from the hazardous item, since the handling unit already lists the crates.
- Needs decision: no
- From: logistics (F1)

### mast/02#F2 · Medium · Language codes in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  ISO 639 repeats the language code of Language/ID and names no locale (a language in a region, e.g.
  English as used in Bayvarra). Section 6 names this case as Medium. The same value occurs in 213
  examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: LocaleCode is absent, or holds a locale (language plus territory, e.g. `en-XB`) from a
  locale list, with a matching listID.
- Options: (a) `en-XB` with a locale list such as BCP 47 (preferred by broad and parties); (b) remove
  it, since nothing in the document depends on a locale (preferred by context).
- Needs decision: no
- From: broad (F3), parties (F3), context (F5)

### mast/02#F3 · Medium · Forwarding instructions that do not say where, when or how to forward
- XPath: `/ForwardingInstructions/cbc:IssueDate` = `2026-06-03`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SE-SH-26-0715`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:HazardousGoodsTransit/cbc:TransportAuthorizationCode` = `CAO`
- Why: Forwarding Instructions is "A document issued to a forwarder, giving instructions regarding the
  action to be taken for the forwarding of goods described therein". The document describes the goods
  in detail but gives no instruction: no place or date of collection, no destination location or
  airport, no requested departure or delivery date, no shipment stage, mode or service (air carriage
  is only implied by the cargo-aircraft-only code), no delivery terms or freight payment, no
  OtherInstruction and no reference to the order it executes. The order agreed CPT to the mast site
  (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CPT`), so the forwarder must arrange carriage
  beyond the airport, which neither this document nor the waybill (main carriage only) shows. The
  consignee's address is the only hint where the goods go. The document's purpose depends on this
  information.
- Condition: the instructions state at least where and when the goods are to be collected, where
  they are to be delivered (place or airport, and the mast site), the requested mode or service, and
  the delivery terms or who pays the freight.
- Options: (a, preferred) add the stages (pre-carriage, main carriage with mode 4, on-carriage) or a
  Delivery with requested period and location, the CPT delivery terms as in the order, and a
  reference to the order; (b) at least destination, mode and a date, e.g. in OtherInstruction.
- Needs decision: no
- From: broad (F1), logistics (F2), context (F2)

### mast/02#F4 · Medium · Shipment gross weight leaves out the transport equipment
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `376`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:GrossWeightMeasure` = `3`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:GrossWeightMeasure` = `25`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods
  plus packaging plus transport equipment". 348 + 3 + 25 = 376 kg (redone in the merge): goods and
  packaging only, whereas the loaded items' own weights are defined as "excluding the transport
  equipment". The shipment travels in two ULDs listed in the same document, an active RKN
  (RKN41207K0) and an AKE (AKE20514K0), whose tares (own knowledge: an AKE about 70–80 kg, an
  active RKN several hundred kilograms) are not included. The same 376 kg is used in 03 and 04.
- Condition: the shipment gross weight includes the tare of the listed transport equipment, or the
  376 kg is given in an element whose definition excludes the equipment.
- Options: (a, preferred) put 376 kg on Consignment/GrossWeightMeasure (which excludes the carrier's
  equipment) and give the shipment weight with tare or leave it out; (b) add the ULD tares.
- Needs decision: no
- From: logistics (F3); broad listed 376 = 348 + 3 + 25 as consistent

### mast/02#F5 · Medium · Battery crates exceed the cargo-aircraft limit of PI 965 Section IA
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:HazardousGoodsTransit/cbc:PackingCriteriaCode` = `PI965IA`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:NetWeightMeasure` = `312`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:Quantity` = `6`
- Why: From the document: 348 kg gross / 6 crates = 58 kg per crate; one battery alone weighs
  312 / 6 = 52 kg. IATA PI 965 Section IA allows at most 35 kg gross per package on cargo aircraft;
  heavier batteries need the approval of the State of Origin under special provision A99, which
  travels with the shipment (own knowledge). The document states CAO and PI 965 IA but no approval,
  so the declared packing does not permit what is packed. (Read as in F1, one crate of 348 kg, the
  excess is larger still.)
- Condition: either each package is within 35 kg gross, or the document carries the A99 approval
  (reference and description) that permits the heavier packages.
- Options: (a, preferred) reference an A99 approval of Bayvarra's aviation authority (a document
  reference and the transit description), because the battery size is part of the story; (b)
  smaller battery modules within 35 kg; (c) if the world's air rules differ, record that.
- Needs decision: yes
- From: broad (F4, Low), logistics (F4)

### mast/02#F6 · Medium · Numbered orange plates for packaged goods carried by air
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- Why: Upper/LowerOrangeHazardPlacardID are "The number for the upper/lower part of the orange hazard
  placard required on the means of transport". Orange plates are an ADR/RID requirement for road
  vehicles and rail wagons; for goods in packages ADR 5.3.2.1.1 requires plain plates without numbers,
  numbered plates only for tanks and bulk (own knowledge). The batteries travel packed in a ULD on a
  cargo aircraft, and no means of transport in this flow requires the numbers 90/3480, so the
  condition of the definition is not met. The numbers themselves are right for UN 3480. The same
  values are in 03.
- Condition: orange-plate numbers are given only where the means of transport requires numbered
  orange plates.
- Options: (a, preferred) remove both elements; (b) a road pre-carriage would still not need numbers
  for packages; mention plain plates in text if needed.
- Needs decision: no
- From: context (F3), logistics (F7, Low), broad (part of F6)

### mast/02#F7 · Medium · Temperature code given next to a measured value
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Temperature/cbc:MeasureCode` = `TARGET`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Temperature/cbc:MeasureCode` = `TARGET`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[3]/cac:Temperature/cbc:MeasureCode` = `TARGET`
- Why: MeasureCode is "A code describing the temperature, when not expressed as a measure". Each of
  these Temperatures also has a Measure (20 °C), so the condition of the definition is not met; the
  code is used as a qualifier ("this measure is a target") rather than as a description of a
  temperature without a measure (such as "ambient" or "frozen"). This list is used in one other
  example (`grep -rl --include='*.xml' TemperatureQualifierCode world/examples`: this file and
  plastics/09-ImportCustomsDeclaration.xml).
- Condition: MeasureCode is present only in a Temperature that has no Measure.
- Options: (a, preferred) remove MeasureCode and say "target transport temperature" through
  AttributeID or Description; (b) use MeasureCode alone if a coded temperature is meant.
- Needs decision: no
- From: context (F4)

### mast/02#F8 · Medium · Placard notation 7 for an excepted package that carries no label and no placard
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "Text of the placard notation corresponding to the hazard class of this
  hazardous item" (or the upper number of the orange plate). UN 2911 is an excepted package: no class
  7 label, and vehicles, containers or ULDs carrying only excepted packages are not placarded; only
  the UN number is marked (own knowledge: SSR-6, ADR 1.7.1.5/5.1.5.4, IATA DGR). The item's own text
  says so. The same value is in 01, 04 and 05.
- Condition: no placard notation is given for the UN 2911 item, and the HazardousItem agrees with its
  own AdditionalInformation.
- Options: (a, preferred) remove PlacardNotation for this item; the class is in HazardClassID; (b) a
  real placard would mean the item is not an excepted package, which changes UN number and story.
- Needs decision: no
- From: broad (F2), logistics (F5), context (F1, as High)

### mast/02#F9 · Medium · Fissile-contents aggregate used for a non-fissile americium source
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: ApplicableRadioactiveIsotope is "The maximum activity of the radioactive contents capable of
  sustaining a nuclear fission chain reaction during carriage". Americium-241 is not fissile (the
  fissile nuclides of the transport regulations are U-233, U-235, Pu-239, Pu-241; IAEA SSR-6, own
  knowledge). The aggregate is also the only place in UBL for a nuclide and its activity, so the
  definition looks defective; that does not lower the severity under the semantic-conformance rule,
  but makes the case a candidate for the TC findings. Same as mast/01#F3.
- Condition: either ApplicableRadioactiveIsotope is used only for fissile contents, or the use is
  recorded in `analysis/codelist-decisions.md` as a finding about a defective UBL definition.
- Options: (a) remove it and state nuclide and activity in the RadioactiveMaterial name or
  description (preferred by context); (b) keep it and record the definition defect for the TC
  write-up (preferred by logistics).
- Needs decision: yes
- From: logistics (F12, Low), context (F6), broad (part of F8)

### mast/02#F10 · Low · Consignor's and consignee's contacts do not fit the transport roles
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: In forwarding instructions the consignor's contact arranges the despatch (shipping or
  logistics) and the consignee's contact receives the goods and, for dangerous goods, should be
  reachable when they arrive. Here they are Saltmere's procurement "Bids office" and Selanu
  Telecom's sales desk for business customers. Same contacts as in mast/01#F9.
- Condition: the consignor's contact handles despatch, and the consignee's contact receives goods
  (stores, site or goods-in).
- Options: (a, preferred) role-specific contacts; (b) drop them.
- Needs decision: no
- From: broad (F9), parties (F4)

### mast/02#F11 · Low · Freight forwarder role defined by UBL as a consolidator, but nothing is consolidated
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `03-Waybill.xml:/Waybill/cbc:ConsolidatedIndicator` = `false`
- Why: UBL defines FreightForwarderParty as "The Party who combines individual smaller consignments
  into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a
  counterpart who mirrors the consolidator's activity by dividing the consolidated consignment into
  its original components." Bayforth does not consolidate: one consignor, one consignment, and the
  waybill is not consolidated. Against that, Forwarding Instructions are by definition "issued to a
  forwarder" and this is the document's only element for that party (parties refuted the finding on
  this ground). The merge could not settle whether this is a misuse or a too-narrow UBL definition.
- Condition: either FreightForwarderParty is used for a party that consolidates, or the use for a
  non-consolidating forwarder is recorded as a deliberate reading (finding on the UBL definition).
- Options: (a, preferred) keep the role and record the narrow definition for the TC write-up;
  (b) make the shipment a consolidation, which changes the story.
- Needs decision: yes
- From: context (F9); refuted by parties (see Considered and refuted)

### mast/02#F12 · Low · Registration date 1 January 1996 shared by many companies
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date is the registration date of about 25 companies in 181 examples
  (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`); it reads
  as a default, not as each company's history (no fillers). Same as mast/01#F12.
- Condition: each company's registration date is its own, or absent.
- Options: (a, preferred) dates from the company histories; (b) drop them.
- Needs decision: yes
- From: parties (F6)

### mast/02#F13 · Low · A mast operator classified as wired telecommunications
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120); 6110 is wired telecommunications. See mast/01#F10.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep 6110 if the world says so.
- Needs decision: yes
- From: broad (F11)

### mast/02#F14 · Low · Selanu Telecom described differently than in the order and the waybill
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: In 01 and 03 Selanu Telecom's English address renderings (street, city, registration city)
  are tagged `en-XL` and its legal form is given in Lisavan and English, each with its languageID;
  here the English renderings are tagged `en-XB` and the legal form has one rendering without
  languageID. The same holds in 04 and 05. The tags follow the issuer's country (01 and 03 are
  issued by island parties, 02, 04, 05 by Saltmere), which may be a deliberate convention; the merge
  could not settle that. The same party should otherwise be described the same way in every example.
- Condition: Selanu Telecom's legal form and address renderings carry the same languageIDs in every
  example of the flow, or the world's convention (tag by issuer) is recorded.
- Options: (a, preferred) both legal-form renderings with their tags, and the English address
  renderings tagged by the address's country (en-XL), everywhere; (b) record the issuer convention.
- Needs decision: yes
- From: broad (F10), parties (F5)

### mast/02#F15 · Low · The consignor named as the party to be notified of its own dangerous goods
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: HazardousItemNotificationParty is "The Party who is notified of a Hazardous Item in this
  Consignment". Saltmere is the consignor that declares the goods in these instructions; it gives the
  notification and needs none. A party to be notified would be one that does not already know: the
  consignee (who receives batteries, a radioactive excepted package and a corrosive liquid), the
  destination handler, or an authority. Saltmere's emergency role is already carried by
  LoadedHazardousItem/ContactParty. Against that, broad read the element as the party notified in
  case of an incident, for which the shipper is the usual party. The merge could not settle which
  reading the definition intends. The same occurs in 03; these are the only two examples with the
  element (`grep -rl --include='*.xml' HazardousItemNotificationParty world/examples`).
- Condition: the HazardousItemNotificationParty is a party that has to be told about the goods and
  is not their consignor, or the element is absent, or the incident reading is confirmed.
- Options: (a, preferred) the consignee Selanu Telecom (or the destination ground handler), which
  must prepare to receive them; (b) remove it, since the consignor is already the emergency contact.
- Needs decision: yes
- From: parties (F1, Medium), context (F8); refuted by broad (see Considered and refuted)

### mast/02#F16 · Low · Carrier's ULD numbers and on-board positions in the consignor's instructions
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `RKN41207K0`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cbc:ID` = `AKE20514K0`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-2`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: PositionOnBoardStowage is "A stowage indicating where to find this hazardous item" on board.
  The consignor issues these instructions on 2026-06-03, a day before the air waybill, and names no
  carrier, flight or aircraft. ULD serial numbers (owner code "K0") and main-deck positions are
  assigned by the carrier or its handling agent at build-up and load planning (own knowledge); they
  are the carrier's data of the waybill (03) copied back into the consignor's instructions. If the
  consignor means a requirement ("accessible"), that is an instruction, not a position.
- Condition: the instructions contain only what the consignor can know when it issues them (e.g. a
  request for a temperature-controlled container, a stowage requirement), not the carrier's
  equipment numbers and stowage positions.
- Options: (a, preferred) remove ULD IDs and positions here (keep them in 03) and state the
  equipment and stowage requirement instead (HandlingInstructions or TransitDescription); (b) if the
  consignor had pre-booked, add the booking (carrier, CarrierAssignedID) that explains the numbers.
- Needs decision: no
- From: broad (F5), logistics (F6), context (F7)

### mast/02#F17 · Low · Reefer settings, food approvals, road data and negatives without a reason
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AirFlowPercent` = `40`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumidityPercent` = `50`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AnimalFoodApprovedIndicator` = `false`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumanFoodApprovedIndicator` = `false`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:TransportEmergencyCardCode` = `TEC9`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:InhalationToxicityZoneCode` = `NOTTOXIC`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- Why: The 5–35 °C range has a reason for lithium-ion batteries, but air-flow and humidity settings
  (relevant to perishables) and the statement that the unit is not approved for animal or human food
  have none: no food is carried, and "not approved" says only what absence would say. Road emergency
  cards and ADR tunnel codes apply to road vehicles; the goods are packed in air ULDs for a
  cargo-aircraft flight and no road leg is given. The inhalation-toxicity zone is defined only for
  substances toxic by inhalation; "not toxic" for a battery states nothing. The same
  HazardousGoodsTransit block is repeated three times (equipment, loaded item, handling unit). These
  values have no business reason in the document (IND5/IND6).
- Condition: every reefer setting, approval indicator and dangerous-goods element present applies to
  the mode and the goods of this shipment, and the transit data is given once where it applies.
- Options: (a, preferred) remove the food indicators, the air-flow and humidity settings, the
  road-only and negative values, and keep the transit data once; (b) keep a value with a stated
  reason (e.g. a humidity limit for the batteries, or a road pre-carriage in its own stage).
- Needs decision: no
- From: broad (F6, without the orange plates, now F6, and the emergency temperature, refuted in the
  merge), context (F10)

### mast/02#F18 · Low · Packaging danger level "4" under the UN/EDIFACT 8339 list ID
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:PackagingDangerLevelCode` = `4`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:PackagingDangerLevelCode` = `4`
- Why: To the reviewers' knowledge UN/EDIFACT 8339 (Packaging danger level) has only the codes 1, 2
  and 3 (great, medium, minor danger). The world's copy of the list (`UNCL8339Code.gc`, "UN/EDIFACT
  8339 Packaging danger level (UBL example world)", agency UN/CEFACT) adds "4 Not assigned". If the
  official directory has no code 4, a world-made code is published under a real list ID. Neither
  logistics nor the merge could check the official directory (UNECE blocks automated access). Code 4
  occurs only in 02 and 03 (`grep -rl --include='*.xml' 'EDED 8339">4<' world/examples`).
- Condition: every code given with `listID="UN/EDIFACT EDED 8339"` is in the official 8339 list; for
  entries without packing group the element is omitted or uses a world list.
- Options: (a, preferred) omit the element for UN 3480 and UN 2911 (no packing group); (b) keep "4"
  only if the official directory has it.
- Needs decision: yes
- From: logistics (F8)

### mast/02#F19 · Low · The emergency contact party has no means of contact
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:ContactParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: ContactParty is "The individual, group, or body who is contacted in case of a hazardous
  incident associated with this item". It carries only Saltmere's register number and name; the only
  Saltmere contact in the document is the consignor's "Bids office", reachable on weekdays
  08:00–17:00. An emergency contact is useful only if it can be reached during the whole journey (a
  24-hour number is required by several states' rules, own knowledge). The other two loaded
  hazardous items (UN 2911, UN 2920) have no ContactParty at all.
- Condition: a contact party, where given, has a means of contact reachable while the goods are in
  transit, and the items without one are covered by the same contact or say why not.
- Options: (a, preferred) give the ContactParty a Contact with a 24-hour emergency number (Saltmere's
  or an emergency response provider's) and use it for all three items; (b) drop ContactParty if the
  world does not model emergency response.
- Needs decision: no
- From: parties (F2, Medium)

### mast/02#F20 · Low · Cargo-aircraft-only liquid in a closed AKE without CAO data
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:Quantity` = `20`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: UN 2920 PG II in 5-litre cans exceeds the passenger-aircraft limit (PI 851: 1 L) and may fly
  only on cargo aircraft (PI 855: 30 L) (own knowledge). Cargo-aircraft-only packages of class 8 must
  be loaded so that the crew can reach them in flight; a closed AKE container is not accessible. The
  battery equipment carries CAO, a packing instruction and "Main deck, accessible", but the AKE with
  the corrosive liquid carries no transit data, no packing instruction and no accessibility statement.
- Condition: the UN 2920 cans carry their CAO status and packing instruction, and their stowage allows
  crew access (or the document says how the requirement is met).
- Options: (a, preferred) give the AKE's hazardous item its own HazardousGoodsTransit (PI 855, CAO)
  and stow the cans accessibly; (b) pack the liquid in inner packagings of at most 1 L.
- Needs decision: yes
- From: logistics (F9)

### mast/02#F21 · Low · Placard endorsement "9A" is the lithium-battery label model
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "Text of the placard endorsement that is to be shown on the shipping
  papers" or the orange plate's lower number. "9A" is the lithium-battery label model for packages;
  the 9A model is not used for placarding and the papers show class 9 (own knowledge). Same as
  mast/01#F5.
- Condition: PlacardEndorsement is absent or holds what the papers or the orange plate show for
  UN 3480; a 9A label, if wanted, is stated as a package label.
- Options: (a, preferred) drop it; (b) `3480` if the orange-plate reading is intended.
- Needs decision: no
- From: logistics (F10)

### mast/02#F22 · Low · Activity of one detector given for the set of ten
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ActivityLevelMeasure is "The measure of the radioactive contents during carriage". The item is
  one set of ten detectors, each with a source; 37 kBq is the usual activity of one detector (own
  knowledge), so the set holds 370 kBq. Both are far below the excepted-package limits. Same as
  mast/01#F4.
- Condition: the activity stated is that of the item as carried (370 kBq), or the text says it is per
  detector.
- Options: (a, preferred) 370 kBq; (b) keep 37 and say "per detector".
- Needs decision: no
- From: broad (F8), logistics (F11), context (part of F6)

### mast/02#F23 · Low · Placard endorsements that only repeat the class (UN 2920)
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[3]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `8`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[3]/cac:Item/cac:HazardousItem/cac:SecondaryHazard/cbc:PlacardEndorsement` = `3`
- Why: The same values as in the order, where broad found them and logistics refuted them
  (mast/01#F6): the endorsement repeats the class of PlacardNotation; under neither reading of the
  definition (an endorsement text on the papers, or the orange plate's lower number, which would be
  2920) is it the class number, in the merge's understanding. No part raised it for this example;
  the merge adds it so that the same values are judged the same way across the flow.
- Condition: PlacardEndorsement is absent or holds an endorsement text or the orange plate's lower
  number, or the owner confirms the class-on-papers reading.
- Options: (a, preferred) drop both; (b) keep them if the reading is accepted.
- Needs decision: yes
- From: merge (as mast/01#F6)

## Checked and consistent
- Shipment total 348 + 3 + 25 = 376 kg (see F4 for the definition), the same in 03 and 04.
- Batteries: 312 kg net / 6 = 52 kg; 4800 Wh / 52 kg = 92 Wh/kg for a pack in a steel case, plausible
  (90–150 Wh/kg at pack level, own knowledge); 0.24 m³ / 6 = 40 L per battery, 1300 kg/m³; packaging
  348 − 312 = 36 kg = 6 kg per crate, light but possible. State of charge below 30 %, CAO and
  PI 965 IA agree with each other.
- AKE contents: detectors 3 kg gross for ten; stripper 20 L at 0.9–1.0 kg/L (propanol 0.80,
  ethanolamine 1.01) = 18–20 kg plus four 5-L cans of about 1 kg = 22–24 kg against 25 kg: plausible.
  Four cans × 5 L = 20 L.
- Equipment capacity (own knowledge): an LD3-size RKN and an AKE each take about 1.5 t gross; 348 kg
  and 28 kg are well within, and 0.24 m³ of batteries fits an RKN interior.
- Temperatures: equipment range 5–35 °C equals the goods items' minimum/maximum; target 20 °C inside;
  emergency temperature 60 °C above the maximum.
- Segregation: the class 8 (3) cans and the lithium batteries are in different ULDs at different
  positions, as required between UN 3480 and class 3 (own knowledge).
- Shipment SE-SH-26-0715, consignment SE-CS-26-0716 and the ULD IDs, weights and positions are the
  same in 03 (and 04); goods items, UN numbers and quantities agree with the order lines of 01;
  DG codes of the goods items as in 01.
- Parties against 01, 03, 04: Saltmere Engineering `20410685`, Bayforth Forwarding `20411644`,
  Selanu Telecom `IC42407`; identifiers, names, address IDs, tax IDs, contacts and endpoints agree
  (apart from F14). Bayforth's tax registration (STT, Coastal State) matches its Lumeport address.
  The consignor is the seller and the consignee the buyer of 01; under CPT the seller instructs the
  forwarder.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode`: temperature control for batteries
  pointless — refuted because keeping lithium batteries between 5 and 35 °C on a flight to a warm
  island is a plausible reason (from broad).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty`: the
  consignor as party to notify — refuted by broad because the shipper is the usual emergency contact;
  the merge could not settle it and kept it as F15 (Needs decision: yes), made by parties and context.
- `/ForwardingInstructions/cac:FreightForwarderParty`: UBL defines the role as a consolidator, while
  Bayforth forwards one unconsolidated consignment — refuted by parties because forwarding
  instructions are "issued to a forwarder" and this is the only element for that party; the merge
  kept it as F11 (Needs decision: yes), made by context.
- `/ForwardingInstructions/cac:FreightForwarderParty/cbc:IndustryClassificationCode`: ISIC 5229 —
  refuted, the class covers freight forwarding (from parties).
- `/ForwardingInstructions/cac:FreightForwarderParty/cac:Contact/cbc:Name`: "Export desk", operations
  planner — refuted, it fits a forwarder handling an export (from parties).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode`: "AM" (refrigerated container) for an
  RKN — refuted because the RKN is an active temperature-controlled container and the indicators
  agree; the second ULD uses the generic UL (from logistics and context; see also Refuted in the
  merge, broad/F7).
- `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:MinimumTemperature/cbc:Measure`: a
  temperature range for goods in the AKE, which cannot control temperature — refuted because the
  range is a requirement on the goods that a heated main deck meets (from logistics).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure`: an
  emergency temperature applies only to self-reactive substances and organic peroxides — refuted
  because the definition ("The threshold temperature at which emergency procedures apply in the
  handling of temperature-controlled goods") is general, the batteries travel in a
  temperature-controlled unit, and 60 °C is a plausible thermal-runaway threshold (from logistics and
  context).

## Refuted in the merge
### broad/F6 (partly) · Low · Emergency temperature for lithium batteries
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure` = `60`
- Broad, as one place of its F6 ("Road and sea data, and negatives without a reason, for an air
  shipment"): an emergency temperature applies to temperature-controlled self-reactive substances
  and organic peroxides (own knowledge), not to lithium batteries; no business reason (IND5).
  Condition: every dangerous-goods element present applies to the mode and the goods.
- Refuted because: UBL's definition is "The threshold temperature at which emergency procedures apply
  in the handling of temperature-controlled goods", not limited to self-reactive substances; the
  batteries are carried in an active temperature-controlled ULD with a 35 °C maximum, and 60 °C is a
  plausible threshold for emergency action against thermal runaway. Logistics and context refuted it
  on the same ground. The other places of broad/F6 are in F6 and F17.

### broad/F7 · Low · Two ULDs of the same kind coded differently
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `AM`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- Broad: RKN41207K0 is by its IATA type code a temperature-controlled LD3-size container, AKE20514K0
  an LD3; both are ULDs, but one is coded "Refrigerated container" (a code used for sea/land reefers),
  the other "ULD"; the RKN's air-flow and humidity settings belong to ventilated reefers. Condition:
  both are coded as ULDs, or the choice of AM is explained. Options: (a) UL for both, with
  RefrigeratedIndicator; (b) keep AM.
- Refuted because: the code's meaning, a refrigerated container, describes the RKN correctly (an
  active temperature-controlled container), and it agrees with RefrigeratedIndicator,
  RefrigerationOnIndicator and PowerIndicator; choosing the more specific code for one ULD and the
  generic one for the other contradicts nothing. Logistics and context refuted it on the same ground.
  The air-flow and humidity settings are kept in F17.

## Changed in the merge
- logistics/F1 → F1: XPaths and wording kept; the 0..1 cardinality of the hazardous item's Package
  added to the Why.
- context/F1 (High) → F8 (Medium): as in mast/01#F1, the text speaks of the label, the contradiction
  rests on the regulations.
- broad/F1, logistics/F2, context/F2 → F3: combined, all XPaths kept.
- broad/F4 (Low) and logistics/F4 (Medium) → F5: Medium, because the stated packing instruction does
  not permit the stated package weights (a value that does not fit its element's meaning).
- context/F3 (Medium), logistics/F7 (Low) and the orange-plate places of broad/F6 → F6: Medium,
  because the definition's condition ("required on the means of transport") is not met.
- logistics/F12 (Low, decision yes) and context/F6 (Medium, decision no) → F9: Medium, decision yes,
  as mast/01#F3; the per-detector part went to F22.
- parties/F1 (Medium) and context/F8 (Low) → F15: Low with Needs decision yes, because broad refuted
  it on a plausible reading of the definition and the merge could neither confirm nor refute it.
- parties/F2 → F19: Medium → Low, because the purpose of forwarding instructions does not depend on
  the emergency contact's telephone number, and a 24-hour number is a state requirement, not a
  general IATA one (own knowledge).
- broad/F5, logistics/F6, context/F7 → F16: combined, with logistics' ULD IDs and context's third
  position.
- broad/F6 → split: orange plates to F6, emergency temperature to "Refuted in the merge", the rest
  merged with context/F10 into F17; Needs decision yes → no, because removing fillers does not change
  the story.
- broad/F10 (decision yes) and parties/F5 (decision no) → F14: decision yes, because the tags follow
  the issuer's country throughout the flow, which may be a convention.
- broad/F9, parties/F4 → F10; broad/F3, parties/F3, context/F5 → F2: combined.
- F23 added by the merge, for consistency with mast/01#F6.

## Outside this review
- Whether an RKN and an AKE fit the ATR 72 freighter's main deck at positions MD-2 and MD-6, together
  with the other loads of flight KXL209 (capacity across documents; from broad and logistics).
