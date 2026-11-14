# LLM review: 21-ContractAwardNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/21-ContractAwardNotice.xml`, Git blob `59a77855a9c7e78ea4690806b5a919a52b58df71` (committed)
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

### tender/21#F1 · High · The opening of tenders is still "scheduled" and not completed in the notice of the award
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate` = `2026-02-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:CompletionIndicator` = `false`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:CurrentStatus/cbc:ConditionCode` = `SCHEDULED`
- XPath: `/ContractAwardNotice/cbc:IssueDate` = `2026-03-13`
- Why: `CompletionIndicator` is "An indicator that this event has been completed (true) or not (false)" and `CurrentStatus` "The current status of this event". The notice is issued on 2026-03-13 and announces an award of 2026-03-09 made on two received tenders (`/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity` = `2`); the opening of 2026-02-26 14:00 necessarily took place. The notice nevertheless says the opening is not completed and is scheduled. The values are those of the contract notice and the call for tenders, where they were true.
- Condition: In the award notice the opening event is either absent or marked completed, with a status that says it took place.
- Options: (a) preferred: `CompletionIndicator` true and a status "held"/"completed"; (b) leave the opening event out of the award notice.
- Needs decision: no

### tender/21#F2 · Medium · Periods of a procedure with invitation in an open procedure
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: `InvitationSubmissionPeriod` is "The period during which invitations to tender must be completed and delivered", `ParticipationInvitationPeriod` "The period during which the invitation to participate must be sent" and `ParticipationRequestReceptionPeriod` "The period during which requests for participation must be completed and delivered". These are steps of a restricted or negotiated procedure, in which operators first ask to take part and are then invited. The procedure is open ("Open procedure with two lots."): every operator may tender directly, nobody requests participation and nobody is invited. The periods also end on or before the day the contract notice was issued (`02-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-02-11`), i.e. before operators could know of the procedure. They have no meaning in this procedure, and none in a notice of its award.
- Condition: A tendering process whose `ProcedureCode` is `OPEN` carries no periods for participation requests or invitations.
- Options: (a) preferred: remove the three periods; (b) if the world's open procedure does have a registration step, describe it and give periods that lie after the contract notice.
- Needs decision: no

### tender/21#F3 · Medium · `OriginalContractingSystemID` in a process that reopens nothing
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- Why: The definition is conditional: "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system". This process is not a reopening of competition inside an existing framework: it is an open procedure that sets up a new framework agreement (`/ContractAwardNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`, contract `PWD-2026-PARKS`). A framework of 2024 occurs nowhere else in the flow.
- Condition: `OriginalContractingSystemID` is absent unless the process is a mini-competition under an earlier framework or purchasing system, which the documents then describe.
- Options: (a) preferred: remove it; (b) if a 2024 framework is being replaced, say so in text; the element still does not fit, because nothing is reopened.
- Needs decision: no

### tender/21#F4 · Medium · `PublishAwardIndicator` true for a supply contract
- XPath: `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: The indicator is "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)". True therefore says that this is an award notice for a service contract of such a category. The procurement is a supply of park benches (lot 2, the installation, is an accessory service of 4320.00 out of 124080.00), and the world names no such service categories. The value seems to be meant as "the award may be published", which is not what the element says.
- Condition: The indicator is absent, or false, for a notice that is not about a service contract of the categories the definition means.
- Options: (a) preferred: remove it; (b) set it to false.
- Needs decision: no

### tender/21#F5 · Medium · The price of paper copies as "reimbursement fee for concession procurement projects"
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- Why: `RequiredFeeAmount` is "The amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "Text describing the reimbursement fee for concession procurement projects". The project is a framework for supplies, not a concession, and the amount is what a paper copy of the procurement documents costs; for that UBL has `TenderingTerms/DocumentationFeeAmount`, which the call for tenders also uses (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`). Stated three times (project and each lot) it also reads as 50 lume per lot. In a notice of the award the price of the tender documents has no use at all.
- Condition: `RequiredFeeAmount` and `FeeDescription` of a procurement project are present only for a concession's reimbursement fee; the documentation fee is not repeated in the award notice.
- Options: (a) preferred: remove both elements from the project and the lots here; (b) none seen for this document.
- Needs decision: no

### tender/21#F6 · Medium · Unit prices as minimum and maximum amount of a deliverable whose estimate is a total
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- Why: `MinimumAmount` and `MaximumAmount` are "The minimum/maximum amount allowed for this deliverable" and `EstimatedAmount` "The estimated total amount of the deliverable"; the deliverable of the line is 240 benches. The estimate, 119760.00, is a total (240 × 499.00), but 350.00 and 600.00 can only be prices of one bench (the tenders offer 480.00 and 499.00 a bench). Three amounts of the same line about the same deliverable are on two different bases, and read as defined the line allows at most 600.00 for a deliverable estimated at 119760.00.
- Condition: Minimum, maximum and estimated amount of a request-for-tender line refer to the same thing (the whole line), or the unit-price limits are in an element or text that says they are per bench.
- Options: (a) preferred: give the limits for the line (240 × 350 = 84000.00 and 240 × 600 = 144000.00), or drop them from the award notice, where price limits for tenders no longer matter; (b) state the unit-price limits in the line's note.
- Needs decision: no

