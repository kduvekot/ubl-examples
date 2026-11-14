# LLM review: 25-Catalogue.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/25-Catalogue.xml`, Git blob `2053b3b6f8e10aa06896f01ab77d01b5ac7d4848` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/25#F1 · High · Sales territory Urvania for prices that are exempt as exports out of Urvania
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- Why: `ApplicableTerritoryAddress` is "The applicable sales territory" of the item location quantity, i.e. where its price, lead time and tax category apply. Both lines give Urvania, the seller's own country. The same blocks exempt the goods as "Export of goods outside Urvania" and the installation as "Service to a business established outside Urvania"; a sale in the territory Urvania is neither. The catalogue is for one customer under the framework `PWD-2026-PARKS` (`/Catalogue/cac:ReferencedContract/cbc:ID` = `PWD-2026-PARKS`), the department in Lumeport, Bayvarra (`/Catalogue/cac:ReceiverParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XB`), where the benches are delivered and installed. Money rated it Medium because the country may have been meant as the jurisdiction of the VAT; that is not what the element means, and the value contradicts the tax category of its own aggregate, so High.
- Condition: the territory of each item location quantity is where the contract customer buys (Bayvarra) and agrees with the tax category next to it, or no territory is stated.
- Options: (a) territory `XB` (preferred); (b) remove the territory, the catalogue being for one customer.
- Needs decision: no
- From: broad (F2, High), parties (F1, High), logistics (F2, High), context (F1, High), money (F1, Medium)

### tender/25#F2 · High · Emission factor × base does not give the emission value
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". Recalculated: 0.82 × 1 EA = 0.82, not 96 kg CO2e; 96 / 0.82 = 117.07, so the factor would need a base of about 117 units of an activity the document does not state (the source names "measured energy use", so perhaps 0.82 kg CO2e per kWh × 117 kWh); 0.82 × 56.5 kg of material = 46.3. "Per bench" is the base of the value, not of the factor. The value itself is plausible (about 2.8 kg CO2e per kg of the 34 kg of primary steel, own knowledge). The same triple occurs in 39 files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: factor × base = value, with the base in the unit the factor refers to; or factor and base are absent.
- Options: (a) drop factor and base and keep the value per bench (preferred, as in the earlier flows); (b) base 117 KWH if the factor is per kWh.
- Needs decision: no
- From: logistics (F4, High), broad (F4, Medium); context listed it under "Outside this review"

