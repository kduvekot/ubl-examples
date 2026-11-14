# LLM review: 03-CallForTenders.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/03-CallForTenders.xml`, Git blob `24f08018e3295692f3f3cc82e4d7e61355b48c44` (committed)
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

### tender/03#F1 · Medium · Language code in LocaleCode
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en`, with `listID="ISO 639"`, is the language code already given in `cbc:ID` of the same `cac:Language`; it names no locale (a locale says where or in which variant the language is used, as the `en-XB` and `en-XU` tags on texts in this flow do). The same value occurs 362 times in 213 of the 250 examples (`grep -r --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'` over `world/examples`, lines and files counted).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is either absent or holds a locale, with a `listID` that names a list of locales.
- Options: Remove `cbc:LocaleCode` (preferred: `cbc:ID` already states the language and nothing in the document uses a locale); or give the locale (`en-XB`) with a matching list.
- Needs decision: no

### tender/03#F2 · Medium · Province in Region
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/cbc:Region` as "The recognized geographic or economic region or group of countries in which this address is located", and `cbc:CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province of Urvania is a country subentity, not a region; the Bayvarran addresses of this flow put their state in `cbc:CountrySubentity`. `Province of Ferrano` in `cbc:Region` occurs 219 times in 104 of the 250 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'` over `world/examples`).
- Condition: The province of an Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list), and `cbc:Region` is absent or holds a region in the sense of the definition.
- Options: Move the value to `cbc:CountrySubentity` (preferred); a code for the province is optional.
- Needs decision: no

### tender/03#F3 · Low · Master data the document does not use (customs trader number, logistics service provider)
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- Why: Section 4.8 of the review rules: data copied from a party's master data into a document that does nothing with it. The customs trader numbers identify the parties towards customs; this CallForTenders is a tendering document and declares nothing to customs (such numbers matter in customs declarations, as in examples 30 and 31 of the flow). The `ServiceProviderParty` ("A party providing a service to this party") names Castrano Logistics as Valdara's provider of "Warehousing and despatch", with a contact at the provider; nothing in this document concerns warehousing or despatch (Castrano acts in `29-DespatchAdvice.xml`).
- Condition: The document carries, for each party, only the identifiers and related parties that its purpose uses.
- Options: Leave these out of the tendering documents (preferred); or keep them only where the document says what they are for.
- Needs decision: no

### tender/03#F4 · Low · Party tax exemption reason worded as a transaction
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/cbc:ExemptionReason` as "A reason for the party's exemption from tax, expressed as text": the party's own status. The text starts with "Sale to a public body", which describes a transaction (a sale by someone else to the department); the code `PUBLIC` comes from a list whose other entries are reasons of a transaction or of goods (`EXP` export, `WATER`, `FOOD`, `RESALE`). What the party itself is, is a public body that buys free of the state sales tax.
- Condition: The exemption reason of the party states the party's status (a public body exempt from the state sales tax), not a kind of sale.
- Options: Reword the text to the party's status, e.g. "Public body: buys free of the state sales tax" (preferred; the code can stay, its definition "A body of the federation, a state or a city buys free of sales tax" fits); or keep the transaction wording only on tax categories of invoices.
- Needs decision: no

### tender/03#F5 · Low · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The legal entity of Lumeport Public Works Department, Procurement Review Board of Bayvarra is described like a company: `CompanyLiquidationStatusCode` ("A code signifying the party's liquidation status") `ACTIVE` ("Active, not in liquidation"), registered in a scheme of type `COMMERCIAL` (code list: "Commercial register: A register of businesses"). The department is a public body (`/CallForTenders/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`), and the information service and the review board are public bodies as well (ISIC 8411 and 8423, public administration). A city department or a public board is not a business in a commercial register and cannot be in liquidation, so the status and the register type say something that has no meaning for these parties.
- Condition: A public body carries no liquidation status, and the register it is identified in is not typed as a commercial register (or the description says in what capacity a public body is entered there).
- Options: Leave out `CompanyLiquidationStatusCode` for public bodies and type their registration scheme differently (preferred; a register type for public bodies would need a code), or leave out the `CorporateRegistrationScheme` details and keep only the identifier.
- Needs decision: no

### tender/03#F6 · Low · Roles filled with the contracting party itself, adding nothing
- XPath: `/CallForTenders/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: Each of these roles names the Lumeport Public Works Department, by register number and name only: the same party that is the `ContractingParty` of this document, with no contact, address or other detail that differs per role. The roles exist for the case that another party (or another office) originates the need, benefits, hands out the documents, receives or evaluates the tenders. Filled with the contracting party itself they say nothing the document does not already say (rule "no fillers, and nothing implied by absence"). The contracting party states that it acts `/CallForTenders/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationType` = `On its own behalf`.
- Condition: Each of these roles is present only where it names a party, office or contact that differs from the contracting party, or adds details (a contact, an address) specific to the role.
- Options: Leave out the roles that only repeat the contracting party (preferred); or give each kept role what distinguishes it (e.g. the contact that receives tenders).
- Needs decision: no

