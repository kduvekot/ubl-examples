# LLM review: 07-TendererQualification.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/07-TendererQualification.xml`, Git blob `b7c5c10127f35b254eea1a4905b11113ef334e8c` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
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

### contest/07#F1 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is a language code, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples`, and `grep -rl` for the file count).
- Condition: no `cbc:LocaleCode` holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since none of these documents needs a locale beyond the language; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID.
- Needs decision: no

### contest/07#F2 · Medium · One completed task declared where the contest asks for two references
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Seating for the Lumeport central library's reading garden, 2024.`
- Why: the contest asks for "Two completed designs of furniture or fittings for public spaces in the last five years" (threshold `03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2`), and the jury selects on these references. The tenderer qualification, "A document declaring the qualifications of a tenderer", lists one `CompletedTask` for Brackenmere and none for Saltmere Engineering; the response (`06-QualificationApplicationResponse.xml`) does not supply them either. The team nevertheless is selected and wins the first prize (`15-ContractAwardNotice.xml`).
- Condition: the qualifications declared by the team include at least two completed designs for public spaces within the five years before the notice, one of them for a coastal site if it is to score on `CR-REF-COAST`.
- Options: (preferred) add the second completed task (for Brackenmere or Saltmere) with its period, and make sure one stands by the sea; or explain why one reference suffices.
- Needs decision: no

### contest/07#F3 · Low · Public bodies described as companies in a commercial register
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the public bodies of this example (Lumeport Public Works Department) are registered in the `Federal business register of Bayvarra` with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"). UBL defines `Corporate Registration Scheme` as "The corporate registration scheme used to register the party" and the liquidation status as "the party's liquidation status". A department of the city, a national information service and a review board are not companies in a commercial register and cannot go into liquidation (the contracting party describes itself as "a department of the city of Lumeport" in `cac:ContractingPartyType/cbc:PartyType` where present). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for a register of public bodies, so the value is forced.
- Condition: no public body carries `CorporateRegistrationTypeCode` `COMMERCIAL` or a `CompanyLiquidationStatusCode`; if a registration scheme is given for a public body, its type says what kind of register it is.
- Options: (preferred) leave the registration type and the liquidation status out for public bodies and keep only the identifier of the register they are in; or add a public-sector register type to the list. The choice is about how the world registers public bodies, which is why it needs a decision.
- Needs decision: yes

### contest/07#F4 · Low · Customs and tax data of the contracting authority that the document does not use
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: this document belongs to a design contest; it declares no goods to customs and states no tax. The contracting authority's customs-trader number and its `PartyTaxScheme` look copied from its master data. In addition, `ExemptionReason` is defined as "A reason for the party's exemption from tax"; the code chosen means "Sale to a public body", which describes a transaction, not the status of the party, and this document records no sale.
- Condition: the contracting authority carries a customs-trader identifier and a `PartyTaxScheme` only where the document uses them; where a tax exemption of the party is stated, it is the party's own status.
- Options: (preferred) leave both out of the tendering documents; or, if the tax data stays, word the exemption reason as the party's status (a public body exempt from the state sales tax).
- Needs decision: no

### contest/07#F5 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: a contact is "The primary contact for this party" in its role in this document. Here Brackenmere Furniture takes part in a design contest through its trade-sales desk (`Customer service officer`, department `Sales`), while its partner Saltmere Engineering, where present, uses a bids office. The contacts look taken from the parties' trading master data.
- Condition: each contact named in this example is one that handles the party's role in the contest (tenders and competitions for a participant, appeals for the review board).
- Options: (preferred) give each party a contact for its role (e.g. a tenders or design office for the participants, a registry clerk or case officer for the review board); or leave the contact out where the role needs none.
- Needs decision: no

### contest/07#F6 · Low · Note gives the engineering firm only the structure while the design lead is its architect
- XPath: `/TendererQualification/cbc:Note` = `The furniture maker leads the team; the engineering firm does the structure and the anchoring.`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40`
- Why: the note says "the engineering firm does the structure and the anchoring", but the response of the same day names the design lead as "Edda Corwin of Saltmere Engineering, … a registered architect" (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `The design lead, Edda Corwin of Saltmere Engineering…`). The team's design is then led by the firm that, by this note, only does the structure. Version 2 (`12-TendererQualification.xml`, design lead Ivo Harlan, Saltmere at 30 %) no longer has this tension.
- Condition: the note and the response agree on what Saltmere Engineering does in the team.
- Options: (preferred) extend the note to "the design lead and the structure and anchoring"; or let the design lead belong to Brackenmere in version 1 as well.
- Needs decision: no

## Checked and consistent
- Participation 60 + 40 = 100 %; lead and member roles agree with the note and with the group name of the response.
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company.
- Completed task period 2024-03-01 to 2024-09-30 lies within the five years before the contract notice.
- Saltmere Engineering's address, register and tax registration are in Upland State like Brackenmere's; it appears only in the two tenderer qualifications, described the same way in both.
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files).

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`: suspected that a register number is not an "identifier for an item of evidence" — refuted because the register entry is the evidence of business identity, and its number identifies it; the schemeID names the register.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`: suspected a conflict with the notices' `EconomicOperatorRoleCode` list — refuted because the two elements have separate lists in the world that share the codes LEAD and MEMBER with the same meaning.
