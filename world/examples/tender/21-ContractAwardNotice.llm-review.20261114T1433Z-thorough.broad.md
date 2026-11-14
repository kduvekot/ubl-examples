# LLM review: 21-ContractAwardNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/21#F1 · High · The opening of tenders is still "scheduled" and "not completed" four days after the award
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate` = `2026-02-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:CompletionIndicator` = `false`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:CurrentStatus/cbc:ConditionCode` = `SCHEDULED`
- Why: CompletionIndicator is "An indicator that this event has been completed (true) or not (false)". The notice is issued on `/ContractAwardNotice/cbc:IssueDate` = `2026-03-13` and reports the award of `/ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-03-09`, two tenders received and an auction held on 6 March. Tenders that were evaluated and awarded have been opened; the event of 2026-02-26 cannot still be scheduled. The values are those of the contract notice and the call for tenders (02, 03), where they were true.
- Condition: an opening event in the award notice is in the past and marked completed, or the event is absent.
- Options: (a) CompletionIndicator true and a status meaning held/completed (preferred, the notice then reports the procedure as it went); (b) leave OpenTenderEvent out of the award notice.
- Needs decision: no

### tender/21#F2 · High · Participation and invitation periods that end before the procedure was announced, in an open procedure
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: the notice refers to the contract notice `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0188`, issued `02-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-02-11`; the call for tenders followed on `03-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-02-12`. According to the periods here, invitations to tender had to be delivered by 1 February and requests for participation by 11 February, i.e. before or on the day the procedure was first announced, and the documents were available from 26 January, sixteen days before the notice. In the flow, the expression of interest (04, 2026-02-14) and the qualification application (07, 2026-02-19) came after these periods ended. In addition, an open procedure has no stage of participation requests and invitations at all ("requests for participation", "invitation to participate" belong to restricted procedures), so the three periods contradict the procedure code.
- Condition: every period of the tendering process lies after the contract notice that announces it, and only periods that exist in an open procedure are given.
- Options: (a) drop the invitation and participation periods and start the document availability at the contract notice (preferred for an open procedure); (b) keep them with dates after 2026-02-11 and make the procedure a restricted one, which changes the story.
- Needs decision: yes (the kind of procedure and its calendar)

### tender/21#F3 · Medium · OriginalContractingSystemID without a reopening
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- Why: the definition has a condition: "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system." This procedure is not a reopening of competition under an existing framework: it is an open procedure that sets up a new framework with one supplier (`/ContractAwardNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`), and its subsequent releases are ordered "without a new competition". A framework of 2024 appears nowhere else in the flow.
- Condition: OriginalContractingSystemID is present only in a procedure that reopens competition under the framework or system it names.
- Options: (a) remove it (preferred); (b) if a predecessor framework is to be mentioned, say so in a note.
- Needs decision: no

### tender/21#F4 · Medium · PublishAwardIndicator on a supplies contract
- XPath: `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`
- Why: "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)." The indicator answers a question that arises only for service contracts of particular categories (in EU practice, whether the authority agrees to publish an award for such services). The project is a supply (`/ContractAwardNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`), and nothing in the world defines such service categories, so "true" asserts something the notice does not mean.
- Condition: the indicator is present only where the contract is a service of a category for which publication is a choice.
- Options: (a) remove it (preferred); (b) define the service categories in the world's procurement law and use it for lot 2 only.
- Needs decision: no

### tender/21#F5 · Medium · Language code in LocaleCode
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code and names no locale. Same pattern in 213 of the 250 examples (`grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`).
- Condition: LocaleCode, where present, identifies a locale and differs in kind from Language/ID.
- Options: (a) a locale (country or language-region tag; preferred); (b) leave it out.
- Needs decision: no

