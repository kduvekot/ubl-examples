# LLM review: 06-QualificationApplicationRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/06#F1 · High · Reference to a call for tenders that no example carries
- XPath: `/QualificationApplicationRequest/cac:AdditionalDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The only document reference of the request names `PWD-2026-PARKS-CFT`. No example has that document ID: the call for tenders of the procedure is `03-CallForTenders.xml` with the ID `LPWD-DOC-26-0189` (the catalogue 25 refers to it by that ID). The reference has no `DocumentType` or `DocumentTypeCode` either, so only its ID says what it is. The same ID is used in 8 examples of the flow (`grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`).
- Condition: The reference resolves to the document ID of the call for tenders (or of the contract notice) of the procedure.
- Options: (a) Preferred: `LPWD-DOC-26-0189`, with a document type. (b) Give 03 the ID used here and change the catalogue.
- Needs decision: no

### tender/06#F2 · Medium · The request states that criteria "have been fulfilled" before anyone has answered
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicatorTypeCode` = `ALL`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:FulfilmentIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:FulfilmentIndicatorTypeCode` = `ALL`
- Why: `TenderingCriterion/FulfilmentIndicator` is "an indication that this criterion has been fulfilled", and in the property group "an indication that this group of criteria have been fulfilled"; the type codes say "how this criterion has been fulfilled". These are results of an evaluation. This document is the buyer's request, issued before the operator has answered; nothing can have been fulfilled, and `true` cannot be meant as a result. The world's code `ALL` is defined as a rule ("Every property must be fulfilled."), which shows the intention: to say how the criterion *is to be* fulfilled. That intention needs only the type code, if at all; the indicator states a fact that does not exist yet.
- Condition: A qualification application request carries no `FulfilmentIndicator`; if the rule "all properties" is to be stated, it is stated without asserting fulfilment.
- Options: (a) Preferred: remove both indicators; keep `FulfilmentIndicatorTypeCode` only if the world reads it as the rule, and record that reading as a difference from the UBL definition ("how this criterion has been fulfilled"). (b) Remove all four and state the rule in `EvaluationMethodTypeCode` and the note.
- Needs decision: yes

### tender/06#F3 · Medium · The turnover criterion holds questions on years in business, registration and consortium share
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Name` = `General yearly turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:CriterionTypeCode` = `ECONOMIC`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:Name` = `Turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:Description` = `The figures.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:Name` = `Years in business`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:Name` = `Registered in a business register`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:SubsidiaryTenderingCriterionPropertyGroup/cbc:Name` = `Consortium`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:SubsidiaryTenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Name` = `Share in the consortium`
- Why: A `TenderingCriterionPropertyGroup` is "the sets of properties that can be used to fulfil the tendering criterion". The criterion is "General yearly turnover" (economic and financial standing), its group "Turnover — The figures." Of its four properties only P-1 is about turnover. "Years in business" is a different requirement (the notices state it separately, as `OperatingYearsQuantity`), "Registered in a business register" is a matter of suitability to pursue the activity (the world's list has the criterion type `SUITABILITY` for it), and "Share in the consortium" is about the composition of the tenderer. None of them can fulfil a turnover criterion; an evaluator reading "all properties" would fail a tenderer on turnover for an unregistered partner.
- Condition: Every property sits under the criterion it helps to fulfil: turnover figures under the turnover criterion, years in business and registration under criteria of their own (or of the type `SUITABILITY`).
- Options: (a) Preferred: split into criteria (turnover; years in business; enrolment in a register) and move the consortium share to the description of the tenderer. (b) Rename the criterion to something that covers all four ("Economic standing and suitability") and change its type, which is weaker.
- Needs decision: no

### tender/06#F4 · Medium · An indicator question that also expects an identifier, a code, a description and a URI
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ValueDataTypeCode` = `INDICATOR`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedID` = `REG`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedCode` = `REGISTERED`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedDescription` = `Entered in a national register.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedURI` = `https://register.bayvarra.example`
- Why: Property P-3 declares the data type of its answer as `INDICATOR`; `ExpectedIndicator` `true` is the matching expectation. It also carries `ExpectedID` ("the expected identifier that the responder has to provide in the criterion response"), `ExpectedCode`, `ExpectedDescription` and `ExpectedURI` ("the expected URL that the responder has to provide"). One property has one answer of one type; a responder cannot provide the identifier `REG`, the code `REGISTERED` and the register's own web address in reply to a yes/no question. `REG` is not an identifier a responder has (that would be its registration number, which the buyer cannot expect in advance), and the URI is the address of the register, which is information for the responder, not an expected answer. The response 07 does not answer P-3 at all.
- Condition: Each property carries only the expectation that matches its `ValueDataTypeCode`.
- Options: (a) Preferred: keep `ExpectedIndicator`; remove the other four (the register's address fits the description or the evidence template). (b) Add separate properties for the registration number (type identifier, no expected value) if it is to be asked.
- Needs decision: no

### tender/06#F5 · Medium · Selection criteria differ from the ones the notices announce
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Name` = `Debt ratio`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumValueNumeric` = `80`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:EmployeeQuantity` = `10`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:SpecificTendererRequirement/cbc:Name` = `Certified timber`
- Why: The request is "a document issued by a buyer defining how the Exclusion Grounds and the Selection Criteria should be addressed" for this procurement. The selection criteria of the procedure are stated identically in 01, 02 and 03: a turnover of at least twice the estimate, three similar supplies in five years, three years in operation, ten employees, certified timber. The request asks for a debt ratio of at most 80 %, which none of the notices announces, and does not ask for the references, the staff or the timber certificate. A criterion that is not in the notice cannot be applied, and announced criteria that are never asked cannot be checked. (Turnover of 250000 lume and three years in business do agree.)
- Condition: The criteria of the request are the exclusion grounds and selection criteria the notices and the call for tenders announce, no more and no fewer.
- Options: (a) Preferred: replace the debt-ratio criterion by the announced technical criterion (references) and add the other announced requirements. (b) Add the debt ratio to the tenderer qualification request of the notices and the call for tenders.
- Needs decision: yes

### tender/06#F6 · Medium · A language code in `LocaleCode`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/06#F7 · Low · Requirements described as questions ("Answer: …"), and one of them is answered
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:TypeCode` = `REQUIREMENT`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:Description` = `Answer: yearly turnover.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:TypeCode` = `REQUIREMENT`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Description` = `Answer: liabilities as a share of total assets.`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- Why: The world's list defines `REQUIREMENT` as "a requirement set by the authority" and `QUESTION` as "a question the tenderer answers". P-1 and P-5 are typed `REQUIREMENT`, yet their descriptions begin with "Answer:" and they declare a data type for the answer; the response 07 answers P-1. Either they are questions, or the answer in 07 replies to something that is not asked.
- Condition: A property the operator must answer is typed as a question; a requirement states the condition and is not answered.
- Options: (a) Preferred: P-1 and P-5 as `QUESTION` with the minimum/maximum as the expectation. (b) Keep them as requirements, reword the descriptions ("At least 250000 lume a year"), and add question properties for the figures.
- Needs decision: no

### tender/06#F8 · Low · The same limit stated two or three times in one property, and "expected" values equal to minimums
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ExpectedAmount` = `250000.00`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:MinimumAmount` = `250000.00`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:ExpectedValueNumeric` = `3`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumValueNumeric` = `3`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumQuantity` = `3`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumValueNumeric` = `80`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumQuantity` = `80`
- Why: `ExpectedAmount` and `ExpectedValueNumeric` are "the expected amount/value that the responder has to provide in the criterion response"; `MinimumAmount`, `MinimumValueNumeric` and `MinimumQuantity` "the minimum … the response must have". A responder is not expected to answer exactly 250000 lume or exactly 3 years; only the minimum is meant. P-2 gives its minimum both as a number and as a quantity, P-5 its maximum both as a number and as a quantity in percent, although each declares one data type (`QUANTITY`, `PERCENT`).
- Condition: Each property states its limit once, in the element that matches its data type, and an expected value only where one exact answer is expected.
- Options: (a) Preferred: remove the `Expected…` elements from P-1 and P-2 and keep one minimum/maximum per property. (b) None other seen.
- Needs decision: no

### tender/06#F9 · Low · Top-level property groups typed "when the indicator is true" without an indicator to depend on
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cbc:PropertyGroupTypeCode` = `ONTRUE`
- Why: `ONTRUE` means the group is processed when a preceding indicator is answered with true (ESPD, from my knowledge; the world's list says "Answered when the criterion applies"). The three groups are the first and only groups of their criteria; no indicator question precedes them (P-1, P-5 and P-6 are amounts and a percentage), so nothing switches them on. The world's list has `ON` ("Always answered") for this case.
- Condition: A group is conditional only where an indicator property precedes it; unconditional groups are typed `ON`.
- Options: (a) Preferred: `ON` for PG-1, PG-2 and PG-3. (b) Add an indicator question before each group ("Does the tenderer meet …?").
- Needs decision: no

### tender/06#F10 · Low · Values that only state the default: no weighting, no translation
- XPath: `/QualificationApplicationRequest/cbc:WeightingTypeCode` = `NONE`
- XPath: `/QualificationApplicationRequest/cbc:WeightScoringMethodologyNote` = `Pass or fail; no weighting.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:TranslationTypeCode` = `NONE`
- Why: All criteria are evaluated pass or fail (`EvaluationMethodTypeCode`), so there is no weighting to describe; a weighting type "no weighting" and a methodology note saying the same state what absence implies. `TranslationTypeCode` `NONE` says that no translation is required of an extract from the Bayvarran register in a Bayvarran procedure.
- Condition: Weighting and translation elements are present only where a weighting or a translation is required.
- Options: (a) Preferred: remove the three. (b) Keep the note if the world's rule is that every request states its scoring method.
- Needs decision: no

### tender/06#F11 · Low · A sub-criterion with a name only
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:SubTenderingCriterion/cbc:ID` = `CR-TURNOVER-A`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:SubTenderingCriterion/cbc:Name` = `Average turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.`
- Why: "Average turnover" is a sub-criterion without description, properties or threshold. The criterion asks for the "turnover of the last three years" with a yearly minimum (P-1, 2023–2025); whether the minimum applies to each year or to the average is exactly what the sub-criterion would have to say, and it does not.
- Condition: The sub-criterion says what it requires, or is absent.
- Options: (a) Preferred: remove it and say in the description that the yearly turnover must reach the minimum in each of the three years (or on average). (b) Give it a description and a property.
- Needs decision: no

## Checked and consistent
- `ExpectedAmount`/`MinimumAmount` 250000.00 and the three years in business agree with the notices (`ThresholdAmount` 250000.00, `OperatingYearsQuantity` 3).
- Procedure code OPEN, folder `PWD-2026-PARKS`, contract name, lot `LOT-1` and the classification 38111 agree with 02/03; `Legislation` names the same Act (`XB-PPA-2019`) as the notices.
- `EvaluationMethodTypeCode` PASSFAIL agrees with the methodology note; the exclusion ground on taxes has a legal reference whose description ("the exception for minor amounts") matches the maximum of 1000.00 lume.
- GLN 9523710900008 of the operator: check digit correct (`check_ids.py`).

## Considered and refuted
- `/QualificationApplicationRequest/cbc:ContractName`: the model defines it here as the title "of a contract associated with this Tender" — refuted as a problem, wording of the model.
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:Legislation/cbc:JurisdictionLevel` = "National" in a federal country (the register is "federal", the tax is a state tax): suspected wrong level — refuted, "national" is the usual name of the country-wide level and the Act is the country's.
- `/QualificationApplicationRequest/cac:EconomicOperatorParty`: a request addressed to one operator in an open procedure, where the request is normally part of the documents — refuted, the model allows it ("the Economic Operator receiving the Qualification Application Request"); nothing contradicts it.
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:CopyQualityTypeCode` and `cbc:CertificationLevelDescription`: suspected fillers — refuted, they say that a plain copy of the register extract is enough, which is real information for the responder.

## Outside this review
- The request is dated 2026-02-13, the day after the call for tenders; the operator answers on 2026-02-19 and tenders on 2026-02-23. Timeline across documents.
