# LLM review: 05-Invoice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/05-Invoice.xml`, Git blob `a846f2c92225b4f657cb71040b2ccfd1f8ecfc9d` (committed)
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

### mast/05#F1 · High · Placard notation for an excepted package that needs no placard
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is "Text of the placard notation corresponding to the hazard class of this hazardous item. Can also be the hazard identification number of the orange placard (upper part) required on the means of transport." UN 2911 (radioactive material, excepted package – instruments or articles) is carried as an excepted package: it needs no class 7 label and no placard (IAEA SSR-6 and ADR 1.7.1.5/5.1.5.4; own knowledge), only the UN number marking. The same HazardousItem says so in its own text, so the placard notation contradicts the explanation next to it. The same value is in 01, 02 and 04 of this flow.
- Condition: No placard notation is given for the excepted package of UN 2911, and the HazardousItem agrees with its own AdditionalInformation.
- Options: (a, preferred) remove PlacardNotation for this item; (b) if a placard were meant, the item would not be an excepted package, which changes UN number and story.
- Needs decision: no

### mast/05#F2 · Medium · Pricing reference without any pricing, holding dangerous-goods indicators
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:HazardousRiskIndicator` = `true`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:BatchQuantity` = `1`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:HazardousRiskIndicator` = `true`
- Why: PricingReference is "A reference to pricing and item location information associated with this invoice line", and OriginalItemLocationQuantity "An original set of location-specific properties (e.g., price and quantity) associated with this item". Here it holds no price, no location and no original quantity, only two hazardous indicators and a delivery batch of one, which say nothing about pricing and repeat `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:HazardousRiskIndicator` = `true`. Lines 2 and 3, which are dangerous goods too, have no such aggregate. The aggregate is used for a meaning other than its definition.
- Condition: PricingReference, where present, carries pricing or location-specific price information the invoice line relies on; hazard status is stated on the item only.
- Options: (a, preferred) remove the PricingReference from line 1; (b) if an original catalogue price per location exists in the story, put it there and drop the indicators.
- Needs decision: no

### mast/05#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". The value repeats the language code from Language/ID (`en`, list ISO 639); it does not name a locale (a language in a country or region, e.g. English as used in Bayvarra). A language code in LocaleCode is the case section 6 names as Medium. The same value occurs 362 times in 213 examples (`grep -rh --include='*.xml' -o '<cbc:LocaleCode[^<]*' world/examples | sort | uniq -c`; every occurrence is `en` with list ISO 639).
- Condition: LocaleCode, where present, holds a locale identifier (language plus territory, e.g. `en-XB`) from a list of locales, or it is absent.
- Options: (a, preferred) remove LocaleCode, since Language/ID already says English and nothing in the document depends on a locale; (b) use a locale code such as `en-XB` with a locale list as listID, consistent with the `en-XB`/`en-XL` languageIDs used elsewhere.
- Needs decision: no

### mast/05#F4 · Medium · Fissile-isotope element used for a non-fissile americium source
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Americium-241 in smoke detectors is not fissile material (the fissile nuclides in the transport regulations are U-233, U-235, Pu-239 and Pu-241; IAEA SSR-6, own knowledge), so the definition's condition is not met. In addition 37 kBq is the typical activity of one ionisation detector, while the item is a set of ten, and the definition speaks of the radioactive contents.
- Condition: ApplicableRadioactiveIsotope is used only for fissile contents; the activity of the americium sources, if stated, is in an element whose definition covers it and refers to the contents it states (one detector or the set).
- Options: (a, preferred) remove ApplicableRadioactiveIsotope and state the activity in the RadioactiveMaterial description (e.g. "10 × 37 kBq Am-241"); (b) record that UBL lacks a non-fissile activity element as a finding for the UBL TC.
- Needs decision: no

### mast/05#F5 · Low · Transport data for dangerous goods in the invoice
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-E,S-C`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `D/E`
- Why: The invoice requests payment; the buyer's accounts payable do nothing with sea emergency schedules, road tunnel codes, placards or radioactive activity of goods that have already been shipped under their own transport documents (02, 03) and announced with the despatch advice (04). The full HazardousItem blocks on all three lines look copied from the item master.
- Condition: The invoice's items carry only data that billing, tax or customs valuation uses, or the reason for the dangerous-goods data is visible in the invoice.
- Options: (a, preferred) remove HazardousItem from the invoice lines (the HazardousRiskIndicator can stay if it serves a purpose); (b) keep only the UN number if the invoice serves as a commercial invoice for customs.
- Needs decision: no

## Checked and consistent
- OrderReference `ST-PO-26-0713` resolves to 01 and DespatchDocumentReference `SE-DA-26-0718` to 04; line references 1–3 and quantities agree with both.
- check_ids.py: RF reference `RF78SEINV260719` and IBAN-like account `XB69BLUM38712001885122` have correct check digits.

## Considered and refuted
- `/Invoice/cbc:DefaultLanguageCode`: suspected a language code where a locale is needed — refuted because the element is defined as the default natural language and `en` is a language code.
