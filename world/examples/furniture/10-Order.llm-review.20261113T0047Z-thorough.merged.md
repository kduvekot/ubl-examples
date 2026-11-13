# LLM review: 10-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/10-Order.xml`, Git blob `4c325d25cd05fed989cbd0f6f69ef7970de5cb48` (committed)
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

### furniture/10#F1 · High · Taxable amount ignores the 3 % repeat-order allowance
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `11834.00`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `11834.00`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:Amount` = `366.00`
- Why: `TaxableAmount` is "The net amount to which the tax percent (rate) is applied to calculate the tax amount". Merge recalculation: 20 × 610 = 12200.00; allowance 0.03 × 12200.00 = 366.00; 12200.00 − 366.00 = 11834.00, which is the line and the document line extension amount. The tax subtotal still gives the gross 12200.00, the figure of `08-Order.xml` without the allowance. The tax amount is 0.00 either way (exempt), which hides the error, but the amounts contradict each other.
- Condition: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` equals the sum of the line extension amounts it covers (11834.00).
- Options: set the taxable amount to 11834.00 (the only option that keeps the arithmetic).
- Needs decision: no
- From: broad, money

### furniture/10#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/10#F3 · Low · Repeat order of 20 sets while at least 17 are in stock, against the replenishment profile
- XPath: `/Order/cbc:IssueDate` = `2026-04-16`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20`
- XPath: `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MinimumInventoryQuantity` = `4`
- XPath: `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10`
- XPath: `06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cbc:Quantity` = `3`
- Why: Merge recalculation: 20 sets were invoiced on 2026-03-22 (`09-Invoice.xml`), and 3 sets were sold between 2026-03-23 and 2026-04-20 (`06-ProductActivity.xml`), so on 2026-04-16 the store held between 17 and 20 sets. The profile in force (2026-03-16 to 2026-08-29) has a reorder point of 4 sets and a target of 10, with an order interval of 14 days (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:OrderIntervalDaysNumeric` = `14`; 2026-03-16 + 28 days = 2026-04-13, not 04-16). Another 20 sets would bring stock to 37 to 40, nearly four times the target, and the cancellation `11-OrderCancellation.xml` six days later gives slow sales as the reason, which were already visible on the order day. Logistics rated this High (a contradiction with 04 and 06). Against that: the profile is a policy ("The store orders; the maker proposes"), not a statement the order contradicts, and a store may pre-order for the season outside it; the sales figure is reported after the order date. The merge can neither confirm a hard contradiction nor dismiss the inconsistency, hence Low with a decision.
- Condition: The repeat order follows from the stock the flow implies and the profile in force (stock at or near the reorder point, quantity bringing it to about the target), or the order states why it departs from the profile.
- Options: (a, preferred) a note giving the reason, e.g. a forward order for the summer peak placed before the slow figures were known, which keeps the cancellation story (broad, logistics, context agree); (b) lower the quantity and move the order to a date on which stock has fallen to the reorder point, which needs higher sales in `06-ProductActivity.xml` and changes the exception story.
- Needs decision: yes
- From: logistics (High), broad (Low), context (Low)

### furniture/10#F4 · Low · Repeat-order discount without a source in the flow
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Repeat order`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`
- XPath: `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.`
- Why: The order applies a 3 % repeat-order discount, but the quotation `02-Quotation.xml` quotes 610 per set without any allowance or repeat terms (`02-Quotation.xml:/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount` = `12200.00`), and the reason code 95 "Discount" names no agreement. The note "Price as quoted" is true of the unit price only (context refuted a contradiction on that ground, see below). Who granted the discount is stated nowhere in the flow.
- Condition: The discount can be traced to an agreement in the flow (the quotation, the contract, or a statement in this order), or the line amount equals the quoted amount.
- Options: (a, preferred) a note naming the basis of the discount (e.g. agreed separately, or the terms of the own-line contract), the smallest change; (b) the repeat-order discount in the quotation, so the order applies agreed terms; (c) drop the discount.
- Needs decision: yes
- From: broad (Low, no), money (Low, yes)

