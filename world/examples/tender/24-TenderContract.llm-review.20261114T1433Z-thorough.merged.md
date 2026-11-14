# LLM review: 24-TenderContract.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/24-TenderContract.xml`, Git blob `f51644d96669fd1bea4cfc230ed7d7bb275322e5` (committed)
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

### tender/24#F1 · High · A latest date for security clearance although no clearance is required
- XPath: `/TenderContract/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/TenderContract/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "The end date until which the candidates can obtain the necessary level of security clearance": it presupposes that a level of clearance is necessary. The security clearance term of the same tendering terms says that none is required and gives the reason. The two values contradict each other; in a contract signed on 2026-03-19 a date of 2026-02-21 for candidates has no use in any case. The same pair is in 01–03, from which the terms are repeated.
- Condition: `LatestSecurityClearanceDate` is present only where the security clearance term requires a clearance.
- Options: (a) remove the date (preferred; the description rules a requirement out); (b) require a clearance, which the story does not support.
- Needs decision: no
- From: broad (F1, High), context (F1, High), logistics (F2, Medium)

### tender/24#F2 · High · Call for tenders and prior notice cited under identifiers no document carries; a "replaced notice" in a contract
- XPath: `/TenderContract/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- Why: A document reference ID is "an identifier for the referenced document". The call for tenders of the flow is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189` and the prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`; no example carries the identifiers cited here (`grep -rl --include='*.xml' PWD-2026-PARKS-CFT world/examples`: tender 01, 02, 03, 06, 15, 17, 19, 24, always as a reference; `PWD-2026-PARKS-PIN`: 01, 02, 03, 24). Other examples cite the same call by its document ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`), so the flow names one call in two ways. `ReplacedNoticeDocumentReference` is moreover "a reference to the notice that is being replaced": a signed contract replaces no notice, and the prior information notice was followed, not replaced, by the contract notice.
- Condition: references to the call for tenders and to notices use an identifier those documents carry, the same one throughout the flow; a replaced-notice reference is present only in a notice that replaces another.
- Options: (a) cite `LPWD-DOC-26-0189` and drop the replaced-notice reference from the contract (preferred); (b) keep the file-style numbers and declare them on 01 and 03 (e.g. as their file reference), so the references resolve.
- Needs decision: no
- From: broad (F5, Medium), logistics (F1, Medium)

### tender/24#F3 · Medium · `PublishAwardIndicator` true for a supply contract
- XPath: `/TenderContract/cbc:PublishAwardIndicator` = `true`
- XPath: `/TenderContract/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: The indicator is "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)". True says this concerns a service contract of such a category; the contract is a framework for the supply of park benches, and the world names no such service categories. The value seems meant as "the award is published", which is not what the element says.
- Condition: the indicator is absent, or false, for a contract that is not a service contract of the categories the definition means.
- Options: (a) remove it (preferred); (b) set it to false.
- Needs decision: no
- From: broad (F6), context (F3)

