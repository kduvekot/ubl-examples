# LLM review: 02-ForwardingInstructions.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### mast/02#F1 · High · Hazardous-item package holds six batteries, the handling unit six crates of one
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:Quantity` = `6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:PackagingTypeCode` = `CR`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[1]/cbc:Quantity` = `1`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[6]/cbc:Quantity` = `1`
- Why: Package/Quantity is "the quantity of items contained in this package". Under the loaded hazardous item it says one crate containing six batteries; the handling unit lists six crates SE-CR-1 to SE-CR-6 with one battery each (Package[1] to Package[6], each `1`). Both cannot be true. The physics favour one battery per crate: six batteries of 52 kg net (312 kg / 6) make a 348 kg package in one crate, which would also be far above the per-package limit (F4).
- Condition: the package description under the hazardous item agrees with the handling unit's packages (one battery per crate, six crates), e.g. `Package/cbc:Quantity` = `1` with six such packages, or the hazardous item refers to the six crates.
- Options: (a) preferred: describe the hazardous item's package as one battery per crate (Quantity 1) and state the six crates in the hazardous item quantity; (b) drop the package from the hazardous item, since the handling unit already lists the crates.
- Needs decision: no

### mast/02#F2 · Medium · The instructions do not say where, when or how the goods are to be forwarded
- XPath: `/ForwardingInstructions/cbc:IssueDate` = `2026-06-03`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- Why: Forwarding Instructions are "issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods". This one says what is carried and who receives it, but gives no pickup place or date, no requested departure or delivery date, no transport mode or stage, no delivery place, no delivery terms and no OtherInstruction. The order agreed CPT to the mast site (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CPT`, `01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu Telecom, mast site`), so the forwarder must arrange carriage beyond the airport, but neither this document nor the waybill (main carriage only) shows it. That the goods must fly cargo-aircraft-only appears only inside the dangerous-goods data.
- Condition: the instructions state at least the collection place and date, the requested delivery place (the mast site) and date or the agreed terms, and the requested mode or routing.
- Options: (a) preferred: add pre-carriage/main-carriage/on-carriage stages (or a Delivery with requested period and delivery location) and the CPT delivery terms; (b) at least OtherInstruction text with place, date and routing.
- Needs decision: no

### mast/02#F3 · Medium · Shipment gross weight leaves out the transport equipment
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `376`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:GrossWeightMeasure` = `3`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:GrossWeightMeasure` = `25`
- Why: Shipment/GrossWeightMeasure is defined as "the weight of the goods plus packaging plus transport equipment". 348 + 3 + 25 = 376 kg, i.e. goods and packaging only. The shipment travels in two pieces of transport equipment listed in the same document, an RKN temperature-controlled container (RKN41207K0) and an AKE container (AKE20514K0), whose tare (own knowledge: an active RKN roughly 1 t, an AKE about 80 kg) is not included. The same 376 kg is used in the forwarding instructions, the waybill and the despatch advice.
- Condition: the shipment gross weight includes the tare of the listed transport equipment, or the 376 kg is given in an element whose definition excludes the equipment (e.g. the consignment's gross weight, which excludes the carrier's equipment).
- Options: (a) preferred: put 376 kg on `Consignment/cbc:GrossWeightMeasure` (goods plus packaging, "excluding the carrier's equipment"), and give the shipment weight with tare or leave it out; (b) add the ULD tares to the shipment weight.
- Needs decision: no

