# LLM review: 07-QualificationApplicationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/07-QualificationApplicationResponse.xml`, Git blob `b7881bd86aa8b49492a0144e2fe61673b25b13f4` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/07#F1 · High · "All criteria answered", but one of six properties has a response
- XPath: `/QualificationApplicationResponse/cbc:Note` = `All criteria answered.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-TURNOVER`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:Note` = `Answer every criterion.`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `P-5`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `P-6`
- Why: The document is "A self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria for a specific procurement." The request 06 defines three criteria (turnover, debt ratio, unpaid taxes) with six properties (P-1 to P-6) and says "Answer every criterion." This response repeats one criterion (`CR-TURNOVER`) and has one criterion response, for P-1. The debt ratio (P-5, at most 80 %), the exclusion ground on unpaid taxes (P-6, at most 1000.00 lume), years in business (P-2) and registration (P-3) are not answered; the consortium share (P-4) does not apply to a sole operator. The note says the opposite of the content, and without an answer to the exclusion ground the self-declaration does not serve its purpose; the pass/fail evaluation cannot be made.
- Condition: There is a criterion response, with its `ValidatedCriterionPropertyID`, for every property of 06 that applies to the operator, and the note agrees with what is answered.
- Options: (a) add responses for P-2, P-3, P-5 and P-6 (several values are already in the document in the wrong place, F4) (preferred); (b) reword the note to a partial answer, which the buyer would then have to query or reject (a story change).
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1), money (F1)

### tender/07#F2 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F3), context (F4), logistics (F4), parties (F1)

### tender/07#F3 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411). It is not a business and cannot be in liquidation; both codes carry a meaning that does not fit the party.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F8), parties (F4)

### tender/07#F4 · Medium · One response value for an amount property carries replies of every other kind
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Response` = `As in the accounts.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseBinaryObject` = `QW5udWFsIGFjY291bnRzIDIwMjUsIGV4dHJhY3Qu`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseCode` = `MET`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseDate` = `2025-12-31`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseID` = `BF-ACC-2025`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseMeasure` = `12`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseNumeric` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseQuantity` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseTime` = `12:00:00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseURI` = `https://www.brackenmere.example/accounts-2025.pdf`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ValueDataTypeCode` = `AMOUNT`
- Why: A `ResponseValue` is one of "The criterion requirement property values"; each `Response…` element is "… used as a reply to the criterion requirement". The response replies to P-1, an amount; `ResponseAmount` 410000.00 answers it. The same value also holds a number and a quantity of 26 years (the answer to P-2, which has its own property), an indicator (the type of P-3), a measure of 12 months, a time of 12:00:00, a date, a code `MET` (a verdict, which is the evaluator's), an identifier and a URI of the accounts (already supplied as evidence), a text and a "binary object" that decodes to the 30-character sentence "Annual accounts 2025, extract." (a "binary graphic, picture, sound or video object" by definition). A turnover has no time of day and no 12-month duration; a reader cannot tell which value is the reply. One element of every type is filled without a business reason (no fillers). The merge's check: the decoded text, the date 2025-12-31 (the balance-sheet date) and the ID/URI of the accounts are at least related to the turnover; the time and the measure are not.
- Condition: A response value carries the reply in the element that matches the data type of the property it answers; answers to other properties are in their own criterion responses; supporting documents are given as evidence.
- Options: (a) keep `ResponseAmount` (and the description) here; move the 26 years to a response for P-2 and the indicator to one for P-3; drop time, measure, code, binary object and the duplicate ID/URI (preferred); (b) if every value type is to be shown, give the request properties that really ask for a date, a URI, a code and so on.
- Needs decision: no
- From: broad (F2), context (F2), logistics (F2), money (F3)

### tender/07#F5 · Medium · Turnover asked for 2023 to 2025, answered for 2025 only
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `Yearly turnover of 410,000 lume.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `Turnover 2025.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:EndDate` = `2025-12-31`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01`
- Why: P-1 applies to 2023-01-01 to 2025-12-31 under a criterion about the turnover "of the last three years" with a sub-criterion "Average turnover". The response gives one amount for 2025, with the accounts of 2025 as the only evidence, and still says the criterion is met. The turnover of 2023 and 2024, or the average, is missing: information the pass/fail evaluation depends on, hence Medium (logistics, money); broad and context rated it Low. The request itself does not say whether each year or the average counts (06 F13), which explains but does not fill the gap.
- Condition: The response covers the period the property asks for (one value per year, each with its period, or the three-year average with the period 2023–2025), with evidence for those years.
- Options: (a) three response values, one per year, with the accounts of the three years as evidence (preferred); (b) one value stated as the three-year average for 2023–2025; (c) ask only for the last year in 06.
- Needs decision: no
- From: broad (F4), context (F5), logistics (F3), money (F2)

### tender/07#F6 · Low · The response does not name the request it answers; its one reference does not say what it is
- XPath: `/QualificationApplicationResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-ESPD-26`
- XPath: `/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:ID` = `LPWD-DOC-26-0192`
- Why: The response uses the criterion and property IDs of the request (`CR-TURNOVER`, `P-1`), which are only meaningful within it, but never names the request `LPWD-DOC-26-0192`; the link exists only through `ContractFolderID`, lot and criterion IDs. Its only document reference, `BF-ESPD-26`, has an ID only and resolves to no example (`grep -l BF-ESPD-26` over the flow's XML finds only this file); by its name it is the operator's self-declaration, which is what this document is (a second number for `BF-DOC-26-0193`?). Context rated it Medium; the merge keeps Low (broad, logistics) and aligns with the contest merge ("Missing reference … to the request (06 response)": Low/no): the request can still be found through the folder and the criterion IDs.
- Condition: The response refers to the qualification application request by its document ID, and every other reference states the kind of document.
- Options: (a) an `AdditionalDocumentReference` to `LPWD-DOC-26-0192` with a document type, and drop `BF-ESPD-26` or give it a document type (preferred); (b) leave the request implicit and only type the existing reference.
- Needs decision: no
- From: broad (F6), context (F3), logistics (F5)

### tender/07#F7 · Low · A sole operator gives its own name as the economic operator group
- XPath: `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere Furniture`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: `EconomicOperatorGroupName` is the "Economic Operator Group Name associated with this Qualification", the name of a group of operators applying together. Brackenmere applies alone (its tenders 17 and 19 name no partner or subcontractor; checked in the merge); its own name repeats the party name and is no group name.
- Condition: The group name is present only when a group of operators applies, and is then the group's name.
- Options: (a) remove it (preferred); none other seen.
- Needs decision: no
- From: broad (F7), context (F6)

### tender/07#F8 · Low · The department's customs trader number in a tendering document
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Copied master data (section 4.8): the customs trader number identifies the department towards customs; this response declares nothing to customs (such numbers are used in the customs declarations 30 and 31).
- Condition: Each party carries only the identifiers the document's purpose uses.
- Options: (a) leave it out of the tendering documents (preferred); (b) keep it only where the document says what it is for.
- Needs decision: no
- From: parties (F2)

### tender/07#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F9), parties (F3)

### tender/07#F10 · Low · Registration date 1 January 1996, shared by 25 unrelated companies
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." The same New Year's Day is given for 25 parties, 271 times in 181 of the 250 examples (recounted: `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, `-l` for files): a default, not a fact of each company.
- Condition: Each company has its own registration date (or none where the world has none).
- Options: (a) a date per company from its history (preferred); (b) drop the date where unused; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F5), broad (F5, part)

### tender/07#F11 · Low · 26 years in business against a registration 30 years ago
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseQuantity` = `26`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: If the quantity of 26 years is the years in business (the only property of 06 measured in years is P-2), it does not agree with a registration on 1996-01-01, 30 years before this response: a company registered in 1996 has been in business at least 30 years. The merge keeps it Low, not High: the 26 sits unlabelled in the response to P-1 (F4), so it is not stated that it means years in business, and the registration date is itself a default (F10).
- Condition: The years in business the operator states and its registration date agree.
- Options: (a) a registration date from Brackenmere's history that fits 26 years (2000), given with F10 (preferred); (b) 30 years in a response to P-2.
- Needs decision: yes
- From: broad (F5)

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit (prefix 952, GS1 range for examples).
- Criterion `CR-TURNOVER`, property `P-1`, lot `LOT-1`, CPC 38111, procedure code OPEN, application type REGULATED, folder and contract name equal those of the request 06.
- Issued 2026-02-19 10:47, six days after the request (2026-02-13 08:25) and before Brackenmere's tenders (17: 2026-02-23, 19: 2026-02-24).
- `ResponseAmount` 410000.00 XBL is above the minimum of 250000.00 of 06 and the notices; the description "Yearly turnover of 410,000 lume." agrees with it; the currency is the one asked (XBL). Turnover 410000.00 is far below the 10000000.00 limit of the size class SMALL (broad).
- `SuppliedEvidence/ID` `EV-ACC-BF` is the `Evidence/ID` of this document; its `DocumentReference` `BF-ACC-2025` equals `ResponseID`; evidence type "Annual accounts" matches the request's template evidence "Accounts"; the confidentiality level is the same in response and evidence. `ResponseBinaryObject` decodes (Base64) to "Annual accounts 2025, extract." (re-done in the merge).
- Parties: Lumeport Public Works Department as ContractingParty; Brackenmere Furniture as EconomicOperatorParty, EvidenceIssuingParty and SignatoryParty, described as in the other examples of the flow (parties compared by script). +999 telephone numbers and `.example` addresses.

## Considered and refuted
- `/QualificationApplicationResponse/cac:Evidence/cac:EvidenceIssuingParty`: audited accounts issued by the company itself — refuted, the accounts are the company's document; the auditor issues the audit opinion, which is not the evidence given (from broad, context, parties).
- `/QualificationApplicationResponse/cac:Evidence/cbc:CandidateStatement` = "True and complete.": the definition speaks of a statement "that the contracting authority accepts as a sufficient response" — refuted, it is the text of the candidate's statement that the buyer accepts (from broad, context).
- `/QualificationApplicationResponse/cac:Evidence/cac:Language`: defined as "a required translation to be part of the response" although the accounts are in English — refuted, it states the language of the evidence, the only reading that makes sense in a response (from broad).
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ConfidentialityLevelCode` = CONFIDENTIAL against a public evaluation — refuted, turnover figures are commonly confidential (from context).
- `/QualificationApplicationResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-ESPD-26`: "ESPD" is an EU term in a fictional world — refuted as a clash, the UBL definition of the request speaks of a "Single Procurement Document"; what the ID refers to is F6 (from context).
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseID`: an identifier as a reply to an amount property, as a separate finding — refuted, it is the ID of the evidence document the response supplies; it is a line of F4 (from logistics).
- `/QualificationApplicationResponse/cac:Evidence/cac:DocumentReference/cbc:ID`: `BF-ACC-2025` resolves to no example — refuted, annual accounts are not a UBL document of the flow and the evidence block says what they are (from logistics).
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseDate`: accounts of 2025 audited by 2026-02-19 — refuted, fast but possible for a small company; a timeline matter (from logistics).
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount`: 410000.00 too small for a tender of 119040.00 over two years (19) — refuted, about 59500 a year, some 15 % of the turnover, and the buyer's threshold is 250000.00 (from money).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` — refuted, a functional contact name; "Procurement office" and "Procurement" name the same unit (from parties).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` — refuted, the level of the tax, not of the party (from parties).
- `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact ("Trade sales") for a procurement procedure — refuted, for a small manufacturer the sales office answers tenders; name, job title and department agree (from parties). Kept refuted in the merge; the contest merge (a) had kept the same contact as Low.

## Refuted in the merge
### context/F7 · Low · "No weighting" repeated from the request
- XPath: `/QualificationApplicationResponse/cbc:WeightingTypeCode` = `NONE`
- XPath: `/QualificationApplicationResponse/cbc:WeightScoringMethodologyNote` = `Pass or fail.`
- Why (context): weighting and scoring method are the buyer's rules; the operator's response repeats them, and what it repeats is that there is no weighting. Condition: the response does not restate that there is no weighting.
- Refuted because: UBL gives the QualificationApplicationResponse its own `WeightingTypeCode` ("A code specifying the Weighting type") and `WeightScoringMethodologyNote`, so the model intends the response to restate the procedure's weighting (the ESPD response echoes the request's procurement-level data, own knowledge); and stating "not weighted" explicitly is what the rule "nothing implied by absence" asks (see the same refutation in 06). The values agree with 06.

## Changed in the merge
- broad/F4, context/F5 (Low) and logistics/F3, money/F2 (Medium) → F5 Medium: the evaluation depends on the missing years.
- context/F3 (Medium) → F6 Low, with broad/F6 and logistics/F5: aligned with the contest merge (missing reference to the request: Low/no).
- broad/F8, parties/F4 (Low) → F3 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- parties/F5 (Needs decision no) → F10 yes: aligned with analysis/review-merge-decisions.md (RegistrationDate 1996-01-01).
- broad/F5 → F11: Needs decision set to yes, because the fix gives Brackenmere a history (with F10); kept apart from F10 because it is a contradiction within this example.
- context/F7: refuted in the merge (above).

## Outside this review
- The tenders of this operator (17, 19) cite as their qualification `VI-DOC-26-0199`, the tenderer qualification of Valdara Industries (13), not this response; that lies in 17 and 19 (from context).
