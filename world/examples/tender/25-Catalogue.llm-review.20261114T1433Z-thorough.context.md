# LLM review: 25-Catalogue.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/25#F1 · High · Sales territory Urvania for prices that are exempt as exports out of Urvania
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- Why: `ApplicableTerritoryAddress` is "The applicable sales territory" of the item location quantity, i.e. where the price, lead time and tax category of that block apply. Both lines give Urvania, the seller's own country. The same block says the goods are tax-free because they are an "Export of goods outside Urvania" and the service because it is a "Service to a business established outside Urvania". A sale in the territory Urvania is not an export out of Urvania. The catalogue is made for one customer under the framework contract `PWD-2026-PARKS`, the department in Lumeport, Bayvarra, where the benches are delivered and installed; the territory to which these contract prices apply is Bayvarra.
- Condition: The sales territory of each line is the territory in which the contract customer buys (Bayvarra), and it agrees with the tax category of the same block.
- Options: (a) preferred: territory `XB`; (b) leave the territory out, the catalogue being for one customer.
- Needs decision: no

### tender/25#F2 · High · Line 2 refers to a line of the call for tenders that does not exist
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersLineReference/cbc:LineID` = `2`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersLineReference` is a "Reference to a Line on a Call For Tenders document". The call for tenders `LPWD-DOC-26-0189` has one request-for-tender line, `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:ID` = `1` (the bench), with sub-line 1.1 (ground anchor set), repeated under lot 1; lot 2, the installation, has no line at all. A line 2 does not exist there.
- Condition: Every call-for-tenders line a catalogue line refers to exists in the call for tenders named.
- Options: (a) preferred: refer line 2 to the lot (LOT-2) in a way the catalogue line allows, or drop the line reference and keep the document reference; (b) give lot 2 of the call for tenders (and the notices that repeat it) a line 2 for the installation.
- Needs decision: no

### tender/25#F3 · High · "By the manufacturer's installers" although the installation is subcontracted
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The tender that won, the award and the contract say that the installation is done by a subcontractor: `24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.` The catalogue issued under that contract says the manufacturer's own installers do it.
- Condition: The description of the installation service does not name installers other than those of the contract (Saltmere Engineering as subcontractor), in both language versions.
- Options: (a) preferred: "by the supplier's subcontractor" or no statement of who installs; (b) none seen.
- Needs decision: no

### tender/25#F4 · Medium · `CatalogueIndicator` in the catalogue itself
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: The indicator is "An indicator that this item was ordered from a catalogue (true) or not (false)". It is a statement about an order. In the catalogue nothing has been ordered yet; true here can only mean "this item is in a catalogue", which is not the definition and is self-evident.
- Condition: `CatalogueIndicator` occurs only on items of documents that order or follow an order (order, despatch, invoice), not in the catalogue.
- Options: (a) preferred: remove it from the catalogue lines; (b) none seen.
- Needs decision: no

### tender/25#F5 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in `LifecycleStageDescription` and `Description`. (The rule of semantic conformance asks for the UBL definition even where another use seems handy.)
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element here and keep the boundary in the lifecycle stage description (or in `EmissionStandardReference`); (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision; the same use occurs wherever the item is repeated)

### tender/25#F6 · Medium · "Active" as status of the price list
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- Why: `StatusCode` of a price list is "A code signifying whether this price list is an original, copy, revision, or cancellation". "Active" is none of these; it is a record status (list `RecordStatusCode`). What the definition asks for is whether `VI-PL-2026` is the original list or a revision of it.
- Condition: The status of the price list is one of original, copy, revision or cancellation (from a list with those meanings), or is absent.
- Options: (a) preferred: "original" from a suitable list; (b) remove it.
- Needs decision: no

### tender/25#F7 · Medium · A province in `Region`
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/25#F8 · Medium · A language code as locale
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/25#F9 · Low · The order constraints of the tender are missing, and the price applies from one bench
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- Why: The awarded tender, whose terms the contract catalogue restates, offers the bench in pallets of 4, in steps of 4, at least 20 and at most 96 per order, with a lead time of 7 days (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity` = `96`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`). The catalogue line has none of the order constraints (the catalogue line has elements for orderable unit, increment, minimum and maximum order quantity), gives 1 bench as "The minimum quantity that can be ordered to qualify for a specific price", and a lead time of 5 days. A buyer reading the catalogue would conclude that a single bench can be ordered within 5 days.
- Condition: The contract catalogue states the same order unit, increment, minimum and maximum order quantity and lead time as the awarded tender, or the difference is explained.
- Options: (a) preferred: add the tender's order constraints to line 1 and use its lead time; (b) if Valdara improved its terms after the award, say so in a note.
- Needs decision: no

### tender/25#F10 · Low · Validity of the contract prices does not match the contract period
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- Why: The prices are contract prices (`CON`) of the framework `PWD-2026-PARKS`, which is valid from 2026-03-23 for 24 months, to 2028-03-22 (`24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:Contract/cac:ValidityPeriod/cbc:StartDate` = `2026-03-23`). The catalogue and its prices are valid from two days before the contract starts and end two days before it ends: a release in the last two days of the framework would have no valid price, and a contract price exists before the contract does.
- Condition: The validity of the contract catalogue and of its contract prices lies within, and covers, the contract's validity.
- Options: (a) preferred: 2026-03-23 to 2028-03-22; (b) keep the issue date as start and say that prices apply from the contract's start.
- Needs decision: no

