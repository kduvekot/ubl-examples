# LLM review: 24-TenderContract.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/24#F1 · High · A deadline for security clearance although none is required
- XPath: `/TenderContract/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: LatestSecurityClearanceDate is "The end date until which the candidates can obtain the necessary level of security clearance". The security clearance term of the same tendering terms says that no clearance is required, with the reason. A deadline for obtaining something that is not necessary contradicts that statement. (The same pair is in 02 and 03, from which these terms are repeated.)
- Condition: a latest date for security clearance is present only when a clearance is required.
- Options: (a) remove LatestSecurityClearanceDate (preferred); (b) require a clearance, which the description rules out.
- Needs decision: no

### tender/24#F2 · Medium · The contract is identified in three ways, and later documents cite none of the document's own identifiers
- XPath: `/TenderContract/cbc:ID` = `LPWD-DOC-26-0210`
- XPath: `/TenderContract/cac:ContractDocumentReference/cbc:ID` = `PWD-CONTRACT-2026-PARKS`
- XPath: `/TenderContract/cac:TenderResult/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/TenderContract/cbc:ContractFolderID` = `PWD-2026-PARKS`
- Why: the note calls this document "The framework contract, signed by both parties." It then refers to a contract document PWD-CONTRACT-2026-PARKS (an identifier that occurs in no other example; searched over tender/*.xml) and names the contract PWD-2026-PARKS, which is at the same time the procurement file (ContractFolderID) and the procurement project of the notices. The order, the invoice and the debit note cite the contract as PWD-2026-PARKS (e.g. `32-Invoice.xml:/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`), so a reader cannot tell whether they mean the file, the project or the contract, and neither LPWD-DOC-26-0210 nor PWD-CONTRACT-2026-PARKS is ever referenced.
- Condition: the contract has one identifier that is distinguishable from the procurement file, this document states it, and the documents that refer to the contract use it.
- Options: (a) make PWD-CONTRACT-2026-PARKS (or another distinct number) the Contract/ID here and in 21–23, 26, 27, 32, 34 (preferred); (b) keep PWD-2026-PARKS as the contract number and drop the separate ContractDocumentReference, saying in the world's rules that file and contract share the number.
- Needs decision: yes (how the department numbers its contracts)

### tender/24#F3 · Medium · The contract does not record what was agreed: no reference to the accepted tender, no prices, and the call's minimum warranty instead of the tendered one
- XPath: `/TenderContract/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0208`
- XPath: `/TenderContract/cac:TenderingTerms/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/TenderContract/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: the framework's releases are ordered "at the framework prices" (21), and the order 26 and invoice 32 use 499.00 and 18.00 per bench. The contract carries only the total of 124080.00 and the award's description; the tender it accepts (15, VI-DOC-26-0201) is not referenced, the unit prices are nowhere, and the only warranty stated is the call's requirement of five years, while the award was won "with ten years of warranty on the coating". The one document reference points to the awarded notification. For a document that both parties sign as the framework contract, its purpose depends on fixing these terms or on naming the tender that fixes them.
- Condition: the contract identifies the accepted tender (or itself states unit prices and the warranty tendered).
- Options: (a) add a reference to VI-DOC-26-0201 as the tender forming part of the contract (preferred, smallest change); (b) carry the awarded lines with unit prices and the tendered warranty.
- Needs decision: no

### tender/24#F4 · Medium · "Precise" subcontracting rate of 30 % next to an amount that is 3.5 %
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- Why: Rate is "The precise percentage allowed to be subcontracted", MaximumPercent "The maximum percentage allowed to be subcontracted", Amount "The monetary amount assigned to the subcontracted task". A precise rate equal to the maximum makes one of them redundant, and neither agrees with the amount: 30 % of 124080.00 is 37224.00, while 4320.00 is 3.48 % (the rate the tender result gives for the same subcontract). The allowed terms thus state a precise 30 % and an amount that is the actual 3.5 %.
- Condition: within one SubcontractTerms, rate and amount describe the same share; a ceiling is given as MaximumPercent only.
- Options: (a) in AllowedSubcontractTerms keep MaximumPercent 30 and drop Rate and Amount (preferred); (b) set Amount to the 30 % ceiling.
- Needs decision: no

### tender/24#F5 · Medium · References to the call for tenders and the "replaced notice" that resolve to nothing
- XPath: `/TenderContract/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- Why: the call for tenders of the procedure is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189` and the prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`; no document carries the identifiers used here. ReplacedNoticeDocumentReference is moreover "a reference to the notice that is being replaced": a contract replaces no notice, and the prior information notice was followed, not replaced, by the contract notice.
- Condition: references to the call and to notices use the identifiers of 03 and 01/02; a replaced-notice reference is present only in a notice that replaces another.
- Options: (a) LPWD-DOC-26-0189 for the call and remove the replaced-notice reference (preferred); (b) add the PWD-… numbers to 01 and 03 as their file references.
- Needs decision: no

### tender/24#F6 · Medium · PublishAwardIndicator on a supplies contract
- XPath: `/TenderContract/cbc:PublishAwardIndicator` = `true`
- Why: "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)." The project is `/TenderContract/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`, and the world defines no such service categories; the indicator states nothing that applies.
- Condition: the indicator is present only for a service contract of a category where publication is a choice.
- Options: (a) remove it (preferred).
- Needs decision: no

### tender/24#F7 · Medium · Language code in LocaleCode
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderContract/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code and names no locale. Same pattern in 213 of the 250 examples (`grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`).
- Condition: LocaleCode, where present, identifies a locale and differs in kind from Language/ID.
- Options: (a) a locale (country or language-region tag; preferred); (b) leave it out.
- Needs decision: no

### tender/24#F8 · Medium · A province in Region
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division of a country, which is CountrySubentity. A province in Region occurs in 104 examples (`grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: the province is in CountrySubentity; Region is absent or holds a geographic or economic region.
- Options: (a) move it to CountrySubentity (preferred).
- Needs decision: no

