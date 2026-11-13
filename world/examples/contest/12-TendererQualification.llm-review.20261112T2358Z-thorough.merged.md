# LLM review: 12-TendererQualification.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/12-TendererQualification.xml`, Git blob `0e1445bc31c9b97d2a3ad93650d9791482d0b7a0` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
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

### contest/12#F1 · Medium · One completed task declared where the contest asks for two references, one of them coastal
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Seating for the Lumeport central library's reading garden, 2024.`
- XPath: `08-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2`
- Why: the tenderer qualification is "A document declaring the qualifications of a tenderer", `CompletedTask` "A former task completed by this qualifying party". The contract notice requires "Two completed designs of furniture or fittings for public spaces in the last five years" (threshold 2), the request scores a second, coastal reference at 40 (`10-QualificationApplicationRequest.xml`), and "the jury selects the participants on their references". The team declares one completed task (Brackenmere, 2024; verified: one `CompletedTask` in the document) and none for the member Saltmere Engineering. The response (`11-QualificationApplicationResponse.xml`) does not give the references either, so no document of the flow carries a second reference, although the team is selected and wins the first prize (`15-ContractAwardNotice.xml`, `16-ContractAwardNotice.xml`). Not raised to High: the document need not list every qualification, so "fewer declared than required" is missing information rather than a statement that contradicts another.
- Condition: the qualifying parties together declare at least two completed tasks meeting the reference criterion (public-space furniture or fittings, within five years), one on a coastal site, or the flow states why one suffices.
- Options: (preferred) add a second `CompletedTask` (to Brackenmere or Saltmere) with period and description, one of the two by the sea; or record that the team was selected despite the threshold (a story change, unlikely).
- Needs decision: no
- From: broad (F2), logistics (F1), context (F2, Low)

### contest/12#F2 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code and repeats `Language/cbc:ID` (section 6: Medium). 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`, recounted).
- Condition: every `Language/LocaleCode` is absent or holds a locale from a locale list named in its `listID`.
- Options: (preferred) leave `LocaleCode` out; or a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### contest/12#F3 · Medium · The contracting authority described as a company in a commercial register, with a liquidation status
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Public Works Department, a city department (ISIC 8411), is entered as `COMMERCIAL` ("A register of businesses") and has a liquidation status; a city department is not a business, is not liquidated and is not a legal person of its own (section 5; parties). The world list has no register type for public bodies.
- Condition: no public body carries a `CompanyLiquidationStatusCode` or a registration scheme of the type "Commercial register".
- Options: (preferred) drop the liquidation status and the registration type for public bodies; or a public-sector register type; or the City of Lumeport as legal entity (a change of who the entity is).
- Needs decision: no
- From: broad (F3), parties (F1), context (F6)

### contest/12#F4 · Low · Contacts that do not fit the members' part in the contest
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: the lead gives its trade-sales desk, the contact for trade customers' orders, not the office that handles the contest. Saltmere's contact is named "Bids office", which fits, but is staffed by a "Procurement officer" of a "Procurement" department, the function that buys, not the one that prepares bids (parties). Both are the parties' general master-data contacts.
- Condition: each member's contact handles its part in the contest (bids or design), with job title and department that agree with the contact's name.
- Options: (preferred) a bids or design office for Brackenmere, and a bid manager or tenders officer in Saltmere's bids office; or no contact where the electronic address is the channel.
- Needs decision: no
- From: broad (F5), parties (F5), context (F4)

