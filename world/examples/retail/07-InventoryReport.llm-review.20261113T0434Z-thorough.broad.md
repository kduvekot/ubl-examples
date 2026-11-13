# LLM review: 07-InventoryReport.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/07-InventoryReport.xml`, Git blob `e1019ee6a13e2a7196d8ba163e99b452ac02b47f` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/07#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/07#F2 · Medium · Language codes in LocaleCode
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/07#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/07#F4 · Low · Stock counted on Sunday, reported as current on Thursday
- XPath: `/InventoryReport/cbc:Note` = `Counted on Sunday evening.`
- XPath: `/InventoryReport/cbc:IssueDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryPeriod/cbc:EndDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:Quantity` = `3`
- Why: 2026-04-23 is a Thursday; the Sunday before is 2026-04-19. The line's `Quantity` is "The quantity of the item reported that is currently in stock", and the report period ends on the Thursday of issue. A count from Sunday evening is four days old at the end of the period; stock may have been sold since. Note and dates do not describe the same moment.
- Condition: the count date stated in the note is the date the reported quantity applies to, and the period end agrees with it (or the note is absent).
- Options: (a, preferred) a note that matches the dates (e.g. "Counted this evening" or the actual weekday); (b) end the period on the counting day.
- Needs decision: no

### retail/07#F5 · Low · Whole item master data copied into an inventory report line
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:CircularityProfile`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: an inventory report tells the supplier how many of an item are in stock; the item needs to be identified. The line carries the full catalogue description (emissions, circularity, dimensions, load test, warranty, transaction conditions, Urvania's tariff code, the distributor's wording "from the distributor's stock"), none of which the report uses.
- Condition: the item carries what identifies it and what the report depends on.
- Options: (a, preferred) name and identifiers only.
- Needs decision: no

### retail/07#F6 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. As the retailer reporting its stock, a store or stock contact would fit better than the buying office. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail (compared by script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of the contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office, or a contact fitting this role; (b) different contacts per role, if the world gives Brightmarket several.
- Needs decision: no

## Checked and consistent
- Inventory value 1560.00 = 3 × 520.00, the trade price of 02-Catalogue: stock valued at purchase price.
- The note on the line (below the minimum of 6 before the promotion) fits the promotion of 06-RetailEvent and explains the order 08-Order the next day.
- The forecast reference `BS-FC-26-0221` resolves to 05-Forecast, issued the day before.
- Inventory location (garden department) is a place within the store, not a company name.
- Retailer, reporting party and supplier are the right parties; Brightmarket and Lumeway are described as in every retail example.

## Considered and refuted
- `/InventoryReport/cac:InventoryReportLine/cbc:AvailabilityDate` = `2026-04-23`: suspected filler, since "If not present, the goods are available now" — refuted: harmless explicit statement, and the rule "nothing implied by absence" favours stating it.
