# LLM review: 05-Forecast.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/05-Forecast.xml`, Git blob `e5ca058f329dbb9d83da42c0dcf6bbefbfd16c1c` (committed)
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

### retail/05#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/05#F2 · High · Reference to the promotion does not resolve to the retail event of the flow
- XPath: `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `BM-RE-26`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:ID` = `BS-RE-26-0222`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:BuyerEventID` = `BM-SPRING-GARDEN-26`
- Why: the forecast "Includes the spring garden promotion", and the only additional document it refers to is `BM-RE-26`. The promotion is announced in 06-RetailEvent, issued the same morning by the same sender, with document ID `BS-RE-26-0222` and buyer's event ID `BM-SPRING-GARDEN-26`. `BM-RE-26` is neither, and no example carries a document with that ID (searched over `world/examples/*/*.xml`). The forecast cannot be linked to the event it is based on.
- Condition: the reference carries the ID of 06-RetailEvent (or the event ID it is known by), and says what it refers to if that is not obvious.
- Options: (a, preferred) reference `BS-RE-26-0222`, with a document type or description naming it as the retail event; (b) if `BM-RE-26` is a separate internal document, describe it and add a reference to 06 as well.
- Needs decision: no

### retail/05#F3 · Medium · Language codes in LocaleCode
- XPath: `/Forecast/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Forecast/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/05#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/05#F5 · Low · Whole item master data copied into a forecast line
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:CircularityProfile`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Dimension[1]`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a sales forecast tells the supplier how many of an item the retailer expects to sell; the item needs to be identified (seller's ID `LD-10442`, GTIN). The forecast line carries the complete catalogue description of the bench instead: dimensions, load test, emissions, circularity data, warranty, transaction conditions and Urvania's customs tariff code (not used between two Bayvarran parties). None of it is used by the forecast; the description "from the distributor's stock" is the catalogue's wording, not the retailer's.
- Condition: the forecast's item carries what identifies it and what the forecast depends on, and no catalogue data the forecast does not use.
- Options: (a, preferred) reduce the item to name and identifiers; (b) keep a few attributes only if the forecast depends on them (e.g. colour variant).
- Needs decision: no

### retail/05#F6 · Low · Frozen document indicator: the value means the opposite of what the line suggests
- XPath: `/Forecast/cac:ForecastLine/cbc:FrozenDocumentIndicator` = `false`
- XPath: `/Forecast/cac:ForecastLine/cbc:Note` = `Week-by-week figures follow in the store's portal.`
- Why: UBL defines `FrozenDocumentIndicator` as "An indicator that the status of the forecast is modifiable (true) or not (false)". By that definition `false` says the forecast line cannot be modified, i.e. it is frozen, which is the opposite of what the element's name and the context suggest (a first version, not based on consensus, with weekly figures still to follow). Whichever meaning is intended, the element is ambiguous as encoded.
- Condition: the indicator's value, read with UBL's definition, says what the story intends (modifiable or not).
- Options: (a, preferred) if the forecast may still change, `true` per UBL's definition, and record the inverted wording of the definition as a finding for the UBL TC; (b) drop the indicator if the story does not need it.
- Needs decision: yes

### retail/05#F7 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. As the sender of a forecast the buying office fits the role. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail (compared by script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of the contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office, or a contact fitting this role; (b) different contacts per role, if the world gives Brightmarket several.
- Needs decision: no

## Checked and consistent
- Forecast period 2026-05-04 to 2026-06-15 contains the promotion period of 06-RetailEvent (2026-05-11 to 2026-05-24); the line's period equals the header's.
- 40 benches in total over six weeks is consistent with 06's planned impact of 17976.00 = 24 × 749.00 during the promotion (consumer price 749.00 from `21-PurchaseReceipt.xml`) and 07-InventoryReport, which refers to this forecast.
- Sender, receiver, buyer and seller are the right parties; both are described as in every retail example.
- Item identifiers (`LD-10442`, GTIN `9520610000012`, `VI-B180`) agree with 02-Catalogue; GTIN and GLN check digits pass.

## Considered and refuted
- `/Forecast/cbc:BasedOnConsensusIndicator` = `false`: suspected to contradict the agreed promotion — refuted: the promotion was agreed, but the forecast quantities are the retailer's own.
- `/Forecast/cbc:IssueTime` = `11:55:00`: checked against 06-RetailEvent's issue at 08:17 the same day — consistent, the event precedes the forecast that includes it.
