# LLM review: 10-QualificationApplicationRequest.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/10-QualificationApplicationRequest.xml`, Git blob `5062e7029b9e54e815b6487b80aa0104eeade8e3` (committed)
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

### contest/10#F1 · Medium · FulfilmentIndicator in the buyer's request says the criterion has been fulfilled
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicator` = `true`
- Why: `TenderingCriterion/FulfilmentIndicator` is "An indication that this criterion has been fulfilled". This document is the buyer's request ("defining how the Exclusion Grounds and the Selection Criteria should be addressed"), issued before any operator answered; nothing has been fulfilled, and the buyer is not the party that declares fulfilment. Only the first of three criteria carries it, so it cannot be read as a flag of the request as a whole. Fulfilment is declared in the response (`11-QualificationApplicationResponse.xml`, `ResponseCode` `MET`). If "must be fulfilled" was meant, `EvaluationMethodTypeCode` `PASSFAIL` already says so.
- Condition: no criterion of the request states that it has been fulfilled.
- Options: (preferred) leave `FulfilmentIndicator` out of the request; or, if a "must be fulfilled" flag is wanted, use an element whose definition says so and record the gap.
- Needs decision: no
- From: broad (F2), context (F1)

### contest/10#F2 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code and repeats `Language/cbc:ID` (section 6: Medium). 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'` over `world/examples`, recounted in the merge).
- Condition: every `Language/LocaleCode` is absent or holds a locale (language and country or region) from a locale list named in its `listID`.
- Options: (preferred) leave `LocaleCode` out, since `Language/ID` already says English; or a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### contest/10#F3 · Medium · The contracting authority described as a company in a commercial register, with a liquidation status
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: Lumeport Public Works Department, a department of the city (ISIC 8411; "Local authority: a department of the city of Lumeport" in the call for tenders, `09-CallForTenders.xml:/CallForTenders/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType`), is entered in the "Federal business register of Bayvarra" as `COMMERCIAL` ("A register of businesses") and has a liquidation status. A city department is not a business and is not liquidated (section 5); it is not a legal person of its own either (parties). The world list has no type for a register of public bodies.
- Condition: no public body carries a `CompanyLiquidationStatusCode` or a registration scheme of the type "Commercial register".
- Options: (preferred) drop the liquidation status and the registration type for public bodies, keep the register name and identifier; or a public-sector register type in the list; or the City of Lumeport as the legal entity (a change of who the entity is).
- Needs decision: no
- From: broad (F3), parties (F1), context (F7)

### contest/10#F4 · Low · The economic operator's contact is a sales desk
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact of a contest participant handles the request to participate, the design and the jury's questions; Brackenmere gives its trade-sales desk, the contact for trade customers' orders (its partner Saltmere Engineering has a "Bids office" elsewhere in the flow). The contact is the party's general master-data contact.
- Condition: the economic operator's contact handles its part in the contest, with job title and department that agree.
- Options: (preferred) a bids or design office of the lead member; or no contact where the electronic address is the channel.
- Needs decision: no
- From: broad (F5), parties (F5), context (F3)

### contest/10#F5 · Low · Customs-trader number and tax registrations in a document that does nothing with them
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: section 4.8: data copied from master data. The request contains no amount, price, payment or tax (money searched for them), and no criterion refers to customs or tax. The customs-trader number serves customs declarations (55 files carry it: `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`); the contracting authority's sales-tax exemption matters for what it buys and pays, which this document does not do (money; unlike the call for tenders, this request carries no production limit or other amount the exemption could qualify). Context refuted the economic operator's tax registration: a qualification step may check a tenderer's tax registration as part of its identity. The merge keeps it in the finding: this request has no criterion (no exclusion ground on taxes, see F8) that asks for it, so nothing here uses it.
- Condition: the parties carry only identifiers and registrations that this document uses (e.g. a tax registration only where a criterion asks about taxes).
- Options: (preferred) leave them out of the qualification documents; keep the operator's tax registration if an exclusion ground on unpaid taxes is added (F8).
- Needs decision: no
- From: broad (F4), money (F1), parties (F4), logistics (F2), context (F6); context's refutation for the operator's registration carried above

### contest/10#F6 · Low · The party's tax exemption reason is worded as a sale
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax". The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is the buyer's status, so the code fits (money's refutation holds for the code); the text begins "Sale to a public body", a transaction, and only its second half states the status. Applies only if F5 keeps the tax scheme.
- Condition: where the exemption reason is stated, the text describes the party's status, not a sale.
- Options: (preferred) "Public body: exempt from the state sales tax", code kept; or a status code for public bodies.
- Needs decision: no
- From: broad (F4, part), parties (F3), context (F6, part)

