# LLM review: 04-CallForTenders.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/04-CallForTenders.xml`, Git blob `d85d67fe6e23e20c10bbcd75651acb9959a75e3e` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 374ad95 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### contest/04#F1 · Medium · Language code in LocaleCode
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language as used in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is the ISO 639 language code itself, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale (section 6 names a language code in `LocaleCode` as Medium). Verified in the XML at every place listed. The same value occurs 362 times in 213 examples (recounted in the merge with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l` and `grep -rl` for the file count; a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also matches other `…LocaleCode` elements).
- Condition: No `cbc:LocaleCode` in the example holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since nothing in the document needs a locale beyond the language that `Language/cbc:ID` already gives; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID. Same as every earlier flow.
- Needs decision: no
- From: broad F1, parties F2, context F1

### contest/04#F2 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: The public bodies of this example (Lumeport Public Works Department, Procurement Review Board of Bayvarra) are entered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). A city department (and, where present, a federal information service or a review board) is not a business in a register of businesses and is not wound up by liquidation; the contracting party describes itself as "a department of the city of Lumeport" (`ContractingPartyType/PartyType`), and its ISIC class is 8411 (public administration). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no type for a register of public bodies, so the value is forced. Verified in the XML. The values carry a meaning that does not fit the party (Medium, as the customs authority described as a company in the earlier flows). Parties added that a city department is not a legal person at all; the legal entity behind it is the City of Lumeport.
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; a registration scheme given for a public body says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep only the register name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list; or give the City of Lumeport as the department's legal entity (this last option changes who the party is and would need a decision).
- Needs decision: no
- From: broad F2, parties F1, context F4

### contest/04#F3 · Low · The brief and the site plan are referred to by a bare identifier
- XPath: `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-PROM-BRIEF`
- XPath: `/CallForTenders/cac:ProvidedDocumentReference/cbc:ID` = `PWD-PROM-SITE-PLAN-A`
- XPath: `/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`
- Why: The call for tenders is "a document used by a Contracting Party to define a procurement project", and its Note and the contract notice ("The brief now states both limits") make the brief and the site plan the substance of what it defines. The two references carry only an identifier: no `DocumentTypeCode` or `DocumentType`, no version or issue date, no `Attachment` or external URI; neither resolves to an example (`flow_index.py`: `-> ?`). A participant cannot tell from the document what they are or how to obtain them, and the change of the site plan in the second call (`09-CallForTenders.xml`) cannot be traced. Counter-argument (context, which refuted it): the Note says what the two references are. It names them, but does not say which reference is which or where to get them. Broad's further point that the rules of the contest are not referenced is refuted (logistics): the rules (awarding terms, prizes, jury, appeal, deadlines) are in this document itself.
- Condition: Each of the two references says what the referenced document is (type or description) and how it is obtained (attachment or external reference).
- Options: (preferred) add `DocumentType` (e.g. "Design brief", "Site plan") and an `Attachment/ExternalReference/URI` on the buyer profile; or at least `DocumentType` and `VersionID`/`IssueDate`, so that the change between the versions is traceable.
- Needs decision: no
- From: broad F6 (part), logistics F2; refuted by context

### contest/04#F4 · Low · Customs and tax master data the procurement document does nothing with
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: `AdditionalPartyIdentification` is "One or more additional identifiers for this Party". The customs trader number (scheme `urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works Department towards customs and is used in its customs declarations (e.g. `tender/31-ImportCustomsDeclaration.xml`); this CallForTenders is a procurement document of a design contest for a service: nothing is imported, declared or transported, and nobody in the document uses the number. It is copied from the party's master data (section 4.8; the value is in 55 examples, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted in the merge). The same holds for the economic operators' own `PartyTaxScheme` ("A tax scheme applying to this party"): nothing in this document is taxed, priced, invoiced or paid, and no criterion refers to a tax registration (money). Counter-argument (context, in 05-07): a qualification step may check a tenderer's tax registration as part of its identity; the request of this flow, however, asks for no such check, so the argument does not give the value a use here.
- Condition: The contracting authority carries no customs trader identifier in this procurement document, and the economic operators carry a `PartyTaxScheme` only where the document uses it.
- Options: (preferred) leave these values out of the procurement documents and keep them where documents use them (customs declarations, invoices); or keep one only where the story gives this document a reason, and say so.
- Needs decision: no
- From: broad F3 (part), parties F4, logistics F3, context F3 (part), money F2

### contest/04#F5 · Low · Tax scheme of the contracting authority in a document that may not use it
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". The contracting authority brings its state sales tax registration and exemption into a procurement document. This document states amounts (prizes, participation payments, an estimated contract value, a production limit of 900 lume a bench) but no tax on them. Broad and context (and money from 05 on) read it as master data copied into a document that does not use it (section 4.8). Money (01-04, 08) refuted that: the buyer's exemption tells candidates that the amounts of the contest and of the follow-up contract are net of the state sales tax. Both readings are possible; the merge could not settle which the world intends.
- Condition: Either the authority's `PartyTaxScheme` is absent from this document, or the world states that procurement documents carry it to show that amounts are net of sales tax (and it is then carried consistently).
- Options: (preferred) leave it out of documents without amounts and decide for the notices whether the exemption is meant as information to candidates (then keep it and say so where amounts are given); or keep it everywhere as the buyer's tax status.
- Needs decision: yes
- From: broad F3 (part), context F3 (part); refuted by money

### contest/04#F6 · Low · Exemption reason of the contracting authority worded as a sale
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", i.e. the party's own status. The text begins "Sale to a public body", the name of the code in the Bayvarran exemption list (whose other codes are reasons for exempt supplies), and so describes a transaction; this document records no sale. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Money refuted the code itself, rightly: the list describes `PUBLIC` as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (verified in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`). What remains is the wording of the text. The same text is in 55 examples (`grep -rl --include='*.xml' 'Sale to a public body: public bodies' world/examples | wc -l`).
- Condition: Where the authority's exemption reason is stated, the text states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status ("Public body: exempt from the state sales tax") and keep the code; or add a status code for public bodies to the list.
- Needs decision: no
- From: broad F3 (part), parties F3, context F3 (part)

### contest/04#F7 · Low · Addressed to one participant before the selection
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/CallForTenders/cbc:IssueDate` = `2026-03-20`
- Why: The contest is restricted: "requests to participate, then designs from three to five selected participants" (`03-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cbc:Description` = `A restricted design contest in two stages…`). This call for tenders is addressed to Brackenmere Furniture alone on 2026-03-20, the day after the contract notice and twelve days before Brackenmere asks to participate (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:IssueDate` = `2026-04-01`); how the department knew Brackenmere as a candidate then is not visible in the flow. Counter-argument (logistics and parties, which refuted it): the procurement documents are available to interested operators from the notice on, and the named receiver is the operator that obtained them. Whether the flow should show that step is a story question.
- Condition: The receiver and the date of this document agree with the two-stage procedure: either it is addressed to a party known as interested at its issue date (and the flow shows how), or it is the general document without a single named receiver.
- Options: (preferred) say in the document (e.g. a `Note`) that it is the set of contest documents obtained by Brackenmere; or leave out the named receiver; or add the step by which Brackenmere registered its interest.
- Needs decision: yes
- From: broad F5, context F2; refuted by logistics and parties

