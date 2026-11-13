# LLM review: 06-RetailEvent.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/06-RetailEvent.xml`, Git blob `d0b57c7c84cd16cde8dca7daf766830c3f61056c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/06#F1 · High · Event comment made after the document was issued
- XPath: `/RetailEvent/cbc:IssueTime` = `08:17:00`
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueDate` = `2026-04-22`
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueTime` = `11:00:00`
- Why: `EventComment/IssueDate`/`IssueTime` are "The date/time on which this comment was made". The comment is dated 2026-04-22 11:00, almost three hours after the retail event document itself was issued (2026-04-22 08:17). A document cannot contain a comment made after its issue.
- Condition: the comment's date and time are not later than the document's issue date and time.
- Options: (a, preferred) a comment time before 08:17 (e.g. the previous day, when the promotion was agreed); (b) a later issue time, still before the forecast of 11:55 that includes the promotion.
- Needs decision: no

### retail/06#F2 · Medium · Language codes in LocaleCode
- XPath: `/RetailEvent/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/06#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/RetailEvent/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/06#F4 · Low · A store opening event without any story behind it
- XPath: `/RetailEvent/cac:MiscellaneousEvent/cbc:MiscellaneousEventTypeCode` = `STOREOPEN`
- XPath: `/RetailEvent/cac:MiscellaneousEvent/cac:EventLineItem/cac:SupplyItem/cbc:Name` = `Park bench Serra 180`
- Why: the retail event is the spring garden promotion (name, description, note, promotional event). The miscellaneous event declares in addition a store opening, with no store, no location, no period and no mention anywhere in the example or the flow; the bench is the only item. It reads as an element added for coverage (no-filler rule), and it states a business fact (a store opens) that the world does not support.
- Condition: a miscellaneous event is present only if the story has one, with what is needed to understand it (which store, when).
- Options: (a, preferred) drop it; (b) give Brightmarket a new store opening in the story and describe it (location, date).
- Needs decision: yes

### retail/06#F5 · Low · A confirmed event whose proposal acceptance deadline is still ahead
- XPath: `/RetailEvent/cbc:RetailEventStatusCode` = `CONFIRMED`
- XPath: `/RetailEvent/cac:PromotionalEvent/cbc:SubmissionDate` = `2026-04-22`
- XPath: `/RetailEvent/cac:PromotionalEvent/cbc:LatestProposalAcceptanceDate` = `2026-04-26`
- Why: `LatestProposalAcceptanceDate` is "The deadline for acceptance of this promotional event", and `SubmissionDate` "The date on which a proposal for this promotional event was submitted". The proposal is submitted today with an acceptance deadline four days later, but the event is already confirmed and, per the note, agreed with the distributor's sales team. Either the event is a proposal awaiting acceptance, or it is confirmed and the deadline has no purpose.
- Condition: status, submission date and acceptance deadline describe the same stage of the event.
- Options: (a, preferred) keep `CONFIRMED` and drop the acceptance deadline (or date the submission before the agreement); (b) make it a proposal and let the confirmation follow.
- Needs decision: no

### retail/06#F6 · Low · Promotional event type repeats the consumer tactic
- XPath: `/RetailEvent/cac:PromotionalEvent/cbc:PromotionalEventTypeCode` = `TPR`
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:ConsumerIncentiveTacticTypeCode` = `TPR`
- Why: UBL's examples for `PromotionalEventTypeCode` are "Holiday, Seasonal Event, Store Closing, Trade Item Introduction": the kind of event. A temporary price reduction is the consumer incentive, which the tactic already codes. The spring garden promotion is a seasonal event.
- Condition: the event type code says what kind of event it is, the tactic code how consumers are attracted.
- Options: (a, preferred) a seasonal event type code (added to the world's list if missing); (b) keep TPR if the world's list defines event types this way, and record why.
- Needs decision: no

### retail/06#F7 · Low · End-cap display and shelf space for benches placed at the store entrance
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:DisplayTacticTypeCode` = `ENDCAP`
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cbc:Comment` = `Benches at the entrance, with a price board.`
- XPath: `/RetailEvent/cac:EventComment/cbc:Comment` = `Shelf space for 12 benches at the entrance.`
- Why: an end-cap is the display at the end of an aisle; the texts place twelve 1.8 m benches at the entrance, which is a floor display, and benches stand on the floor, not on shelf space. Code and texts describe different displays.
- Condition: display tactic code and texts describe the same display.
- Options: (a, preferred) a floor or entrance display code (UBL's examples include FLOOR_STACK_DISPLAY), and "floor space" in the comment; (b) keep the end-cap and change the texts.
- Needs decision: no

### retail/06#F8 · Low · Participating location named after the company, without identification
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:ParticipatingLocationsLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- Why: `ParticipatingLocationsLocation` is "The location of the stores involved in the event". The name is the company plus the city, with no address or GLN, although Brightmarket's store is identified elsewhere in the flow (its address and GLN `9522610900002` appear in every example). The supplier cannot tell which store takes part if Brightmarket has more than one.
- Condition: the location names the store (and is identified as elsewhere in the flow).
- Options: (a, preferred) the store's name and its address or GLN; (b) keep the name if Brightmarket has only one store, and say so.
- Needs decision: no

### retail/06#F9 · Low · Planned sales value at the undiscounted price
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:RetailPlannedImpact/cbc:Amount` = `17976.00`
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cbc:Amount` = `74.90`
- Why: 17976.00 = 24 × 749.00, i.e. 24 benches at the regular consumer price (749.00, the base of the 10 % discount in `21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:BaseAmount`). During a temporary price reduction of 74.90 per bench the planned sales are made at 674.10, which gives 16178.40. The planned impact as a sales forecast should use the price at which the benches are sold.
- Condition: the planned impact equals the planned quantity × the promotional price (or the text says what else it measures).
- Options: (a, preferred) 16178.40 for 24 benches; (b) state that the amount is valued at the regular price, if that is the convention.
- Needs decision: no

### retail/06#F10 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RetailEvent/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. As the sender announcing the promotion to the supplier, the buying office fits the role. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail (compared by script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of the contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office, or a contact fitting this role; (b) different contacts per role, if the world gives Brightmarket several.
- Needs decision: no

## Checked and consistent
- Promotion period 2026-05-11 to 2026-05-24 (two weeks, as the description says) lies within the forecast period of 05-Forecast; the tactic's and the planned impact's periods equal it.
- 10 % of 749.00 = 74.90, the amount of the promotional line item; the same discount is applied in 21-PurchaseReceipt on 2026-05-15, within the promotion.
- First shipment availability 2026-04-29 matches the despatch in 12-DespatchAdvice (issued 2026-04-29).
- The event is referenced by 08-Order (`08-Order.xml:/Order/cac:AdditionalDocumentReference/cbc:ID` = `BS-RE-26-0222`).
- Seller's item ID `LD-10442` is the bench of 02-Catalogue.

## Considered and refuted
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:TradeItemPackingLabelingTypeCode` = `STICKER`: suspected a code that does not describe trade item packing — refuted: a price sticker on the item is a form of price-pack labelling.
- `/RetailEvent/cac:OriginalDocumentReference/cbc:ID` = `BM-PROMO-PLAN-26`: unresolved in the flow — refuted as a finding: Brightmarket's internal promotion plan, a document outside the flow, which is legitimate.