### contest/10#F7 · Low · The coastal-site criterion asks a question that does not cover what it scores
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:Description` = `Whether one of the two references stands within one kilometre of the sea.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Description` = `The project, the client, the year and what the team designed.`
- Why: the criterion scores the distance of a reference from the sea, but its only property asks for "The project, the client, the year and what the team designed", word for word the question of the public-space criterion, without the site or its distance from the sea. Verified in the XML: the two properties `P-REF-PUBLIC-1` and `P-REF-COAST-1` have the same name and description.
- Condition: the coastal criterion asks for the site of the reference and its distance from the sea.
- Options: (preferred) add a property for the site (place, distance from the sea); or reword the existing property.
- Needs decision: no
- From: context (F4)

### contest/10#F8 · Low · No exclusion grounds in a request that defines how exclusion grounds are addressed
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:CriterionTypeCode` = `SUITABILITY`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:CriterionTypeCode` = `TECHNICAL`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:CriterionTypeCode` = `TECHNICAL`
- Why: the QualificationApplicationRequest is "A document issued by a buyer defining how the Exclusion Grounds and the Selection Criteria should be addressed". All three criteria are selection criteria; none is of the type `EXCLUSION` the world list offers ("A ground for excluding a tenderer"). The register extract later records "no exclusion grounds recorded" (`13-BusinessInformation.xml:/BusinessInformation/cbc:BriefDescription` = `Brackenmere Furniture: registered, no exclusion grounds recorded.`), so exclusion grounds exist in the world's procedure, but participants are never asked to declare them.
- Condition: the request contains the exclusion grounds that apply, or the world states that the register check replaces the self-declaration in a design contest.
- Options: (preferred) add one exclusion criterion (e.g. convictions or unpaid taxes) answered in the response; or record why the contest has none.
- Needs decision: yes
- From: context (F5)

### contest/10#F9 · Low · The request points to "the contest notice" without referring to it
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Description` = `The two completed designs of furniture or fittings for public spaces in the last five years that the contest notice asks for.`
- Why: the criteria repeat the requirements of the contract notice `LPWD-DOC-26-0634` (`03-ContractNotice.xml`, version 2 `08-ContractNotice.xml`, with a different design-lead requirement in each version), and the text points to "the contest notice", but the request has no document reference to it; the procurement is identified only by `ContractFolderID` and `ContractName`. Verified: the request contains no `DocumentReference` element.
- Condition: the request refers to the contract notice it implements.
- Options: (preferred) an `AdditionalDocumentReference` to `LPWD-DOC-26-0634` with a type saying it is the contract notice; or leave it implicit through `ContractFolderID` and drop the textual pointer.
- Needs decision: no
- From: logistics (F1)

### contest/10#F10 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID"; 1 January is a holiday and the same date is given for 25 companies (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, recounted), which points to a filler unless the world has a reason.
- Condition: Brackenmere's registration date has a reason in the world, or the element is absent.
- Options: (preferred) each company its own date; or leave it out; or record 1996-01-01 as an event in the story.
- Needs decision: yes
- From: parties (F6)

## Checked and consistent
- Weights 60 + 40 = 100 as `WeightScoringMethodologyNote` states; the professional qualification is pass/fail (broad, logistics, context).
- Criterion, group and property IDs are unique; the response refers to `CR-PROF` and `P-PROF-1`, which resolve here (broad, logistics).
- The criteria follow the contract notice of the same version (architect or registered industrial designer, CN v2; two references in five years) (broad, logistics, context).
- Codes (DESIGNCONTEST, REGULATED, WEIGHTED, SUITABILITY/TECHNICAL, PASSFAIL/WEIGHTED, ON, QUESTION, DESCRIPTION) are from the lists their `listID` names and fit their elements (logistics).
- Version chain: `VersionID` 2, `PreviousVersionID` 1, issued 2026-04-05 09:40, after CN v2 (08:19) (logistics).
- No amounts or financial criteria; Brackenmere's tax registration is the same throughout the flow (money).
- Parties identical across the flow; GLN check digit valid, GS1 prefix 952 reserved for demonstrations; +999 and `.example` not real (broad, parties).
- Physics: nothing to calculate (logistics).

## Considered and refuted
- `/QualificationApplicationRequest/cbc:IssueTime` = `09:40:00`: version 2 issued before the call for tenders of the same day (16:45) — refuted: the request follows CN v2 (08:19), not the call (from broad).
- `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:Description`: a criterion the contract notice does not state — refuted: it scores a property of the two references the notice asks for (from broad). Its property is a finding (F7).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: the code describes a transaction — refuted for the code by its list definition (from money); the text is F6.
- Missing financial-standing criterion — refuted: a design contest selects on references and professional qualification; nothing in the flow asks for financial standing (from money).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 too general — refuted (from parties).
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: "Procurement office" vs contact "Procurement" — refuted: the same unit (from parties).
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name`: a request addressed to a single operator — refuted: the questionnaire an interested operator obtains may name it (from parties).
- `/QualificationApplicationRequest/cbc:CustomizationID`: request and response sharing a customization — refuted: one customization per document pair throughout the world (from logistics).
- `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Name` = `The reference`: one property for two references — refuted: a response may give several values for one property (from context).
- `/QualificationApplicationRequest/cbc:QualificationApplicationTypeCode` = `REGULATED`: fits a procedure under the procurement rules (from context).
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: refuted by context as part of the operator's identity for the selection; the merge disagrees and keeps it in F5 with the argument.

## Changed in the merge
- broad/F3 (Low, yes), parties/F1 (Medium, yes), context/F7 (Low, no) → F3: Medium, needs decision no (meaning does not fit the party; aligned with the earlier flows).
- broad/F4, money/F1, parties/F4, logistics/F2, context/F6 → F5 (copied customs and tax data) and F6 (wording of the exemption reason, parties/F3).
- broad/F5, parties/F5, context/F3 → F4; `Department` line added.

## Outside this review
- The same party descriptions recur in the other flows that carry these parties; they belong to those examples' reviews (from parties).
