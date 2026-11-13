# LLM review: 06-ProductActivity.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/06#F1 · Medium · ActivityProperty carries the weather, not a property of the activity
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:ActivityProperty/cbc:Name` = `Weather`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:ActivityProperty/cbc:Value` = `Rain three weeks out of four.`
- Why: `SalesItem/ActivityProperty` is "A class to describe the activity (for example "sales", "movement", ...) related to the item". The weather is not a description of the sales activity but an explanation of why sales were low; it is commentary, which belongs in a note. The element is used for a meaning other than its definition.
- Condition: `ActivityProperty` describes the activity of the item (e.g. its kind, channel or condition), or is absent; the weather, if kept, is in a note.
- Options: (a) move the weather into the document or line note, next to the existing note on the promotion (preferred); (b) replace it with a real activity property if the story has one (e.g. sales channel "in store").
- Needs decision: no

### furniture/06#F2 · Medium · LocaleCode holds a bare language code
- XPath: `/ProductActivity/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProductActivity/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/06#F3 · Low · One four-week total where weekly figures were requested
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityPeriod/cbc:EndDate` = `2026-04-20`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cbc:Quantity` = `3`
- Why: This report answers the item information request (`DocumentReference` `BF-DOC-26-0569`), which asked for weekly figures (`03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:TimeFrequencyCode` = `WEEKLY`). It reports one quantity for four weeks. Either weekly reports preceded it (none exists in the flow) or the report should break the figure down per week; as it stands the response does not match the frequency requested.
- Condition: the report's lines match the requested frequency (one activity line, or one sales item, per week), or the request asks for a four-weekly figure.
- Options: (a) four weekly lines with their own `ActivityPeriod` (preferred: shows the "rain three weeks out of four" pattern in the figures); (b) change the request's frequency.
- Needs decision: no

### furniture/06#F4 · Low · Buyer and seller of the line are the trading partners, not the parties of the sales reported
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: In an activity data line, `BuyerCustomerParty` is "The buyer of the item" and `SellerSupplierParty` "The seller of the item". The activity reported is the store's retail sale (`SupplyChainActivityTypeCode` `SALES`, at a tax-inclusive retail price of 957.44 to customers' gardens). In that sale the seller is Brightmarket Stores and the buyers are consumers; Brackenmere is not a party to it. Copying the two trading partners into the line, which are already the sender and receiver of the report, gives the line parties that contradict the activity it describes.
- Condition: the line's buyer and seller are the parties of the activity reported, or both are absent.
- Options: (a) remove both (preferred: sender and receiver already identify the partners, and consumers are not identified); (b) seller = Brightmarket Stores and no buyer.
- Needs decision: no

### furniture/06#F5 · Low · ActivityFinalLocation names no location
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityFinalLocation/cbc:Name` = `Customers' gardens in Lumeport`
- Why: `ActivityFinalLocation` is "The location to which the goods are moved"; it is meant for movements between identifiable locations (transfers, shipments). For retail sales the goods leave the supply chain; "customers' gardens" is not a location anyone can identify or use, and nothing in the flow uses it. It reads as a filler for the element.
- Condition: `ActivityFinalLocation` is absent for the sales line, or names a real location the goods are moved to.
- Options: (a) remove it (preferred); (b) none other seen.
- Needs decision: no

### furniture/06#F6 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); in a report of the store's own retail sales the maker's brand contradicts that unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/06#F7 · Low · Sender's master data copied into the report
- XPath: `/ProductActivity/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ProductActivity/cac:SenderParty/cac:AdditionalWebSite`
- XPath: `/ProductActivity/cac:SenderParty/cac:SocialMediaProfile`
- XPath: `/ProductActivity/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in a sales report (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `ActivityOriginLocation` (garden department, GLN 9522610900026, check digit OK) is the location where the sales are observed, as the definition allows ("the location where the movement of goods is observed").
- `ActivityPeriod` of document and line agree (2026-03-23 to 2026-04-20), fall inside the requested period of `03-ItemInformationRequest.xml` and equal the observation period of `07-ExceptionNotification.xml`.
- `TaxExclusivePrice` and `TaxInclusivePrice` as retail prices fit a sales report.

## Considered and refuted
- `/ProductActivity/cbc:Note` = `Sales were slow after the promotion ended.`: no promotion appears in the flow — refuted because a store's own in-store promotion need not be exchanged with the maker; the note is plausible context.
- `/ProductActivity/cbc:DocumentCurrencyCode` = `XBL`: suspected filler — refuted because the report carries prices.
