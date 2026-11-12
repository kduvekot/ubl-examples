# LLM review: 04-DespatchAdvice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/04-DespatchAdvice.xml`, Git blob `96e68e1c850420976f9df7c6ba1c6da30707cd43` (committed)
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

### mast/04#F1 · Medium · Placard notation 7 for an excepted package that carries no class 7 label
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "text of the placard notation corresponding to the hazard class of this hazardous item" (or the upper number of the orange plate). UN 2911 is an excepted package: it carries no class 7 label, and vehicles, containers or ULDs carrying only excepted packages are not placarded (SSR-6 and the modal rules, own knowledge). The element thus states a class 7 placard that the text next to it, rightly, says does not exist. The same value is in the order, forwarding instructions, despatch advice and invoice of this flow (4 examples, grep over `*.xml`).
- Condition: no placard notation for UN 2911, or one that matches the excepted-package marking (the UN number only) and does not contradict the additional information.
- Options: (a) preferred: remove `PlacardNotation` from this hazardous item, because nothing is placarded; (b) keep the hazard class only in `HazardClassID` (already present).
- Needs decision: no

### mast/04#F2 · Low · "Consignment note" for goods sent on an air waybill
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: The goods travel by air with Kelaro Air Cargo under an air waybill (`03-Waybill.xml:/Waybill/cbc:WaybillTypeCode` = `AWB`). "Consignment note" is the road/rail document (CMR/CIM); under the Montreal Convention damage is reported to the carrier in writing within the time limits, not on a consignment note.
- Condition: the note names the transport document actually used (the air waybill) or the way damage is to be reported to the air carrier.
- Options: (a) preferred: "report any damage to the carrier on the air waybill / in writing"; (b) drop the note.
- Needs decision: no

### mast/04#F3 · Low · Shipment gross weight is goods plus packaging only
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `376`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport equipment". 376 kg is the sum of the goods' gross weights in the transport documents (348 + 3 + 25), without the two ULDs they travel in (mast/02#F3, mast/03#F3). The despatch advice does not describe the equipment, but the value it states is not what the element means.
- Condition: the 376 kg is given in an element that excludes the transport equipment (Consignment/GrossWeightMeasure), or the shipment weight includes it.
- Options: (a) preferred: move the value to the consignment's gross weight; (b) leave the shipment weight out.
- Needs decision: no

### mast/04#F4 · Low · Despatch advice without despatch date, expected delivery or transport reference
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-06-04`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- Why: A despatch advice tells the buyer what was sent and when to expect it. This one names carrier and consignment but has no despatch date or time (only the issue date), no estimated delivery, no delivery place, no packages and no reference to the air waybill (KXL-WB-26-0717, issued four hours later). The buyer cannot plan the receipt at the mast site from it.
- Condition: the advice states at least when the goods were despatched and when (or where) delivery is expected, or references the transport document that does.
- Options: (a) preferred: add Shipment/Delivery with an estimated delivery period and the delivery location, and the despatch date; (b) at least a reference to the waybill once issued.
- Needs decision: no

### mast/04#F5 · Low · Placard endorsement "9A" for the lithium batteries
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "text of the placard endorsement that is to be shown on the shipping papers" or the lower number of the orange plate. "9A" is the label model for lithium batteries on packages; to my knowledge the ADR and IMDG placarding rules say the 9A model is not to be used for placarding (the placard is model 9), and shipping papers show the class "9", not "9A". The orange-plate number would be 3480. The same value occurs in 4 examples of this flow (grep over `*.xml`).
- Condition: the value is what a placard or the shipping papers show for UN 3480 (e.g. none, or `3480` as orange-plate number), and the 9A label, if wanted, is stated as a package label.
- Options: (a) preferred: drop `PlacardEndorsement` (the class is in `PlacardNotation`/`HazardClassID`); (b) use `3480` if the orange-plate reading is intended.
- Needs decision: no

### mast/04#F6 · Low · Activity of one detector given for a set of ten
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ActivityLevelMeasure is "the measure of the radioactive contents during carriage". The item is a set of ten detectors, "each with a small americium-241 source"; 37 kBq is the usual activity of one detector (own knowledge), so the contents of the item are 10 × 37 = 370 kBq. As it stands, the value under-states the item's activity by a factor of ten, or leaves the reader to guess that it is per detector. Either value is far below the excepted-package limits (Am-241 A2 = 1 × 10⁻³ TBq; instrument limit 10⁻² A2 = 10 MBq, package limit A2 = 1 GBq), so the classification is not affected.
- Condition: the activity stated is that of the item as carried (370 kBq for the set), or the text says it is per detector.
- Options: (a) preferred: `370` kBq for the set; (b) keep 37 and say "per detector" in the material's name or description.
- Needs decision: no

### mast/04#F7 · Low · ApplicableRadioactiveIsotope is defined for fissile contents, americium-241 is not fissile
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: In UBL 2.5 RadioactiveMaterial/ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Am-241 is not a fissile nuclide in the sense of SSR-6 (fissile: U-233, U-235, Pu-239, Pu-241; own knowledge), so the element, read by its definition, does not fit. The definition looks like a defect in UBL (the aggregate is the only place to give a nuclide and its activity), which makes this a candidate for the findings to the UBL TC rather than a fix of the example alone.
- Condition: either the use is recorded as a deliberate deviation from a defective definition (a finding for the TC write-up), or the isotope is given in an element whose definition fits.
- Options: (a) preferred: record the definition defect in the analysis and keep the element; (b) remove the isotope and state the nuclide and activity in the material's name/description.
- Needs decision: yes

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `ST-PO-26-0713` resolves to mast/01 (an Order); order line references 1–3 exist there; delivered quantities 6 EA, 1 SET, 20 LTR equal the ordered quantities.
- Line notes against the data: "Six packs" = 6 EA; "One set of ten" = 1 SET of ten detectors; "Four cans of five litres" = 20 LTR.
- Physics, back-up time (figures from the document, load from own knowledge): 6 × 4.8 kWh = 28.8 kWh; over four hours that is 7.2 kW at full discharge, or about 5.8 kW at 80 % usable capacity: plausible for a telecom mast site (typically 2–8 kW).
- Shipment SE-SH-26-0715 and consignment SE-CS-26-0716 are the same as in 02 and 03; the carrier is the waybill's carrier.
- Dates: issued 2026-06-04 13:20, after the order (2026-06-01) and the forwarding instructions (2026-06-03), before the waybill (17:15) and the invoice (17:34).

## Considered and refuted
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: "DELIVERY" for an advice sent at despatch — refuted: the code ("Delivery") types the despatch as a delivery to the customer; nothing in the example presents it as a confirmation of receipt.
