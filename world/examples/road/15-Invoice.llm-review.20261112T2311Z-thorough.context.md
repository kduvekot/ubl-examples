# LLM review: 15-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/15-Invoice.xml`, Git blob `8fdcb4b50214e654097ed80dd7c97b81f9267569` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/15#F1 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/15#F2 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/15#F3 · Medium · Emission factor and base do not give the stated emission
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/15#F4 · Medium · Province given as Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/15#F5 · Medium · LocaleCode holds a language code
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/15#F6 · Low · Invoice line 2 does not identify the substituted 2026 casting
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- Why: the order response replaced the ordered side frame by the 2026 casting (`02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`). The invoice line bills the base item `VI-C180` without the extended ID, so the buyer cannot match the billed item to the substituted one it accepted.
- Condition: line 2 identifies the billed casting as the 2026 variant (e.g. `ExtendedID` `2026`).
- Options: (a) add the extended ID `2026` (preferred: same identification as in the order response); (b) a line note naming the substitution.
- Needs decision: no

### road/15#F7 · Low · Contacts that do not fit an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the accounting supplier's contact on an invoice is its billing or accounts-receivable function, not the order desk; the accounting customer's contact is accounts payable, not Lumeway's customer service in Sales.
- Condition: the accounting contacts are the billing functions of both parties.
- Options: (a) accounts receivable / accounts payable contacts (preferred); (b) drop job titles and departments that do not fit.
- Needs decision: no

### road/15#F8 · Low · Master and product data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: the invoice bills the goods; the seller's stock-exchange listing, its logistics provider, search keywords, the circularity profile and the product's emission figure play no part in billing (section 4.8, IND5). Warranty text can belong on an invoice in some practice, but nothing in this flow refers to it.
- Condition: party and item data in the invoice have a use in billing or paying.
- Options: (a) drop listing, service provider, keyword, circularity profile and emission (preferred); (b) keep the warranty only if the story uses the invoice as warranty proof.
- Needs decision: no

## Checked and consistent
- Order `LD-PO-26-0149` and despatch advice `CL-DA-26-0153` resolve to `01-Order.xml` and `04-DespatchAdvice.xml`; invoice lines 1 and 2 refer to order lines 1 and 2 with the ordered quantities and prices.
- Accounting customer = buyer = delivery party (Lumeway); accounting supplier = seller (Valdara); the buyer's accounting code and text repeat those of the order, which is the buyer's own code passed on to the seller.
- Issued 2026-03-24 after the despatch on 2026-03-23; the tax category `G` (export) fits the FCA export from Urvania.

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode` = `4410`: suspected copied without reason — refuted because the order gave the seller this code (`01-Order.xml:/Order/cbc:AccountingCostCode` = `4410`) and the invoice returns it for the buyer's booking of the goods.
