# LLM review: 06-RetailEvent.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/06-RetailEvent.xml`, Git blob `d0b57c7c84cd16cde8dca7daf766830c3f61056c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/06#F1 · High · Event comment made after the document was issued
- XPath: `/RetailEvent/cbc:IssueDate` = `2026-04-22`
- XPath: `/RetailEvent/cbc:IssueTime` = `08:17:00`
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueDate` = `2026-04-22`
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueTime` = `11:00:00`
- Why: `EventComment/IssueDate`/`IssueTime` are "The date/time on which this comment was made". The comment ("Shelf space for 12 benches at the entrance.") is dated 11:00, 2 h 43 min after the retail event document that carries it was issued (08:17 the same day). A document cannot contain a comment made after its issue.
- Condition: the comment's date and time are not later than the document's issue date and time.
- Options: (a, preferred) a comment time before 08:17 (e.g. from the meeting with the distributor's sales team the note mentions); (b) a later issue time, still before the forecast 05 (11:55) that builds on the event; (c) no comment time.
- Needs decision: no
- From: broad, logistics, context

### retail/06#F2 · Medium · "Original document" reference is not a forecast and resolves nowhere
- XPath: `/RetailEvent/cac:OriginalDocumentReference/cbc:ID` = `BM-PROMO-PLAN-26`
- XPath: `05-Forecast.xml:/Forecast/cbc:ID` = `BS-FC-26-0221`
- Why: in a RetailEvent, `OriginalDocumentReference` is "A reference to a Forecast document associated with this event" (verified with annotate.py). `BM-PROMO-PLAN-26` is by its name a promotion plan, has no document type and occurs in no other example (verified: grep finds only this file). The flow's forecast, 05, is issued after this event (11:55 vs 08:17) and refers to the promotion, so it cannot be the original document either. Broad refuted the reference as an internal document outside the flow, which settles its existence but not the element's meaning: a document of another kind in an element defined for a forecast.
- Condition: `OriginalDocumentReference`, if present, identifies a forecast that exists before this event.
- Options: (a, preferred) drop it: the event comes first and 05 follows it (05#F1 makes 05 point here); (b) if the plan matters, RetailEvent has no general document reference, so it would be named in the note.
- Needs decision: no
- From: logistics, context (broad refuted)

### retail/06#F3 · Medium · A language code in LocaleCode
- XPath: `/RetailEvent/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats the language code. 362 occurrences in 213 files (verified).
- Condition: every `LocaleCode` holds a locale from a locale list, or is absent.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad, parties, context

### retail/06#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/RetailEvent/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is a vehicle access detail. 79 occurrences in 76 files (verified).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it; (b) record it in Bayvarra's address format.
- Needs decision: no
- From: broad, parties

### retail/06#F5 · Medium · The promotional line item carries the reduction, not the promotional price
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cbc:Amount` = `74.90`
- XPath: `21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `674.1`
- XPath: `21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:Amount` = `74.90`
- XPath: `21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:BaseAmount` = `749.00`
- Why: a `PromotionalEventLineItem` is "A line item for a promotional event involving a specific product at a specific location; it describes the expected impacts associated with the event and specifies the promotional price of the item", and its `Amount` "The amount associated with this promotional event line item", i.e. the promotional price. Recomputed: the regular consumer price is 749.00, 10 % off (`/RetailEvent/cbc:Description` = `Ten per cent off garden furniture for two weeks.`) is 74.90, so the promotional price is 749.00 − 74.90 = 674.10, which is the till price in 21. The line item gives 74.90, the reduction. Read as a price, 74.90 would also be far below the distributor's trade price of 520 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`). Broad and context checked 74.90 as "10 % of 749.00", which is arithmetically right but not what the element holds.
- Condition: the promotional event line item's amount is the bench's promotional price, 674.10, consistent with the till price in 21.
- Options: (a, preferred) 674.10; (b) if the reduction is what the event should communicate, state it in the tactic or description and still give the price here.
- Needs decision: no
- From: money

### retail/06#F6 · Medium · A store opening event that nothing in the document or the flow supports
- XPath: `/RetailEvent/cac:MiscellaneousEvent/cbc:MiscellaneousEventTypeCode` = `STOREOPEN`
- XPath: `/RetailEvent/cac:MiscellaneousEvent/cac:EventLineItem/cac:SupplyItem/cbc:Name` = `Park bench Serra 180`
- XPath: `/RetailEvent/cbc:Description` = `Ten per cent off garden furniture for two weeks.`
- Why: `MiscellaneousEvent` is "A miscellaneous event associated with this event", here a store opening ("Store opening" in the world's list). Nothing in the document (name, description, note, comments, locations) or the flow mentions a store opening, which store opens or when; the participating location is the existing Lumeport store, and the event is a temporary price reduction. The element states a business fact the world does not support (IND5/IND6); it reads as added for coverage. Medium (context) rather than Low (broad): it is not just unused data but a statement to the supplier about an event that does not exist.
- Condition: either the story has a store opening (named store, date) that the event describes, or there is no `MiscellaneousEvent`.
- Options: (a, preferred) drop it; (b) give Brightmarket a store opening in the story and describe it (location, date, why the bench is part of it).
- Needs decision: yes
- From: broad (Low), context (Medium)

### retail/06#F7 · Low · A confirmed event whose proposal acceptance deadline is still ahead
- XPath: `/RetailEvent/cbc:RetailEventStatusCode` = `CONFIRMED`
- XPath: `/RetailEvent/cac:PromotionalEvent/cbc:SubmissionDate` = `2026-04-22`
- XPath: `/RetailEvent/cac:PromotionalEvent/cbc:LatestProposalAcceptanceDate` = `2026-04-26`
- Why: `SubmissionDate` is "The date on which a proposal for this promotional event was submitted" and `LatestProposalAcceptanceDate` "The deadline for acceptance of this promotional event". The proposal is submitted on the issue date with an acceptance deadline four days later, yet the event is already confirmed and, per the note, agreed with the distributor's sales team. Context checked it as possible (a proposal accepted before its deadline is confirmed); then the deadline is past its purpose in a document that reports the confirmed state, so it stays a consistency remark.
- Condition: status, submission date and acceptance deadline describe the same stage of the event.
- Options: (a, preferred) keep `CONFIRMED` and drop the deadline (or date the submission before the agreement); (b) make it a proposal and let the confirmation follow.
- Needs decision: no
- From: broad (context checked it as consistent)

### retail/06#F8 · Low · Signature without anything that signs
- XPath: `/RetailEvent/cac:Signature/cbc:ID` = `BM-SIG-26-0422E`
- Why: only an ID and a signatory, no method or attachment; nothing in the story needs a signed event notice (IND5/IND6). 137 of 147 signatures in the world have this shape (lxml).
- Condition: a signature with a reason and its data, or none.
- Options: (a, preferred) drop it; (b) method and attachment with a reason.
- Needs decision: yes (world-wide convention, as in the air and utilities merges)
- From: context (signature part of its F6)

### retail/06#F9 · Low · Party master data the event notice does nothing with
- XPath: `/RetailEvent/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RetailEvent/cac:SenderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/RetailEvent/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/RetailEvent/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/RetailEvent/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: a promotion notice to the supplier uses no customs trader number, share capital or tax registration. The logo, web shop and social-media profile are the weakest part: they could serve a consumer promotion (context), but the event (flyer, price board, sticker) refers to none of them. Master data (section 4.8); `CorporateStockAmount` holds share capital where UBL defines "The number of shares in the capital stock of a corporation" (TC write-up note).
- Condition: the parties carry what the event notice uses.
- Options: (a, preferred) leave them out; (b) keep the web shop or social-media profile only if the promotion is advertised there (then say so in the feature tactic).
- Needs decision: no
- From: parties (F3, F4, F6), context (F6, master-data part)

### retail/06#F10 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: announcing a promotion to the supplier fits the buying office; job title and department are a seller's customer service and contradict the name. Same contact in 41 files (verified).
- Condition: name, job title and department agree with each other and with the role.
- Options: (a, preferred) buyer's (or category manager's) job title in purchasing.
- Needs decision: no
- From: broad, parties

### retail/06#F11 · Low · Promotional event type repeats the consumer tactic
- XPath: `/RetailEvent/cac:PromotionalEvent/cbc:PromotionalEventTypeCode` = `TPR`
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:ConsumerIncentiveTacticTypeCode` = `TPR`
- Why: `PromotionalEventTypeCode` is "A code signifying the type of this promotional event. Examples can be: Holiday, Seasonal Event, Store Closing, Trade Item Introduction": the kind of event. A temporary price reduction is the consumer incentive, which the tactic code already says. The spring garden promotion is a seasonal event, and the world's list has `SEASONAL` "Seasonal promotion" (verified in `world/codelists/lists.json`).
- Condition: the event type says what kind of event it is, the tactic how consumers are attracted.
- Options: (a, preferred) `SEASONAL`; (b) keep `TPR` and record why the world's list uses it as an event type.
- Needs decision: no
- From: broad

### retail/06#F12 · Low · Participating location named after the company, without identification
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:ParticipatingLocationsLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `22-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- Why: `ParticipatingLocationsLocation` is "The location of the stores involved in the event described in this line item". The name is the company plus the town, with no address or GLN, although the flow identifies Brightmarket's places by GLN (goods-in `9522610900019` in 08, the garden department of the Lumeport store `9522610900026` in 22). A supplier planning deliveries cannot tell which store, or whether all Lumeport stores, take part. Parties refuted it (the value names the store in Lumeport, the usual way to name a store); that holds if Brightmarket has one store in Lumeport, which nothing states.
- Condition: the location identifies the store(s) taking part (store name and, where one exists, GLN or address).
- Options: (a, preferred) the store's name and the garden department's GLN `9522610900026`; (b) one event line item per store if several take part.
- Needs decision: no
- From: broad, logistics, context (parties refuted)

### retail/06#F13 · Low · Planned sales value at the regular price, not the promotional price
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:RetailPlannedImpact/cbc:Amount` = `17976.00`
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cbc:Amount` = `74.90`
- XPath: `05-Forecast.xml:/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `40`
- Why: `RetailPlannedImpact/Amount` is the "Estimated monetary value of the planned event as an impact", here of sales (purpose SALES) over the two promotion weeks. Recomputed: 17976.00 = 24 × 749.00, 24 benches at the regular price; at the promotional price the event is about, 24 × 674.10 = 16178.40. It cannot be reconciled with the line item's amount either (17976.00 / 74.90 = 240 benches, against shelf space for 12 and a forecast of 40 for six weeks). The quantity 24 is consistent with the order (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `24`); only the valuation is off. Context noted the question for the money lens and refuted `TOTAL` as forecast type (the amount is a total figure).
- Condition: the planned sales value equals the planned quantity × the promotional price (24 × 674.10 = 16178.40), or the event states that it values at regular prices.
- Options: (a, preferred) 16178.40; (b) keep 17976.00 with a note that it is valued at regular prices.
- Needs decision: no
- From: broad, money

### retail/06#F14 · Low · End-cap display and shelf space for benches placed at the store entrance
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:DisplayTacticTypeCode` = `ENDCAP`
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cbc:Comment` = `Benches at the entrance, with a price board.`
- XPath: `/RetailEvent/cac:EventComment/cbc:Comment` = `Shelf space for 12 benches at the entrance.`
- Why: the world's list describes `ENDCAP` as "End-cap display", "At the end of an aisle." (verified in `world/codelists/lists.json`); the texts place twelve 1.8 m benches at the entrance, which is a floor display (the list also has `FLOORSTAND` "Floor stand"), and benches stand on the floor, not on shelf space. Code and text equivalents describe different displays. Context refuted it (an end-cap at the head of a shelf run near the entrance is plausible); the list's own description "at the end of an aisle" makes that reading weaker, so it stays a remark.
- Condition: display code and texts describe the same display.
- Options: (a, preferred) `FLOORSTAND` and "floor space" in the comment; (b) keep the end-cap and change the texts.
- Needs decision: no
- From: broad (context refuted)

## Checked and consistent
- Promotion period 2026-05-11 to 2026-05-24 is two weeks, as the description says; the tactic's and the planned impact's periods equal it; it lies within 05's forecast period and contains the consumer's purchase in 21 (`21-PurchaseReceipt.xml:/PurchaseReceipt/cbc:PurchaseDate` = `2026-05-15`).
- 10 % in the description matches 21's factor (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.1`); 749.00 × 0.1 = 74.90; 749.00 − 74.90 = 674.10.
- Event tactic quantity 12 EA equals the shelf space in the comment; 24 benches equals the order 08; stock 3 + 24 against a display of 12 is consistent (logistics).
- `FirstShipmentAvailabilityDate` 2026-04-29 is the despatch date of 12 (`12-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-04-29`).
- The event is referenced by 08 (`08-Order.xml:/Order/cac:AdditionalDocumentReference/cbc:ID` = `BS-RE-26-0222`); seller's item ID `LD-10442` is the bench of 02; SellerEventID and BuyerEventID are distinct identifiers of the two parties.
- Roles: the buyer Brightmarket sends the promotion to its supplier Lumeway, as in the order; both parties described as in every retail example; GLN check digits correct.

## Considered and refuted
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:TradeItemPackingLabelingTypeCode` = `STICKER`: does not describe trade item packing — refuted, a price sticker on the item is price-pack labelling, and the world's list names it "Price sticker" (from broad).
- `/RetailEvent/cac:OriginalDocumentReference/cbc:ID` = `BM-PROMO-PLAN-26`: unresolved — refuted by broad as an internal document outside the flow; the element's meaning is F2 (from broad).
- The order's 5 % promotion support (`08-Order.xml:/Order/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.05`) is not mentioned in the event — refuted, the event describes the consumer-facing promotion; the supplier's contribution belongs to the trade documents (from money).
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:DisplayTacticTypeCode`: end-cap at the entrance — refuted by context (plausible near the entrance); not followed, F14 (from context).
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:RetailPlannedImpact/cbc:ForecastTypeCode`: `TOTAL` rather than a promotional type — refuted, the amount is the total sales value (from context).
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:ParticipatingLocationsLocation/cbc:Name` = `Brightmarket Stores, Lumeport`: names the company — refuted by parties (the usual way to name a store); not followed, F12 (from parties).
- `/RetailEvent/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: misuse — refuted (from parties).
- `/RetailEvent/cac:PromotionalEvent/cbc:LatestProposalAcceptanceDate`: checked by context as consistent with a confirmed status; not followed, F7 (from context).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined.
- logistics/F2, context/F2 → F2: combined; broad's refutation answered in the Why.
- money/F1 → F5: kept Medium; broad's and context's "74.90 = 10 % of 749" checks answered in the Why.
- broad/F4 (Low/yes), context/F3 (Medium/yes) → F6: Medium.
- context/F6 split into F8 (signature; "Needs decision" no → yes, aligned with the air and utilities merges) and F9 (master data, with parties/F3, F4 (Low/yes → no, see 01#F6), F6).
- broad/F8, logistics/F3, context/F5 → F12: combined; parties' refutation answered.
- broad/F9, money/F2 → F13: combined.
- broad/F2, parties/F1, context/F4 → F3; broad/F3, parties/F2 → F4; broad/F10, parties/F5 → F10: combined.
