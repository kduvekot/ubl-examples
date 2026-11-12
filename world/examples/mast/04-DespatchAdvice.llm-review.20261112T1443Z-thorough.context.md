# LLM review: 04-DespatchAdvice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: context

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

### mast/04#F1 · High · Placard notation for an excepted package that needs no placard
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is "Text of the placard notation corresponding to the hazard class of this hazardous item. Can also be the hazard identification number of the orange placard (upper part) required on the means of transport." UN 2911 (radioactive material, excepted package – instruments or articles) is carried as an excepted package: it needs no class 7 label and no placard (IAEA SSR-6 and ADR 1.7.1.5/5.1.5.4; own knowledge), only the UN number marking. The same HazardousItem says so in its own text, so the placard notation contradicts the explanation next to it. The same value is in 01, 02 and 05 of this flow.
- Condition: No placard notation is given for the excepted package of UN 2911, and the HazardousItem agrees with its own AdditionalInformation.
- Options: (a, preferred) remove PlacardNotation for this item; (b) if a placard were meant, the item would not be an excepted package, which changes UN number and story.
- Needs decision: no

### mast/04#F2 · Medium · Language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". The value repeats the language code from Language/ID (`en`, list ISO 639); it does not name a locale (a language in a country or region, e.g. English as used in Bayvarra). A language code in LocaleCode is the case section 6 names as Medium. The same value occurs 362 times in 213 examples (`grep -rh --include='*.xml' -o '<cbc:LocaleCode[^<]*' world/examples | sort | uniq -c`; every occurrence is `en` with list ISO 639).
- Condition: LocaleCode, where present, holds a locale identifier (language plus territory, e.g. `en-XB`) from a list of locales, or it is absent.
- Options: (a, preferred) remove LocaleCode, since Language/ID already says English and nothing in the document depends on a locale; (b) use a locale code such as `en-XB` with a locale list as listID, consistent with the `en-XB`/`en-XL` languageIDs used elsewhere.
- Needs decision: no

### mast/04#F3 · Medium · Fissile-isotope element used for a non-fissile americium source
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Americium-241 in smoke detectors is not fissile material (the fissile nuclides in the transport regulations are U-233, U-235, Pu-239 and Pu-241; IAEA SSR-6, own knowledge), so the definition's condition is not met. In addition 37 kBq is the typical activity of one ionisation detector, while the item is a set of ten, and the definition speaks of the radioactive contents.
- Condition: ApplicableRadioactiveIsotope is used only for fissile contents; the activity of the americium sources, if stated, is in an element whose definition covers it and refers to the contents it states (one detector or the set).
- Options: (a, preferred) remove ApplicableRadioactiveIsotope and state the activity in the RadioactiveMaterial description (e.g. "10 × 37 kBq Am-241"); (b) record that UBL lacks a non-fissile activity element as a finding for the UBL TC.
- Needs decision: no

### mast/04#F4 · Low · Note asks for damage to be reported on a "consignment note" the flow does not have
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods travel by air under the air waybill of 03 (`03-Waybill.xml:/Waybill/cbc:Name` = `Air waybill under the Montreal Convention`). A consignment note is the road (CMR) or rail document; under the Montreal Convention damage is notified to the carrier in writing (own knowledge). The note points the consignee to a document that does not exist in this flow.
- Condition: The note names the transport document actually used (the air waybill) or the carrier to whom damage is notified.
- Options: (a, preferred) say "on the air waybill" or "to the carrier"; (b) drop the sentence.
- Needs decision: no

### mast/04#F5 · Low · "No status" codes that say nothing
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cbc:LineStatusCode` = `NoStatus`
- Why: The codes state that the document and its lines have no status; that is what their absence means. They carry no business information (no-filler rule). `NoStatus` occurs in 29 examples (`grep -rl --include='*.xml' 'NoStatus' world/examples | wc -l`).
- Condition: DocumentStatusCode and LineStatusCode are present only with a status that means something for this despatch (e.g. a replacement or a cancelled line).
- Options: (a, preferred) remove them; (b) keep them only where the story gives the document or a line a status.
- Needs decision: no

## Checked and consistent
- OrderReference `ST-PO-26-0713` resolves to 01; line references 1–3 match the order lines; delivered quantities (6 EA, 1 SET, 20 LTR) equal the ordered ones.
- Shipment `SE-SH-26-0715` and consignment `SE-CS-26-0716` are those of 02 and 03; the carrier Kelaro Air Cargo is the carrier of 03.
- Line notes agree with the structured data: six packs × 4.8 kWh = 28.8 kWh, four hours of back-up at about 7.2 kW for a mast site is plausible; four 5-litre cans = 20 L.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode`: suspected transport data the despatch advice does nothing with — refuted because the despatch advice accompanies dangerous goods to the consignee, who handles them on arrival; the hazard data has a reason here.
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: suspected mismatch — refuted because `DELIVERY` fits a despatch advice announcing the delivery to the buyer.