### tender/24#F4 · Medium · The contract does not identify the accepted tender or the prices its releases are ordered at
- XPath: `/TenderContract/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0208`
- XPath: `/TenderContract/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:PriceEvaluationCode` = `UNITPRICE`
- XPath: `/TenderContract/cac:TenderResult/cbc:Description` = `Both lots to Valdara Industries: the best price-quality ratio, with ten years of warranty on the coating.`
- Why: The document is "The framework contract, signed by both parties", and releases are ordered "at the framework prices, without a new competition" (`21-ContractAwardNotice.xml`, the framework's usage description). The contract carries only the total of the awarded tender for 240 benches; the unit prices (499 lume a bench and 18 lume an installation, readable only from the lines of `15-Tender.xml`) are nowhere in it, and the tender it accepts (VI-DOC-26-0201) is not referenced. Its one document reference points to the awarded notification, which itself references only minutes and an evaluation report, not the tender. The ten-year coating warranty is stated only in the result's description (it is in `15-Tender.xml` as an awarding-criterion response "Ten years on the coating."). For a framework contract that the later orders and invoices refer to for their prices, the purpose depends on fixing these terms or naming the tender that fixes them. Money rated it Low because the catalogue (25) lists the prices; the catalogue is a later document of the supplier, not a term of the contract, so Medium is kept.
- Condition: the contract identifies the accepted tender, or itself states the unit prices that govern releases.
- Options: (a) add a reference to the tender VI-DOC-26-0201 as part of the contract (preferred, smallest change); (b) carry the two awarded tender lines with quantity, unit price and line amount in `AwardedTenderedProject`.
- Needs decision: no
- From: broad (F3, Medium), money (F6, Low)

### tender/24#F5 · Medium · Language code in `LocaleCode`
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderContract/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used". The value (listID `ISO 639`) repeats the language code of the sibling `cbc:ID` and names no locale. The Urvanian parties of the flow carry no `LocaleCode`. 362 such elements in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`).
- Condition: no `LocaleCode` holds a bare language code; each one present names a locale from a list of locales.
- Options: (a) remove `LocaleCode` where the language ID says everything (preferred, as in all earlier flows); (b) give a real locale (e.g. `en-XB`) from a list that defines locales.
- Needs decision: no
- From: broad (F7), parties (F1), context (F5)

### tender/24#F6 · Medium · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The department is a public body (`/TenderContract/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode` = `8411`, general public administration). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a municipal department cannot be wound up like a company, and a registration scheme typed "Commercial register" does not fit a body that is not a company. A general business register may list public bodies, so the register number itself is not questioned.
- Condition: the legal entity of the public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and type the register neutrally or omit the type (preferred); (b) reduce the legal entity to registration name and CompanyID; (c) the City of Lumeport as the legal entity (changes the story).
- Needs decision: no
- From: parties (F4, Low), context (F9, Low), broad (F11, Low, part)

### tender/24#F7 · Medium · A province in `Region`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country … such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the same document use (`Coastal State`). 219 such values in 104 files (`grep -rh --include='*.xml' '<cbc:Region>Province of' world/examples`).
- Condition: the province of an Urvanian address is in `CountrySubentity` (with a code where a list exists); `Region` is absent or holds a region in the sense of the definition.
- Options: (a) move it to `CountrySubentity` (preferred); (b) if "Province of Ferrano" is a postal region only, say so in the world's address rules.
- Needs decision: no
- From: broad (F8), parties (F2), context (F4)

### tender/24#F8 · Medium · `VariantConstraintIndicator` true with a maximum of one variant
- XPath: `/TenderContract/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- Why: The indicator is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)". True says any number of variants may be offered, while `MaximumVariantQuantity` limits them to one. The definition has no value for "allowed, limited in number"; `VariantConstraintCode` = `ALLOWED` and the maximum already say what is meant. Not High, because the binary definition leaves no correct value for the situation; the element is used with a meaning other than its definition.
- Condition: the indicator is not true when the number of variants is limited.
- Options: (a) omit the indicator (preferred); (b) remove the maximum if variants are really unlimited.
- Needs decision: no
- From: context (F2)

### tender/24#F9 · Medium · The tender guarantee's amount does not follow from its rate
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: `AmountRate` is "the rate used to calculate the amount of liability in this financial guarantee". Recalculated: 2 % of the estimate and awarded value (`/TenderContract/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`) is 2481.60; 2 % of lot 1 (119760.00) is 2395.20; 2400.00 is 2 % of 120000.00, an amount that occurs nowhere in the flow. The performance guarantee of `22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00` is exactly 5 % of 124080.00. The guarantee certificate follows the amount (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`); the pair is also in 01–03. Medium, not High, because the base of the rate is not stated.
- Condition: `LiabilityAmount` = `AmountRate` % of an amount the document states, or the rate is absent and the amount is a fixed sum.
- Options: (a) drop `AmountRate` and describe a fixed guarantee of 2400.00 lume (preferred: leaves the certificate untouched); (b) set the amount to 2481.60 here, in 01–03 and in 14. (If F12 removes the tender guarantee from the contract, this finding is resolved here and remains for 01–03.)
- Needs decision: no
- From: money (F2); context noted the figures under "Checked"

