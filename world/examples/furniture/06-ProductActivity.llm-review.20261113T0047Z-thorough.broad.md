# LLM review: 06-ProductActivity.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/06-ProductActivity.xml`, Git blob `b8bd3b68d78e4195bf7df8c905e21d85b0c22321` (committed)
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

### furniture/06#F1 · Medium · Language code in LocaleCode
- XPath: `/ProductActivity/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProductActivity/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/06#F2 · Low · Four-week aggregate although weekly figures were requested
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityPeriod/cbc:EndDate` = `2026-04-20`
- XPath: `03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:TimeFrequencyCode` = `WEEKLY`
- Why: The request this report answers (`/ProductActivity/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0569`) asks for weekly figures (`TimeFrequencyCode` WEEKLY, note "Weekly figures, please, for the whole season"). This report gives one figure, 3 sets, for four weeks. Either the weekly reports are missing or the report does not answer the request as asked.
- Condition: The activity report's periods match the requested weekly frequency (one data line or one report per week), or the request asks for four-weekly figures.
- Options: (a, preferred) one `SupplyChainActivityDataLine` per week of the period (the four values adding up to 3 sets), which also lets 07 compare against the criterion; (b) change the request to four-weekly reporting.
- Needs decision: no

### furniture/06#F3 · Low · Final location is the customers' gardens
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityFinalLocation/cbc:Name` = `Customers' gardens in Lumeport`
- Why: `ActivityFinalLocation` is "The location to which the goods are moved". For retail sales the store does not know or report where customers take their goods; "Customers' gardens in Lumeport" is not a location anyone can use, and nothing in the flow uses it (IND5).
- Condition: `ActivityFinalLocation` is absent, or names a real location the goods are moved to (e.g. a store-to-store transfer).
- Options: (a, preferred) remove it; the origin location (the garden department) is enough for sales.
- Needs decision: no

### furniture/06#F4 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/ProductActivity/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ProductActivity/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ProductActivity/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxInclusivePrice/cbc:PriceAmount` = `957.44`: 899 × 1.065 = 957.435, rounded 957.44, i.e. a 6.5 % state sales tax; 6.5 % is the STT rate used elsewhere in the examples (seven `cbc:Percent` values of 6.5 next to a standard-rated `S` category, counted with `grep -B3 -A8` on the category ID over `*.xml`).
- Retail price 899 against the purchase price 610 in `08-Order.xml`: a plausible retail margin.
- The reported 3 sets and the period 2026-03-23 to 2026-04-20 are exactly what `07-ExceptionNotification.xml` compares (source value 3 SET, same observation period), and the period starts on the effective date of criterion line 1 in `05-ExceptionCriteria.xml`.
- GLN `9522610900026` of the garden department: check digit correct (check_ids.py).

## Considered and refuted
- `/ProductActivity/cbc:Note` and `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:ActivityProperty/cbc:Value`: two explanations (end of promotion, rain) — refuted, they do not contradict each other.
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:Name`: name contains the company name — refuted, the location is a department of the store, and the name identifies the place.
