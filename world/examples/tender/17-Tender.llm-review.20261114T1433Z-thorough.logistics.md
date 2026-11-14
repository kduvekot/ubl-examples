# LLM review: 17-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/17-Tender.xml`, Git blob `ea8d3a233b928425f6a062a240c2497a8e4da8a4` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/17#F1 · High · The tender names the other tenderer's qualification document, which is issued two days later
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cbc:IssueDate` = `2026-02-23`
- Why: the element is "a reference to the tenderer qualification document that has been used to qualify the tenderer". `VI-DOC-26-0199` is `13-TendererQualification.xml:/TendererQualification/cbc:ID` = `VI-DOC-26-0199`, the qualification of Valdara Industries, the competing tenderer, issued on `13-TendererQualification.xml:/TendererQualification/cbc:IssueDate` = `2026-02-25`, two days after this tender. Brackenmere cannot have been qualified by it and cannot have known its number. Brackenmere's own qualification in the flow is `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193` (2026-02-19). The same wrong reference is in Brackenmere's second tender (19).
- Condition: the reference names a qualification document of the tenderer itself, issued before the tender.
- Options: (a) refer to `BF-DOC-26-0193` (preferred; it is a qualification application response rather than a TendererQualification, which the fixing session should weigh); (b) add a TendererQualification of Brackenmere to the flow and refer to it; (c) remove the reference.
- Needs decision: yes

### tender/17#F2 · High · Call for tenders referenced under an ID that no document has
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: `CallForTenderDocumentReference` is "a reference to the call for tender document of which this tender result of". The call for tenders is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`, and the catalogue refers to the call for tenders by its real ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`). The ID occurs in 8 examples (01, 02, 03, 06, 15, 17, 19, 24; `grep -l` over `tender/*.xml`).
- Condition: both references carry the ID of example 03.
- Options: (a) `LPWD-DOC-26-0189` (preferred); (b) give the call for tenders the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no

### tender/17#F3 · High · Warranty on the frame: five years on the line, six years in the criterion response
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: the tender line offers a warranty of five years on the frame (text and period, 5 ANN); the response to the quality criterion `AC-2`, which the department scores in years, offers six years on the frame and the slats. Both statements are about the frame of the same bench, and they differ. (In Valdara's tender 15 the two do not collide: five years on the frame, ten on the coating.) The line's warranty text and period are identical to those of 15 and seem to have been carried over.
- Condition: the warranty stated on the tender line agrees with the warranty offered in the criterion response.
- Options: (a) six years on the line as well (text and `WarrantyValidityPeriod`) (preferred: the criterion response is the value that is evaluated); (b) five years in the response, which changes the score.
- Needs decision: no

### tender/17#F4 · Medium · Evidence reference with the other tenderer's document number
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- Why: `EvidenceDocumentReference` is "a reference to a non-structured evidentiary document supporting this tendered project". The ID has the prefix Valdara Industries uses for its documents (`VI-…`) and is the same ID as in Valdara's tender (`15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`), while every other document number in this tender is Brackenmere's (`BF-DS-PARK`, `BF-SLAT-PB2`, `BF-SIG-TENDER-17`). Brackenmere cannot support its tender with a competitor's reference document; the value is carried over from 15 (it is also in 19).
- Condition: the evidence reference names a document of the tenderer.
- Options: (a) a Brackenmere reference (e.g. a `BF-REF-…` document) with a document type (preferred); (b) remove the reference.
- Needs decision: no

### tender/17#F5 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/17#F6 · Low · "Replacement item" that looks like a spare part, identified only by a number
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- Why: `ReplacementRelatedItem` is "a catalogue item that may be a replacement for the item described in this tender line", i.e. another item that can be supplied instead of the bench. The ID reads as a slat for the bench PB-2, a spare part of the tendered item, not a substitute for it; it has no name or description and occurs nowhere else in the flow (only in 17 and 19).
- Condition: the related item is one that can replace the bench, and is identifiable; a spare part is given in an element for accessories or components, or left out.
- Options: (a) remove it, or name a real alternative model (preferred); (b) if a spare part is meant, use `AccessoryRelatedItem`/`ComponentRelatedItem` if the tender line offers one.
- Needs decision: no

### tender/17#F7 · Low · The tendered price is given as the response to the quality criterion
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `116640.00`
- Why: `AC-2` is the quality criterion of the call for tenders (in years); `Amount` is "the monetary amount tendered for this awarding criterion", and 116640.00 XBL is the tender total, which answers the price criterion `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`. There is no response for `AC-1`.
- Condition: an amount in a criterion response belongs to the criterion the response names.
- Options: (a) add a response for `AC-1` with the amount and remove it from the `AC-2` response (preferred); (b) remove the amount.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit.
- Issued 2026-02-23 16:37, after Brackenmere's qualification response (07, 2026-02-19) and status exchange (08/09), before the deadline 2026-02-26 12:00. `BF-DOC-26-0203` follows `BF-DOC-26-0194` in number and date. The withdrawal 18 refers to this tender by its ID.
- `ValidityPeriod` 90 DAY, `TenderEnvelopeID` `ENV-1`, lots `LOT-1`/`LOT-2`, `CallForTendersLineReference/LineID` 1 and sub-line 1.1 (240 SET) correspond to the call for tenders.
- Arithmetic: 240 × 470.00 = 112800.00 (line 1); 240 × 16.00 = 3840.00 (line 2); sum 116640.00 = monetary total. The unit price 470.00 is inside the range 350.00 to 600.00 of the price criterion.
- Lead time 7 DAY within the required 10; the quality response of 6 ANN is inside the criterion's range of 5 to 10 years; `AC-2.1` exists.
- `DocumentReference` `BF-DS-PARK` is used consistently at document and line level (and in 19).

## Considered and refuted
- `/Tender/cac:DocumentReference/cbc:ID`: generic reference with only an ID, resolving nowhere — refuted because the same ID on the tender line, next to the item, shows it is the data sheet of the tendered bench, as `VI-DS-B180` is in 15.
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount`: 18 says the price per bench "was entered wrongly" — refuted as a finding here: 470.00 is the tendered price of this document, corrected to 480.00 in 19 (115200.00 / 240); that is the story, not an inconsistency of this example.

## Outside this review
- The tender mentions "Courier of the guarantee's original" (`AdditionalFee`), and the terms require a tender guarantee, but the flow contains a guarantee certificate only for Valdara (14), none for Brackenmere. Whether the flow needs one is a question of the story.
- The tendering terms do not allow multiple tenders (`MultipleTendersCode` NOTALLOWED in 01 to 03). This tender is withdrawn only on 2026-02-24 17:56 (18), after the second tender 19 was issued (2026-02-24 12:10); the overlap is reported with 18.