### tender/24#F10 · Medium · Allowed subcontracting "precisely" 30 % next to an amount that is 3.5 %, and a rounded "precise" rate in the result
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- Why: `Rate` is "The precise percentage allowed to be subcontracted", `MaximumPercent` "The maximum percentage allowed to be subcontracted", `Amount` "The monetary amount assigned to the subcontracted task". In the allowed terms the precise rate repeats the maximum, and the amount next to it is 3.48 % of the contract (recalculated: 4320.00 / 124080.00 = 3.48 %; 30 % would be 37224.00). The same document then gives the same 4320.00 a rate of 3.5, itself rounded (3.5 % of 124080.00 = 4342.80). One document thus states the share of one amount as 30 % and as 3.5 %. The allowed amount equal to the winner's installation price already stood in the call (03) before any tender; that lies in 03.
- Condition: within `AllowedSubcontractTerms` a ceiling is carried only in `MaximumPercent`, and `Rate`/`Amount`, if present, describe the same share; within `TenderResult/SubcontractTerms`, `Rate` × 124080.00 / 100 = `Amount` to the cent, or the rate is absent.
- Options: (a) in the allowed terms keep `MaximumPercent` 30 and the description and remove `Rate` and `Amount`; in the result keep `Amount` and remove `Rate` (preferred); (b) keep the allowed amount as the estimate of the installation lot and say so.
- Needs decision: no
- From: broad (F4), money (F1)

### tender/24#F11 · Low · The contract is identified in three ways, and the separate contract reference says nothing about what it is
- XPath: `/TenderContract/cbc:ID` = `LPWD-DOC-26-0210`
- XPath: `/TenderContract/cac:ContractDocumentReference/cbc:ID` = `PWD-CONTRACT-2026-PARKS`
- XPath: `/TenderContract/cac:TenderResult/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/TenderContract/cbc:ContractFolderID` = `PWD-2026-PARKS`
- Why: This document is itself the signed contract. It cites a contract document `PWD-CONTRACT-2026-PARKS` with no type, description or date, which occurs in no other example (`grep -rl --include='*.xml' PWD-CONTRACT-2026-PARKS world/examples`: this example only); the UBL definition of the element ("A reference to a set of minutes") is a copy error in the model and gives no guidance. The contract's `Contract/ID` is the same as the procurement file (`ContractFolderID`), and the order, the invoice and the debit note cite that number (`32-Invoice.xml:/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`). Logistics refuted the equality of contract and folder number (it is used consistently as the contract number in 21–23, 26, 27, 32, 34); broad held that a reader cannot tell file, project and contract apart. The unexplained third number remains in either reading.
- Condition: the contract reference says what document it is and how it relates to the contract `PWD-2026-PARKS` (or is absent); whether contract and file share one number is stated by the world's numbering rule.
- Options: (a) add `DocumentType` (e.g. "Signed contract text") or drop the reference, and keep `PWD-2026-PARKS` as the contract number (preferred: no other example changes); (b) make a distinct number the `Contract/ID` here and in 21–23, 26, 27, 32, 34.
- Needs decision: yes (whether the department numbers contract and file alike; broad yes, logistics no)
- From: broad (F2, Medium), logistics (F3, Low); context listed it under "Outside this review"

