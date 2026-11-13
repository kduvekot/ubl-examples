# LLM review: 08-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/08-Order.xml`, Git blob `01257b4f8b6e604e5ea78070a814e95bca35ab3d` (committed)
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

### furniture/08#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode` (context, parties, earlier flows); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/08#F2 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores is the buyer of the order. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact of a buyer. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/08#F3 · Low · Store master data copied into the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo reference, online-shop website, photo-sharing profile and share capital are master data; an order for garden sets does nothing with any of them (section 4.8). The order's line note mentions the store's own line, but nothing in the order ties the logo to a label (no line, attachment or note uses it); in 01 and 02 the parties part refuted the logo for the sourcing documents on that ground, and the merge kept it there as the weakest part. The same four elements are carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: these elements are present only where the document has a reason for them; a logo kept for the own label is tied to it in the document.
- Options: (a, preferred) remove them; (b) keep the logo only if the order uses it for the own-label artwork, and say so.
- Needs decision: no
- From: context, parties

### furniture/08#F4 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/08#F5 · Low · The order says neither when nor, by identifier, where to deliver
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: The order is the document the delivery is made against, but its `Delivery` names only the receiving party (no address), with no `DeliveryLocation` and no requested delivery date or period. The place appears only as free text under the delivery terms, although the request for quotation identified the store's goods-in by GLN (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Brightmarket Stores, goods-in`), and the store's other orders do the same (`retail/08-Order.xml`). A location identified elsewhere should carry the same identifier. The delivery time is left to the lead time of the profile (5 days, `04-TradeItemLocationProfile.xml`), which the order does not refer to; the goods were delivered within a week (the invoice `09-Invoice.xml` is dated 2026-03-22), so the information existed. Low, not Medium: an order can rely on the agreed lead time and DAP terms (same judgement as merger B for 10 and 15).
- Condition: the order's delivery identifies the goods-in location by its GLN `9522610900019` (and its name), and either carries a requested delivery date or period or refers to the agreed lead time.
- Options: (a, preferred) `Delivery/DeliveryLocation` with ID and name as in 01, and a `RequestedDeliveryPeriod` (e.g. 2026-03-19 to 2026-03-21, inside the 5-day lead time); the Incoterms place can then refer to it; (b) at least the GLN on the existing `DeliveryTerms/DeliveryLocation`, and a note that delivery follows the agreed lead time.
- Needs decision: no
- From: broad, logistics, parties

