# LLM review: 01-Order.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/01-Order.xml`, Git blob `b65397fa0c7cc5caf77d2e114d9eb2db2610109c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/01#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 bench (EA) the calculated value is 0.82, not the 96 kg CO2e stated in ValueMeasure. No other quantity in the item makes 0.82 a meaningful factor either: the bench consumes 34 kg steel and 22.5 kg hardwood (CircularityProfile), and 96 / 56.5 kg = 1.70, 96 / 34 kg = 2.82. The same three values occur in 39 examples (counted with `grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`), all for this bench.
- Condition: ValueFactorNumeric × ValueBaseMeasure gives ValueMeasure in the unit of ValueMeasure (or the factor and base are absent).
- Options: (a) preferred: drop factor and base, since the 96 kg is a product footprint per bench, not a factor applied to an activity; (b) give the factor that produced 96 kg with its real base (e.g. kg CO2e per kg of material, with the material mass as base).
- Needs decision: no

### rail/01#F2 · Medium · FullnessIndicationCode carries the emission boundary, not the fullness of equipment
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL defines EmissionCalculationMethod/FullnessIndicationCode as "a code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value comes from the world's EmissionBoundary list ("How much of a product's life an emission figure includes"), a system boundary of a product footprint. A bench's cradle-to-gate footprint involves no transport equipment whose fullness could be a parameter. The code is valid in its list but not the kind of value the element names. 39 occurrences over `*.xml`, all CRADLETOGATE (`grep -rc --include='*.xml' CRADLETOGATE`).
- Condition: FullnessIndicationCode, where present, says how full a piece of transport equipment is; the product footprint's boundary is not carried in it.
- Options: (a) preferred: drop the element here and express the boundary in LifecycleStageCode/LifecycleStageDescription (see F3) or EmissionStandardReference; (b) if the owner considers there is no other element for the boundary, keep it and record it as a gap for the UBL TC, which is a story-level choice.
- Needs decision: yes

### rail/01#F3 · Medium · Lifecycle stage code covers less than the stage description
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: The world's LifecycleStage list defines MANUFACTURING as "Making the product (EN 15804 module A3)" and SOURCING as "Raw material supply and its transport (EN 15804 modules A1 and A2)". The description (and the Description "Mining, steel making, casting, galvanising, sawing and the transport between them", and the cradle-to-gate boundary) covers A1 to A3. The code and its text equivalent therefore describe different stages.
- Condition: the code(s) and the description name the same life-cycle stages.
- Options: (a) preferred: split into two EnvironmentalEmission entries, SOURCING and MANUFACTURING, if the split is known; (b) keep one entry and narrow the description to manufacturing only, with a value that matches; (c) a list code for A1–A3 together.
- Needs decision: no

### rail/01#F4 · Medium · LocaleCode holds a bare language code
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used". `en` with listID ISO 639 is a language, already given in Language/ID; it names no locale. The buyer is in Bayvarra, and the example itself uses `en-XB` as languageID for Bayvarran English. The same value occurs 362 times over `*.xml` (`grep -rh --include='*.xml' '<cbc:LocaleCode' | wc -l`).
- Condition: LocaleCode, where present, is a locale (language and region, e.g. `en-XB`) from a list of locales, or the element is absent.
- Options: (a) preferred: `en-XB` with a locale list (BCP 47 style), matching the languageID used for Bayvarran English; (b) drop LocaleCode.
- Needs decision: no

### rail/01#F5 · Medium · Province in Region
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "the political or administrative division of a country … such as the name of its county, province, or state". A province is the textbook case of CountrySubentity. The Bayvarran buyer's address in the same document puts its state in CountrySubentity. 219 occurrences of `Province of Ferrano` in Region over `*.xml`.
- Condition: Urvanian provinces are in CountrySubentity (with a code where a list exists), unless the world defines them as non-administrative regions.
- Options: (a) preferred: move to CountrySubentity; (b) if Urvanian "provinces" are deliberately economic regions without administrative status, keep Region and say so in the world's address rules.
- Needs decision: yes

### rail/01#F6 · Low · Seller master data the order does nothing with
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The order is the buyer's request for 192 benches. The seller's share listing on the Ferrano Stock Exchange and its warehousing provider (Castrano Logistics) play no part in it: the buyer orders DAP to its own siding and neither element is used by any line, delivery or term of the order.
- Condition: the order carries only party data with a reason in an order.
- Options: (a) preferred: drop both from the order; (b) keep the service provider only if the buyer is meant to deal with the warehouse (then say so, e.g. in the delivery).
- Needs decision: no

### rail/01#F7 · Low · Product data of the seller's catalogue copied into the buyer's order
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- Why: An order says what the buyer wants. Repairability score, maintenance frequency, resource consumption, packaging waste per bench, warranty text and the cradle-to-gate footprint are statements of the seller about its product; the buyer does not set them and the order does nothing with them. Item identification, description, colour and the properties the buyer selects (frame colour) are enough to order.
- Condition: every item element in the order is something the buyer specifies or needs to identify the item.
- Options: (a) preferred: leave the product passport data to the documents that carry it (catalogue, product documentation VI-RM-B180); (b) keep it only if the story says the buyer orders against these declared values (e.g. a tender requirement), and say so.
- Needs decision: no

## Checked and consistent
- DeliveryTerms DAP with the delivery location at the buyer's siding, and the delivery party being the buyer, fit an order delivered by rail to the buyer.
- TaxTotal with category G and exemption EXP fits an export from Urvania to Bayvarra; 192 × 49900 = 9580800 = line extension = anticipated payable amount.
- OrderTypeCode 220, DocumentCurrencyCode XUF (the seller's currency), AccountingCost "Stock purchases" for a wholesaler: fit the document.
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass `check_ids.py`.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription` = `Stretch film and pallet straps, per bench`: suspected that packaging waste is not waste of the profiled item — refuted because WasteGenerated is "the waste generated by the profiled entity" and the packaging of each bench is plausibly counted for it (the presence question is part of F7).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`: suspected filler — refuted because a symbology for the standard item number is a legitimate attribute of that identification.
- `/Order/cbc:AccountingCost` = `Stock purchases`: checked that it is the buyer's cost text (Lumeway, a wholesaler buying for stock) — fits.
