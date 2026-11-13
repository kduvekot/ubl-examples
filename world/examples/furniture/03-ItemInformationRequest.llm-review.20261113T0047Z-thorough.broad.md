# LLM review: 03-ItemInformationRequest.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/03#F1 · Medium · One request line asks for activity, forecast and metric data at once
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:ForecastTypeCode` = `TOTAL`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: The UBL definition of `ForecastTypeCode` in this line reads: "The information request can be either about supply chain activity or about forecasts or about performance metrics, so it will be optional": a line asks for one of the three kinds. This line sets all three. The note asks for "Weekly figures, please, for the whole season", i.e. sales activity, and the answer `06-ProductActivity.xml` is a Product Activity with `SupplyChainActivityTypeCode` SALES only; no forecast or performance history is sent in the flow. The forecast and metric codes therefore have no counterpart.
- Condition: Each Item Information Request line asks for one kind of information (activity, forecast or metric), and every kind requested is answered or at least plausible in the flow.
- Options: (a, preferred) keep only `SupplyChainActivityTypeCode` SALES, which is what the note and 06 match; (b) split into separate lines per kind if forecasts or metrics are meant to be requested too.
- Needs decision: no

### furniture/03#F2 · Medium · Language code in LocaleCode
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/03#F3 · Low · Own-line item carries the maker's brand
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/03#F4 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/ItemInformationRequest/cac:Period/cbc:StartDate` = `2026-03-16` to `2026-05-11`: eight weeks of the season, starting on the day of the first order `08-Order.xml`; the request (2026-03-12) precedes it.
- Roles: `BuyerCustomerParty` ("The Buyer from whom the Item Information is requested") is the receiver Brightmarket, `SellerSupplierParty` ("The Seller requesting") is the sender Brackenmere; consistent.
- `/ItemInformationRequest/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`; the reply `06-ProductActivity.xml` references this request.
- GS1 check digits (check_ids.py).

## Considered and refuted
- `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cbc:Quantity` = `20`: suspected meaningless in a request — refuted because "The quantity the given information are related to" can be the 20 sets quoted and ordered, which is what the request concerns.
