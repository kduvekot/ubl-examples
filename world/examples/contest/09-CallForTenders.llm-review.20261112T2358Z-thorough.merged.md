# LLM review: 09-CallForTenders.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/09-CallForTenders.xml`, Git blob `9f861a12870496547d09c98a4f266718a7a6d679` (committed)
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

### contest/09#F1 · Medium · Language code in LocaleCode
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language in a country or region (English as used in Bayvarra); `en` with `listID` `ISO 639` is the language code itself and repeats the sibling `cbc:ID`, so the element carries the language, not a locale (section 6 names "a language code in `LocaleCode`" as Medium). The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'` over `world/examples`, `grep -rl` for the files; recounted in the merge).
- Condition: every `Language/LocaleCode` in the example is absent or holds a locale (language and country or region) from a locale list named in its `listID`.
- Options: (preferred) leave `LocaleCode` out, because nothing in the document depends on a locale and `Language/ID` already says English; or a real locale (e.g. `en-XB` from BCP 47) with a matching `listID`.
- Needs decision: no
- From: broad, parties, context

### contest/09#F2 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: Lumeport Public Works Department (ISIC 8411) and the Procurement Review Board of Bayvarra (ISIC 8423) are registered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("the party's liquidation status"; code "Active, not in liquidation"). A city department and a review board are not businesses and are not wound up by liquidation (section 5); the same document calls the department "a department of the city of Lumeport", so the legal-entity data contradicts the party type next to it. A department is also not a legal person of its own (parties). The world list has no register type for public bodies (COMMERCIAL, CHARITY, ASSOCIATION, FARM), so the value is forced. The same description is carried by every occurrence of these parties (Public Works Department in 55 files, counted with `grep -rl --include='*.xml' XB-TR-410548 world/examples`).
- Condition: no public body in the example carries a `CompanyLiquidationStatusCode` or a registration scheme of the type "Commercial register"; if a registration scheme is given for a public body, its type says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep the register's name and identifier, because nothing in the story needs a register type for them; or add a public-sector register type to the world list; or give the City of Lumeport as the department's legal entity (a change of who the legal entity is, which would need a decision).
- Needs decision: no
- From: broad, parties, context

### contest/09#F3 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: a contact is "The primary contact for this party", here in its role in the contest. Brackenmere Furniture takes part through its trade-sales desk (a customer service officer in sales, the contact for trade customers' orders), while its consortium partner Saltmere Engineering is given a bids office elsewhere in the flow. The review board's registry, which receives appeals, is staffed by a "Procurement officer" of a "Procurement" department: the function of a buyer, not of the body that reviews buyers. The contacts are the parties' general master-data contacts.
- Condition: each contact in the example handles the party's part in the contest (tenders or competitions for the participant, the registry or appeals for the review board), with job title and department that agree with it.
- Options: (preferred) a bids or design office for Brackenmere and a registry clerk or case officer for the review board; or leave the contact out where the electronic address is the channel.
- Needs decision: no
- From: broad (F4), parties (F5), context (F5, F8; grouped in the merge)

### contest/09#F4 · Low · Customs-trader number and the economic operator's tax registration in a document that does nothing with them
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: section 4.8: data copied from a party's master data into a document that does not use it. The customs-trader identifier (scheme `urn:ubl-examples:world:XB:customs-trader`) serves the department's customs declarations (e.g. in the tender flow), not a design contest for a service; Brackenmere's state sales-tax registration serves its invoices. This call for tenders is not taxed, priced, invoiced, paid or declared, and nothing in it refers to either value. The customs number is in all 55 files that carry the department (`grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted).
- Condition: the parties in the example carry only identifiers and registrations that this document or its procedure uses.
- Options: (preferred) leave both out of the procurement documents; keep them where documents use them (customs, invoices).
- Needs decision: no
- From: broad (F3), money (F2), parties (F4), logistics (F3), context (F3)

### contest/09#F5 · Low · The contracting authority's tax scheme in a call for tenders without tax content
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: broad and context: the document states no tax, so the department's `PartyTaxScheme` looks copied from its master data (section 4.8). Money refuted this for the contracting authority: the call sets a production limit ("at most 900 lume a bench") and announces a follow-up service contract, and the buyer's exemption tells candidates that such amounts are net of the state sales tax. The merge cannot settle it: the exemption is a fact about the buyer that bidders may need for their prices, but the document does not say that its amounts are net, and the only amounts it carries (prizes, participation payments) are not supplies to the buyer.
- Condition: the contracting authority's tax scheme is in the document only if the document relies on it (e.g. a statement that amounts are net of the state sales tax), or it is absent.
- Options: (preferred) leave it out, and state "excluding state sales tax" with the production limit if that is what bidders need; or keep it and add that statement.
- Needs decision: yes
- From: broad (F3, part), context (F3, part); refuted by money (Considered and refuted)

