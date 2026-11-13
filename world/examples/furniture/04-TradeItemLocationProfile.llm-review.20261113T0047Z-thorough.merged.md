# LLM review: 04-TradeItemLocationProfile.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/04-TradeItemLocationProfile.xml`, Git blob `666a857de25e67c953a50e5da8e5c010b96c5933` (committed)
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

### furniture/04#F1 · Medium · ReplenishmentOwnerDescription describes a division of work, not the partner maintaining the profile
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:ReplenishmentOwnerDescription` = `The store orders; the maker proposes.`
- XPath: `/TradeItemLocationProfile/cbc:Note` = `The store holds stock; the maker replenishes.`
- Why: `ReplenishmentOwnerDescription` is "The trading partner maintaining this item management profile". The value describes who does what, not a trading partner, so the element carries a meaning other than its definition. In addition, the two texts read differently: the note says the maker replenishes (as in vendor-managed inventory), the description that the store orders and the maker only proposes. The flow follows the second reading: the store issues the orders (`08-Order.xml`, `10-Order.xml`) and sends this profile itself. The logistics part refuted the contradiction (both can hold: the store places the orders, the maker supplies them); the merge accepts that the texts can be reconciled and therefore keeps the text disagreement only as part of this finding, while the misuse of the element stands on its own.
- Condition: `ReplenishmentOwnerDescription` names the trading partner that maintains the profile, and the note and the description state the same replenishment arrangement.
- Options: (a, preferred) `ReplenishmentOwnerDescription` naming Brightmarket Stores (the sender, who orders), and a note that matches ("The store holds stock and orders on the maker's proposals"), which keeps the orders of the flow; (b) a vendor-managed story with Brackenmere as owner, which would change who issues the orders.
- Needs decision: no
- From: broad, context (logistics refuted the contradiction part)

### furniture/04#F2 · Medium · MinimumQuantity "to qualify for a specific price" without any price
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:MinimumQuantity` = `2`
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MultipleOrderQuantity` = `2`
- Why: Under `ItemLocationQuantity`, `MinimumQuantity` is "The minimum quantity that can be ordered to qualify for a specific price". This `ItemLocationQuantity` carries only `LeadTimeMeasure` and `MinimumQuantity`, no `Price`, so there is no specific price to qualify for; the value equals the order multiple and reads as a plain minimum order quantity, which is not what the element means in this parent. The merge tried the reading that the price meant is the quoted 610 per set (`02-Quotation.xml`, referenced by the profile): the profile does not say so, and the quotation's price is not conditional on a minimum, so the price condition would only be implied (IND6).
- Condition: `ItemLocationQuantity/MinimumQuantity` is present only together with the price it qualifies for, or is absent; the ordering step stays in `MultipleOrderQuantity`.
- Options: (a, preferred) remove `MinimumQuantity` and rely on `MultipleOrderQuantity`; (b) add the price the minimum qualifies for (e.g. 610 XBL per set), if the story has a quantity price.
- Needs decision: no
- From: broad, context, logistics

### furniture/04#F3 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TradeItemLocationProfile/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode` (context, parties, earlier flows); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/04#F4 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores sends its replenishment profile as the buyer. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact for replenishment planning with a supplier. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying or replenishment-planning contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/04#F5 · Low · Party master data copied into the replenishment profile
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/TradeItemLocationProfile/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/TradeItemLocationProfile/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo reference, online-shop website, photo-sharing profile, share capital (with the fully-paid-shares indicator) and both parties' state-sales-tax registrations are master data. A replenishment profile carries no amounts, tax treatment, payment or label and does nothing with any of them (section 4.8). The store's four marketing and capital elements are carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: these elements are present only in documents that have a reason to carry them.
- Options: (a, preferred) remove them here, keeping identification, name, address, contact and electronic address; (b) keep any of them only with a reason the document states (none is apparent).
- Needs decision: no
- From: context, parties

