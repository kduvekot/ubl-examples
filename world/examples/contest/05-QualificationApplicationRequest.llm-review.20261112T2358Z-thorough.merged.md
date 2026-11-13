# LLM review: 05-QualificationApplicationRequest.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/05-QualificationApplicationRequest.xml`, Git blob `28d9b7bf1f028e6d60a3a976a753b0913f3d8eed` (committed)
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

### contest/05#F1 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language as used in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is the ISO 639 language code itself, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale (section 6 names a language code in `LocaleCode` as Medium). Verified in the XML at every place listed. The same value occurs 362 times in 213 examples (recounted in the merge with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l` and `grep -rl` for the file count; a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also matches other `…LocaleCode` elements).
- Condition: No `cbc:LocaleCode` in the example holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since nothing in the document needs a locale beyond the language that `Language/cbc:ID` already gives; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID. Same as every earlier flow.
- Needs decision: no
- From: broad F1, parties F2, context F2

### contest/05#F2 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The public body of this example (Lumeport Public Works Department) is entered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carries `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). A city department (and, where present, a federal information service or a review board) is not a business in a register of businesses and is not wound up by liquidation; the contracting party describes itself as "a department of the city of Lumeport" (`ContractingPartyType/PartyType`), and its ISIC class is 8411 (public administration). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no type for a register of public bodies, so the value is forced. Verified in the XML. The values carry a meaning that does not fit the party (Medium, as the customs authority described as a company in the earlier flows). Parties added that a city department is not a legal person at all; the legal entity behind it is the City of Lumeport.
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; a registration scheme given for a public body says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep only the register name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list; or give the City of Lumeport as the department's legal entity (this last option changes who the party is and would need a decision).
- Needs decision: no
- From: broad F3, parties F1, context F7

### contest/05#F3 · Medium · Fulfilment indicator set in the buyer's request
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:FulfilmentIndicator` = `true`
- Why: `Tendering Criterion. Fulfilment Indicator` is "An indication that this criterion has been fulfilled" (verified in the model). This document is the buyer's request ("defining how the Exclusion Grounds and the Selection Criteria should be addressed"), issued before any economic operator has answered; nothing can have been fulfilled, and the buyer is not the party that declares fulfilment. Only the first of the three criteria carries it (verified), so it cannot be read as a general flag either. The answer comes in the response, with `ResponseCode` `MET` (`06-QualificationApplicationResponse.xml`).
- Condition: No criterion of the request states that it has been fulfilled.
- Options: (preferred) leave `FulfilmentIndicator` out of the request; "must be met" is already said by `EvaluationMethodTypeCode` `PASSFAIL`.
- Needs decision: no
- From: broad F2, context F1

### contest/05#F4 · Low · Customs and tax master data the procurement document does nothing with
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: `AdditionalPartyIdentification` is "One or more additional identifiers for this Party". The customs trader number (scheme `urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works Department towards customs and is used in its customs declarations (e.g. `tender/31-ImportCustomsDeclaration.xml`); this QualificationApplicationRequest is a procurement document of a design contest for a service: nothing is imported, declared or transported, and nobody in the document uses the number. It is copied from the party's master data (section 4.8; the value is in 55 examples, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted in the merge). The same holds for the economic operators' own `PartyTaxScheme` ("A tax scheme applying to this party"): nothing in this document is taxed, priced, invoiced or paid, and no criterion refers to a tax registration (money). Counter-argument (context, in 05-07): a qualification step may check a tenderer's tax registration as part of its identity; the request of this flow, however, asks for no such check, so the argument does not give the value a use here.
- Condition: The contracting authority carries no customs trader identifier in this procurement document, and the economic operators carry a `PartyTaxScheme` only where the document uses it.
- Options: (preferred) leave these values out of the procurement documents and keep them where documents use them (customs declarations, invoices); or keep one only where the story gives this document a reason, and say so.
- Needs decision: no
- From: broad F4 (part), parties F4, logistics F2, context F6 (part), money F1 (part)

