# LLM review: 01-PriorInformationNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/01#F1 · High · A latest date for obtaining security clearance, although no clearance is required
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "the end date until which the candidates can obtain the necessary level of security clearance". The same tendering terms say, in `SecurityClearanceTerm`, that no clearance is required ("Parks are public places."). There is no "necessary level" to obtain, so the date has nothing to refer to and contradicts the term. The term itself only states what its absence would say (CLAUDE.md: nothing implied by absence).
- Condition: The tendering terms do not carry a latest clearance date while they say that no clearance is required; a security clearance term is present only if a clearance is in fact asked.
- Options: (a) Preferred: remove the date and the "not required" term, since nothing in the world asks for a clearance for park benches. (b) Give the procedure a real clearance requirement (e.g. for work in a guarded site) and keep both.
- Needs decision: no

### tender/01#F2 · High · Reference to a call for tenders that no example carries
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersDocumentReference` is "a reference to a Call for Tender associated with these tendering terms". No example of the flow has the document ID `PWD-2026-PARKS-CFT`: the call for tenders is `03-CallForTenders.xml` with the ID `LPWD-DOC-26-0189`, and the catalogue of the flow refers to it by that ID. In addition, this notice is issued on 2026-01-12, a month before the call for tenders (2026-02-12, approved 2026-01-25): the prior information notice refers to a document that did not exist when it was issued. The same ID is used in 8 examples of the flow (01, 02, 03, 06, 15, 17, 19, 24; `grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml` lists these 8 files).
- Condition: Every reference to the call for tenders of this procedure resolves to the ID of `03-CallForTenders.xml`; a notice issued before the call for tenders exists does not refer to it.
- Options: (a) Preferred: remove the reference from the prior information notice. (b) Keep it only if the story says the documents were already registered under that number, and then use the same number as the ID of 03.
- Needs decision: no

### tender/01#F3 · High · A replaced notice is named, but this is the first version of the first notice
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/PriorInformationNotice/cbc:VersionID` = `1`
- XPath: `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `ReplacedNoticeDocumentReference` is "a reference to the notice that is being replaced". This is version 1 of the prior information notice, the first notice of the procedure; nothing is replaced. The ID named, `PWD-2026-PARKS-PIN`, looks like a name for this very notice (whose ID is `LPWD-DOC-26-0187`) and is carried by no example. The same reference occurs in 4 examples (01, 02, 03, 24; `grep -l PWD-2026-PARKS-PIN world/examples/tender/*.xml`).
- Condition: `ReplacedNoticeDocumentReference` is present only in a notice that replaces an earlier notice, and then carries that notice's document ID.
- Options: (a) Preferred: remove it. (b) If the flow should show a corrected notice, add that notice and let it, and only it, carry the reference.
- Needs decision: no

### tender/01#F4 · High · Lot 2 is "works" in the prior information notice and "services" in the contract notice and the call for tenders
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = `INSTALL`
- Why: The same lot of the same procedure is described with two different contract natures: `WORKS` in `01-PriorInformationNotice.xml`, `SERVICES` (sub-type `INSTALL`, CPC 87390 "Installation services of other goods n.e.c.") in `02-ContractNotice.xml` and `03-CallForTenders.xml`. The name differs as well. The nature of a lot decides which rules and thresholds apply; nothing in the later documents says that it was changed.
- Condition: Lot 2 has the same `ProcurementTypeCode` and the same name in every example that describes it.
- Options: (a) Preferred: `SERVICES` everywhere (anchoring delivered benches is an installation service, as the CPC code of 02 and 03 says). (b) `WORKS` everywhere, with a matching classification. (c) Keep the change and state it in the contract notice as a change against the prior information.
- Needs decision: no

### tender/01#F5 · Medium · Variants are flagged as unconstrained in number, with a maximum of one
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:VariantConstraintCode` = `ALLOWED`
- Why: `VariantConstraintIndicator` is "an indicator that variants are allowed and unconstrained in number (true) or not allowed (false)". `MaximumVariantQuantity` limits the tenderer to one variant, so variants are allowed but constrained in number; the value `true` asserts the opposite of the limit next to it. The indicator has no value for "allowed with a limit"; the code `ALLOWED` and the quantity already say it.
- Condition: The indicator is not `true` while a maximum number of variants is given.
- Options: (a) Preferred: leave the indicator out and keep `VariantConstraintCode` and `MaximumVariantQuantity`. (b) Drop the maximum and keep `true`, if the buyer really accepts any number of variants.
- Needs decision: no

### tender/01#F6 · Medium · `MaximumAdvertisementAmount` of 500 lume is not the maximum advertised value of the procedure
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- Why: The definition is "the maximum advertised monetary value of the tendering process". The procedure is advertised with an estimate of 124080.00 and a maximum of 148896.00 lume; 500.00 is neither. The value reads like a cap on advertising costs to be reimbursed by the awardee (the Spanish practice the element comes from, from my knowledge of CODICE), which is not what the UBL definition says, and nothing else in the document explains a cost of 500 lume.
- Condition: The amount is the maximum value at which the procedure is advertised, or the element is absent.
- Options: (a) Preferred: remove it (the maximum is already in `RequestedTenderTotal/MaximumAmount`). (b) Set it to the advertised maximum. (c) If advertising costs charged to the awardee are part of the story, state them in a clause or note and record the unclear UBL definition as a finding for the TC.
- Needs decision: yes

### tender/01#F7 · Medium · The reimbursement fee of concession projects is used for the price of paper copies
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: `RequiredFeeAmount` is "the amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "text describing the reimbursement fee for concession procurement projects". This is a purchase of supplies under a framework, not a concession, and the text describes the price of paper copies of the documents. That price has its own element, `TenderingTerms/DocumentationFeeAmount` ("the amount to be paid to obtain the contract documents and additional documentation"), which already carries the same 50.00 lume.
- Condition: `RequiredFeeAmount` and `FeeDescription` are absent from a project that is not a concession; the price of paper copies is stated once, in `DocumentationFeeAmount` (its explanation in a note of the tendering terms).
- Options: (a) Preferred: remove both elements and move the sentence to a `TenderingTerms/Note`. (b) None other seen: the definition leaves no room for a non-concession fee.
- Needs decision: no

### tender/01#F8 · Medium · A strategic-procurement code in the element for an additional contract nature
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- Why: In `ProcurementAdditionalType`, `ProcurementTypeCode` is "a code signifying the type of procurement project (e.g., goods, works, services)" and `ProcurementType` the same as text. `GREEN` ("Environmental impact", from the list StrategicProcurementCode) is not a type of procurement in that sense but a policy objective. eForms uses the aggregate this way (BT-06 strategic procurement, from my knowledge of the eForms SDK); under the repository's rule of semantic conformance that practice does not change the UBL definition. The project does have a real additional nature that is not stated here: lot 2 is installation (services or works) next to the supplies of lot 1.
- Condition: `ProcurementAdditionalType/ProcurementTypeCode` carries a contract nature (supplies, services, works); the environmental objective is stated where UBL has a place for it.
- Options: (a) Preferred: put the additional nature of lot 2 here and state the environmental objective in the elements that already carry it (`ContractExecutionRequirement` with `ENVIRONMENTAL`, `SpecificTendererRequirement`), or in the project note. (b) Keep it as the eForms-compatible encoding and record it as a deliberate difference with a finding for the UBL TC.
- Needs decision: yes

### tender/01#F9 · Medium · A language code in `LocaleCode`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply, e.g. Bayvarra for English as used there). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: `LocaleCode`, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/01#F10 · Low · Design-contest indicators in a supply procedure
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:NoFurtherNegotiationIndicator` = `true`
- XPath: `/PriorInformationNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: `PrizeIndicator` ("whether a prize will be awarded") and `FollowupContractIndicator` ("if any service contract following the contest will be awarded to the winner or one of the winners of the contest") belong to design contests; with `false` they only state what their absence says (nothing implied by absence). `BindingOnBuyerIndicator` ("if the decision is binding on the buyer") is the jury-decision indicator of a contest; here there is no jury decision, the buyer's own committee evaluates. `NoFurtherNegotiationIndicator` ("if no further negotiation is allowed") says something only in a procedure that could have negotiation; in an open procedure it is never allowed.
- Condition: The awarding terms of an open supply procedure carry none of the four indicators, unless the document explains what each refers to.
- Options: (a) Preferred: remove all four. (b) Keep `NoFurtherNegotiationIndicator` if the world's procurement law lets an open procedure be followed by negotiation, and say so.
- Needs decision: no

### tender/01#F11 · Low · Works quality control stated for a supply project
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: `QualityControlCode` is "the indication of whether or not the control quality is included in the works project". The project is `SUPPLIES`; "Inspection on delivery" is an acceptance rule for delivered goods, not quality control included in a works project.
- Condition: `QualityControlCode` is present only for (the part of) a project that is works, with a value that says whether quality control is part of it; the inspection of delivered benches is stated as a delivery or acceptance term.
- Options: (a) Preferred: remove it and state the inspection on delivery in the contract conditions or a note. (b) Keep it only on the installation lot if that lot is works (see the finding on lot 2).
- Needs decision: no

### tender/01#F12 · Low · "At least" in the text, "greater than" in the code
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- Why: The description sets a minimum that is included ("at least twice the estimate"); `ExpressionCode` `GT` and the expression "Turnover > 2 × estimate" exclude the threshold itself. A tenderer with a turnover of exactly the threshold passes by the text and fails by the code. (Twice the estimate of 124080.00 is 248160.00; the threshold is the rounded 250000.00, which the text does not say either.)
- Condition: Description, code and expression state the same comparison against the same amount.
- Options: (a) Preferred: a "greater than or equal" code and "≥", with the description naming 250000 lume. (b) Change the text to "more than".
- Needs decision: no

### tender/01#F13 · Low · The qualification request is given the role "consortium lead"
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads a consortium.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: `EconomicOperatorRole` here is "a class to describe the tenderer contracting role", i.e. the role to which this set of qualifications applies. With `LEAD` the only qualification request of the procedure applies to consortium leads only, although its content (legal form, turnover, references, certified timber) is asked of every tenderer, and the tenders of the flow come from single tenderers. "Leads a consortium." describes a party, not a requirement.
- Condition: The qualification request applies to the tenderers it is meant for: no role when it applies to every tenderer, or one request per role with the requirements of that role.
- Options: (a) Preferred: remove the role. (b) Add what is specific to a lead (e.g. joint liability) in a second request with that role.
- Needs decision: no

### tender/01#F14 · Low · Subcontract terms: a "precise" share equal to the maximum, an amount that is not that share, and a price flagged as known
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:UnknownPriceIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Description` = `Installation may be subcontracted.`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted", `MaximumPercent` "the maximum percentage allowed to be subcontracted": the buyer sets a ceiling, so only the maximum has a reason; a precise share is what a tenderer states. `Amount` ("the monetary amount assigned to the subcontracted task") is 4320.00, the estimate of the installation lot, which is 3.5 % of the estimate of 124080.00 (4320 / 124080), not 30 %; the terms do not say which of the two limits holds. `UnknownPriceIndicator` `false` says the subcontract price is known, which a buyer cannot say before tenders exist; it states what absence would imply.
- Condition: The buyer's subcontract terms state one limit (a maximum share, or the task that may be subcontracted with its estimated amount), and no statement about a subcontract price that does not exist yet.
- Options: (a) Preferred: keep `MaximumPercent`, `SubcontractingConditionsCode` and `Description`; remove `Rate`, `Amount` and `UnknownPriceIndicator`. (b) Keep `Amount` as the estimate of the installation and explain it in the description.
- Needs decision: no

### tender/01#F15 · Low · The tender envelope is tied to lot 1 only
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:Description` = `One encrypted envelope per tender.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cac:DocumentTenderRequirement/cbc:Description` = `Unit prices per lot.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric` = `2`
- Why: The only `TenderPreparation` names lot 1 as the lot it applies to, while its texts speak of "one encrypted envelope per tender" and "unit prices per lot" and a tenderer may tender for both lots. Nothing says how a tender for lot 2 is prepared.
- Condition: The tender preparation covers every lot a tender can be submitted for (no lot named, both lots named, or one preparation per lot).
- Options: (a) Preferred: remove the lot from the preparation, since the envelope rule is the same for both. (b) Name both lots.
- Needs decision: no

### tender/01#F16 · Low · Quality criterion: a range in years without explanation, and one sub-criterion of half the weight
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:WeightNumeric` = `40`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:Name` = `Durability of the coating`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- Why: `MinimumQuantity` and `MaximumQuantity` are "the minimum/maximum quantity for an awarding criterion". The criterion "Quality" has no description and does not say what is counted in years from 5 to 10; presumably the warranty offered (the required warranty is 5 years), but then the range belongs to a warranty criterion, not to "Quality" as a whole. Its only sub-criterion, "Durability of the coating", weighs 20 of the 40 points; the other 20 are not assigned.
- Condition: The quality criterion says what its quantity range measures, and its sub-criteria add up to its weight.
- Options: (a) Preferred: two sub-criteria (coating durability 20, warranty years 20, the latter with the 5–10 year range) and a description. (b) Remove the range and the single sub-criterion.
- Needs decision: no

### tender/01#F17 · Low · The additional classification is the parent group of the main one, and the installation is not classified at project level
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `38111`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- Why: `AdditionalCommodityClassification` is "an association to additional classification categories for the deliverable requested". CPC 381 "Furniture" is the group that contains the main class 38111 "Seats, primarily with metal frames"; it adds no further category. The second deliverable of the project, the installation (lot 2), is not classified at project level (the later notices classify lot 2 as CPC 87390).
- Condition: Additional classifications name categories the main one does not already imply; a project with a supply lot and an installation lot shows both.
- Options: (a) Preferred: 87390 as the additional classification of the project; no "Furniture" on lot 2. (b) Remove the additional classification.
- Needs decision: no

### tender/01#F18 · Low · Eight further roles all filled with the contracting party itself
- XPath: `/PriorInformationNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The contracting party is repeated as originator ("a party who originated the tendering process"), beneficiary, and in six roles of the tendering terms (additional information, document provider, tender recipient, contract responsible, evaluation, qualification request recipient). These roles exist for the case that another body does the task (a central purchasing body, another department as beneficiary, a platform operator). Where the contracting party does everything itself, the repetitions say nothing the `ContractingParty` does not say, and they suggest eight distinct roles in a procedure that has one actor. The parks department that the benches are for ("Head of parks" sits on the committee) would be a real originator or beneficiary, if it is a body of its own.
- Condition: A role party is present where a party other than the contracting party fills the role, or where the receiver needs the role's own contact data (e.g. where tenders are received).
- Options: (a) Preferred: keep `TenderRecipientParty` and `AdditionalInformationParty` if they get their own contact (platform, helpdesk); remove the rest. (b) Keep all as an explicit statement and accept the repetition.
- Needs decision: yes

### tender/01#F19 · Low · Urvanian is declared as a language of the notice, but the notice has no Urvanian text
- XPath: `/PriorInformationNotice/cbc:NoticeLanguageCode` = `en`
- XPath: `/PriorInformationNotice/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- XPath: `/PriorInformationNotice/cac:AdditionalNoticeLanguage/cbc:Name` = `Urvanian`
- Why: `AdditionalNoticeLanguage` is "an additional official language used for this prior information notice". Every text of the notice is given once, in English, and no element carries a `languageID` (0 occurrences in this file). The notice therefore declares a language it is not written in. If the declaration means that a translation is published separately, the element still describes this document.
- Condition: Every language declared for the notice is used in it (texts repeated with `languageID`), or is not declared.
- Options: (a) Preferred: add the Urvanian rendering of the main texts (name, description, lots), which also gives the cross-border publication under the Trade Accord a visible reason. (b) Remove the additional language.
- Needs decision: no

### tender/01#F20 · Low · Customs trader number of the contracting party in a tendering document
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The prior information notice identifies the department also by its customs trader number. Nothing in this document is declared to customs; the number is used only when the benches are imported (31). It looks copied from the party's master data into a document that does not use it.
- Condition: A party carries the identifiers the document uses or that the receiver needs to identify it; no customs number in a procurement notice or call.
- Options: (a) Preferred: leave the customs trader number to the customs and transport documents. (b) Keep it if the world's rule is that every document carries all identifiers of a party; then the rule should be stated.
- Needs decision: no

### tender/01#F21 · Low · A prior information notice with the complete operational terms of the later call
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID` = `OPEN-1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cac:TenderEncryptionData/cbc:MessageFormat` = `CMS`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallFrameworkContractsAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:AverageSubsequentContractAmount` = `20680.00`
- XPath: `/PriorInformationNotice/cac:TenderingProcess/cbc:Description` = `Planned as an open procedure in two lots.`
- XPath: `/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26`
- Why: A prior information notice is "a document used by a contracting party to declare the intention to buy goods, services, or works during a specified period". This one carries the same tendering terms, word for word, as the contract notice and the call for tenders: envelope and encryption certificate, the date by which the tender guarantee must be constituted, penalty clause, committee member, appeal terms. Several of them point to things this notice does not describe: `OpenTenderID` `OPEN-1` identifies an opening event that only 02 and 03 define (`TenderingProcess/OpenTenderEvent`); the minimum bid step speaks of "the electronic auction", and two amounts are amounts "of subsequent framework contracts", while the process description of this notice only says "planned as an open procedure in two lots" and mentions neither an auction nor a framework. A reader of this notice alone cannot tell that a framework with an auction is planned, yet gets the cipher of the envelope.
- Condition: The prior information notice states what is known and useful a month ahead (subject, lots, estimate, planned dates, main conditions), and every detail it carries can be understood from the notice itself: the framework and the auction are stated if amounts and bid steps refer to them, and no identifier points to an event the notice does not contain.
- Options: (a) Preferred: reduce the tendering terms of the notice to the main conditions and say in the process description that a framework with one supplier and an electronic auction are planned. (b) Keep the full terms and add the framework, the auction and the opening event to the notice's `TenderingProcess`.
- Needs decision: yes

## Checked and consistent
- Lots and amounts: the project estimate 124080.00 is the sum of the lot estimates of 02/03 (119760.00 + 4320.00); the request-for-tender line (240 × 499 = 119760.00) and the unit price bounds 350–600 agree with the price criterion's `MinimumAmount`/`MaximumAmount`.
- `WeightingAlgorithmCode` WSUM, description "Price 60 %, quality 40 %" and the criterion weights 60 and 40 agree; `AwardingMethodTypeCode` BESTVALUE fits two weighted criteria.
- `PaymentFrequencyCode` PERRELEASE agrees with the payment terms ("30 days after each accepted release") and with the framework of 02/03 ("Releases every few months").
- `RecurringProcurementIndicator` true, "about four years" and `EstimatedTimingFurtherPublication` 2030 agree with the planned period (to 2028-03-22) plus one extension of a year.
- `PostAwardProcess`: catalogue, order, invoice and payment are indeed electronic in the flow (25, 26, 32, 36).
- `RequiredItemLocationQuantity/LeadTimeMeasure` of 10 days fits the first delivery (order 26 issued 2026-03-23, `RequestedDeliveryDate` 2026-04-02).
- `OtherConditionsIndicator` true has its `AdditionalConditions`; `RequiredCurriculaIndicator` true has its `RequiredCurriculaCode`.
- `ContractExtension`: one renewal of 12 months with 120 benches, renewal amount = half of the estimate; `MaximumNumberNumeric` 1 and `RenewalsIndicator` true agree.

## Considered and refuted
- `/PriorInformationNotice/cac:TenderingTerms/cbc:FundingProgramCode`: a code without `listID` was suspected — refuted for this lens because `PARKS-26` is the department's own programme number (party-internal codes are exempt from the listID rule, CLAUDE.md), and it matches `FundingProgram`.
- `/PriorInformationNotice/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric` and `cbc:MaximumLotsAwardedNumeric` (both 2 of 2 lots): suspected to say nothing — refuted because they are the explicit statement that a tenderer may tender for and win both lots, which `GroupingLots` ("Lots 1 and 2 may be awarded together.") builds on.
- `/PriorInformationNotice/cac:ProcurementProject/cbc:RequestedDeliveryDate` = 2026-04-02 in a two-year project: suspected not to be "the" delivery date — refuted because it is the first release and equals the start of the delivery period of the request-for-tender line.
- `/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = PURCHASE: the definition speaks of "the subcategory of the type of work"; suspected misuse — refuted because purchase (as against lease or rental) is a sub-type of a supply contract and the definition's examples are only examples.
- `/PriorInformationNotice/cac:ProcurementProject/cbc:SMESuitableIndicator` = true against a required turnover of 250000 lume and 10 employees: suspected contradiction — refuted, a firm of that size is still a small enterprise.
- `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:OperatingYearsQuantity` and `cbc:EmployeeQuantity`: the model prints the definition of another element ("Textual description of the legal form …") for both, as for `PriceEvaluationCode`; suspected misuse — refuted, the element names say what they are and the values (3 years, 10 persons) fit; the definitions are an error of the UBL model, not of the example.
- `/PriorInformationNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealInformationParty`: suspected wrong party (the review board "presents the information for the appeal") — refuted, the board that hears appeals is the natural source of information on them.
- `/PriorInformationNotice/cac:TenderingTerms/cac:ContractResponsibleParty`: "the Party who executes the Contract" could mean the contractor — refuted as a wrong party, since in the procurement documents it is the body that concludes and manages the contract; it is kept only in the finding on repeated roles.
- `/PriorInformationNotice/cbc:PlannedDate` = 2026-01-26 against the contract notice issued on 2026-02-11: suspected contradiction — refuted for this example because it is a plan; the contract notice itself asks for publication on 2026-01-27 and opens its periods on 2026-01-26, so the plan was kept and the odd value is the issue date of 02 (reported there).
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` ("when used in an auction"): suspected to have no auction — refuted as such because 02 and 03 define the electronic auction (`TenderingProcess/AuctionTerms`); what remains is that this notice does not say so (finding on the operational terms).
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallFrameworkContractsAmount`: suspected to have no framework — refuted as such because 02 and 03 define the framework agreement; kept in the same finding.

## Outside this review
- The tender guarantee of 2400.00 lume at a rate of 2 % is 2 % of neither estimate (124080.00 → 2481.60; lot 1 119760.00 → 2395.20); this is arithmetic for the money lens and is noted here only so it is not lost.
