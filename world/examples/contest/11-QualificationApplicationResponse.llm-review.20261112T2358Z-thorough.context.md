# LLM review: 11-QualificationApplicationResponse.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/11-QualificationApplicationResponse.xml`, Git blob `786906485480cbed630ad927abbdceded6391e3d` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
- Checkout: branch `claude/keen-feynman-45qjti`, commit 690a166 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### contest/11#F1 · Medium · No response to the two scored reference criteria
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-PROF-1`
- XPath: `10-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-REF-PUBLIC`
- XPath: `10-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-REF-COAST`
- Why: UBL: the QualificationApplicationResponse is a self-declaration "that it meets the Selection Criteria". The request (10-QualificationApplicationRequest.xml) has three criteria, two of them scored (60 and 40) and the basis on which "the jury selects the participants on their references". The response answers only the pass-or-fail criterion CR-PROF; the references, the only scored part, are not given. The tenderer qualification of the same team carries a single completed task (see its review), so no document of the flow gives the two references the selection depends on.
- Condition: The response answers every criterion of the request, in particular CR-REF-PUBLIC and CR-REF-COAST, with the references the team offers.
- Options: Preferred: add TenderingCriterion and TenderingCriterionResponse entries for both reference criteria (two references, one of them coastal). Alternative: answer them by reference to the tenderer qualification, if the world's procedure splits it that way, and say so.
- Needs decision: no

### contest/11#F2 · Medium · LocaleCode carries a language code
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines Language/LocaleCode as "A code signifying the locale in which this language is used", and Language/ID as "An identifier for this language". Every party here gives `en` with listID `ISO 639` in both: the locale element repeats the language code instead of naming a locale (a language in a region, such as en-XB). A language code is a valid code, but not the one the definition names. The same pattern (`<cbc:LocaleCode listID="ISO 639">`) occurs in 213 example files, 362 times (counted with `grep -c` over `world/examples/*/*.xml`).
- Condition: Every LocaleCode either names a locale (language and country/region) from a locale scheme, or is absent.
- Options: Preferred: drop LocaleCode where the party has no locale to state beyond its language (Language/ID already says English). Alternative: a locale code such as `en-XB` with a locale listID (e.g. BCP 47).
- Needs decision: no

### contest/11#F3 · Low · Group named, but the response describes only one of its members
- XPath: `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: "Economic Operator Group Name associated with this Qualification" names a group of Brackenmere and Saltmere, and the design lead belongs to Saltmere Engineering in version 1. The contract notice asks a group to name a lead member. The response has one EconomicOperatorParty (Brackenmere) without a role, and Saltmere does not appear; the tenderer qualification of the same date describes the group with roles `LEAD` and `MEMBER`.
- Condition: A response for a group identifies the members of the group (or states that the lead answers for the group, with its role).
- Options: Preferred: add Saltmere Engineering as a second EconomicOperatorParty with roles for both. Alternative: keep one party but mark it as the group lead.
- Needs decision: no

### contest/11#F4 · Low · Evidence not linked to the response it supports
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ID` = `CRR-PROF`
- XPath: `/QualificationApplicationResponse/cac:Evidence/cbc:ID` = `EV-REG-LEAD`
- Why: The certificate of registration (`EV-REG-LEAD`) stands on its own at document level. The response CRR-PROF does not refer to it (TenderingCriterionResponse has EvidenceSupplied for that), and the evidence has no issuer, date or document reference, so nothing says which certificate supports which answer.
- Condition: The evidence is referenced from the response it supports, or carries what identifies the certificate.
- Options: Preferred: an EvidenceSupplied reference from CRR-PROF to EV-REG-LEAD. Alternative: drop the evidence entry, since the register number is in the response text.
- Needs decision: no

### contest/11#F5 · Low · The same text twice: response description and response value description
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Ivo Harlan, is registered as an industrial designer, no. ID-220…`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `The design lead, Ivo Harlan, is registered as an industrial designer, no. ID-220…`
- Why: The criterion response and its response value carry the identical sentence. The value answers the property ("The register and the registration number of the design lead"); the response description adds nothing to it. Duplicated content without its own business reason (IND5).
- Condition: Each text says something of its own, or only one of them is present.
- Options: Preferred: keep the sentence in the ResponseValue and drop the response Description. Alternative: let the response Description summarise and the value give register and number only.
- Needs decision: no

### contest/11#F6 · Low · Economic operator contact is a sales desk, not the contest contact
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The contact of a participant in a design contest is the person or office that handles the request to participate, the design and the questions of the jury. The contact given is a sales or order desk (`Customer service officer` in `Sales`), which fits a trading partner taking orders, not a team entering a contest. Elsewhere in the flow the consortium member Saltmere Engineering is given a "Bids office" contact, which shows the kind of contact meant.
- Condition: The economic operator's contact in this document is the office or person that handles the contest.
- Options: Preferred: a bids or design office contact for the lead member. Alternative: no contact, where the electronic address is the channel.
- Needs decision: no

### contest/11#F7 · Low · No self-declaration on exclusion grounds
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- Why: UBL defines the response as "A self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria". The response declares nothing on exclusion grounds, because the request (10-QualificationApplicationRequest.xml) asks for none (see its review). The two belong together.
- Condition: The response declares on the exclusion grounds the request contains, or the world documents why the contest has none.
- Options: As for the request: preferred an exclusion criterion answered here.
- Needs decision: yes

### contest/11#F8 · Low · Tax and customs identity copied into a document that does nothing with them
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: QualificationApplicationResponse carries no amount that is taxed, no tax total and no customs procedure, yet the parties bring their state sales tax registration (PartyTaxScheme, with TaxScheme `STT`) and their customs trader number (AdditionalPartyIdentification, scheme `customs-trader`). Section 4.8 of the review rules: data copied from a party's master data into a document that does not use it. For the contracting authority the tax scheme also states ExemptionReasonCode `PUBLIC`, whose meaning in the list is "Sale to a public body"; PartyTaxScheme/ExemptionReasonCode is "A reason for the party's exemption from tax", so even where the scheme is kept, the reason should be the party's own status, not a kind of sale.
- Condition: The parties of this document carry no tax scheme and no customs trader number, unless something in the document uses them; where a PartyTaxScheme of a public body is kept, its exemption reason names the party's status.
- Options: Preferred: leave PartyTaxScheme and the customs trader identifier out of the notices and qualification documents, as the Bayvarra Information Service is described throughout the flow. Alternative: keep them only where a tax or customs check is part of the step, and say so in the document.
- Needs decision: no

### contest/11#F9 · Low · Public bodies described as companies in the commercial register, with a liquidation status
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The public bodies of this document (ISIC 84xx: Lumeport Public Works Department, "a department of the city of Lumeport") are registered in a CorporateRegistrationScheme of type `COMMERCIAL` ("Commercial register") and carry CompanyLiquidationStatusCode `ACTIVE` ("Active, not in liquidation"). A city department or a state authority is not a company in a commercial register and cannot be liquidated, so "the party's liquidation status" has no meaning for it (review checklist, party legal entity).
- Condition: No public body in this document has a liquidation status, and its registration scheme, if stated, is not a commercial register.
- Options: Preferred: no CompanyLiquidationStatusCode for public bodies, and a registration scheme of a type for public bodies (or none). Alternative: keep the federal register but with a type code that says it registers public bodies.
- Needs decision: no

## Checked and consistent
- ValidatedCriterionPropertyID `P-PROF-1` exists in the request and is the property this answer gives (register and number).
- ResponseCode `MET` agrees with the text (the lead is registered as the version of the request requires: industrial designer, allowed from version 2 on).
- EconomicOperatorGroupName agrees with the result text of `15-ContractAwardNotice.xml` ("the Brackenmere and Saltmere design team").

## Considered and refuted
- `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: the economic operator's own tax registration in a qualification document — not made part of the copied-data finding, because a qualification step may check a tenderer's tax registration (it is part of its identity for the selection), unlike the contracting authority's.
