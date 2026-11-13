# LLM review: 04-CallForTenders.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/04-CallForTenders.xml`, Git blob `d85d67fe6e23e20c10bbcd75651acb9959a75e3e` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 219a684 2026-11-12 Reviews of the road flow, run 20261112T2311Z-thorough: merge complete
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
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is a language code, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples`, and `grep -rl` for the file count).
- Condition: no `cbc:LocaleCode` holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since none of these documents needs a locale beyond the language; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID.
- Needs decision: no

### contest/04#F2 · Low · Public bodies described as companies in a commercial register
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the public bodies of this example (Lumeport Public Works Department, Procurement Review Board of Bayvarra) are registered in the `Federal business register of Bayvarra` with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"). UBL defines `Corporate Registration Scheme` as "The corporate registration scheme used to register the party" and the liquidation status as "the party's liquidation status". A department of the city, a national information service and a review board are not companies in a commercial register and cannot go into liquidation (the contracting party describes itself as "a department of the city of Lumeport" in `cac:ContractingPartyType/cbc:PartyType` where present). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for a register of public bodies, so the value is forced.
- Condition: no public body carries `CorporateRegistrationTypeCode` `COMMERCIAL` or a `CompanyLiquidationStatusCode`; if a registration scheme is given for a public body, its type says what kind of register it is.
- Options: (preferred) leave the registration type and the liquidation status out for public bodies and keep only the identifier of the register they are in; or add a public-sector register type to the list. The choice is about how the world registers public bodies, which is why it needs a decision.
- Needs decision: yes

### contest/04#F3 · Low · Customs and tax data of the contracting authority that the document does not use
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: this document belongs to a design contest; it declares no goods to customs and states no tax. The contracting authority's customs-trader number and its `PartyTaxScheme` look copied from its master data. In addition, `ExemptionReason` is defined as "A reason for the party's exemption from tax"; the code chosen means "Sale to a public body", which describes a transaction, not the status of the party, and this document records no sale.
- Condition: the contracting authority carries a customs-trader identifier and a `PartyTaxScheme` only where the document uses them; where a tax exemption of the party is stated, it is the party's own status.
- Options: (preferred) leave both out of the tendering documents; or, if the tax data stays, word the exemption reason as the party's status (a public body exempt from the state sales tax).
- Needs decision: no

### contest/04#F4 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: a contact is "The primary contact for this party" in its role in this document. Here Brackenmere Furniture takes part in a design contest through its trade-sales desk (`Customer service officer`, department `Sales`), while its partner Saltmere Engineering, where present, uses a bids office; the Procurement Review Board's registry, which receives appeals, is staffed by a `Procurement officer` of a `Procurement` department, the function of a buyer, not of the body that reviews buyers. The contacts look taken from the parties' trading master data.
- Condition: each contact named in this example is one that handles the party's role in the contest (tenders and competitions for a participant, appeals for the review board).
- Options: (preferred) give each party a contact for its role (e.g. a tenders or design office for the participants, a registry clerk or case officer for the review board); or leave the contact out where the role needs none.
- Needs decision: no

### contest/04#F5 · Low · Addressed to one participant before the selection
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/CallForTenders/cbc:IssueDate` = `2026-03-20`
- Why: the contest is restricted: "requests to participate, then designs from three to five selected participants" (`03-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cbc:Description` = `A restricted design contest in two stages…`). This document is addressed to Brackenmere Furniture alone on 2026-03-20, the day after the contract notice, twelve days before Brackenmere asked to participate (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:IssueDate` = `2026-04-01`) and before any selection (the register extracts used for it are dated May, `13-BusinessInformation.xml:/BusinessInformation/cbc:IssueDate` = `2026-05-05`). How the department knew Brackenmere as a candidate at that point is not visible in the flow; if the document is the general procurement document made available to all interested parties, a single named receiver does not fit it.
- Condition: the receiver and the date of this document agree with the two-stage procedure: either it is addressed to a party known as a candidate at its issue date, or it is the general document without a single named receiver.
- Options: (preferred) leave out the named receiver, or move the issue date after the point where Brackenmere registered its interest; or add the step in the story by which Brackenmere became a candidate. Which way the story goes is a decision.
- Needs decision: yes

### contest/04#F6 · Low · References to the brief and site plan carry only an identifier, and only the prior information notice is referenced
- XPath: `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-PROM-BRIEF`
- XPath: `/CallForTenders/cac:ProvidedDocumentReference/cbc:ID` = `PWD-PROM-SITE-PLAN-A`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`
- XPath: `/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`
- Why: the `Note` announces "the brief, the site plan and the rules of the contest". The brief and the site plan are referenced by an internal identifier only, with no document type, description or attachment, and the rules of the contest are not referenced at all. The only notice referenced is `LPWD-DOC-26-0633`, the prior information notice (`01-PriorInformationNotice.xml`, `02-PriorInformationNotice.xml`), not the contract notice `LPWD-DOC-26-0634` (`03-ContractNotice.xml`, `08-ContractNotice.xml`) that opened the contest and was published the day before (or the same day for version 2); `NoticeDocumentReference` is "A reference to a notice pertaining to this tendering process", and the contract notice is the one that does.
- Condition: every document the call announces is referenced and says what it is; the contract notice of the contest is among the referenced notices.
- Options: (preferred) add a `DocumentTypeCode` or `DocumentDescription` to the brief and site-plan references, a reference for the rules, and a `NoticeDocumentReference` to `LPWD-DOC-26-0634`; or drop "the rules" from the note if they are part of the brief.
- Needs decision: no

## Checked and consistent
- Prizes 8,000 + 4,000 + 2,000 lume and the text "Three prizes; the first is 8,000 lume" agree; the participation payment (1,000 lume) and the jury (five members) are the same in all notices and calls.
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company.
- Tendering terms, process and project agree value for value with the contract notice of the same date (`03-ContractNotice.xml`).
- Issue date 2026-03-20 is after the contract notice (2026-03-19) and before the request period ends (2026-04-18).
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files).

## Considered and refuted
- `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cbc:IndustryClassificationCode` = `8423`: suspected that "Public order and safety activities" does not fit a procurement review board — refuted because ISIC 8423 includes the administration of courts and the judicial system, and a review board deciding appeals is a quasi-judicial body (own knowledge of ISIC Rev.4).
- `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`: suspected that the indicator ("the number of candidates … has been reduced") cannot be true before the selection — refuted because the notice describes the procedure, which reduces the candidates to three to five by selection; read for the process, the value is correct.
- `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`: suspected that the estimate should have risen with the first prize (6,000 to 8,000 lume between the two versions of the prior information notice) — refuted because the flow does not say what the 54,000 lume consist of (prizes 14,000 + participation payments up to 5,000 leave about 35,000 for the follow-up contract); without a breakdown no arithmetic contradiction can be shown.