### mast/02#F4 · Medium · Battery crates exceed the cargo-aircraft limit of PI 965 Section IA
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:HazardousGoodsTransit/cbc:PackingCriteriaCode` = `PI965IA`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:NetWeightMeasure` = `312`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:Quantity` = `6`
- Why: Calculated from the document: 348 kg gross / 6 crates = 58 kg per crate; one battery alone weighs 312 / 6 = 52 kg. IATA PI 965 Section IA (own knowledge) allows at most 35 kg gross per package on cargo aircraft; heavier batteries need the approval of the State of Origin under special provision A99, and that approval travels with the shipment. The document states CAO and PI 965 IA but no approval, so the declared packing does not permit what is packed.
- Condition: either each package is within 35 kg gross, or the document carries the A99 approval (reference and description) that permits the heavier packages.
- Options: (a) preferred: add a reference to the A99 approval of Bayvarra's aviation authority (e.g. in the hazardous goods transit description and a document reference), because the battery size is part of the story; (b) use smaller battery modules within 35 kg.
- Needs decision: yes

### mast/02#F5 · Medium · Placard notation 7 for an excepted package that carries no class 7 label
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "text of the placard notation corresponding to the hazard class of this hazardous item" (or the upper number of the orange plate). UN 2911 is an excepted package: it carries no class 7 label, and vehicles, containers or ULDs carrying only excepted packages are not placarded (SSR-6 and the modal rules, own knowledge). The element thus states a class 7 placard that the text next to it, rightly, says does not exist. The same value is in the order, forwarding instructions, despatch advice and invoice of this flow (4 examples, grep over `*.xml`).
- Condition: no placard notation for UN 2911, or one that matches the excepted-package marking (the UN number only) and does not contradict the additional information.
- Options: (a) preferred: remove `PlacardNotation` from this hazardous item, because nothing is placarded; (b) keep the hazard class only in `HazardClassID` (already present).
- Needs decision: no

### mast/02#F6 · Low · Carrier's ULD numbers and on-board positions in the consignor's instructions
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `RKN41207K0`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cbc:ID` = `AKE20514K0`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-2`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: The consignor (Saltmere Engineering) issues these instructions on 2026-06-03, a day before the air waybill. ULD serial numbers (with the owner's code "K0") and positions on the aircraft's main deck are assigned by the carrier or its handling agent at build-up and load planning (own knowledge); the consignor, which has not yet booked a flight (the instructions name no carrier and no flight), cannot know them. They are the carrier's data copied back into the consignor's instructions.
- Condition: the instructions contain only what the consignor can know when it issues them (e.g. a request for a temperature-controlled container), not the carrier's equipment numbers and stowage positions.
- Options: (a) preferred: remove the ULD IDs and stowage positions here (keep them in the waybill) and state the equipment requirement instead; (b) if the consignor had pre-booked, add the booking (CarrierAssignedID, carrier) that explains the numbers.
- Needs decision: no

### mast/02#F7 · Low · Orange-plate numbers on an air ULD
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- Why: The orange plate is an ADR/RID marking for road and rail vehicles and tank/bulk containers (own knowledge); the numbers 90/3480 are correct for UN 3480 but have no use in a ULD carried on a cargo aircraft, which is the only stage in the flow. The document gives no road leg in which the equipment would need them.
- Condition: orange-plate numbers appear only where a road or rail leg of the equipment needs them.
- Options: (a) preferred: remove them; (b) keep them only if a road leg with this equipment is added.
- Needs decision: no

### mast/02#F8 · Low · Packaging danger level "4" under the UN/EDIFACT 8339 list ID
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:PackagingDangerLevelCode` = `4`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:PackagingDangerLevelCode` = `4`
- Why: To my knowledge UN/EDIFACT 8339 (Packaging danger level) has only the codes 1, 2 and 3 (great, medium, minor danger). The world's copy of the list (`UNCL8339Code.gc`, "UBL example world") adds "4 Not assigned". If 8339 D22A has no code 4, a world-made code is published under a real list ID. I could not check the official directory (UNECE blocks automated access).
- Condition: every code given with `listID="UN/EDIFACT EDED 8339"` is in the official 8339 list; for entries without packing group the element is omitted or uses a world list.
- Options: (a) preferred: omit the element for UN 3480 and UN 2911 (no packing group); (b) keep "4" only if the official directory has it.
- Needs decision: yes

### mast/02#F9 · Low · Cargo-aircraft-only liquid in a closed AKE without CAO data
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:Quantity` = `20`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: UN 2920 PG II in 5-litre cans exceeds the passenger-aircraft limit (PI 851: 1 L) and can only fly on cargo aircraft (PI 855: 30 L) (own knowledge). Cargo-aircraft-only packages of class 8 must be loaded so that the crew can reach them in flight; a closed AKE container is not accessible. The battery equipment carries CAO, packing instruction and "Main deck, accessible", but the AKE with the corrosive liquid carries no transit data, no packing instruction and no accessibility statement.
- Condition: the UN 2920 cans carry their CAO status and packing instruction, and their stowage allows crew access (or the document states how the requirement is met).
- Options: (a) preferred: give the AKE's hazardous item its own HazardousGoodsTransit (PI 855, CAO) and stow the cans accessibly (e.g. loose on an accessible position or in an open ULD); (b) pack the liquid in inner packagings of at most 1 L so that it may also fly on passenger aircraft.
- Needs decision: yes

### mast/02#F10 · Low · Placard endorsement "9A" for the lithium batteries
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "text of the placard endorsement that is to be shown on the shipping papers" or the lower number of the orange plate. "9A" is the label model for lithium batteries on packages; to my knowledge the ADR and IMDG placarding rules say the 9A model is not to be used for placarding (the placard is model 9), and shipping papers show the class "9", not "9A". The orange-plate number would be 3480. The same value occurs in 4 examples of this flow (grep over `*.xml`).
- Condition: the value is what a placard or the shipping papers show for UN 3480 (e.g. none, or `3480` as orange-plate number), and the 9A label, if wanted, is stated as a package label.
- Options: (a) preferred: drop `PlacardEndorsement` (the class is in `PlacardNotation`/`HazardClassID`); (b) use `3480` if the orange-plate reading is intended.
- Needs decision: no

