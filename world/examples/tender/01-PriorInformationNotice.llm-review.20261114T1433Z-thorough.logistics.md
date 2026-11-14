# LLM review: 01-PriorInformationNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/01-PriorInformationNotice.xml`, Git blob `8ffc7805e1260abb517917498ec704d7f21b863c` (committed)
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

### tender/01#F1 · High · Reference to a call for tenders that does not exist under this ID, in a notice issued a month before it
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: `CallForTendersDocumentReference` is "a reference to a Call for Tender associated with these tendering terms". No example of the flow has the document ID `PWD-2026-PARKS-CFT`. The call for tenders of the procedure is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`, issued on `03-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-02-12`, a month after this notice (`/PriorInformationNotice/cbc:IssueDate` = `2026-01-12`); the catalogue refers to it by that ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`). So the reference cannot be resolved, and a prior information notice cannot yet refer to the call for tenders. The ID `PWD-2026-PARKS-CFT` occurs in 8 examples of the flow (01, 02, 03, 06, 15, 17, 19, 24; `grep -l` over `tender/*.xml`).
- Condition: every `CallForTendersDocumentReference/cbc:ID` of the flow is the ID of the call for tenders (example 03), and a document issued before the call for tenders does not refer to it.
- Options: (a) remove the reference from the prior information notice (preferred: the document does not exist yet); (b) keep it only in documents issued after 2026-02-12, with the ID `LPWD-DOC-26-0189`.
- Needs decision: no

### tender/01#F2 · High · "Replaced notice" in a first version of the first notice of the procedure
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/PriorInformationNotice/cbc:VersionID` = `1`
- Why: `ReplacedNoticeDocumentReference` is "a reference to the notice that is being replaced". This is version 1 of the first notice of the procedure; no earlier notice exists, and no example has the ID `PWD-2026-PARKS-PIN` (it occurs only as this reference, in 01, 02, 03 and 24). If the ID is meant to name this very notice, the notice would replace itself, and under another ID than its own (`/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`).
- Condition: a `ReplacedNoticeDocumentReference` is present only where a notice replaces an earlier one, and then carries the ID of that notice.
- Options: (a) remove it here (preferred); (b) add an earlier notice to the story that this one replaces.
- Needs decision: no

### tender/01#F3 · Medium · Latest date to obtain a security clearance although none is required
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "the end date until which the candidates can obtain the necessary level of security clearance". The same tendering terms say that no clearance is required, so there is no "necessary level" and the date has no meaning (a value without a business reason, rule "no fillers"). The date itself (five days before the tender deadline of 2026-02-26 stated in 02 and 03) would be plausible if a clearance were required.
- Condition: the date is present only if a security clearance is required.
- Options: (a) remove the date (preferred); (b) require a clearance, which would change the story.
- Needs decision: no

### tender/01#F4 · Medium · Lot 2 is "works" here and "services" in every later document
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- Why: the same lot `LOT-2` is described as services in the contract notice, the call for tenders and the award notice: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`, `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`, `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`, and named `Installation of the benches` there. Nothing in the flow says the nature of the lot was changed between the prior information notice and the contract notice. Kept at Medium rather than High because a prior information notice states intentions.
- Condition: the nature code and the name of lot 2 are the same in every document of the procedure, or the change is stated.
- Options: (a) use `SERVICES` and the same name here (preferred: installation of delivered benches is classified as a service in 02, CPC 87390); (b) use `WORKS` everywhere.
- Needs decision: no

