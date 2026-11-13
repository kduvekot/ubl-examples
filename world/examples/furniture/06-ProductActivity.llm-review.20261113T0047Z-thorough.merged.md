# LLM review: 06-ProductActivity.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/06-ProductActivity.xml`, Git blob `b8bd3b68d78e4195bf7df8c905e21d85b0c22321` (committed)
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

### furniture/06#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/ProductActivity/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProductActivity/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode` (context, parties, earlier flows); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/06#F2 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/ProductActivity/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ProductActivity/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ProductActivity/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores reports its sales to the supplier as the buyer. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact for supplier collaboration. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying or planning contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/06#F3 · Low · Party master data copied into the sales report
- XPath: `/ProductActivity/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ProductActivity/cac:SenderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/ProductActivity/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/ProductActivity/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/ProductActivity/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/ProductActivity/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo reference, online-shop website, photo-sharing profile, share capital (with the fully-paid-shares indicator) and both parties' state-sales-tax registrations are master data. A sales report carries no tax treatment, payment or label and does nothing with any of them (section 4.8); its retail prices do not depend on the parties' registrations. The parties part suggested one way the online shop could gain a reason (reporting online-shop sales separately), but this report gives one in-store figure for the garden department. The store's four marketing and capital elements are carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: these elements are present only in documents that have a reason to carry them.
- Options: (a, preferred) remove them here, keeping identification, name, address, contact and electronic address; (b) give the report a reason for the online shop (a separate online-sales line) and keep only that.
- Needs decision: no
- From: context, parties

### furniture/06#F4 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/ProductActivity/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/ProductActivity/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/06#F5 · Low · Buyer and seller of the activity line are the trading partners, not the parties of the retail sales reported
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: In an activity data line, `BuyerCustomerParty` is "The buyer of the item" and `SellerSupplierParty` "The seller of the item". The activity reported is the store's retail sale (`SupplyChainActivityTypeCode` SALES, at a tax-inclusive retail price, to customers). In that sale the seller is Brightmarket Stores and the buyers are consumers; Brackenmere is not a party to it. The parties part refuted this: buyer and seller state the trade relationship the planning data belong to, which is UBL's design for these documents. The merge cannot settle it: "the buyer of the item" fits Brightmarket as the buyer from Brackenmere, but in a line that reports the store's sales, the item's seller in that activity is the store.
- Condition: the line's buyer and seller are the parties of the activity reported, or both are absent, or the reading that they name the trading relationship is recorded.
- Options: (a, preferred) remove both: sender and receiver already identify the trading partners, and consumers are not identified; (b) seller = Brightmarket Stores and no buyer; (c) keep them under the trading-relationship reading.
- Needs decision: yes
- From: context (parties refuted it, see Why)

### furniture/06#F6 · Low · One four-week figure where weekly figures were requested
- XPath: `/ProductActivity/cac:ActivityPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/ProductActivity/cac:ActivityPeriod/cbc:EndDate` = `2026-04-20`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityPeriod/cbc:EndDate` = `2026-04-20`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cbc:Quantity` = `3`
- XPath: `03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:TimeFrequencyCode` = `WEEKLY`
- Why: The report answers the maker's request (`/ProductActivity/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0569`, i.e. `03-ItemInformationRequest.xml`), whose `TimeFrequencyCode` is "the frequency with which item information will be sent to the requester": weekly, with the note "Weekly figures, please". This report is the only one in the flow and gives one sales figure for the span from Monday 2026-03-23 to Monday 2026-04-20. That span is 29 days counted inclusively (recalculated by the merge), i.e. four Monday-to-Sunday weeks plus the Monday of the fifth week, which is also the issue day, so the last day is only partly covered at the issue time 16:35. The store's own text ("Rain three weeks out of four.") counts four weeks.
- Condition: the report gives the sales per week requested (one activity line or period per week), or request and report agree on a four-week figure; the period ends on the last day it fully covers.
- Options: (a) four weekly lines with their own `ActivityPeriod`, whose quantities add up to 3 sets (preference of broad and context: it also shows the rain pattern and lets 07 compare against the criterion); (b) end the period on Sunday 2026-04-19, keep one four-week figure and change the request to a four-weekly frequency, because the exception criterion and notification also work on four weeks (logistics' preference). The merge prefers (a), which leaves the request as asked.
- Needs decision: no
- From: broad, context, logistics

### furniture/06#F7 · Low · ActivityFinalLocation "Customers' gardens"
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityFinalLocation/cbc:Name` = `Customers' gardens in Lumeport`
- Why: `ActivityFinalLocation` is "The location to which the goods are moved". For retail sales the goods leave the supply chain; the store does not know or report where customers take them, "customers' gardens" is not a location anyone can identify or use, and nothing in the flow uses it (IND5). The logistics and parties parts refuted this: for consumer sales the location to which the goods are moved is the consumers' premises, which a store can only describe in general terms, and the text says so truthfully. The merge cannot settle whether a truthful but unusable description is a business reason for the element.
- Condition: `ActivityFinalLocation` is absent for the sales line, or names a location the goods are moved to that a reader can use (e.g. a store-to-store transfer), or the general description is accepted as the story's choice.
- Options: (a, preferred) remove it: the origin location (the garden department) is enough for sales; (b) keep it as a deliberate description.
- Needs decision: yes
- From: broad, context (logistics, parties refuted it, see Why)

