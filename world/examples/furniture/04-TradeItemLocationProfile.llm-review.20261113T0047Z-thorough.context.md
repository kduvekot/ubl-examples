# LLM review: 04-TradeItemLocationProfile.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/04#F1 · Medium · MinimumQuantity used as a minimum order quantity without any price
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:MinimumQuantity` = `2`
- Why: Under `ItemLocationQuantity`, `MinimumQuantity` is defined as "The minimum quantity that can be ordered to qualify for a specific price". The `ItemLocationQuantity` here has no `Price` at all, so there is no specific price to qualify for; the value (2 sets, equal to `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MultipleOrderQuantity` = `2`) is used as a plain minimum order quantity, which is not what the element means in this parent.
- Condition: `ItemLocationQuantity/MinimumQuantity` is present only together with the price it qualifies for, or is absent; a plain minimum or multiple order quantity is carried by `MultipleOrderQuantity` (already present).
- Options: (a) remove `MinimumQuantity` and rely on `MultipleOrderQuantity` (preferred); (b) add the price the minimum qualifies for, if the story has a quantity price.
- Needs decision: no

### furniture/04#F2 · Medium · LocaleCode holds a bare language code
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TradeItemLocationProfile/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/04#F3 · Low · Who replenishes: the two texts disagree, and neither names the profile's owner
- XPath: `/TradeItemLocationProfile/cbc:Note` = `The store holds stock; the maker replenishes.`
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:ReplenishmentOwnerDescription` = `The store orders; the maker proposes.`
- Why: `ReplenishmentOwnerDescription` is "The trading partner maintaining this item management profile": it should name the partner that maintains the profile. The value instead describes a division of tasks, and that description disagrees with the document note: one says the maker replenishes (vendor-managed), the other that the store orders and the maker only proposes. The rest of the flow follows the second reading (the store issues the orders `08-Order.xml` and `10-Order.xml`).
- Condition: `ReplenishmentOwnerDescription` names the partner maintaining the profile, and the note and the description agree on who decides replenishment.
- Options: (a) `ReplenishmentOwnerDescription` = the store (the sender of this profile) and a note that says the store orders on the maker's proposals (preferred: matches the orders of the flow); (b) a vendor-managed story, which would change who issues the orders.
- Needs decision: yes

### furniture/04#F4 · Low · Frozen period for forecasts in a flow where the store orders itself
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:FrozenPeriodDaysNumeric` = `7`
- Why: `FrozenPeriodDaysNumeric` is "The number of days in the future that an order forecast quantity automatically becomes a confirmed order for a product". That presupposes order forecasts that turn into orders automatically. In this flow the store places explicit orders (`08-Order.xml`, `10-Order.xml`, and cancels the second with `11-OrderCancellation.xml`); no order forecast is exchanged, and the profile itself says "The store orders". A frozen period has nothing to act on.
- Condition: either the flow has order forecasts that become orders within the frozen period, or `FrozenPeriodDaysNumeric` is absent.
- Options: (a) remove it (preferred: keeps the story of explicit orders); (b) add forecasts to the story.
- Needs decision: yes

### furniture/04#F5 · Low · A location profile without the location
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity`
- Why: The document is "A document specifying trade item attributes relating to replenishment policies", per location of the item (its name, and `ItemLocationQuantity` "A set of location-specific properties"). The profile names no location: neither the store's goods-in (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`) nor the garden department where the stock is sold (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:ID` = `9522610900026`). The inventory levels (minimum 4, target 10 sets) are meaningless without saying where that stock is held.
- Condition: the profile says for which location its quantities apply (e.g. through `ItemLocationQuantity/ApplicableTerritoryAddress` or the item's location), or the story makes clear it covers the store's only stock point.
- Options: (a) add the store location the profile applies to (preferred); (b) state it in the note.
- Needs decision: no

### furniture/04#F6 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/04#F7 · Low · Sender's master data copied into the profile
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:AdditionalWebSite`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:SocialMediaProfile`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in a replenishment profile (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `ProfileStatusCode` = `ACTIVE` with `Period` 2026-03-16 to 2026-08-29 and the profile's `EffectivePeriod` the same: consistent with each other and with the exception criteria `05-ExceptionCriteria.xml`.
- `MinimumInventoryQuantity` 4, `TargetInventoryQuantity` 10, `MultipleOrderQuantity` 2, `OrderIntervalDaysNumeric` 14, `LeadTimeMeasure` 5 days, `TargetServicePercent` 95: each fits its definition and they fit together (minimum below target, multiples of 2 reach the target).

## Considered and refuted
- `/TradeItemLocationProfile/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568`: a profile referring to the quotation was suspected to be a reference without purpose — refuted because the profile sets replenishment for the item and terms quoted there.
