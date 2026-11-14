# LLM review: 20-TendererQualificationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/20-TendererQualificationResponse.xml`, Git blob `6cb54f8c8eae89a453504f165e001d727d6477c8` (committed)
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

### tender/20#F1 · High · Appeal period against the qualification decision is the award's appeal period
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`
- Why: PresentationPeriod is "the period during which an appeal can be presented". "The decision" of this document is the qualification resolution of `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:ResolutionDate` = `2026-03-03`, notified the same day (`/TendererQualificationResponse/cbc:IssueDate` = `2026-03-03`). Ten days from it end on 13 March. The stated period starts six days after the document, on the day of the award, and is identical to the appeal period of the award decision in `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09` and `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`. On 3 March the award date was not yet known, and for six days no appeal against the qualification decision could be presented although the text gives ten days from the decision.
- Condition: The period starts at the qualification decision or its notification (3 March) and is ten days long, or the text and the dates otherwise describe the same period.
- Options: (a) preferred: 2026-03-03 to 2026-03-13; (b) only a `cbc:DurationMeasure` of 10 DAY, as in the call for tenders.
- Needs decision: no

### tender/20#F2 · Low · Minutes reference with only an ID, not resolvable in the flow
- XPath: `/TendererQualificationResponse/cac:ResolutionDocumentReference/cbc:ID` = `PWD-MIN-QUAL-26`
- Why: "A document (e.g., meeting minutes) relating to consideration of tenderer qualifications." The element name tells the kind, but there is no issue date or description, and no other example mentions the document (grep for `>PWD-MIN-QUAL-26<` over `world/examples/**/*.xml`: this example only), so the reader cannot tell whether these are the minutes of the session of 3 March 10:00.
- Condition: The reference carries at least the date of the minutes (`cbc:IssueDate`), which agrees with the resolution date.
- Options: add `cbc:IssueDate` 2026-03-03 and a `cbc:DocumentType` (preferred); or leave as is.
- Needs decision: no

## Checked and consistent
- No identifiers with check digits in this example (`check_ids.py` reports none).
- Resolution date and time (3 March 10:00) precede the issue time (3 March 15:09) and follow the opening of the tenders (26 February 14:00) and Valdara's qualification `13-TendererQualification.xml` (25 February); they precede the award (9 March 09:30).
- Both resolutions name lots that exist (LOT-1, LOT-2), which are the lots Valdara's qualification names as interested lots; the note "Qualified for both lots" agrees with two ADMITTED resolutions.
- The remark on the installers' qualifications matches the call for tenders' required curricula (INSTALLERS).
- `cbc:ContractFolderID` and `cbc:ContractName` agree with the rest of the flow; AdmissionCode ADMITTED is in its list and fits the element.

## Considered and refuted
- `/TendererQualificationResponse`: no reference to the tenderer qualification it answers (`VI-DOC-26-0199`) — refuted: the document type has no element for it; receiver and contract folder identify the case.
- `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:ResolutionTime`: qualification decided only after the tenders were opened — refuted: usual in an open procedure, where qualification and tender arrive together.

## Outside this review
- The flow has no qualification response for the second tenderer, Brackenmere Furniture, whose tender was evaluated and ranked second (`23-UnawardedNotification.xml`).
