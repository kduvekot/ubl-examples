# LLM review: 16-TenderReceipt.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/16-TenderReceipt.xml`, Git blob `358439bdf09247da5f2bd664dc2d3fc8e35e72b0` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/16#F1 · Medium · A language code in `LocaleCode`
- XPath: `/TenderReceipt/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/16#F2 · Low · The receipt was "created" at 11:42 and issued at 17:47
- XPath: `/TenderReceipt/cbc:RegisteredDate` = `2026-02-25`
- XPath: `/TenderReceipt/cbc:RegisteredTime` = `11:42:00`
- XPath: `/TenderReceipt/cbc:IssueDate` = `2026-02-25`
- XPath: `/TenderReceipt/cbc:IssueTime` = `17:47:00`
- XPath: `15-Tender.xml:/Tender/cbc:IssueTime` = `09:13:00`
- Why: `RegisteredDate`/`RegisteredTime` are "the date/time, assigned by the sender, on which/at which the Tender Receipt was created"; `IssueTime` is the time "at which this document was issued". By these definitions the receipt was created at 11:42 and issued six hours later, at 17:47. The value 11:42 reads as the time the tender (issued 09:13) was registered on the platform, which is the fact a tenderer wants confirmed, but that is not what the definition says, and the document does not say which of the two times is the time of receipt. For an acknowledgement that proves timely receipt this matters.
- Condition: The registered time and the issue time of the receipt agree with their definitions (creation and issue of the receipt), and the time at which the tender was received is stated unambiguously.
- Options: (a) Preferred: registered and issue time a few moments apart (an automatic receipt), and the time of receipt of the tender in the note. (b) Keep 11:42 as the time of receipt and say so in the note, recording the reading as a difference from the definition.
- Needs decision: no

### tender/16#F3 · Low · The logistics provider of Valdara Industries, with contract number and key account desk, in a tender receipt
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: `ServiceProviderParty` is "a party providing a service to this party": Castrano Logistics, which warehouses and despatches for Valdara Industries, with the number of their arrangement and its key account desk. An acknowledgement of receipt has no use for the warehouse contractor of the tenderer. It looks copied from the party's master data into a document that does not use it.
- Condition: The party carries a service provider only in documents in which that provider acts or must be known (despatch, transport, customs).
- Options: (a) Preferred: remove the service provider here. (b) If the provider matters to the buyer, declare it where the document has a place for it (as a subcontractor or in the delivery terms).
- Needs decision: no

### tender/16#F4 · Low · Customs trader numbers of the parties in a tender receipt
- XPath: `/TenderReceipt/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- Why: The parties are identified also by their customs trader numbers. Nothing in this document is declared to customs; the numbers are used only when the benches cross the border (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- `TenderDocumentReference` `VI-DOC-26-0201` is the tender 15 of the receiver, issued the same morning (09:13) and registered at 11:42, a day before the deadline of 2026-02-26 12:00 ("Received on time").
- The note ("encrypted, unopened until the opening") agrees with the encryption data and the opening event of 02/03 (2026-02-26 14:00).
- ISIN XU0001042501 of the receiver's listing: check digit correct (`check_ids.py`).

## Considered and refuted
- `/TenderReceipt/cbc:Note`: "unopened until the opening" in a receipt was suspected to say more than a receipt can know — refuted, it is the department's own commitment and matches the procedure.

## Outside this review
- No tender receipt exists in the flow for the tenders of Brackenmere (17, 19), although its withdrawal (18) cites one (`PWD-RCPT-BF-1`); noted in 18.