### furniture/08#F6 · Low · Line item UUID that nothing uses
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:UUID` = `4278e92c-6141-5575-b08f-555e19cf4b75`
- Why: `LineItem/UUID` is "A universally unique identifier for this line item". It is useful when another document refers to the line item by it; no example does (Grep for `4278e92c` over `world/examples/*/*.xml` finds only this file, re-run by the merge), and the repeat order `10-Order.xml` has no line item UUID. The line is already identified by its `ID` and the order number. Without a use it is a filler (IND5).
- Condition: the line item UUID is absent, or a document of the flow refers to it.
- Options: (a, preferred) remove it; (b) let the invoice or credit note refer to the line by it.
- Needs decision: no
- From: context

### furniture/08#F7 · Low · Initial order of twice the target inventory
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:MaximumQuantity` = `20`
- XPath: `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10`
- Why: The replenishment profile that takes effect on the order day (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cac:EffectivePeriod/cbc:StartDate` = `2026-03-16`) sets a target inventory of 10 sets and a reorder point of 4. The first order brings the store to 20 sets, twice the target. Opening stock for a season can exceed the running target (the broad part refuted the same question in its review of 04 on that ground), but neither document says so, and the later story (slow sales, a repeat order cancelled, six sets taken back so that 11 remain) reads as a consequence of exactly this overstock. The profile is a policy, not a statement the order contradicts, so the merge cannot settle it.
- Condition: the initial quantity and the target inventory are consistent, or a note explains why the opening order exceeds the target (e.g. stock for a launch promotion, cf. `06-ProductActivity.xml` "after the promotion ended").
- Options: (a, preferred) a note in the order or the profile that the opening order covers a launch promotion, which keeps the story and its amounts; (b) lower the initial quantity to the target (10 sets), which changes the invoice, the return and the credit note.
- Needs decision: yes
- From: logistics (broad refuted the question in 04, see Why)

### furniture/08#F8 · Low · "Original" price identical to the price, next to a note that says so
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610`
- XPath: `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.`
- Why: `PricingReference/OriginalItemLocationQuantity` is "An original set of location-specific properties (e.g., price and quantity) associated with this item"; it says something when the price ordered differs from an original one. Here the original price equals the price, and the note and the quotation line reference already say the price is the quoted one. The money part refuted this: with the note "Price as quoted.", the pricing reference is the quoted price the order relies on, and a reference equal to the price is a legitimate statement that no change was made. The merge keeps it at Low: the statement is already made twice (note and `QuotationLineReference`), so the aggregate adds no information (IND5).
- Condition: `OriginalItemLocationQuantity` is absent, or its price differs from the line price for a reason the story gives.
- Options: (a, preferred) remove the pricing reference; (b) keep it only in an order whose price departs from the quotation.
- Needs decision: no
- From: broad, context (money refuted it, see Why)

### furniture/08#F9 · Low · Maker's brand on an item for the store's own line
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Note` = `The store's own line: bench and two chairs per set.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The line note and the description describe the store's own line, sold under the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`), and the store has its own item number for it (`/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:BuyersItemIdentification/cbc:ID` = `BM-551004`): a private-label product, normally sold under the retailer's brand. The maker's brand points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName` (the GTIN may then also be the store's); (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line.
- Needs decision: yes
- From: broad, context

### furniture/08#F10 · Low · Sub-line prices without the quantity they apply to
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cac:Price/cbc:PriceAmount` = `380`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[2]/cac:Price/cbc:PriceAmount` = `115`
- Why: `BaseQuantity` is "The quantity at which this price applies". The main line states it (`/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`, unit SET); the two sub-line prices do not, so "per one piece" is only implied by absence (IND6). The arithmetic works with a base of 1 EA (20 × 380 = 7600.00; 40 × 115 = 4600.00). Across the examples, 12 of the 117 `Price` elements with a `PriceAmount` have no `BaseQuantity`, in 6 files (money part, counted with a script over `world/examples/*/*.xml`).
- Condition: every `Price` in the order states the quantity it applies to, or the convention that a missing base quantity means one unit of the line's unit is recorded as a deliberate decision.
- Options: (a, preferred) add `BaseQuantity` 1 EA to both sub-line prices, matching the main line; (b) record the convention.
- Needs decision: no
- From: money

### furniture/08#F11 · Low · Quotation line referenced twice
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:LineReference/cbc:LineID` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:LineReference/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568`
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- Why: The order line has the dedicated `QuotationLineReference` ("A reference to a quotation line associated with this order line"), and the line item additionally has a generic `LineReference` ("A reference to a line in a document associated with this line item") to line 1 of the same quotation `BF-DOC-26-0568`. The two references say the same thing; the generic one adds no information the order uses (IND5).
- Condition: the quotation line is referenced once, by `QuotationLineReference` (with its document through `/Order/cac:QuotationDocumentReference`).
- Options: (a, preferred) remove the `LineItem/LineReference`; (b) none other seen.
- Needs decision: no
- From: broad, context

## Checked and consistent
- Main line (recalculated by the merge): 20 sets × 610 = 12200.00 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `12200.00` = `/Order/cac:OrderLine/cac:LineItem/cac:ItemPriceExtension/cbc:Amount` = `12200.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `12200.00`.
- Bill of materials: sub-lines 20 benches × 380 = 7600.00 and 40 chairs × 115 = 4600.00, sum 12200.00; per set 380 + 2 × 115 = 610; 40 chairs = two per set, as the note says.
- Tax: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00`, exempt category E, rate 0, `RESALE` for a store buying its own-label line for resale; 0.00 at document and line level (`/Order/cac:OrderLine/cac:LineItem/cac:TaxTotal/cbc:TaxAmount` = `0.00`); the same treatment in 09-Invoice and 13-CreditNote.
- Quantity bounds: minimum 10 ≤ quantity 20 ≤ maximum 20; back order allowed, minimum 5 ≤ maximum 10 (= 20 − 10); all multiples of the order multiple 2 of the profile.
- Reference: `/Order/cac:QuotationDocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`; quotation line 1 exists; item, quantity and price (`02-Quotation.xml:/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610`) agree; the order (2026-03-16) lies within the quotation's validity (to 2026-05-05).
- `WarrantyParty` = the maker with a two-year `WarrantyValidityPeriod`: fits a maker's warranty. `AccountingCostCode` 6120 / `AccountingCost` "Garden department" is the buyer's own cost centre, as defined, at header and line.
- Codes: OrderTypeCode 220, DAP, SET, EA, ANN resolve; GS1 check digits pass (`check_ids.py`, re-run by the merge); party data are identical to the other examples of the flow (parties part).

## Considered and refuted
- `/Order/cbc:AccountingCostCode` and `/Order/cac:OrderLine/cac:LineItem/cbc:AccountingCostCode`: duplicated — refuted because header and line cost codes are both defined and may coincide (from broad).
- `/Order/cac:OrderLine/cac:LineItem/cac:ItemPriceExtension/cbc:Amount` = `12200.00`: equal to the line extension amount, suspected filler — refuted because the two have different definitions (price × quantity versus amount including allowances) and coincide without allowances (from context).
- `/Order/cac:OrderLine/cac:LineItem/cbc:InspectionMethodCode` = `VISUAL`: suspected without purpose — refuted because goods-in inspection of furniture is a real requirement of the buyer (from context).
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID` = `STT`: the state whose exemption applies is not stated (seller in Upland State, buyer and delivery in Coastal State) — refuted because no tax is due under either state, the parties' tax schemes name their jurisdictions, and no tax category in the examples carries a jurisdiction (from money).
- `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cbc:LineExtensionAmount` = `7600.00`: double counting of sub-lines with the main line — refuted because the totals use only the main line; the sub-lines break it down and sum to it (from money).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name`: the delivery party equals the buyer — refuted because `DeliveryParty` ("The party to whom goods should be delivered") has no "if different" condition, and the order has no other place naming the receiving party (from parties).
- `/Order/cac:OrderLine/cac:LineItem/cac:WarrantyParty/cac:PartyName/cbc:Name`: the warranty party equals the seller — refuted because Brackenmere makes the furniture and gives the two-year warranty itself (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge) (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F3 (from parties).
- `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`: filler repeating the line price — refuted by money (statement that nothing changed); kept by the merge as F8.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F4 by the merge.

## Changed in the merge
- broad/F1, context/F1, parties/F1 → F1: combined; preferred option set to removal, broad's `en-XB` kept as option (b).
- broad/F5, parties/F3 → F2: combined.
- context/F6, parties/F4 → F3: grouped into one finding, one XPath line per element.
- parties' refuted RegistrationDate → F4: made a finding (Low, needs decision) for alignment with the earlier flows.
- broad/F4, logistics/F1, parties/F2 → F5: combined; the missing delivery date of logistics included.
- context/F2 → F6: kept.
- logistics/F2 → F7: kept Low/yes; broad's refutation in 04 added.
- broad/F3 (pricing part), context/F3 → F8: split from broad/F3, which also covered the double line reference, because the money part refuted the pricing part only; money's refutation carried into Why.
- broad/F2, context/F5 → F9: combined.
- money/F1 → F10: kept.
- broad/F3 (reference part), context/F4 → F11: combined.