### tender/24#F9 · Low · The project has another name than in every other document of the procedure
- XPath: `/TenderContract/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/TenderContract/cbc:ContractName` = `Park benches for the parks renewal programme`
- Why: the procurement project is named `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme` in the notices, the call and the award notice, and the contract's own ContractName uses that name. Only the ProcurementProject of the contract calls it differently.
- Condition: the project name in the contract is the name used in the procedure.
- Options: (a) use "Park benches for the parks renewal programme" (preferred).
- Needs decision: no

### tender/24#F10 · Low · The signed contract repeats the tender-phase terms of the call
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cac:TenderEncryptionData/cbc:MessageFormat` = `CMS`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderValidityPeriod/cbc:DurationMeasure` = `90`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AppealTerms/cbc:Description` = `Appeals to the review board within ten days of the award.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- Why: the TenderingTerms are those of the call for tenders, complete: how tenders are enveloped and encrypted, the tender guarantee due on 2026-02-26 (which the guarantee certificate says is "Released at the award"), the documentation fee, variants, qualification criteria, awarding criteria and auction step, the evaluation committee, who receives tenders, and the appeal against the award. All of that is over when the contract is signed. The terms that do govern the contract (penalty clause, warranty, payment terms, price revision, subcontracting, execution requirement) are in the same block and are hard to tell from the rest; the performance guarantee demanded at the award (22) is not among them.
- Condition: the contract carries the terms that apply to its execution; terms that only governed the submission and evaluation of tenders are absent (or the performance guarantee replaces the tender guarantee).
- Options: (a) reduce TenderingTerms to the execution terms (preferred); (b) keep the full copy and state in a note that the call's terms are annexed.
- Needs decision: no

### tender/24#F11 · Low · Master data of the contractor that the contract does not use; public body as a company
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: the contractor is described with its warehouse provider and stock listing, and its contact for a framework contract is the sales order desk ("Customer service officer"); the subcontractor who is part of the contract (Saltmere Engineering) is not a party of the document. The contracting authority, a municipal department, is described as a company in a commercial register with a liquidation status.
- Condition: the parties carry what the contract uses; the department carries no liquidation status and no commercial-register type.
- Options: (a) reduce the contractor's data and correct the department's legal entity (preferred).
- Needs decision: no

## Checked and consistent
- `/TenderContract/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0208` is the awarded notification (22), a previously sent document between the same parties.
- Tender result identical to 21: AwardID, award 2026-03-09 09:30, 2 tenders (119040.00 and 124080.00), contract from 2026-03-23 for 24 months, 124080.00, subcontract 240 × 18.00 = 4320.00 = 3.48 %.
- Issue date 2026-03-19 lies in the formalization period 2026-03-19 to 2026-03-22 and before the contract start 2026-03-23; both parties sign (Signature 1 the department, Signature 2 Valdara).
- Turnover threshold 250000.00 against "twice the estimate" (2 × 124080.00 = 248160.00): rounded up, consistent.
- Budget line 124080.00 equals the awarded amount.
- OID 2.16.840.1.101.3.4.1.46 is AES-256-GCM (from my knowledge of the NIST arc), matching the algorithm ID.
- Payment terms "30 days after each accepted release" and penalty "0.5 % per day late, at most 10 %" are the terms the later invoice and debit note are compared with in their reviews.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/TenderContract/cac:TenderingTerms/cbc:FundingProgramCode`: a code without listID — refuted as a finding because it is the department's own programme code (party-internal codes are exempt from the listID rule) and has its text in FundingProgram.
- `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name`: the model defines the role as "The Economic Operator issuing the inquiry on the status of a tendering process" — refuted because that definition is a leftover of another document type; in a contract the economic operator is the contractor.
- `/TenderContract/cac:ReceiverParty/cac:PartyName/cbc:Name`: the contractor as receiver of a document it co-signed — refuted because the department issues the signed contract and sends it to the contractor.
- `/TenderContract/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate`: the contract is issued on the last day of the appeal period — not a contradiction within this example (it gives no appeal dates); listed below.
- `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount`: 250000.00 is not exactly twice the estimate — refuted, a rounded threshold.

## Outside this review
- The appeal period of 23 (to 2026-03-19) and the issue of this contract on 2026-03-19 17:24: whether the standstill had run is a timeline question (see 23).
- The copied terms have the same problems in 02 and 03 (security clearance date, subcontract rate, references).