### contest/04#F8 · Low · Registration date 1996-01-01 looks like a default, not the party's date
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday, and the same date is the registration date of 25 different companies in all three countries (271 occurrences in 181 files, recounted in the merge with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples`). That points to a filler (IND5) unless the world has a reason (e.g. one re-registration day), which the examples do not show.
- Condition: The registration date of Brackenmere Furniture is a date with a reason in the world, or the element is absent.
- Options: (preferred) give each company its own registration date from its history; or leave the element out where nothing uses it; or record a 1996 re-registration in the story. Same as every earlier flow.
- Needs decision: yes
- From: parties F6

### contest/04#F9 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: A contact is "The primary contact for this party" and should handle the party's part in this document (section 5). Brackenmere Furniture takes part in the contest through its "Trade sales" desk with a `Customer service officer` of the `Sales` department, the contact for trade customers' orders, not the office that handles a contest. The Procurement Review Board's "Registry", which receives appeals, is staffed by a `Procurement officer` of a `Procurement` department: the function of a buyer, not of the body that reviews buyers. The contacts are the parties' general contacts from the goods flows, the same in every example that carries these parties. Verified in the XML.
- Condition: Each contact in the example handles the party's part in the contest (requests to participate, designs and questions of the jury for a participant; appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a contact for their role (a bids or design office for the participants, a registry clerk or registrar for the review board); or leave the contact out where the electronic address is the channel.
- Needs decision: no
- From: broad F4, parties F5, context F5 and F8

### contest/04#F10 · Low · Requested legal form applies to the follow-up contract, not to the contest participants
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Limited company (private): a group of participants forms one before the follow-u…`
- Why: `TendererQualificationRequest. Company Legal Form Code` is "The legal status requested for potential tenderers". The code `LTD` requests a private limited company, while the text says that for the contest itself a group only names a lead member and forms the company before the follow-up contract is awarded (context). Counter-argument (broad, which refuted it): the text explains the code, and a legal form to be taken by a group before award is exactly the kind of requested legal status the element carries. Both readings are possible; the merge cannot settle it.
- Condition: What the code requests and what the text says apply to the same tenderers at the same step.
- Options: (preferred) keep the code and word the text as the requirement on groups ("a group forms a limited company before the follow-up contract is awarded"); or state the requirement for the follow-up contract in text only.
- Needs decision: yes
- From: context F6; refuted by broad (in 03)

### contest/04#F11 · Low · DurationPeriod of the reference criterion is the look-back window, not the criterion's validity
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Two completed designs of furniture or fittings for public spaces in the last five years.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cac:DurationPeriod/cbc:DurationMeasure` = `5`
- Why: `EvaluationCriterion. Duration_ Period` "Describes the period for which the evaluation criterion is valid" (verified in the model). The 5 years are the window in which the two reference designs must have been completed ("in the last five years"), not a period during which the criterion applies: a legitimate value in an element whose definition means something else (context).
- Condition: The five-year window is stated where it means a reference window (the Description already does), and `DurationPeriod`, if kept, gives the period for which the criterion is valid.
- Options: (preferred) keep the window in the Description and drop `DurationPeriod`; or keep it and record the reading as a finding on the UBL definition.
- Needs decision: no
- From: context F7

### contest/04#F12 · Low · CandidateReductionConstraintIndicator says the candidates have already been reduced
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`
- Why: UBL: "An indicator that the number of candidates participating in this process has been reduced (true) or not (false)". This document is issued before the requests to participate are due, so no candidate has been selected or dropped; what it announces is that the number will be limited, which the `EconomicOperatorShortList` already states (context). Counter-argument (broad, which refuted it): read for the procedure, the process does reduce the candidates to three to five. eForms maps its BT-52 "successive reduction" to this element (own knowledge), but under the semantic-conformance rule the definition decides; practice is context only.
- Condition: The indicator is absent from documents issued before any reduction, or its reading as "will be reduced" is recorded as a finding on the UBL definition.
- Options: (preferred) leave it out of the notice and the call (the short list carries the limitation); or keep it and record the reading for the TC write-up.
- Needs decision: no
- From: context F9; refuted by broad

### contest/04#F13 · Low · The call refers to the prior information notice but not to the contract notice
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`
- Why: `NoticeDocumentReference` is "A reference to a notice pertaining to this tendering process". The only notice referred to is `LPWD-DOC-26-0633`, the prior information notice (`01-PriorInformationNotice.xml`, `02-PriorInformationNotice.xml`); the contract notice `LPWD-DOC-26-0634` (`03-ContractNotice.xml`, issued 2026-03-19), which opened the contest and sets the deadlines and requirements this call repeats, is not referred to, although it exists before this document. The link is only implicit, through `ContractFolderID`. Verified in the XML.
- Condition: The call refers to the contract notice `LPWD-DOC-26-0634` (with or without the prior information notice).
- Options: (preferred) add a second `NoticeDocumentReference` with `LPWD-DOC-26-0634` and keep the PIN reference; or replace the PIN reference by the contract-notice reference.
- Needs decision: no
- From: broad F6 (part), logistics F1

### contest/04#F14 · Low · What the estimated contract amount of 54,000 lume covers is not stated
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: `RequestedTenderTotal` holds "Budget monetary amounts for the project as whole" and `EstimatedOverallContractAmount` is "The estimated overall monetary amount of a contract". The procurement is a design contest for services (`ProcurementTypeCode` `SERVICES`, UN CPC 83912): prizes, payments of 1,000 lume to each of at most five participants and a follow-up service contract. Nothing says what the 54,000 lume cover. The figure is exactly 60 × the production limit of 900 lume a bench in the project description (recalculated), which suggests the production cost of the benches, a contract this procurement does not award. Read instead as prizes, payments and follow-up contract (the usual way of valuing a design contest, money's own knowledge of Directive 2014/24/EU Art. 78), it should have changed when the first prize rose from 6,000 to 8,000 lume between the two versions of the prior information notice (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`, `02-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), while the estimate stayed at 54,000 in every notice. Counter-argument (broad, which refuted it): without a breakdown no arithmetic contradiction can be shown (prizes 14,000 or 16,000 and payments up to 5,000 leave room for a follow-up contract of about 35,000). The merge cannot settle what the figure is meant to be, hence Low with a decision. In this document the first prize is already 8,000 lume.
- Condition: The estimated overall contract amount is the estimated value of what this procurement buys (prizes, payments and/or the follow-up service contract), agrees with the prize amounts of the same version, and what it covers can be read from the notice.
- Options: (a, preferred) keep an estimate of prizes, payments and follow-up contract, say what it covers and adjust it with the prize change; (b) if 54,000 is the production budget, remove it from `RequestedTenderTotal` and keep the per-bench limit in the description.
- Needs decision: yes
- From: money F1; refuted by broad

## Checked and consistent
- Merge: every finding above was re-checked against the XML (values, positions, counts) and against the referenced examples; the definitions quoted were looked up in UBL-Entities-2.5.gc and the code meanings in `world/codelists/gc/`. The counts were redone over `*.xml` only.
- Prizes 8,000 + 4,000 + 2,000 lume and the text "Three prizes; the first is 8,000 lume" agree; the participation payment (1,000 lume) and the jury (five members) are the same in all notices and calls. (from broad)
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company. (from broad)
- Tendering terms, process and project agree value for value with the contract notice of the same date (`03-ContractNotice.xml`). (from broad)
- Issue date 2026-03-20 is after the contract notice (2026-03-19) and before the request period ends (2026-04-18). (from broad)
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). (from broad)
- Prizes: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`, second 4,000, third 2,000 lume; `PrizeDescription` ("Three prizes; the first is 8,000 lume.") agrees with the three `Prize` aggregates and their ranks. (from money)
- Currency: every amount is in `XBL` (Lume), the currency of the contracting authority's tax scheme (`TaxScheme/CurrencyCode` `XBL`). (from money)
- Payments to participants: 1,000 lume to each selected participant that submits a conforming design; with at most five participants (`EconomicOperatorShortList/MaximumQuantity` 5) the outlay is at most 5,000 lume, and prizes plus payments total at most 19,000 lume (calculated). (from money)
- The prize amounts equal those of every other version of the notices from 02 onwards (02, 03, 04, 08, 09 and the award notice 16), compared over `*.xml`. (from money)
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data). (from parties)
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address. (from parties)
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606). (from parties)
- Brackenmere's GLN 9523710900008 has a valid check digit (check_ids.py) and uses GS1 prefix 952, which GS1 reserves for demonstrations (own knowledge). (from parties)
- Deadlines and process data agree with the contract notice of the same date range: submission deadline 2026-06-12 12:00, participation deadline 2026-04-18 (CN v1, 03), short list 3/5/5, prizes 8,000 / 4,000 / 2,000 lume, design-lead requirement architect (03). (from logistics)
- Receiver identifiers: Brackenmere Furniture, register 20412466 (= PartyLegalEntity CompanyID and endpoint XB:20412466), GLN 9523710900008 (check digit correct, `check_ids.py`; GS1 prefix 952 is reserved for demonstrations and examples, so it cannot be mistaken for a real GLN), address UL-ADR-821551; the same in every example of the flow that carries the party. (from logistics)
- Codes: ProcedureCode DESIGNCONTEST, SubmissionMethodCode ELECTRONIC, EvaluationCriterionTypeCode REFERENCES, PrizeRankCode values, CPC 83912, ISIC 3100 for a furniture maker. (from logistics)
- `/CallForTenders/cbc:IssueDate` = `2026-03-20` follows the contract notice (2026-03-19) and lies before the participation deadline. (from logistics)
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against. (from logistics)
- Prize amounts: Prize[1] = `8000.00`, Prize[2] = 4000.00, Prize[3] = 2000.00 lume, matching the PrizeDescription ("the first is 8,000 lume") and version 2 of the PIN. (from context)
- The short list (minimum 3, expected and maximum 5) agrees with the process description ("three to five selected participants") and with `02-PriorInformationNotice.xml`. (from context)
- Dates: requests to participate due before designs (participation `2026-04-18`, designs 2026-06-12 12:00), both after the issue date. (from context)
- ProcessJustification: PreviousCancellationReasonCode `UNSUITABLE` ("No suitable tender") agrees with its text (both designs of the cancelled contest were unacceptable). (from context)
- The appeal terms name a receiver of appeals (the review board) and a time limit; the AppealTerms aggregate fits. (from context)