### furniture/06#F8 · Low · ActivityProperty carries the weather, an explanation rather than a property of the activity
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:ActivityProperty/cbc:Name` = `Weather`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:ActivityProperty/cbc:Value` = `Rain three weeks out of four.`
- Why: `SalesItem/ActivityProperty` is "A class to describe the activity (for example "sales", "movement", ...) related to the item". The weather is not a description of the sales activity (its kind, channel or condition) but an explanation of why sales were low, i.e. commentary of the kind the document note carries next to it (`/ProductActivity/cbc:Note` = `Sales were slow after the promotion ended.`). The merge tried the reading that the weather is a circumstance of the sales activity and therefore describes it: the definition's examples are kinds of activity, which supports the context part, but the definition is open enough that the other reading cannot be excluded.
- Condition: `ActivityProperty` describes the activity of the item, or is absent; the weather, if kept, is in a note; or the reading that circumstances of the activity are properties is recorded.
- Options: (a, preferred) move the weather into the line or document note, next to the note on the promotion; (b) replace it with a real activity property if the story has one (e.g. sales channel "in store").
- Needs decision: yes
- From: context

### furniture/06#F9 · Low · Maker's brand on an item for the store's own line
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The description says the set is made for the store's own line, sold under the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); in a report of the store's own retail sales, the maker's brand points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line.
- Needs decision: yes
- From: context

## Checked and consistent
- Retail prices (recalculated by the merge): `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxExclusivePrice/cbc:PriceAmount` = `899` × 1.065 = 957.435, rounded to `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxInclusivePrice/cbc:PriceAmount` = `957.44`, i.e. 6.5 % state sales tax, the standard rate for consumer sales in Lumeport elsewhere in the world (packaging/08-PurchaseReceipt, packaging/09-PurchaseReceipt; money part). The retail price 899 lies above the purchase price 610 of `08-Order.xml`, a plausible margin; currency `XBL` matches the purchase documents.
- Stock (from logistics, recalculated): 20 sets delivered by 2026-03-22 (`09-Invoice.xml`), 3 sold in the period, so at most 17 on hand on 2026-04-20; after the return of 6 sets in `12-InstructionForReturns.xml` 11 remain, close to the target inventory of 10 in `04-TradeItemLocationProfile.xml`.
- Location: the origin GLN `9522610900026` (check digit passes, `check_ids.py`) is the store's garden department, the same GLN and meaning as in `retail/22-Order.xml`, rightly different from the goods-in GLN `9522610900019`; "the location where the movement of goods is observed" fits.
- The period and the quantity (3 sets) are those `07-ExceptionNotification.xml` compares; the report precedes the notification (2026-04-20 16:35 before 2026-04-21 17:49); the period starts on the effective date of criterion line 1 of `05-ExceptionCriteria.xml` and lies inside the requested period of 03.
- Codes SALES and SET resolve; item identification matches the flow; party data are identical to the other examples of the flow (parties part).

## Considered and refuted
- `/ProductActivity/cbc:Note` = `Sales were slow after the promotion ended.`: no promotion appears in the flow — refuted because a store's own in-store promotion need not be exchanged with the maker; the note gives context and no other value depends on it (from context, logistics); its two explanations (promotion, rain) do not contradict each other (from broad).
- `/ProductActivity/cbc:DocumentCurrencyCode` = `XBL`: suspected filler — refuted because the report carries prices (from context).
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxInclusivePrice/cbc:PriceAmount`: the tax-inclusive price implies a rate the document never states (IND6) — refuted because `SalesItem` has no element for the tax category or rate; the pair of prices is how UBL expresses the retail price here (from money).
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxExclusivePrice`: data the maker does not need — refuted because sales reporting to a supplier under a sell-through threshold commonly carries the selling price, so the supplier can judge whether the price explains the low sales (from money).
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:Name`: name contains the company name — refuted because it names the store's garden department, identified by its own GLN (from broad, parties).
- `/ProductActivity/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge) (from parties).
- `/ProductActivity/cac:ReceiverParty/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/ProductActivity/cac:ReceiverParty/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact as receiver of a planning document — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/ProductActivity/cac:ReceiverParty/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/ProductActivity/cac:SenderParty/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F3 (from parties).
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat receiver and sender — refuted by parties (trade relationship); kept by the merge as F5 with both arguments.
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityFinalLocation/cbc:Name`: not an identifiable location — refuted by logistics and parties; kept by the merge as F7 with both arguments.
- `/ProductActivity/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F4 by the merge.

## Changed in the merge
- broad/F1, context/F2, parties/F1 → F1: combined; preferred option set to removal, broad's `en-XB` kept as option (b).
- broad/F4, parties/F2 → F2: combined.
- context/F7, parties/F3, parties/F4 → F3: grouped as one problem (master data in a document that does not use it).
- parties' refuted RegistrationDate → F4: made a finding (Low, needs decision) for alignment with the earlier flows.
- context/F4 → F5: needs decision changed from no to yes, because the parties part refuted it with a reading the merge cannot exclude.
- broad/F2, context/F3, logistics/F1 → F6: combined; the period-end point of logistics added; both preferences listed, the merge prefers (a).
- broad/F3, context/F5 → F7: needs decision changed from no to yes, because logistics and parties refuted it and the merge cannot settle it.
- context/F1 → F8: severity lowered from Medium to Low and needs decision set to yes, because the definition ("A class to describe the activity") is open enough that the weather as a circumstance of the sales cannot be excluded.
- context/F6 → F9: kept.
