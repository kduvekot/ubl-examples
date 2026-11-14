# LLM review: 24-TenderContract.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/24-TenderContract.xml`, Git blob `f51644d96669fd1bea4cfc230ed7d7bb275322e5` (committed)
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

### tender/24#F1 · High · A latest date for security clearance although no clearance is required
- XPath: `/TenderContract/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "The end date until which the candidates can obtain the necessary level of security clearance": it presupposes that a level of clearance is necessary. The security clearance term of the same tendering terms says that none is required, and explains why. One of the two is wrong; and in a contract signed on 2026-03-19 a date of 2026-02-21 for candidates has no use in any case.
- Condition: `LatestSecurityClearanceDate` is present only where the security clearance term requires a clearance.
- Options: (a) preferred: remove the date (here and in the other documents that carry the same terms); (b) none seen, the description rules a requirement out.
- Needs decision: no

### tender/24#F2 · Medium · `VariantConstraintIndicator` true with a maximum of one variant
- XPath: `/TenderContract/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- Why: The indicator is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)". True therefore says that any number of variants may be offered, while `MaximumVariantQuantity` ("Maximum number of variants the tenderer is allowed to present") limits them to one. The definition has no value for "allowed, limited in number"; the sibling `VariantConstraintCode` = `ALLOWED` and the maximum already say what is meant.
- Condition: The indicator is not true when the number of variants is limited; the limit is expressed by `MaximumVariantQuantity` and `VariantConstraintCode`.
- Options: (a) preferred: omit the indicator; (b) remove the maximum if variants are really unlimited.
- Needs decision: no