### tender/21#F7 · Medium · A province in `Region`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/21#F8 · Medium · A language code as locale
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/21#F9 · Low · An electronic auction is announced, and the award shows no trace of one
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:LowerTenderAmount` = `119040.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:HigherTenderAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `AuctionConstraintIndicator` "Indicates whether an electronic auction will be used before the awarding of a contract (true) or not (false)", and the terms say that after the evaluation every tenderer with an admissible tender is invited to an auction on the unit prices. The notice comes after the award, so "will be used" is past; yet the awarded amount and the lowest and highest tender are exactly the totals of the tenders as submitted (`15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`, `19-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`), and no document of the flow mentions that the auction was held, when, or with what result (searched "auction" in `world/examples/tender/*.xml`: only the terms and the minimum improvement bid of the criteria). Either the auction was held without any bid, or it was not held; the award notice, whose purpose is to report the outcome, says neither.
- Condition: The award notice either reports the auction (held on a date, with or without bids, final prices) or does not announce one; announced auction and reported result agree.
- Options: (a) preferred: state in the tender result that the auction was held and no tenderer lowered its price (or adapt the amounts if one did); (b) drop the auction from the procedure in all its documents.
- Needs decision: yes (changes the story of the procedure)

### tender/21#F10 · Low · The award notice repeats what was needed to prepare a tender
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AdditionalInformationRequestPeriod/cbc:EndDate` = `2026-02-19`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:SubmissionMethodCode` = `ELECTRONIC`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:RequiredDocumentReference/cbc:ID` = `PWD-PRICE-TPL`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProvidedDocumentReference/cbc:ID` = `PWD-SITE-PLAN`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:RequiredDocumentReference/cbc:ID` = `PWD-PRICE-TPL`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProvidedDocumentReference/cbc:ID` = `PWD-SITE-PLAN`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- Why: A contract award notice is "A document published by a Contracting Party to announce the awarding of a procurement project". Deadlines for documents, questions and tenders, the submission method, the price template tenderers had to fill in, the site plan given to them and tendering terms "as for the procedure" (of which this notice carries only the appeal body) were instructions to tenderers; all of them lie in the past and none is used by the announcement of the award. The block is the same as in the contract notice and reads as copied from it. (What identifies the procedure and its object — procedure type, lots, description, quantities, value — is rightly there.)
- Condition: The award notice carries of the tendering process and the lots only what identifies them and what the award refers to.
- Options: (a) preferred: remove the past instructions to tenderers; (b) keep them if the world's notice form prescribes a full repetition, and record that rule.
- Needs decision: yes (how much of the notice is repeated is a design decision for all notices of the flow)

### tender/21#F11 · Low · The installation lot is described with the supply lot's text
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- Why: Lot 2 is a service lot (`SERVICES`, `INSTALL`, CPC 87390 installation services). Its description is the description of the whole project and of lot 1 (the supply of benches, "delivered"), its strategic type asks for recycled steel and certified timber, which are properties of the goods of lot 1 and cannot be met by an installation service, and its extension speaks of more benches rather than of their installation. The lot-specific values (name, type codes, classification, amounts 4320.00 / 2160.00) are right; the texts are the project's.
- Condition: The description, strategic type and option text of lot 2 describe the installation service (anchoring 240 benches; 120 more installations in the extension), and environmental requirements are stated for lot 2 only if the installation has one.
- Options: (a) preferred: give lot 2 its own description and option text and drop the green procurement type from it; (b) keep the green type with a requirement that fits an installation.
- Needs decision: no

### tender/21#F12 · Low · Urvanian declared as additional language of a notice that has no Urvanian text
- XPath: `/ContractAwardNotice/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- XPath: `/ContractAwardNotice/cbc:NoticeLanguageCode` = `en`
- Why: `AdditionalNoticeLanguage` is "An additional official language used in this contract award notice". No text of the notice is in Urvanian: the only values tagged `qau` are the street and town of the winner's address (3 elements with `languageID="qau"`, counted with grep in this XML), which are parts of an address, not of the notice. Urvanian is also the language of Urvania; the notice is of a Bayvarran authority, whose documents give English as its language.
- Condition: Every language declared for the notice is one in which the notice's texts (note, descriptions) are actually given, or the declaration is absent.
- Options: (a) preferred: remove the additional language; (b) give the notice's texts in Urvanian as well (with words from the lexicon), if the Trade Accord requires publication in both languages.
- Needs decision: yes

### tender/21#F13 · Low · The contracting party repeated as originator and as beneficiary
- XPath: `/ContractAwardNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractAwardNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `OriginatorCustomerParty` and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") hold the same party as `ContractingParty`. They add information only when another body originated the need or benefits from the supply; here they repeat the contracting party, with no business reason of their own (rule "no fillers").
- Condition: Both are present only when they are a party other than the contracting party, or are absent.
- Options: (a) preferred: remove both; (b) name the body that uses the benches, if the world has one.
- Needs decision: no

