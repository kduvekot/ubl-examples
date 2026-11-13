# LLM review: 06-QualificationApplicationResponse.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/06-QualificationApplicationResponse.xml`, Git blob `b89ddaa322929529c260e62567adcd7133757db3` (committed)
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

### contest/06#F1 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language as used in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is the ISO 639 language code itself, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale (section 6 names a language code in `LocaleCode` as Medium). Verified in the XML at every place listed. The same value occurs 362 times in 213 examples (recounted in the merge with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l` and `grep -rl` for the file count; a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also matches other `…LocaleCode` elements).
- Condition: No `cbc:LocaleCode` in the example holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since nothing in the document needs a locale beyond the language that `Language/cbc:ID` already gives; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID. Same as every earlier flow.
- Needs decision: no
- From: broad F1, parties F2, context F2

### contest/06#F2 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The public body of this example (Lumeport Public Works Department) is entered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carries `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). A city department (and, where present, a federal information service or a review board) is not a business in a register of businesses and is not wound up by liquidation; the contracting party describes itself as "a department of the city of Lumeport" (`ContractingPartyType/PartyType`), and its ISIC class is 8411 (public administration). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no type for a register of public bodies, so the value is forced. Verified in the XML. The values carry a meaning that does not fit the party (Medium, as the customs authority described as a company in the earlier flows). Parties added that a city department is not a legal person at all; the legal entity behind it is the City of Lumeport.
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; a registration scheme given for a public body says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep only the register name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list; or give the City of Lumeport as the department's legal entity (this last option changes who the party is and would need a decision).
- Needs decision: no
- From: broad F3, parties F1, context F9

