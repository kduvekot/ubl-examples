# LLM review: 03-ItemInformationRequest.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/03-ItemInformationRequest.xml`, Git blob `831fa39b706e496e223832845d95a8ebe56ea67b` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/03#F1 · Medium · One request line asks for activity, forecast and performance metric at once
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:ForecastTypeCode` = `TOTAL`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: The definition of `ForecastTypeCode` in this line states the model's intent: "The information request can be either about supply chain activity or about forecasts or about performance metrics, so it will be optional". The three codes are alternatives that say which kind of information a line asks for. This line sets all three, so it asks at once for actual sales, a total forecast and a sales-in-units metric. The note asks only for "weekly figures", and the answer `06-ProductActivity.xml` reports only actual sales (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cbc:SupplyChainActivityTypeCode` = `SALES`); no forecast and no performance history is ever sent in the flow.
- Condition: each request line carries exactly one of the three kinds of request (activity, forecast or metric), and every kind requested is answered by a document of the flow.
- Options: (a) keep only `SupplyChainActivityTypeCode` = `SALES` (preferred: it is what the note asks and what 06 answers); (b) split into separate lines per kind and add the answering documents.
- Needs decision: no

### furniture/03#F2 · Medium · LocaleCode holds a bare language code
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/03#F3 · Low · "The whole season" against a request period that ends in May
- XPath: `/ItemInformationRequest/cbc:Note` = `Weekly figures, please, for the whole season.`
- XPath: `/ItemInformationRequest/cac:Period/cbc:EndDate` = `2026-05-11`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:Period/cbc:EndDate` = `2026-05-11`
- Why: The note asks for figures for the whole season, but the request's `Period` ("The period of time to which the Item Information Request applies") and the line's period end on 2026-05-11. The season of this item, as the store's replenishment profile and exception criteria define it, runs to 2026-08-29 (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:Period/cbc:EndDate` = `2026-08-29`). Text and structured period disagree.
- Condition: the note and the periods describe the same span.
- Options: (a) reword the note to the first eight weeks (preferred: keeps dates and the flow unchanged); (b) extend the periods to the end of the season.
- Needs decision: no

### furniture/03#F4 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`), so `BrandName` ("A brand name of this item") = the maker's name contradicts the description, unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under in the story, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword the texts to a maker-branded exclusive line.
- Needs decision: yes

### furniture/03#F5 · Low · Receiver's master data copied into the request
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:AdditionalWebSite`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:SocialMediaProfile`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital of the store have no use in a request for sales figures (section 4.8). Carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `BuyerCustomerParty` ("The Buyer from whom the Item Information is requested") is the receiver and `SellerSupplierParty` ("The Seller requesting the Item Information") the sender: roles fit the definitions.
- `TimeFrequencyCode` = `WEEKLY` fits the note.
- `DocumentReference` resolves to the quotation `02-Quotation.xml`, the agreement on which the collaboration is based.

## Considered and refuted
- `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cbc:Quantity` = `20`: a quantity in a request for figures was suspected to be meaningless — refuted because `SalesItem/Quantity` is mandatory ("The quantity the given information are related to") and 20 sets is the quantity quoted in `02-Quotation.xml` and ordered four days later in `08-Order.xml`, the stock the figures relate to.
