# LLM review: 14-BusinessInformation.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/14-BusinessInformation.xml`, Git blob `ea59d9c8ec70285678a63c9762adc18d4f21b15e` (committed)
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

### contest/14#F1 · Medium · Language code in LocaleCode
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is a language code, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples`, and `grep -rl` for the file count).
- Condition: no `cbc:LocaleCode` holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since none of these documents needs a locale beyond the language; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID.
- Needs decision: no

### contest/14#F2 · Low · Public bodies described as companies in a commercial register
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the public bodies of this example (Lumeport Public Works Department, Bayvarra Information Service) are registered in the `Federal business register of Bayvarra` with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"). UBL defines `Corporate Registration Scheme` as "The corporate registration scheme used to register the party" and the liquidation status as "the party's liquidation status". A department of the city, a national information service and a review board are not companies in a commercial register and cannot go into liquidation (the contracting party describes itself as "a department of the city of Lumeport" in `cac:ContractingPartyType/cbc:PartyType` where present). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for a register of public bodies, so the value is forced.
- Condition: no public body carries `CorporateRegistrationTypeCode` `COMMERCIAL` or a `CompanyLiquidationStatusCode`; if a registration scheme is given for a public body, its type says what kind of register it is.
- Options: (preferred) leave the registration type and the liquidation status out for public bodies and keep only the identifier of the register they are in; or add a public-sector register type to the list. The choice is about how the world registers public bodies, which is why it needs a decision.
- Needs decision: yes

### contest/14#F3 · Low · Customs and tax data of the contracting authority that the document does not use
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: this document belongs to a design contest; it declares no goods to customs and states no tax. The contracting authority's customs-trader number and its `PartyTaxScheme` look copied from its master data. In addition, `ExemptionReason` is defined as "A reason for the party's exemption from tax"; the code chosen means "Sale to a public body", which describes a transaction, not the status of the party, and this document records no sale.
- Condition: the contracting authority carries a customs-trader identifier and a `PartyTaxScheme` only where the document uses them; where a tax exemption of the party is stated, it is the party's own status.
- Options: (preferred) leave both out of the tendering documents; or, if the tax data stays, word the exemption reason as the party's status (a public body exempt from the state sales tax).
- Needs decision: no

### contest/14#F4 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: a contact is "The primary contact for this party" in its role in this document. Here Brackenmere Furniture takes part in a design contest through its trade-sales desk (`Customer service officer`, department `Sales`), while its partner Saltmere Engineering, where present, uses a bids office. The contacts look taken from the parties' trading master data.
- Condition: each contact named in this example is one that handles the party's role in the contest (tenders and competitions for a participant, appeals for the review board).
- Options: (preferred) give each party a contact for its role (e.g. a tenders or design office for the participants, a registry clerk or case officer for the review board); or leave the contact out where the role needs none.
- Needs decision: no

### contest/14#F5 · Low · Production capability given as an amount without saying what it measures
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00`
- Why: `Capability. Value Amount` is "A monetary amount as a measure of this capability". With the type `PRODUCTION` and the description "Furniture of wood and steel, designed and made in its own workshop", the reader cannot tell whether the amount is annual turnover, the value of annual production or the capacity of the workshop, nor for which period. For a register extract used in a selection, that is the information needed to use the figure.
- Condition: the capability says what the amount measures and for which period (e.g. with a `ValidityPeriod` and a description or a type that names the measure).
- Options: (preferred) add the period (`cac:ValidityPeriod`) and name the measure in the description (e.g. "turnover of the financial year 2025"); or use a capability type for turnover if the list has one.
- Needs decision: no

### contest/14#F6 · Low · Only the lead member's register extract; the group member is not covered
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/BusinessInformation/cbc:BriefDescription` = `Brackenmere Furniture: registered, no exclusion grounds recorded.`
- Why: the participant is a group, "Brackenmere and Saltmere design team" (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`), with Saltmere Engineering as member (`07-TendererQualification.xml`, 40 %, and 30 % in `12-TendererQualification.xml`). The extract states "no exclusion grounds recorded" for Brackenmere only; no extract for Saltmere Engineering exists in the flow, although exclusion grounds are normally checked for every member of a group.
- Condition: the flow shows that the exclusion grounds of every member of the group were checked, or says why the member is not checked.
- Options: (preferred) add an extract for Saltmere Engineering (a separate BusinessInformation example), or a `BusinessPartyGroup` if the register issues one extract for a group; or state in the story why the member need not be checked. Adding a document is a decision.
- Needs decision: yes

### contest/14#F7 · Low · Registration date on New Year's Day
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `Party Legal Entity. Registration Date` is "The registration date of the CompanyID". 1 January is a public holiday in most registers' calendars and a typical placeholder for "year only"; in a register extract, the registration date is part of what the extract certifies. (Own knowledge; the world's calendar of holidays is not checked here.)
- Condition: the registration date is a real date on which the register could have registered the company.
- Options: (preferred) use the actual registration date of Brackenmere in the world's story; or leave it out if only the year is known.
- Needs decision: no

### contest/14#F8 · Low · Version 2 changes the capability amount without saying why
- XPath: `/BusinessInformation/cbc:VersionID` = `2`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00`
- Why: version 2 of the extract, four days after version 1, changes only the amount from `6410000.00` (`13-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6410000.00`) to `6830000.00`. Nothing says whether this corrects an error or reflects new accounts filed in between, which matters to the department that uses the figure for the selection.
- Condition: the extract says why the figure changed (correction, or new period).
- Options: (preferred) add a `Note` (and, if it is a new period, the capability's validity period); or another means the register uses for corrections.
- Needs decision: no

## Checked and consistent
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company.
- `NoticeTypeCode` `BUSREG` (business registration notice) and `NoticeSubType` `EXTRACT` (register extract) fit the note "Extract from the register of economic operators" and the document type.
- Sender (the national information service), receiver (the contracting authority) and business party (Brackenmere Furniture) fit a register extract requested for a selection; the extract is issued after the request period ends (2026-05-02) and before the tender deadline (2026-06-12).
- Brackenmere's legal entity (SMALL, LTD, active) is the same as in the tenderer qualifications; a turnover-scale amount of 6.4 to 6.8 million lume is plausible for a small enterprise against the contest's 900 lume per bench.
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files).

## Considered and refuted
- `/BusinessInformation/cbc:BriefDescription` = `Brackenmere Furniture: registered, no exclusion grounds recorded.`: suspected that the exclusion statement has no structured counterpart — refuted because BusinessInformation has no element for exclusion grounds, so the brief description is where it belongs.
- `/BusinessInformation/cbc:IssueDate` = `2026-05-09`: suspected that a new extract four days later is unnecessary — refuted because the changed amount gives the version a reason (its explanation is the subject of a finding).
