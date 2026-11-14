# LLM review: 01-PriorInformationNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/01#F1 · High · A latest date for security clearance although no clearance is required
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: LatestSecurityClearanceDate is "The end date until which the candidates can obtain the necessary level of security clearance." The same tendering terms say that no clearance is required, because parks are public places. A date by which a clearance that is not required must be obtained contradicts that statement, and it has no business reason (CLAUDE.md: no fillers). The same pair occurs in 02-ContractNotice.xml, 03-CallForTenders.xml and 24-TenderContract.xml (grep for `LatestSecurityClearanceDate` over `world/examples/*/*.xml`: these 4 files).
- Condition: the tendering terms do not carry both a latest security clearance date and a statement that no clearance is required.
- Options: (a) remove LatestSecurityClearanceDate (preferred: a bench supply needs no clearance); (b) make a clearance required and say for what.
- Needs decision: no

### tender/01#F2 · High · The notice says it replaces a prior information notice that does not exist
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/PriorInformationNotice/cbc:VersionID` = `1`
- XPath: `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`
- Why: ReplacedNoticeDocumentReference is "A class defining a reference to the notice that is being replaced." This is version 1 of the first notice of the procedure; nothing was published before it that it could replace, and no document of the flow has the ID `PWD-2026-PARKS-PIN` (its name suggests it is this notice itself, whose ID is `LPWD-DOC-26-0187`). The same reference is repeated in 02, 03 and 24, where it could at best mean "the contract notice replaces the prior information notice", but there too the ID is not the ID of this notice.
- Condition: the notice names a replaced notice only if an earlier notice was replaced, and then by that notice's ID.
- Options: (a) remove the reference here (preferred); (b) add an earlier, withdrawn notice to the story.
- Needs decision: yes

### tender/01#F3 · High · Reference to a call for tenders under an ID no document carries
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: "A reference to a Call for Tender associated with these tendering terms." The call for tenders of this procedure is 03-CallForTenders.xml, whose ID is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`, issued a month after this notice. No document has the ID `PWD-2026-PARKS-CFT`, and at the time of the prior information notice the call for tenders did not exist yet. 25-Catalogue.xml refers to the call for tenders as `LPWD-DOC-26-0189`, so the flow uses two IDs for one document.
- Condition: every reference to the call for tenders uses the ID of 03-CallForTenders.xml, and a document issued before the call for tenders does not refer to it.
- Options: (a) remove the reference from the prior information notice (preferred); (b) keep one ID for the call for tenders throughout the flow.
- Needs decision: no

### tender/01#F4 · High · Lot 2 is works here and a service in the contract notice
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- Why: The same lot `LOT-2` of the same procedure is classified as works here and as services (sub-type INSTALL, CPC 87390 installation services) in 02, 03 and 21, and its name differs. The nature of a lot (works or services) decides thresholds and rules and does not change between the advance notice and the notice.
- Condition: lot 2 has the same name and the same procurement type in every document of the flow.
- Options: (a) services and "Installation of the benches" here as well (preferred: three documents say so); (b) works everywhere.
- Needs decision: no

### tender/01#F5 · Medium · Variants limited to one, but the indicator says their number is unconstrained
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- Why: VariantConstraintIndicator is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)." MaximumVariantQuantity ("Maximum number of variants the tenderer is allowed to present") limits them to one. By the definition, `true` says the number is unconstrained; neither value of the indicator describes "allowed, at most one".
- Condition: the indicator and the maximum do not contradict each other.
- Options: (a) drop the indicator and keep VariantConstraintCode `ALLOWED` with the maximum (preferred); (b) drop the maximum.
- Needs decision: no

### tender/01#F6 · Medium · Fee for paper copies in the element for the reimbursement fee of concessions
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: RequiredFeeAmount is "The amount of the reimbursement fee for concession procurement projects" and FeeDescription "Text describing the reimbursement fee for concession procurement projects." This is a supply contract, not a concession, and the 50 lume are the price of paper copies of the documents, which DocumentationFeeAmount ("The amount to be paid to obtain the contract documents and additional documentation") already states.
- Condition: no concession fee is stated for a procurement that is not a concession; the documentation fee is stated once, in DocumentationFeeAmount.
- Options: (a) remove RequiredFeeAmount and FeeDescription and, if wanted, move the explanation to a note of the tendering terms (preferred); (b) none other seen.
- Needs decision: no

