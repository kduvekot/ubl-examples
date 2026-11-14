# LLM review: 20-TendererQualificationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/20-TendererQualificationResponse.xml`, Git blob `6cb54f8c8eae89a453504f165e001d727d6477c8` (committed)
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

### tender/20#F1 · High · The appeal period is the award's, which did not exist yet, and contradicts "within ten days" of this decision
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:ResolutionDate` = `2026-03-03`
- XPath: `/TendererQualificationResponse/cbc:IssueDate` = `2026-03-03`
- XPath: `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09`
- XPath: `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cbc:Description` = `Appeals to the review board within ten days of the award.`
- Why: `PresentationPeriod` is "The period during which an appeal can be presented". The decision notified here is the qualification resolution of 2026-03-03, notified the same day; "within ten days" of it ends on 2026-03-13. The period given runs 2026-03-09 to 2026-03-19, exactly the appeal period of the award decision (23), which was taken six days after this document was issued: a date the sender could not know, and for six days no appeal against "the decision" could be presented. Text and dates of the same aggregate contradict each other. The call for tenders allows appeals only "within ten days of the award", so whether a qualification decision can be appealed on its own is a question of the world's procurement law (context).
- Condition: Text and period describe the same appeal: either a period from the qualification decision (2026-03-03 to 2026-03-13), or the text says the appeal lies against the award and gives no dates unknown on 2026-03-03.
- Options: (a) period 2026-03-03 to 2026-03-13 (preferred by broad, logistics, context); (b) only a `DurationMeasure` of 10 DAY, as in the call; (c) if only the award can be appealed, say so and leave the period out (or drop AppealTerms, see F8).
- Needs decision: yes
- From: broad (Medium), logistics (High), context (High, needs decision yes)

### tender/20#F2 · Medium · Language code in LocaleCode
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID` and names no locale; the Urvanian parties carry none. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred by parties and context); (b) a locale such as `en-XB` from a locale list (preferred by broad).
- Needs decision: no
- From: broad, parties, context

### tender/20#F3 · Medium · Province in Region
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country" that `CountrySubentity` holds, as the Bayvarran addresses of the same document do (`Coastal State`). 219 occurrences in 104 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: The province is in `CountrySubentity`; `Region` is absent or holds a region in its sense.
- Options: (a) move it to `CountrySubentity` (preferred); (b) if Urvania's address format has no administrative level and the value is a postal region only, state that in the world's address rules (parties).
- Needs decision: no
- From: broad, parties, context

### tender/20#F4 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The sender is a city department (ISIC 8411). A liquidation status ("Active, not in liquidation") has no meaning for it, and a scheme of type `COMMERCIAL` ("A register of businesses") does not fit a public body; the register number itself is not questioned (parties). Same in all examples of the flow.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type (preferred); (b) reduce the legal entity to registration name and identifier.
- Needs decision: no
- From: broad, parties, context

### tender/20#F5 · Low · Master data of the receiver that the notification does not use, and its order desk as contact
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- Why: The document tells Valdara it is admitted. The department describes the receiver with its logistics service provider (Castrano, whose key account desk has no means of contact), its share capital, its stock exchange listing and the mobile number of its order desk; none of this bears on the notification (section 4.8; the block is in all 22 full descriptions of Valdara in the flow, parties). The contact is the sales order desk, which handles orders; a qualification decision goes to whoever handles the tender. Counter-arguments (parties, refuted): share capital and listing describe the party as a legal entity; and Valdara itself gives the order desk as its contact in 13 and 15, so the department answers the contact it was given. The merge keeps them, as 15 and 16: the listing and capital were inputs of the qualification, not of its notification, and the unfit contact is Valdara's master data in every role.
- Condition: The receiver carries what the notification needs (identification, name, address, a contact that handles tenders, electronic address); service providers, securities and capital only where a document uses them.
- Options: (a) reduce the receiver to what the notification needs and give Valdara a tender contact (preferred); (b) keep the full party data everywhere and record that as a world rule.
- Needs decision: no
- From: broad, parties (service provider only; listing, capital and contact refuted), context