### contest/06#F3 · Medium · The two scored reference criteria of the request are not answered
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-PROF-1`
- XPath: `05-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-REF-PUBLIC`
- XPath: `05-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-REF-COAST`
- Why: The QualificationApplicationResponse is "A self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria", and its `TenderingCriterion` is "The criterion as described in the Qualification Application Request". The request has three criteria: `CR-PROF` (pass or fail) and the two references `CR-REF-PUBLIC` (weight 60) and `CR-REF-COAST` (weight 40), on which "the jury selects the participants" (`03-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cbc:LimitationDescription` = `The jury selects the participants on their references.`). This response repeats and answers only `CR-PROF` (verified: one `TenderingCriterion`, one `TenderingCriterionResponse`); `P-REF-PUBLIC-1` and `P-REF-COAST-1` get no answer, and the tenderer qualification of the same day gives one completed task only (`07-TendererQualification.xml`). No document of the flow carries what the selection is made on, yet the team is selected and wins (`15-ContractAwardNotice.xml`). Medium (missing information the purpose depends on), not High: no value contradicts another.
- Condition: The response answers every criterion of the request it responds to, with responses validating `P-REF-PUBLIC-1` and `P-REF-COAST-1`, or states why a criterion is not answered.
- Options: (preferred) add the two criteria and responses (project, client, year and what the team designed; one reference on a coastal site), consistent with the completed tasks of the tenderer qualification; or, if the story wants an incomplete response, make that visible (e.g. `ResponseCode` for not met, or a note).
- Needs decision: no
- From: broad F2, context F1, logistics F1

### contest/06#F4 · Low · The response does not refer to the request it answers
- XPath: `/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0637`
- Why: The response answers the request `LPWD-DOC-26-0636` (`05-QualificationApplicationRequest.xml`) and repeats its criterion and property IDs, but carries no `AdditionalDocumentReference` to it (verified); the request exists in two versions with different design-lead requirements (`10-QualificationApplicationRequest.xml`), so which one is answered can only be inferred from the issue dates (logistics).
- Condition: The response identifies the request (ID `LPWD-DOC-26-0636`, and its version) that it answers.
- Options: (preferred) an `AdditionalDocumentReference` to `LPWD-DOC-26-0636` with its `VersionID`; or leave it implicit through `ContractFolderID`.
- Needs decision: no
- From: logistics F2

### contest/06#F5 · Low · Group named, but the response neither lists its other member nor gives the lead's role
- XPath: `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: The response is made for a group ("Economic Operator Group Name associated with this Qualification"), and the contract notice asks a group to name its lead (`03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`). `EconomicOperatorParty` has `EconomicOperatorRole` ("The role of the party in a tender consortium") and `QualifyingParty` for this, but carries only the `Party`; Saltmere Engineering, whose architect is named as design lead, appears only in free text. The tenderer qualification of the same day encodes the roles (`07-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`). Counter-argument (broad, which refuted the missing second party): the lead answers for the group and its composition is declared in the tenderer qualification. That covers the second member, not the missing role of the lead.
- Condition: The response states in structured form that Brackenmere Furniture answers as lead of the group, consistent with the tenderer qualification (and, if the group's members are to be identified here, lists Saltmere Engineering with its role).
- Options: (preferred) add `EconomicOperatorParty/EconomicOperatorRole` with the lead role; optionally a second `EconomicOperatorParty` (or a `QualifyingParty`) for Saltmere with the member role.
- Needs decision: no
- From: parties F7, context F3; second-member part refuted by broad

### contest/06#F6 · Low · Customs and tax master data the procurement document does nothing with
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: `AdditionalPartyIdentification` is "One or more additional identifiers for this Party". The customs trader number (scheme `urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works Department towards customs and is used in its customs declarations (e.g. `tender/31-ImportCustomsDeclaration.xml`); this QualificationApplicationResponse is a procurement document of a design contest for a service: nothing is imported, declared or transported, and nobody in the document uses the number. It is copied from the party's master data (section 4.8; the value is in 55 examples, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted in the merge). The same holds for the economic operators' own `PartyTaxScheme` ("A tax scheme applying to this party"): nothing in this document is taxed, priced, invoiced or paid, and no criterion refers to a tax registration (money). Counter-argument (context, in 05-07): a qualification step may check a tenderer's tax registration as part of its identity; the request of this flow, however, asks for no such check, so the argument does not give the value a use here.
- Condition: The contracting authority carries no customs trader identifier in this procurement document, and the economic operators carry a `PartyTaxScheme` only where the document uses it.
- Options: (preferred) leave these values out of the procurement documents and keep them where documents use them (customs declarations, invoices); or keep one only where the story gives this document a reason, and say so.
- Needs decision: no
- From: broad F4 (part), parties F4, logistics F4, context F8 (part), money F1 (part)

### contest/06#F7 · Low · Tax scheme of the contracting authority in a document that may not use it
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". The contracting authority brings its state sales tax registration and exemption into a procurement document. This document states no amount at all: nothing in it is priced, taxed or paid. Broad and context (and money from 05 on) read it as master data copied into a document that does not use it (section 4.8). Money (01-04, 08) refuted that: the buyer's exemption tells candidates that the amounts of the contest and of the follow-up contract are net of the state sales tax. Both readings are possible; the merge could not settle which the world intends, although in this document, which has no amounts, the money argument is weaker.
- Condition: Either the authority's `PartyTaxScheme` is absent from this document, or the world states that procurement documents carry it to show that amounts are net of sales tax (and it is then carried consistently).
- Options: (preferred) leave it out of documents without amounts and decide for the notices whether the exemption is meant as information to candidates (then keep it and say so where amounts are given); or keep it everywhere as the buyer's tax status.
- Needs decision: yes
- From: broad F4 (part), context F8 (part), money F1 (part)

### contest/06#F8 · Low · Exemption reason of the contracting authority worded as a sale
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", i.e. the party's own status. The text begins "Sale to a public body", the name of the code in the Bayvarran exemption list (whose other codes are reasons for exempt supplies), and so describes a transaction; this document records no sale. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Money refuted the code itself, rightly: the list describes `PUBLIC` as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (verified in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`). What remains is the wording of the text. The same text is in 55 examples (`grep -rl --include='*.xml' 'Sale to a public body: public bodies' world/examples | wc -l`).
- Condition: Where the authority's exemption reason is stated, the text states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status ("Public body: exempt from the state sales tax") and keep the code; or add a status code for public bodies to the list.
- Needs decision: no
- From: broad F4 (part), parties F3, context F8 (part)

### contest/06#F9 · Low · Registration date 1996-01-01 looks like a default, not the party's date
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday, and the same date is the registration date of 25 different companies in all three countries (271 occurrences in 181 files, recounted in the merge with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples`). That points to a filler (IND5) unless the world has a reason (e.g. one re-registration day), which the examples do not show.
- Condition: The registration date of Brackenmere Furniture is a date with a reason in the world, or the element is absent.
- Options: (preferred) give each company its own registration date from its history; or leave the element out where nothing uses it; or record a 1996 re-registration in the story. Same as every earlier flow.
- Needs decision: yes
- From: parties F6

### contest/06#F10 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: A contact is "The primary contact for this party" and should handle the party's part in this document (section 5). Brackenmere Furniture takes part in the contest through its "Trade sales" desk with a `Customer service officer` of the `Sales` department, the contact for trade customers' orders, not the office that handles a contest. The contacts are the parties' general contacts from the goods flows, the same in every example that carries these parties. Verified in the XML.
- Condition: Each contact in the example handles the party's part in the contest (requests to participate, designs and questions of the jury for a participant; appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a contact for their role (a bids or design office for the participants, a registry clerk or registrar for the review board); or leave the contact out where the electronic address is the channel.
- Needs decision: no
- From: broad F5, parties F5, context F6

### contest/06#F11 · Low · Design lead from Saltmere against the division of work in the tenderer qualification
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Edda Corwin of Saltmere Engineering, is a registered architect, no. AR-4417, in the register of the Bayvarran Chamber of Architects.`
- XPath: `07-TendererQualification.xml:/TendererQualification/cbc:Note` = `The furniture maker leads the team; the engineering firm does the structure and the anchoring.`
- Why: This response names Edda Corwin "of Saltmere Engineering", a registered architect, as the design lead, while the tenderer qualification issued the same day says that the furniture maker leads the team and the engineering firm "does the structure and the anchoring" (40 % of the work, `07-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40`). Read strictly, the architect leading the design belongs to the firm that only does structure and anchoring. Counter-argument (context in 07, which refuted it): leading the team (consortium lead) and being the design lead are different roles, and an engineering firm can employ the architect. The examples do not settle which is meant (parties). The second version names another design lead (`11-QualificationApplicationResponse.xml`).
- Condition: The design lead's firm and the division of work stated in the tenderer qualification agree.
- Options: (preferred) say in the tenderer qualification's note who provides the design lead; or attribute the design lead to Brackenmere.
- Needs decision: yes
- From: parties F8 (same problem as 07 broad F6); refuted by context in 07

### contest/06#F12 · Low · The same text twice: response description and response value description
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Edda Corwin of Saltmere Engineering, is a registered architect,…`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `The design lead, Edda Corwin of Saltmere Engineering, is a registered architect,…`
- Why: The criterion response and its response value carry the identical sentence (verified). The value answers the property ("The register and the registration number of the design lead"); the response description adds nothing (context: duplicated content without its own reason, IND5). Counter-argument (broad, which refuted it): the two elements mean different things and repeating the text is harmless. Kept as Low: the duplicate has no business reason.
- Condition: Each text says something of its own, or only one of them is present.
- Options: (preferred) keep the sentence in the `ResponseValue` and drop the response `Description`; or let the description summarise and the value give register and number only.
- Needs decision: no
- From: context F5; refuted by broad

### contest/06#F13 · Low · Evidence not linked to the response it supports, and not identifiable
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ID` = `CRR-PROF`
- XPath: `/QualificationApplicationResponse/cac:Evidence/cbc:ID` = `EV-REG-LEAD`
- XPath: `/QualificationApplicationResponse/cac:Evidence/cbc:Name` = `Certificate of registration of the design lead`
- Why: The certificate of registration (`EV-REG-LEAD`) stands at document level ("The evidence supporting this criterion requirement response"). The response `CRR-PROF` does not refer to it, although `TenderingCriterionResponse` has `SuppliedEvidence` for that ("A reference to the Evidence supporting this criterion property response"; the older `EvidenceSupplied` is deprecated in UBL 2.5, verified in the model), and the evidence has no `DocumentReference` and no `EvidenceIssuingParty`, so the buyer can neither tie it to the answer nor retrieve it.
- Condition: The response the certificate supports refers to `EV-REG-LEAD`, and the evidence identifies the certificate or its issuer.
- Options: (preferred) add `SuppliedEvidence` with `EV-REG-LEAD` to `CRR-PROF` and a `DocumentReference` (or the issuing chamber) to the evidence; or drop the evidence if the registration number in the text is enough.
- Needs decision: no
- From: broad F6, context F4, logistics F3

### contest/06#F14 · Low · No self-declaration on exclusion grounds
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- Why: UBL defines the response as "A self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria". It declares nothing on exclusion grounds, because the request (`05-QualificationApplicationRequest.xml`) asks for none; the two belong together (context).
- Condition: The response declares on the exclusion grounds the request contains, or the world documents why the contest has none.
- Options: As for the request: (preferred) an exclusion criterion answered here; or document why there is none.
- Needs decision: yes
- From: context F7

## Checked and consistent
- Merge: every finding above was re-checked against the XML (values, positions, counts) and against the referenced examples; the definitions quoted were looked up in UBL-Entities-2.5.gc and the code meanings in `world/codelists/gc/`. The counts were redone over `*.xml` only.
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company. (from broad)
- `TenderingCriterion` `CR-PROF` and `ValidatedCriterionPropertyID` `P-PROF-1` exist in the request (`05-QualificationApplicationRequest.xml`). (from broad)
- The answer (registered architect) meets the criterion "a registered architect" of version 1 of the request; `ResponseCode` `MET` agrees. (from broad)
- Issued 2026-04-01, within the request period (to 2026-04-18, `03-ContractNotice.xml`). (from broad)
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). (from broad)
- The document has no amounts, prices, payment means or financial criteria (searched for `Amount`, `currencyID`, `Price`, `Payment`, `Percent` in the `*.xml`); its criteria are professional qualification and references only, so there is no money arithmetic to check. (from money)
- Brackenmere's tax registration `UL-1237398` is the same as in every other contest example that carries it (04, 05, 06, 07, 09–16) and in its register extract (13, 14). (from money)
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data). (from parties)
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address. (from parties)
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606). (from parties)
- Brackenmere's GLN 9523710900008 has a valid check digit (check_ids.py) and uses GS1 prefix 952, which GS1 reserves for demonstrations (own knowledge). (from parties)
- References that resolve: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF` and `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-PROF-1` exist in the request (05-QualificationApplicationRequest.xml). (from logistics)
- The answer fits the requirement in force: a registered architect (CN v1, QAR v1); ResponseCode MET fits; EvidenceTypeCode CERTIFICATE fits a certificate of registration. (from logistics)
- Dates: issued 2026-04-01, before the participation deadline (2026-04-18) and after the request. (from logistics)
- Party identifiers of Brackenmere (register 20412466, GLN 9523710900008 with correct check digit) and of the department (20410548) agree with the other examples. (from logistics)
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against. (from logistics)
- ValidatedCriterionPropertyID `P-PROF-1` exists in the request and is the property this answer gives (register and number). (from context)
- ResponseCode `MET` agrees with the text (the lead is registered as the version of the request requires: architect). (from context)
- EconomicOperatorGroupName agrees with the result text of `15-ContractAwardNotice.xml` ("the Brackenmere and Saltmere design team"). (from context)

## Considered and refuted
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description`: suspected a redundant copy of the response's own description — refuted as a finding because `ResponseValue/Description` is the value of the property (data type DESCRIPTION) and the response description describes the response; repeating the text is harmless. (from broad) Not followed in the merge: kept as F12, with this argument recorded there as counter-argument.
- `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: suspected that the group member Saltmere Engineering should also be an economic operator party — refuted because the group is named in `EconomicOperatorGroupName` and its composition is declared in the tenderer qualification; the lead answers for the group. (from broad) Not followed in the merge: kept as F5, with this argument recorded there as counter-argument.
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction rather than the party's status — refuted because the list defines it as the buyer's status ("A body of the federation, a state or a city buys free of sales tax"); its presence is part of finding F1. (from money) Accepted in the merge for the code; the wording of the text remains finding F8.
- Missing financial standing criterion (turnover): considered whether a qualification request without one lacks something the document needs — refuted because a design contest selects participants on their references and professional qualification; nothing in the flow asks for financial standing. (from money)
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better. (from parties)
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department. (from parties)
- `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`: suspected that a group name without the second member as EconomicOperatorParty is an unresolved reference — refuted for this lens: the group's members are identified in the tenderer qualification (07-TendererQualification.xml: Brackenmere 20412466 and Saltmere Engineering 20410685); whether each member must also send its own response is a question of the parties lens. (from logistics) Not followed in the merge: kept as F5, with this argument recorded there as counter-argument.
- `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: the economic operator's own tax registration in a qualification document — not made part of the copied-data finding, because a qualification step may check a tenderer's tax registration (it is part of its identity for the selection), unlike the contracting authority's. (from context) Not followed in the merge: kept as F6, with this argument recorded there as counter-argument.

## Changed in the merge
- broad F3 + parties F1 + context F9 → one finding, Medium, Needs decision no (as in 01-05).
- broad F2 + context F1 + logistics F1 → one finding (all Medium); the counter-check against the tenderer qualification added.
- parties F7 + context F3 → one finding; broad's refutation of the missing second party recorded as counter-argument.
- broad F4, context F8 and money F1 regrouped into three findings (customs identifier + operator's tax scheme, Low/no; authority's tax scheme, Low/yes; wording, Low/no), aligned with merger B.
- context F6 merged into the contacts finding of broad F5 / parties F5.
- broad F6 + context F4 + logistics F3 → one finding; the option now names `SuppliedEvidence` (broad and context named the deprecated `EvidenceSupplied`).
- context F5 (duplicate text) kept Low/no; broad's refutation recorded as counter-argument.
- Every finding merged from several parts keeps the clearest wording and all evidence; findings are numbered by severity and then by position in the document.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews. (from parties)