### tender/01#F7 · Medium · Language code in LocaleCode
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` is the language again (already in `cbc:ID`), not a locale (a language as used in a place, e.g. English as used in Bayvarra). The value adds nothing and carries another meaning than the element's. The same value sits in every fully described party of the flow.
- Condition: LocaleCode, where present, identifies a locale, from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/01#F8 · Medium · A strategic-procurement code in ProcurementTypeCode
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- Why: ProcurementTypeCode is "A code signifying the type of procurement project (e.g., goods, works, services)", and ProcurementAdditionalType "An association to additional procurement type." `GREEN` (list StrategicProcurementCode, "Environmental impact") is not a type of procurement in that sense but a policy goal. eForms uses the element this way (strategic procurement); by the repository's rule on semantic conformance that practice does not change the UBL meaning. My own knowledge of eForms is the source for that remark.
- Condition: ProcurementAdditionalType carries a type of procurement (goods, works, services), or the green-procurement statement is carried elsewhere.
- Options: (a) state the additional type that really applies (the project also contains works: `/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`) and carry the environmental aim in the execution requirement that is already there (preferred); (b) keep it and record it as a finding on eForms practice.
- Needs decision: yes

### tender/01#F9 · Low · Maximum advertised value of 500 lume against an estimate of 124 080
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: MaximumAdvertisementAmount is "The maximum advertised monetary value of the tendering process." Read by that definition, 500 lume contradicts the estimate of 124 080 and the maximum of 148 896. The value looks like the maximum cost of publishing the notices that the successful tenderer has to bear (the meaning the element has in the Spanish CODICE model it comes from; my own knowledge), which the UBL definition does not say. Nothing in the notice explains the 500.
- Condition: the amount fits the definition (the advertised value of the process), or the element is absent.
- Options: (a) remove it (preferred, no business reason is visible); (b) keep it as advertising cost with a note, and record the unclear UBL definition as a finding.
- Needs decision: yes

### tender/01#F10 · Low · Guarantee of 2 400 is not 2 % of any stated amount
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: AmountRate is "The rate used to calculate the amount of liability in this financial guarantee." 2 % of the estimated contract amount 124 080.00 is 2 481.60; of the bench line 119 760.00 it is 2 395.20; 2 400.00 is 2 % of 120 000, an amount the notice does not state. The amount is probably rounded, but neither base nor rounding is said.
- Condition: rate × base = liability amount for a base the notice states, or the description says the amount is rounded and from what.
- Options: (a) say in the description what the 2 % is taken of and that it is rounded (preferred); (b) set the amount to the calculated value.
- Needs decision: no

### tender/01#F11 · Low · "At least twice" coded as "greater than"
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: "At least" is ≥; `GT` ("Greater than") and "Turnover > 2 × estimate" exclude a turnover of exactly the threshold. Also 2 × 124 080.00 = 248 160.00, while `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00` (rounded up, not said).
- Condition: description, expression code and expression state the same comparison.
- Options: (a) use a "greater than or equal" code and expression if the list has one (preferred); (b) change the description to "more than".
- Needs decision: no

### tender/01#F12 · Low · The tenderer is required to lead a consortium
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads a consortium.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: Within a TendererQualificationRequest ("Required set of qualifications for a tenderer") the EconomicOperatorRole ("A class to describe the tenderer contracting role") states the role the qualification set applies to. As written, the whole set (three years of operation, ten employees, turnover, references) applies to consortium leads only, while the legal form says any form may tender and the tenderers of the flow (Valdara Industries, Brackenmere Furniture) tender alone.
- Condition: the role of the qualification request matches who must meet it (a sole tenderer as well as a consortium lead), or the role is absent.
- Options: (a) remove the role (preferred); (b) use a role that covers sole tenderers and lead members.
- Needs decision: no

### tender/01#F13 · Low · Contest indicators in a supply procedure
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- Why: FollowupContractIndicator "Indicates if any service contract following the contest will be awarded to the winner or one of the winners of the contest", and PrizeIndicator whether a prize will be awarded. Both belong to design contests; this is an open procedure for supplies. Stating `false` for something that cannot apply is a filler (CLAUDE.md: no fillers, nothing implied by absence).
- Condition: indicators that only make sense for a design contest are absent from this procedure.
- Options: (a) remove both (preferred); (b) none other seen.
- Needs decision: no

### tender/01#F14 · Low · Quality criterion with a range of 5 to 10 years and no explanation
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- Why: The criterion "Quality" has a minimum and a maximum quantity in years, but no description and no calculation expression; its only sub-criterion is "Durability of the coating" (weight 20 of 40; the other 20 are not described). A reader cannot tell what the years measure (probably the warranty offered, as the required warranty is 5 years).
- Condition: the criterion says what quantity is scored between 5 and 10 years, and its sub-criteria account for its weight.
- Options: (a) add a description ("warranty offered, 5 to 10 years") and the missing sub-criterion (preferred); (b) remove the quantities.
- Needs decision: no

### tender/01#F15 · Low · Framework amounts in a notice that does not announce a framework agreement
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallFrameworkContractsAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:AverageSubsequentContractAmount` = `20680.00`
- XPath: `/PriorInformationNotice/cac:TenderingProcess/cbc:Description` = `Planned as an open procedure in two lots.`
- Why: EstimatedOverallFrameworkContractsAmount is "The estimated overall monetary amount of subsequent framework contracts" and AverageSubsequentContractAmount "The average monetary amount for the subsequent contracts following this budget amount." They presuppose a framework agreement with call-offs. The tendering process of this notice says nothing of a framework agreement (02 and 03 do, in `cac:TenderingProcess/cac:FrameworkAgreement`); only "Two years of releases" hints at it. 124 080 / 6 = 20 680, so six releases are assumed, which the notice does not say either.
- Condition: a notice that states framework amounts also says that a framework agreement is planned.
- Options: (a) say in the tendering process that a framework agreement with releases is planned (preferred); (b) remove the two amounts from the prior information notice.
- Needs decision: no