### tender/20#F6 · Low · The review board as information party, receiver and mediator of the appeal, without any means of contact
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: `MediationParty` is "The Party who mediates any appeal", `AppealReceiverParty` "The Party who receives the appeal". Mediation is an attempt to settle before or instead of the decision, by someone other than the deciding body; the description names one step only ("goes to the review board"), and nothing in the flow says the board mediates. The same board in all three slots looks filled because the roles exist (the same in 02). Whether Bayvarra's procurement law has a mediation stage is a story question.
- Condition: `MediationParty` is present only if the procedure has mediation, with the body that mediates; `AppealInformationParty` only where it adds something to the receiver.
- Options: (a) keep `AppealReceiverParty` only (preferred); (b) name a separate mediation body and describe the step.
- Needs decision: yes
- From: broad, parties, context

### tender/20#F7 · Low · The party to appeal to cannot be reached from this document
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PostalAddress/cbc:StreetName` = `Justice Row`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:ElectronicMail` = `registry@review-xb.example`
- Why: The receiver of appeals is given by register number and name only, while the notices describe the same board in full (21). A recipient with only this document cannot lodge the appeal from it; Low because the board can be looked up by its number.
- Condition: The appeal receiver carries at least a postal or electronic address, as in the notices (if the appeal terms stay, F8).
- Options: (a) describe the receiver as in 21 (preferred); (b) at least its electronic address and contact.
- Needs decision: no
- From: parties, broad (in its mediator finding)

### tender/20#F8 · Low · Appeal terms in a notification that admits the receiver to everything
- XPath: `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:AdmissionCode` = `ADMITTED`
- XPath: `/TendererQualificationResponse/cac:QualificationResolution[2]/cbc:AdmissionCode` = `ADMITTED`
- XPath: `/TendererQualificationResponse/cbc:Note` = `Qualified for both lots.`
- Why: An appeal is a remedy against an adverse decision; the receiver is admitted to both lots and is the only addressee, so it has nothing to appeal against. The appeal terms have a use in a notification that excludes the operator (none exists in the flow, see "Outside this review"), or as a standard legal notice.
- Condition: Appeal terms are present only where the receiver can appeal the notified decision, or the text says against which decision it may appeal.
- Options: (a) remove the appeal terms here (preferred); (b) keep them as a standard notice, with dates that fit (F1).
- Needs decision: yes
- From: context

### tender/20#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax": the party's status. The text begins "Sale to a public body", a transaction. Counter-argument (broad, refuted): the text states the status (second half). The merge keeps it, as in 15–19; the code itself fits (list description: a public body "buys free of sales tax"), parties would prefer a status code. A qualification notification has no tax content, so the tax scheme is also copied master data.
- Condition: The party's exemption reason states its status only.
- Options: (a) reword the text, keeping the code (preferred); (b) a party-status code; (c) leave the tax scheme out of this document.
- Needs decision: no
- From: parties (broad refuted it; context listed it under "Outside this review")

### tender/20#F10 · Low · Italian text tagged English, and en-XB here against en-XU in Valdara's own documents
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The second rendering of Valdara's street and city is tagged `en-XB` here and `en-XU` in the documents Valdara issues (13), with identical text; one of the tags cannot describe the text, it follows the issuer's country (`en-XB` in 13 examples of the flow, `en-XU` in 9, parties). The text is Italian. Counter-argument (broad, refuted): the world's English names for Urvanian places are Italianate throughout, accepted as exonyms. No convention is stated; aligned with the earlier flows (Low, decision).
- Condition: One recorded rule for these renderings and their tags, applied in every example.
- Options: (a) tag by what the text is (`en-XU`) everywhere (preferred by parties); (b) keep the issuer-dependent tag and record the rule.
- Needs decision: yes
- From: parties (broad refuted the Italian half)

