# LLM review: 07-QualificationApplicationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/07-QualificationApplicationResponse.xml`, Git blob `b7881bd86aa8b49492a0144e2fe61673b25b13f4` (committed)
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

### tender/07#F1 · High · "All criteria answered", but only one of six properties has a response
- XPath: `/QualificationApplicationResponse/cbc:Note` = `All criteria answered.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-TURNOVER`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:Note` = `Answer every criterion.`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-DEBT`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-TAXES`
- Why: The request 06 asks three criteria with six properties (P-1 turnover, P-2 years in business, P-3 registration, P-4 consortium share, P-5 debt ratio, P-6 unpaid taxes) and says "Answer every criterion." This response has one TenderingCriterionResponse, for P-1, and repeats only the criterion CR-TURNOVER; its note says all criteria are answered. The document is "A self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria"; nothing is declared about the exclusion ground CR-TAXES or about the debt ratio.
- Condition: Every property of the request has a response (or the note does not claim it), including the exclusion ground.
- Options: (a) add responses for P-2 to P-6 (preferred; several of the values are already there, see the next finding); (b) reduce the request to what is answered.
- Needs decision: no

### tender/07#F2 · Medium · One response value carries eleven kinds of reply
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`
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
- Why: A ResponseValue is one of "The criterion requirement property values"; each Response… element is "used as a reply to the criterion requirement". The property answered, P-1, asks for an amount. The amount 410 000.00 answers it. The other ten values answer nothing P-1 asks: a time of 12:00:00, a measure of 12 months, the number and the quantity 26 (years, which would answer P-2), an indicator (which would answer P-3), a code, a date, an identifier, a URI and a text file. A reader cannot tell which value is the reply; several have no business meaning at all (the time), which the repository's rule against fillers excludes.
- Condition: A response value carries the reply in the data type the property asks for; other properties are answered in their own responses.
- Options: (a) keep ResponseAmount here, move years (26) and the registration indicator to responses for P-2 and P-3, and drop the rest (the accounts are already referenced as evidence) (preferred); (b) none other seen.
- Needs decision: no

### tender/07#F3 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/07#F4 · Low · Turnover of one year where three were asked
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `Yearly turnover of 410,000 lume.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01`
- Why: The request asks the turnover of the last three years (2023-01-01 to 2025-12-31); the response gives one figure for 2025 only.
- Condition: The response covers the period the request asks for.
- Options: (a) three response values, one per year (preferred); (b) the request asks for the last year only.
- Needs decision: no

### tender/07#F5 · Low · 26 years in business, registered 30 years ago
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseQuantity` = `26`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: If the quantity of 26 years is the years in business (the request's P-2), it does not agree with the registration on 1996-01-01, 30 years before this response.
- Condition: Years in business and registration date agree.
- Options: (a) 30 years, or an individual registration date (see the review of 06) (preferred); (b) none other seen.
- Needs decision: no

### tender/07#F6 · Low · No reference to the request that is answered; a reference to an unexplained "ESPD"
- XPath: `/QualificationApplicationResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-ESPD-26`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:ID` = `LPWD-DOC-26-0192`
- Why: The response does not name the request it answers (`LPWD-DOC-26-0192`); the link is only implied by folder, lot and criterion ID. Its one document reference, `BF-ESPD-26`, has an ID only: the response itself is the self-declaration (its own ID is `BF-DOC-26-0193`), so it is not clear what other document is meant.
- Condition: The response refers to the request by its ID, and any other reference says what it is.
- Options: (a) reference `LPWD-DOC-26-0192` with a document type, and drop or explain `BF-ESPD-26` (preferred); (b) none other seen.
- Needs decision: no

### tender/07#F7 · Low · A group name for a single economic operator
- XPath: `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere Furniture`
- Why: EconomicOperatorGroupName is the "Economic Operator Group Name associated with this Qualification", i.e. the name of a group of operators tendering together. Brackenmere Furniture answers alone; its own name as group name is a filler.
- Condition: The group name is present only when a group of economic operators applies.
- Options: (a) remove it (preferred); (b) none other seen.
- Needs decision: no

### tender/07#F8 · Low · A public body described as a company in a commercial register
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/07#F9 · Low · The department's tax exemption reason describes a sale
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit.
- Criterion `CR-TURNOVER`, property `P-1`, lot `LOT-1`, CPC 38111, procedure code, application type, folder and contract name equal those of the request 06; the response (2026-02-19) follows the request (2026-02-13).
- Turnover 410 000.00 is above the minimum of 250 000.00 and far below the 10 000 000.00 limit of the size class SMALL.
- SuppliedEvidence `EV-ACC-BF` is the Evidence of this document; its DocumentReference `BF-ACC-2025` equals ResponseID; evidence type "Annual accounts" matches the request's template evidence "Accounts".
- The base64 object decodes to "Annual accounts 2025, extract." (text/plain).

## Considered and refuted
- `/QualificationApplicationResponse/cac:Evidence/cac:EvidenceIssuingParty`: audited accounts issued by the company itself — refuted because the accounts are the company's document; the auditor only audits them.
- `/QualificationApplicationResponse/cac:Evidence/cbc:CandidateStatement`: "True and complete." is the candidate's statement, while the definition speaks of a statement "that the contracting authority accepts as a sufficient response" — refuted because the text is such a statement by the candidate.
- `/QualificationApplicationResponse/cac:Evidence/cac:Language`: defined as "a required translation to be part of the response" although the accounts are in English already — refuted because it states the language of the evidence, the only reading that makes sense in a response.
