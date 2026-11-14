# LLM review: 20-TendererQualificationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/20-TendererQualificationResponse.xml`, Git blob `6cb54f8c8eae89a453504f165e001d727d6477c8` (committed)
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

### tender/20#F1 · Medium · The appeal period starts six days after the decision it is said to follow
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- Why: PresentationPeriod is "The period during which an appeal can be presented". The decision this document notifies was formalized on `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:ResolutionDate` = `2026-03-03` and notified the same day; "within ten days" of it ends on 2026-03-13. The period given instead runs for ten days from 2026-03-09, the day of the award notifications (22-AwardedNotification.xml and 23-UnawardedNotification.xml are issued 2026-03-09), a date that lies in the future of this document and belongs to another decision. Read literally, the qualification decision cannot be appealed during the first six days after it.
- Condition: the description and the presentation period describe the same appeal: either the period starts with this decision, or the text says the appeal is against the award and when that period starts.
- Options: (a) period 2026-03-03 to 2026-03-13 for an appeal against the qualification decision (preferred); (b) keep the dates and reword the description to the appeal against the award ("within ten days of the award", as in the call for tenders); (c) leave AppealTerms out of a notice of admission.
- Needs decision: no

### tender/20#F2 · Medium · Language code in LocaleCode
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of Language/ID and names no locale. Same pattern in 213 of the 250 examples (`grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`).
- Condition: LocaleCode, where present, identifies a locale and differs in kind from Language/ID.
- Options: (a) a locale (country or language-region tag; preferred); (b) leave it out.
- Needs decision: no

### tender/20#F3 · Medium · A province in Region
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a "political or administrative division of a country … such as the name of its county, province, or state", which is the definition of CountrySubentity. Valdara's address carries this value in every example of the flow that gives its postal address.
- Condition: the province of an Urvanian address is in CountrySubentity (with its code where the world has one), and Region is absent or holds a geographic or economic region.
- Options: (a) move the value to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/20#F4 · Low · The same board informs about, receives and mediates the appeal
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: MediationParty is "The Party who mediates any appeal"; mediation is an attempt to settle before or instead of the review, by someone other than the body that decides the appeal. Here the board that receives and decides the appeal is also the mediator, and none of the three carries an address or contact, so the document does not say how an appeal is lodged. The three identical entries look like one party copied into every slot.
- Condition: each appeal role that is present is held by a party that really has it, and the receiver of appeals can be reached (address, contact or electronic address).
- Options: (a) keep AppealReceiverParty with a contact, drop MediationParty unless the world has a mediation body (preferred); (b) name a separate mediator.
- Needs decision: yes (whether Bayvarra has mediation in procurement appeals is a story question)

### tender/20#F5 · Low · Master data of the receiver that this notice does not use
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- Why: the document tells Valdara that it is admitted. The authority describes the receiver with its logistics service provider, its share capital, its stock exchange listing and the mobile number of its order desk; none of this bears on the notification, and it is data the receiver holds about itself, not something the sender states. The contact is the sales order desk ("Customer service officer"), which handles orders, while a qualification decision goes to whoever submitted the tender. (Valdara's own tender names the same order desk: `15-Tender.xml:/Tender/cac:TendererParty/cac:Contact/cbc:Name` = `Order desk`, so the authority may simply answer to the contact it was given.)
- Condition: the receiver is identified and addressed with what the notification needs; service providers, securities and capital are present only in documents that use them.
- Options: (a) reduce the receiver to identification, name, address, contact and electronic address (preferred); (b) keep as is if the world's convention is to send full party data in every document, and record that as a rule.
- Needs decision: no

### tender/20#F6 · Low · The public works department described as a company in a commercial register
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the sender is a municipal department (ISIC 8411). It is not a company in a commercial register and has no liquidation status. Same description in every example of the flow that gives the department's legal entity.
- Condition: the department's legal entity carries only what applies to a public body, without a liquidation status and without a commercial-register type.
- Options: (a) drop the liquidation status and type the scheme as a register of public bodies (preferred); (b) drop CorporateRegistrationScheme for public bodies.
- Needs decision: no

## Checked and consistent
- Lots LOT-1 and LOT-2 exist in 03-CallForTenders.xml; both resolutions say ADMITTED and the note "Qualified for both lots." agrees; the remark on the installers matches lot 2 (installation) and Valdara's qualification with Saltmere as subcontractor (13).
- Resolution 2026-03-03 10:00 precedes the issue time 2026-03-03 15:09, and both follow the tender deadline 2026-02-26 12:00 (03).
- Sender and receiver are the contracting authority and the tenderer of 15-Tender.xml; Valdara's identifiers (XU-R-104274, tax number, ISIN) are the same as in 13 and 15.
- check_ids.py: ISIN XU0001042501 has a correct check digit.

## Considered and refuted
- `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: "Via delle Officine" tagged `en-XB` is not English — refuted because the world's English-language names for Urvanian places are Italianate throughout (Ferrano, Castrano); accepted as the fictional exonym.
- `/TendererQualificationResponse/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: "Sale to a public body" is a transaction, not the party's status — refuted because the text states the party's status (public bodies are exempt).
- `/TendererQualificationResponse/cac:ResolutionDocumentReference/cbc:ID`: PWD-MIN-QUAL-26 is no example of the flow — refuted because it is the authority's internal minutes ("e.g., meeting minutes"), not a UBL document.
- `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:AdmissionCode`: the definition speaks of an indicator (true/false) — refuted because the element is a code and ADMITTED is unambiguous.
- `/TendererQualificationResponse/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD 0990 could be a real ISO 6523 code — refuted from my knowledge of the ICD list, where 0990 is not assigned.

## Outside this review
- No qualification response to Brackenmere Furniture exists in the flow, although its tender (19) stayed in the procedure and it received an unawarded notification (23).
