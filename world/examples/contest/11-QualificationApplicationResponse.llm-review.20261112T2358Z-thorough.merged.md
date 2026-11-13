# LLM review: 11-QualificationApplicationResponse.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/11-QualificationApplicationResponse.xml`, Git blob `786906485480cbed630ad927abbdceded6391e3d` (committed)
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

### contest/11#F1 · Medium · The two scored reference criteria of the request are not answered
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-PROF-1`
- XPath: `10-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-REF-PUBLIC`
- XPath: `10-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-REF-COAST`
- Why: the response is "a self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria", and its `TenderingCriterion` is the criterion "as described in the Qualification Application Request". The request has three criteria; this response repeats and answers only the pass/fail `CR-PROF`. The two criteria that carry the whole score (`CR-REF-PUBLIC` 60, `CR-REF-COAST` 40; properties `P-REF-PUBLIC-1`, `P-REF-COAST-1`), and on which "The jury selects the participants on their references." (`03-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cbc:LimitationDescription`), get no response. The tenderer qualification of the same team (`12-TendererQualification.xml`) does not fill the gap: it lists one completed task, not two references, and nothing on a coastal site. Verified in the XML: one `TenderingCriterion`, one `TenderingCriterionResponse`. The selection cannot be made from the documents of the flow, yet Brackenmere's team is selected and wins (`15-ContractAwardNotice.xml`).
- Condition: the response answers every criterion of the request, with responses validating `P-PROF-1`, `P-REF-PUBLIC-1` and `P-REF-COAST-1`, or states why a criterion is not answered.
- Options: (preferred) add the two criteria and their responses (project, client, year and what the team designed; one reference on a coastal site), consistent with the completed tasks of `12-TendererQualification.xml`; or answer them by reference to the tenderer qualification and say so; or make an incomplete response visible (e.g. a `NOTMET` response) if the story wants one.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### contest/11#F2 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code and repeats `Language/cbc:ID` (section 6: Medium). 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`, recounted).
- Condition: every `Language/LocaleCode` is absent or holds a locale from a locale list named in its `listID`.
- Options: (preferred) leave `LocaleCode` out; or a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### contest/11#F3 · Medium · The contracting authority described as a company in a commercial register, with a liquidation status
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Public Works Department, a department of the city (ISIC 8411), is entered as `COMMERCIAL` ("A register of businesses") and has a liquidation status; a city department is not a business, is not liquidated and is not a legal person of its own (section 5; parties). The world list has no register type for public bodies.
- Condition: no public body carries a `CompanyLiquidationStatusCode` or a registration scheme of the type "Commercial register".
- Options: (preferred) drop the liquidation status and the registration type for public bodies; or a public-sector register type; or the City of Lumeport as legal entity (a change of who the entity is).
- Needs decision: no
- From: broad (F3), parties (F1), context (F9)

### contest/11#F4 · Low · The group's lead role and its other member are not encoded
- XPath: `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: the response is made for a group, and the contest notice asks a group to name its lead (`03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`). `EconomicOperatorParty` has `EconomicOperatorRole` ("The role of the party in a tender consortium") and `QualifyingParty` for this, but carries only the `Party`: the response does not say that Brackenmere answers as lead, and Saltmere Engineering does not appear, although version 1 relied on its architect. The tenderer qualification names the roles (`12-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`). Broad and logistics refuted it: the group is named in `EconomicOperatorGroupName`, its composition is declared in the tenderer qualification, and the lead answers for the group. The merge keeps the finding at Low: the lead may answer for the group, but the document should then say it does so as lead, which is what the role element is for.
- Condition: the response states in structured form that Brackenmere answers as lead of the group (and, optionally, identifies the other member), consistent with the tenderer qualification.
- Options: (preferred) add `EconomicOperatorParty/EconomicOperatorRole` with `LEAD`; optionally a second `EconomicOperatorParty` for Saltmere Engineering with `MEMBER`.
- Needs decision: no
- From: parties (F7), context (F3); refuted by broad and logistics (counter-argument above)

### contest/11#F5 · Low · The new design lead is not attributed to a member of the group
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Ivo Harlan, is registered as an industrial designer, no. ID-2208, in the register of the Bayvarran Design Council.`
- Why: in version 2 the design lead changes to Ivo Harlan, a registered industrial designer, but the response does not say which member employs him; version 1 named "Edda Corwin of Saltmere Engineering" (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description`). The criterion is met through a member of the group; the change of the participation shares to 70/30 (`12-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `70`) suggests he is Brackenmere's, but no document says so. The new version also does not say what changed from version 1.
- Condition: the response says which member of the group the design lead belongs to.
- Options: (preferred) name his firm in the description, as version 1 did.
- Needs decision: yes
- From: parties (F8)

