# LLM review: 06-RetailEvent.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/06#F1 · High · A comment made after the document was issued
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueTime` = `11:00:00`
- XPath: `/RetailEvent/cac:EventComment/cbc:IssueDate` = `2026-04-22`
- XPath: `/RetailEvent/cbc:IssueTime` = `08:17:00`
- Why: EventComment IssueDate/IssueTime are "The date/time on which this comment was made". The
  comment ("Shelf space for 12 benches at the entrance.") is dated 11:00, almost three hours after
  the retail event document carrying it was issued at 08:17 the same day.
- Condition: the comment's time is not later than the document's issue time.
- Options: a comment time before 08:17 (preferred), or no comment time.
- Needs decision: no

### retail/06#F2 · Medium · OriginalDocumentReference points to a promotion plan, not to a forecast
- XPath: `/RetailEvent/cac:OriginalDocumentReference/cbc:ID` = `BM-PROMO-PLAN-26`
- Why: in RetailEvent, OriginalDocumentReference is "A reference to a Forecast document associated
  with this event". `BM-PROMO-PLAN-26` is by its name a promotion plan, has no document type, and
  matches no example; the forecast of the flow is 05-Forecast.xml (`BS-FC-26-0221`), issued later the
  same day. The element is used for a document of another kind.
- Condition: OriginalDocumentReference identifies a forecast; other associated documents go
  elsewhere or nowhere.
- Options: (a) preferred: drop it, since the forecast follows the event and refers to it (05 should
  then point here, see its review); (b) if the promotion plan matters, carry it in a general
  reference outside RetailEvent's forecast reference — RetailEvent has none, so it would be dropped.
- Needs decision: no

### retail/06#F3 · Medium · A store opening event that the document says nothing about
- XPath: `/RetailEvent/cac:MiscellaneousEvent/cbc:MiscellaneousEventTypeCode` = `STOREOPEN`
- XPath: `/RetailEvent/cac:MiscellaneousEvent/cac:EventLineItem/cac:SupplyItem/cbc:Name` = `Park bench Serra 180`
- XPath: `/RetailEvent/cbc:Description` = `Ten per cent off garden furniture for two weeks.`
- Why: MiscellaneousEvent is "A miscellaneous event associated with this event", here a store
  opening. Nothing in the document (name, description, note, comments, locations) mentions a store
  opening, which store opens, or when; the participating location is the existing Lumeport store, and
  the event is a temporary price reduction. The element adds an event that has no place in the story
  (IND5/IND6).
- Condition: either the story has a store opening (named store, period or date) that the event
  describes, or there is no MiscellaneousEvent.
- Options: (a) preferred: drop it; (b) give Brightmarket a store opening in the story and describe it
  (location, date, why the bench is part of it).
- Needs decision: yes

### retail/06#F4 · Medium · A language code in LocaleCode
- XPath: `/RetailEvent/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is the language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/06#F5 · Low · The participating location is named after the company
- XPath: `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:ParticipatingLocationsLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- Why: ParticipatingLocationsLocation is "The location of the stores involved in the event". Its
  only content is a name made of the company and the town; it gives no store, no address and no GLN,
  although Brightmarket identifies its places by GLN elsewhere (its own GLN
  `/RetailEvent/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`).
- Condition: the location identifies the store (name of the store, address or GLN).
- Options: the store's name and address or GLN (preferred).
- Needs decision: no

### retail/06#F6 · Low · Signature and master data the event does nothing with
- XPath: `/RetailEvent/cac:Signature/cbc:ID` = `BM-SIG-26-0422E`
- XPath: `/RetailEvent/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/RetailEvent/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the signature has only an ID and a signatory; a promotion notice uses no customs trader number,
  share capital or tax registrations. (The social-media profile could serve a promotion, but nothing
  in the event refers to it.)
- Condition: each is absent or used.
- Options: drop them.
- Needs decision: no

## Checked and consistent
- Event period 2026-05-11 to 2026-05-24 is "two weeks"; the planned impact and the tactic have the
  same period; the period lies inside the forecast period of 05-Forecast.xml.
- Promotion amount 74.90 XBL is ten per cent of the consumer price 749.00 XBL used in
  21-PurchaseReceipt.xml; planned impact 17976.00 XBL = 24 × 749.00, the 24 benches of 08-Order.xml at the regular
  price (whether the impact should be valued at the reduced price is a question for the money lens).
- FirstShipmentAvailabilityDate 2026-04-29 is the despatch date of 12-DespatchAdvice.xml; the
  proposal was submitted on the issue date and the acceptance deadline (2026-04-26) is later, so a
  confirmed status at issue is possible.
- The supply item `LD-10442` is the bench of 02-Catalogue.xml.

## Considered and refuted
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:EventTactic/cac:EventTacticEnumeration/cbc:DisplayTacticTypeCode`:
  end-cap display for benches at the entrance — refuted because an end-cap (a display at the head of a
  run of shelving) is a plausible way to show benches near the entrance.
- `/RetailEvent/cac:PromotionalEvent/cac:PromotionalSpecification/cac:PromotionalEventLineItem/cac:EventLineItem/cac:RetailPlannedImpact/cbc:ForecastTypeCode`:
  `TOTAL` for a promotion's impact rather than `PROMOTIONAL` — refuted because the amount is the total
  sales value of the 24 benches, which is a total figure.
