# LLM review: 05-ExceptionCriteria.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/05-ExceptionCriteria.xml`, Git blob `440e2b01e4a52b0bcacdcd69708f6bc057bfaf71` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/05#F1 · Medium · Sales threshold without a time basis
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdQuantity` = `5`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:Note` = `Slow sales.`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:EffectivePeriod/cbc:EndDate` = `2026-08-29`
- Why: Line 1 triggers an exception when sales are less than 5 sets, but does not say over which interval (per week, per four weeks, over the season). Its only period is the `EffectivePeriod` ("The period during which this exception criteria line is in effect", 2026-03-23 to 2026-08-29, 23 weeks), which would mean fewer than 5 sets in the whole season and could not be judged before its end. Line 2 has the time basis it needs (`/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cac:ForecastExceptionCriterionLine/cbc:TimeDeltaDaysQuantity` = `28`); line 1 has none. The flow reads the threshold two ways: the notification applies it to four weeks (2026-03-23 to 2026-04-20; `07-ExceptionNotification.xml:/ExceptionNotification/cac:ExceptionNotificationLine/cbc:Note` = `Three sets sold against five expected.`), while the item information request asked for weekly figures (`03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:TimeFrequencyCode` = `WEEKLY`); against weekly figures, "fewer than 5 sets a week" would be met almost every week with 20 sets for the season. The criterion cannot be evaluated without the interval, which is the document's purpose ("to specify the thresholds … beyond which exceptions will be triggered").
- Condition: line 1 states the interval over which sales are compared with the threshold, in a structured element or at least in the line note, and that interval is the observation period the notification uses.
- Options: (a, preferred) state the four-week basis in the line note ("fewer than 5 sets in four weeks"), since UBL has no structured interval element for an operational criterion, matching 07; (b) a weekly threshold, with 07 changed to match; (c) express the criterion as a forecast-comparison line, where `TimeDeltaDaysQuantity` can carry 28 days, if the story treats it as a comparison with the plan.
- Needs decision: no
- From: broad, context, logistics

### furniture/05#F2 · Medium · Line 1 is both an operational and a metric criterion
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: In `ExceptionCriteriaLine`, `SupplyChainActivityTypeCode` "Establishes the criterion for one of the three types of exceptions. There can be three types of exception criteria: Operational, Metric and Forecast Exceptions. This will be set if this Exception is about an Operational Exception." `PerformanceMetricTypeCode` sets a metric criterion, and line 2 shows the third type (`ForecastExceptionCriterionLine`). Line 1 sets two of the three types at once, so it does not say whether "Slow sales" is an operational criterion on sales activity or a metric criterion on sales in units; the notification `07-ExceptionNotification.xml` then carries both as well. The merge tried the reading that the metric code merely names the unit of the sales figure: the definition presents the codes as the marks of distinct exception types, and the unit is already in `ThresholdQuantity` (`unitCode` SET).
- Condition: each criteria line establishes exactly one of the three types of exception.
- Options: (a, preferred) keep `SupplyChainActivityTypeCode` = `SALES` only: the threshold is a sales quantity in sets, i.e. an operational criterion, which the note and the product activity report match; (b) keep the metric only and drop the activity code, if the story means a performance metric.
- Needs decision: no
- From: broad, context, logistics

### furniture/05#F3 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExceptionCriteria/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode` (context, parties, earlier flows); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/05#F4 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores sets the exception criteria as the buyer. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact for supplier collaboration. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying or planning contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/05#F5 · Low · Party master data copied into the exception criteria
- XPath: `/ExceptionCriteria/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/ExceptionCriteria/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo reference, online-shop website, photo-sharing profile, share capital (with the fully-paid-shares indicator) and both parties' state-sales-tax registrations are master data. Exception criteria carry no amounts, tax treatment, payment or label and do nothing with any of them (section 4.8). The store's four marketing and capital elements are carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: these elements are present only in documents that have a reason to carry them.
- Options: (a, preferred) remove them here, keeping identification, name, address, contact and electronic address; (b) keep any of them only with a reason the document states (none is apparent).
- Needs decision: no
- From: context, parties

### furniture/05#F6 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/ExceptionCriteria/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/ExceptionCriteria/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/05#F7 · Low · Comparison and resolution codes differ from the values UBL names
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdValueComparisonCode` = `LT`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cbc:ThresholdValueComparisonCode` = `GT`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ExceptionResolutionCode` = `REVIEW`
- Why: UBL's definition of `ThresholdValueComparisonCode` says "Allowed values are: EXCEEDS_EXCEPTION_VALUE FALLS_BELOW_EXCEPTION_VALUE", and that of `ExceptionResolutionCode` lists "Possible values are: DEFAULT_TO_AVERAGE_OF_COMPARED_VALUES DEFAULT_TO_BUYERS_VALUE DEFAULT_TO_HIGH_VALUE …". The world's lists use other codes (LT/GT, REVIEW), while for neighbouring elements of the same line they follow the values UBL names (`CollaborationPriorityCode` HIGH). For the comparison code the definition says "allowed", so the departure is from the definition's wording; a joint review is not one of the listed resolutions, which all default to a value. The broad part refuted the comparison code: it comes from the world's own list with its listID, and "Less than" means the same as "falls below". The merge cannot settle whether the definition's value list binds: the meaning matches, so it is not a semantic misuse, but the rule that real lists come from their sources speaks for the values UBL names.
- Condition: the comparison code uses the values the definition allows, or the world's list records why it departs from them; the resolution code uses a listed value, or the list records the extension.
- Options: (a, preferred) give the world's ThresholdValueComparisonCode list the two values UBL names, and keep REVIEW as a documented extension, since a joint review is the story's real resolution; (b) keep both lists and record the departures as a finding about UBL's definitions for the TC write-up.
- Needs decision: yes
- From: logistics (broad refuted the comparison code, see Why)