### furniture/04#F6 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/TradeItemLocationProfile/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/TradeItemLocationProfile/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/04#F7 · Low · Frozen period for order forecasts in a flow without order forecasts
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:FrozenPeriodDaysNumeric` = `7`
- Why: `FrozenPeriodDaysNumeric` is "The number of days in the future that an order forecast quantity automatically becomes a confirmed order for a product". That presupposes order forecasts that turn into orders automatically. In this flow the store places explicit orders (`08-Order.xml`, `10-Order.xml`, the second cancelled with `11-OrderCancellation.xml`), no Forecast document exists in the flow (searched over `world/examples/furniture/*.xml`), and the profile itself says "The store orders". Two parts saw it otherwise: broad refuted the suspicion because `07-ExceptionNotification.xml` names a seller forecast issued on 2026-03-16, and logistics read "the maker proposes" as proposals that become firm a week ahead. The merge cannot settle it: the forecast named in 07 is no document of the flow (see the review of 07), but the maker's proposals could be such forecasts.
- Condition: either the flow has order forecasts (or proposals) that become orders within the frozen period, or `FrozenPeriodDaysNumeric` is absent.
- Options: (a, preferred) remove it, keeping the story of explicit orders; (b) make the maker's proposals order forecasts in the story and say so.
- Needs decision: yes
- From: context (broad refuted it; logistics found it consistent)

### furniture/04#F8 · Low · Maker's brand on an item for the store's own line
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The description says the set is made for the store's own line, sold under the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`): a private-label product, normally sold under the retailer's brand. The maker's brand points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line.
- Needs decision: yes
- From: broad, context

### furniture/04#F9 · Low · A location profile that does not say for which location
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10`
- Why: The document is "A document specifying trade item attributes relating to replenishment policies", per location of the item (its name, and `ItemLocationQuantity` "A set of location-specific properties"). The profile names no location: neither the store's goods-in (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`) nor the garden department where the stock is sold (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:ID` = `9522610900026`). Inventory levels (minimum 4, target 10 sets) and a lead time say little without where that stock is held. The logistics part refuted this: UBL 2.5 gives this document no location element, and the garden department is identified in 06. The merge keeps it at Low: `ItemLocationQuantity` does offer `ApplicableTerritoryAddress`, and a note can name the stock point; but the refutation shows that a structured location is not available, so no more than Low.
- Condition: the profile says for which location its quantities apply (through `ItemLocationQuantity/ApplicableTerritoryAddress` or a note), or the story makes clear the store has a single stock point for the item.
- Options: (a, preferred) name the stock point (the garden department) in a note or as applicable address; (b) leave it, if the story has only one stock point, and say so.
- Needs decision: no
- From: context (logistics refuted it, see Why)

## Checked and consistent
- Profile quantities (recalculated by the merge): reorder point `MinimumInventoryQuantity` 4 sets below target `TargetInventoryQuantity` 10 sets; replenishing from 4 to 10 needs 6 sets, a whole multiple of the order multiple 2; the lead time of 5 days fits within the order interval of 14 days; `TargetServicePercent` 95 fits its definition.
- Periods: `/TradeItemLocationProfile/cac:Period/cbc:StartDate` = `2026-03-16` to 2026-08-29, identical to the profile's `EffectivePeriod`, to `ProfileStatusCode` ACTIVE and to the validity of `05-ExceptionCriteria.xml`; the profile starts the day of the first order (`08-Order.xml`, 2026-03-16).
- Lead time 5 days against the flow: order `08-Order.xml` on 2026-03-16, invoice `09-Invoice.xml` on 2026-03-22.
- Reference: `/TradeItemLocationProfile/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`.
- GS1 check digits pass (`check_ids.py`, re-run by the merge); party data are identical to the other examples of the flow (parties part).

## Considered and refuted
- `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10` against the first order of 20 sets — refuted here because an opening order at season start may exceed the running target (from broad); the logistics part raised the same question as a finding in the review of `08-Order.xml`, where it is kept as Low with a decision.
- `/TradeItemLocationProfile/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568`: a profile referring to the quotation suspected to be a reference without purpose — refuted because the profile sets replenishment for the item and terms quoted there (from context).
- `/TradeItemLocationProfile/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat sender and receiver — refuted because sender and receiver are the message parties while buyer and seller state the trade relationship, as UBL designs these documents; they are given only by identifier and name (from parties).
- `/TradeItemLocationProfile/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge) (from parties).
- `/TradeItemLocationProfile/cac:ReceiverParty/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/TradeItemLocationProfile/cac:ReceiverParty/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact as receiver of a planning document — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/TradeItemLocationProfile/cac:ReceiverParty/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/TradeItemLocationProfile/cac:SenderParty/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F5 (from parties).
- `/TradeItemLocationProfile/cbc:Note` against `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:ReplenishmentOwnerDescription`: contradiction refuted by logistics; carried into F1, where the merge keeps the element's misuse.
- `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:FrozenPeriodDaysNumeric`: filler without forecasts — refuted by broad; kept by the merge as F7 with both arguments.
- `/TradeItemLocationProfile/cac:ItemManagementProfile`: profile without a location — refuted by logistics; kept by the merge as F9 at Low.
- `/TradeItemLocationProfile/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F6 by the merge.

## Changed in the merge
- broad/F1, context/F3 → F1: combined at Medium (broad) rather than Low (context), because the value does not name a trading partner, which is a meaning other than the element's definition; needs decision set to no (context said yes), because the preferred option keeps the flow's orders as they are; logistics' refutation of the contradiction carried into Why.
- broad/F2, context/F1, logistics/F1 → F2: combined at Medium; logistics had Low. Medium because the element is used without the condition its definition names.
- broad/F3, context/F2, parties/F1 → F3: combined; preferred option set to removal, broad's `en-XB` kept as option (b).
- broad/F5, parties/F2 → F4: combined.
- context/F7, parties/F3, parties/F4 → F5: grouped as one problem (master data in a document that does not use it).
- parties' refuted RegistrationDate → F6: made a finding (Low, needs decision) for alignment with the earlier flows.
- context/F4 → F7: kept Low/yes; the counter-arguments of broad and logistics added.
- broad/F4, context/F6 → F8: combined.
- context/F5 → F9: kept Low/no; logistics' refutation carried into Why; XPath lines changed from the bare aggregate to two of its values so that the citation carries a value.