### tender/25#F11 · Low · The warranty that won the award is not in the contract catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- Why: The award went to Valdara "with ten years of warranty on the coating" (`21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:Description`), the answer of its tender to the quality criterion; the tender line itself says "Five years on the frame." The catalogue for the contract states only five years on the frame, now "against corrosion", which is what the coating protects against. The ten-year coating warranty, a term of the awarded tender, is nowhere on the item.
- Condition: The warranty information of the bench in the contract catalogue includes the ten years on the coating that the awarded tender offered and is not narrower than the tender.
- Options: (a) preferred: "Five years on the frame, ten years on the coating." in both languages; (b) none seen.
- Needs decision: no

### tender/25#F12 · Low · Nothing on the item shows the recycled steel the contract requires
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ResourceOriginDescription` = `Steel made from Serravona ore in Urvania`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: The contract has the execution requirement "At least 30 % recycled steel in the frames." (`24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:ContractExecutionRequirement/cbc:Description`). The circularity profile, the place for exactly this, says the steel is made from ore, and the emission description starts at mining; no document of the flow after the contract mentions recycled content (searched "recycled" in `world/examples/tender/*.xml`: only the notices, the call for tenders and the contract). As written, the item does not meet, or at least does not show that it meets, the requirement it was awarded under.
- Condition: The resource consumption of the bench states the share of recycled steel (at least 30 %), consistent with the origin description and the emission's description.
- Options: (a) preferred: split the steel into two resource consumptions (ore-based and recycled scrap) or state the share in the origin description; (b) drop the execution requirement from the procedure.
- Needs decision: yes (changes what the product is made of, or the terms of the procedure)

### tender/25#F13 · Low · Lifecycle stage "Manufacturing" for an emission from the mine to the gate
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and the description is the same "expressed as a text". The text covers raw material extraction, steel making and manufacturing (cradle to gate); the code names only the manufacturing stage. Code and text should say the same.
- Condition: The lifecycle stage code and its description cover the same stages.
- Options: (a) preferred: a code for the whole upstream-and-production span if the list has or gets one; (b) one emission per stage, each with its own value.
- Needs decision: no

### tender/25#F14 · Low · Two keywords in one `Keyword`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: `Keyword` is "A keyword (search string) for this item" and may repeat; the value holds two keywords separated by a comma, so neither is a search string of its own.
- Condition: Each `Keyword` element holds one keyword.
- Options: (a) preferred: two `Keyword` elements; (b) none seen.
- Needs decision: no

### tender/25#F15 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/25#F16 · Low · Master data of a party that the document does not use
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Catalogue/cac:ProviderParty/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The catalogue describes items and prices for the contract customer; the provider's share capital and listing and the contact of its warehouse provider are not used by it. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- Prices against the awarded tender at the rate the order states (100 ferra = 1 lume, `26-Order.xml`): 49900 XUF = 499.00 XBL a bench (240 × 499.00 = 119760.00, lot 1), 1800 XUF = 18.00 XBL per installation (240 × 18.00 = 4320.00, lot 2).
- `ReferencedContract` `PWD-2026-PARKS` is the framework contract; contractor customer and receiver are the department, provider and seller Valdara Industries; the catalogue is issued after the contract (2026-03-19) and before the first order (2026-03-23), and the contract announces the use of an electronic catalogue.
- `CallForTendersDocumentReference` `LPWD-DOC-26-0189` is the document ID of the call for tenders; line 1 of it is the bench ("Park bench, 1800 mm"), and the item is 1800 mm long.
- Item against the call for tenders line: steel frame, five hardwood slats, ground anchors (four anchors and bolts supplied; sub-line 1.1 "Ground anchor set").
- Colour: extended ID `GRY`, physical attribute colour of the frame `GRY`, property "Frame colour" = "Ferro grey": agree.
- Seat height 450 mm within its range 440–460 mm; depth 620 mm, height 780 mm, length 1800 mm, three seats: plausible for a bench (my own judgement).
- Classification: HS 940179 and CPC 38111 (seats with metal frames), tariff code 94017910 as an extension of the HS code.
- Every text given in two languages is tagged `qau` and `en-XU`; the Urvanian texts were not checked for meaning.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount`: a contract price in ferra although the contract was awarded in lume — refuted for this lens because the order states a fixed rate of 100 and the amounts convert exactly; which currency binds is for the money part.
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: "service to a business" although the customer is a public body — refuted for this lens; tax treatment is the money part's.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode`: an 8-digit national tariff code in an element defined as "harmonized international commodity code" — refuted because the tariff code extends the HS code and is used for the same regulatory purpose.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ResourceOriginDescription`: slats from Bayvarra in an item of Urvanian origin — refuted, origin of the item is where it is made.
- `/Catalogue/cac:SellerSupplierParty`: repeats the provider — refuted because the definition of provider (who provides the catalogue) and seller differ and both are needed to say they coincide in a contract catalogue.
- `/Catalogue/cbc:Name`: a general name for a contract catalogue — refuted, a free name assigned by the sender.

## Outside this review
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82` with `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1` does not give `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96` (0.82 × 1 = 0.82; 96 / 0.82 = 117); physics and factor arithmetic are the logistics part's lens. Not judged here, recorded so it is not lost.