### contest/09#F6 · Low · The party's tax exemption reason is worded as a sale
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", the party's own status. The code `PUBLIC` is named "Sale to a public body" in the Bayvarran list, but its definition ("A body of the federation, a state or a city buys free of sales tax") describes the buyer's status, so the code fits (money's refutation holds for the code). The text, however, begins "Sale to a public body", a transaction this document does not contain; only its second half states the status. Applies only if F5 keeps the tax scheme.
- Condition: where the contracting authority's exemption reason is stated, the text describes the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) "Public body: exempt from the state sales tax" with the code kept; or a status code for public bodies in the list.
- Needs decision: no
- From: broad (F3, part), parties (F3), context (F3, part); money refuted the code (carried below)

### contest/09#F7 · Low · The call does not refer to the contract notice it belongs to
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`
- Why: `NoticeDocumentReference` is "A reference to a notice pertaining to this tendering process". The only notice referenced is the prior information notice (`01-PriorInformationNotice.xml`, `02-PriorInformationNotice.xml`); the contract notice `LPWD-DOC-26-0634` that opened the competition and whose deadlines and qualification this call repeats (`03-ContractNotice.xml`, and as version 2 `08-ContractNotice.xml` of the same day, 08:19) is not referenced. The link is only implicit, through `ContractFolderID`. Verified: `LPWD-DOC-26-0634` occurs only in 03, 08, 15 and 16 (`grep -c` over `world/examples/contest/*.xml`).
- Condition: the call refers to the contract notice `LPWD-DOC-26-0634` (with or without the prior information notice).
- Options: (preferred) add a second `NoticeDocumentReference` to `LPWD-DOC-26-0634` and keep the PIN reference; or replace the PIN reference.
- Needs decision: no
- From: broad (F6, part), logistics (F1)

### contest/09#F8 · Low · The brief and the site plan are referenced by a bare identifier, and version 2 does not say what changed
- XPath: `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-PROM-BRIEF`
- XPath: `/CallForTenders/cac:ProvidedDocumentReference/cbc:ID` = `PWD-PROM-SITE-PLAN-B`
- XPath: `/CallForTenders/cbc:VersionID` = `2`
- Why: the two references carry only an identifier: no document type or description, no version or date, no attachment or URI, and neither resolves to an example (`flow_index.py`: `-> ?`), so a participant cannot tell from the document what they are or how to get them. Version 2 replaces `PWD-PROM-SITE-PLAN-A` (`04-CallForTenders.xml:/CallForTenders/cac:ProvidedDocumentReference/cbc:ID` = `PWD-PROM-SITE-PLAN-A`) by plan B without saying what changed, and keeps the brief's ID although the process justification says "The brief now states both limits". Context refuted the ID-only part: the `Note` ("The brief, the site plan and the rules of the contest.") says what the references are. The merge keeps the finding: the note names the documents in general but does not say which reference is which, nor where to get them.
- Condition: each reference says what the referenced document is (type code or description) and how it is obtained, and the change from site plan A to B can be read from the document.
- Options: (preferred) a `DocumentType` ("Design brief", "Site plan") and an attachment or URI on the buyer profile, plus a `DocumentDescription` or version on the site plan saying what changed; at least the type and a version or issue date.
- Needs decision: no
- From: broad (F6, part), logistics (F2); context refuted (counter-argument above)

### contest/09#F9 · Low · Requested legal form applies to the follow-up contract, not to the contest participants
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Limited company (private): a group of participants forms one before the follow-u…`
- Why: `TendererQualificationRequest/CompanyLegalFormCode` is "The legal status requested for potential tenderers". The code requests a private limited company, but the text says that for the contest itself a group only names a lead member and forms the company before the follow-up contract. Code and text describe different moments and different addressees.
- Condition: what the code requests and what the text says apply to the same tenderers at the same step.
- Options: (preferred) state the requirement for the follow-up contract in text only and drop the code, if participants need no legal form; or keep the code and word the text as a requirement on groups at the time of the contest.
- Needs decision: no
- From: context (F6)

### contest/09#F10 · Low · DurationPeriod of the reference criterion holds the look-back window
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cac:DurationPeriod/cbc:DurationMeasure` = `5`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Two completed designs of furniture or fittings for public spaces in the last five years.`
- Why: `EvaluationCriterion/DurationPeriod` "Describes the period for which the evaluation criterion is valid." The five years are the window in which the references must have been completed, not a period during which the criterion applies.
- Condition: the five-year window is stated where it means a reference window (the description already does), and `DurationPeriod`, if kept, is the criterion's validity.
- Options: (preferred) drop `DurationPeriod` and keep the window in the description; or keep it and record the reading as a note on the UBL definition.
- Needs decision: no
- From: context (F7)

### contest/09#F11 · Low · Estimated contract amount of 54,000 lume: what it covers is not stated, and it is unchanged after the first prize rose
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: `EstimatedOverallContractAmount` is "The estimated overall monetary amount of a contract". This is a services procurement (`SERVICES`, UN CPC 83912): prizes, participation payments and a follow-up design service contract. 54,000 is exactly 60 × the 900 lume production limit, which suggests the production cost of the benches, a supply this procedure does not award. Read as prizes, payments and follow-up contract (the usual valuation of a design contest, Directive 2014/24/EU Art. 78, own knowledge of money), it should have changed when the first prize rose from 6,000 (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`) to 8,000; it is 54,000 in every notice. Broad refuted the prize part: without a breakdown (prizes 14,000 + payments up to 5,000 leave 35,000 for the follow-up contract) no arithmetic contradiction can be shown. The merge agrees that nothing contradicts arithmetically, and keeps the finding for the unstated content.
- Condition: what the estimate covers can be read from the notice, and it is the value of what this procedure buys, consistent with the prizes of the same version.
- Options: (a, preferred) state what the estimate covers and adjust it in the version where the first prize rose; (b) if 54,000 is the production budget, remove it from `RequestedTenderTotal` and keep the per-bench limit in the description.
- Needs decision: yes
- From: money (F1); broad's refutation carried as counter-argument

### contest/09#F12 · Low · Addressed to one economic operator before the participants are selected
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/CallForTenders/cbc:IssueDate` = `2026-04-05`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-05-02`
- Why: the contest is restricted, "requests to participate, then designs from three to five selected participants" (`/CallForTenders/cac:TenderingProcess/cbc:Description`). The call is addressed to Brackenmere alone on 2026-04-05, before the requests to participate are due (2026-05-02) and before any selection (no document records it; the register extracts used for the checks are dated 2026-05-05, `13-BusinessInformation.xml:/BusinessInformation/cbc:IssueDate` = `2026-05-05`). If the call is the general set of contest documents, one named receiver is narrower than what it is; if it is the invitation to submit designs, it comes before the selection. Parties and logistics refuted it: in a restricted contest the documents are available to interested operators from the notice on, and Brackenmere is one that obtained them. Both readings are possible; which one the story means is a decision.
- Condition: the receiver and the date fit what the call is in this procedure: contest documents obtained by an interested operator (and the document says so), or an invitation to selected participants after the selection.
- Options: (preferred) keep Brackenmere as the receiver that obtained the documents and say in the document that they are available to all with the notice; or move the call after the selection and add the selection step to the flow.
- Needs decision: yes
- From: broad (F5), context (F2); refuted by parties and logistics (counter-argument above)

### contest/09#F13 · Low · CandidateReductionConstraintIndicator says the candidates have already been reduced
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`
- Why: UBL: "An indicator that the number of candidates participating in this process has been reduced (true) or not (false)." The call is issued before requests to participate are due, so no candidate has been dropped yet. Broad refuted it: read for the process, which reduces candidates to three to five by selection, `true` is correct; eForms uses the element in a notice for a procedure in successive stages (BT-52, own knowledge of the merge). Under the agreed rule of semantic conformance the definition ("has been reduced") prevails over that practice, so the finding stands; broad's reading is recorded as the counter-argument.
- Condition: the indicator states something true at the issue date, or the reading "the process reduces the number of candidates" is recorded as the world's interpretation of the definition.
- Options: (preferred) leave it out of the call, since `EconomicOperatorShortList` already states the limitation; or keep it and record the reading as a finding on the UBL definition.
- Needs decision: no
- From: context (F9, Low/no); broad refuted (counter-argument above)

### contest/09#F14 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday, and the same date is the registration date of 25 companies in all three countries (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'` over `world/examples`, recounted). That points to a filler (IND5), unless the world has a reason (e.g. a re-registration day under the Trade Accord).
- Condition: Brackenmere's registration date is a date with a reason in the world, or the element is absent.
- Options: (preferred) each company its own date from its history; or leave it out; or record 1996-01-01 as an event in the story.
- Needs decision: yes
- From: parties (F6)

## Checked and consistent
- Prizes 8,000 + 4,000 + 2,000 lume agree with `PrizeDescription` ("Three prizes; the first is 8,000 lume.") and with every version from 02 onwards (broad, money, context); payments of 1,000 lume to at most five participants: at most 5,000, prizes plus payments at most 19,000 lume (money, recomputed).
- Currency `XBL` is the currency of the contracting authority's tax scheme, and not assigned in ISO 4217 (money, own knowledge).
- Tendering terms, process and project agree with the contract notice of the same day (`08-ContractNotice.xml`: widened design-lead qualification, participation deadline 2026-05-02, submission 2026-06-12 12:00, short list 3/5/5) (broad, logistics, context).
- Version chain: `VersionID` 2, `PreviousVersionID` 1, same ID as `04-CallForTenders.xml`, issued after the CN v2 (logistics).
- Brackenmere's GLN `9523710900008`: check digit valid (`check_ids.py`); GS1 prefix 952 is reserved for demonstrations (broad, parties, logistics).
- Every party is described identically in every example of the flow that carries it; register ID, `CompanyID` and endpoint agree; tax jurisdiction matches the address; telephone numbers +999 and `.example` domains are not real (parties).
- `PreviousCancellationReasonCode` `UNSUITABLE` agrees with its text; the short list agrees with the process description; deadlines are after the issue date (context).
- Physics: no goods, packages, equipment or capacities; nothing to calculate (logistics).

## Considered and refuted
- `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cbc:IndustryClassificationCode` = `8423`: suspected not to fit a review board — refuted because ISIC 8423 includes the administration of courts and the judicial system, and the board is quasi-judicial (from broad).
- `/CallForTenders/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode` = `8411`: suspected too general for a works department — refuted: the department is part of the city's general administration (from parties).
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department` = `Procurement office`: against the contact department "Procurement" — refuted: the same unit, once as addressee, once as contact department (from parties).
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the code describes a transaction — refuted for the code: its list definition ("A body of the federation, a state or a city buys free of sales tax") is the buyer's status (from money). The wording of the text is kept as F6.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: suspected as copied master data — refuted by money (the exemption tells candidates that amounts are net); the merge could not settle it, so it is F5.
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[3]/cbc:Description`: a conditional third prize against "Three prizes" and `PrizeIndicator` true — refuted: a conditional third prize is an ordinary contest term (from money).
- `/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`: suspected that the rules lack a reference — refuted: the rules (awarding terms, prizes, jury, appeal, deadlines) are in this document itself (from logistics; broad had it as part of its F6, see Changed in the merge).
- `/CallForTenders/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: an aggregate for acting on behalf of a third party — refuted: the world list offers OWN and BEHALF, and stating OWN avoids implying it by absence (from context).
- `/CallForTenders/cac:TenderingProcess/cac:ProcessJustification/cbc:Description`: should justify the choice of procedure, not the relaunch — refuted: the aggregate also carries the reason a previous process was cancelled (from context).
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` and `BindingOnBuyerIndicator` = `true`: agree with the prize text (from context).
- `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`: a role in a request — refuted: the notice asks a group to name a lead member (from context).
- `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator`: refuted by broad; the merge disagrees and keeps it as F13 (Low).
- `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount`: the prize-change part refuted by broad; kept with money's finding as F11.
- `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name`: refuted by parties and logistics as documents available to interested operators; kept as F12 (needs decision) with that argument.
- `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID`: ID-only refuted by context; kept as F8 with the counter-argument.

## Changed in the merge
- broad/F1, parties/F2, context/F1 → F1: combined; wording from broad and parties.
- broad/F2 (Low, yes), parties/F1 (Medium, yes), context/F4 (Low, no) → F2: Medium, needs decision no, because the code carries a meaning that does not fit the party (section 6 Medium; aligned with customs-as-company in all earlier flows); the City-as-legal-entity idea of parties kept as an option.
- broad/F4, parties/F5, context/F5 and F8 → F3: grouped into one contact finding (section 3); added the receiver's `Department` line.
- broad/F3, money/F2, parties/F4, logistics/F3, context/F3 → split into F4 (customs number and economic operator's tax registration: all agree), F5 (contracting authority's tax scheme: money refuted, cannot settle, so Low/yes) and F6 (exemption wording: parties' finding, code part refuted by money).
- broad/F6 → split into F7 (contract notice not referenced, with logistics/F1) and F8 (ID-only brief and site plan, with logistics/F2); its "rules of the contest are not referenced" part moved to Considered and refuted, following logistics.
- context/F9 (Low, no) → F13: kept Low, needs decision no; broad's refutation and the eForms practice added as counter-argument (semantic conformance: the definition prevails).
- money/F1 → F11: broad's refutation added as counter-argument; severity and decision unchanged.
- broad/F5, context/F2 → F12: combined; parties' and logistics' refutations added as counter-argument.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01) recur in the other flows that carry these parties; they belong to those examples' reviews (from parties).
