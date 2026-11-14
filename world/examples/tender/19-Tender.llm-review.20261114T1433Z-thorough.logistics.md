# LLM review: 19-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/19-Tender.xml`, Git blob `21feca31f7c744f8e198c18ed5445abb1d1142ee` (committed)
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

### tender/19#F1 · High · The tender "corrects the withdrawn tender" but is issued before the withdrawal
- XPath: `/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `/Tender/cbc:IssueTime` = `12:10:00`
- XPath: `/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.`
- Why: The note calls the first tender (`17-Tender.xml:/Tender/cbc:ID` = `BF-DOC-26-0203`) "the withdrawn tender". The withdrawal is `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:ID` = `BF-DOC-26-0204`, issued `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueDate` = `2026-02-24` at `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueTime` = `17:56:00`, i.e. 5 h 46 min after this tender, and its note says `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.` Each document says the other comes later. The document numbers follow the withdrawal's order (…0203 tender, …0204 withdrawal, …0205 this tender), not the issue times. In addition the procedure does not allow several tenders from one tenderer (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`), so at 12:10 Brackenmere would have had two live tenders.
- Condition: The issue date and time of this tender are later than those of the withdrawal `BF-DOC-26-0204` and not later than the submission deadline (`03-CallForTenders.xml:/CallForTenders/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`, 12:00), and the notes of 18 and 19 agree on the order.
- Options: (a) preferred: issue this tender after 24 Feb 17:56 (e.g. on 25 Feb), which keeps both notes and the numbering true; (b) issue the withdrawal before 12:10 on 24 Feb.
- Needs decision: no