### tender/20#F11 · Low · Valdara's legal form in one untagged rendering
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`
- Why: Here the legal form occurs once, without `languageID` and without the Urvanian text, while the address beside it is in both languages, tagged, and Valdara's own documents give the legal form twice (13). Split from parties/F5, as the earlier flows treat it separately.
- Condition: The legal form is rendered like the address (both renderings, tagged).
- Options: (a) both renderings, tagged (preferred); (b) at least tag the single rendering.
- Needs decision: no
- From: parties

### tender/20#F12 · Low · Minutes reference with only an ID
- XPath: `/TendererQualificationResponse/cac:ResolutionDocumentReference/cbc:ID` = `PWD-MIN-QUAL-26`
- Why: "A document (e.g., meeting minutes) relating to consideration of tenderer qualifications." The element name gives the kind, but nothing ties the minutes to the session of 2026-03-03 10:00 (no date, no description), and no other example mentions them. Broad and context only refuted that the minutes are not an example of the flow, which this finding does not claim.
- Condition: The reference carries at least the date of the minutes, agreeing with the resolution date.
- Options: (a) add `cbc:IssueDate` 2026-03-03 and a document type (preferred); (b) leave as is.
- Needs decision: no
- From: logistics

## Checked and consistent
- No identifiers with check digits apart from the ISIN `XU0001042501` (check digit correct, `check_ids.py`).
- Resolutions 2026-03-03 10:00 precede the issue 15:09, follow the opening (2026-02-26 14:00) and Valdara's qualification (13, 2026-02-25), and precede the award (2026-03-09).
- Two resolutions, LOT-1 and LOT-2, both `ADMITTED`, agree with "Qualified for both lots."; the remark on the installers matches lot 2, the required installers' curricula and Saltmere as Valdara's subcontractor (13, 15).
- Sender is the contracting department, receiver the tenderer of 13 and 15, signature the sender's; folder and contract name as in the flow.
- Parties: register numbers the same throughout the flow (department 20410548 in 36 examples, Valdara XU-R-104274 in 23, Castrano XU-R-104411 in 22, review board 20410822 in 7); `CompanyID` = `PartyIdentification`, electronic address and tax scheme consistent (parties, by script).

## Considered and refuted
- `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: "Via delle Officine" tagged English — refuted as the world's Italianate exonym (from broad; the merge carries the question as F10).
- `/TendererQualificationResponse/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: a transaction, not a status — refuted, the text states the status (from broad; the merge keeps F9).
- `/TendererQualificationResponse/cac:ResolutionDocumentReference/cbc:ID`: not an example of the flow — refuted, internal minutes, not a UBL document (from broad, context).
- `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:AdmissionCode`: the definition speaks of an indicator — refuted, a code in the model and `ADMITTED` is unambiguous (from broad, context).
- `/TendererQualificationResponse/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD 0990 real — refuted from knowledge of the ICD list (from broad, parties).
- `/TendererQualificationResponse/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` malformed — refuted (from parties).
- `/TendererQualificationResponse/cac:SenderParty/cac:Contact/cbc:Telephone`: +999 real — refuted, unassigned (from parties).
- `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: master data not used — refuted for the parties lens, part of the legal entity; ISIN check digit correct and `XU` no real prefix (from parties; the merge keeps the presence question in F5).
- `/TendererQualificationResponse/cac:ReceiverParty/cac:Contact/cbc:Name`: order desk for a qualification decision — refuted, Valdara gave this contact itself (from parties; the merge keeps it in F5).
- `/TendererQualificationResponse/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name`: wrong party for "presents the information for the appeal" — refuted, the board informs about the procedure in every notice (from parties; its redundancy is in F6).
- `/TendererQualificationResponse`: no reference to the qualification it answers — refuted, the document type has no element for it (from logistics).
- `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:ResolutionTime`: qualification decided after the opening — refuted, usual in an open procedure (from logistics).
- `/TendererQualificationResponse/cbc:ContractName`: definition speaks of a tender — refuted, the procurement's title (from context).

## Changed in the merge
- broad/F1 (Medium/no), logistics/F1 (High/no), context/F1 (High/yes) → F1: High/yes (text and period contradict; the dates lie after the issue date; whether the qualification can be appealed at all is the world's law).
- broad/F6, parties/F4, context/F6 → F4: raised to Medium, as analysis/review-merge-decisions.md and the other tender merges.
- broad/F5, parties/F6, context/F7 → F5: one master-data finding, with the contact (broad) added; parties' refutations carried.
- broad/F4, parties/F8, context/F4 → F6; parties/F7 kept apart as F7 (reachability, needs decision no).
- parties/F5 split into F10 (tags, Low/yes) and F11 (untagged legal form, Low/no), as the earlier flows.

## Outside this review
- No qualification response to Brackenmere exists in the flow, although its tender (19) was evaluated and ranked second (23) (from broad, logistics).
