# LLM review: 07-TendererQualification.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/07-TendererQualification.xml`, Git blob `b7c5c10127f35b254eea1a4905b11113ef334e8c` (committed)
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

### contest/07#F1 · Medium · One completed task declared where the contest asks for two references
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Seating for the Lumeport central library's reading garden, 2024.`
- XPath: `03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2`
- Why: The tenderer qualification is "A document declaring the qualifications of a tenderer", and `CompletedTask` is "A former task completed by this qualifying party". The contract notice requires two completed designs of furniture or fittings for public spaces in the last five years (threshold 2, five years), the jury selects on these references, and the request scores a second, coastal reference at 40. The team declares one completed task (Brackenmere, 2024) and none for the member Saltmere Engineering (verified: one `CompletedTask` in the document); the response of the same day does not answer the reference criteria either (`06-QualificationApplicationResponse.xml`). On what the flow shows, the team does not meet the threshold it is later selected and ranked on (`15-ContractAwardNotice.xml`). Medium (broad, logistics; context gave Low): the information the document's purpose depends on is missing.
- Condition: The qualifying parties together declare at least two completed tasks that meet the criterion (public-space furniture or fittings, completed within five years), one of them on a coastal site, or the flow states why one suffices.
- Options: (preferred) add a second `CompletedTask` (for Brackenmere or Saltmere) with period and description, one of the two near the sea; or record that one suffices (a story change, unlikely).
- Needs decision: no
- From: broad F2, logistics F1, context F2

### contest/07#F2 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language as used in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is the ISO 639 language code itself, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale (section 6 names a language code in `LocaleCode` as Medium). Verified in the XML at every place listed. The same value occurs 362 times in 213 examples (recounted in the merge with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l` and `grep -rl` for the file count; a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also matches other `…LocaleCode` elements).
- Condition: No `cbc:LocaleCode` in the example holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since nothing in the document needs a locale beyond the language that `Language/cbc:ID` already gives; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID. Same as every earlier flow.
- Needs decision: no
- From: broad F1, parties F2, context F1

### contest/07#F3 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The public body of this example (Lumeport Public Works Department) is entered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carries `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). A city department (and, where present, a federal information service or a review board) is not a business in a register of businesses and is not wound up by liquidation; the contracting party describes itself as "a department of the city of Lumeport" (`ContractingPartyType/PartyType`), and its ISIC class is 8411 (public administration). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no type for a register of public bodies, so the value is forced. Verified in the XML. The values carry a meaning that does not fit the party (Medium, as the customs authority described as a company in the earlier flows). Parties added that a city department is not a legal person at all; the legal entity behind it is the City of Lumeport.
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; a registration scheme given for a public body says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep only the register name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list; or give the City of Lumeport as the department's legal entity (this last option changes who the party is and would need a decision).
- Needs decision: no
- From: broad F3, parties F1, context F6

### contest/07#F4 · Low · Note gives the engineering firm only the structure while the design lead is its architect
- XPath: `/TendererQualification/cbc:Note` = `The furniture maker leads the team; the engineering firm does the structure and the anchoring.`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40`
- XPath: `06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Edda Corwin of Saltmere Engineering…`
- Why: The note says the engineering firm "does the structure and the anchoring", but the response of the same day names the design lead as "Edda Corwin of Saltmere Engineering, … a registered architect". The team's design is then led by the firm that, by this note, only does the structure. Counter-argument (context, which refuted it): leading the team and being the design lead are different roles, and an engineering firm can employ the architect. Version 2 (`12-TendererQualification.xml`) no longer has the tension. Needs decision set to yes, as for the same problem in `06-QualificationApplicationResponse.xml` (parties): the merge cannot settle which reading is meant.
- Condition: The note and the response agree on what Saltmere Engineering does in the team.
- Options: (preferred) extend the note to "the design lead and the structure and anchoring"; or let the design lead belong to Brackenmere in version 1 as well.
- Needs decision: yes
- From: broad F6; refuted by context

### contest/07#F5 · Low · BusinessIdentityEvidenceID holds the party's register number, and only for the lead
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID` = `20412466`
- Why: `QualifyingParty. Business Identity Evidence. Identifier` is "An identifier for an item of evidence to support the business identity of this qualifying party". The value is Brackenmere's own register number, the same as its `CompanyID` and `PartyIdentification`, not the identifier of a piece of evidence (an extract, a certificate); the member Saltmere has none (context, parties). Counter-argument (broad and logistics, which refuted it): the register entry is the evidence of business identity, and its number, with the register's schemeID, identifies it. Both readings are possible.
- Condition: `BusinessIdentityEvidenceID` identifies an item of evidence (a document) for each qualifying party that gives one, or is absent.
- Options: (preferred) leave it out, because the register number is already in the legal entity; or give the identifier of an actual register extract.
- Needs decision: yes
- From: context F3, parties F7; refuted by broad and logistics

