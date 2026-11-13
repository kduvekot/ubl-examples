# LLM review: 10-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/10-Order.xml`, Git blob `4c325d25cd05fed989cbd0f6f69ef7970de5cb48` (committed)
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

### furniture/10#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/10#F2 · Low · A repeat order of 20 sets against the agreed replenishment policy
- XPath: `/Order/cbc:IssueDate` = `2026-04-16`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20`
- Why: The store's replenishment profile `04-TradeItemLocationProfile.xml` sets a target inventory of 10 sets and a reorder point of 4 (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10`, `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MinimumInventoryQuantity` = `4`). The first 20 sets were invoiced on 2026-03-22 and only 3 were sold up to 2026-04-20 (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cbc:Quantity` = `3`), so on 2026-04-16 the store held at least 17 sets, well above target. A second order of 20 sets has no reason in the situation the flow describes; the cancellation `11-OrderCancellation.xml` six days later even calls them "not needed".
- Condition: the repeat order follows from the stock situation and the profile (e.g. it is placed when stock reaches the reorder point, for the quantity that restores the target), or the story gives another reason for it (e.g. a planned promotion or a seasonal pre-order), stated in the order.
- Options: (a) give the order a stated reason, such as a pre-order for the summer peak placed before the slow figures were known (preferred: keeps the cancellation story); (b) lower the quantity and date it to the reorder point.
- Needs decision: yes

### furniture/10#F3 · Low · Quotation line reference without the quotation
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- Why: `QuotationLineReference` is "A reference to a quotation line associated with this order line". This order has no `QuotationDocumentReference` (its header refers to the earlier order, `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574`), and the line reference names no document. "Line 1" therefore cannot be resolved from this order: the reader has to guess that it means line 1 of quotation `BF-DOC-26-0568` via the earlier order.
- Condition: the quotation whose line is referenced is identified in this order (by `QuotationDocumentReference` or the line reference's own document reference), or the line reference is absent.
- Options: (a) add `QuotationDocumentReference` `BF-DOC-26-0568` next to the order reference (preferred: the repeat order is still priced as quoted); (b) remove the line reference.
- Needs decision: no

### furniture/10#F4 · Low · "Original" price identical to the price
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610`
- Why: `OriginalItemLocationQuantity` is "An original set of location-specific properties (e.g., price and quantity) associated with this item". It equals the line price; the repeat-order discount is a separate allowance on the line, not a different price. The aggregate adds nothing that the note `Price as quoted.` does not already say.
- Condition: `OriginalItemLocationQuantity` is absent, or its price differs from the line price for a reason the story gives.
- Options: (a) remove it (preferred).
- Needs decision: no

### furniture/10#F5 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Note` = `The store's own line: bench and two chairs per set.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the note unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the texts.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/10#F6 · Low · Buyer's master data copied into the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in an order (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `OrderDocumentReference` ("A reference to another Order") resolves to `08-Order.xml`, the order this one repeats.
- The repeat-order allowance (3 % of 12200 = 366, line 11834) fits the order's purpose; the rest of the line repeats `08-Order.xml`.

## Considered and refuted
- `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.` next to a 3 % discount — refuted as a contradiction because the price itself is the quoted 610; the discount is an allowance on top.
