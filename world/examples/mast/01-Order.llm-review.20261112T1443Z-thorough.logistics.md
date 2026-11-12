# LLM review: 01-Order.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/01-Order.xml`, Git blob `a15e986388f03b87c705a9a004911992c536b517` (committed)
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

### mast/01#F1 · Medium · Placard notation 7 for an excepted package that carries no class 7 label
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "text of the placard notation corresponding to the hazard class of this hazardous item" (or the upper number of the orange plate). UN 2911 is an excepted package: it carries no class 7 label, and vehicles, containers or ULDs carrying only excepted packages are not placarded (SSR-6 and the modal rules, own knowledge). The element thus states a class 7 placard that the text next to it, rightly, says does not exist. The same value is in the order, forwarding instructions, despatch advice and invoice of this flow (4 examples, grep over `*.xml`).
- Condition: no placard notation for UN 2911, or one that matches the excepted-package marking (the UN number only) and does not contradict the additional information.
- Options: (a) preferred: remove `PlacardNotation` from this hazardous item, because nothing is placarded; (b) keep the hazard class only in `HazardClassID` (already present).
- Needs decision: no

### mast/01#F2 · Low · Placard endorsement "9A" for the lithium batteries
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "text of the placard endorsement that is to be shown on the shipping papers" or the lower number of the orange plate. "9A" is the label model for lithium batteries on packages; to my knowledge the ADR and IMDG placarding rules say the 9A model is not to be used for placarding (the placard is model 9), and shipping papers show the class "9", not "9A". The orange-plate number would be 3480. The same value occurs in 4 examples of this flow (grep over `*.xml`).
- Condition: the value is what a placard or the shipping papers show for UN 3480 (e.g. none, or `3480` as orange-plate number), and the 9A label, if wanted, is stated as a package label.
- Options: (a) preferred: drop `PlacardEndorsement` (the class is in `PlacardNotation`/`HazardClassID`); (b) use `3480` if the orange-plate reading is intended.
- Needs decision: no

### mast/01#F3 · Low · Activity of one detector given for a set of ten
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ActivityLevelMeasure is "the measure of the radioactive contents during carriage". The item is a set of ten detectors, "each with a small americium-241 source"; 37 kBq is the usual activity of one detector (own knowledge), so the contents of the item are 10 × 37 = 370 kBq. As it stands, the value under-states the item's activity by a factor of ten, or leaves the reader to guess that it is per detector. Either value is far below the excepted-package limits (Am-241 A2 = 1 × 10⁻³ TBq; instrument limit 10⁻² A2 = 10 MBq, package limit A2 = 1 GBq), so the classification is not affected.
- Condition: the activity stated is that of the item as carried (370 kBq for the set), or the text says it is per detector.
- Options: (a) preferred: `370` kBq for the set; (b) keep 37 and say "per detector" in the material's name or description.
- Needs decision: no

### mast/01#F4 · Low · ApplicableRadioactiveIsotope is defined for fissile contents, americium-241 is not fissile
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: In UBL 2.5 RadioactiveMaterial/ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Am-241 is not a fissile nuclide in the sense of SSR-6 (fissile: U-233, U-235, Pu-239, Pu-241; own knowledge), so the element, read by its definition, does not fit. The definition looks like a defect in UBL (the aggregate is the only place to give a nuclide and its activity), which makes this a candidate for the findings to the UBL TC rather than a fix of the example alone.
- Condition: either the use is recorded as a deliberate deviation from a defective definition (a finding for the TC write-up), or the isotope is given in an element whose definition fits.
- Options: (a) preferred: record the definition defect in the analysis and keep the element; (b) remove the isotope and state the nuclide and activity in the material's name/description.
- Needs decision: yes

### mast/01#F5 · Low · CPT delivery place given only as text
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu Telecom, mast site`
- Why: Under CPT the named place is where the seller's contracted carriage ends, so it decides how far the seller must arrange transport (here: beyond Selanu airport to the mast). The place has neither an address nor an identifier; the consignee's address appears only in the transport documents (`02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`), and nothing says whether the mast site is that address.
- Condition: the delivery location of the CPT term is identified (address or location ID) so that the transport documents can be checked against it.
- Options: (a) preferred: give `DeliveryLocation` the mast site's address; (b) if the mast site is the consignee's address, say so in the description.
- Needs decision: no

## Checked and consistent
- Battery energy: 48 V × 100 Ah = 4,800 Wh = 4.8 kWh, as the description says.
- Coating stripper: 20 LTR in 5-litre cans = 4 cans (the despatch advice says "Four cans of five litres").
- UN 2920 classification (own knowledge of the precedence table): flash point 28 °C puts the flammable property in class 3 PG III (23–60 °C); against class 8 PG II the precedence table gives class 8 primary with subsidiary 3, as stated; ethanolamine (corrosive) and propanol (flammable) fit as technical names.
- Codes against their lists and the UN entries (own knowledge): UN 3480 class 9, EmS F-A,S-I, ERG 147, tunnel code E; UN 2911 class 7, EmS F-I,S-S, ERG 161, no packing group; UN 2920 PG II, EmS F-E,S-C, ERG 132, tunnel code D/E. All match.
- State of charge below 30 % matches IATA PI 965 for UN 3480 by air.
- HS codes: 850760 lithium-ion accumulators, 853110 fire alarms, 381400 paint/varnish removers fit the items.

## Considered and refuted
- `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement`: "8" for UN 2920 — refuted: shows the primary class on the papers, a legitimate reading of the definition.
- `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:UNDGCode`: whether smoke detectors could be exempt consumer products rather than UN 2911 — refuted because the consumer-product exemption applies only after sale to the end user, and 370 kBq exceeds the Am-241 consignment exemption limit (10 kBq; own knowledge).
