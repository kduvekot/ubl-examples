# LLM review: 25-Catalogue.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/25#F1 · High · Line 2 refers to a line of the call for tenders that does not exist
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersLineReference/cbc:LineID` = `2`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: CallForTendersLineReference is a "Reference to a Line on a Call For Tenders document". 03-CallForTenders.xml (ID LPWD-DOC-26-0189) has one request-for-tender line only, `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:ID` = `1` (the bench, with sub-line 1.1 for the anchors), repeated under lot 1; lot 2 (installation) has no line. Line 2 of the catalogue therefore points to nothing.
- Condition: every call-for-tenders line reference resolves to a line of 03, or is absent.
- Options: (a) drop the line reference of catalogue line 2 and refer to lot 2 another way, or not at all (preferred); (b) give lot 2 of the call a request-for-tender line 2 for the installation (then also in 02, 21).
- Needs decision: no

### tender/25#F2 · High · Sales territory Urvania for a catalogue that serves a customer in Bayvarra, with export tax treatment
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason[2]` = `Export of goods outside Urvania`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason[2]` = `Service to a business established outside Urvania`
- Why: ApplicableTerritoryAddress is "The applicable sales territory" of the price, lead time and tax category next to it. The catalogue belongs to the framework contract with the Lumeport Public Works Department and its prices are the contract prices for deliveries to Lumeport, Bayvarra. The tax categories in the same aggregates say so: export out of Urvania, service to a customer outside Urvania. A sale inside the territory Urvania would not be an export, and the installation (anchoring benches in Lumeport's parks) cannot take place in Urvania at all.
- Condition: the sales territory of each line is where the contract's customer buys and the tax treatment applies (Bayvarra), or the territory is absent.
- Options: (a) territory XB (preferred); (b) remove ApplicableTerritoryAddress, the catalogue being for one customer.
- Needs decision: no

### tender/25#F3 · High · Installation "by the manufacturer's installers", but the contract has it done by a subcontractor
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: the award and the contract state that the installation is subcontracted: `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.` Valdara's qualification (13) was likewise "The manufacturer with Saltmere as subcontractor for the installation." The catalogue issued two days after the contract says the manufacturer's own installers do the work.
- Condition: the catalogue's description of the installation agrees with the contract on who installs.
- Options: (a) "… by Saltmere Engineering, the manufacturer's installation subcontractor" or simply drop the clause (preferred); (b) none other seen.
- Needs decision: no

### tender/25#F4 · Medium · Emission factor that does not lead to the emission value
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". The value is 96 kg CO2e for the base of 1 bench (EA). 0.82 × 1 is not 96, and no quantity in the document gives 96 with this factor: 96 / 0.82 = 117.07, while the bench's materials are 34 kg steel and 22.5 kg hardwood (0.82 × 56.5 kg = 46.3; 0.82 × 34 kg = 27.9). The source names "measured energy use", so the factor may be kg CO2e per kWh, but then the activity (about 117 kWh per bench) is not stated and the factor cannot be applied by a reader. Plausibility of the value itself: 96 kg CO2e for 34 kg of ore-based, galvanised cast steel plus sawn wood is about 2.8 kg CO2e per kg steel, in the usual range for primary steel (my knowledge: about 2 to 2.5 kg per kg before casting and galvanising).
- Condition: factor × the stated base (or a stated activity quantity) gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric and keep value per bench (preferred); (b) state the activity so that factor × activity = 96 (e.g. in Description).
- Needs decision: no

### tender/25#F5 · Medium · Language code in LocaleCode; province in Region
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division and belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; the province is in CountrySubentity.
- Options: (a) a locale code, and move the province (preferred).
- Needs decision: no

### tender/25#F6 · Low · Catalogue and price validity are shifted two days against the contract
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- Why: the catalogue carries the "Contract price" of the framework `/Catalogue/cac:ReferencedContract/cbc:ID` = `PWD-2026-PARKS`, which runs from 2026-03-23 for 24 months, to 2028-03-22 (`24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:Contract/cac:ValidityPeriod/cbc:StartDate` = `2026-03-23`). The contract prices are stated as valid from two days before the contract starts and end two days before it ends, so the last two days of the framework have no catalogue price.
- Condition: the validity of the contract prices covers the contract's period.
- Options: (a) price validity 2026-03-23 to 2028-03-22, catalogue validity from its issue to 2028-03-22 (preferred).
- Needs decision: no

### tender/25#F7 · Low · Ordering terms of the tender are missing or different
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `1`
- Why: the tender that became the contract offers a lead time of `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7` days, a minimum order of `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20` benches, pallets of 4 and increments of 4. The contract catalogue gives 5 days and a minimum of 1, and none of the ordering units (CatalogueLine has OrderableUnit, ContentUnitQuantity, OrderQuantityIncrementNumeric, MinimumOrderQuantity for this). A buyer ordering from the catalogue would not learn that benches come in fours and from 20 up.
- Condition: lead time and ordering quantities in the catalogue agree with the tender, or a difference is explained.
- Options: (a) carry the tender's ordering terms and lead time (preferred); (b) keep 5 days as an improvement and say so.
- Needs decision: no

### tender/25#F8 · Low · CatalogueIndicator inside the catalogue; two keywords in one element
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: CatalogueIndicator is "An indicator that this item was ordered from a catalogue (true) or not (false)"; in the catalogue itself nothing has been ordered, so the indicator has no statement to make. Keyword is "A keyword (search string) for this item" and is repeatable; two keywords are packed into one string, so a search for the exact keyword fails.
- Condition: CatalogueIndicator appears only in documents that order or report items; each keyword is its own element.
- Options: (a) remove the indicator here, split the keywords (preferred).
- Needs decision: no

### tender/25#F9 · Low · Steel "made from ore" against the contract's requirement of recycled steel
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ResourceOriginDescription` = `Steel made from Serravona ore in Urvania`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: the contract requires `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:ContractExecutionRequirement/cbc:Description` = `At least 30 % recycled steel in the frames.` The catalogue for that contract describes the 34 kg of steel only as made from ore and reports emissions from the mine onward. The wording does not exclude a scrap share, but the document written for this contract is silent on the one material requirement the contract makes.
- Condition: the resource description of the steel is compatible with, and preferably states, the recycled share the contract requires.
- Options: (a) add the recycled share ("… with 30 % scrap", or a second ResourceConsumption for recycled steel; preferred); (b) leave as is and prove the share elsewhere.
- Needs decision: no

