# LLM review: 03-ContractNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/03-ContractNotice.xml`, Git blob `7954b4a6494a5104f6b223a28caf36da90fc85ff` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 690a166 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### contest/03#F1 · Medium · LocaleCode carries a language code
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines Language/LocaleCode as "A code signifying the locale in which this language is used", and Language/ID as "An identifier for this language". Every party here gives `en` with listID `ISO 639` in both: the locale element repeats the language code instead of naming a locale (a language in a region, such as en-XB). A language code is a valid code, but not the one the definition names. The same pattern (`<cbc:LocaleCode listID="ISO 639">`) occurs in 213 example files, 362 times (counted with `grep -c` over `world/examples/*/*.xml`).
- Condition: Every LocaleCode either names a locale (language and country/region) from a locale scheme, or is absent.
- Options: Preferred: drop LocaleCode where the party has no locale to state beyond its language (Language/ID already says English). Alternative: a locale code such as `en-XB` with a locale listID (e.g. BCP 47).
- Needs decision: no

### contest/03#F2 · Medium · NoticeTypeCode `CN` is the standard-procedure type, not a design-contest notice
- XPath: `/ContractNotice/cbc:NoticeTypeCode` = `CN`
- Why: The procedure is a design contest (ProcedureCode `DESIGNCONTEST`). In the world's NoticeTypeCode list `CN` is described as "Contract notice … Calls for competition (eForms cn-standard)"; the list has no notice type for a design contest, while the eForms list it cites distinguishes them (cn-standard for a standard procedure, cn-desg for a design contest). The UBL definition of ContractAwardNotice/NoticeTypeCode itself names the distinction: "The type of notice (CAN general, CAN social, Design)". So the code exists but is not the one this situation calls for.
- Condition: The notice type code of this notice identifies a design-contest notice.
- Options: Preferred: add design-contest notice types to the NoticeTypeCode list (as eForms cn-desg / can-desg) and use them here. Alternative: keep `CN`/`CAN` but change the list's description so that it covers design contests.
- Needs decision: yes

### contest/03#F3 · Low · Tax and customs identity copied into a document that does nothing with them
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: ContractNotice carries no amount that is taxed, no tax total and no customs procedure, yet the parties bring their state sales tax registration (PartyTaxScheme, with TaxScheme `STT`) and their customs trader number (AdditionalPartyIdentification, scheme `customs-trader`). Section 4.8 of the review rules: data copied from a party's master data into a document that does not use it. For the contracting authority the tax scheme also states ExemptionReasonCode `PUBLIC`, whose meaning in the list is "Sale to a public body"; PartyTaxScheme/ExemptionReasonCode is "A reason for the party's exemption from tax", so even where the scheme is kept, the reason should be the party's own status, not a kind of sale.
- Condition: The parties of this document carry no tax scheme and no customs trader number, unless something in the document uses them; where a PartyTaxScheme of a public body is kept, its exemption reason names the party's status.
- Options: Preferred: leave PartyTaxScheme and the customs trader identifier out of the notices and qualification documents, as the Bayvarra Information Service is described throughout the flow. Alternative: keep them only where a tax or customs check is part of the step, and say so in the document.
- Needs decision: no

### contest/03#F4 · Low · Public bodies described as companies in the commercial register, with a liquidation status
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The public bodies of this document (ISIC 84xx: Lumeport Public Works Department, "a department of the city of Lumeport", Bayvarra Information Service, Procurement Review Board of Bayvarra) are registered in a CorporateRegistrationScheme of type `COMMERCIAL` ("Commercial register") and carry CompanyLiquidationStatusCode `ACTIVE` ("Active, not in liquidation"). A city department or a state authority is not a company in a commercial register and cannot be liquidated, so "the party's liquidation status" has no meaning for it (review checklist, party legal entity).
- Condition: No public body in this document has a liquidation status, and its registration scheme, if stated, is not a commercial register.
- Options: Preferred: no CompanyLiquidationStatusCode for public bodies, and a registration scheme of a type for public bodies (or none). Alternative: keep the federal register but with a type code that says it registers public bodies.
- Needs decision: no

