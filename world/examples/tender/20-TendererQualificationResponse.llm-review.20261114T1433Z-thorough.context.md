# LLM review: 20-TendererQualificationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/20#F1 · High · The appeal period does not belong to the decision this document notifies
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:ResolutionDate` = `2026-03-03`
- Why: `PresentationPeriod` is "The period during which an appeal can be presented", and the text says the appeal against "the decision" must be made within ten days. The decision notified here is the qualification resolution of 2026-03-03 (issue date of the document the same day), so ten days run to 2026-03-13. The period given starts six days after the decision and ends sixteen days after it. It is exactly the appeal period of the award decision of 2026-03-09 (`23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:StartDate` = `2026-03-09`, `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`), a decision that did not exist yet when this document was issued. Text and period contradict each other.
- Condition: The appeal period starts on (or after notification of) the qualification resolution and ends ten days later, or the text states the period it actually means.
- Options: (a) preferred: 2026-03-03 to 2026-03-13; (b) if the law of the world only allows an appeal after the award (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cbc:Description` = `Appeals to the review board within ten days of the award.`), say so in the description and leave the period out, since its dates were not known on 2026-03-03.
- Needs decision: yes (whether a qualification decision can be appealed on its own)

### tender/20#F2 · Medium · A province in `Region`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/20#F3 · Medium · A language code as locale
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/20#F4 · Low · The review board is also the mediator and the source of appeal information
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/TendererQualificationResponse/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: `MediationParty` is "The Party who mediates any appeal", `AppealReceiverParty` "The Party who receives the appeal". Mediation is an attempt to settle a dispute before or instead of a decision, by someone other than the body that decides; the description names only one step ("goes to the review board"). The same board in all three roles tells the reader nothing beyond the receiver, and makes the deciding body its own mediator.
- Condition: `MediationParty` is present only if the world has a mediation step, with the body that mediates; `AppealInformationParty` only if it adds something to the receiver.
- Options: (a) preferred: keep `AppealReceiverParty` only; (b) name a real mediation body and describe the step.
- Needs decision: yes (whether the world has mediation in procurement appeals)

### tender/20#F5 · Low · Appeal terms in a notification that admits the receiver to everything
- XPath: `/TendererQualificationResponse/cac:AppealTerms`
- XPath: `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:AdmissionCode` = `ADMITTED`
- XPath: `/TendererQualificationResponse/cac:QualificationResolution[2]/cbc:AdmissionCode` = `ADMITTED`
- Why: The document tells Valdara Industries that it is admitted to both lots (`/TendererQualificationResponse/cbc:Note` = `Qualified for both lots.`). An appeal is a remedy against an adverse decision; the receiver has nothing to appeal against, and the document is addressed to it alone. The appeal terms have a use only in a notification that excludes the operator, at least for one lot.
- Condition: Appeal terms are present only where the notified decision can be appealed by the receiver, or the text says against which decision (e.g. the admission of competitors) the receiver may appeal.
- Options: (a) preferred: remove the appeal terms from this fully positive notification; (b) keep them as a standard legal notice, with dates that fit (F1).
- Needs decision: yes

### tender/20#F6 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TendererQualificationResponse/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/20#F7 · Low · Master data of a party that the document does not use
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/TendererQualificationResponse/cac:ReceiverParty/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The document only tells the receiver whether it is admitted; none of these plays a part in it (the listing and share capital were inputs of the qualification, not of its notification, and Castrano Logistics does nothing here). Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py`: ISIN XU0001042501 has a correct check digit.
- Note "Qualified for both lots." against two resolutions, one per lot (LOT-1, LOT-2), both `ADMITTED`; the lots exist in the call for tenders (park benches; installation).
- Resolution time 10:00 on 2026-03-03 precedes the issue time 15:09 the same day.
- The resolution for lot 2 mentions the installers: Valdara's tender names a subcontractor for the installation (Saltmere Engineering in `15-Tender.xml`).
- Sender is the contracting party, receiver the tenderer whose qualification (`13-TendererQualification.xml`) is decided; the signature is the sender's.

## Considered and refuted
- `/TendererQualificationResponse/cac:QualificationResolution[1]/cbc:AdmissionCode`: the definition speaks of an indicator (true/false) while the value is a code — refuted because the element is a code in the UBL 2.5 model and `ADMITTED` is in the world's list with the meaning "Admitted".
- `/TendererQualificationResponse/cac:ResolutionDocumentReference/cbc:ID`: minutes `PWD-MIN-QUAL-26` are no example of the flow — refuted for this lens because the element is defined for exactly such a document ("e.g., meeting minutes") which is not a UBL document.
- `/TendererQualificationResponse/cbc:ContractName`: its definition ("Short title of a contract associated with this Tender") speaks of a tender — refuted because the value is the title of the procurement, the same in every document of the flow.

## Outside this review
- The receiver's contact is the order desk of the sales department (`Customer service officer`), which is not who handles a qualification in a tender procedure; contacts against roles are the parties part's lens.
- The tax exemption reason of the sender ("Sale to a public body…") describes a transaction rather than the party's status; parties part.