### tender/24#F3 · Medium · `PublishAwardIndicator` true for a supply contract
- XPath: `/TenderContract/cbc:PublishAwardIndicator` = `true`
- XPath: `/TenderContract/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: The indicator is "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)". True says that this concerns a service contract of such a category; the contract is a framework for the supply of park benches, and the world names no such service categories. The value seems meant as "the award is published", which is not what the element says.
- Condition: The indicator is absent, or false, for a contract that is not a service contract of the categories the definition means.
- Options: (a) preferred: remove it; (b) set it to false.
- Needs decision: no

### tender/24#F4 · Medium · A province in `Region`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/24#F5 · Medium · A language code as locale
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderContract/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/24#F6 · Low · The signed contract carries the instructions for tendering
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cbc:TenderEnvelopeID` = `ENV-1`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cac:TenderEncryptionData/cbc:MessageFormat` = `CMS`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderValidityPeriod/cbc:DurationMeasure` = `90`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:LowTendersDescription` = `Prices 30 % below the average are examined.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderRecipientParty`
- XPath: `/TenderContract/cac:TenderingTerms/cac:QualificationRequestRecipientParty`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderEvaluationParty`
- XPath: `/TenderContract/cac:TenderingTerms/cac:DocumentProviderParty`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AdditionalInformationParty`
- XPath: `/TenderContract/cac:TenderingTerms/cac:ContractualDocumentReference/cbc:ID` = `PWD-CONTRACT-DRAFT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:EstimatedTimingFurtherPublication` = `2030`
- Why: The document is "The framework contract, signed by both parties." (`/TenderContract/cbc:Note`). Its tendering terms are the complete terms of the call for tenders: how to pack and encrypt a tender, the tender guarantee due on 2026-02-26, the fee for the tender documents, the ban on multiple tenders, variants, how long tenders stay valid, the qualification requirements (including the role of a consortium lead, where the contractor is a single company with a subcontractor), the award criteria with the auction's minimum bid and the evaluation committee, who receives tenders and qualification requests, a "document that will become part of the awarded contract" (the draft, in the contract itself), a notice "that is being replaced" and the timing of a next notice. All of this governed the competition, which ended with the award; a contract between the two parties does nothing with it. (Terms that do bind the parties are rightly there: penalty clause, payment terms and frequency, price revision, warranty, execution requirement, allowed subcontracting, legislation, post-award process, budget line, contract responsible party.)
- Condition: The tendering terms of the contract contain only terms that apply between the parties during the contract; the reference to the contract text points to the signed contract, not the draft.
- Options: (a) preferred: reduce the terms to those that bind the parties; (b) keep the full copy if the world's rule is that the contract restates the tender documents, and record that rule.
- Needs decision: yes (how much the contract repeats is a design decision)

### tender/24#F7 · Low · Indicators of a design contest in a supply framework
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- Why: `PrizeIndicator` "Indicates whether a prize will be awarded", `FollowupContractIndicator` "Indicates if any service contract following the contest will be awarded to the winner or one of the winners of the contest" and `BindingOnBuyerIndicator` "Indicates if the decision is binding on the buyer" (the jury's decision) describe a design contest. This is an open procedure for a supply framework with no contest, jury or prize. The two "false" values state something that needs no stating (rule: nothing implied by absence, no fillers), and "binding on the buyer: true" has no decision of a jury to refer to.
- Condition: The three indicators are present only in the documents of a design contest.
- Options: (a) preferred: remove them (here and wherever the same awarding terms are carried); (b) none seen.
- Needs decision: no

### tender/24#F8 · Low · Two names for the same project in one document
- XPath: `/TenderContract/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/TenderContract/cbc:ContractName` = `Park benches for the parks renewal programme`
- Why: The project is named "Park benches for the parks renewal programme" as contract name here and as project name in the notices and the call for tenders (`21-ContractAwardNotice.xml:/ContractAwardNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`). The project name of the contract is a different text, found otherwise only in the procurement status request and status (`08-ProcurementStatusRequest.xml`, `09-ProcurementStatus.xml`; counted with grep over `world/examples/tender/*.xml`: 3 examples). The contract should name its object as the procedure did.
- Condition: The procurement project has the same name in the contract as in the notices and the call for tenders.
- Options: (a) preferred: use "Park benches for the parks renewal programme"; (b) none seen.
- Needs decision: no

### tender/24#F9 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
## Checked and consistent
- `check_ids.py`: ISIN XU0001042501 has a correct check digit.
- The note "signed by both parties" against two signatures, one of the contracting party and one of Valdara Industries.
- `PreviousDocumentReference` `LPWD-DOC-26-0208` is the awarded notification; the tender result is identical to the one in the award notice and the notifications (award `PWD-2026-PARKS-AWARD-1`, 2026-03-09 09:30, both lots, 124080.00, two tenders, subcontract terms 4320.00 / 3.5 %).
- Issue date 2026-03-19 lies in the formalization period 2026-03-19 to 2026-03-22; contract start 2026-03-23, 24 months.
- Economic operator, receiver and winning party are Valdara Industries; the contracting party is the department.
- Post-award process: electronic catalogue, order, invoice and payment are all used later in the flow (`25-Catalogue.xml`, `26-Order.xml`, `32-Invoice.xml`, `36-RemittanceAdvice.xml`).
- Tender guarantee 2 % of the estimate: 2 % × 124080.00 = 2481.60, stated as 2400.00 (2 % of 120000); noted, not judged (money lens).
- Subcontracting: the winner subcontracts 3.5 %, within the allowed 30 %.

## Considered and refuted
- `/TenderContract/cac:TenderResult/cbc:ReceivedTenderQuantity` (and the lowest/highest tender and advertisement amounts): award statistics in a contract — refuted because the UBL definition of the document is "A document published by a Contracting Party to announce the awarding of a procurement project" and the tender result is mandatory in it.
- `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:ServiceProviderParty`: the logistics provider and the share and listing data of the contractor looked like unused master data — refuted here because the contract is where the contractor is identified in full, and Castrano Logistics despatches the goods under it (`29-DespatchAdvice.xml`).
- `/TenderContract/cac:ReceiverParty`: repeats the economic operator — refuted because the document is sent to it for signature and filing.
- `/TenderContract/cac:TenderingTerms/cac:ContractAcceptancePeriod`: a period for accepting the contract in the contract — refuted as a term between the parties.
- `/TenderContract/cac:TenderingTerms/cac:WarrantyValidityPeriod`: 5 years although the tender offered 10 years on the coating — refuted because 5 years is the required general warranty and the 10 years are in the tender result's description.
- `/TenderContract/cac:TenderingProcess`: only identifier and procedure code — refuted, that is all the contract needs of it.

## Outside this review
- `/TenderContract/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` has no listID; codes against lists are the logistics part's lens.
- `/TenderContract/cac:ContractDocumentReference/cbc:ID` = `PWD-CONTRACT-2026-PARKS` and `/TenderContract/cac:TenderResult/cac:Contract/cbc:ID` = `PWD-2026-PARKS` are two identifiers for the contract; later documents use the second. Logistics part.
- The contract is issued on the last day of the appeal period (see the review of `22-AwardedNotification.xml`).
- The allowed-subcontract amount of 4320.00 in the terms equals the winner's subcontract price and stood in the call for tenders before any tender; that lies in `03-CallForTenders.xml`.
