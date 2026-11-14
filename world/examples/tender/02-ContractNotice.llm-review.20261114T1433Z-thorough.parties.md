# LLM review: 02-ContractNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/02-ContractNotice.xml`, Git blob `1902067078eeb7c2dc70b632a4e813bb3c440b21` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/02#F1 · Medium · Language code in LocaleCode
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en`, with `listID="ISO 639"`, is the language code already given in `cbc:ID` of the same `cac:Language`; it names no locale (a locale says where or in which variant the language is used, as the `en-XB` and `en-XU` tags on texts in this flow do). The same value occurs 362 times in 213 of the 250 examples (`grep -r --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'` over `world/examples`, lines and files counted).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is either absent or holds a locale, with a `listID` that names a list of locales.
- Options: Remove `cbc:LocaleCode` (preferred: `cbc:ID` already states the language and nothing in the document uses a locale); or give the locale (`en-XB`) with a matching list.
- Needs decision: no

### tender/02#F2 · Low · Master data the document does not use (customs trader number)
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Section 4.8 of the review rules: data copied from a party's master data into a document that does nothing with it. The customs trader numbers identify the parties towards customs; this ContractNotice is a tendering document and declares nothing to customs (such numbers matter in customs declarations, as in examples 30 and 31 of the flow).
- Condition: The document carries, for each party, only the identifiers and related parties that its purpose uses.
- Options: Leave these out of the tendering documents (preferred); or keep them only where the document says what they are for.
- Needs decision: no

### tender/02#F3 · Low · Party tax exemption reason worded as a transaction
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/cbc:ExemptionReason` as "A reason for the party's exemption from tax, expressed as text": the party's own status. The text starts with "Sale to a public body", which describes a transaction (a sale by someone else to the department); the code `PUBLIC` comes from a list whose other entries are reasons of a transaction or of goods (`EXP` export, `WATER`, `FOOD`, `RESALE`). What the party itself is, is a public body that buys free of the state sales tax.
- Condition: The exemption reason of the party states the party's status (a public body exempt from the state sales tax), not a kind of sale.
- Options: Reword the text to the party's status, e.g. "Public body: buys free of the state sales tax" (preferred; the code can stay, its definition "A body of the federation, a state or a city buys free of sales tax" fits); or keep the transaction wording only on tax categories of invoices.
- Needs decision: no

### tender/02#F4 · Low · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The legal entity of Bayvarra Information Service, Lumeport Public Works Department, Procurement Review Board of Bayvarra is described like a company: `CompanyLiquidationStatusCode` ("A code signifying the party's liquidation status") `ACTIVE` ("Active, not in liquidation"), registered in a scheme of type `COMMERCIAL` (code list: "Commercial register: A register of businesses"). The department is a public body (`/ContractNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`), and the information service and the review board are public bodies as well (ISIC 8411 and 8423, public administration). A city department or a public board is not a business in a commercial register and cannot be in liquidation, so the status and the register type say something that has no meaning for these parties.
- Condition: A public body carries no liquidation status, and the register it is identified in is not typed as a commercial register (or the description says in what capacity a public body is entered there).
- Options: Leave out `CompanyLiquidationStatusCode` for public bodies and type their registration scheme differently (preferred; a register type for public bodies would need a code), or leave out the `CorporateRegistrationScheme` details and keep only the identifier.
- Needs decision: no

### tender/02#F5 · Low · Roles filled with the contracting party itself, adding nothing
- XPath: `/ContractNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: Each of these roles names the Lumeport Public Works Department, by register number and name only: the same party that is the `ContractingParty` of this document, with no contact, address or other detail that differs per role. The roles exist for the case that another party (or another office) originates the need, benefits, hands out the documents, receives or evaluates the tenders. Filled with the contracting party itself they say nothing the document does not already say (rule "no fillers, and nothing implied by absence"). The contracting party states that it acts `/ContractNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationType` = `On its own behalf`.
- Condition: Each of these roles is present only where it names a party, office or contact that differs from the contracting party, or adds details (a contact, an address) specific to the role.
- Options: Leave out the roles that only repeat the contracting party (preferred); or give each kept role what distinguishes it (e.g. the contact that receives tenders).
- Needs decision: no