### tender/25#F10 · Low · The department described as a company in a commercial register
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: a municipal department (ISIC 8411) is not a company in a commercial register and has no liquidation status.
- Condition: no liquidation status and no commercial-register type on the department.
- Options: (a) remove them (preferred).
- Needs decision: no

## Checked and consistent
- Prices: 49900 XUF and 1800 XUF are the tender's 499.00 XBL and 18.00 XBL at the rate the order and invoice use (1 XBL = 100 XUF; 26, 32).
- `/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189` is the call for tenders (03) and its line 1 is the bench.
- Item against the call and tender: 1800 mm, steel frame, five hardwood slats, ground anchors; model Serra 180 as tendered in 15; warranty "Five years on the frame" as on the tender line.
- Physics: three seats on 1800 mm (600 mm each); load 450 kg = 150 kg per seat; seat height 450 mm within 440–460; steel 34 kg + hardwood 22.5 kg = 56.5 kg per bench (the weight the despatch advice can be compared with); 22.5 kg of hardwood at about 700 kg/m³ is 0.032 m³, i.e. five slats of 1.8 m with about 90 × 40 mm cross-section, plausible.
- Classification: HS 9401.79 (other seats with metal frames) and CPC 38111 fit a steel-framed bench (my knowledge of HS 2022 and CPC 2.1); the national tariff code extends the HS code.
- Tax categories: G (export) for the goods and O (outside scope) for the service agree with their exemption reasons; texts are given in Urvanian and English with matching language tags.
- Colour: ExtendedID GRY, PhysicalAttribute COLOUR/FRM/GRY and property "Frame colour" = Ferro grey agree.
- Parties: provider and seller Valdara, receiver and contractor customer the department, as in the contract.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID`: 771020000027 has 12 digits and a valid GS1 mod-10 check digit, so it could be read as a UPC-A/GTIN-12 — refuted as a finding because its schemeID is the world's own item scheme, the issuer scope 771 and the symbology Code 128 mark it as not GS1; noted so that the owner can confirm the number range against GS1 prefixes.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity`: 1 contradicts the tender's minimum order of 20 — refuted as a contradiction because here it is "the minimum quantity that can be ordered to qualify for a specific price" (the price applies from one piece); the missing ordering terms are F7.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:WarrantyInformation[2]`: five years, while the award speaks of ten years — refuted because the ten years are on the coating (criterion response in 15) and the tender line also says five years on the frame.
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: "Service to a business" although the customer is a public body — refuted because the Urvanian rule turns on the customer being established abroad, and the same reason is used on the invoice; whether Urvania treats public bodies as businesses is not decidable from the examples.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount`: contract in lume, catalogue in ferra — refuted because the order names XUF as pricing currency.
- `/Catalogue/cac:ProviderParty/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted here because a catalogue may tell the buyer who warehouses and despatches the goods.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:OriginCountry/cbc:IdentificationCode`: XU although the slats come from Bayvarra — refuted, origin follows the manufacture of the bench.