### tender/03#F7 · Low · Large enterprise with 180 employees
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- Why: Valdara Industries is described as `LARGE`, which the code list defines as "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL or 5,000,000,000 XUF). In its tenderer qualification the same party states `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180` employees and a financial capability of `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00` XBL. 180 is below 250, and the only financial figure given is far below the turnover limit, so nothing in the flow supports `LARGE`; by the persons criterion the company is medium-sized. The contradiction is not strict, because the turnover is not stated as such: hence Low, but it needs a decision on what Valdara is.
- Condition: The size class of Valdara Industries agrees with the number of employees and the financial figures stated for it in the flow.
- Options: Decide Valdara's size once: 250 or more employees in the qualification (preferred if it is meant to be a large listed company), or `MEDIUM` in every example that describes it.
- Needs decision: yes

### tender/03#F8 · Low · Contact of Valdara Industries is the order desk
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- Why: In this document Valdara Industries is the tenderer invited by the call for tenders. Its contact is the `Order desk` with a `Customer service officer` and the mailbox `order@…`: the function that takes purchase orders for delivery (it is the right contact in the order documents 26–28 of the flow). Questions on a tender, a qualification or a guarantee go to whoever prepares bids, not to the order desk (checklist: the contact fits the role).
- Condition: The contact of Valdara Industries in the tendering documents is a function that handles tenders, or the contact is left out where the document needs none.
- Options: Give Valdara a tender or bid contact for the tendering documents (preferred); or leave the contact out here.
- Needs decision: no

### tender/03#F9 · Low · Technical committee of three officers, one named
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:TechnicalCommitteeDescription` = `Three officers of the department.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:JobTitle` = `Head of parks`
- Why: `TechnicalCommitteePerson` is "A member of a committee of experts evaluating the subjective criteria for awarding the contract" (0..n). The description says the committee has three officers of the department; one person is listed. A reader cannot tell whether the other two are unnamed on purpose or missing. The person is the same in every example of the flow that names the committee (01, 02, 03, 24).
- Condition: The persons listed and the description agree: all members are listed, or the description says that only the chair (or one member) is named.
- Options: Say in the description that Mara Delling chairs the committee and the other two members are appointed later (preferred, least change); or list all three.
- Needs decision: no

### tender/03#F10 · Low · Contact of the review board described as a procurement officer
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: The contact of the party that receives appeals is named `Registry`, but its job title is `Procurement officer` and its department `Procurement`. A review board decides on appeals against procurement decisions; its registry does not buy. Job title and department are identical to those of the contracting department's own contact in this example, and do not agree with the contact name (checklist: "Do job title, department and name agree with each other?").
- Condition: Name, job title and department of the contact describe the same function, one that fits the party's role in this document.
- Options: Give the contact a job title and department of its own function (e.g. registrar / registry; bid manager / sales) (preferred).
- Needs decision: no

### tender/03#F11 · Low · Location of the opening named after the organisation, without an address
- XPath: `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- Why: `OccurrenceLocation` is "The location of this event" and its `Name` "The name of this location". The value is the name of the department followed by the square: the organisation, not a place (checklist: "the name is the place, not the company"). The same building is identified elsewhere in this example by an address with a register identifier (`/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`, Civic Square 6), which the location does not use. The event is described as an electronic opening that tenderers follow online, so the physical place matters little; if it is given, it should be findable.
- Condition: The location of the opening is a place: a name of a room or building and/or the address (or address identifier) of the building; or it is absent for a purely electronic opening.
- Options: Give the location the address of Civic Square 6 with its register identifier, and a room name (preferred); or leave the location out and keep the description.
- Needs decision: no

