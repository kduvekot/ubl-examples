# LLM review: 06-QualificationApplicationRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/06-QualificationApplicationRequest.xml`, Git blob `0aa9ad5b8c13d2a778a247ffd72698f140609eec` (committed)
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

### tender/06#F1 · High · Call for tenders referenced under an ID no document carries
- XPath: `/QualificationApplicationRequest/cac:AdditionalDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The reference points to the call for tenders of the procedure as `PWD-2026-PARKS-CFT`. The call for tenders is 03-CallForTenders.xml with the ID `LPWD-DOC-26-0189`; no document of the flow has the ID `PWD-2026-PARKS-CFT`. That ID is used in 8 examples (grep over the flow's XML files: 01, 02, 03, 06, 15, 17, 19, 24), while 25-Catalogue.xml uses `LPWD-DOC-26-0189`, so the flow has two IDs for one document.
- Condition: The reference carries the ID of 03-CallForTenders.xml (or 03 carries the ID the references use).
- Options: (a) use `LPWD-DOC-26-0189` (preferred); (b) keep one procedure-level ID for the call for tenders and carry it in 03 as well.
- Needs decision: no

### tender/06#F2 · Medium · The request already says that the criterion is fulfilled
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:FulfilmentIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicatorTypeCode` = `ALL`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:FulfilmentIndicatorTypeCode` = `ALL`
- Why: FulfilmentIndicator is "An indication that this criterion has been fulfilled" (for the group: "that this group of criteria have been fulfilled"), FulfilmentIndicatorTypeCode "A code signifying how this criterion has been fulfilled". This is the buyer's request, sent before the economic operator has answered anything; nothing has been fulfilled yet, and the buyer cannot state it. If the code is meant as "all properties must be met", the indicator still states a result that does not exist.
- Condition: A request states no result of the evaluation; fulfilment is stated, if at all, after the response.
- Options: (a) remove the two indicators from the request (and the type codes, unless the list defines them as a rule for fulfilment) (preferred); (b) carry them in a document that reports the evaluation.
- Needs decision: no

### tender/06#F3 · Medium · An indicator property with an expected identifier, code and URI
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ValueDataTypeCode` = `INDICATOR`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedID` = `REG`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedCode` = `REGISTERED`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedURI` = `https://register.bayvarra.example`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedIndicator` = `true`
- Why: The property "Registered in a business register" is typed as an indicator, and `ExpectedIndicator` = true is its expected answer. It also carries ExpectedID ("The expected identifier that the responder has to provide in the criterion response") `REG`, ExpectedCode `REGISTERED` and ExpectedURI ("The expected URL that the responder has to provide"). A responder cannot be expected to provide the identifier `REG` or the URL of the register as its answer to a yes/no question; the three values are the same statement again in other data types, without a business reason (CLAUDE.md: no fillers).
- Condition: A property expects an answer of the data type it declares, and only that.
- Options: (a) keep ExpectedIndicator and the description, remove ExpectedID, ExpectedCode and ExpectedURI (preferred); (b) split into separate properties (e.g. one asking for the register number as an identifier).
- Needs decision: no