### tender/25#F3 · High · Line 2 refers to a line the call for tenders does not have
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersLineReference/cbc:LineID` = `2`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersLineReference` is a "Reference to a Line on a Call For Tenders document". The call `LPWD-DOC-26-0189` has one request-for-tender line, `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:ID` = `1` (the bench, with sub-line 1.1 for the anchors), repeated under lot 1; lot 2 (installation) has no line (verified with lxml: two RequestForTenderLine elements in 03, both ID 1). A line 2 exists only in the tenders (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:ID` = `2`).
- Condition: every call-for-tenders line reference resolves to a line of 03, or is absent.
- Options: (a) drop the line reference of catalogue line 2 and keep the document reference (preferred); (b) give lot 2 of the call a request-for-tender line for the installation (then also in 02, 21).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F2)

### tender/25#F4 · Medium · A province in `Region`
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country", i.e. `CountrySubentity`, which the Bayvarran addresses use. 219 such values in 104 files (`grep -rh --include='*.xml' '<cbc:Region>Province of' world/examples`).
- Condition: the province is in `CountrySubentity`; `Region` is absent or holds a region in the sense of the definition.
- Options: (a) move it to `CountrySubentity` (preferred); (b) record a world address rule if it is a postal region only.
- Needs decision: no
- From: broad (F5, part), parties (F2), context (F7)

### tender/25#F5 · Medium · Language code in `LocaleCode`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value (listID `ISO 639`) repeats the language code of `cbc:ID`. 362 such elements in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or names a locale from a list of locales.
- Options: (a) remove it (preferred, as in all earlier flows); (b) a real locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad (F5, part), parties (F3), context (F8)

### tender/25#F6 · Medium · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The receiver is a municipal department (ISIC 8411). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be wound up like a company, and a scheme typed "Commercial register" does not fit a body that is not a company. The register number itself is not questioned.
- Condition: the public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and type the register neutrally or omit the type (preferred); (b) reduce the legal entity to registration name and CompanyID.
- Needs decision: no
- From: broad (F10, Low), parties (F8, Low), context (F15, Low)

### tender/25#F7 · Medium · "Active" as the status of the price list
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- Why: `PriceList/StatusCode` is "A code signifying whether this price list is an original, copy, revision, or cancellation". "Active" from the record-status list (`RecordStatusCode`) is none of these; a code from a list meant for another element.
- Condition: the status of the price list is one of original, copy, revision or cancellation, from a list with those meanings, or is absent.
- Options: (a) "original" from a suitable list (preferred); (b) remove it.
- Needs decision: no
- From: context (F6)

### tender/25#F8 · Medium · `CatalogueIndicator` in the catalogue itself
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: The indicator is "An indicator that this item was ordered from a catalogue (true) or not (false)", a statement about an order. In the catalogue nothing has been ordered; true can only mean "this item is in a catalogue", which is not the definition. Broad rated it Low; Medium because the element carries a meaning other than its definition.
- Condition: `CatalogueIndicator` occurs only on items of documents that order or follow an order.
- Options: (a) remove it from the catalogue lines (preferred).
- Needs decision: no
- From: context (F4, Medium), broad (F8, Low, part)

### tender/25#F9 · Medium · Lifecycle stage "Manufacturing" for an emission from the mine to the gate
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and the description is the same "expressed as a text". The text covers raw material extraction, steel making and manufacturing (cradle to gate); the code names only manufacturing. Code and text contradict each other in scope.
- Condition: the lifecycle stage code and its description cover the same stages.
- Options: (a) omit the code, or one emission per stage (preferred where the list has no cradle-to-gate code); (b) add a code for the whole span to the list.
- Needs decision: no
- From: context (F13, Low)

### tender/25#F10 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says nothing about transport equipment; the item is a bench. The boundary is already in `LifecycleStageDescription`. 39 files carry it (`grep -rl --include='*.xml' CRADLETOGATE world/examples | wc -l`).
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent.
- Options: (a) remove it and keep the boundary in the lifecycle description (preferred); (b) record for the UBL TC write-up that the calculation method has no element for the system boundary.
- Needs decision: no
- From: context (F5, Needs decision yes)

### tender/25#F11 · Medium · Installation "by the manufacturer's installers", but the award has it done by a subcontractor
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The tender names a subcontractor for the installation (`15-Tender.xml:/Tender/cac:SubcontractorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`), and the award and contract say `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`; Valdara's qualification says "The manufacturer with Saltmere as subcontractor for the installation." (13). The catalogue says the manufacturer's installers do the work. Broad and context rated it High; parties argued that the phrase can be read loosely ("installers engaged by the manufacturer"), logistics gave Low. The loose reading cannot be excluded, so the merge rates it Medium: taken as written it attributes the work to another party than the award.
- Condition: the description of the installation does not attribute the work to a party other than the one tender and award name, in both language versions.
- Options: (a) "by the supplier's installation subcontractor" or drop the clause (preferred); (b) if the manufacturer's own staff install, remove the subcontractor from tender and award (changes the story).
- Needs decision: no
- From: broad (F3, High), context (F3, High), parties (F4, Medium), logistics (F6, Low)

### tender/25#F12 · Low · Catalogue and price validity shifted two days against the contract, and unchanged across the January price revisions
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- Why: The contract runs from `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:Contract/cac:ValidityPeriod/cbc:StartDate` = `2026-03-23` for 24 months, to 2028-03-22. The contract prices are valid two days before the contract exists and end two days before it does, so a release on 21 or 22 March 2028 has no catalogue price. The contract also revises prices (`24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cbc:PriceRevisionFormulaDescription` = `Steel index each January.`), so a price promised unchanged across January 2027 and 2028 contradicts it in substance.
- Condition: the validity of the contract prices lies within and covers the contract period, and does not extend past the next price revision unless the catalogue says the price is subject to it.
- Options: (a) price validity 2026-03-23 to 2028-03-22 with a note that the January revision replaces the price by a new catalogue (preferred: one catalogue for the framework); (b) price validity 2026-03-23 to 2026-12-31 (money's preference).
- Needs decision: no
- From: broad (F6), logistics (F5), context (F10), money (F3)

### tender/25#F13 · Low · Master data of the parties that the catalogue does nothing with
- XPath: `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Catalogue/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketName` = `Ferrano Stock Exchange`
- XPath: `/Catalogue/cac:ProviderParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Catalogue/cac:ProviderParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: The catalogue describes items and prices for the contract customer. The provider's share capital, fully-paid indicator and listing, its warehousing provider (with a contact that has a name and no means of contact) and both parties' customs-trader numbers are not used by it. Counter-arguments carried: broad held that a catalogue may tell the buyer who warehouses and despatches the goods; parties held that the listing is part of the description of a listed company. Neither is a use in this document; the despatch advice carries Castrano in its own role. (`CorporateStockAmount` also holds share capital where UBL defines "number of shares"; a note for the TC write-up.)
- Condition: the parties carry what the catalogue uses.
- Options: (a) leave these elements out of the catalogue (preferred); (b) keep those for which a use can be stated, and give the service provider's contact a means of contact.
- Needs decision: no
- From: parties (F6), context (F16); customs-trader numbers added in the merge

### tender/25#F14 · Low · Same Urvanian party tagged `en-XU` here and `en-XB` (with a single untagged legal form) in the Bayvarran-issued examples
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: This Valdara-issued catalogue tags the English renderings `en-XU` and gives the legal form in `qau` and `en-XU`; the Bayvarran-issued examples tag the same texts `en-XB` and give the legal form once, untagged (`03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`, `03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`). This example is the consistent `en-XU` side; the finding is the inconsistency across the flow (`en-XB` in 13 examples, `en-XU` in 9, `grep -c` over `world/examples/tender/*.xml`). Whether the tag is meant to follow the issuer cannot be settled. The renderings are moreover Italian names and an Italian legal form tagged as English; the earlier flows kept that as a second Low/yes question (world convention of Italianate English names, or not), folded in here by the merge.
- Condition: the same name carries the same `languageID` in every example of the flow, or the rule by which it differs is documented.
- Options: (a) `en-XU` everywhere, as here (preferred); (b) document the issuer-dependent rule.
- Needs decision: yes
- From: parties (F5)

### tender/25#F15 · Low · Party tax exemption reason worded as a transaction
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax"; the text begins with a kind of sale, only its second half is the party's status. The code's list description reads as a buyer status, so it can stay.
- Condition: the party-level exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: exempt from the state sales tax" (preferred); (b) also a status code.
- Needs decision: no
- From: parties (F7)

### tender/25#F16 · Low · Ordering terms of the awarded tender missing or different
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- Why: The awarded tender offers the bench on pallets of 4, in steps of 4, at least 20 and at most 96 per order, with a lead time of 7 days (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:OrderQuantityIncrementNumeric` = `4`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity` = `96`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`). The catalogue line carries none of the order constraints (it has `OrderableUnit`, `ContentUnitQuantity`, `OrderQuantityIncrementNumeric`, `MinimumOrderQuantity`, `MaximumOrderQuantity` for them), grants the contract price from one bench ("The minimum quantity that can be ordered to qualify for a specific price") and promises 5 days. Logistics rated it High; Low kept because a seller may grant more than it tendered (broad's refutation of a contradiction, carried) and 5 days is shorter than 7, not inconsistent with it.
- Condition: the catalogue states the tender's order unit, increment, minimum and maximum and its lead time, or a difference is explained.
- Options: (a) carry the tender's ordering terms and lead time (preferred); (b) keep the wider terms as a stated concession.
- Needs decision: no
- From: broad (F7), money (F4), logistics (F3, High), context (F9)

### tender/25#F17 · Low · "Contract prices" in ferra for a contract tendered and awarded in lume, with no rate in the catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `49900`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `1800`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceTypeCode` = `CON`
- Why: CON is the price agreed in a contract. The tender, award and contract are in lume (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`, i.e. 499 XBL a bench; 4320.00 for 240 installations, i.e. 18 XBL). The catalogue states 49900 and 1800 XUF, which match only at 100 ferra to the lume, a rate the catalogue does not mention and the order takes from a forward contract (`26-Order.xml:/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`). If the rate moves, a release priced from the catalogue no longer costs what was tendered. Broad and context refuted it because the order names XUF as pricing currency and the amounts convert exactly; that shows the flow is consistent after the catalogue, not which currency the contract fixes.
- Condition: the catalogue's contract prices are in the currency the contract fixes, or the contract/catalogue states the fixed rate that ties them to the awarded amounts.
- Options: (a) contract prices in XBL (499 and 18) as tendered (preferred); (b) keep XUF and state in contract and catalogue that prices are fixed at 100 ferra to the lume.
- Needs decision: yes (which currency the framework's prices are in is story)
- From: money (F2); broad and context refuted it (carried as counter-argument)

### tender/25#F18 · Low · Installation exempted as a "service to a business" for a customer that is a public body
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:ID` = `O`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason[2]` = `Service to a business established outside Urvania`
- Why: The world's list defines SVCABROAD as a service to a business established outside Urvania, taxed where the customer is established. The only customer is a public authority (ISIC 8411), and the anchoring of benches in Lumeport is outside Urvanian VAT because of where it is performed. Broad refuted it: the rule turns on the customer being established abroad, and the invoice uses the same reason; whether Urvania treats a foreign public body as a business cannot be decided from the examples. Both arguments stand.
- Condition: the exemption reason's definition covers a public-body customer and a service performed on land outside Urvania.
- Options: (a) widen the definition of SVCABROAD to "a customer established outside Urvania" if that is the world's rule (preferred); (b) a reason for work on immovable property abroad, used here and in 32, 33.
- Needs decision: yes
- From: money (F5); broad refuted it (carried)

### tender/25#F19 · Low · Two keywords in one `Keyword`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: `Keyword` is "A keyword (search string) for this item" and repeats; two keywords in one string are no search string of their own.
- Condition: each `Keyword` holds one keyword.
- Options: (a) two `Keyword` elements (preferred).
- Needs decision: no
- From: broad (F8, part), context (F14)

### tender/25#F20 · Low · The warranty that won the award is not in the contract catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- Why: The award went to Valdara "with ten years of warranty on the coating" (`21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:Description` = `Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.`), its tender's answer to the quality criterion ("Ten years on the coating." in 15). The contract catalogue states only five years on the frame, now "against corrosion", which is what the coating protects against. Broad refuted a contradiction between 5 and 10 years (different parts of the bench); the omission of the awarded term remains.
- Condition: the bench's warranty information in the contract catalogue includes the ten years on the coating.
- Options: (a) "Five years on the frame, ten years on the coating." in both languages (preferred).
- Needs decision: no
- From: context (F11)

### tender/25#F21 · Low · World item number that is a valid GTIN-12
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- Why: The number has 12 digits and a valid GS1 mod-10 check digit (recalculated: 7), so it reads as a GTIN-12 / UPC-A in the GS1 US/Canada range; the rule "fictional values must not be mistaken for real ones" applies. Broad and logistics refuted it because the schemeID is the world's own item scheme, the issuer scope 771 and Code 128 mark it as not GS1; the earlier flows' merges kept it as Low/yes because whether the number is assigned could not be checked and the format is a world-wide convention. The value occurs in 39 files (`grep -rl --include='*.xml' '>771020000027<' world/examples | wc -l`).
- Condition: the world item numbers cannot be read as valid GTINs, or it is recorded that they were checked against GS1.
- Options: (a) change the world item-number format so it is not a valid GTIN (preferred); (b) record the verification.
- Needs decision: yes
- From: added in the merge from broad's and logistics' refutations, aligned with analysis/review-merge-decisions.md

### tender/25#F22 · Low · Nothing on the item shows the recycled steel the contract requires
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ResourceOriginDescription` = `Steel made from Serravona ore in Urvania`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: The contract requires `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:ContractExecutionRequirement/cbc:Description` = `At least 30 % recycled steel in the frames.` The circularity profile, the place for this, says the steel is made from ore, and the emission starts at mining; no document after the contract mentions recycled content (`grep -rn --include='*.xml' -i recycled world/examples/tender`: only 01–03, 21, 24). The wording does not exclude a scrap share, so this cannot be called a contradiction.
- Condition: the resource consumption of the bench states the recycled share (at least 30 %), consistent with origin and emission descriptions.
- Options: (a) split the steel into ore-based and recycled resource consumptions, or state the share in the origin description (preferred); (b) drop the execution requirement from the procedure.
- Needs decision: yes (what the product is made of, or the procedure's terms)
- From: broad (F9, no), context (F12, yes)

## Checked and consistent
- Prices against the awarded tender at 100 ferra to the lume (26-Order): 49900 XUF = 499 XBL (240 × 499 = 119760.00, lot 1), 1800 XUF = 18 XBL (240 × 18 = 4320.00, lot 2); `BaseQuantity` 1 EA on both.
- `CatalogueLine[1]` call-for-tenders line 1 and document `LPWD-DOC-26-0189` resolve to the bench line of 03.
- `ReferencedContract` `PWD-2026-PARKS` is the framework of 21–24; the catalogue is issued after the contract (19 March) and before the first order (23 March), which cites it; the contract announces an electronic catalogue.
- Parties: provider and seller Valdara, receiver and contractor customer the department; identifiers the same across the flow; provider's "Order desk" contact fits a catalogue from which releases are ordered (from parties).
- Tax categories G (export) and O (outside scope) with reasons EXP / SVCABROAD, 0 %, VAT, texts in `qau` and `en-XU`.
- Item against call and tender: 1800 mm, steel frame, five hardwood slats, four ground anchors; model Serra 180; warranty "five years on the frame" as on the tender line.
- Physics (recalculated): three seats on 1800 mm; 450 kg = 150 kg per seat; seat height 450 within 440–460 mm; 22.5 kg hardwood at about 700 kg/m³ = 0.032 m³, five slats of 1.8 m with about 36 cm² cross-section; 34 + 22.5 = 56.5 kg of material per bench.
- Classification: HS 940179 and CPC 38111 fit a steel-framed bench; tariff code 94017910 extends the HS code (own knowledge).
- Colour: ExtendedID GRY, PhysicalAttribute COLOUR/FRM/GRY and "Frame colour" = Ferro grey agree.
- `check_ids.py`: ISIN XU0001042501 correct.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID`: valid GTIN-12 check digit — refuted by broad and logistics (world's own scheme, Code 128); the merge disagrees and makes it F21 (from broad, logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity`: 1 contradicts the tender's minimum of 20 — refuted as a contradiction because the element is the quantity qualifying for a price; carried in F16 as Low (from broad).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:WarrantyInformation[2]`: five years while the award speaks of ten — refuted: the ten years are on the coating, the tender line also says five years on the frame; F20 keeps the omission (from broad).
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: "service to a business" for a public body — refuted by broad (rule turns on establishment abroad; same reason on the invoice) and by context for its lens; the merge keeps money's F18 with both arguments (from broad, context).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount`: contract in lume, catalogue in ferra — refuted by broad and context (order names XUF; amounts convert exactly); the merge keeps money's F17 (from broad, context).
- `/Catalogue/cac:ProviderParty/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted by broad (a catalogue may tell who despatches); the merge keeps it in F13 (from broad).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:OriginCountry/cbc:IdentificationCode`: XU although the slats come from Bayvarra — refuted, origin follows the manufacture of the bench (from broad; likewise context for `ResourceConsumption[2]`).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount`: no price for the special colour later charged 200.00 lume (27) — refuted: that charge rests on a later quotation VI-QT-26-0071 (from money).
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:Percent`: 0 % on an out-of-scope category — refuted: UBL has no rule against it and 0 is what is charged (from money).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID`: general price list ID on a contract price — refuted, a seller may keep contract prices in its own list (from money).
- `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` instead of ISO 8601 — refuted: text element, used alike everywhere (from parties).
- `/Catalogue/cac:ProviderParty/cac:Contact/cbc:Telephone`: +999 a real country code — refuted: not assigned in E.164 (from parties).
- `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: unused master data — refuted by parties as part of a listed company's description; the merge keeps it in F13 (from parties).
- `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990` a real ICD — refuted, not allocated (own knowledge) (from parties).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cac:StandardPropertyIdentification/cac:IssuerParty/cac:PartyName/cbc:Name`: Codana issuing a property identifier — refuted: it maintains the Urvanian property scheme, same in 7 examples (from parties).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure`: 56.5 kg consumed per bench — refuted here: consumption may exceed the finished weight; the shipped weight is compared in 29 (from logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID`: GRY although the first release was moss green — refuted for the catalogue: grey is the standard variant; the change comes later (from logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:MeasurementPeriod/cbc:StartDate`: 2025 data for a 2026 catalogue — refuted: a footprint is calculated from the previous year (from logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode`: 8-digit national tariff code in a "harmonized international" element — refuted: it extends the HS code for the same purpose (from context).
- `/Catalogue/cac:SellerSupplierParty`: repeats the provider — refuted: provider and seller are different roles (from context).
- `/Catalogue/cbc:Name`: a general name — refuted, a free name assigned by the sender (from context).

## Changed in the merge
- broad/F2, parties/F1, logistics/F2, context/F1, money/F1 → F1: High (money's Medium not followed; its reading is quoted).
- logistics/F4 (High), broad/F4 (Medium) → F2: High, aligned with analysis/review-merge-decisions.md (bench emission triple High/no); preferred option changed to dropping factor and base, as in the earlier flows.
- broad/F5 → F4 and F5: split into Region and LocaleCode.
- broad/F10, parties/F8, context/F15 → F6: raised from Low to Medium, aligned with the decisions file (public bodies as companies).
- broad/F8 → F8 and F19: split; CatalogueIndicator Medium (context), Keyword Low.
- context/F13 → F9: raised from Low to Medium, aligned with the decisions file (LifecycleStageCode MANUFACTURING with a cradle-to-gate description: Medium/no).
- context/F5 → F10: Needs decision changed from yes to no, aligned with the decisions file (CRADLETOGATE: Medium/no; TC write-up as option).
- broad/F3, context/F3 (High), parties/F4 (Medium), logistics/F6 (Low) → F11: Medium, because the possessive can be read loosely.
- broad/F6, logistics/F5, context/F10, money/F3 → F12: combined; money's price-revision point and option added.
- parties/F6, context/F16 → F13: combined; customs-trader numbers added by the merge.
- broad/F7, money/F4, logistics/F3 (High), context/F9 → F16: Low; logistics' High lowered (wider terms are not a contradiction).
- F21 added by the merge from the refutations of broad and logistics, aligned with the earlier flows (GTIN-like world item numbers: Low/yes).
- broad/F9 (no), context/F12 (yes) → F22: Needs decision yes.
