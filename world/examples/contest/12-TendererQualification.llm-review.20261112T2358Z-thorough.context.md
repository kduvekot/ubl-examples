# LLM review: 12-TendererQualification.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/12-TendererQualification.xml`, Git blob `0e1445bc31c9b97d2a3ad93650d9791482d0b7a0` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
- Checkout: branch `claude/keen-feynman-45qjti`, commit 690a166 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### contest/12#F1 · Medium · LocaleCode carries a language code
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines Language/LocaleCode as "A code signifying the locale in which this language is used", and Language/ID as "An identifier for this language". Every party here gives `en` with listID `ISO 639` in both: the locale element repeats the language code instead of naming a locale (a language in a region, such as en-XB). A language code is a valid code, but not the one the definition names. The same pattern (`<cbc:LocaleCode listID="ISO 639">`) occurs in 213 example files, 362 times (counted with `grep -c` over `world/examples/*/*.xml`).
- Condition: Every LocaleCode either names a locale (language and country/region) from a locale scheme, or is absent.
- Options: Preferred: drop LocaleCode where the party has no locale to state beyond its language (Language/ID already says English). Alternative: a locale code such as `en-XB` with a locale listID (e.g. BCP 47).
- Needs decision: no

### contest/12#F2 · Low · One completed task where the selection asks for two references, one coastal
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Seating for the Lumeport central library's reading garden, 2024.`
- XPath: `08-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2`
- Why: The tenderer qualification is "A document declaring the qualifications of a tenderer"; CompletedTask is "A former task completed by this qualifying party". The contract notice requires two completed designs for public spaces in the last five years, and the qualification request scores a second, coastal one. The team declares one task (seating for the library reading garden, which is not on the coast as far as the text says), and the consortium member none; the response does not give the references either (see its review). On what the flow shows, the team does not meet the threshold it is later selected and ranked on.
- Condition: The qualifying parties together declare at least two completed tasks that meet the reference criterion, one of them on a coastal site.
- Options: Preferred: a second CompletedTask (e.g. on the coast) for the lead or the member. Alternative: if the team qualifies otherwise, say how in the document.
- Needs decision: no

### contest/12#F3 · Low · BusinessIdentityEvidenceID holds the party's register number
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyIdentification/cbc:ID` = `20412466`
- Why: QualifyingParty/BusinessIdentityEvidenceID: "An identifier for an item of evidence to support the business identity of this qualifying party." The value is the company's own register number, the same as its PartyIdentification, not the identifier of a piece of evidence (an extract, a certificate). It can be read as "the register entry is the evidence", which is why it is only Low.
- Condition: BusinessIdentityEvidenceID identifies an item of evidence (e.g. a register extract), or is absent.
- Options: Preferred: the identifier of the register extract the team supplies (the flow has one, `13-BusinessInformation.xml`, issued later by the register). Alternative: drop it, since the party identification already gives the number.
- Needs decision: no

### contest/12#F4 · Low · Economic operator contact is a sales desk, not the contest contact
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The contact of a participant in a design contest is the person or office that handles the request to participate, the design and the questions of the jury. The contact given is a sales or order desk (`Customer service officer` in `Sales`), which fits a trading partner taking orders, not a team entering a contest. Elsewhere in the flow the consortium member Saltmere Engineering is given a "Bids office" contact, which shows the kind of contact meant.
- Condition: The economic operator's contact in this document is the office or person that handles the contest.
- Options: Preferred: a bids or design office contact for the lead member. Alternative: no contact, where the electronic address is the channel.
- Needs decision: no

### contest/12#F5 · Low · Tax and customs identity copied into a document that does nothing with them
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: TendererQualification carries no amount that is taxed, no tax total and no customs procedure, yet the parties bring their state sales tax registration (PartyTaxScheme, with TaxScheme `STT`) and their customs trader number (AdditionalPartyIdentification, scheme `customs-trader`). Section 4.8 of the review rules: data copied from a party's master data into a document that does not use it. For the contracting authority the tax scheme also states ExemptionReasonCode `PUBLIC`, whose meaning in the list is "Sale to a public body"; PartyTaxScheme/ExemptionReasonCode is "A reason for the party's exemption from tax", so even where the scheme is kept, the reason should be the party's own status, not a kind of sale.
- Condition: The parties of this document carry no tax scheme and no customs trader number, unless something in the document uses them; where a PartyTaxScheme of a public body is kept, its exemption reason names the party's status.
- Options: Preferred: leave PartyTaxScheme and the customs trader identifier out of the notices and qualification documents, as the Bayvarra Information Service is described throughout the flow. Alternative: keep them only where a tax or customs check is part of the step, and say so in the document.
- Needs decision: no

### contest/12#F6 · Low · Public bodies described as companies in the commercial register, with a liquidation status
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The public bodies of this document (ISIC 84xx: Lumeport Public Works Department, "a department of the city of Lumeport") are registered in a CorporateRegistrationScheme of type `COMMERCIAL` ("Commercial register") and carry CompanyLiquidationStatusCode `ACTIVE` ("Active, not in liquidation"). A city department or a state authority is not a company in a commercial register and cannot be liquidated, so "the party's liquidation status" has no meaning for it (review checklist, party legal entity).
- Condition: No public body in this document has a liquidation status, and its registration scheme, if stated, is not a commercial register.
- Options: Preferred: no CompanyLiquidationStatusCode for public bodies, and a registration scheme of a type for public bodies (or none). Alternative: keep the federal register but with a type code that says it registers public bodies.
- Needs decision: no

## Checked and consistent
- ParticipationPercent of lead and member add up to 100 (`70` + `30`).
- TendererRoleCode `LEAD` / `MEMBER` agree with the Note ("The furniture maker leads the team") and with the contract notice's requirement that a group names a lead member.
- The completed task lies within the five-year window (2024-03-01 to 2024-09-30).

## Considered and refuted
- `/TendererQualification/cbc:Note` = `The furniture maker leads the team; the engineering firm does the structure and the anchoring.`: suspected a contradiction with the response of version 1, where the design lead is "of Saltmere Engineering" — refuted: leading the team (consortium lead) and being the design lead are different roles, and an engineering firm can employ the registered architect.
- `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cbc:IndustryClassificationCode` = `4290`: suspected that a firm doing structure and anchoring of a bench design should be classed as engineering services (ISIC 7110) — refuted: Saltmere Engineering is a civil engineering contractor in other flows (tender), and the classification is the party's, not the task's.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: the economic operator's own tax registration in a qualification document — not made part of the copied-data finding, because a qualification step may check a tenderer's tax registration (it is part of its identity for the selection), unlike the contracting authority's.