### furniture/05#F8 · Low · ExceptionStatusCode, defined for shipment exceptions, used for the status of a sales criterion
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ExceptionStatusCode` = `ACTIVE`
- Why: UBL 2.5 defines `ExceptionCriteriaLine/ExceptionStatusCode` as "A code signifying status specific to a shipment exception". The value "Criterion in force" is the status of a sales criterion; there is no shipment exception. The broad part refuted this: in a criteria line the element can only mean the criterion's status, and the word "shipment" is carried over in the UBL definition. The merge agrees that the definition reads like a copying error in UBL, but under semantic conformance the value does not meet it as written, and only line 1 carries it, so line 2 is not marked "in force" by the same reasoning. Whether to keep it and report the definition, or drop it, is a decision.
- Condition: either `ExceptionStatusCode` is absent here, or its use is kept consciously, the definition problem is recorded for the UBL TC write-up, and both lines carry it alike.
- Options: (a, preferred) remove it, since `ValidityPeriod` and `EffectivePeriod` already say the criterion is in force; (b) keep it, add it to line 2, and record the definition for the TC.
- Needs decision: yes
- From: context (broad refuted it, see Why)

### furniture/05#F9 · Low · Maker's brand on an item for the store's own line
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:SupplyItem/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:SupplyItem/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The description says the set is made for the store's own line, sold under the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`): a private-label product, normally sold under the retailer's brand. The maker's brand points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line.
- Needs decision: yes
- From: broad, context

## Checked and consistent
- Reference: `/ExceptionCriteria/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0570` resolves to `04-TradeItemLocationProfile.xml`; the validity period 2026-03-16 to 2026-08-29 equals its period.
- Line 1's effective period starts `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:EffectivePeriod/cbc:StartDate` = `2026-03-23`, after the first delivery (invoice `09-Invoice.xml` of 2026-03-22), and is the start of the observation period of `07-ExceptionNotification.xml`.
- Line 2: seller forecast (`DataSourceCode` SELLER) compared with the buyer's plan (`ComparisonDataSourceCode` BUYER), deviation greater than 30 % (`P1`), over 28 days; the codes agree with its note "Forecast far from the store's own plan."
- Priority HIGH and resolution REVIEW of line 1 are the values `07-ExceptionNotification.xml` reports.
- Item identification matches the rest of the flow (BF-GS-01, GTIN 9523710000012, check digit passes with `check_ids.py`, re-run by the merge); party data are identical to the other examples of the flow (parties part).

## Considered and refuted
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:EffectivePeriod/cbc:StartDate` = `2026-03-23`: a line starting a week after the document's validity suspected to be inconsistent — refuted because a line may come into effect later; the first week after delivery is a plausible run-in (from context).
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cbc:ThresholdQuantity` = `30` in percent: a percentage as a "quantity" — refuted because `ThresholdQuantity` with unit percent is a quantity in UBL terms and fits a forecast variance (from context).
- `/ExceptionCriteria/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat sender and receiver — refuted because sender and receiver are the message parties while buyer and seller state the trade relationship, as UBL designs these documents (from parties).
- `/ExceptionCriteria/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge) (from parties).
- `/ExceptionCriteria/cac:ReceiverParty/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/ExceptionCriteria/cac:ReceiverParty/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact as receiver of a planning document — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/ExceptionCriteria/cac:ReceiverParty/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/ExceptionCriteria/cac:SenderParty/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F5 (from parties).
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ExceptionStatusCode` = `ACTIVE`: refuted by broad (carried-over word in UBL's definition); kept by the merge as F8.
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdValueComparisonCode` = `LT`: refuted by broad (world's own list, same meaning); kept by the merge as part of F7.
- `/ExceptionCriteria/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F6 by the merge.

## Changed in the merge
- broad/F1, context/F3, logistics/F1 → F1: combined at Medium (broad); context and logistics had Low. Medium because information the document's purpose depends on (the interval of the threshold) is missing (section 6); the note XPath of logistics and the options of all three added.
- broad/F2, context/F1, logistics/F2 → F2: combined at Medium (broad, context); logistics had Low. Medium because the line declares itself of two exception types, against the definition.
- broad/F3, context/F2, parties/F1 → F3: combined; preferred option set to removal, broad's `en-XB` kept as option (b).
- broad/F5, parties/F2 → F4: combined.
- context/F6, parties/F3, parties/F4 → F5: grouped as one problem (master data in a document that does not use it).
- parties' refuted RegistrationDate → F6: made a finding (Low, needs decision) for alignment with the earlier flows.
- logistics/F3 → F7: kept Low/yes; broad's refutation of the comparison code carried into Why.
- context/F4 → F8: kept Low/yes; broad's refutation carried into Why.
- broad/F4, context/F5 → F9: combined.
