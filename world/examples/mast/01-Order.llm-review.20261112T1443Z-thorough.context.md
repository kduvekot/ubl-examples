# LLM review: 01-Order.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: context

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

### mast/01#F1 · High · Placard notation for an excepted package that needs no placard
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is "Text of the placard notation corresponding to the hazard class of this hazardous item. Can also be the hazard identification number of the orange placard (upper part) required on the means of transport." UN 2911 (radioactive material, excepted package – instruments or articles) is carried as an excepted package: it needs no class 7 label and no placard (IAEA SSR-6 and ADR 1.7.1.5/5.1.5.4; own knowledge), only the UN number marking. The same HazardousItem says so in its own text, so the placard notation contradicts the explanation next to it. The same value is in 02, 04 and 05 of this flow (all four examples that carry this item's HazardousItem with a placard notation).
- Condition: No placard notation is given for the excepted package of UN 2911, and the HazardousItem agrees with its own AdditionalInformation.
- Options: (a, preferred) remove PlacardNotation for this item; (b) if a placard were meant, the item would not be an excepted package, which changes UN number and story.
- Needs decision: no

### mast/01#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". The value repeats the language code from Language/ID (`en`, list ISO 639); it does not name a locale (a language in a country or region, e.g. English as used in Bayvarra). A language code in LocaleCode is the case section 6 names as Medium. The same value occurs 362 times in 213 examples (`grep -rh --include='*.xml' -o '<cbc:LocaleCode[^<]*' world/examples | sort | uniq -c`; every occurrence is `en` with list ISO 639).
- Condition: LocaleCode, where present, holds a locale identifier (language plus territory, e.g. `en-XB`) from a list of locales, or it is absent.
- Options: (a, preferred) remove LocaleCode, since Language/ID already says English and nothing in the document depends on a locale; (b) use a locale code such as `en-XB` with a locale list as listID, consistent with the `en-XB`/`en-XL` languageIDs used elsewhere.
- Needs decision: no

### mast/01#F3 · Medium · Fissile-isotope element used for a non-fissile americium source
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Americium-241 in smoke detectors is not fissile material (the fissile nuclides in the transport regulations are U-233, U-235, Pu-239 and Pu-241; IAEA SSR-6, own knowledge), so the definition's condition is not met. In addition 37 kBq is the typical activity of one ionisation detector, while the item is a set of ten, and the definition speaks of the radioactive contents.
- Condition: ApplicableRadioactiveIsotope is used only for fissile contents; the activity of the americium sources, if stated, is in an element whose definition covers it and refers to the contents it states (one detector or the set).
- Options: (a, preferred) remove ApplicableRadioactiveIsotope and state the activity in the RadioactiveMaterial description (e.g. "10 × 37 kBq Am-241"); (b) record that UBL lacks a non-fissile activity element as a finding for the UBL TC.
- Needs decision: no

### mast/01#F4 · Low · Transport data for dangerous goods in the buyer's order
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `State of charge below 30 %, as the air rules require.`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:MaritimePollutantCode` = `N`
- Why: The order is the buyer's (Selanu Telecom) request to buy. Under the delivery terms `/Order/cac:DeliveryTerms/cbc:ID` = `CPT` the seller arranges and pays the carriage, so placards, sea emergency schedules (EmS), road tunnel codes, the marine-pollutant status and the state of charge "as the air rules require" are the consignor's and carrier's data. The buyer neither chooses the mode (the order does not name one) nor classifies the goods for transport; this data looks copied from the item master into a document that does nothing with it. The UN number and the hazardous indicator, which tell the seller what kind of goods are ordered, have a reason.
- Condition: The order's HazardousItem carries only what the buyer needs to identify what is ordered (e.g. UN number, class, proper shipping name), or the reason for transport data is visible in the order.
- Options: (a, preferred) reduce HazardousItem in the order to identification (UNDGCode, HazardClassID, ProperShippingName) and keep the transport data in the forwarding instructions and waybill; (b) keep it with a stated reason (e.g. the buyer prescribes air carriage — then the order should say so).
- Needs decision: no

## Checked and consistent
- DG classification codes are consistent with the real regulations (own knowledge): UN 3480 class 9, EmS F-A,S-I, ERG 147, tunnel E; UN 2920 class 8 (3) PG II, EmS F-E,S-C, ERG 132, tunnel D/E, flashpoint 28 °C fits a flammable subsidiary risk; UN 2911 EmS F-I,S-S, ERG 161.
- Delivery: DeliveryParty and the CPT location are the buyer's mast site, consistent with the buyer as consignee in 02 and 03.

## Considered and refuted
- `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cbc:HazardousRiskIndicator`: suspected that excepted packages are not "subject to an international regulation" — refuted because excepted packages remain subject to the transport regulations (marking, documentation limits), only with reduced requirements.
- `/Order/cac:DeliveryTerms/cbc:ID`: suspected that CPT needs a named place — refuted because the DeliveryLocation names the mast site.