### contest/05#F5 · Low · Tax scheme of the contracting authority in a document that may not use it
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". The contracting authority brings its state sales tax registration and exemption into a procurement document. This document states no amount at all: nothing in it is priced, taxed or paid. Broad and context (and money from 05 on) read it as master data copied into a document that does not use it (section 4.8). Money (01-04, 08) refuted that: the buyer's exemption tells candidates that the amounts of the contest and of the follow-up contract are net of the state sales tax. Both readings are possible; the merge could not settle which the world intends, although in this document, which has no amounts, the money argument is weaker.
- Condition: Either the authority's `PartyTaxScheme` is absent from this document, or the world states that procurement documents carry it to show that amounts are net of sales tax (and it is then carried consistently).
- Options: (preferred) leave it out of documents without amounts and decide for the notices whether the exemption is meant as information to candidates (then keep it and say so where amounts are given); or keep it everywhere as the buyer's tax status.
- Needs decision: yes
- From: broad F4 (part), context F6 (part), money F1 (part)

### contest/05#F6 · Low · Exemption reason of the contracting authority worded as a sale
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", i.e. the party's own status. The text begins "Sale to a public body", the name of the code in the Bayvarran exemption list (whose other codes are reasons for exempt supplies), and so describes a transaction; this document records no sale. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Money refuted the code itself, rightly: the list describes `PUBLIC` as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (verified in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`). What remains is the wording of the text. The same text is in 55 examples (`grep -rl --include='*.xml' 'Sale to a public body: public bodies' world/examples | wc -l`).
- Condition: Where the authority's exemption reason is stated, the text states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status ("Public body: exempt from the state sales tax") and keep the code; or add a status code for public bodies to the list.
- Needs decision: no
- From: broad F4 (part), parties F3, context F6 (part)

### contest/05#F7 · Low · Addressed to one participant before the selection
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/QualificationApplicationRequest/cbc:IssueDate` = `2026-03-20`
- Why: The contest is restricted: "requests to participate, then designs from three to five selected participants" (`03-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cbc:Description` = `A restricted design contest in two stages…`). This qualification application request is addressed to Brackenmere Furniture alone on 2026-03-20, the day after the contract notice and twelve days before Brackenmere asks to participate (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:IssueDate` = `2026-04-01`); how the department knew Brackenmere as a candidate then is not visible in the flow. Counter-argument (parties, which refuted it): the procurement documents are available to interested operators from the notice on, and the named receiver is the operator that obtained them. Whether the flow should show that step is a story question.
- Condition: The receiver and the date of this document agree with the two-stage procedure: either it is addressed to a party known as interested at its issue date (and the flow shows how), or it is the general document without a single named receiver.
- Options: (preferred) say in the document (e.g. a `Note`) that it is the set of contest documents obtained by Brackenmere; or leave out the named receiver; or add the step by which Brackenmere registered its interest.
- Needs decision: yes
- From: broad F6; refuted by parties

