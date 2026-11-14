# LLM review: 24-TenderContract.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/24-TenderContract.xml`, Git blob `f51644d96669fd1bea4cfc230ed7d7bb275322e5` (committed)
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

### tender/24#F1 · Medium · Call for tenders and prior notice cited under identifiers no document carries
- XPath: `/TenderContract/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- Why: A DocumentReference ID is "an identifier for the referenced document". The call for tenders of the flow is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189` and the prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`; no document has the IDs cited here (grep for `>PWD-2026-PARKS-CFT<` over `world/examples/**/*.xml`: tender 01, 02, 03, 06, 15, 17, 19, 24, always as a reference; `>PWD-2026-PARKS-PIN<`: 01, 02, 03, 24). Other examples cite the same two documents by their document IDs (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`; `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`). In addition ReplacedNoticeDocumentReference is "a reference to the notice that is being replaced": a signed contract replaces no notice.
- Condition: References to the call for tenders and to notices use an identifier those documents carry, the same one throughout the flow; a replaced-notice reference is present only where a notice replaces another.
- Options: (a) preferred: cite `LPWD-DOC-26-0189`, and drop the replaced-notice reference from the contract; (b) keep the file-style numbers but declare them on the documents themselves.
- Needs decision: no

### tender/24#F2 · Medium · A latest date for security clearance although none is required
- XPath: `/TenderContract/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- Why: "The end date until which the candidates can obtain the necessary level of security clearance." The same terms state that no clearance is required ("Parks are public places"), so there is no clearance to obtain by any date; and in a contract signed on 19 March the date is four weeks past. The pair is copied from the call for tenders (same values in 01–03).
- Condition: The date is present only if a clearance is required.
- Options: remove the date (preferred).
- Needs decision: no

### tender/24#F3 · Low · The contract is identified by three different numbers
- XPath: `/TenderContract/cac:ContractDocumentReference/cbc:ID` = `PWD-CONTRACT-2026-PARKS`
- XPath: `/TenderContract/cac:TenderResult/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/TenderContract/cbc:ID` = `LPWD-DOC-26-0210`
- Why: This document is itself "the framework contract, signed by both parties". Its `cac:Contract/cbc:ID` ("an identifier for this contract") is the number order, invoice and debit note use for the contract. `PWD-CONTRACT-2026-PARKS` reads as a third number of the same contract; it has no type, description or date and occurs nowhere else (grep over `world/examples/**/*.xml`: this example only). (The UBL 2.5 definition of this element, "A reference to a set of minutes", is evidently a copy error in the model and gives no guidance.) The reader cannot tell whether it is the signed contract text, an annex, or the same thing as `PWD-2026-PARKS`.
- Condition: The reference says what document it is and how it relates to the contract `PWD-2026-PARKS`, or uses the contract's number.
- Options: (a) preferred: add `cbc:DocumentType` (e.g. "Signed contract text") and an issue date; (b) drop it.
- Needs decision: no

### tender/24#F4 · Low · Tender-phase references and dates carried into the signed contract
- XPath: `/TenderContract/cac:TenderingTerms/cac:ContractualDocumentReference/cbc:ID` = `PWD-CONTRACT-DRAFT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`
- Why: ContractualDocumentReference is "a reference to a document that will become part of the awarded contract": in the signed contract the draft has been replaced by the contract itself. The only guarantee in the terms is the tender guarantee, due on 26 February, three weeks before this document; the guarantee that matters for the contract, the performance guarantee due 19 March (`22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`), is not mentioned. The terms are the call for tenders' terms unchanged.
- Condition: The contract carries the terms that govern the contract; references and dates that only applied to tendering are absent or updated.
- Options: (a) preferred: reduce the tendering terms to what binds the parties (penalty, warranty, payment, subcontracting, execution requirement) and name the performance guarantee; (b) leave as a record of the tendered terms.
- Needs decision: no

### tender/24#F5 · Low · Signed on the last day of the appeal period
- XPath: `/TenderContract/cbc:IssueDate` = `2026-03-19`
- XPath: `/TenderContract/cbc:IssueTime` = `17:24:00`
- XPath: `/TenderContract/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- Why: The unsuccessful tenderer may present an appeal until and including `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`; the awarded notification promises the contract "after the standstill period". The contract is signed at 17:24 on that last day.
- Condition: The contract's date is after the last day on which an appeal can be presented.
- Options: (a) preferred: sign on 20 March (formalisation period 20–22 March); (b) end the appeal period on 18 March.
- Needs decision: yes

### tender/24#F6 · Low · The project has another name than in the rest of the flow
- XPath: `/TenderContract/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/TenderContract/cbc:ContractName` = `Park benches for the parks renewal programme`
- Why: The procurement project is named `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme` in the notices and the call for tenders, and the contract name of this very document uses that name; the project here has no ID and a different name.
- Condition: The same project has the same name (and its ID `PWD-2026-PARKS`) wherever it is described.
- Options: use the call for tenders' name and ID (preferred).
- Needs decision: no

## Checked and consistent
- No identifiers with check digits outside the parties (`check_ids.py` reports no failures).
- `cac:PreviousDocumentReference` LPWD-DOC-26-0208 is the awarded notification to Valdara, the document this contract follows.
- Issue time 19 March 17:24 lies within the formalisation period 19–22 March and before the contract start `2026-03-23`; `cac:TenderResult/cbc:StartDate` equals the contract validity start; 24 MON end on 2028-03-22.
- `cac:TenderResult` agrees with 21, 22 and 23; tender statistics agree with 21 and with the tenders (119040.00 = 19, 124080.00 = 15; 2 tenders after the withdrawal of 17; 1 foreign).
- TenderingProcess ID PWD-2026-PARKS-P and lots LOT-1/LOT-2 are those of the call for tenders; two signatures, one per party.
- Codes in TenderingTerms and TenderResult are in their lists (same values as the call for tenders).

## Considered and refuted
- `/TenderContract/cac:TenderResult/cbc:ReceivedTenderQuantity`: `2` against three tender documents — refuted: 17 was withdrawn and replaced by 19.
- `/TenderContract/cac:TenderResult/cac:Contract/cbc:ID`: equal to `cbc:ContractFolderID` — refuted: consistent use as the contract number in 21–23, 26, 27, 32 and 34.
- `/TenderContract/cac:TenderingTerms/cac:AppealTerms/cac:PresentationPeriod/cbc:DurationMeasure`: appeal terms in a signed contract — refuted for this lens: a duration without dates contradicts nothing; whether it belongs in a contract is a question of context.
- `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID`: `OPEN-1` — refuted: resolves to the opening event of the call for tenders.