### tender/21#F14 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/21#F15 · Low · Master data of a party that the document does not use
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The notice announces that this party won; who stores and despatches its goods, how many shares it has and where they are listed is not part of that announcement. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py`: ISIN XU0001042501 has a correct check digit.
- Tender result against the tenders: two tenders counted (Valdara `15-Tender.xml`, Brackenmere `19-Tender.xml`; `17-Tender.xml` was withdrawn), both electronic, one foreign (Valdara, Urvania); lowest 119040.00 and highest 124080.00 are their totals; awarded amount 124080.00 is Valdara's total; rank 1; description "ten years of warranty on the coating" is Valdara's criterion response.
- Subcontract terms: 240 × 18.00 = 4320.00; 4320.00 / 124080.00 = 3.48 %, given as 3.5; `UnknownPriceIndicator` false with an amount; Saltmere Engineering is the subcontractor of Valdara's tender.
- Amounts of project and lots: 119760.00 + 4320.00 = 124080.00; minimum = half (120 of 240 benches), maximum = × 1.2 (288 of 240); renewal 62040.00 = 59880.00 + 2160.00; framework maximum 186120.00 = 124080.00 + 62040.00; average subsequent contract 20680.00 = 124080.00 / 6 ("Releases every few months" over 24 months).
- Dates: award 2026-03-09 09:30 before the issue of the notice (2026-03-13) and the requested publication (2026-03-14); contract start 2026-03-23 = start of the planned period and of the contract's validity (24 months, to 2028-03-22); formalization period 2026-03-19 to 2026-03-22 contains the contract's issue date (`24-TenderContract.xml`, 2026-03-19).
- `PreviousDocumentReference` `LPWD-DOC-26-0188` is the contract notice, `NoticeDocumentReference` `LPWD-DOC-26-0187` the prior information notice.
- `NoticeTypeCode` `CAN`, `TenderResultCode` `AWARDED`, `ContractTypeCode` and `ContractingSystemCode` `FRAMEWORK`, one operator in the framework: agree with each other.

## Considered and refuted
- `/ContractAwardNotice/cac:ProcurementProject/cbc:QualityControlCode`: the definition speaks of a "works project" while this is a supply — refuted because the value ("Inspection on delivery") is a quality control that fits a supply, and the definition's wording is read as the project.
- `/ContractAwardNotice/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator`: true without a named agreement — refuted because the world has the Lumeport Trade Accord, under which a foreign tenderer takes part and wins.
- `/ContractAwardNotice/cac:TenderingProcess/cbc:TerminatedIndicator`: false although the competition is over — refuted because "terminated" means ended without result; the procedure ended with an award.
- `/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity`: three tenders exist in the flow — refuted because one was withdrawn before the deadline; two remained.
- `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Rate`: defined as the percentage "allowed" to be subcontracted, used for the actual share — refuted as a legitimate reading in a result (the share the awarded tender subcontracts).
- `/ContractAwardNotice/cac:TenderingProcess/cac:ContractingSystem`: "Only when the procedure is repetitive" — refuted because the framework's releases are the repetition.
- `/ContractAwardNotice/cbc:RegulatoryDomain`: names a domain rather than a law — refuted as a legitimate reading of "Information about the law that defines the regulatory domain".
- `/ContractAwardNotice/cac:ReceiverParty`: a receiver of a published notice — refuted because the Bayvarra Information Service is where the notices of the flow are sent for publication.
- `/ContractAwardNotice/cac:ProcurementProject/cbc:RequestedDeliveryDate`: one date for a two-year framework — refuted because it is the start of the delivery period of line 1 (first release).

## Outside this review
- The estimates of the project and the lots (124080.00, 119760.00, 4320.00) equal the winner's tender to the cent, already in the prior information notice, the contract notice and the call for tenders, which were issued before any tender existed; this lies in those examples.
- The start dates of the document availability, invitation and participation periods (2026-01-26) precede the contract notice (2026-02-11) and the call for tenders (2026-02-12); a timeline question across the documents.
- The same identifier `PWD-2026-PARKS` serves as contract folder, procurement project and contract; identifier kinds are the logistics part's lens.