### mast/02#F11 · Low · Activity of one detector given for a set of ten
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ActivityLevelMeasure is "the measure of the radioactive contents during carriage". The item is a set of ten detectors, "each with a small americium-241 source"; 37 kBq is the usual activity of one detector (own knowledge), so the contents of the item are 10 × 37 = 370 kBq. As it stands, the value under-states the item's activity by a factor of ten, or leaves the reader to guess that it is per detector. Either value is far below the excepted-package limits (Am-241 A2 = 1 × 10⁻³ TBq; instrument limit 10⁻² A2 = 10 MBq, package limit A2 = 1 GBq), so the classification is not affected.
- Condition: the activity stated is that of the item as carried (370 kBq for the set), or the text says it is per detector.
- Options: (a) preferred: `370` kBq for the set; (b) keep 37 and say "per detector" in the material's name or description.
- Needs decision: no

### mast/02#F12 · Low · ApplicableRadioactiveIsotope is defined for fissile contents, americium-241 is not fissile
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: In UBL 2.5 RadioactiveMaterial/ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Am-241 is not a fissile nuclide in the sense of SSR-6 (fissile: U-233, U-235, Pu-239, Pu-241; own knowledge), so the element, read by its definition, does not fit. The definition looks like a defect in UBL (the aggregate is the only place to give a nuclide and its activity), which makes this a candidate for the findings to the UBL TC rather than a fix of the example alone.
- Condition: either the use is recorded as a deliberate deviation from a defective definition (a finding for the TC write-up), or the isotope is given in an element whose definition fits.
- Options: (a) preferred: record the definition defect in the analysis and keep the element; (b) remove the isotope and state the nuclide and activity in the material's name/description.
- Needs decision: yes

## Checked and consistent
- Physics, batteries (figures from the document): 6 × 4.8 kWh; net 312 kg / 6 = 52 kg per battery, i.e. 4,800 / 52 = 92 Wh/kg for a pack in a steel case: plausible (own knowledge: 90–150 Wh/kg at pack level). Net volume 0.24 m³ / 6 = 40 L per battery; density 312 / 0.24 = 1,300 kg/m³: plausible for a cased pack with internal voids. Packaging 348 − 312 = 36 kg for six crates = 6 kg per crate: light but possible for plywood crates.
- Physics, AKE contents: smoke detectors 3 kg gross for ten detectors (about 0.2 kg each plus a box); stripper 20 L at a density of about 0.9–1.0 kg/L (propanol 0.80, ethanolamine 1.01) = 18–20 kg plus four 5-litre steel cans of about 1 kg = 22–24 kg against 25 kg stated: plausible. Four cans × 5 L = 20 L, as the goods item says.
- Physics, equipment capacity (own knowledge): an LD3-size RKN and an AKE each take about 1.5 t gross; 348 kg and 28 kg are well within, and 0.24 m³ net of batteries fits an RKN's roughly 2 m³ interior.
- Shipment total 348 + 3 + 25 = 376 kg (see F3 for the definition).
- Temperatures: equipment range 5–35 °C equals the goods items' minimum/maximum; target 20 °C lies inside; emergency temperature 60 °C above the maximum.
- UN 3480 by air: CAO, state of charge below 30 % and PI 965 IA agree with each other; class 9 needs no crew access, so "Main deck, accessible" is more than required.
- The same equipment IDs, weights and stowage occur in the waybill (`03-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `RKN41207K0`); shipment SE-SH-26-0715 and consignment SE-CS-26-0716 are the same in 02, 03 and 04.
- DG codes of the goods items (EmS, ERG, tunnel codes, packing groups, flash point against the class 8/3 precedence) checked as in the order: consistent.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode`: "AM" (refrigerated container) for an RKN — refuted: the RKN is an active temperature-controlled container, and the indicators (refrigeration on, power) agree.
- `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:MinimumTemperature/cbc:Measure`: temperature range for goods in the AKE, which cannot control temperature — refuted: the range is a requirement on the goods that a heated main deck meets; it does not claim equipment control.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure`: an emergency temperature is a concept of self-reactive substances — refuted: as an operational threshold for lithium batteries (thermal runaway) 60 °C is a legitimate reading of "threshold temperature at which emergency procedures apply".

## Outside this review
- Whether an RKN and an AKE fit the ATR 72 freighter's main deck together with the other loads of flight KXL209 (capacity across documents).
