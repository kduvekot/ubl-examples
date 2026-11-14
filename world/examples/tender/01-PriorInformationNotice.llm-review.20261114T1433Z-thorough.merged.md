# LLM review: 01-PriorInformationNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/01-PriorInformationNotice.xml`, Git blob `8ffc7805e1260abb517917498ec704d7f21b863c` (committed)
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

### tender/01#F1 · High · A latest date for obtaining security clearance, although no clearance is required
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "The end date until which the candidates can obtain the necessary level of security clearance." The same tendering terms say that no clearance is required (code `NOTREQUIRED`, "No security clearance is needed."), because parks are public places. There is no "necessary level" to obtain, so the date contradicts the term next to it and has no business reason (no fillers). The "not required" term itself only states what its absence would say (nothing implied by absence). The same pair occurs in 4 files: 01, 02, 03 and 24 (`grep -l LatestSecurityClearanceDate world/examples/*/*.xml`). The date itself (five days before the tender deadline of 02/03) would be plausible if a clearance were required.
- Condition: the tendering terms do not carry a latest security clearance date while they say that no clearance is required; a security clearance term is present only if a clearance is asked.
- Options: (a) preferred: remove the date, and the "not required" term with it, since nothing in the world asks for a clearance for park benches; (b) give the procedure a real clearance requirement (e.g. work on a guarded site) and keep both, which changes the story.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F3, Medium)

### tender/01#F2 · High · Reference to a call for tenders under an ID no document carries, in a notice issued a month before the call
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-02-12`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersDocumentReference` is "A reference to a Call for Tender associated with these tendering terms." No example of the flow has the document ID `PWD-2026-PARKS-CFT`; the call for tenders of the procedure is 03-CallForTenders.xml with the ID `LPWD-DOC-26-0189`, and the catalogue refers to it by that ID, so the flow uses two IDs for one document. In addition, this notice is issued on 2026-01-12, a month before the call for tenders: it refers to a document that did not exist yet. The ID `PWD-2026-PARKS-CFT` occurs in 8 files of the flow: 01, 02, 03, 06, 15, 17, 19, 24 (`grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`).
- Condition: every reference to the call for tenders uses the ID of 03-CallForTenders.xml, and a document issued before the call for tenders does not refer to it.
- Options: (a) preferred: remove the reference from the prior information notice; (b) keep one ID for the call for tenders throughout the flow and refer to it only from documents issued after it.
- Needs decision: no
- From: broad (F3), context (F2), logistics (F1)

### tender/01#F3 · High · A replaced notice is named, but this is version 1 of the first notice of the procedure
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/PriorInformationNotice/cbc:VersionID` = `1`
- XPath: `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `ReplacedNoticeDocumentReference` is "A class defining a reference to the notice that is being replaced." Nothing was published before this notice that it could replace, and no example has the ID `PWD-2026-PARKS-PIN`. The name suggests this very notice, which would then replace itself, under another ID than its own `LPWD-DOC-26-0187`. The reference occurs in 4 files: 01, 02, 03, 24 (`grep -l PWD-2026-PARKS-PIN world/examples/tender/*.xml`).
- Condition: a replaced notice is named only in a notice that replaces an earlier one, and then by that notice's document ID.
- Options: (a) preferred: remove the reference; (b) add an earlier, replaced notice to the story and let only the replacing notice carry the reference.
- Needs decision: no
- From: broad (F2, Needs decision yes), context (F3), logistics (F2)

### tender/01#F4 · High · Lot 2 is "works" here and "services" in the contract notice, the call for tenders and the award notice
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = `INSTALL`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- Why: The same lot `LOT-2` of the same procedure is classified as works here and as services (sub-type `INSTALL`, CPC 87390 installation services) in 02, 03 and 21, and its name differs. The nature of a lot decides which rules and thresholds apply, and nothing in the later documents says that it was changed. Logistics rated it Medium because a prior information notice states intentions; the merge keeps High because another example of the flow contradicts it and no change is stated (section 6).
- Condition: lot 2 has the same name and the same procurement type in every document of the flow, or a change is stated.
- Options: (a) preferred: `SERVICES` and "Installation of the benches" here as well (three later documents and the CPC code say so); (b) `WORKS` everywhere with a matching classification; (c) keep the change and state it in the contract notice.
- Needs decision: no
- From: broad (F4), context (F4), logistics (F4, Medium)

### tender/01#F5 · Medium · A language code in `LocaleCode`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language of the sibling `cbc:ID`; it names no locale (a language as used in a place, e.g. English as used in Bayvarra). The same value occurs 362 times in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `-rl` for files).
- Condition: `LocaleCode`, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) preferred: remove `LocaleCode` (nothing in the document uses a locale); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F7), context (F9), logistics (F5), parties (F1)