### tender/21#F6 · Medium · A province in Region
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division of a country, which is CountrySubentity. A province in Region occurs in 104 examples (`grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: the province is in CountrySubentity; Region is absent or holds a geographic or economic region.
- Options: (a) move it to CountrySubentity (preferred).
- Needs decision: no

### tender/21#F7 · Low · An additional notice language of which the notice contains nothing
- XPath: `/ContractAwardNotice/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- Why: "An additional official language used in this contract award notice." Every text of the notice is in English only; the only `languageID` attributes in the document are on the winner's street and city names. Urvanian is the language of Urvania, not an official language of Bayvarra as far as the examples show (the Bayvarran parties all have language English).
- Condition: a language named as used in the notice is used in it (texts repeated with that languageID), or it is not named.
- Options: (a) remove AdditionalNoticeLanguage (preferred); (b) repeat the notice's texts in Urvanian, if publication in the winner's language is part of the Trade Accord.
- Needs decision: no

### tender/21#F8 · Low · The estimate made before the procedure equals the winning tender to the cent
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: the authority's estimate (already in the contract notice and the call, before any tender existed) is 240 × 499.00 + 240 × 18.00, exactly the unit prices Valdara then tendered (15-Tender.xml: 119760.00 and 4320.00). An estimate that matches one tenderer's later prices to the cent is not plausible, and in a real procedure would raise the question of how the tenderer knew it.
- Condition: the estimate is a figure the authority could have had before the tenders (a round budget figure), different from the awarded amount; the amounts derived from it (minimum, maximum, average release, renewal) follow.
- Options: (a) a rounded estimate, e.g. 125000 or per-unit 500 and 20 (preferred); (b) keep and state in the notice that the "estimate" has been updated to the awarded value, which the element names do not support.
- Needs decision: no

### tender/21#F9 · Low · The opening is electronic but has the department as its location
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- Why: OccurrenceLocation is "the location of this event"; the name is the organisation plus a street, not a place where tenderers could attend, and the description says the opening is online. A reader cannot tell whether one may attend in person.
- Condition: the location of the opening is either the online place (e.g. the platform address) or a room that can be attended, and agrees with the description.
- Options: (a) drop the location, the description and AccessToolsURI being enough (preferred); (b) name the room and say attendance is possible.
- Needs decision: no

### tender/21#F10 · Low · Lot 2 (installation) carries the description and classification of the benches
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- Why: lot 2 is `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`, a service. Its description is that of the whole project (supply of benches), its additional classification is CPC 381 (furniture), and its "green" requirement speaks of steel and timber, which an installation service does not supply. The lot was filled with the project's data.
- Condition: the description, classifications and strategic requirements of lot 2 describe the installation service.
- Options: (a) own description ("Anchoring of 240 benches in the parks …") and only the service classification (preferred); (b) none other seen.
- Needs decision: no

### tender/21#F11 · Low · Public bodies described as companies; the review board's contact is a procurement officer
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: the department, the information service and the review board are public bodies (ISIC 8411, 8411, 8423). None is a company in a commercial register, and none has a liquidation status. The review board's contact is named "Registry", which fits, but its job title and department are those of a buying office; a board that judges procurement appeals has no procurement department answering appeals.
- Condition: public bodies carry no liquidation status and no commercial-register type; the registry's job title and department agree with the name "Registry".
- Options: (a) drop the liquidation status, type the register as one of public bodies, and give the registry a registrar/clerk title (preferred).
- Needs decision: no

### tender/21#F12 · Low · Master data of the winner that a published notice does not use
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: an award notice names the winner. The winner's logistics provider, the mobile number of its order desk and its customs trader number have no function in a notice for publication, and the installer who matters for the award (Saltmere Engineering, the subcontractor for lot 2) appears only in free text (`/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Description`).
- Condition: the winning party carries what a published award needs (identity, name, address, size); data about its own suppliers and sales desk is absent.
- Options: (a) reduce the winner's party data (preferred); (b) keep if full party data in every document is the world's rule.
- Needs decision: no

## Checked and consistent
- References: `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0188` is the contract notice (02); `/ContractAwardNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187` is the prior information notice (01). The minutes PWD-MIN-AWARD-26 are also cited by 22 and 23.
- Tender amounts: lower 119040.00 is Brackenmere's corrected tender (19), higher 124080.00 is Valdara's (15); awarded 124080.00 = 119760.00 + 4320.00. Received tenders 2 (17 was withdrawn), electronic 2, foreign 1 (Valdara, Urvania).
- Subcontracting: 240 × 18.00 = 4320.00; 4320.00 / 124080.00 = 3.48 %, given as 3.5.
- Derived amounts: minimum 62040.00 = 120/240 × 124080.00; maximum 148896.00 = 288/240 × 124080.00 = FrameworkAgreement EstimatedMaximumValueAmount; MaximumValueAmount 186120.00 = 124080.00 + renewal 62040.00; average release 20680.00 = 124080.00 / 6 ("every few months" over 24 months). The same holds per lot (119760.00: 59880.00, 143712.00, 19960.00; 4320.00: 2160.00, 5184.00, 720.00).
- Dates: award 2026-03-09 09:30 precedes the notifications 22 and 23 of the same day and this notice (2026-03-13); formalization 2026-03-19 to 2026-03-22 contains the issue date of the contract (24, 2026-03-19); contract start 2026-03-23 = PlannedPeriod start = TenderResult StartDate; 24 months end 2028-03-22.
- Description "ten years of warranty on the coating" matches Valdara's criterion response in 15.
- CPC 38111 (seats with metal frames) for lot 1 and 87390 (installation services n.e.c.) for lot 2 fit, from my knowledge of CPC 2.1.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/ContractAwardNotice/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator`: "true" might claim coverage by the real WTO GPA — refuted because the UBL 2.5 definition says "a government procurement agreement" in general, which the Trade Accord can be.
- `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Rate`: "precise percentage" but 3.5 is rounded from 3.48 — refuted as ordinary rounding to one decimal.
- `/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity`: three tenders were submitted (15, 17, 19) — refuted because 17 was withdrawn before the deadline and does not count as received.
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount`: 350.00 and 600.00 are unit prices next to an estimated line total — refuted because the call's price criterion defines the same range per bench, so the reading is fixed within the flow.
- `/ContractAwardNotice/cac:TenderResult/cac:Contract/cbc:ID`: PWD-2026-PARKS is also the folder and project ID — refuted here because the contract is not yet formalized when the notice is issued and the authority may number it after the file; how the later documents identify the contract is looked at with 24 and 26.
- `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:UUID`: the same UUID as the project-level line — refuted because it is the same line, repeated under its lot.
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: transaction-like reason on the party — refuted, the text states the party's status.
- `/ContractAwardNotice/cac:TenderingProcess/cbc:TerminatedIndicator`: false although the competition is over — refuted because "terminated" means stopped without result; the procedure ended with an award.

## Outside this review
- The same periods (F2), OriginalContractingSystemID (F3) and estimate (F8) are in 02-ContractNotice.xml and 03-CallForTenders.xml.