### contest/05#F8 · Low · Registration date 1996-01-01 looks like a default, not the party's date
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday, and the same date is the registration date of 25 different companies in all three countries (271 occurrences in 181 files, recounted in the merge with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples`). That points to a filler (IND5) unless the world has a reason (e.g. one re-registration day), which the examples do not show.
- Condition: The registration date of Brackenmere Furniture is a date with a reason in the world, or the element is absent.
- Options: (preferred) give each company its own registration date from its history; or leave the element out where nothing uses it; or record a 1996 re-registration in the story. Same as every earlier flow.
- Needs decision: yes
- From: parties F6

### contest/05#F9 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: A contact is "The primary contact for this party" and should handle the party's part in this document (section 5). Brackenmere Furniture takes part in the contest through its "Trade sales" desk with a `Customer service officer` of the `Sales` department, the contact for trade customers' orders, not the office that handles a contest. The contacts are the parties' general contacts from the goods flows, the same in every example that carries these parties. Verified in the XML.
- Condition: Each contact in the example handles the party's part in the contest (requests to participate, designs and questions of the jury for a participant; appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a contact for their role (a bids or design office for the participants, a registry clerk or registrar for the review board); or leave the contact out where the electronic address is the channel.
- Needs decision: no
- From: broad F5, parties F5, context F3

### contest/05#F10 · Low · No exclusion grounds in a request that defines how exclusion grounds are addressed
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:CriterionTypeCode` = `SUITABILITY`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:CriterionTypeCode` = `TECHNICAL`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:CriterionTypeCode` = `TECHNICAL`
- Why: UBL defines the QualificationApplicationRequest as "A document issued by a buyer defining how the Exclusion Grounds and the Selection Criteria should be addressed". All three criteria are selection criteria; none is of type `EXCLUSION`, which the world's CriterionTypeCode list offers. The register extract later records "no exclusion grounds" (`13-BusinessInformation.xml`), so exclusion grounds exist in the world's procedure, but the participants are never asked to declare them (context). Whether design contests in the world have none is a story question.
- Condition: Either the request contains the exclusion grounds that apply to the contest, or the world states that design contests have none and the register check replaces the self-declaration.
- Options: (preferred) add one exclusion criterion (e.g. convictions or unpaid taxes) answered in the response; or document why the contest has none.
- Needs decision: yes
- From: context F5

### contest/05#F11 · Low · The request does not identify the contract notice whose criteria it implements
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Description` = `The two completed designs of furniture or fittings for public spaces in the last five years that the contest notice asks for.`
- Why: The request's criteria repeat the requirements of the contract notice (`03-ContractNotice.xml`) and its text points to "the contest notice", but the document has no `AdditionalDocumentReference` to it (`LPWD-DOC-26-0634`, verified: the request carries no document reference at all); the procurement is identified only by `ContractFolderID` and `ContractName`. The notice exists in two versions with different requirements for the design lead, so the reference is how the request is tied to the version it implements.
- Condition: The request refers to the contract notice `LPWD-DOC-26-0634` it implements.
- Options: (preferred) an `AdditionalDocumentReference` with `LPWD-DOC-26-0634` and a `DocumentTypeCode` or `DocumentType` saying it is the contract notice; or leave it implicit and drop the textual pointer.
- Needs decision: no
- From: logistics F1

### contest/05#F12 · Low · The coastal-site criterion asks a question that does not cover what it scores
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:Description` = `Whether one of the two references stands within one kilometre of the sea.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Description` = `The project, the client, the year and what the team designed.`
- Why: The criterion scores whether a reference stands within one kilometre of the sea, but its only property asks for "The project, the client, the year and what the team designed", the same question as the public-space reference, without the site or its distance from the sea (context; verified). A response to the property does not have to give the jury the fact the criterion is about.
- Condition: The property (or a second property) of the coastal criterion asks for the site of the reference and its distance from the sea.
- Options: (preferred) add a property for the site (place, distance from the sea); or reword the existing property.
- Needs decision: no
- From: context F4

## Checked and consistent
- Merge: every finding above was re-checked against the XML (values, positions, counts) and against the referenced examples; the definitions quoted were looked up in UBL-Entities-2.5.gc and the code meanings in `world/codelists/gc/`. The counts were redone over `*.xml` only.
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company. (from broad)
- Weights 60 + 40 = 100 for the two scored criteria, as `WeightScoringMethodologyNote` states; the professional qualification is pass/fail, as stated. (from broad)
- The criteria match the contract notice: "a registered architect" as in `03-ContractNotice.xml`, and the two references "in the last five years". (from broad)
- Criterion, property-group and property IDs (`CR-PROF`/`P-PROF-1`, `CR-REF-PUBLIC`/`P-REF-PUBLIC-1`, `CR-REF-COAST`/`P-REF-COAST-1`) are unique; the responses refer to `CR-PROF` and `P-PROF-1`. (from broad)
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). (from broad)
- The document has no amounts, prices, payment means or financial criteria (searched for `Amount`, `currencyID`, `Price`, `Payment`, `Percent` in the `*.xml`); its criteria are professional qualification and references only, so there is no money arithmetic to check. (from money)
- Brackenmere's tax registration `UL-1237398` is the same as in every other contest example that carries it (04, 05, 06, 07, 09–16) and in its register extract (13, 14). (from money)
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data). (from parties)
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address. (from parties)
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606). (from parties)
- Brackenmere's GLN 9523710900008 has a valid check digit (check_ids.py) and uses GS1 prefix 952, which GS1 reserves for demonstrations (own knowledge). (from parties)
- Criterion structure: three criteria with unique IDs (`/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:ID` = `CR-PROF`, `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-REF-PUBLIC`, `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-REF-COAST`), each with one property group and property with unique IDs; the response (06) refers to CR-PROF and P-PROF-1, which resolve here. (from logistics)
- Weights: WeightNumeric 60 and 40 add up to 100 and match WeightScoringMethodologyNote (pass/fail for the lead, references weighted 60 and 40). (from logistics)
- CR-REF-PUBLIC agrees with the contract notice's TechnicalEvaluationCriterion (two designs, five years); CR-PROF agrees with the design-lead requirement of the notice version in force (architect, CN v1). (from logistics)
- Codes: ProcedureCode DESIGNCONTEST, QualificationApplicationTypeCode REGULATED, WeightingTypeCode WEIGHTED, CriterionTypeCode SUITABILITY / TECHNICAL, EvaluationMethodTypeCode PASSFAIL / WEIGHTED, PropertyGroupTypeCode ON, TypeCode QUESTION, ValueDataTypeCode DESCRIPTION — each from the list its listID names, and the meaning fits the element. (from logistics)
- `/QualificationApplicationRequest/cbc:IssueDate` = `2026-03-20` follows the contract notice (2026-03-19). (from logistics)
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against. (from logistics)
- Weights: `/QualificationApplicationRequest/cbc:WeightScoringMethodologyNote` says pass or fail for the design lead and 60 / 40 for the references; the criteria carry `PASSFAIL`, WeightNumeric 60 and 40, which add up to 100. (from context)
- The professional criterion's Description follows the contract notice of the same version ("registered architect" in version 1, "or registered industrial designer" in version 2). (from context)
- The economic operator receiving the request (EconomicOperatorParty) is the operator that answers it in the response of the same version. (from context)

