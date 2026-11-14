# LLM review: 06-QualificationApplicationRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/06-QualificationApplicationRequest.xml`, Git blob `0aa9ad5b8c13d2a778a247ffd72698f140609eec` (committed)
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

### tender/06#F1 · High · Call for tenders referenced under an ID that no document has
- XPath: `/QualificationApplicationRequest/cac:AdditionalDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The request's only document reference ("a reference to an additional document associated with this document") names `PWD-2026-PARKS-CFT`, by its ID the call for tenders. The call for tenders of the procedure, issued the day before, is 03-CallForTenders.xml with the ID `LPWD-DOC-26-0189`, and the catalogue 25 refers to it by that ID; no example has the document ID `PWD-2026-PARKS-CFT`. The reference carries no `DocumentType` or `DocumentTypeCode`, so only its ID says what it is. The merge re-checked the possible reading that `PWD-2026-PARKS-CFT` names the set of procurement documents rather than the message: 03 itself cites the ID in `CallForTendersDocumentReference`, so the flow uses it as a procedure-level name, but no document carries it, and here it is cited as a document. The ID occurs in 8 examples (01, 02, 03, 06, 15, 17, 19, 24; `grep -rl --include='*.xml' PWD-2026-PARKS-CFT world/examples`).
- Condition: The reference resolves to the document ID of an existing document (the call for tenders 03, or the contract notice), and says what kind of document it is.
- Options: (a) `LPWD-DOC-26-0189` with a document type "Call for tenders" (preferred: the catalogue already uses it); (b) give the call for tenders the ID `PWD-2026-PARKS-CFT` throughout the flow and change the catalogue.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1)

### tender/06#F2 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale (a language as used in a place, such as the `en-XB` tags on texts in the flow). Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `-l` for files).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales named in `listID`.
- Options: (a) remove `LocaleCode` (preferred: `cbc:ID` states the language and nothing in the document uses a locale); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F4), context (F6), logistics (F3), parties (F1)

### tender/06#F3 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status"; `ACTIVE` means "Active, not in liquidation", and the scheme type `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411). A city department is not a business in a commercial register and cannot be in liquidation, so both codes carry a meaning that does not fit the party. The same description of the department is used in every example of the flow that describes it in full (broad compared a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop `CompanyLiquidationStatusCode` and the `COMMERCIAL` type for public bodies, keeping the register name and number (preferred); (b) a register type for public bodies in the world's list; (c) record in the world's rules that public bodies are entered in the federal business register.
- Needs decision: no
- From: broad (F9), parties (F4)

### tender/06#F4 · Medium · The turnover criterion holds questions on years in business, registration and consortium share
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Name` = `General yearly turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:CriterionTypeCode` = `ECONOMIC`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:Name` = `Turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:Description` = `The figures.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:Name` = `Years in business`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:Name` = `Registered in a business register`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:SubsidiaryTenderingCriterionPropertyGroup/cbc:Name` = `Consortium`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:SubsidiaryTenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Name` = `Share in the consortium`
- Why: A `TenderingCriterionPropertyGroup` is "The sets of properties that can be used to fulfil the tendering criterion". The criterion is "General yearly turnover" (type "Economic and financial standing"), its group "Turnover — The figures." Of its four properties only P-1 is about turnover. Years in business is a requirement of its own (the notices state it as `OperatingYearsQuantity`), registration in a register is suitability to pursue the activity (the world's list has the criterion type `SUITABILITY`), and the share in a consortium describes the tenderer's composition. None of them can fulfil a turnover criterion; with `FulfilmentIndicatorTypeCode` `ALL` ("Every property must be fulfilled") an unregistered partner would fail the tenderer on turnover. The property group is used with a meaning other than its definition, hence Medium (context); broad rated it Low.
- Condition: Every property sits under a criterion it helps to fulfil: turnover figures under the turnover criterion; years in business and registration under criteria of their own; the consortium share where the tenderer's composition is asked.
- Options: (a) split into criteria (turnover; years in business; enrolment in a register, type `SUITABILITY`) and move the consortium share to a criterion or question about the group, with the operator's role (preferred); (b) rename the criterion to cover all four and change its type (weaker: one pass/fail result for unrelated conditions).
- Needs decision: no
- From: broad (F5, part), context (F3)

### tender/06#F5 · Medium · The request states that the turnover criterion "has been fulfilled" before anyone has answered
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicatorTypeCode` = `ALL`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:FulfilmentIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:FulfilmentIndicatorTypeCode` = `ALL`
- Why: `FulfilmentIndicator` is "An indication that this criterion has been fulfilled" (in the group: "that this group of criteria have been fulfilled"); the type code is "A code signifying how this criterion has been fulfilled". These are results of an evaluation. This document is the buyer's request, issued before the operator has answered (07 answers on 2026-02-19); nothing can have been fulfilled. The world's code `ALL` is defined as a rule ("Every property must be fulfilled."), which shows the intent: to say how the criterion is to be fulfilled. That intent needs at most the type code, read as a rule; the indicator asserts a fact that does not exist yet. Only criterion 1 carries the indicators.
- Condition: The request carries no `FulfilmentIndicator`; where the rule "all properties" is stated, it is stated without asserting fulfilment.
- Options: (a) remove both indicators; keep `FulfilmentIndicatorTypeCode` only as the rule, and record that reading as a difference from the UBL definition ("how this criterion has been fulfilled") for the TC write-up (preferred); (b) remove all four and state the rule in the note.
- Needs decision: no
- From: broad (F2), context (F2)

### tender/06#F6 · Medium · "Expected" amounts and values that are the threshold, not an answer the responder has to give
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ExpectedAmount` = `250000.00`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:MinimumAmount` = `250000.00`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:ExpectedValueNumeric` = `3`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumValueNumeric` = `3`
- Why: `ExpectedAmount` is "The expected amount that the responder has to provide in the criterion response", `ExpectedValueNumeric` "The expected value that the responder has to provide"; `MinimumAmount` and `MinimumValueNumeric` are "The minimum amount/value the response must have". Each responder answers its own figure (`07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`), and any figure at or above the threshold passes; there is no amount or number the answer is expected to equal. As it stands each property says both "answer 250000.00 (3)" and "answer at least 250000.00 (3)".
- Condition: A threshold is carried as the minimum only; an expected value is given only where one exact answer is expected.
- Options: (a) drop `ExpectedAmount` from P-1 and `ExpectedValueNumeric` from P-2 (preferred); none seen that keeps them.
- Needs decision: no
- From: money (F1), context (F8, part)

### tender/06#F7 · Medium · An indicator property that also expects an identifier, a code and a URI
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ValueDataTypeCode` = `INDICATOR`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedID` = `REG`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedCode` = `REGISTERED`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedURI` = `https://register.bayvarra.example`
- Why: P-3 ("Registered in a business register") declares its answer to be an indicator, and `ExpectedIndicator` `true` is the matching expectation. It also carries `ExpectedID` ("The expected identifier that the responder has to provide in the criterion response"), `ExpectedCode` ("The expected code …") and `ExpectedURI` ("The expected URL that the responder has to provide"). A responder cannot provide the identifier `REG` (it identifies nothing; a register number differs per operator and cannot be expected in advance), and the URI is the register's own address, information for the responder rather than an answer. One yes/no property has one answer of one type; the other three are the same statement again without a business reason (no fillers). The response 07 does not answer P-3 at all. Context also listed `ExpectedDescription` ("Entered in a national register."); the merge leaves it out of the condition: it describes the expected answer and fits an indicator.
- Condition: Each property carries only the expectation that matches its `ValueDataTypeCode`; an expected identifier, where present, is one the responder can actually give.
- Options: (a) keep `ExpectedIndicator` and `ExpectedDescription`, remove `ExpectedID`, `ExpectedCode` and `ExpectedURI` (the register's address can go in the description or the evidence template) (preferred); (b) split into separate properties (e.g. one asking for the register number as an identifier, without an expected value).
- Needs decision: no
- From: broad (F3), context (F4), logistics (F2)

### tender/06#F8 · Medium · The request's criteria are not those the notices announce
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Name` = `Debt ratio`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumValueNumeric` = `80`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:EvaluationCriterionTypeCode` = `TURNOVER`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:EmployeeQuantity` = `10`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:SpecificTendererRequirement/cbc:Name` = `Certified timber`
- Why: The document is "A document issued by a buyer defining how the Exclusion Grounds and the Selection Criteria should be addressed … for a specific procurement". The notices and the call for tenders (01, 02, 03, verified in 02 and 03) announce one financial criterion, the turnover, plus three similar supplies in five years, three years of operation, ten employees and certified timber. The request asks for turnover and years in business, adds a pass/fail debt ratio of at most 80 % that none of them announces, and does not ask for the references, the staff or the timber certificate. Of the exclusion grounds ("any of the exclusion situations of the Public Procurement Act") only taxes and contributions are asked. The response 07 answers none of the debt ratio. The merge rates it Medium (with context): the document's purpose is to define the criteria of the procedure, and it defines others than the procedure's; broad and money rated it Low. Not High: the notices do not state that their list is exhaustive, so no value is contradicted outright.
- Condition: The criteria of the request are the exclusion grounds and selection criteria the notices and the call for tenders announce, no more and no fewer (or the notices announce what the request asks).
- Options: (a) replace the debt ratio by the announced criteria (references, staff, certified timber) (preferred: the published terms bind the procedure); (b) add the debt ratio to the tenderer qualification request of the notices and the call for tenders.
- Needs decision: yes
- From: broad (F6), context (F5), money (F3)

### tender/06#F9 · Low · Document number ahead of its date in the department's own series
- XPath: `/QualificationApplicationRequest/cbc:ID` = `LPWD-DOC-26-0192`
- XPath: `/QualificationApplicationRequest/cbc:IssueDate` = `2026-02-13`
- XPath: `05-ExpressionOfInterestResponse.xml:/ExpressionOfInterestResponse/cbc:ID` = `LPWD-DOC-26-0191`
- XPath: `05-ExpressionOfInterestResponse.xml:/ExpressionOfInterestResponse/cbc:IssueDate` = `2026-02-15`
- Why: The ID is "An identifier for this document, assigned by the sender". The department's numbers run in one series; number 0192 is issued on 2026-02-13, two days before number 0191. Across the flow the numbers 0187 to 0225 follow the order of the examples over all senders, not the issue dates. Low: nothing says the numbers are assigned in time order.
- Condition: Within one sender's series a higher number is not issued before a lower one (or the ID does not suggest a running number).
- Options: (a) issue this request after 05, e.g. on 2026-02-16, still three days before the response 07 (preferred, smallest change); (b) number the documents per sender in the order of their issue times.
- Needs decision: no
- From: logistics (F4)

### tender/06#F10 · Low · The department's customs trader number in a tendering document
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Data copied from the party's master data into a document that does nothing with it (section 4.8). A customs trader number identifies the party towards customs; this request declares nothing to customs (such numbers are used in the customs declarations 30 and 31 of the flow).
- Condition: Each party carries only the identifiers the document's purpose uses.
- Options: (a) leave the customs trader number out of the tendering documents (preferred); (b) keep it only where the document says what it is for.
- Needs decision: no
- From: parties (F2)

### tender/06#F11 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax, expressed as text": the party's own status. The text begins with "Sale to a public body", a property of a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax", quoted by parties) is a buyer status and fits; only the wording of the name and text describes a sale.
- Condition: The party's exemption reason states the party's status (a public body that buys free of the state sales tax).
- Options: (a) reword the text to the status, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F10), parties (F3)

### tender/06#F12 · Low · Registration date 1 January 1996, shared by 25 unrelated companies
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Brackenmere Furniture shares the date, a New Year's Day, with Marrowdale Sawmill and 23 other parties: 271 occurrences in 181 of the 250 examples (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, `-l` for files). It reads as a default, not a fact of each company. In the response Brackenmere states 26 years in business (`07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseNumeric` = `26`), which would mean 2000, not 1996; that contradiction is a finding of 07.
- Condition: Each company has its own registration date, consistent with what it says about its age (or none where the world has none).
- Options: (a) a date per company from its history (preferred: the flow compares the age with `OperatingYearsQuantity`); (b) drop the date where the document does not need it; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: broad (F8), parties (F5)

### tender/06#F13 · Low · Which turnover must reach 250000 is not said; a sub-criterion with a name only; "at least" here, "greater than" in the notice
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:SubTenderingCriterion/cbc:ID` = `CR-TURNOVER-A`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:SubTenderingCriterion/cbc:Name` = `Average turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:EndDate` = `2025-12-31`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- Why: P-1 asks for a "Yearly turnover" of at least 250000.00 over three years, under a criterion about the turnover "of the last three years" with a sub-criterion "Average turnover" that has only an ID and a name: no description, property or threshold. Whether each year, the average or the sum must reach the minimum is exactly what the sub-criterion would have to say. The response answers one year only (`07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`). The notice compares with "greater than", whereas a minimum includes the threshold.
- Condition: The request states which turnover figure is compared with the threshold (each year, or the three-year average), with a period that fits; the sub-criterion says what it requires or is absent; the comparison is the same as in the notice.
- Options: (a) "average yearly turnover 2023–2025 of at least 250000 lume" in the request and the notices, without the empty sub-criterion (preferred); (b) give the sub-criterion a description and a property; (c) the last year only, with the period 2025.
- Needs decision: no
- From: money (F2), context (F11), broad (F5, part)

### tender/06#F14 · Low · Top-level property groups typed "when the indicator is true" without an indicator to depend on
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- Why: The world's list defines `ONTRUE` as "Answered when the criterion applies (ESPD ONTRUE)"; in the ESPD model (own knowledge) it marks a group processed when a preceding indicator is answered true. The three groups are the first and only groups of their criteria; no indicator precedes them (P-1, P-5 and P-6 are amounts and a percentage). The list has `ON` ("Always answered") for this case.
- Condition: A group is conditional only where an indicator property precedes it; unconditional groups are typed `ON`.
- Options: (a) `ON` for PG-1, PG-2 and PG-3 (preferred); (b) an indicator question before each group.
- Needs decision: no
- From: broad (F7, part), context (F9)

### tender/06#F15 · Low · Properties typed as requirements but described as questions to answer, and answered
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:TypeCode` = `REQUIREMENT`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:Description` = `Answer: yearly turnover.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:TypeCode` = `REQUIREMENT`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Description` = `Answer: liabilities as a share of total assets.`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- Why: The world's list defines `REQUIREMENT` as "A requirement set by the authority" and `QUESTION` as "A question the tenderer answers". P-1 and P-5 are typed `REQUIREMENT`, yet their descriptions begin "Answer:", they declare a data type for an answer, and 07 answers P-1. The other properties (P-2, P-3, P-4, P-6) with the same wording are typed `QUESTION`.
- Condition: A property the operator must answer is typed as a question; a requirement states the condition and is not answered.
- Options: (a) P-1 and P-5 as `QUESTION`, with the minimum/maximum as the limit (preferred); (b) keep them as requirements with reworded descriptions ("At least 250000 lume a year") and add question properties for the figures.
- Needs decision: no
- From: broad (F7, part), context (F7)

### tender/06#F16 · Low · The same limit stated twice in one property, as a number and as a quantity
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumValueNumeric` = `3`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumQuantity` = `3`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumValueNumeric` = `80`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumQuantity` = `80`
- Why: For the argument (context): P-2 declares the data type `QUANTITY` and P-5 `PERCENT`, each one type; the limit is stated once as a bare number and once as a quantity (3 ANN, 80 P1), which is the same statement twice without a business reason. Against it (broad, logistics, money refuted it): the values agree, and `…ValueNumeric` and `…Quantity` are alternative carriers of the same limit, one without and one with a unit; redundancy is not a contradiction. The merge cannot settle whether one property may state its limit in both carriers, so the finding stays Low with both arguments.
- Condition: Either each property states its limit once, in the element that matches its data type, or the world records that both carriers are filled on purpose.
- Options: (a) keep `MinimumQuantity` for P-2 (type quantity) and `MaximumValueNumeric` for P-5 (a percentage is a number), drop the other (preferred); (b) record the convention.
- Needs decision: yes
- From: context (F8, part); refuted by broad, logistics and money (see "Considered and refuted")

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` (Brackenmere) has a correct check digit; prefix 952 is the GS1 range for demonstrations and examples (own knowledge), so it cannot be mistaken for a real company's.
- The turnover threshold 250000.00 XBL equals `ThresholdAmount` of the notices; "twice the estimate" is 2 × 124080.00 = 248160.00 (`EstimatedOverallContractAmount` in 01/02), rounded up to 250000.00 (re-done in the merge). Three years in business equal `OperatingYearsQuantity` 3. Debt ratio 80 as a number and as 80 P1 (percent) agree.
- `ApplicablePeriod` 2023-01-01 to 2025-12-31 is "the last three years" before the issue date; 2025 is the last financial year for the debt ratio. The 1000.00 lume maximum of P-6 gives a figure to the "minor amounts" of the criterion's description and of the legislation entry.
- Procedure code OPEN, `ContractFolderID` and project `PWD-2026-PARKS`, contract name, lot `LOT-1` and CPC 38111 agree with 02 and 03; `Legislation/ID` `XB-PPA-2019` is the procurement act of the notices. Criterion, group and property IDs are unique in the document. `EvaluationMethodTypeCode` PASSFAIL agrees with the methodology note.
- Issued 2026-02-13 08:25, the morning after the call for tenders (2026-02-12 13:26); the response 07 follows on 2026-02-19.
- Parties: Lumeport Public Works Department as ContractingParty and SignatoryParty, Brackenmere Furniture as EconomicOperatorParty; both described identically to the other examples of the flow that carry them (parties and broad compared them by script), apart from the findings. ISIC 3100 and 8411 fit; ISIC 3100 is the class the notice requires. Telephone numbers use +999 (not assigned, ITU-T E.164, own knowledge); web and mail addresses are in `.example`.
- Codes: CPC 38111; ISIC 3100, 8411; units ANN and P1; XBL; the world-list codes resolve.

## Considered and refuted
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumQuantity`: the minimum of three years stated three times (`ExpectedValueNumeric`, `MinimumValueNumeric`, `MinimumQuantity`) — refuted because the three agree; redundant, not wrong (from broad, logistics). The merge made the expected value part of F6 (its definition is not a minimum) and kept the numeric/quantity double as F16, Low/yes, with this argument.
- `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumQuantity`: 80 P1 beside `MaximumValueNumeric` 80 — refuted, same value, alternative carriers of the same limit, P1 is percent (from logistics, money); carried as the counter-argument of F16.
- `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumAmount`: 1000 lume as the limit of "minor amounts" is not in the legislation text — refuted because the buyer may set the limit in the request (from broad).
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:MinimumAmount`: 250000 against "twice the estimate" (248160) — refuted for this example: the request repeats the notices' threshold and does not mention the estimate; the difference lies in the notices (from money).
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name`: a sales contact ("Trade sales", customer service officer, Sales) for a qualification request — refuted because for a small furniture maker a public buyer's request is a sales matter, and name, job title and department agree (from broad, parties). The merge keeps the refutation; the contest merge (a) had kept the same contact as a Low finding (see the decisions file).
- `/QualificationApplicationRequest/cbc:IssueDate`: the request (2026-02-13) is sent to Brackenmere before it shows any interest, and after the call for tenders although the criteria belong to the procurement documents — refuted because in an open procedure the buyer may send the self-declaration form to an operator that obtained the documents (from broad, logistics).
- `/QualificationApplicationRequest/cac:EconomicOperatorParty`: a request addressed to one operator in an open procedure — refuted, the model defines the party as "The Economic Operator receiving the Qualification Application Resquest" (from context).
- `/QualificationApplicationRequest/cbc:ContractName`: the model's definition speaks of "a contract associated with this Tender" — refuted, wording of the model (from context).
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:Legislation/cbc:JurisdictionLevel` = `National` in a federal country — refuted, "national" is the usual name of the country-wide level and the Act is the country's (from context).
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:CopyQualityTypeCode` and `cbc:CertificationLevelDescription` as fillers — refuted, they tell the responder that a plain copy of the register extract is enough (from context).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` as an invalid form — refuted, the definition prescribes no format and the value reads as UTC−1 (from parties).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` belonging in `Room` — refuted, it is "The specific identifable location within a building where mail is delivered" (from parties).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` with a job title, and department "Procurement office" vs "Procurement" — refuted, a functional contact name is usual and both wordings name the same unit (from parties).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` against a local authority — refuted, the code is the level of the tax (the state sales tax), not of the party (from parties).

## Refuted in the merge
### context/F10 · Low · Values that only state the default: no weighting, no translation
- XPath: `/QualificationApplicationRequest/cbc:WeightingTypeCode` = `NONE`
- XPath: `/QualificationApplicationRequest/cbc:WeightScoringMethodologyNote` = `Pass or fail; no weighting.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:TranslationTypeCode` = `NONE`
- Why (context): all criteria are pass or fail, so there is no weighting to describe; "no weighting" and the methodology note state what absence implies; `TranslationTypeCode` `NONE` says that no translation is required of a Bayvarran register extract in a Bayvarran procedure. Condition: weighting and translation elements only where a weighting or a translation is required.
- Refuted because: the repository's rule is "nothing implied by absence" (IND6): a value must not be left to be inferred from a missing element, so saying explicitly that the criteria are not weighted is what the rule asks, and the world's list defines `NONE` as "The criteria are not weighted". `TranslationTypeCode` `NONE` is defined as "The document is accepted in its own language", real information for a foreign operator (an open procedure is open to operators from Urvania and Lisavu). Both are statements with a business reason, not fillers.

## Changed in the merge
- broad/F5 → F4 and F13: split; the misplaced properties (years, registration, consortium) are F4 (with context/F3), the empty sub-criterion joins money/F2 and context/F11 in F13. F4 raised from Low (broad) to Medium (context): the property group is used with a meaning other than its definition.
- broad/F7 → F14 and F15: split into the group type (ONTRUE) and the property type (REQUIREMENT), each combined with the separate context finding (F9, F7).
- context/F8 → F6 and F16: split; the expected values equal to the minimums join money/F1 as F6 (Medium, element meaning); the numeric/quantity double is F16, Low with Needs decision: yes, because three parts refuted it.
- context/F2 Needs decision yes → F5 no: aligned with broad and with the contest merge (FulfilmentIndicator in a request, Medium/no); the fix is encoding.
- broad/F6 (Low), money/F3 (Low), context/F5 (Medium) → F8 Medium, Needs decision yes: the document's purpose is to define the procedure's criteria.
- broad/F9, parties/F4 (Low) → F3 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies: Medium/no).
- broad/F8, parties/F5 (Needs decision no) → F12 yes: aligned with analysis/review-merge-decisions.md (RegistrationDate 1996-01-01: Low/yes); counts re-done.
- context/F4: `ExpectedDescription` taken out of the condition (F7): it fits an indicator.
- context/F10: refuted in the merge (above).

## Outside this review
- No qualification application request to Valdara Industries exists in the flow, although Valdara submits a tenderer qualification (13); whether one is needed is a question of the flow's story (from broad).
- Timeline: the request is dated 2026-02-13, the day after the call for tenders; the operator answers on 2026-02-19 and tenders on 2026-02-23 (from context).