### tender/02#F6 · Low · Technical committee of three officers, one named
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:TechnicalCommitteeDescription` = `Three officers of the department.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:JobTitle` = `Head of parks`
- Why: `TechnicalCommitteePerson` is "A member of a committee of experts evaluating the subjective criteria for awarding the contract" (0..n). The description says the committee has three officers of the department; one person is listed. A reader cannot tell whether the other two are unnamed on purpose or missing. The person is the same in every example of the flow that names the committee (01, 02, 03, 24).
- Condition: The persons listed and the description agree: all members are listed, or the description says that only the chair (or one member) is named.
- Options: Say in the description that Mara Delling chairs the committee and the other two members are appointed later (preferred, least change); or list all three.
- Needs decision: no

### tender/02#F7 · Low · Contact of the review board described as a procurement officer
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: The contact of the party that receives appeals is named `Registry`, but its job title is `Procurement officer` and its department `Procurement`. A review board decides on appeals against procurement decisions; its registry does not buy. Job title and department are identical to those of the contracting department's own contact in this example, and do not agree with the contact name (checklist: "Do job title, department and name agree with each other?").
- Condition: Name, job title and department of the contact describe the same function, one that fits the party's role in this document.
- Options: Give the contact a job title and department of its own function (e.g. registrar / registry; bid manager / sales) (preferred).
- Needs decision: no

### tender/02#F8 · Low · Location of the opening named after the organisation, without an address
- XPath: `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- Why: `OccurrenceLocation` is "The location of this event" and its `Name` "The name of this location". The value is the name of the department followed by the square: the organisation, not a place (checklist: "the name is the place, not the company"). The same building is identified elsewhere in this example by an address with a register identifier (`/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`, Civic Square 6), which the location does not use. The event is described as an electronic opening that tenderers follow online, so the physical place matters little; if it is given, it should be findable.
- Condition: The location of the opening is a place: a name of a room or building and/or the address (or address identifier) of the building; or it is absent for a purely electronic opening.
- Options: Give the location the address of Civic Square 6 with its register identifier, and a room name (preferred); or leave the location out and keep the description.
- Needs decision: no

## Checked and consistent
- Parties and roles: Lumeport Public Works Department as AdditionalInformationParty, BeneficiaryParty, ContractResponsibleParty, ContractingParty, DocumentProviderParty, OriginatorCustomerParty, QualificationRequestRecipientParty, SignatoryParty, TenderEvaluationParty, TenderRecipientParty; Bayvarra Information Service as ReceiverParty; Procurement Review Board of Bayvarra as AppealInformationParty, AppealReceiverParty, MediationParty. Each is the party the role's definition asks for (apart from the findings).
- Every party is identified by the same register number wherever it is named in this example, and the full descriptions (identifiers, address, tax scheme, legal entity, contact, electronic address) are identical, element by element, to those of the same party in all other examples of the tender flow that carry it (compared by script over the 36 `*.xml` of the flow and over the other flows), apart from what the findings and the refuted candidates below say.
- `check_ids.py`: no identifier with a check digit in this example.
- ISIC Rev. 4 classes fit the parties (own knowledge of ISIC): 8411 general public administration, 8423 public order and safety (review board).
- Telephone numbers use the country code +999, which is not assigned to a country (own knowledge of ITU-T E.164); all web and mail addresses are in `.example`.

## Considered and refuted
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: suspected that `-1` is not a valid form of a time zone offset — refuted because the definition ("as an offset from Universal Coordinated Time (UTC)") prescribes no format and the value reads unambiguously as UTC−1; it is the same for all addresses of the flow.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: suspected that `Room 2.14` belongs in `cbc:Room` — refuted because `InhouseMail` is "The specific identifable location within a building where mail is delivered", and a room where the procurement office takes its mail is such a location; `Room` would also be defensible.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: suspected that a contact named after an office (`Procurement office`) with a job title is inconsistent, and that the address department `Procurement office` differs from the contact department `Procurement` — refuted because UBL recommends a functional name for `Contact/cbc:Name`, and the two department wordings name the same unit.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: suspected that `STATE` contradicts the party type "local authority" — refuted because `TaxLevelCode` is the level of the tax within the scheme (the state sales tax), not the level of government of the party.
- `/ContractNotice/cac:TenderingTerms/cac:ContractResponsibleParty`: suspected that "The Party who executes the Contract" means the contractor, who is not known yet — refuted because the role is a party on the buyer's side in the tendering terms (the body that administers the contract); the department fits. (That it only repeats the contracting party is the finding on repeated roles.)
- `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:MediationParty`: suspected that the review board cannot be both the receiver of appeals and the mediator — refuted because nothing in UBL or in the world forbids a review board that also mediates; the party is identified consistently in the three appeal roles.
- `/ContractNotice/cac:ReceiverParty`: suspected that an information service is not a proper receiver of a notice — refuted because the notice is sent for publication, and the publication service is "the Party receiving this Document"; its contact (`Publications and register`) fits that.