### contest/11#F6 · Low · The evidence is not linked to the response it supports and does not identify the certificate
- XPath: `/QualificationApplicationResponse/cac:Evidence/cbc:ID` = `EV-REG-LEAD`
- XPath: `/QualificationApplicationResponse/cac:Evidence/cbc:Name` = `Certificate of registration of the design lead`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ID` = `CRR-PROF`
- Why: the link from a response to its evidence is `TenderingCriterionResponse/SuppliedEvidence` ("A reference to the Evidence supporting this criterion property response"; the older `EvidenceSupplied` is deprecated in UBL 2.5, checked in the model). `CRR-PROF` has no such link, so `EV-REG-LEAD` is referred to by nothing; the evidence also has no document reference or issuing party (the Bayvarran Design Council named in the text).
- Condition: the response the certificate supports refers to `EV-REG-LEAD`, and the evidence identifies the certificate or its issuer.
- Options: (preferred) `SuppliedEvidence` with ID `EV-REG-LEAD` in `CRR-PROF`, and a `DocumentReference` or `EvidenceIssuingParty` on the evidence; or drop the evidence if the registration number in the text is enough.
- Needs decision: no
- From: broad (F6), logistics (F3), context (F4)

### contest/11#F7 · Low · The response does not refer to the request it answers
- XPath: `/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0637`
- Why: the response answers `LPWD-DOC-26-0636` (`10-QualificationApplicationRequest.xml`), which exists in two versions with different design-lead requirements, but carries no document reference to it; which version is answered can only be guessed from the issue dates. The link is only implicit, through `ContractFolderID`.
- Condition: the response identifies the request (and its version) it answers.
- Options: (preferred) an `AdditionalDocumentReference` to `LPWD-DOC-26-0636` with its `VersionID`; or leave it implicit.
- Needs decision: no
- From: logistics (F2)

### contest/11#F8 · Low · The same sentence as response description and as response value
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Ivo Harlan, is registered as an industrial designer, no. ID-220…`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `The design lead, Ivo Harlan, is registered as an industrial designer, no. ID-220…`
- Why: the value answers the property ("The register and the registration number of the design lead"); the response description repeats it word for word and adds nothing (IND5). Broad refuted it: the two elements have different definitions (the value of the property, and a description of the response), so repeating the text is harmless. The merge keeps it as a Low remark: harmless, but a value without its own reason.
- Condition: each text says something of its own, or only one is present.
- Options: (preferred) keep the sentence in the `ResponseValue` and drop the response `Description`; or let the description summarise and the value give register and number only.
- Needs decision: no
- From: context (F5); refuted by broad (counter-argument above)

### contest/11#F9 · Low · No self-declaration on exclusion grounds
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- Why: the response is defined as stating "that it does not fall under the Exclusion Grounds"; it declares nothing on them, because the request asks for none (`10-QualificationApplicationRequest.xml`, its review). The two belong together.
- Condition: the response declares on the exclusion grounds the request contains, or the world records why the contest has none.
- Options: as for the request: (preferred) an exclusion criterion answered here.
- Needs decision: yes
- From: context (F7)

### contest/11#F10 · Low · The economic operator's contact is a sales desk
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact of a contest participant handles the request to participate and the jury's questions; Brackenmere gives its trade-sales desk (Saltmere has a "Bids office" elsewhere in the flow).
- Condition: the economic operator's contact handles its part in the contest.
- Options: (preferred) a bids or design office of the lead; or no contact.
- Needs decision: no
- From: broad (F5), parties (F5), context (F6)

