# LLM review: 15-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/15-Tender.xml`, Git blob `a052a0ed15639e25ddae372a37b1960f7b6a9857` (committed)
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

### tender/15#F1 · High · Call for tenders referenced under an ID that no document has
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: `CallForTenderDocumentReference` is "a reference to the call for tender document of which this tender result of". The call for tenders, addressed to this tenderer, is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`. Valdara itself uses the real ID a month later (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`). The line reference (`/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersLineReference/cbc:LineID` = `1`) is right for example 03, but hangs on a document ID that does not resolve. The ID occurs in 8 examples (01, 02, 03, 06, 15, 17, 19, 24; `grep -l` over `tender/*.xml`).
- Condition: both references carry the ID of example 03.
- Options: (a) `LPWD-DOC-26-0189` (preferred); (b) give the call for tenders the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no

### tender/15#F2 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:SubcontractorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/15#F3 · Low · Replacement item and evidence that cannot be found anywhere
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- Why: `ReplacementRelatedItem` is "a catalogue item that may be a replacement for the item described in this tender line". The ID occurs only here in the whole flow; Valdara's catalogue under the framework (25) lists `VI-B180` and `VI-INST-B` and no `VI-C180-2026`, and the tender gives the replacement no name or description, so the department cannot tell what would replace the Serra 180. `EvidenceDocumentReference` is "a reference to a non-structured evidentiary document supporting this tendered project"; it has only the ID `VI-REF-2025`, and the qualification document the tender refers to calls its reference evidence `13-TendererQualification.xml:/TendererQualification/cac:Evidence/cbc:ID` = `EV-FER-PARKS` ("Ferrano reference"). Whether the two are the same document is not visible.
- Condition: the replacement item is identifiable (named, or present in the catalogue), and the evidence reference says what the evidence is, or uses the ID of the evidence in 13 if it is the same.
- Options: (a) add a name to the replacement item and a document type to the evidence reference (preferred); (b) remove the replacement item if no real alternative model exists.
- Needs decision: no

### tender/15#F4 · Low · The tender does not refer to the guarantee it has to be accompanied by
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: the tendering terms require a tender guarantee, constituted by 2026-02-26; the bank issued the certificate for this tender the day before (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:ID` = `BL-DOC-26-0200`, guarantee `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`). The tender mentions the guarantee only in a fee description; neither number appears in it (they occur only in 14), although the tender has a generic `DocumentReference` (used for the data sheet). The department has to match guarantee and tender by party and folder alone.
- Condition: the tender carries a reference to its guarantee (certificate or guarantee number).
- Options: (a) add a `DocumentReference` with `BL-DOC-26-0200` and a document type (preferred); (b) leave the link to the folder ID.
- Needs decision: no

### tender/15#F5 · Low · The tendered price is given as the response to the quality criterion
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `124080.00`
- Why: `AwardingCriterionID` is "an identifier of the awarding criterion being referred to"; `AC-2` is the quality criterion of the call for tenders (measured in years, 5 to 10), and the response's quantity of 10 years answers it. `Amount` is "the monetary amount tendered for this awarding criterion"; 124080.00 XBL is the tender total, which answers the price criterion `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`. There is no response for `AC-1`. The amount is attached to the wrong criterion.
- Condition: an amount in a criterion response belongs to the criterion the response names.
- Options: (a) add a response for `AC-1` with the amount and remove it from the `AC-2` response (preferred); (b) remove the amount, the price being in the monetary total.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.
- Issued 2026-02-25 09:13, before the deadline 2026-02-26 12:00 and after the qualification document (13, 08:52) and the guarantee (14, 2026-02-24). The receipt 16 (2026-02-25 17:47) refers to this tender by its ID `VI-DOC-26-0201`.
- `TendererQualificationDocumentReference` `VI-DOC-26-0199` resolves to 13, a tenderer qualification by the same tenderer, with the same subcontractor (Saltmere Engineering, 20410685) and the same two lots.
- `ValidityPeriod` 90 DAY = the validity the tendering terms require; `TenderEnvelopeID` `ENV-1` and envelope type COMBINED as in the terms; lots `LOT-1`, `LOT-2`.
- `CallForTendersLineReference/LineID` 1 and sub-line 1.1 (240 SET ground anchors) correspond to line 1 and sub-line 1.1 of the call for tenders (240 EA, 240 SET).
- Arithmetic of quantities: 240 × 499.00 = 119760.00 (line 1); 240 × 18.00 = 4320.00 (line 2); sum 124080.00 = monetary total, the estimate of the notice.
- Ordering data: pallet of 4, increment 4, minimum 20, maximum 96 are multiples of 4; the first release (26) orders 40 EA, within these bounds. Pallet of four benches of 1800 × 620 × 780 mm (catalogue 25): two side by side (1240 mm) in two layers (1560 mm) fit a 1800 × 1240 mm load unit, so the unit is physically plausible.
- Lead time 7 DAY is within the 10 days required; warranty 5 ANN equals the requirement; the coating warranty of 10 ANN is within the criterion's range of 5 to 10 years; `AC-2.1` exists in the call for tenders.
- `DocumentReference` `VI-DS-B180` (document and line) is the item specification the catalogue, order, despatch advice and invoice of the flow refer to.
- Unit codes EA, SET, DAY, ANN; world-list codes resolve.

## Considered and refuted
- `/Tender/cac:DocumentReference/cbc:ID`: generic reference with only an ID — refuted because the same ID is used as `ItemSpecificationDocumentReference` in 25, 26, 29 to 33, which shows what it is (the bench's data sheet).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure`: 7 days here, 5 days in the catalogue 25 — refuted, the catalogue is issued after the award and may offer a shorter time than the tender promised.
- `/Tender/cbc:IssueTime`: tender issued 21 minutes after the qualification document — refuted, both are prepared together and sent in sequence.
- `/Tender/cac:TenderedProject/cbc:VariantID`: `V0` although the terms allow one variant — refuted, an identifier for the base tender is a legitimate use.