### tender/01#F5 · Medium · Language code in LocaleCode
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant (a country or region), not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale (for example the country where this variant of the language is used) from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/01#F6 · Low · Document reference with only an ID that does not say what it refers to
- XPath: `/PriorInformationNotice/cac:DocumentReference/cbc:ID` = `PWD-PARKS-PLAN-26`
- Why: `DocumentReference` here is the generic "reference to another document associated with this document". The ID occurs nowhere else in the flow (only in 01), and the reference carries neither a document type nor a description, so a reader cannot tell what the document is (presumably the parks renewal plan) or where to find it.
- Condition: the reference says what kind of document it is (`DocumentType` or `DocumentDescription`), or is removed.
- Options: (a) add a document type such as "Parks renewal plan 2026" (preferred); (b) remove the reference.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no identifiers with check digits in this example.
- Issue 2026-01-12 14:18 < requested publication 2026-01-13 < planned contract notice 2026-01-26 < guarantee constitution end 2026-02-26 < planned period 2026-03-23 to 2028-03-22 (exactly two years, matching "over two years" and the 24-month framework in 02) < estimated further publication 2030 ("about four years").
- `RequestedDeliveryDate` 2026-04-02 = start of the line's `DeliveryPeriod`; 2026-03-23 (start of the planned period, and the date of the order in 26) + lead time 10 days = 2026-04-02.
- Guarantee `ConstitutionPeriod/EndDate` 2026-02-26 is the tender deadline of 02/03; the guarantee certificate 14 is issued on 2026-02-24, in time.
- `OptionValidityPeriod/EndDate` 2028-03-22 = end of the planned period; renewal 12 MON.
- `ContractFolderID` `PWD-2026-PARKS` is the same in all tendering documents of the flow; lots `LOT-1`/`LOT-2` are defined in the document and used consistently in `TenderPreparation` and `LotsGroup`.
- `TenderPreparation/OpenTenderID` `OPEN-1` matches `OpenTenderEvent/IdentificationID` `OPEN-1` in 02 and 03.
- `SpecificTendererRequirement/LegalReference` "XB-ENV-2021 art. 12" names the act referenced in `EnvironmentalLegislationDocumentReference`.
- Codes: OID 2.16.840.1.101.3.4.1.46 is AES-256-GCM (own knowledge, NIST CSOR); CPC Ver.2.1 38111 "Seats, primarily with metal frames" and 381 "Furniture"; ISIC Rev.4 3100 and 8411; unit codes ANN, DAY, MON, EA, SET, IE (UN/ECE Rec. 20); tax category E in 5305 and scheme STT in 5153; all world-list codes resolve in the listing (no `?? NOT IN LIST`).
- The request-for-tender line (ID 1, same UUID) is identical in 01, 02 and 03: 240 EA, 120 to 288, delivery period, lead time, warranty 5 years.

## Considered and refuted
- `/PriorInformationNotice/cbc:PlannedDate`: the contract notice was planned for 2026-01-26 but 02 is issued on 2026-02-11 — refuted for this example because a planned date may slip, and 02's own dates (requested publication 2026-01-27, periods starting 2026-01-26) agree with the plan; the contradiction lies in 02's issue date and is reported there.
- `/PriorInformationNotice/cbc:RequestedPublicationDate`: only 13 days between the prior information notice and the planned contract notice — refuted because the fictional procurement act sets its own minimum periods; no real rule applies.
- `/PriorInformationNotice/cac:TenderingTerms/cbc:FundingProgramCode`: code without `listID` — refuted because it is the department's own programme code (party-internal codes are exempt from the listID rule).
- `/PriorInformationNotice/cac:ProcurementProject/cbc:ID`: same value as `ContractFolderID` — refuted because the department may name its procurement file after the project; they are not used as document references in this example.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumQuantity`: 288 is less than 240 plus the 120 benches of the extension option — refuted because 288 = 240 × 1.2 is the tolerance of the base quantity (the budget maximum is 124080 × 1.2 too) and the extension is a separate option with its own renewal amount.
- `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID`: refers to an opening event not contained in this notice — refuted because it is an identifier, the event is defined in 02/03 with the same ID.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cac:DocumentReference/cbc:ID`: reference with only an ID — refuted because its place (a document associated with the request-for-tender line) and its ID (`PWD-SPEC-BENCH-26`) say it is the bench specification, which 03 names as its technical document.