### contest/07#F6 · Low · Registration date 1996-01-01 looks like a default, not the party's date
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday, and the same date is the registration date of 25 different companies in all three countries (271 occurrences in 181 files, recounted in the merge with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples`). That points to a filler (IND5) unless the world has a reason (e.g. one re-registration day), which the examples do not show.
- Condition: The registration date of Brackenmere Furniture is a date with a reason in the world, or the element is absent.
- Options: (preferred) give each company its own registration date from its history; or leave the element out where nothing uses it; or record a 1996 re-registration in the story. Same as every earlier flow.
- Needs decision: yes
- From: parties F6

### contest/07#F7 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: A contact is "The primary contact for this party" and should handle the party's part in this document (section 5). Brackenmere Furniture takes part in the contest through its "Trade sales" desk with a `Customer service officer` of the `Sales` department, the contact for trade customers' orders, not the office that handles a contest. Saltmere Engineering's "Bids office" is staffed by a `Procurement officer` of a `Procurement` department; a bidder's bids office prepares tenders (a sales function), procurement is buying. The contacts are the parties' general contacts from the goods flows, the same in every example that carries these parties. Verified in the XML.
- Condition: Each contact in the example handles the party's part in the contest (requests to participate, designs and questions of the jury for a participant; appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a contact for their role (a bids or design office for the participants, a registry clerk or registrar for the review board); or leave the contact out where the electronic address is the channel.
- Needs decision: no
- From: broad F5, parties F5, context F4

### contest/07#F8 · Low · Saltmere Engineering's legal entity gives no legal form
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Saltmere Engineering`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Brackenmere Furniture Ltd`
- Why: `PartyLegalEntity/RegistrationName` is "The name of the party as registered with the relevant legal authority". Saltmere is entered in the federal business register, but its registered name has no legal-form suffix and its legal entity has no `CompanyLegalFormCode` (verified), whereas the lead's registered name is "Brackenmere Furniture Ltd" with form `LTD`. For a group that the contest requires to form a limited company before the follow-up contract, the members' legal forms are relevant (parties). The same description of Saltmere is used in the tender and mast flows.
- Condition: Saltmere Engineering's registered name and legal form are those of a registered business, consistent with how other registered companies are described.
- Options: (preferred) give Saltmere its registered name with legal form and `CompanyLegalFormCode`; or, if it is a sole trader or partnership in the world, say so in the legal form.
- Needs decision: no
- From: parties F8

### contest/07#F9 · Low · Customs and tax master data the procurement document does nothing with
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1232055`
- Why: `AdditionalPartyIdentification` is "One or more additional identifiers for this Party". The customs trader number (scheme `urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works Department towards customs and is used in its customs declarations (e.g. `tender/31-ImportCustomsDeclaration.xml`); this TendererQualification is a procurement document of a design contest for a service: nothing is imported, declared or transported, and nobody in the document uses the number. It is copied from the party's master data (section 4.8; the value is in 55 examples, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted in the merge). The same holds for the economic operators' own `PartyTaxScheme` ("A tax scheme applying to this party"): nothing in this document is taxed, priced, invoiced or paid, and no criterion refers to a tax registration (money). Counter-argument (context, in 05-07): a qualification step may check a tenderer's tax registration as part of its identity; the request of this flow, however, asks for no such check, so the argument does not give the value a use here.
- Condition: The contracting authority carries no customs trader identifier in this procurement document, and the economic operators carry a `PartyTaxScheme` only where the document uses it.
- Options: (preferred) leave these values out of the procurement documents and keep them where documents use them (customs declarations, invoices); or keep one only where the story gives this document a reason, and say so.
- Needs decision: no
- From: broad F4 (part), parties F4, logistics F2, context F5 (part), money F1 (part)

### contest/07#F10 · Low · Tax scheme of the contracting authority in a document that may not use it
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". The contracting authority brings its state sales tax registration and exemption into a procurement document. This document states no amount at all: nothing in it is priced, taxed or paid. Broad and context (and money from 05 on) read it as master data copied into a document that does not use it (section 4.8). Money (01-04, 08) refuted that: the buyer's exemption tells candidates that the amounts of the contest and of the follow-up contract are net of the state sales tax. Both readings are possible; the merge could not settle which the world intends, although in this document, which has no amounts, the money argument is weaker.
- Condition: Either the authority's `PartyTaxScheme` is absent from this document, or the world states that procurement documents carry it to show that amounts are net of sales tax (and it is then carried consistently).
- Options: (preferred) leave it out of documents without amounts and decide for the notices whether the exemption is meant as information to candidates (then keep it and say so where amounts are given); or keep it everywhere as the buyer's tax status.
- Needs decision: yes
- From: broad F4 (part), context F5 (part), money F1 (part)

### contest/07#F11 · Low · Exemption reason of the contracting authority worded as a sale
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", i.e. the party's own status. The text begins "Sale to a public body", the name of the code in the Bayvarran exemption list (whose other codes are reasons for exempt supplies), and so describes a transaction; this document records no sale. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Money refuted the code itself, rightly: the list describes `PUBLIC` as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (verified in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`). What remains is the wording of the text. The same text is in 55 examples (`grep -rl --include='*.xml' 'Sale to a public body: public bodies' world/examples | wc -l`).
- Condition: Where the authority's exemption reason is stated, the text states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status ("Public body: exempt from the state sales tax") and keep the code; or add a status code for public bodies to the list.
- Needs decision: no
- From: broad F4 (part), parties F3, context F5 (part)

## Checked and consistent
- Merge: every finding above was re-checked against the XML (values, positions, counts) and against the referenced examples; the definitions quoted were looked up in UBL-Entities-2.5.gc and the code meanings in `world/codelists/gc/`. The counts were redone over `*.xml` only.
- Participation 60 + 40 = 100 %; lead and member roles agree with the note and with the group name of the response. (from broad)
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company. (from broad)
- Completed task period 2024-03-01 to 2024-09-30 lies within the five years before the contract notice. (from broad)
- Saltmere Engineering's address, register and tax registration are in Upland State like Brackenmere's; it appears only in the two tenderer qualifications, described the same way in both. (from broad)
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). (from broad)
- Shares of the group: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `60` and `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40` add up to 100 (calculated). (from money)
- The document has no amounts, prices or payment data (searched for `Amount`, `currencyID`, `Price`, `Payment` in the `*.xml`). (from money)
- The tax registrations of Brackenmere (`UL-1237398`) and Saltmere (`UL-1232055`) are the same in 07 and 12. (from money)
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data). (from parties)
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address. (from parties)
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606). (from parties)
- Brackenmere's GLN 9523710900008 has a valid check digit (check_ids.py) and uses GS1 prefix 952, which GS1 reserves for demonstrations (own knowledge). (from parties)
- Participation percentages of the two qualifying parties add up to 100 (60 + 40). (from parties)
- Participation: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `60` and `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40` add up to 100 %. (from logistics)
- Roles: TendererRoleCode LEAD for Brackenmere and MEMBER for Saltmere Engineering, consistent with the Note and with the contract notice's EconomicOperatorRole LEAD (the group names a lead member). (from logistics)
- Completed task period 2024-03-01 to 2024-09-30 lies within the five years before the issue date and agrees with the year in its description. (from logistics)
- Identifiers: Brackenmere register 20412466 and GLN 9523710900008 (check digit correct), Saltmere Engineering register 20410685 with its endpoint XB:20410685 and address UL-ADR-587295; the department 20410548. (from logistics)
- `/TendererQualification/cbc:IssueDate` = `2026-04-01`, before the participation deadline 2026-04-18. (from logistics)
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against. (from logistics)
- ParticipationPercent of lead and member add up to 100 (`60` + `40`). (from context)
- TendererRoleCode `LEAD` / `MEMBER` agree with the Note ("The furniture maker leads the team") and with the contract notice's requirement that a group names a lead member. (from context)
- The completed task lies within the five-year window (2024-03-01 to 2024-09-30). (from context)

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`: suspected that a register number is not an "identifier for an item of evidence" — refuted because the register entry is the evidence of business identity, and its number identifies it; the schemeID names the register. (from broad) Not followed in the merge: kept as F5, with this argument recorded there as counter-argument.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`: suspected a conflict with the notices' `EconomicOperatorRoleCode` list — refuted because the two elements have separate lists in the world that share the codes LEAD and MEMBER with the same meaning. (from broad)
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent`: considered whether the shares should match a split of prize money or of the follow-up fee — refuted because no document of the flow states such a split; the percentage is the members' share in the group, as its definition says. (from money)
- `/TendererQualification/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better. (from parties)
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department. (from parties)
- `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cbc:IndustryClassificationCode`: Saltmere's industry classification 4290 "Construction of other civil engineering projects" was suspected not to fit a firm that provides the structural design and (in version 1 of the response) the design lead — refuted because a civil engineering contractor commonly designs structures and anchorings and employs engineers and architects, and Saltmere acts as a construction customer in other flows (mast), where 4290 fits; the code describes its main activity, not its share in this team. (from parties)
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`: suspected that the party's register number is not "an identifier for an item of evidence" — refuted: the evidence of business identity is the registration in the federal business register, and its number, with the register's schemeID, is how that evidence is identified and checked (as the extract 13/14 does). (from logistics) Not followed in the merge: kept as F5, with this argument recorded there as counter-argument.
- `/TendererQualification/cbc:Note` = `The furniture maker leads the team; the engineering firm does the structure and the anchoring.`: suspected a contradiction with the response of version 1, where the design lead is "of Saltmere Engineering" — refuted: leading the team (consortium lead) and being the design lead are different roles, and an engineering firm can employ the registered architect. (from context) Not followed in the merge: kept as F4, with this argument recorded there as counter-argument.
- `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cbc:IndustryClassificationCode` = `4290`: suspected that a firm doing structure and anchoring of a bench design should be classed as engineering services (ISIC 7110) — refuted: Saltmere Engineering is a civil engineering contractor in other flows (tender), and the classification is the party's, not the task's. (from context)
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`: the economic operator's own tax registration in a qualification document — not made part of the copied-data finding, because a qualification step may check a tenderer's tax registration (it is part of its identity for the selection), unlike the contracting authority's. (from context) Not followed in the merge: kept as F9, with this argument recorded there as counter-argument.

## Changed in the merge
- broad F2 + logistics F1 (Medium) + context F2 (Low) → one finding, Medium: the stated threshold is not met by what the document declares, and its purpose depends on it.
- broad F3 + parties F1 + context F6 → one finding, Medium, Needs decision no (as in 01-06).
- broad F6 (note vs design lead) Needs decision no → yes, aligned with the same problem in 06 (parties F8), because context refuted it with a reading the merge cannot dismiss.
- context F3 + parties F7 (BusinessIdentityEvidenceID) → one finding, Needs decision no → yes, because broad and logistics refuted it.
- broad F4, context F5 and money F1 regrouped into three findings (customs identifier + both members' tax schemes, Low/no; the authority's tax scheme, Low/yes; wording, Low/no), aligned with merger B.
- context F4 merged into the contacts finding of broad F5 / parties F5; Saltmere's contact (parties) included.
- Every finding merged from several parts keeps the clearest wording and all evidence; findings are numbered by severity and then by position in the document.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews. (from parties)