### tender/24#F12 · Low · The signed contract repeats the tender-phase terms of the call and leaves out the performance guarantee
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:EstimatedTimingFurtherPublication` = `2030`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderValidityPeriod/cbc:DurationMeasure` = `90`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cbc:TenderEnvelopeID` = `ENV-1`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cac:TenderEncryptionData/cbc:MessageFormat` = `CMS`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TenderContract/cac:TenderingTerms/cac:ContractualDocumentReference/cbc:ID` = `PWD-CONTRACT-DRAFT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:LowTendersDescription` = `Prices 30 % below the average are examined.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/TenderContract/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/TenderContract/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AppealTerms/cbc:Description` = `Appeals to the review board within ten days of the award.`
- Why: The tendering terms are those of the call for tenders, complete: how tenders are enveloped and encrypted, the tender guarantee ("a financial guarantee of a tenderer or bid submitter's actual entry into a contract in the event that it is the successful bidder"), due three weeks earlier and "Released at the award." (`14-GuaranteeCertificate.xml`), the fee "to be paid to obtain the contract documents", the advertising ceiling, the admission threshold, the role of a consortium lead (the contractor is a single company), award criteria with the auction step and the committee, the parties who received tenders and qualification requests, a draft "that will become part of the awarded contract" (in the contract itself) and the timing of a next notice. All of that ended with the award. The guarantee the award did require by the day of signature, the performance guarantee (`22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00`, due `22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`), is not in the contract. The terms that do bind the parties (penalty clause, payment terms and frequency, price revision, warranty, execution requirement, subcontracting ceiling, legislation, post-award process, budget line, contract responsible party) are in the same block and hard to tell from the rest.
- Condition: the contract's tendering terms contain only terms that apply between the parties from signature, and a guarantee stated in it is the one in force during performance.
- Options: (a) reduce the terms to those that bind the parties and state the performance guarantee (preferred); (b) keep the full copy with a note that the call's terms are annexed, and record that rule.
- Needs decision: no (reducing the copy changes the encoding, not what happened; money and context said yes, broad, logistics and parties no)
- From: broad (F10), money (F3), parties (F7), logistics (F4), context (F6)

### tender/24#F13 · Low · Signed on the last day of the appeal period
- XPath: `/TenderContract/cbc:IssueDate` = `2026-03-19`
- XPath: `/TenderContract/cbc:IssueTime` = `17:24:00`
- XPath: `/TenderContract/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- Why: The unsuccessful tenderer may present an appeal until `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`, and the awarded notification says "The contract follows after the standstill period." (`22-AwardedNotification.xml:/AwardedNotification/cbc:Note`). The contract is signed at 17:24 on that last day. Whether the end date is inclusive cannot be read from the XML, so the contradiction cannot be settled.
- Condition: the contract is dated after the last day on which an appeal can be presented.
- Options: (a) sign on 20 March, formalisation period 20–22 March (preferred); (b) end the appeal period on 18 March.
- Needs decision: yes
- From: logistics (F5); broad and context listed it under "Outside this review"

### tender/24#F14 · Low · The project has another name than in the rest of the procedure
- XPath: `/TenderContract/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/TenderContract/cbc:ContractName` = `Park benches for the parks renewal programme`
- Why: The procurement project is named `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme` in the notices, the call and the award notice, and this document's own `ContractName` uses that name. "Park benches for the city parks" occurs otherwise only in 08 and 09 (`grep -rn --include='*.xml' 'Park benches for the city parks' world/examples`: 3 files).
- Condition: the procurement project has the same name in the contract as in the notices and the call.
- Options: (a) use "Park benches for the parks renewal programme" (preferred).
- Needs decision: no
- From: broad (F9), logistics (F6), context (F8)

### tender/24#F15 · Low · Party tax exemption reason worded as a transaction
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax". The text begins with a kind of sale ("Sale to a public body"); only its second half is the party's status. The code's list description ("Sale to a public body") also reads as a transaction, but describes the buyer's status, so the code can stay.
- Condition: the party-level exemption reason states the party's status, not a transaction.
- Options: (a) reword the text to the status, e.g. "Public body: exempt from the state sales tax" (preferred); (b) also use a code that names the status.
- Needs decision: no
- From: parties (F3)

### tender/24#F16 · Low · Same Urvanian party tagged `en-XB` here and `en-XU` elsewhere
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: The second rendering of Valdara's names is tagged `languageID="en-XB"` here; in the Urvanian-issued examples the same texts are tagged `en-XU` (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). The text is identical, so the tag follows the issuer's country, not the text. `en-XB` occurs in 13 examples of the flow, `en-XU` in 9 (`grep -c 'languageID="en-XB"' world/examples/tender/*.xml`, likewise `en-XU`). Both readings ("as an English reader in the issuer's country writes it" or an inconsistency) are defensible; earlier merges could not settle it either. The renderings are also Italian names ("Via delle Officine") tagged as English; the earlier flows kept that as a second Low/yes question (world convention of Italianate English names, or not), folded in here by the merge.
- Condition: the English rendering of a given name carries the same `languageID` in every example, or the rule by which it differs is documented.
- Options: (a) tag it by the text (`en-XU`) everywhere (preferred); (b) document the issuer-dependent rule.
- Needs decision: yes
- From: parties (F5, part)

