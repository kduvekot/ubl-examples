# LLM review: 04-TradeItemLocationProfile.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/04-TradeItemLocationProfile.xml`, Git blob `666a857de25e67c953a50e5da8e5c010b96c5933` (committed)
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

### furniture/04#F1 · Medium · ReplenishmentOwnerDescription describes a process, and contradicts the note
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:ReplenishmentOwnerDescription` = `The store orders; the maker proposes.`
- XPath: `/TradeItemLocationProfile/cbc:Note` = `The store holds stock; the maker replenishes.`
- Why: `ReplenishmentOwnerDescription` is "The trading partner maintaining this item management profile". The value describes a division of work, not a trading partner. It also does not agree with the document note: the note says the maker replenishes, the description says the store orders and the maker only proposes. In the flow the store issues the orders (`08-Order.xml`, `10-Order.xml`) and sends this profile itself.
- Condition: `ReplenishmentOwnerDescription` names the trading partner that maintains the profile, and the note and the description state the same replenishment arrangement.
- Options: (a, preferred) `ReplenishmentOwnerDescription` naming Brightmarket Stores (the sender, who orders), and a note that matches ("The store holds stock and orders; the maker proposes quantities"); (b) if the maker is meant to replenish (vendor-managed), name Brackenmere and let the orders follow from that.
- Needs decision: no

### furniture/04#F2 · Medium · Price-break minimum used as a minimum order quantity
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:MinimumQuantity` = `2`
- Why: In `ItemLocationQuantity`, `MinimumQuantity` is "The minimum quantity that can be ordered to qualify for a specific price". The aggregate carries no price, so there is no price to qualify for; the value is used as a minimum order quantity, which `MultipleOrderQuantity` (2 SET) already covers.
- Condition: `ItemLocationQuantity/cbc:MinimumQuantity` is present only together with the price it qualifies for, or is absent.
- Options: (a, preferred) remove it, as `MultipleOrderQuantity` states the ordering step; (b) add the price that applies from 2 sets if a price break is meant.
- Needs decision: no

### furniture/04#F3 · Medium · Language code in LocaleCode
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TradeItemLocationProfile/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/04#F4 · Low · Own-line item carries the maker's brand
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/04#F5 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- Profile quantities agree with each other: minimum inventory 4 SET below target inventory 10 SET, ordering in multiples of 2 SET, order interval 14 days, lead time 5 days.
- Lead time 5 days against the flow: order `08-Order.xml` on 2026-03-16, invoice `09-Invoice.xml` on 2026-03-22.
- `/TradeItemLocationProfile/cac:Period/cbc:StartDate` = `2026-03-16` to `2026-08-29`, identical to the effective period of the profile and the validity of `05-ExceptionCriteria.xml`.
- `/TradeItemLocationProfile/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`.

## Considered and refuted
- `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:FrozenPeriodDaysNumeric` = `7`: suspected filler without forecasts — refuted because `07-ExceptionNotification.xml` refers to a seller forecast issued on 2026-03-16, so order forecasts exist in the world.
- `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10` against the first order of 20 sets: refuted, an opening order at season start may exceed the running target.