### contest/12#F5 · Low · BusinessIdentityEvidenceID holds the register number, and only for the lead
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID` = `20412466`
- Why: `QualifyingParty/BusinessIdentityEvidenceID` is "An identifier for an item of evidence to support the business identity of this qualifying party". The value is Brackenmere's register number, the identity itself, already given as `PartyLegalEntity/CompanyID` and `PartyIdentification/ID`; an item of evidence would be, e.g., a register extract. Saltmere has none, so the two members are treated differently without a reason. Broad and logistics refuted it: the register entry is the evidence of business identity, and its number with the register's `schemeID` is how it is identified and checked (as the extracts 13/14 do). The merge cannot settle it: that reading is possible, but then the element repeats an identifier the party already carries, and the member's identity is not evidenced at all.
- Condition: `BusinessIdentityEvidenceID` identifies an item of evidence for each qualifying party that gives one, or is absent.
- Options: (preferred) leave it out, since the register number is in the legal entity; or the identifier of an actual register extract (the flow's extract is issued later by the register, `13-BusinessInformation.xml`).
- Needs decision: yes
- From: parties (F7), context (F3); refuted by broad and logistics (counter-argument above)

### contest/12#F6 · Low · Saltmere Engineering's legal entity gives no legal form
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Saltmere Engineering`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Brackenmere Furniture Ltd`
- Why: `PartyLegalEntity/RegistrationName` is "The name of the party as registered with the relevant legal authority". Saltmere is in the commercial register, but its registered name has no legal-form suffix and its legal entity no `CompanyLegalFormCode`, while the lead is "Brackenmere Furniture Ltd" with `LTD`. In a group that must form a limited company before the follow-up contract (`09-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm`), the members' forms matter; Saltmere's registered name reads like a trading name.
- Condition: Saltmere's registered name and legal form are those of a registered business, described as other registered companies are.
- Options: (preferred) its registered name with legal form and `CompanyLegalFormCode`; or, if it is a sole trader or partnership in the world, say so in the legal form.
- Needs decision: no
- From: parties (F8)

### contest/12#F7 · Low · Customs-trader number and tax registrations in a document that does nothing with them
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1232055`
- Why: section 4.8. The document has no amounts, prices or payments (money searched for them) and declares no tax- or customs-related qualification. The customs number serves customs declarations (55 files carry it, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`); the authority's exemption serves what it buys. Context refuted the members' own tax registrations (a qualification step may check them); the merge keeps them in the finding, because nothing in this document (no exclusion ground on taxes, see `10-QualificationApplicationRequest.xml`) asks for them.
- Condition: the parties carry only identifiers and registrations the document uses.
- Options: (preferred) leave them out of the qualification documents; keep the members' tax registrations if a tax-related ground is added to the request.
- Needs decision: no
- From: broad (F4), money (F1), parties (F4), logistics (F2), context (F5)

### contest/12#F8 · Low · The party's tax exemption reason is worded as a sale
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the code's list definition ("A body of the federation, a state or a city buys free of sales tax") is the buyer's status and fits; the text begins "Sale to a public body", a transaction. Applies only if F7 keeps the tax scheme.
- Condition: where stated, the text describes the party's status, not a sale.
- Options: (preferred) "Public body: exempt from the state sales tax"; or a status code.
- Needs decision: no
- From: broad (F4, part), parties (F3), context (F5, part)

### contest/12#F9 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the same date for 25 companies (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, recounted), a holiday; a filler unless the world has a reason.
- Condition: Brackenmere's registration date has a reason in the world, or is absent.
- Options: (preferred) its own date; or leave it out; or record the date as a story event.
- Needs decision: yes
- From: parties (F6)

## Checked and consistent
- Participation 70 + 30 = 100 % (broad, money, parties, logistics, context, recomputed).
- Roles `LEAD`/`MEMBER` agree with the note ("The furniture maker leads the team") and with the notice's request that a group name a lead member (broad, logistics, context).
- The completed task (2024-03-01 to 2024-09-30) lies within the five-year window and agrees with the year in its description (broad, logistics, context).
- Identifiers: Brackenmere 20412466 (GLN check digit valid, prefix 952 reserved), Saltmere 20410685 with endpoint and address in Upland State; described the same in 07 and 12 (broad, parties, logistics, money).
- Version chain: `VersionID` 2, same ID as `07-TendererQualification.xml`; only the participation shares change (logistics).
- Physics: nothing to calculate (logistics).

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`: refuted by broad and logistics (the register entry is the evidence); kept as F5 (Low) with that argument.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`: a conflict with the notices' `EconomicOperatorRoleCode` list — refuted: separate world lists sharing LEAD and MEMBER with the same meaning (from broad).
- `/TendererQualification/cbc:Note` = `The furniture maker leads the team; the engineering firm does the structure and the anchoring.`: a contradiction with the design lead "of Saltmere Engineering" of version 1 — refuted: consortium lead and design lead are different roles; in version 2 the new design lead is not assigned to Saltmere, and its 30 % share fits structure and anchoring (from broad and context).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent`: should match a split of prize money or fees — refuted: no such split is stated; the percentage is the share in the group (from money).
- `/TendererQualification/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 too general — refuted (from parties).
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: address vs contact department — refuted: the same unit (from parties).
- `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cbc:IndustryClassificationCode` = `4290`: should be engineering services (7110) — refuted: Saltmere is a civil engineering contractor in other flows, and the code is the party's main activity, not its share in this team (from parties and context).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: refuted by context (part of the operator's identity); the merge disagrees and keeps it in F7.

## Changed in the merge
- broad/F2 (Medium), logistics/F1 (Medium), context/F2 (Low) → F1: Medium, because the selection on references depends on the missing information (section 6); not High, see Why.
- broad/F3 (Low, yes), parties/F1 (Medium, yes), context/F6 (Low, no) → F3: Medium, needs decision no (aligned with the earlier flows).
- broad/F5, parties/F5, context/F4 → F4: grouped; Saltmere's "Bids office" name added to the Why, since it fits and only job title and department do not.
- parties/F7, context/F3 (Low, no) → F5: combined; broad's and logistics' refutations added; needs decision yes, because the merge cannot settle which reading holds (aligned with merger A for 07).
- broad/F4, money/F1, parties/F4, logistics/F2, context/F5 → F7 and F8 (wording of the exemption, parties/F3).

## Outside this review
- Version 2 of the tenderer qualification (09:52) is issued before version 2 of the response (`11-QualificationApplicationResponse.xml`, 14:18) on the same day; harmless in itself, noted for the timeline review (from broad).
- The same party descriptions recur in the other flows that carry these parties; they belong to those examples' reviews (from parties).