## Considered and refuted
- `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cbc:IndustryClassificationCode` = `8423`: suspected that "Public order and safety activities" does not fit a procurement review board — refuted because ISIC 8423 includes the administration of courts and the judicial system, and a review board deciding appeals is a quasi-judicial body (own knowledge of ISIC Rev.4). (from broad)
- `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`: suspected that the indicator ("the number of candidates … has been reduced") cannot be true before the selection — refuted because the notice describes the procedure, which reduces the candidates to three to five by selection; read for the process, the value is correct. (from broad) Not followed in the merge: kept as F12, with this argument recorded there as counter-argument.
- `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`: suspected that the estimate should have risen with the first prize (6,000 to 8,000 lume between the two versions of the prior information notice) — refuted because the flow does not say what the 54,000 lume consist of (prizes 14,000 + participation payments up to 5,000 leave about 35,000 for the follow-up contract); without a breakdown no arithmetic contradiction can be shown. (from broad) Not followed in the merge: kept as F14, with this argument recorded there as counter-argument.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction ("Sale to a public body") rather than the party's own status — refuted because the list defines the code as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer, and `ExemptionReason` says so ("public bodies are exempt from the state sales tax"). (from money) Accepted in the merge for the code; the wording of the text remains finding F6.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: suspected as master data copied into a notice without tax content — refuted because the notice sets a production limit of 900 lume a bench and announces a follow-up service contract; the buyer's exemption tells candidates that these amounts are net of the state sales tax. (from money) Not followed in the merge: kept as F5, with this argument recorded there as counter-argument.
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[3]/cbc:Description`: suspected that a third prize awarded only "if the jury finds it of prize standard" contradicts "Three prizes" and `PrizeIndicator` true — refuted because a conditional third prize is an ordinary contest term and the first two prizes are unconditional. (from money)
- `XBL` as currency: checked that it is not a code assigned in ISO 4217 (own knowledge: the assigned X-codes near it are XBA–XBD, bond-market units); it is the world's fictional Lume. (from money)
- `/CallForTenders/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better. (from parties)
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department. (from parties)
- `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name`: the call for tenders is addressed to Brackenmere Furniture before it applied (its application is of 2026-04-01) and before the jury selected participants — refuted as a party problem: in a restricted contest the brief and site plan are made available to interested operators from the notice on, and Brackenmere is one that asked for them; the receiver is the right kind of party for the role. (from parties) Not followed in the merge: kept as F7, with this argument recorded there as counter-argument.
- `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: suspected that a restricted contest should send the call only to selected participants, after the requests to participate — refuted: the procurement documents are available from the notice onwards, and the receiver is the operator that obtained them; the selection of participants concerns who may submit designs, not who may read the brief. (from logistics) Not followed in the merge: kept as F7, with this argument recorded there as counter-argument.
- `/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`: suspected that "the rules of the contest" lack a reference — refuted: the rules (awarding terms, prizes, jury, appeal, deadlines) are in this document itself. (from logistics)
- `/CallForTenders/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: suspected that an aggregate defined as "The type of represention empowering the party to act on behalf of a third party" does not belong to a party acting for itself — refuted because the world's list offers `OWN` and `BEHALF` as the two answers, and stating `OWN` explicitly avoids implying it by absence (IND6). (from context)
- `/CallForTenders/cac:TenderingProcess/cac:ProcessJustification/cbc:Description` = `Relaunch of the design contest PWD-2025-PROM-DC…`: suspected that a justification "for the selection of this tendering process" should explain the choice of a design contest rather than the relaunch — refuted: the aggregate also carries the reason a previous process was cancelled (PreviousCancellationReasonCode), and the text explains why the same procedure is run again. (from context)
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `true` and `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`: checked whether the indicators agree with their text — they do: the first prize says its author "is invited to negotiate the follow-up service contract", and nothing in the text makes the jury's ranking advisory. (from context)
- `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`: whether a role belongs in a qualification request — refuted: the notice asks a group to name a lead member, which is what the role states. (from context)
- `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-PROM-BRIEF`: a reference with an ID only — refuted for this lens: the Note ("The brief, the site plan and the rules of the contest") says what the two references are, and the rules are the call itself. (from context) Not followed in the merge: kept as F3, with this argument recorded there as counter-argument.
- `/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`: broad's sub-claim (part of its F6) that the rules of the contest are not referenced — refuted in the merge because the rules (awarding terms, prizes, jury, appeal terms, deadlines) are in this call itself, as logistics argued (from broad; refutation from logistics)

## Changed in the merge
- broad F2 + parties F1 + context F4 → one finding, Medium, Needs decision no (as in 01-03). The receiver Brackenmere is a company and is not part of it.
- broad F6 split into two findings (bare identifiers; missing contract-notice reference), merged with logistics F2 and F1; its sub-claim that the rules of the contest are not referenced is dropped from the condition, because the rules are in the call itself (logistics); see "Considered and refuted".
- broad F3, context F3 and money F2 regrouped: customs identifier + the receiver's tax scheme (money F2) in one finding (Low/no, aligned with merger B), the authority's tax scheme in its own (Low/yes, refuted by money), the wording in its own (Low/no).
- context F5 (sales desk) and F8 (registry) merged into the contacts finding of broad F4 / parties F5.
- broad F5 / context F2 (addressed to one participant) merged; Low/yes kept, with the refutations of logistics and parties as counter-argument.
- context F6 (requested legal form) Needs decision no → yes (broad refuted the same point in 03).
- Every finding merged from several parts keeps the clearest wording and all evidence; findings are numbered by severity and then by position in the document.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews. (from parties)