### tender/01#F16 · Low · A city department described as a company in a commercial register
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: A department of a city is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The receiver, Bayvarra Information Service, is classified `8411` (general public administration) and is described the same way. The same description of the department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: a public body carries no liquidation status, and its registration scheme is described as what it is (a register of public bodies, or the business register with a type that fits).
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/01#F17 · Low · The department's tax exemption reason describes a sale
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction (and used as such in `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`); the party's own status is "is a public body".
- Condition: the party's exemption reason states the party's status; the transaction's reason stays on the tax category.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

### tender/01#F18 · Low · Funding programme code without a list
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`
- Why: The agreed rule is that every code has a listID (except party-internal codes). `PARKS-26` has none, so it is not said whose list it is from (the city's programmes, presumably).
- Condition: the code names its list, or the programme is given as text only.
- Options: (a) add the city's list of programmes as listID (preferred); (b) keep only `cbc:FundingProgram`.
- Needs decision: no

### tender/01#F19 · Low · Document reference without any indication of what it is
- XPath: `/PriorInformationNotice/cac:DocumentReference/cbc:ID` = `PWD-PARKS-PLAN-26`
- Why: The reference has only an ID; no type, description or date says what the document is (the department's parks plan, presumably) or why the notice refers to it. The ID occurs in no other example (grep over `world/examples/*/*.xml`).
- Condition: the reference says what kind of document it points to.
- Options: (a) add DocumentType or DocumentDescription (preferred); (b) remove the reference.
- Needs decision: no

## Checked and consistent
- check_ids.py: no check-digit identifiers reported as wrong.
- Line amounts: 240 × 499 = 119 760.00 (EstimatedAmount); 240 anchor sets × 18 = 4 320.00 = AllowedSubcontractTerms/Amount; 119 760 + 4 320 = 124 080.00 = EstimatedOverallContractAmount = BudgetAccountLine/TotalAmount. MinimumAmount 62 040.00 = half; MaximumAmount 148 896.00 = 1.2 × 124 080; MaximumQuantity 288 = 1.2 × 240; MinimumQuantity 120 = half. Renewal amount 62 040.00 = 120 benches × 517 (= 124 080 / 240).
- Dates: planned period starts 2026-03-23; lead time 10 days gives 2026-04-02 = RequestedDeliveryDate = start of the delivery period; end 2028-03-22 = two years.
- Award criteria weights 60 + 40 = 100; warranty 5 years in the terms and on the line.
- OID `2.16.840.1.101.3.4.1.46` is AES-256-GCM (own knowledge), matching the algorithm ID.
- CPC 38111 "Seats, primarily with metal frames" and ISIC 3100 "Manufacture of furniture" fit the benches; ISIC 8411 fits the department.
- NoticeDocumentReference in 02-ContractNotice.xml and 03-CallForTenders.xml point back to this notice's ID `LPWD-DOC-26-0187`.

## Considered and refuted
- `/PriorInformationNotice/cbc:PlannedDate`: planned publication of the contract notice 2026-01-26, while 02-ContractNotice.xml was issued 2026-02-11 — refuted because a planned date is a plan; a slip does not make the notice wrong.
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid`: mentions an electronic auction that this notice does not otherwise announce — refuted as a finding of its own because 02 and 03 define the auction (`cac:TenderingProcess/cac:AuctionTerms`) and the element is defined for auctions; the prior information notice need not carry the auction terms.
- `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate`: `Rate` ("The precise percentage allowed to be subcontracted") and `MaximumPercent` both 30, with an amount of 4 320 (3.5 % of the estimate) — refuted because the amount is the estimate of the installation that may be subcontracted and lies under the maximum; the repetition of 30 is redundant but not contradictory.
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` is not written as an ISO 8601 offset — refuted because the element is text ("as an offset from … UTC") and the world's time zone is fictional.
- `/PriorInformationNotice/cac:OriginatorCustomerParty`: originator, beneficiary and the six parties of the tendering terms are all the department itself — refuted because each role's definition is met by the department and a notice may name them.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumQuantity`: 288 is less than 240 plus the extension of 120 — refuted because the maximum is the tolerance of the base contract and the extension is a separate option.
- `/PriorInformationNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID`: `OPEN-1` identifies an opening event the notice does not describe — refuted because 02 and 03 describe the opening event; an identifier alone is acceptable here.
- `/PriorInformationNotice/cac:AdditionalNoticeLanguage/cbc:ID`: Urvanian as additional language of a Bayvarran notice — refuted because tenderers from Urvania (Valdara Industries) take part under the Trade Accord.

## Outside this review
- Whether a prior information notice should already carry the complete tendering terms (envelopes, encryption, committee, penalty) is a question of the flow's story; the same block is repeated in 02, 03 and 24.