### tender/19#F2 · High · Brackenmere's tender cites Valdara's tenderer qualification, issued a day later
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- Why: "A reference to the tenderer qualification document that has been used to qualify the tenderer." `VI-DOC-26-0199` is `13-TendererQualification.xml`, the qualification of another tenderer (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`, with Saltmere Engineering as subcontractor), a competitor of Brackenmere in this procedure. It was moreover issued on `13-TendererQualification.xml:/TendererQualification/cbc:IssueDate` = `2026-02-25`, a day after this tender, so it could not be cited on 24 Feb. Brackenmere's own qualification document in the flow is `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193` (19 Feb). The same reference occurs in `17-Tender.xml` (grep for `>VI-DOC-26-0199<` over `world/examples/**/*.xml`: 13, 15, 17, 19).
- Condition: The reference names a qualification document of Brackenmere Furniture that exists at the tender's issue time, or is absent.
- Options: (a) preferred: refer to `BF-DOC-26-0193` (it is a QualificationApplicationResponse, the document Brackenmere actually qualified with; whether that counts as "the tenderer qualification document" is a judgment, but it is the only qualification document of this tenderer); (b) add a TendererQualification of Brackenmere to the flow and cite it; (c) drop the reference.
- Needs decision: yes

### tender/19#F3 · High · The quality response promises six years of warranty, the line five
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- Why: The response to criterion AC-2 (`cbc:AwardingCriterionDescription` "Warranty and coating"; the criterion is scored between 5 and 10 years, `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`) offers six years on frame and slats, while the tender line for the same bench states a warranty validity period of five years and "Five years on the frame". The tender is scored on a period that its own line does not grant. (In `15-Tender.xml` the 10 years are "on the coating", which does not contradict five years on the frame; here both statements are about the frame.)
- Condition: The warranty period of the line and the period offered for AC-2 are the same, or the texts make clear that they cover different things.
- Options: (a) preferred: line warranty 6 years, "Six years on the frame and the slats."; (b) response 5 years.
- Needs decision: no

### tender/19#F4 · Medium · Evidence reference with another tenderer's document number
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- Why: "A reference to a non-structured evidentiary document supporting this tendered project." The identifier carries the prefix Valdara Industries uses for its own documents (VI-DOC-…, VI-DS-B180, VI-ESPD-26) and is the same evidence `15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025` cites, i.e. Valdara's references of 2025. Brackenmere's own documents are numbered BF-… (`BF-DS-PARK`, BF-ESPD-26, BF-ACC-2025 in `07-QualificationApplicationResponse.xml`). The reference has only an ID, so nothing else says what it is. Occurs in 15, 17 and 19 (grep for `>VI-REF-2025<` over `*.xml`).
- Condition: The evidence reference identifies a document of Brackenmere Furniture (and preferably says what kind of evidence it is), or is absent.
- Options: (a) preferred: an own evidence document of Brackenmere (e.g. its reference list) with a DocumentType; (b) drop it.
- Needs decision: no

### tender/19#F5 · Medium · The call for tenders is cited under an identifier no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: "A reference to the call for tender document of which this tender result of"; a DocumentReference ID is "an identifier for the referenced document". The call for tenders of the flow is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`. That string only occurs as a reference (grep for `>PWD-2026-PARKS-CFT<` over `world/examples/**/*.xml`: tender 01, 02, 03, 06, 15, 17, 19, 24), including inside the call for tenders itself (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`), whereas `25-Catalogue.xml:/Catalogue/cac:CatalogueLine/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189` cites the same document by its document ID. The line reference `cac:CallForTendersLineReference/cbc:LineID` = 1 can only be resolved against `LPWD-DOC-26-0189`.
- Condition: Every reference to the call for tenders in the flow uses one identifier, and that identifier is one the call for tenders carries as its own (its `cbc:ID`, or an identifier it visibly declares for itself).
- Options: (a) preferred: cite `LPWD-DOC-26-0189`; (b) keep `PWD-2026-PARKS-CFT` as the department's file number of the tender documents, but then make it recognisable (DocumentType/DocumentDescription) and use it in the catalogue too.
- Needs decision: no

### tender/19#F6 · Low · References with only an ID that do not say what they are
- XPath: `/Tender/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`
- Why: `cac:DocumentReference` is the generic "reference to another document associated with this document"; with only an ID the reader cannot tell that this is (presumably) the data sheet of the bench PB-2. The document is not part of the flow (grep for `>BF-DS-PARK<` over `*.xml`: 17 and 19 only), so nothing else explains it.
- Condition: The reference states the kind of document (DocumentType or DocumentTypeCode).
- Options: add `cbc:DocumentType` "Data sheet" (preferred).
- Needs decision: no

### tender/19#F7 · Low · "Replacement" item looks like a spare part
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:Quantity` = `1`
- Why: "A catalogue item that may be a replacement for the item described in this tender line." The identifier reads as a slat of the PB-2 bench, i.e. a part of the tendered item, not an item that can take its place; one slat does not replace one bench (quantity 1 EA). Nothing else in the tender or the flow identifies `BF-SLAT-PB2` (grep over `*.xml`: 17 and 19 only), so this rests on the identifier alone.
- Condition: The related item is an item that can be supplied instead of the bench PB-2, or the aggregate is absent.
- Options: (a) preferred: name a real substitute bench of Brackenmere; (b) remove it (TenderLine has no element for spare parts).
- Needs decision: no

### tender/19#F8 · Low · Signature identifier carries the example's file number
- XPath: `/Tender/cac:Signature/cbc:ID` = `BF-SIG-TENDER-19`
- Why: "An identifier for this signature", assigned by the signer. The suffix 19 is the position of this example in the flow's file numbering (`17-Tender.xml:/Tender/cac:Signature/cbc:ID` = `BF-SIG-TENDER-17`); Brackenmere has no reason to number its second tender "19". All other signature IDs of the flow are business names (BF-SIG-WD, PWD-SIG-RCPT, VI-SIG-TQ).
- Condition: The signature ID does not depend on the example's file number.
- Options: derive it from the document number (e.g. BF-SIG-0205) (preferred).
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN 9523710900008 has a correct check digit.
- Issue time 24 Feb 12:10 is before the submission deadline 26 Feb 12:00 and after the call for tenders (12 Feb) and Brackenmere's qualification response (19 Feb).
- `cbc:ContractFolderID` PWD-2026-PARKS, contract name, envelope ENV-1 / COMBINED, validity 90 DAY and lots LOT-1 and LOT-2 agree with `03-CallForTenders.xml`.
- `cac:CallForTendersLineReference/cbc:LineID` 1 exists in the call for tenders (bench, 240 EA; sub-line 1.1 ground anchor set 240 SET, same as here).
- Awarding criterion IDs AC-2 and AC-2.1 exist in the call for tenders; 6 years lies within the scored range 5–10 years.
- Arithmetic: 115200.00 / 240 = 480.00 per bench (within the CfT's 350–600); 3840.00 / 240 = 16.00; 115200.00 + 3840.00 = 119040.00. The corrected price differs from 17 only in the bench price (470 → 480), as the note says.
- Order units: pallet of 4, increment 4, minimum 20 and maximum 96 are multiples of 4; 240 = 60 pallets. Lead time 7 days is within the required 10 days.
- All codes (TenderTypeCode, TenderEnvelopeTypeCode, FeeTypeCode, PackLevelCode, ISIC 3100/8411, units EA/SET/DAY/ANN) are in their lists and fit their elements.

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity`: 96 is less than the tendered quantity 240 — refuted: the contract is a framework with releases; minimum and maximum apply per order, and the releases of the flow are within them.
- `/Tender/cac:TenderedProject/cac:TenderLine[2]`: no `CallForTendersLineReference` for the installation line — refuted: the call for tenders has only line 1 (the bench); installation is lot 2 without a request line, so there is nothing to refer to.
- `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount`: the tender total under the quality criterion AC-2 instead of the price criterion AC-1 — not kept as a finding of this lens (amounts belong to the money lens); noted so it is not lost: "the monetary amount tendered for this awarding criterion" would fit AC-1.
- `/Tender/cac:TenderedProject/cbc:VariantID`: `V0` although one variant is allowed — refuted: V0 reads as the base tender; nothing contradicts it.

## Outside this review
- `18-TenderWithdrawal.xml` cites a tender receipt `PWD-RCPT-BF-1` that is not in the flow; there is no receipt for this second tender either. Belongs to 18 and to the flow's story.