### tender/01#F6 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status", and the register type `COMMERCIAL` is "Commercial register: A register of businesses." The department is a local authority, and Bayvarra Information Service is classified ISIC 8411 (general public administration). A city department or a public service is not a business in a commercial register and cannot be in liquidation, so both values carry a meaning that does not fit these parties. The world's list of register types has no type for public bodies (COMMERCIAL, CHARITY, ASSOCIATION, FARM). The department is described the same way in all 36 examples of the flow (broad, by a hash of the party's leaf values).
- Condition: a public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or says in what capacity a public body is entered there).
- Options: (a) preferred: drop `CompanyLiquidationStatusCode` for public bodies and give their registration scheme a type that fits (a new code for a register of public bodies), or leave out the scheme details and keep the identifier; (b) state in the world's rules that public bodies are entered in the federal business register, and drop at least the liquidation status.
- Needs decision: no
- From: broad (F16, Low), parties (F4, Low)

### tender/01#F7 · Medium · Variants flagged as unconstrained in number, with a maximum of one
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:VariantConstraintCode` = `ALLOWED`
- Why: `VariantConstraintIndicator` is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)." `MaximumVariantQuantity` ("Maximum number of variants the tenderer is allowed to present") limits the tenderer to one variant. The indicator has no value for "allowed, at most one"; `true` asserts the opposite of the limit next to it, while `ALLOWED` and the maximum already say what is meant.
- Condition: the indicator is not `true` while a maximum number of variants is given.
- Options: (a) preferred: leave the indicator out and keep `VariantConstraintCode` and `MaximumVariantQuantity`; (b) drop the maximum, if any number of variants is accepted.
- Needs decision: no
- From: broad (F5), context (F5)

### tender/01#F8 · Medium · Tender guarantee of 2400.00 is not 2 % of any amount the notice states
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:Description` = `A bank guarantee for the tender.`
- Why: `AmountRate` is "The rate used to calculate the amount of liability in this financial guarantee." Recalculated: 2 % of the estimated contract amount 124080.00 is 2481.60; 2 % of the bench line 119760.00 is 2395.20; 2400.00 is 2 % of 120000.00, an amount the notice does not state. The certificate of the flow follows the amount (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`), so the rate is what does not fit. Money rated it High (arithmetic that does not hold), broad Low (probably rounded); the merge sets Medium: no base is stated, so no product can be shown to fail, but the information the guarantee is calculated from is missing and the rate cannot be applied as given. Merger D rates the same values in 24 Medium.
- Condition: liability amount = rate × a base the notice states (with the rounding said), or no rate is given.
- Options: (a) preferred: drop `AmountRate` and say in the description that the guarantee is a fixed 2400 lume; (b) state the base and the rounding (2 % of the lot 1 estimate, rounded to the hundred); (c) set the amount to the calculated value here and in every document that repeats it, including 14.
- Needs decision: no
- From: money (F2, High), broad (F10, Low), context (Outside this review)

### tender/01#F9 · Medium · Turnover criterion: "at least" in the text, "greater than" in the code, and a threshold that is not twice the estimate
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: "At least" is ≥; `GT` ("Greater than") and "Turnover > 2 × estimate" exclude a turnover of exactly the threshold. The world's ExpressionCode list has `GE` ("Greater than or equal to"). Twice the estimate of 124080.00 is 248160.00, not 250000.00: a turnover of 249000 meets the expression and fails the threshold. The definition of `ThresholdAmount` ("Estimated monetary amount of the threshold") leaves room for a rounded figure, but the rounding is not said.
- Condition: description, expression code, expression and threshold amount state the same comparison against the same limit.
- Options: (a) preferred: `GE` and "≥", with the description naming 250000 lume (about twice the estimate); (b) threshold 248160.00 with one comparison throughout; (c) change the text to "more than".
- Needs decision: no
- From: money (F3), broad (F11, Low), context (F12, Low)

### tender/01#F10 · Medium · Subcontract terms: a "precise" share equal to the maximum, an amount that is 3.5 % of the estimate, and a subcontract price flagged as known
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:UnknownPriceIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: `Rate` is "The precise percentage allowed to be subcontracted", `MaximumPercent` "The maximum percentage allowed to be subcontracted", `Amount` "The monetary amount assigned to the subcontracted task". The buyer sets a ceiling (30 %), so a "precise" share of 30 % says something else at the same time. The amount 4320.00 is the estimate of the installation and 3.48 % of 124080.00 (30 % would be 37224.00); the award documents of the flow pair the same amount with the matching rate (`22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`, `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`), so the flow uses `Rate` once as a limit and once as the actual share. `UnknownPriceIndicator` `false` says the subcontract price is known, which a buyer cannot say before tenders exist. Broad refuted the finding (the amount is the installation estimate and lies under the maximum; the repeated 30 is redundant, not contradictory); the merge agrees that the amount is not defined as rate × base, which is why it is not High (money), but `Rate` is used with a meaning other than its definition, which makes it Medium rather than Low (context).
- Condition: the buyer's subcontract terms state the limit it really sets (and, if wanted, the task that may be subcontracted with its estimate, explained), and make no statement about a subcontract price that does not exist yet.
- Options: (a) preferred: keep `MaximumPercent`, `SubcontractingConditionsCode` and `Description`; remove `Rate`, `Amount` and `UnknownPriceIndicator`; (b) keep `Amount` as the installation estimate, explained in the description, without `Rate`.
- Needs decision: no
- From: money (F1, High), context (F14, Low); broad refuted it (Considered and refuted)

### tender/01#F11 · Medium · The price of paper copies in the element for the reimbursement fee of concessions
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: `RequiredFeeAmount` is "The amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "Text describing the reimbursement fee for concession procurement projects." This is a supply contract, not a concession, and the 50 lume are the price of paper copies of the documents, which `DocumentationFeeAmount` ("The amount to be paid to obtain the contract documents and additional documentation") already states with the same value.
- Condition: no concession fee in a project that is not a concession; the documentation fee is stated once, in `DocumentationFeeAmount`, and its explanation in a text of the tendering terms.
- Options: (a) preferred: remove both elements and move the sentence to a `TenderingTerms/Note`; (b) none other seen.
- Needs decision: no
- From: broad (F6), context (F7), money (F4)

### tender/01#F12 · Medium · A strategic-procurement code in the element for an additional procurement type
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- Why: `ProcurementTypeCode` is "A code signifying the type of procurement project (e.g., goods, works, services)", and `ProcurementAdditionalType` "An association to additional procurement type." `GREEN` (list StrategicProcurementCode, "Environmental impact", noted there as eForms env-imp) is a policy objective, not a type of procurement in that sense. eForms uses the aggregate this way (BT-06, own knowledge); under the rule of semantic conformance that practice does not change the UBL meaning. The project's real additional nature (the installation lot) is not stated here.
- Condition: `ProcurementAdditionalType` carries a type of procurement; the environmental objective is stated where UBL has a place for it, or the difference is recorded as a deliberate finding for the TC.
- Options: (a) preferred: state the additional type that applies (the installation lot) and carry the environmental aim in the `ContractExecutionRequirement` and `SpecificTendererRequirement` that already state it; (b) keep the eForms-compatible encoding and record it as a finding for the UBL TC.
- Needs decision: yes
- From: broad (F8), context (F8)

### tender/01#F13 · Medium · Request line: minimum and maximum amount are unit prices, the estimated amount is a line total
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:Quantity` = `240`
- Why: The three elements are defined for the same thing: "The minimum amount allowed for this deliverable", "The maximum amount allowed for this deliverable", "The estimated total amount of the deliverable". The estimate is the total for 240 benches (240 × 499 = 119760), while minimum and maximum are prices of one bench. Read by the definitions, the line allows at most 600.00 for a deliverable estimated at 119760.00. The unit-price limits already sit where they belong, in the price criterion (`/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount` = `350.00`).
- Condition: minimum, maximum and estimated amount of the line are on the same basis.
- Options: (a) preferred: line totals in the line (for 240 benches 84000.00 and 144000.00) and the unit-price limits only in the price criterion; (b) drop minimum and maximum from the line and state the unit-price limits in the line's note.
- Needs decision: no
- From: money (F5)

### tender/01#F14 · Low · Urvanian declared as a language of the notice, but the notice has no Urvanian text
- XPath: `/PriorInformationNotice/cbc:NoticeLanguageCode` = `en`
- XPath: `/PriorInformationNotice/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- Why: `AdditionalNoticeLanguage` is "An additional official language used for this prior information notice." Every text is given once, in English; no element carries a `languageID` (0 in this file, counted with grep). Broad refuted a different question (why Urvanian at all: Urvanian tenderers take part under the Trade Accord), which the merge accepts; what remains is that the notice is not written in the language it declares.
- Condition: every language declared for the notice is used in it (texts repeated with `languageID`), or it is not declared.
- Options: (a) preferred: add the Urvanian rendering of the main texts (name, description, lots); (b) remove the additional language.
- Needs decision: no
- From: context (F19)

### tender/01#F15 · Low · Document reference with only an ID
- XPath: `/PriorInformationNotice/cac:DocumentReference/cbc:ID` = `PWD-PARKS-PLAN-26`
- Why: The generic `DocumentReference` carries neither a type nor a description, so a reader cannot tell what the document is (presumably the parks renewal plan) or why the notice refers to it. The ID occurs only in this file (grep over `world/examples/*/*.xml`).
- Condition: the reference says what kind of document it points to, or is removed.
- Options: (a) preferred: add `DocumentType` or `DocumentDescription`; (b) remove the reference.
- Needs decision: no
- From: broad (F19), logistics (F6)

### tender/01#F16 · Low · Customs trader number of the contracting party in a tendering document
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The prior information notice declares nothing to customs; the number is used when the benches are imported (31). It is copied from the party's master data into a document that does nothing with it (section 4.8).
- Condition: a party carries the identifiers the document uses; no customs number in a procurement notice.
- Options: (a) preferred: leave the customs trader number to the customs and transport documents; (b) keep it only if the world states a rule that every document carries all identifiers of a party.
- Needs decision: no
- From: context (F20), parties (F2)

### tender/01#F17 · Low · The department's tax exemption reason is worded as a sale
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: In `PartyTaxScheme`, the exemption reason is "A reason for the party's exemption from tax". The text starts with "Sale to a public body", a property of a transaction (a sale by someone else to the department), the same text as on the tax category of the project (`/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Sale to a public body`). The code's definition fits the party ("A body of the federation, a state or a city buys free of sales tax", world list XB TaxExemptionReasonCode). Money refuted the finding because the second half of the text states the party's status; the merge keeps it at Low because the first half still describes a transaction.
- Condition: the party's exemption reason states the party's status; the transaction's reason stays on the tax category.
- Options: (a) preferred: reword the text to the status, e.g. "Public body: buys free of the state sales tax", and keep the code; (b) a separate party-status code.
- Needs decision: no
- From: broad (F17), parties (F3); money refuted it (Considered and refuted)

### tender/01#F18 · Low · Eight further roles all filled with the contracting party itself
- XPath: `/PriorInformationNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The contracting party is repeated, by register number and name only, as originator, beneficiary and in six roles of the tendering terms, while it states that it acts `/PriorInformationNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationType` = `On its own behalf`. These roles exist for the case that another body or office does the task (a central purchasing body, a beneficiary department, a platform). Filled with the contracting party itself they say nothing the `ContractingParty` does not already say (no fillers). Broad refuted it (each role's definition is met by the department, and a notice may name them, IND6 explicit statement); the merge keeps it at Low, as the contest merges did for originator and beneficiary equal to the buyer. Context asked whether the parks department ("Head of parks" sits on the committee) is a body of its own that would be the real originator or beneficiary; that would change the story, but the preferred option does not.
- Condition: a role party is present only where it names a party, office or contact that differs from the contracting party, or adds details specific to the role.
- Options: (a) preferred: leave out the roles that only repeat the contracting party; keep `TenderRecipientParty` or `AdditionalInformationParty` only with their own contact (platform, helpdesk); (b) make the parks department the originator or beneficiary if it is a body of its own (story); (c) keep all as an explicit statement.
- Needs decision: no
- From: context (F18, Needs decision yes), parties (F5); broad refuted it (Considered and refuted)

### tender/01#F19 · Low · Maximum advertisement amount of 500 lume: advertised value or advertising cost?
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:AdvertisementAmount` = `320.00`
- Why: The definition is "The maximum advertised monetary value of the tendering process." Read literally, 500.00 is neither the estimate (124080.00) nor the maximum (148896.00) at which the procedure is advertised (broad, context). Money refuted that reading: the element pairs with `TenderResult/AdvertisementAmount` ("The monetary value of the advertisement for this tendering process"), which the award notice fills with 320.00; read together they are the cost of advertising the procedure (the CODICE meaning, own knowledge of broad and context), and 320 stays under the cap. The merge cannot settle which reading the UBL definition means; nothing in the notice explains the 500 either way.
- Condition: the amount fits the definition as the world reads it, with a stated reason (e.g. the awardee bears the advertising costs up to 500 lume), or the element is absent.
- Options: (a) preferred: decide the reading; if it is the advertising cost, say in a note or clause that the awardee bears it and record the unclear UBL definition for the TC write-up; (b) remove it; (c) set it to the advertised maximum value.
- Needs decision: yes
- From: broad (F9), context (F6, Medium); money refuted it (Considered and refuted)

### tender/01#F20 · Low · Penalty clause without the amount its percentages apply to
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: The clause does not say of what the percentages are taken (the contract value, the late release, the late part). The flow later applies it to the installation price of one release (`34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`); as published, the clause cannot be applied, and the debit note's base is one choice among several.
- Condition: the clause names the base of the percentages, and it is the base the debit note uses.
- Options: (a) preferred: "0.5 % of the price of the late part of a release per day late, at most 10 % of that price"; (b) another base, with the debit note following it.
- Needs decision: no
- From: money (F8)

### tender/01#F21 · Low · The qualification request is given the role "consortium lead"
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads a consortium.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: Within a `TendererQualificationRequest` ("Required set of qualifications for a tenderer"), `EconomicOperatorRole` ("A class to describe the tenderer contracting role") states the role the set applies to. With `LEAD` the only qualification request of the procedure applies to consortium leads only, although its content is asked of every tenderer, and the tenderers of the flow (Valdara Industries, Brackenmere Furniture) tender alone. The world's list also has `SOLE` ("Tenders alone"). "Leads a consortium." describes a party, not a requirement.
- Condition: the role of the qualification request matches who must meet it, or the role is absent.
- Options: (a) preferred: remove the role; (b) one request per role, with what is specific to a lead (e.g. joint liability) in a request with `LEAD`.
- Needs decision: no
- From: broad (F12), context (F13)

### tender/01#F22 · Low · Details that refer to a framework agreement, an electronic auction and an opening event the notice does not announce
- XPath: `/PriorInformationNotice/cac:TenderingProcess/cbc:Description` = `Planned as an open procedure in two lots.`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallFrameworkContractsAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:AverageSubsequentContractAmount` = `20680.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID` = `OPEN-1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cac:TenderEncryptionData/cbc:MessageFormat` = `CMS`
- Why: `EstimatedOverallFrameworkContractsAmount` ("The estimated overall monetary amount of subsequent framework contracts") and `AverageSubsequentContractAmount` presuppose a framework agreement with call-offs (124080 / 6 = 20680, so six releases are assumed, which the notice does not say); `MinimumImprovementBid` is defined "when used in an auction"; `OpenTenderID` identifies an opening event. This notice's tendering process mentions none of them; only 02 and 03 define the framework (`TenderingProcess/FrameworkAgreement`), the auction (`02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`) and the opening event with ID `OPEN-1`. A reader of the prior information notice alone gets the cipher of the envelope but is not told that a framework with an auction is planned. Money and context refuted the framework amount and the auction step "as such" (02 and 03 define them; "Two years of releases" hints at call-offs); logistics and broad refuted `OpenTenderID` (an identifier defined in 02/03 suffices). The merge accepts that the values are right for the procedure and keeps only what remains: the notice does not announce what they refer to.
- Condition: a notice that states framework amounts, an auction bid step or an opening identifier also says that a framework, an auction and an opening are planned, or does not carry these details.
- Options: (a) preferred: say in the process description that a framework with releases and an electronic auction are planned; (b) reduce the tendering terms of the prior information notice to the main conditions (subject, lots, estimate, planned dates), leaving the operational details (envelope, encryption, bid step, opening) to 02 and 03 (context's preference; see Outside this review).
- Needs decision: no
- From: broad (F15), money (F7), context (F21, Needs decision yes)

### tender/01#F23 · Low · The tender preparation is tied to lot 1 only
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:Description` = `One encrypted envelope per tender.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cac:DocumentTenderRequirement/cbc:Description` = `Unit prices per lot.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric` = `2`
- Why: The only `TenderPreparation` names lot 1, while its texts speak of "one encrypted envelope per tender" and "unit prices per lot", and a tenderer may tender for both lots. Nothing says how a tender for lot 2 is prepared.
- Condition: the tender preparation covers every lot a tender can be submitted for (no lot, both lots, or one preparation per lot).
- Options: (a) preferred: remove the lot from the preparation; (b) name both lots.
- Needs decision: no
- From: context (F15)

### tender/01#F24 · Low · Design-contest and negotiation indicators in an open supply procedure
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:NoFurtherNegotiationIndicator` = `true`
- XPath: `/PriorInformationNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: `PrizeIndicator` ("Indicates whether a prize will be awarded") and `FollowupContractIndicator` ("Indicates if any service contract following the contest will be awarded to the winner …") belong to design contests; with `false` they only state what their absence says. `BindingOnBuyerIndicator` ("Indicates if the decision is binding on the buyer") is the jury-decision indicator of a contest (eForms, own knowledge); here the buyer's own committee evaluates. `NoFurtherNegotiationIndicator` says something only in a procedure that could have negotiation; an open procedure has none.
- Condition: the awarding terms of this open supply procedure carry none of these indicators, unless the document explains what each refers to.
- Options: (a) preferred: remove all four; (b) keep `NoFurtherNegotiationIndicator` only if the world's procurement act lets an open procedure be followed by negotiation, and say so.
- Needs decision: no
- From: broad (F13, the two contest indicators), context (F10, all four)

### tender/01#F25 · Low · Quality criterion: a range of 5 to 10 years without explanation, and one sub-criterion of half its weight
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:WeightNumeric` = `40`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:Name` = `Durability of the coating`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- Why: `MinimumQuantity`/`MaximumQuantity` are "The minimum/maximum quantity for an awarding criterion." The criterion "Quality" has no description or expression, so a reader cannot tell what is counted from 5 to 10 years (presumably the warranty offered; the required warranty is 5 years). Its only sub-criterion weighs 20 of 40; the other 20 are not described. Money refuted the weight part (the rest is the warranty scored by the parent itself); that is a plausible reading, but the document does not state it, so the finding stays.
- Condition: the quality criterion says what its range measures, and its sub-criteria (or a description) account for its weight.
- Options: (a) preferred: two sub-criteria (coating durability 20, warranty years 20 with the 5–10 year range) and a description; (b) a description of the criterion only ("warranty offered, 5 to 10 years; coating durability"); (c) remove the range.
- Needs decision: no
- From: broad (F14), context (F16); money refuted the weight part (Considered and refuted)

### tender/01#F26 · Low · Technical committee of three officers, one named
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:TechnicalCommitteeDescription` = `Three officers of the department.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- Why: `TechnicalCommitteePerson` is "A member of a committee of experts evaluating the subjective criteria for awarding the contract" (0..n). The description says three officers; one is listed, and the reader cannot tell whether the other two are unnamed on purpose. The same committee appears in 01, 02, 03 and 24.
- Condition: the persons listed and the description agree.
- Options: (a) preferred: say that Mara Delling chairs the committee and the other members are appointed later; (b) list all three.
- Needs decision: no
- From: parties (F6)

### tender/01#F27 · Low · The whole two-year amount on one budget account of 2026
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric` = `2026`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MonetaryScope` = `Two years of releases.`
- Why: The releases run from 2026-03-23 to 2028-03-22, paid 30 days after each release, so the spending falls in the budget years 2026 to 2028. The single line charges the full estimate to an account of the year 2026 ("The number of the year for this budget account"). It may be meant as a multi-year commitment authorised in 2026; the document does not say so.
- Condition: the budget account line(s) show the budget year(s) of the spending, or say that the line is a multi-year commitment of the 2026 budget.
- Options: (a) one budget account per year with its amount; (b) preferred, smallest: state in the monetary scope or a note that it is a two-year commitment of the 2026 budget.
- Needs decision: yes
- From: money (F9)

### tender/01#F28 · Low · Works quality control stated for a supply project
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: `QualityControlCode` is "The indication of whether or not the control quality is included in the works project." The project is supplies; "Inspection on delivery" ("The buyer inspects every delivery") is an acceptance rule for delivered goods, not quality control included in a works project.
- Condition: `QualityControlCode` is present only for a works project or lot; the inspection of delivered benches is stated as a delivery or acceptance term.
- Options: (a) preferred: remove it and state the inspection in the contract conditions or a note; (b) keep it on the installation lot only if that lot is works (see F4).
- Needs decision: no
- From: context (F11)

### tender/01#F29 · Low · The buyer's estimates equal the winning tender to the cent
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- Why: The notice of 2026-01-12 estimates exactly the amounts Valdara tenders on 2026-02-25 (499 and 18 lume per bench), while the other tenderer offers 119040.00 (`19-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`). An estimate met to the cent reads as the outcome copied back into the estimate; all derived figures (minimum, maximum, renewal, average release, budget line) inherit it.
- Condition: the buyer's estimate differs from the tendered prices, or the story explains the equality (a published ceiling price the tenderer chose to offer).
- Options: (a) preferred: a rounded estimate (e.g. 500 and 20 lume per bench: 124800.00) with the derived amounts following it; (b) keep the figures and say in the tender that it offers the published estimate.
- Needs decision: yes
- From: money (F6)

### tender/01#F30 · Low · The additional classification is the parent group of the main one; the installation is not classified at project level
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `38111`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- Why: `AdditionalCommodityClassification` is "An association to additional classification categories for the deliverable requested." CPC 381 "Furniture" is the group that contains the main class 38111 "Seats, primarily with metal frames"; it adds no category. The second deliverable, the installation (lot 2, classified CPC 87390 in 02, 03 and 21), is not classified at project level.
- Condition: additional classifications name categories the main one does not already imply.
- Options: (a) preferred: 87390 as the additional classification of the project; (b) remove the additional classification.
- Needs decision: no
- From: context (F17)

## Checked and consistent
- Amounts (redone): 240 × 499 = 119760.00 (line estimate); 240 × 18 = 4320.00; 119760 + 4320 = 124080.00 = `EstimatedOverallContractAmount` = `EstimatedOverallFrameworkContractsAmount` = `TotalAmount` = `BudgetAccountLine/TotalAmount`; 124080 / 240 = 517; 120 × 517 = 62040.00 (minimum and renewal); 288 × 517 = 148896.00 (maximum; 288 = 1.2 × 240); 124080 / 6 = 20680.00 = the first release invoiced in 32 before the colour surcharge. Tax exempt, so `TaxIncludedIndicator` false does not contradict.
- Award weights 60 + 40 = 100, matching "Price 60 %, quality 40 %."; WSUM and BESTVALUE fit; formula "60 × lowest / tendered" fits INVERSE; price limits 350–600 contain the estimate's 499 and the tendered bench prices.
- Dates: issue 2026-01-12 14:18 < requested publication 2026-01-13 < planned contract notice 2026-01-26 < guarantee constitution end 2026-02-26 (the tender deadline of 02/03; certificate 14 issued 2026-02-24) < planned period 2026-03-23 to 2028-03-22 (two years) < further publication 2030 ("about four years"); 2026-03-23 + 10 days lead time = 2026-04-02 = `RequestedDeliveryDate` = start of the line's delivery period; option validity end = end of the planned period.
- `PaymentFrequencyCode` PERRELEASE agrees with "30 days after each accepted release."; `PostAwardProcess` indicators agree with the electronic catalogue, order, invoice and payment of the flow (25, 26, 32, 36); `OtherConditionsIndicator` and `RequiredCurriculaIndicator` have their text and code.
- `ContractFolderID` `PWD-2026-PARKS` is the same in all tendering documents; `OpenTenderID` `OPEN-1` matches the opening event of 02 and 03; the request-for-tender line is identical in 01, 02 and 03; `LegalReference` "XB-ENV-2021 art. 12" names the referenced environmental act.
- `NoticeDocumentReference` in 02 and 03 points to this notice's ID `LPWD-DOC-26-0187`.
- Codes: OID 2.16.840.1.101.3.4.1.46 is AES-256-GCM (own knowledge, NIST); CPC 38111 and ISIC 3100 fit the benches, ISIC 8411 the department and the information service; tax category E / STT agrees with the department's own tax scheme; all world-list codes resolve (no `?? NOT IN LIST`); XBL is not an assigned ISO 4217 code; telephone country code +999 is not assigned (ITU-T E.164, own knowledge).
- `check_ids.py`: no identifier with a check digit in this example.
- Every party is described identically in all examples of the flow that carry it (parties, by script), apart from the findings.

## Considered and refuted
- `/PriorInformationNotice/cbc:PlannedDate`: planned contract notice 2026-01-26, while 02 is issued 2026-02-11 — refuted because a planned date is a plan; 02's own dates agree with the plan, so the odd value is 02's issue date (reported there) (from broad, context, logistics).
- `/PriorInformationNotice/cbc:RequestedPublicationDate`: only 13 days between this notice and the planned contract notice — refuted because the fictional procurement act sets its own periods (from logistics).
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid`: an auction the notice does not announce — refuted as a finding of its own because 02 and 03 define the auction; what remains is in F22 (from broad, context).
- `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate`: rate and maximum both 30 with an amount of 3.5 % — refuted by broad because the amount is the estimate of the installation and lies under the maximum — the merge disagrees in part and keeps it as F10 (from broad).
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` not in ISO 8601 form — refuted because the element is text with no prescribed format and reads unambiguously as UTC−1 (from broad, parties).
- `/PriorInformationNotice/cac:OriginatorCustomerParty`: originator, beneficiary and six roles all the department — refuted by broad because each role's definition is met — the merge disagrees and keeps it as F18 (from broad).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumQuantity`: 288 is less than 240 + 120 of the extension — refuted because 288 = 1.2 × 240 is the tolerance of the base contract and the extension is a separate option (from broad, logistics).
- `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID`: an opening event the notice does not describe — refuted because 02 and 03 define the event with the same ID; what remains is in F22 (from broad, logistics).
- `/PriorInformationNotice/cac:AdditionalNoticeLanguage/cbc:ID`: Urvanian as additional language of a Bayvarran notice — refuted because Urvanian tenderers take part under the Trade Accord; the different point that the notice has no Urvanian text is F14 (from broad).
- `/PriorInformationNotice/cac:TenderingTerms/cbc:FundingProgramCode`: a code without `listID` — refuted because `PARKS-26` is the department's own programme number (party-internal codes are exempt) and matches `FundingProgram` (from context, logistics; broad's finding is under "Refuted in the merge").
- `/PriorInformationNotice/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric`: both 2 of 2 lots, suspected to say nothing — refuted because they state explicitly that a tenderer may tender for and win both lots (from context).
- `/PriorInformationNotice/cac:ProcurementProject/cbc:RequestedDeliveryDate`: one date for a two-year project — refuted because it is the first release and equals the start of the line's delivery period (from context).
- `/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementSubTypeCode`: PURCHASE against "subcategory of the type of work" — refuted because purchase is a sub-type of a supply contract and the definition's wording is an example (from context).
- `/PriorInformationNotice/cac:ProcurementProject/cbc:SMESuitableIndicator`: true against a turnover of 250000 and 10 employees — refuted, a firm of that size is still small (from context).
- `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:OperatingYearsQuantity` and `cbc:EmployeeQuantity` (and `PriceEvaluationCode`): the model prints the definition of the legal form — refuted, an error of the UBL model; the values fit the element names (from context; a note for the TC write-up).
- `/PriorInformationNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealInformationParty`: suspected wrong party — refuted, the review board is the natural source of information on appeals (from context).
- `/PriorInformationNotice/cac:TenderingTerms/cac:ContractResponsibleParty`: "the Party who executes the Contract" could mean the contractor — refuted because in the tendering terms it is the body that administers the contract; the repetition is in F18 (from context, parties).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallFrameworkContractsAmount`: framework amount without a framework — refuted "as such" because 02 and 03 declare the framework and the amount equals what the releases add up to — the merge agrees with the values and keeps the missing announcement as F22 (from context, money).
- `/PriorInformationNotice/cac:ProcurementProject/cbc:ID`: same value as `ContractFolderID` — refuted, the department may name its file after the project (from logistics).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cac:DocumentReference/cbc:ID`: reference with only an ID — refuted because its place and ID say it is the bench specification, which 03 names as its technical document (from logistics).
- `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount`: 500.00 against the advertised value — refuted by money (pairs with `AdvertisementAmount` 320.00 in 21) — the merge cannot settle it and keeps it as F19, Low, Needs decision yes (from money).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount`: 148896.00 against the renewal (124080 + 62040 = 186120) — refuted because the maximum follows the base contract's maximum quantity and the renewal is a separate option (from money).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount`: 119760.00 not adding up to 124080.00 — refuted, the difference 4320.00 is the installation (lot 2) without a goods line (from money).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: the notice's exemption says nothing about the taxes the invoice later shows — refuted because those depend on the supplier's establishment, unknown when the notice is issued (from money).
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason`: transaction wording — refuted by money because the second half states the party's status — the merge disagrees and keeps it as F17 (from money).
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric`: one sub-criterion of 20 in a parent of 40 — refuted by money (the rest is the warranty scored by the parent) — the merge keeps it in F25 because the document does not say so (from money).
- `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate`: 2 rather than 0.02 — refuted, the flow writes percentages as rates the same way and UBL does not fix it (from money).
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: `Room 2.14` belongs in `Room` — refuted, a room where the office takes its mail fits the definition (from parties).
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: functional contact name; address department "Procurement office" vs contact department "Procurement" — refuted, UBL allows a functional name and both wordings name one unit (from parties).
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: `STATE` for a local authority — refuted, it is the level of the tax (state sales tax), not of the party (from parties).
- `/PriorInformationNotice/cac:ReceiverParty`: an information service as receiver — refuted, the notice is sent for publication and the publication service is the receiver (from parties).

## Refuted in the merge
### broad/F18 · Low · Funding programme code without a list
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`
- Why (broad): the agreed rule is that every code has a listID (except party-internal codes); `PARKS-26` has none, so it is not said whose list it is from.
- Condition (broad): the code names its list, or the programme is given as text only.
- Refuted because: the rule itself exempts party-internal codes (CLAUDE.md, Q1), and `PARKS-26` is the department's own programme number, explained by the sibling `FundingProgram` = "Parks renewal programme 2026"; the context and logistics parts refuted it on the same ground. Adding a listID would be possible but is not required.

## Changed in the merge
- broad/F1, context/F1, logistics/F3 → F1: combined; High kept (two parts), logistics' Medium raised, because the date contradicts the term beside it; context's option to remove the "not required" term added.
- broad/F2, context/F3, logistics/F2 → F3: combined; Needs decision set to no (broad said yes) because the preferred option is removal, an encoding change; aligned with merger D.
- logistics/F4 → F4: Medium raised to High: the lot is contradicted by three other examples of the flow, and no change is stated.
- broad/F16, parties/F4 → F6: Low raised to Medium, as the main table of `analysis/review-merge-decisions.md` (public bodies as companies) and mergers B, C, D.
- money/F2 (High), broad/F10 (Low) → F8: set to Medium, because no base is stated (no product can be shown to fail), while the information the rate needs is missing; aligned with merger D.
- money/F3 (Medium), broad/F11, context/F12 (Low) → F9: combined at Medium (code and text state different comparisons; the list has `GE`).
- money/F1 (High), context/F14 (Low) → F10: combined at Medium; broad's refutation carried into Why; aligned with merger D.
- broad/F9 (Low), context/F6 (Medium) → F19: Low with Needs decision yes, because money's refutation (pairing with `AdvertisementAmount` 320.00) cannot be dismissed.
- context/F18 (yes), parties/F5 (no) → F18: Needs decision no, because the preferred option (drop repetitions) does not change the story; context's story question kept as option (b).
- broad/F15, money/F7, context/F21 → F22: combined into one finding on what the notice does not announce; context's Needs decision yes set to no, because option (a) only adds a sentence; context's broader question (reduce the PIN) kept as option (b) and under Outside this review.
- broad/F13, context/F10 → F24: grouped (four indicators).
- broad/F14, context/F16 → F25: combined; money's refutation of the weight part noted.
- broad/F19, logistics/F6 → F15; context/F20, parties/F2 → F16; broad/F17, parties/F3 → F17; broad/F5, context/F5 → F7; broad/F6, context/F7, money/F4 → F11; broad/F8, context/F8 → F12; broad/F12, context/F13 → F21; broad/F7, context/F9, logistics/F5, parties/F1 → F5: combined, wording merged, severity unchanged.

## Outside this review
- Whether a prior information notice should carry the complete tendering terms of the later call (envelopes, encryption, guarantee constitution date, committee, penalty, budget line) is a question of the flow's story; the same block is repeated in 02, 03 and 24 (from broad, money, context F21).
- The invoice of the first release applies the supplier's standard terms (2 % settlement discount, 8 % penalty interest) rather than "30 days after each accepted release"; that lies in 32 (from money).