### contest/11#F11 · Low · Customs-trader number and tax registrations in a document that does nothing with them
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: section 4.8. The response has no amount, price, payment or tax, and no criterion about customs or taxes; the customs number serves customs declarations (55 files carry it, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`), the authority's exemption serves what it buys. Context refuted the operator's own registration (a qualification step may check it); the merge keeps it in the finding because no criterion of this response asks for it (see F9).
- Condition: the parties carry only identifiers and registrations the document uses.
- Options: (preferred) leave them out of the qualification documents; keep the operator's tax registration if an exclusion ground on taxes is added.
- Needs decision: no
- From: broad (F4), money (F1), parties (F4), logistics (F4), context (F8)

### contest/11#F12 · Low · The party's tax exemption reason is worded as a sale
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the code's list definition is the buyer's status (money's refutation holds for the code), but the text begins "Sale to a public body", a transaction. Applies only if F11 keeps the tax scheme.
- Condition: where stated, the text describes the party's status, not a sale.
- Options: (preferred) "Public body: exempt from the state sales tax"; or a status code.
- Needs decision: no
- From: broad (F4, part), parties (F3), context (F8, part)

### contest/11#F13 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the same date for 25 companies (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, recounted), a holiday; a filler unless the world has a reason.
- Condition: Brackenmere's registration date has a reason in the world, or is absent.
- Options: (preferred) its own date; or leave it out; or record the date as a story event.
- Needs decision: yes
- From: parties (F6)

## Checked and consistent
- `CR-PROF` and `P-PROF-1` exist in the request; the answer (registered industrial designer) meets the widened criterion of version 2; `ResponseCode` `MET` agrees; `EvidenceTypeCode` `CERTIFICATE` fits (broad, logistics, context).
- Issued 2026-04-13, after the request and before the participation deadline 2026-05-02 (`08-ContractNotice.xml`) (broad, logistics).
- Version chain: `VersionID` 2, `PreviousVersionID` 1, same ID as `06-QualificationApplicationResponse.xml` (logistics).
- `EconomicOperatorGroupName` agrees with the result text of `15-ContractAwardNotice.xml` (context).
- No amounts; Brackenmere's tax registration the same throughout the flow (money).
- Parties identical across the flow; GLN check digit valid; +999 and `.example` not real (broad, parties).
- Physics: nothing to calculate (logistics).

## Considered and refuted
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description`: a redundant copy of the response description — refuted by broad as harmless; the merge keeps it as F8 (Low) with that argument.
- `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: Saltmere should also be an economic operator party — refuted by broad (the lead answers for the group); `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName`: group without its second member — refuted by logistics (members identified in the tenderer qualification). The merge keeps the missing lead role as F4 (Low).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: the code describes a transaction — refuted for the code by its list definition (from money); the text is F12.
- Missing financial-standing criterion — refuted: a design contest selects on references and qualification (from money).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 too general — refuted (from parties).
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: address department vs contact department — refuted: the same unit (from parties).
- `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: refuted by context as part of the operator's identity; the merge disagrees and keeps it in F11.

## Changed in the merge
- broad/F2 (Medium), logistics/F1 (Medium), context/F1 (Medium) → F1: combined; the one-completed-task point of logistics and context added.
- broad/F3 (Low, yes), parties/F1 (Medium, yes), context/F9 (Low, no) → F3: Medium, needs decision no (aligned with the earlier flows).
- parties/F7, context/F3 → F4: combined; preferred option is the lead role (parties); the second party is optional; broad's and logistics' refutations added.
- broad/F6, logistics/F3, context/F4 → F6: combined; the option names `SuppliedEvidence` (UBL 2.5) rather than the deprecated `EvidenceSupplied` that broad and context named.
- parties/F8 → F5: noted that version 2 does not say what changed.
- broad/F4, money/F1, parties/F4, logistics/F4, context/F8 → F11 and F12 (wording of the exemption, parties/F3).
- broad/F5, parties/F5, context/F6 → F10; `Department` line added.

## Outside this review
- The same party descriptions recur in the other flows that carry these parties; they belong to those examples' reviews (from parties).