### tender/06#F4 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/06#F5 · Low · Questions about years in business, registration and consortium share under the turnover criterion
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Name` = `General yearly turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:Name` = `Turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:Name` = `Years in business`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:Name` = `Registered in a business register`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:SubsidiaryTenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Name` = `Share in the consortium`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:SubTenderingCriterion/cbc:Name` = `Average turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:Description` = `The figures.`
- Why: TenderingCriterionPropertyGroup is "The sets of properties that can be used to fulfil the tendering criterion". The criterion is the yearly turnover (economic and financial standing); years in business, entry in a register and the share in a consortium do not fulfil a turnover criterion, they are other criteria (suitability, the notice's OperatingYearsQuantity). The sub-criterion "Average turnover" has only an ID and a name and asks nothing.
- Condition: Each criterion contains the properties that fulfil it; a sub-criterion says what it asks.
- Options: (a) own criteria for years in business and registration, the consortium share with the operator's role, and either properties for or no "Average turnover" (preferred); (b) rename the criterion to cover all of it.
- Needs decision: no

### tender/06#F6 · Low · The request's criteria are not those the notice announced
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Name` = `Debt ratio`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumValueNumeric` = `80`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:EmployeeQuantity` = `10`
- Why: The document defines "how the Exclusion Grounds and the Selection Criteria should be addressed". The notice and the call for tenders announce as selection criteria: turnover of 250 000, three years of operation, ten employees, three reference supplies in five years, and certified timber. The request asks for turnover and years, but not for employees, references or the timber certificate, and it adds a debt ratio of at most 80 % that the notice does not announce. Of the exclusion grounds ("any of the exclusion situations of the Public Procurement Act") only taxes and contributions are asked.
- Condition: The criteria of the request are those announced in the notice and the call for tenders, no more and no fewer (or the notice announces what the request asks).
- Options: (a) add the missing criteria and announce the debt ratio in the notice (preferred); (b) reduce the notice to what is asked.
- Needs decision: yes

### tender/06#F7 · Low · A requirement described as a question to answer; groups typed "when the indicator is true" without an indicator
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:TypeCode` = `REQUIREMENT`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:Description` = `Answer: yearly turnover.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- Why: In the criterion model this document comes from (ESPD; own knowledge) a requirement is a condition the buyer states and a question is what the operator answers; a property typed REQUIREMENT whose description starts "Answer:" mixes the two (P-1 and P-5). `ONTRUE` ("When the indicator is true") marks a group that applies only if a preceding yes/no question was answered with yes; the three top-level groups depend on no such question.
- Condition: Property types agree with their descriptions, and a conditional group type is used only for a group that depends on an indicator question.
- Options: (a) type the answered properties QUESTION with the limits as minimum/maximum, and use the unconditional group type for top-level groups (preferred); (b) reword the descriptions.
- Needs decision: no

### tender/06#F8 · Low · Both companies in Marrowdale were registered on 1 January 1996
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID." Brackenmere Furniture and Marrowdale Sawmill, two unrelated companies, have the same registration date, a New Year's Day; it reads as a default value, not as a date from each company's history. In 07 Brackenmere states 26 years (which would be 2000).
- Condition: Each company has its own registration date, consistent with what it says about its age.
- Options: (a) individual dates (preferred); (b) drop the date where the document does not need it.
- Needs decision: no

### tender/06#F9 · Low · A public body described as a company in a commercial register
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/06#F10 · Low · The department's tax exemption reason describes a sale
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit; prefix 952 is the GS1 range for demonstrations and examples (own knowledge), so it cannot be a real company.
- Turnover threshold 250 000.00 (expected and minimum) equals the threshold of the notice; period 2023-01-01 to 2025-12-31 is "the last three years"; three years in business equals OperatingYearsQuantity 3 of the notice; debt ratio 80 as numeric and as quantity in percent agree.
- Procedure code OPEN, project `PWD-2026-PARKS`, lot `LOT-1`, contract name and CPC 38111 agree with 02 and 03. Legislation `XB-PPA-2019` is the procurement act referenced in the notice.
- Brackenmere Furniture is described identically in 06 to 09, 17 to 19 and 23 (hash of leaf values); ISIC 3100 is the class the notice requires.

## Considered and refuted
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumQuantity`: the minimum of three years is stated three times (ExpectedValueNumeric, MinimumValueNumeric, MinimumQuantity) — refuted because the three agree; redundant, not wrong.
- `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumAmount`: 1 000 lume as the limit of "minor amounts" is not in the legislation text quoted — refuted because the buyer may set the limit in the request.
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name`: trade sales as the contact for a qualification request — refuted because for a small furniture maker the sales office handles tenders.
- `/QualificationApplicationRequest/cbc:IssueDate`: the request (2026-02-13) is sent before Brackenmere shows any interest — refuted because in an open procedure the buyer may send the self-declaration form to any operator that downloaded the documents.

## Outside this review
- No qualification application request to Valdara Industries exists in the flow, although Valdara submits a qualification (13); whether one is needed is a question of the flow's story.