## Considered and refuted
- `/QualificationApplicationRequest/cbc:IssueTime` = `15:02:00`: suspected an order problem with the call for tenders of the same day (16:56) — refuted because the request does not depend on the call; both follow the contract notice of 2026-03-19. (from broad)
- `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:Description` = `Whether one of the two references stands within one kilometre of the sea.`: suspected that it adds a criterion the contract notice does not state — refuted because it scores a property of the two references the notice asks for, which is how a weighted criterion refines a selection criterion. (from broad)
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction rather than the party's status — refuted because the list defines it as the buyer's status ("A body of the federation, a state or a city buys free of sales tax"); its presence is part of finding F1. (from money) Accepted in the merge for the code; the wording of the text remains finding F6.
- Missing financial standing criterion (turnover): considered whether a qualification request without one lacks something the document needs — refuted because a design contest selects participants on their references and professional qualification; nothing in the flow asks for financial standing. (from money)
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better. (from parties)
- `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department. (from parties)
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name`: a qualification application request addressed to a single economic operator was suspected — refuted: the request is the questionnaire an interested operator obtains, and naming the operator that asked for it is legitimate; Brackenmere is the one that answers it (06/11). (from parties) Not followed in the merge: kept as F7, with this argument recorded there as counter-argument.
- `/QualificationApplicationRequest/cbc:CustomizationID` = `urn:ubl-examples:world:trns:qualification-application:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0`: suspected that request and response should not share one customization ID — refuted: the world uses one customization per document pair throughout (billing, order-status, tender …, counted over `*.xml`), which CustomizationID allows. (from logistics)
- `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:Name` = `The reference`: one property for "the two completed designs" — refuted: a response may give several response values for one property, so one question can collect both references. (from context)
- `/QualificationApplicationRequest/cbc:QualificationApplicationTypeCode` = `REGULATED`: fits a procedure under the procurement rules. (from context)
- `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: the economic operator's own tax registration in a qualification document — not made part of the copied-data finding, because a qualification step may check a tenderer's tax registration (it is part of its identity for the selection), unlike the contracting authority's. (from context) Not followed in the merge: kept as F4, with this argument recorded there as counter-argument.

## Changed in the merge
- broad F3 + parties F1 + context F7 → one finding, Medium, Needs decision no (as in 01-04).
- broad F4, context F6 and money F1 regrouped into three findings (customs identifier + the operator's tax scheme, Low/no; the authority's tax scheme, Low/yes; the wording, Low/no), aligned with merger B; context's refutation of the operator's tax scheme is recorded as counter-argument.
- context F3 merged into the contacts finding of broad F5 / parties F5.
- broad F6 (addressed to one participant) kept Low/yes; parties' refutation recorded as counter-argument.
- Every finding merged from several parts keeps the clearest wording and all evidence; findings are numbered by severity and then by position in the document.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews. (from parties)
