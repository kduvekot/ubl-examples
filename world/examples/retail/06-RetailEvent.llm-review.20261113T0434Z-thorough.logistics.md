# LLM review: 06-RetailEvent.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/06-RetailEvent.xml`, Git blob `d0b57c7c84cd16cde8dca7daf766830c3f61056c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
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
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueTime` = `11:00:00`
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueDate` = `2026-04-22`
- XPath: `/RetailEvent/cbc:IssueTime` = `08:17:00`
- XPath: `/RetailEvent/cbc:IssueDate` = `2026-04-22`
- Why: EventComment/IssueTime is "The time at which this comment was made." A comment contained in a document issued at 08:17 cannot have been made at 11:00 the same day.
- Condition: the comment's date and time are not later than the document's issue date and time.
- Options: (a, preferred) comment time before 08:17 (e.g. from the sales meeting the note mentions); (b) issue the event later than 11:00, keeping it before the forecast 05 (11:55), which builds on it.
- Needs decision: no

### retail/06#F2 · Medium · "Original document" reference is not a forecast and resolves nowhere
- XPath: `/RetailEvent/cac:OriginalDocumentReference/cbc:ID` = `BM-PROMO-PLAN-26`
- XPath: `05-Forecast.xml:/Forecast/cbc:ID` = `BS-FC-26-0221`
- Why: In a RetailEvent, OriginalDocumentReference is "A reference to a Forecast document associated with this event." `BM-PROMO-PLAN-26` names a promotion plan, not a forecast, and occurs in no other example (`grep -rn --include='*.xml' 'BM-PROMO-PLAN' world/examples`: this file only). The flow's forecast, 05, is issued after this event (11:55 vs 08:17) and refers back to the promotion, so it cannot be the original document either.
- Condition: OriginalDocumentReference, if present, identifies a forecast that exists before this event; otherwise a promotion plan is referenced through an element meant for any document, with its type stated.
- Options: (a, preferred) drop OriginalDocumentReference: the event comes first and the forecast 05 follows it; (b) keep the plan as a generic reference with DocumentType "Promotion plan", if the RetailEvent schema offers one (it has no AdditionalDocumentReference, so (a) is likely the way).
- Needs decision: no

### retail/06#F3 · Low · Participating location named after the company, without an identifier
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:ParticipatingLocationsLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `22-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- Why: ParticipatingLocationsLocation is "The location of the stores involved in the event". The name is the retailer plus a city, not a store, and carries no GLN, although the flow identifies Brightmarket's places by GLN: goods-in `9522610900019` in 08, and the garden department of the Lumeport store `9522610900026` in 22 (also `furniture/06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:Name` = `Brightmarket Stores, garden department, Lumeport`). A supplier planning deliveries for the promotion cannot tell which store (or whether all Lumeport stores) take part.
- Condition: the participating location identifies the store(s) taking part, by name of the store and, where one exists, its GLN.
- Options: (a, preferred) the store's name and the garden department's GLN `9522610900026`, where the display stands; (b) if several stores take part, one event line item per store.
- Needs decision: no

## Checked and consistent
- Periods: promotion 2026-05-11 to 2026-05-24 (two weeks, as the description says), the same in the planned impact and the event tactic; it lies within the forecast period of 05.
- Dates: SubmissionDate 2026-04-22 = issue date; LatestProposalAcceptanceDate 2026-04-26 is after it; FirstShipmentAvailabilityDate 2026-04-29 is the day the despatch advice 12 is issued (`12-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-04-29`).
- Quantities: event tactic quantity 12 EA equals the shelf space in the comment; planned impact 17976.00 XBL = 24 × 749 XBL, the regular consumer price, of which 74.90 is the 10 % reduction (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `674.1` = 749 − 74.90, with `21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:AllowanceCharge/cbc:Amount` = `74.90`). 24 benches equals the order 08; consistent with stock 3 + 24 against a display of 12.
- Item `LD-10442` matches catalogue line 1 of 02.
- SellerEventID and BuyerEventID are distinct identifiers of the two parties; the order 08 references this event by its document ID `BS-RE-26-0222`.
