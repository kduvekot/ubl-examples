# LLM review: 10-QualificationApplicationRequest.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/10-QualificationApplicationRequest.xml`, Git blob `5062e7029b9e54e815b6487b80aa0104eeade8e3` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 70e2a4d 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### contest/10#F1 · Medium · FulfilmentIndicator in the request states the criterion is already fulfilled
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicator` = `true`
- Why: TenderingCriterion/FulfilmentIndicator: "An indication that this criterion has been fulfilled." This document is the buyer's request, issued before any economic operator has answered; nothing can have been fulfilled yet, and the buyer is not the party that declares fulfilment. Only the first of the three criteria carries it, so it also cannot be read as a general flag of the request.
- Condition: No criterion of the request states that it has been fulfilled.
- Options: Preferred: remove the indicator from the request (fulfilment is declared in the response, `06-QualificationApplicationResponse.xml`, through ResponseCode `MET`). Alternative: if a "must be fulfilled" flag is meant, use an element whose definition says so and record the gap.
- Needs decision: no

### contest/10#F2 · Medium · LocaleCode carries a language code
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines Language/LocaleCode as "A code signifying the locale in which this language is used", and Language/ID as "An identifier for this language". Every party here gives `en` with listID `ISO 639` in both: the locale element repeats the language code instead of naming a locale (a language in a region, such as en-XB). A language code is a valid code, but not the one the definition names. The same pattern (`<cbc:LocaleCode listID="ISO 639">`) occurs in 213 example files, 362 times (counted with `grep -c` over `world/examples/*/*.xml`).
- Condition: Every LocaleCode either names a locale (language and country/region) from a locale scheme, or is absent.
- Options: Preferred: drop LocaleCode where the party has no locale to state beyond its language (Language/ID already says English). Alternative: a locale code such as `en-XB` with a locale listID (e.g. BCP 47).
- Needs decision: no

### contest/10#F3 · Low · Economic operator contact is a sales desk, not the contest contact
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The contact of a participant in a design contest is the person or office that handles the request to participate, the design and the questions of the jury. The contact given is a sales or order desk (`Customer service officer` in `Sales`), which fits a trading partner taking orders, not a team entering a contest. Elsewhere in the flow the consortium member Saltmere Engineering is given a "Bids office" contact, which shows the kind of contact meant.
- Condition: The economic operator's contact in this document is the office or person that handles the contest.
- Options: Preferred: a bids or design office contact for the lead member. Alternative: no contact, where the electronic address is the channel.
- Needs decision: no

### contest/10#F4 · Low · The coastal-site criterion asks a question that does not cover what it scores
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:Description` = `Whether one of the two references stands within one kilometre of the sea.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Description` = `The project, the client, the year and what the team designed.`
- Why: The criterion scores "Whether one of the two references stands within one kilometre of the sea", but its only property asks for "The project, the client, the year and what the team designed", the same question as the public-space reference, without the place or its distance from the sea. A response to this property does not give the jury the fact the criterion is about.
- Condition: The property (or a second property) of the coastal criterion asks for the location of the reference and its distance from the sea.
- Options: Preferred: add a property for the site of the reference (place, distance from the sea). Alternative: reword the existing property so that it asks for the site.
- Needs decision: no

### contest/10#F5 · Low · No exclusion grounds in a request that defines how exclusion grounds are addressed
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:CriterionTypeCode` = `SUITABILITY`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:CriterionTypeCode` = `TECHNICAL`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:CriterionTypeCode` = `TECHNICAL`
- Why: UBL defines the QualificationApplicationRequest as "A document issued by a buyer defining how the Exclusion Grounds and the Selection Criteria should be addressed". All three criteria are selection criteria (`SUITABILITY`, `TECHNICAL`); none is of type `EXCLUSION`, which the world's CriterionTypeCode list offers. The register extract later records "no exclusion grounds" (`13-BusinessInformation.xml:/BusinessInformation/cbc:BriefDescription`), so exclusion grounds exist in the world's procedure, but the participants are never asked to declare them.
- Condition: Either the request contains the exclusion grounds that apply to the contest, or the world states that design contests have none and the register check replaces the self-declaration.
- Options: Preferred: add one exclusion criterion (e.g. convictions or unpaid taxes) answered in the response. Alternative: document why the contest has none.
- Needs decision: yes

### contest/10#F6 · Low · Tax and customs identity copied into a document that does nothing with them
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: QualificationApplicationRequest carries no amount that is taxed, no tax total and no customs procedure, yet the parties bring their tax registration (PartyTaxScheme) and, where they have one, their customs trader number (AdditionalPartyIdentification, scheme `customs-trader`). Section 4.8 of the review rules: data copied from a party's master data into a document that does not use it. For the contracting authority the tax scheme also states ExemptionReasonCode `PUBLIC`, whose meaning in the list is "Sale to a public body"; PartyTaxScheme/ExemptionReasonCode is "A reason for the party's exemption from tax", so even where the scheme is kept, the reason should be the party's own status, not a kind of sale.
- Condition: The parties of this document carry no tax scheme and no customs trader number, unless something in the document uses them; where a PartyTaxScheme of a public body is kept, its exemption reason names the party's status.
- Options: Preferred: leave PartyTaxScheme and the customs trader identifier out of the notices and qualification documents, as the Bayvarra Information Service is described throughout the flow. Alternative: keep them only where a tax or customs check is part of the step, and say so in the document.
- Needs decision: no

### contest/10#F7 · Low · Public bodies described as companies in the commercial register, with a liquidation status
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The public bodies of this document (ISIC 84xx: Lumeport Public Works Department, "a department of the city of Lumeport") are registered in a CorporateRegistrationScheme of type `COMMERCIAL` ("Commercial register") and carry CompanyLiquidationStatusCode `ACTIVE` ("Active, not in liquidation"). A city department or a state authority is not a company in a commercial register and cannot be liquidated, so "the party's liquidation status" has no meaning for it (review checklist, party legal entity).
- Condition: No public body in this document has a liquidation status, and its registration scheme, if stated, is not a commercial register.
- Options: Preferred: no CompanyLiquidationStatusCode for public bodies, and a registration scheme of a type for public bodies (or none). Alternative: keep the federal register but with a type code that says it registers public bodies.
- Needs decision: no

## Checked and consistent
- Weights: `/QualificationApplicationRequest/cbc:WeightScoringMethodologyNote` says pass or fail for the design lead and 60 / 40 for the references; the criteria carry `PASSFAIL`, WeightNumeric 60 and 40, which add up to 100.
- The professional criterion's Description follows the contract notice of the same version ("registered architect" in version 1, "or registered industrial designer" in version 2).
- The economic operator receiving the request (EconomicOperatorParty) is the operator that answers it in the response of the same version.

## Considered and refuted
- `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Name` = `The reference`: one property for "the two completed designs" — refuted: a response may give several response values for one property, so one question can collect both references.
- `/QualificationApplicationRequest/cbc:QualificationApplicationTypeCode` = `REGULATED`: fits a procedure under the procurement rules.
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: the economic operator's own tax registration in a qualification document — not made part of the copied-data finding, because a qualification step may check a tenderer's tax registration (it is part of its identity for the selection), unlike the contracting authority's.