### furniture/10#F5 · Low · Quotation line reference without the quotation
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- XPath: `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574`
- Why: `QuotationLineReference` is "A reference to a quotation line associated with this order line" and holds only a line number. This order has no `QuotationDocumentReference` (unlike `08-Order.xml`), and its only document reference is to the earlier order, so line 1 of quotation `BF-DOC-26-0568` has to be inferred through `08-Order.xml`. The reference is incomplete rather than broken, and the order does not depend on it.
- Condition: The quotation whose line is referenced is identified in this order (by `QuotationDocumentReference` or the line reference's own document reference), or the line reference is absent.
- Options: (a, preferred) add `QuotationDocumentReference` `BF-DOC-26-0568`, since the price is the quoted one and the quotation is valid to 2026-05-05; (b) remove the line reference.
- Needs decision: no
- From: broad (Medium), logistics (Low), context (Low)

### furniture/10#F6 · Low · Delivery place in text only and no requested delivery date
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: The store's goods-in is identified in the request for quotation (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`, name `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Brightmarket Stores, goods-in`), but the order, against which the delivery is made, names it only in free text, and the delivery party carries no address. The order also has no requested delivery date or period; for this order it matters, because the cancellation `11-OrderCancellation.xml` turns on whether the delivery was still ahead ("cancelled before production"). Low: the agreed lead time of 5 days (`04-TradeItemLocationProfile.xml`) gives an implied date.
- Condition: The order's delivery identifies the goods-in by GLN 9522610900019 (and its name), as in `01-RequestForQuotation.xml`, and states a requested delivery date or period.
- Options: (a, preferred) `Delivery/DeliveryLocation` with ID and name, and a `RequestedDeliveryPeriod` after the cancellation date 2026-04-22; (b) add the GLN to the existing `DeliveryTerms/DeliveryLocation` and refer to the lead time in a note.
- Needs decision: no
- From: parties (place), logistics (place and date)

### furniture/10#F7 · Low · Own-line item carries the maker's brand
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Note` = `The store's own line: bench and two chairs per set.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The note and the description say the set is the store's own line, and the quotation adds the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` ("A brand name of this item") names the maker. Text and brand disagree unless the story means a co-branded or exclusive maker-branded line.
- Condition: The item's brand and its description of the line agree.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) reword as an exclusive Brackenmere line made for the store.
- Needs decision: yes
- From: broad, context

### furniture/10#F8 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name ("Buying office"), job title ("Customer service officer") and department ("Sales", the department serving the store's own customers) do not agree with each other, and a buyer's contact buys. The same contact is used in every example where Brightmarket is described in full.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the buyer role.
- Options: (a, preferred) a buyer contact, e.g. job title "Buyer", department "Purchasing"; (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/10#F9 · Low · Store's master data copied into the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital come from the store's master data; nothing in a purchase order for own-line garden furniture uses them (section 4.8, IND5). Carried on Brightmarket in examples 01 to 14.
- Condition: Present only in documents of the flow where they have a business reason.
- Options: (a, preferred) remove them from this document; (b) give the flow a reason and keep them only there.
- Needs decision: no
- From: parties (web site, social media), context (also logo and share capital)

### furniture/10#F10 · Low · "Original" price identical to the line price
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610`
- Why: `OriginalItemLocationQuantity` is "An original set of location-specific properties (e.g., price and quantity) associated with this item". Its price equals the line price; the repeat-order discount is an allowance on the line, not a different price, so the aggregate adds nothing the note `Price as quoted.` and the line price do not already say. Money had refuted it as a filler because it records the quoted price the note refers to; the merge keeps context's finding because the line price already is the quoted price.
- Condition: `OriginalItemLocationQuantity` is absent, or its price differs from the line price for a reason the story gives.
- Options: (a, preferred) remove it.
- Needs decision: no
- From: context (money refuted it)

### furniture/10#F11 · Low · Sub-line prices and the original price without base quantity
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cac:Price/cbc:PriceAmount` = `380`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[2]/cac:Price/cbc:PriceAmount` = `115`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:Price/cbc:PriceAmount` = `610`
- Why: `BaseQuantity` is "The quantity at which this price applies". The main line states it (1 SET), the sub-lines and the original price do not, so "per piece" or "per set" is implied by absence (IND6). Merge recount (lxml over `world/examples/*/*.xml`): 12 of 117 `Price` elements with a `PriceAmount` lack it, 3 of them in this order.
- Condition: Every `Price` in the order states the quantity it applies to, or the convention is recorded as a decision.
- Options: (a, preferred) add `BaseQuantity` 1 EA to both sub-line prices (and 1 SET to the original price, unless it is removed under F10); (b) record the convention.
- Needs decision: no
- From: money (sub-lines); the original price added in the merge

### furniture/10#F12 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/*/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Allowance: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:BaseAmount` = `12200.00` × 0.03 = 366.00; 12200.00 − 366.00 = 11834.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11834.00` (merge recalculation).
- Sub-lines: 20 × 380 = 7600.00, 40 × 115 = 4600.00, sum 12200.00 = the allowance's base amount; 20 benches + 40 chairs = 20 sets.
- `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574` ("A reference to another Order") resolves to `08-Order.xml`, an order of the same buyer, seller and item; this order is cancelled by `11-OrderCancellation.xml`, and no charge for it appears later in the flow.
- The order date 2026-04-16 lies within the quotation's validity (to 2026-05-05) and the profile's effective period.
- Quantities: minimum 10 ≤ 20 ≤ maximum 20; back order 5 to 10; 20 is a multiple of the profile's multiple order quantity 2.
- Parties: described identically across the flow; GLNs and GTIN pass their check digits.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:SubLineItem[1]/cbc:LineExtensionAmount` = `7600.00`: suspected that the sub-lines should carry the 3 % allowance (they sum to 12200.00, not 11834.00) — refuted because the allowance is applied on the main line to the base 12200.00, which the sub-lines make up (from money).
- `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.` next to a 3 % discount: suspected contradiction — refuted because the price itself is the quoted 610 and the discount is a separate allowance (from context); the missing source of the discount is F4.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F12 by the merge.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact — refuted because it fits the seller role and name, title and department agree (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number in `Name`/`ID` — refuted because the aggregate is the profile; its presence is F9 (from parties).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name`: delivery party equals the buyer — refuted because `DeliveryParty` has no "if different" condition and the order names the receiving party nowhere else (from parties).
- `/Order/cac:OrderLine/cac:LineItem/cac:WarrantyParty/cac:PartyName/cbc:Name`: warranty party equals the seller — refuted because Brackenmere makes the furniture and gives the two-year warranty itself (from parties).

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F12: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- logistics/F1 → F3: High → Low with "Needs decision: yes", combined with broad/F4 and context/F2, because the profile is a policy, not a statement the order contradicts, and the merge could not settle it (both arguments in "Why"); stock and order-interval arithmetic redone.
- broad/F5 (no) and money/F2 (yes) → F4: combined, "Needs decision: yes" because where the discount was agreed is story.
- broad/F2 (Medium) → F5: lowered to Low with logistics/F3 and context/F3: the reference is incomplete, not broken, and the order's purpose does not depend on it.
- parties/F2 and logistics/F2 → F6: combined (place and date).
- broad/F3, parties/F1, context/F1 → F2: removal preferred (broad preferred en-XB), as in earlier flows.
- parties/F4 and context/F6 → F9: grouped.
- context/F4 → F10: kept against money's refutation, with money's argument.
- money/F3 → F11: the original price (also without base quantity) added; count verified.

## Outside this review
- Whether the store could have known the slow sales on 2026-04-16 and when the first delivery arrived are timeline questions across 06, 09, 10 and 11; F3 records what this order contradicts.
