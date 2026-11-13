# LLM review: 03-ItemInformationRequest.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/03-ItemInformationRequest.xml`, Git blob `831fa39b706e496e223832845d95a8ebe56ea67b` (committed)
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

### furniture/03#F1 · Medium · One request line asks for activity, forecast and performance metric at once
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:ForecastTypeCode` = `TOTAL`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: The UBL definition of `ForecastTypeCode` in this line states the model's intent: "The information request can be either about supply chain activity or about forecasts or about performance metrics, so it will be optional". The three codes are alternatives that say which kind of information a line asks for; this line sets all three, so it asks at once for actual sales, a total forecast and a sales-in-units metric, and does not say which kind is meant. The note asks for weekly figures, and the answer `06-ProductActivity.xml` reports actual sales only (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cbc:SupplyChainActivityTypeCode` = `SALES`); no forecast and no performance history is sent anywhere in the flow (no Forecast or performance document in `world/examples/furniture/*.xml`). The merge tried the reading that the forecast and metric codes merely qualify the sales request; the definition rules it out, since it presents the three as either/or.
- Condition: each request line asks for one kind of information (activity, forecast or metric); a second kind, if wanted, is a line of its own and is answered in the flow.
- Options: (a, preferred) keep only `SupplyChainActivityTypeCode` = `SALES`, which is what the note asks and 06 answers; (b) split into separate lines per kind and add the answering documents to the flow.
- Needs decision: no
- From: broad, context, logistics

### furniture/03#F2 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode` (context, parties, earlier flows); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/03#F3 · Low · "For the whole season" against a request period of eight weeks
- XPath: `/ItemInformationRequest/cbc:Note` = `Weekly figures, please, for the whole season.`
- XPath: `/ItemInformationRequest/cac:Period/cbc:EndDate` = `2026-05-11`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:Period/cbc:EndDate` = `2026-05-11`
- Why: The note asks for figures for the whole season, but the request's `Period` ("The period of time to which the Item Information Request applies") and the line's period run from Monday 2026-03-16 to Monday 2026-05-11. The season of the item, as the store's replenishment profile and exception criteria define it, runs to 2026-08-29 (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:Period/cbc:EndDate` = `2026-08-29`; the same end in `05-ExceptionCriteria.xml:/ExceptionCriteria/cac:ValidityPeriod/cbc:EndDate` = `2026-08-29`). Text and structured period disagree. Moreover, for weekly figures from a Monday, eight full weeks end on Sunday 2026-05-10; 2026-03-16 + 56 days = 2026-05-11 adds one day of a ninth week (recalculated by the merge: 2026-03-16 and 2026-05-11 are both Mondays).
- Condition: the note and the periods describe the same span, and the period ends on a week boundary if weekly figures are requested.
- Options: (a) reword the note to the first eight weeks and end the periods on 2026-05-10 (context's preference: keeps the flow unchanged); (b) extend the periods to the end of the season (2026-08-29, or the last Sunday before it), matching the note and the replenishment profile (logistics' preference). The merge prefers neither: (a) is the smaller change, (b) matches the profile.
- Needs decision: no
- From: context, logistics

### furniture/03#F4 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/ItemInformationRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/03#F5 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores is the buyer from whom the sales figures are requested. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the store's contact for supplier collaboration. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying or planning contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/03#F6 · Low · Party master data copied into a request for sales figures
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo reference, online-shop website, photo-sharing profile, share capital (with the fully-paid-shares indicator) and both parties' state-sales-tax registrations are master data. This document carries no amounts, no tax treatment, no payment and no label: a request for sales figures does nothing with any of them (section 4.8). The store's four marketing and capital elements are carried on Brightmarket Stores in examples 01 to 14 of the flow. (The parties part refuted the logo for the sourcing documents 01 and 02 because of the own label; that argument does not reach a request for sales figures.)
- Condition: these elements are present only in documents that have a reason to carry them.
- Options: (a, preferred) remove them here, keeping identification, name, address, contact and electronic address; (b) keep any of them only with a reason the document states (none is apparent).
- Needs decision: no
- From: context, parties

### furniture/03#F7 · Low · Maker's brand on an item for the store's own line
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The description says the set is made for the store's own line, sold under the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`): a private-label product, normally sold under the retailer's brand. The maker's brand points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line.
- Needs decision: yes
- From: broad, context

## Checked and consistent
- Roles: `BuyerCustomerParty` ("The Buyer from whom the Item Information is requested") is the receiver Brightmarket and `SellerSupplierParty` ("The Seller requesting the Item Information") the sender Brackenmere, as the definitions say.
- Reference: `/ItemInformationRequest/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`; item and parties agree. The reply `06-ProductActivity.xml` references this request.
- Dates: the request (2026-03-12) precedes the period start `/ItemInformationRequest/cac:Period/cbc:StartDate` = `2026-03-16`, the day of the first order `08-Order.xml`.
- Codes: `TimeFrequencyCode` WEEKLY ("the frequency with which item information will be sent to the requester") fits the note; SALES and SET resolve in their lists; GS1 check digits pass (`check_ids.py`, re-run by the merge).
- Party data are identical to the other examples of the flow; register number, `CompanyID` and electronic-address suffix agree per party (parties part).

## Considered and refuted
- `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cbc:Quantity` = `20`: a quantity in a request for figures suspected to be meaningless — refuted because `SalesItem/Quantity` is mandatory ("The quantity the given information are related to") and 20 sets is the quantity quoted in `02-Quotation.xml` and ordered in `08-Order.xml`, the stock the figures relate to (from broad, context, logistics).
- `/ItemInformationRequest/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat the receiver and sender — refuted because sender and receiver are the message parties while buyer and seller state the trade relationship, as the definitions of this document require; they are given only by identifier and name (from parties).
- `/ItemInformationRequest/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge) (from parties).
- `/ItemInformationRequest/cac:SenderParty/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/ItemInformationRequest/cac:SenderParty/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact as sender of a planning document — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/ItemInformationRequest/cac:SenderParty/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/ItemInformationRequest/cac:ReceiverParty/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F6 (from parties).
- `/ItemInformationRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F4 by the merge.

## Changed in the merge
- broad/F1, context/F1, logistics/F1 → F1: combined; same severity in all parts.
- broad/F2, context/F2, parties/F1 → F2: combined; preferred option set to removal, broad's `en-XB` kept as option (b).
- context/F3, logistics/F2 → F3: combined; both parts' preferred options listed, the merge prefers neither; the week-boundary point (logistics) included.
- parties' refuted RegistrationDate → F4: made a finding (Low, needs decision) for alignment with the earlier flows.
- broad/F4, parties/F2 → F5: combined.
- context/F5, parties/F3, parties/F4 → F6: grouped as one problem (master data copied into a document that does not use it), one XPath line per element.
- broad/F3, context/F4 → F7: combined.