### tender/24#F17 · Low · Legal form of the Urvanian party in one untagged rendering
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Where Valdara is described in Urvanian-issued examples, the legal form is given twice, in Urvanian (`qau`) and in English (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`); here it occurs once, untagged, while the address next to it is rendered in both languages.
- Condition: the legal form is rendered like the address (both renderings, tagged) wherever the party is described in full.
- Options: (a) both renderings, tagged (preferred).
- Needs decision: no
- From: parties (F5, part; split off in the merge)

### tender/24#F18 · Low · Master data of the parties that the contract does nothing with
- XPath: `/TenderContract/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: The contractor is described with its warehousing provider (Castrano Logistics, with a contact that has a name and no means of contact) and its stock listing, and both parties with their customs-trader numbers. The contract stores, despatches and declares nothing. Counter-arguments carried: context held that the contract is where the contractor is identified in full and that Castrano despatches under it (29); parties held that the listing is part of the description of a listed company. Neither makes the data used by this document; the despatch advice carries Castrano in its own role. Customs-trader number XB-TR-410548 occurs in 55 files (`grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`), 36 of them in tender. (Broad's remark that the subcontractor Saltmere is not a party of the contract is refuted in the merge: `TenderContract` has no subcontractor role; the subcontract is described in `SubcontractTerms`.)
- Condition: the parties carry what the contract uses.
- Options: (a) leave the service provider, listing and customs-trader numbers out of the contract (preferred); (b) if the world wants the full description wherever a party is described in full, give the service provider's contact a means of contact.
- Needs decision: no
- From: broad (F11, part), parties (F6); customs-trader numbers added in the merge

### tender/24#F19 · Low · The contractor's contact is the sales order desk
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: For a framework contract the contractor's contact would be the person or desk that manages the contract (key account, contracts); the order desk with a customer-service job title is the contact for orders, copied from the party's master data.
- Condition: the contractor's contact fits the role of managing the contract.
- Options: (a) a contract or key-account contact (preferred); (b) drop the contact.
- Needs decision: no
- From: broad (F11, part; split off in the merge)

### tender/24#F20 · Low · The penalty clause names no base for its percentages
- XPath: `/TenderContract/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: The clause is the contract's only statement of the penalty and says neither of what amount the 0.5 % and the 10 % are taken nor what "late" refers to. The later debit note must choose: `34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.` On the contract value the same three days would be 1861.20 lume (recalculated: 124080.00 × 0.005 × 3).
- Condition: the clause states the base of both percentages and the event that is late, and the debit note's amount follows from it.
- Options: (a) word the clause as the flow applies it, e.g. "0.5 % of the price of the late part of a release per day of delay, at most 10 % of that price" (preferred); (b) another base, with the debit note recalculated.
- Needs decision: no
- From: money (F4)

### tender/24#F21 · Low · Turnover threshold not "twice the estimate", and "at least" coded as "greater than"
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: Twice the estimate (124080.00) is 248160.00, not 250000.00; the description says "at least" (≥) while code and expression say "greater than" (>). Broad refuted the amount as a rounded threshold; that leaves the text, which states no rounding, and the comparison mismatch, which no rounding explains. Low here, although merger A rates the same criterion Medium in 01–03: in the signed contract the criterion no longer decides anything (admission is over), so the mismatch misleads no reader about an obligation.
- Condition: amount, description, code and expression state one rule.
- Options: (a) "Yearly turnover of at least 250000 lume (about twice the estimate)" with a greater-or-equal code (preferred); (b) threshold 248160.00 and one comparison. (Resolved here also by F12 option (a), which removes the criterion from the contract; it remains for 01–03.)
- Needs decision: no
- From: money (F5); broad refuted the amount (carried as argument)

### tender/24#F22 · Low · Indicators of a design contest in a supply framework
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- Why: `PrizeIndicator` "Indicates whether a prize will be awarded", `FollowupContractIndicator` "Indicates if any service contract following the contest will be awarded to the winner …" and `BindingOnBuyerIndicator` "Indicates if the decision is binding on the buyer" describe a design contest and its jury. This is an open procedure for a supply framework; the two "false" values state what needs no stating (IND5/IND6), and "binding: true" has no jury decision to refer to.
- Condition: the three indicators are present only in the documents of a design contest.
- Options: (a) remove them (preferred).
- Needs decision: no
- From: context (F7)

## Checked and consistent
- `PreviousDocumentReference` `LPWD-DOC-26-0208` is the awarded notification (22) to Valdara, the document this contract follows.
- Tender result identical to 21, 22 and 23: award `PWD-2026-PARKS-AWARD-1` on 2026-03-09 09:30, two tenders (119040.00 = 19-Tender, 124080.00 = 15-Tender; 17 was withdrawn), one foreign, both electronic; contract from 2026-03-23 for 24 months (ends 2028-03-22). 124080.00 = lot 1 119760.00 (240 × 499) + lot 2 4320.00 (240 × 18), checked in 15.
- Issue date 2026-03-19 lies in the formalisation period 2026-03-19 to 2026-03-22 and before the contract start; two signatures, the department and Valdara, matching the note.
- Budget line 124080.00 = estimate = awarded amount; advertisement 320.00 ≤ ceiling 500.00; awarding criterion AC-1 range 350.00–600.00 contains both tenderers' unit-price totals (517, 496).
- `PaymentFrequencyCode` PERRELEASE agrees with "30 days after each accepted release.".
- OID 2.16.840.1.101.3.4.1.46 is AES-256-GCM (own knowledge of the NIST arc).
- "A next procedure in about four years" and `EstimatedTimingFurtherPublication` 2030 agree (2026 + 4).
- The warranty of 5 years equals the tender's `WarrantyValidityPeriod` (5 ANN, "Five years on the frame.") in 15.
- Parties: Lumeport Public Works Department `20410548` and Valdara `XU-R-104274` identified the same way across the flow; CompanyID = PartyIdentification, endpoint = country prefix + number, tax scheme fits the country (from parties). Valdara's RegistrationDate is 1962-04-12, not the recurring 1996-01-01.
- `check_ids.py`: ISIN XU0001042501 correct.

## Considered and refuted
- `/TenderContract/cac:TenderingTerms/cbc:FundingProgramCode`: a code without listID — refuted because it is the department's own programme code (party-internal codes are exempt from the listID rule) and has its text in FundingProgram (from broad; context listed it as outside its lens).
- `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name`: the model defines the role as "The Economic Operator issuing the inquiry on the status of a tendering process" — refuted because that definition is a leftover of another document type; in a contract the economic operator is the contractor (from broad).
- `/TenderContract/cac:ReceiverParty/cac:PartyName/cbc:Name`: the contractor as receiver, redundant next to the economic operator — refuted because the department issues the signed contract and sends it to the contractor (from broad, parties, context).
- `/TenderContract/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate`: issue on the last day of the appeal period — broad saw no contradiction within this example; the merge follows logistics and keeps it as F13 (Low, yes) (from broad).
- `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount`: 250000.00 not exactly twice the estimate — refuted by broad as a rounded threshold; the merge keeps money's F21 for the text/code mismatch (from broad).
- `/TenderContract/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric`: the whole 24-month framework on the 2026 budget — refuted because a commitment can be entered in the year of signature and nothing contradicts it (from money).
- `/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note`: the invoice applies other terms (30 days from invoice, 2 % discount, 8 % interest) — refuted as a finding of the contract, whose term is clear; the difference belongs to 32 (from money).
- `/TenderContract/cac:TenderingTerms/cbc:PriceRevisionFormulaDescription`: "Steel index each January." gives no formula — refuted: the element is a description and no document applies a revision (from money).
- `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount`: award criteria in a contract — refuted for money (range consistent); presence covered by F12 (from money).
- `/TenderContract/cac:TenderResult/cbc:AdvertisementAmount`: the authority's advertising cost in a contract — refuted as harmless repetition of the published result (from money).
- `/TenderContract/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` instead of ISO 8601 `-01:00` — refuted: the element is text and every address of the flow uses the same form (from parties).
- `/TenderContract/cac:ContractingParty/cac:Party/cac:Contact/cbc:Telephone`: +999 a real country code — refuted: +999 is not assigned in ITU-T E.164 (from parties).
- `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: unused master data — parties refuted it as part of the legal-entity description; the merge disagrees and keeps it in F18, with that argument (from parties).
- `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990` a real ISO 6523 ICD — refuted: 0990 is not an allocated ICD (own knowledge; register not consulted online) (from parties).
- `/TenderContract/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name`: "The Party who executes the Contract" could mean the contractor — refuted: for a contracting authority it reads as the unit that concludes and administers the contract (from parties).
- `/TenderContract/cac:TenderResult/cbc:ReceivedTenderQuantity`: `2` against three tender documents — refuted: 17 was withdrawn and replaced by 19 (from logistics); award statistics in a contract — refuted because the tender result is mandatory in the document (from context).
- `/TenderContract/cac:TenderResult/cac:Contract/cbc:ID`: equal to `ContractFolderID` — refuted by logistics as consistent use; carried as counter-argument in F11 (from logistics).
- `/TenderContract/cac:TenderingTerms/cac:AppealTerms/cac:PresentationPeriod/cbc:DurationMeasure`: appeal terms in a signed contract — refuted for logistics (contradicts nothing); presence covered by F12 (from logistics).
- `/TenderContract/cac:TenderingTerms/cac:TenderPreparation/cbc:OpenTenderID`: `OPEN-1` — refuted: resolves to the opening event of the call (from logistics).
- `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:ServiceProviderParty`: unused master data — refuted by context (the contract identifies the contractor in full; Castrano despatches under it); the merge disagrees and keeps it in F18 (from context).
- `/TenderContract/cac:TenderingTerms/cac:ContractAcceptancePeriod`: a period for accepting the contract in the contract — refuted as a term between the parties (from context).
- `/TenderContract/cac:TenderingTerms/cac:WarrantyValidityPeriod`: 5 years although the award mentions ten years on the coating — refuted: 5 years is the general warranty (also in 15), the ten years are in the result's description (from context; also refutes the warranty part of broad F3, see "Changed in the merge").
- `/TenderContract/cac:TenderingProcess`: only identifier and procedure code — refuted, that is all the contract needs (from context).

## Refuted in the merge
### broad/F11 (part) · Low · The subcontractor who is part of the contract is not a party of the document
- XPath (in the part): `/TenderContract/cac:EconomicOperatorParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch` (finding on unused master data, with the remark "the subcontractor who is part of the contract (Saltmere Engineering) is not a party of the document").
- Refuted because: the UBL 2.5 `TenderContract` has only Contracting Party, Economic Operator Party and Receiver Party (checked in the model), so there is no role for a subcontractor; the subcontract is stated in `TenderResult/SubcontractTerms/Description`, which names Saltmere. The rest of broad/F11 is in F6, F18 and F19.

## Changed in the merge
- broad/F5, logistics/F1 → F2: raised from Medium to High: a reference to an identifier no document carries is section 6's "referenced document that does not exist", and the flow cites the same call under two IDs (25 uses LPWD-DOC-26-0189).
- logistics/F2 → F1: Medium raised to High, as broad and context, because the date and the code contradict each other.
- broad/F3 + money/F6 → F4: combined; Medium kept (money's Low argument quoted); broad's warranty sub-claim weakened, because the 5-year warranty is the tender's own (context's refutation).
- parties/F4, context/F9, broad/F11 (part) → F6: raised from Low to Medium, aligned with analysis/review-merge-decisions.md (public bodies as companies: Medium/no).
- broad/F2 (Medium, yes) + logistics/F3 (Low, no) → F11: Low, Needs decision yes; logistics' refutation of the folder-number equality carried as counter-argument.
- broad/F10, money/F3, parties/F7, logistics/F4, context/F6 → F12: one finding; Needs decision no (money and context said yes).
- parties/F5 → F16 and F17: split into the tag question (Low, yes) and the untagged legal form (Low, no), as in the earlier flows.
- broad/F11 → F6, F18, F19: split into the public-body legal entity, copied master data and the contact; customs-trader numbers added to F18 by the merge.
- money/F2 → F9: note added that F12 option (a) would resolve it in this document.

## Outside this review
- The allowed-subcontract amount 4320.00 equal to the winner's installation price stood in the call (03) before any tender was received; that lies in 03 (from context).
- The copied terms have the same problems in 01–03 (security clearance date, subcontract rate, guarantee rate, references) (from broad).
- "Ten years of warranty on the coating" in the award result against the tender's awarding-criterion response: consistent with 15; whether the coating warranty should appear as a warranty period lies with 15/21.
