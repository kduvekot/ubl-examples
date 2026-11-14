# LLM review: 25-Catalogue.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/25-Catalogue.xml`, Git blob `2053b3b6f8e10aa06896f01ab77d01b5ac7d4848` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/25#F1 · High · Line 2 refers to a line the call for tenders does not have
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersLineReference/cbc:LineID` = `2`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: "Reference to a Line on a Call For Tenders document." `03-CallForTenders.xml` (ID LPWD-DOC-26-0189) has one request line, `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:ID` = `1` (the bench, with sub-line 1.1 for the anchor set), repeated in lot 1; lot 2 (installation) has no request line. Line 2 exists only in the tenders (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:ID` = `2`, "Installation of a park bench").
- Condition: The line reference resolves to a line of the referenced call for tenders, or is absent.
- Options: (a) preferred: drop the line reference of catalogue line 2 and keep the document reference (the installation is lot 2 of that call); (b) give the call for tenders a request line for the installation.
- Needs decision: no

### tender/25#F2 · High · The sales territory is Urvania, but the catalogue is for a buyer in Bayvarra and the tax treatment is export
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- Why: ApplicableTerritoryAddress is "the applicable sales territory" of the price, lead time and tax category of this aggregate. The catalogue is the contract catalogue for the Lumeport Public Works Department (`/Catalogue/cac:ReferencedContract/cbc:ID` = `PWD-2026-PARKS`), whose benches are delivered to and installed in Lumeport, Bayvarra (XB). The tax categories in the same aggregates say so themselves: "Export of goods outside Urvania" and "Service to a business established outside Urvania" cannot apply to sales in the territory XU. XU is the seller's country, not the territory sold into.
- Condition: The territory of each price is where the contract's deliveries take place (XB), consistent with the tax category next to it.
- Options: (a) preferred: country XB; (b) remove the territory (the contract already limits the catalogue to this buyer).
- Needs decision: no

### tender/25#F3 · High · Minimum quantity and lead time differ from the tender the contract was awarded on
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- Why: The catalogue implements the framework contract awarded on `15-Tender.xml`. For the same bench that tender states `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20` (orderable unit "Pallet of 4", increment 4, maximum 96) and a lead time of `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7` days. MinimumQuantity here is "the minimum quantity that can be ordered to qualify for a specific price": the contract price from one bench contradicts the tendered minimum of 20; nothing in the catalogue line carries the pallet unit, the increment or the maximum (CatalogueLine has `OrderableUnit`, `ContentUnitQuantity`, `OrderQuantityIncrementNumeric`, `MinimumOrderQuantity`, `MaximumOrderQuantity` for them). The shorter lead time (5 against 7 days) is not a contradiction in itself but is a second term that differs without explanation.
- Condition: The catalogue's ordering terms for the bench are those of the awarded tender (minimum 20, steps of 4, maximum 96, lead time), or a document of the flow explains the change.
- Options: (a) preferred: minimum quantity 20 EA and the order unit elements as in the tender, lead time 7 DAY; (b) keep 5 days as an improvement and only align the quantities.
- Needs decision: no

### tender/25#F4 · High · Emission factor × base does not give the emission value
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". 0.82 × 1 EA = 0.82, not 96 kg CO2e. 96 / 0.82 = 117.07, so the factor would need a base of about 117 units of something (the factor source names "measured energy use", so perhaps 0.82 kg CO2e per kWh × 117 kWh), which the document does not state; "per bench" (1 EA) is the base of the value, not of the factor. The same three values occur with this item in 39 examples across flows (files containing `ValueFactorNumeric>0.82<`, counted with grep over `world/examples/**/*.xml`).
- Condition: factor × base quantity = value, with the base in the unit the factor refers to; or factor and base are absent and only the value per bench is stated.
- Options: (a) preferred: base measure 117 KWH (value 95.94 ≈ 96), if the factor is per kWh; (b) drop factor and base.
- Needs decision: no

### tender/25#F5 · Low · Catalogue and price validity are shifted two days against the contract
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- Why: The contract the catalogue belongs to runs from `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:Contract/cac:ValidityPeriod/cbc:StartDate` = `2026-03-23` for 24 months, i.e. to 2028-03-22. The contract prices are offered from two days before the contract starts and expire two days before it ends, so a release ordered on 21 or 22 March 2028 has no valid catalogue price.
- Condition: Catalogue and contract-price validity cover the contract period (2026-03-23 to 2028-03-22).
- Options: (a) preferred: validity 2026-03-23 to 2028-03-22; (b) keep the start at the issue date and end on 2028-03-22.
- Needs decision: no

### tender/25#F6 · Low · Installation "by the manufacturer's installers", but the contract names a subcontractor
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The award says `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.` The installers are therefore Saltmere's, not the manufacturer's. (Parties are outside this lens; noted because it concerns who performs the service the catalogue line describes.)
- Condition: The description agrees with the subcontracting of the installation.
- Options: "by the manufacturer's subcontractor, Saltmere Engineering" (preferred), or drop the clause.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no failures. The standard item number 771020000027 (scheme `urn:ubl-examples:world:item`, issuer scope 771) identifies the same item, Park bench Serra 180 / VI-B180, wherever it occurs (tender, retail, road, sea, rail, carnet).
- `cac:ReferencedContract/cbc:ID` PWD-2026-PARKS is the contract of 21–24; the catalogue is issued (21 March) after the contract was signed (19 March) and before the first order (23 March), which cites it (`26-Order.xml`, CatalogueDocumentReference VI-CAT-26-0211).
- `CatalogueLine[1]/cac:CallForTendersLineReference/cbc:LineID` 1 and the document reference LPWD-DOC-26-0189 resolve to the bench line of the call for tenders.
- Prices: 49900 XUF and 1800 XUF per unit are 499.00 and 18.00 XBL at the flow's rate of 0.01, the tendered unit prices (119760.00 / 240; 4320.00 / 240).
- Classification: HS 9401.79 (seats with metal frames, other) and CPC 38111 fit a steel-framed bench; the national tariff code 94017910 extends the HS code.
- Physics: 1800 × 620 × 780 mm with a seat height of 450 mm (440–460) is a normal three-seat bench; 450 kg distributed load = 150 kg per seat for 3 seats. 22.5 kg of hardwood at about 700 kg/m³ is 0.032 m³, i.e. five slats of 1.8 m with a cross-section of about 36 cm² each (e.g. 90 × 40 mm), plausible. 34 kg of steel at roughly 2 kg CO2e per kg plus galvanising and timber is of the order of the stated 96 kg CO2e per bench.
- "Supplied with four ground anchors" agrees with the anchor set per bench of the call for tenders and tenders; warranty text agrees with the tender (five years on the frame).
- Codes (PriceTypeCode, RecordStatusCode, tax categories G and O, colour, dimension attribute, emission, lifecycle, resource, waste, scoring codes) are in their lists and fit their elements.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID`: `771020000027` is 12 digits with a valid GS1 mod-10 check digit and could be read as a GTIN-12 — refuted: the scheme is declared as the world's own item scheme, not GS1, and no document calls it a GTIN.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure`: 34 kg steel + 22.5 kg hardwood = 56.5 kg consumed per bench — refuted here: consumption may exceed the finished weight (offcuts, casting returns); the comparison with the shipped weight is made in the despatch advice.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID`: `GRY` although the first release was delivered in moss green — refuted for the catalogue: grey is the standard variant; the order change of 24 March comes later.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:MeasurementPeriod/cbc:StartDate`: emissions measured over 2025 for a 2026 catalogue — refuted: a product footprint is calculated from the previous year's data.