### contest/03#F5 · Low · Requested legal form applies only to the follow-up contract, not to the contest participants
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Limited company (private): a group of participants forms one before the follow-u…`
- Why: TendererQualificationRequest/CompanyLegalFormCode: "The legal status requested for potential tenderers". The code `LTD` states that tenderers must be private limited companies, but the text next to it says that for the contest itself a group only names a lead member, and that the company is formed before the follow-up contract. For the participants this document addresses, no legal form is requested; the code and its text describe different moments.
- Condition: What the code requests and what the text says apply to the same tenderers at the same step.
- Options: Preferred: keep the code only if participants must already be (or form) a limited company; otherwise state the requirement for the follow-up contract in text only (e.g. in the description of the follow-up negotiation). Alternative: keep both and rephrase the text so that it states a requirement on groups at the time of the contest.
- Needs decision: no

### contest/03#F6 · Low · DurationPeriod of the reference criterion is the look-back window, not the criterion's validity
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Two completed designs of furniture or fittings for public spaces in the last five years.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cac:DurationPeriod/cbc:DurationMeasure` = `5`
- Why: EvaluationCriterion/DurationPeriod: "Describes the period for which the evaluation criterion is valid." The 5 years here are the window in which the two reference designs must have been completed ("in the last five years"), not a period during which the criterion applies. A legitimate value, but in an element whose definition means something else.
- Condition: The five-year window is stated where it means a reference window (the Description already does), and DurationPeriod, if kept, gives the period for which the criterion is valid.
- Options: Preferred: keep the window in the Description and drop DurationPeriod. Alternative: keep it and record the reading as a note on the UBL definition.
- Needs decision: no

### contest/03#F7 · Low · Review board registry described as a procurement officer
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: The appeal receiver is the Procurement Review Board; its contact is its "Registry", which receives appeals. Job title `Procurement officer` and department `Procurement` describe a buyer's staff, not the registry of a review body that decides on appeals against buyers.
- Condition: The review board's contact has a job title and department that fit a registry of appeals.
- Options: Preferred: a registry clerk or registrar in the registry. Alternative: name only the registry and its channels.
- Needs decision: no

### contest/03#F8 · Low · CandidateReductionConstraintIndicator says the candidates have already been reduced
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`
- Why: UBL: "An indicator that the number of candidates participating in this process has been reduced (true) or not (false)." This document is issued before the requests to participate are due, so no candidate has been selected or dropped yet; what it announces is that the number will be limited (the short list of three to five). Read by its definition, `true` states something that has not happened.
- Condition: The indicator either is absent here (the short list already carries the planned limitation) or its meaning in the world is documented as "will be reduced".
- Options: Preferred: leave it out of the notice and the call; the EconomicOperatorShortList already states the limitation. Alternative: keep it and record the reading as a finding about the UBL definition.
- Needs decision: no

## Checked and consistent
- Prize amounts: Prize[1] = `8000.00`, Prize[2] = 4000.00, Prize[3] = 2000.00 lume, matching the PrizeDescription ("the first is 8,000 lume") and version 2 of the PIN.
- The short list (minimum 3, expected and maximum 5) agrees with the process description ("three to five selected participants") and with `02-PriorInformationNotice.xml`.
- Dates: requests to participate due before designs (participation `2026-04-18`, designs 2026-06-12 12:00), both after the issue date.
- ProcessJustification: PreviousCancellationReasonCode `UNSUITABLE` ("No suitable tender") agrees with its text (both designs of the cancelled contest were unacceptable).
- The appeal terms name a receiver of appeals (the review board) and a time limit; the AppealTerms aggregate fits.

## Considered and refuted
- `/ContractNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: suspected that an aggregate defined as "The type of represention empowering the party to act on behalf of a third party" does not belong to a party acting for itself — refuted because the world's list offers `OWN` and `BEHALF` as the two answers, and stating `OWN` explicitly avoids implying it by absence (IND6).
- `/ContractNotice/cac:TenderingProcess/cac:ProcessJustification/cbc:Description` = `Relaunch of the design contest PWD-2025-PROM-DC…`: suspected that a justification "for the selection of this tendering process" should explain the choice of a design contest rather than the relaunch — refuted: the aggregate also carries the reason a previous process was cancelled (PreviousCancellationReasonCode), and the text explains why the same procedure is run again.
- `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `true` and `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`: checked whether the indicators agree with their text — they do: the first prize says its author "is invited to negotiate the follow-up service contract", and nothing in the text makes the jury's ranking advisory.
- `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`: whether a role belongs in a qualification request — refuted: the notice asks a group to name a lead member, which is what the role states.
- `/ContractNotice/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`: suspected a wrong receiver for a notice of a city department — refuted because a notice goes to the publication office, and the Information Service is that office (its contact is "Publications and register").