## Checked and consistent
- Parties and roles: Lumeport Public Works Department as AdditionalInformationParty, BeneficiaryParty, ContractResponsibleParty, ContractingParty, DocumentProviderParty, OriginatorCustomerParty, QualificationRequestRecipientParty, SignatoryParty, TenderEvaluationParty, TenderRecipientParty; Procurement Review Board of Bayvarra as AppealInformationParty, AppealReceiverParty; Valdara Industries as ReceiverParty. Each is the party the role's definition asks for (apart from the findings).
- Every party is identified by the same register number wherever it is named in this example, and the full descriptions (identifiers, address, tax scheme, legal entity, contact, electronic address) are identical, element by element, to those of the same party in all other examples of the tender flow that carry it (compared by script over the 36 `*.xml` of the flow and over the other flows), apart from what the findings and the refuted candidates below say.
- `check_ids.py`: ISIN XU0001042501: check digit correct.
- ISIC Rev. 4 classes fit the parties (own knowledge of ISIC): 3100 manufacture of furniture, 8411 general public administration, 8423 public order and safety (review board).
- Telephone numbers use the country code +999, which is not assigned to a country (own knowledge of ITU-T E.164); all web and mail addresses are in `.example`.

## Considered and refuted
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: suspected that `-1` is not a valid form of a time zone offset — refuted because the definition ("as an offset from Universal Coordinated Time (UTC)") prescribes no format and the value reads unambiguously as UTC−1; it is the same for all addresses of the flow.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: suspected that `Room 2.14` belongs in `cbc:Room` — refuted because `InhouseMail` is "The specific identifable location within a building where mail is delivered", and a room where the procurement office takes its mail is such a location; `Room` would also be defensible.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: suspected that a contact named after an office (`Procurement office`) with a job title is inconsistent, and that the address department `Procurement office` differs from the contact department `Procurement` — refuted because UBL recommends a functional name for `Contact/cbc:Name`, and the two department wordings name the same unit.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: suspected that `STATE` contradicts the party type "local authority" — refuted because `TaxLevelCode` is the level of the tax within the scheme (the state sales tax), not the level of government of the party.
- `/CallForTenders/cac:TenderingTerms/cac:ContractResponsibleParty`: suspected that "The Party who executes the Contract" means the contractor, who is not known yet — refuted because the role is a party on the buyer's side in the tendering terms (the body that administers the contract); the department fits. (That it only repeats the contracting party is the finding on repeated roles.)
- `/CallForTenders/cac:ReceiverParty`: suspected that one named receiver is wrong for a call for tenders that other operators answer too — refuted because this instance is the copy sent to Valdara; which operators were invited is a question for the context review.
- `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: suspected (1) that `Via delle Officine` and `Ferrano` are not English although tagged `en-XB`/`en-XU`, and (2) that the same address and legal form are rendered differently across the flow (tag `en-XB` and legal form in "English" only in documents issued in Bayvarra: 03, 12, 14, 16, 20–24, 26, 27, 31, 34, 36; tag `en-XU` plus the Urvanian legal form in documents issued by Valdara: 13, 15, 25, 28–30, 32, 33, 35) — refuted because these are the invented world's English-language names of Urvanian places and legal forms (accepted as given), the texts themselves are identical in all examples, and the tag follows the locale of the document's issuer consistently.
- `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: suspected a mismatch with the definition "The number of shares in the capital stock of a corporation" (the value is an amount in a currency) — refuted because the element is of an amount type and can only hold the capital stock as money; the definition's wording is a matter of the UBL model, not of the example.
- `/CallForTenders/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: suspected that ICD `0990` is an assigned ISO 6523 code used for a fictional agency — refuted as far as own knowledge goes: the assigned ICDs are far below 0990; the ICD register was not available to check (see the report).
- `/CallForTenders/cac:ReceiverParty/cac:Language/cbc:ID`: suspected that `qau` is a real ISO 639 code — refuted because qaa–qtz is the range ISO 639-2/3 reserves for local use.
