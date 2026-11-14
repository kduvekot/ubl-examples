# LLM review: 13-TendererQualification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/13-TendererQualification.xml`, Git blob `fbf9d6ddac8eb891f81b7a2f593f1db23d28b8d1` (committed)
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

### tender/13#F1 · Medium · Classification code and register number used as evidence identifiers
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessClassificationEvidenceID` = `ISIC-3100`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `XU-R-104274`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- Why: `BusinessClassificationEvidenceID` is "An identifier for an item of evidence to support the classification of this qualifying party" and `BusinessIdentityEvidenceID` "An identifier for an item of evidence to support the business identity of this qualifying party": identifiers of evidence (a register extract, a certificate). The first holds the classification itself (ISIC class 3100, which the `BusinessClassificationScheme` next to it already gives), the second the party's register number with the register's scheme, identical to the party identifier. Neither identifies an item of evidence; the other evidence of this document has identifiers of its own (`EV-FER-PARKS`, `EV-DEC-1`).
- Condition: Both elements identify an item of evidence (a document), not the fact the evidence is to prove.
- Options: Give identifiers of the evidence, e.g. of the register extract (the business information of example 12, `BIS-DOC-26-0198`, is such an extract) (preferred); or leave the two elements out.
- Needs decision: no

### tender/13#F2 · Medium · Subcontractor in AdditionalQualifyingParty, and a consortium lead without a consortium
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:TendererRoleCode` = `SUBCONTRACTOR`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads.`
- Why: `AdditionalQualifyingParty` is defined as "The qualifications of a tenderer party other than the main tenderer party when bidding as a consortium". Saltmere Engineering is given there with the role `SUBCONTRACTOR`, and the tender itself names it as `15-Tender.xml:/Tender/cac:SubcontractorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`, not as a second tenderer: there is no consortium. Yet Valdara's role is `LEAD` twice (code lists: "Consortium lead: Leads a group of economic operators"), with the description `Leads.`, which says nothing. A tenderer that bids alone and relies on a subcontractor is `SOLE` ("Tenders alone"); the subcontractor is not a consortium member.
- Condition: The roles tell one story that the tender (15) shares: either Valdara tenders alone with Saltmere as subcontractor (role `SOLE`; the subcontractor not presented as a consortium member), or the two form a consortium (Saltmere `MEMBER`, and a tenderer in example 15).
- Options: Sole tenderer with a subcontractor (preferred: it is what example 15 says): Valdara `SOLE` with a role description that says so; whether the subcontractor's qualification may stay in `AdditionalQualifyingParty` is a judgement on the definition (UBL offers no other place for a subcontractor relied on).
- Needs decision: yes

### tender/13#F3 · Medium · Province in Region
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/cbc:Region` as "The recognized geographic or economic region or group of countries in which this address is located", and `cbc:CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province of Urvania is a country subentity, not a region; the Bayvarran addresses of this flow put their state in `cbc:CountrySubentity`. `Province of Ferrano` in `cbc:Region` occurs 219 times in 104 of the 250 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'` over `world/examples`).
- Condition: The province of an Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list), and `cbc:Region` is absent or holds a region in the sense of the definition.
- Options: Move the value to `cbc:CountrySubentity` (preferred); a code for the province is optional.
- Needs decision: no

### tender/13#F4 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en`, with `listID="ISO 639"`, is the language code already given in `cbc:ID` of the same `cac:Language`; it names no locale (a locale says where or in which variant the language is used, as the `en-XB` and `en-XU` tags on texts in this flow do). The same value occurs 362 times in 213 of the 250 examples (`grep -r --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'` over `world/examples`, lines and files counted).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is either absent or holds a locale, with a `listID` that names a list of locales.
- Options: Remove `cbc:LocaleCode` (preferred: `cbc:ID` already states the language and nothing in the document uses a locale); or give the locale (`en-XB`) with a matching list.
- Needs decision: no

### tender/13#F5 · Low · 41 operating years against a registration 63 years ago
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:OperatingYearsQuantity` = `41`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`
- XPath: `/TendererQualification/cbc:IssueDate` = `2026-02-25`
- Why: `OperatingYearsQuantity` is "The number of years that this qualifying party has been in operation": 41. The legal entity in the same aggregate was registered on 1962-04-12, 63 years before the issue date (2026 − 1962 = 63, the 64th year not yet complete). 22 years between registration and the start of operation are unexplained.
- Condition: Operating years and registration date tell one history, or the difference is explained.
- Options: State 63 operating years (preferred: the registration date is used for Valdara in 75 places across the examples); or explain the 41 (e.g. years of bench production) in a description.
- Needs decision: no

### tender/13#F6 · Low · Large enterprise with 180 employees
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- Why: Valdara Industries is described as `LARGE`, which the code list defines as "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL or 5,000,000,000 XUF). In this example the same party states 180 employees and a financial capability of 9,200,000.00 XBL. 180 is below 250, and the only financial figure given is far below the turnover limit, so nothing in the flow supports `LARGE`; by the persons criterion the company is medium-sized. The contradiction is not strict, because the turnover is not stated as such: hence Low, but it needs a decision on what Valdara is.
- Condition: The size class of Valdara Industries agrees with the number of employees and the financial figures stated for it in the flow.
- Options: Decide Valdara's size once: 250 or more employees in the qualification (preferred if it is meant to be a large listed company), or `MEDIUM` in every example that describes it.
- Needs decision: yes

### tender/13#F7 · Low · Production capability of Valdara Industries: 6,000 in the register extract, 4,000 in its own qualification
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.`
- Why: Both documents describe the capability of the same party to produce benches, for the same evaluation, two days apart. This qualification gives a technical capability of 4,000 benches a year; the other document gives `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000` (`12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:Description` = `Steel frame benches, cast, galvanised and coated in its own plant.`). Neither says why the figures differ (all products against benches only, capacity against output). It could not be settled whether they describe the same measure; if they do, they contradict each other.
- Condition: The two documents give the same figure for the same capability, or each says what its figure measures so that both can be true.
- Options: Use one figure in both (preferred); or word the descriptions so that the difference is explained (e.g. "6,000 pieces of street furniture a year, of which 4,000 benches").
- Needs decision: yes

### tender/13#F8 · Low · Master data the document does not use (customs trader number, logistics service provider)
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- Why: Section 4.8 of the review rules: data copied from a party's master data into a document that does nothing with it. The customs trader numbers identify the parties towards customs; this TendererQualification is a tendering document and declares nothing to customs (such numbers matter in customs declarations, as in examples 30 and 31 of the flow). The `ServiceProviderParty` ("A party providing a service to this party") names Castrano Logistics as Valdara's provider of "Warehousing and despatch", with a contact at the provider; nothing in this document concerns warehousing or despatch (Castrano acts in `29-DespatchAdvice.xml`).
- Condition: The document carries, for each party, only the identifiers and related parties that its purpose uses.
- Options: Leave these out of the tendering documents (preferred); or keep them only where the document says what they are for.
- Needs decision: no

### tender/13#F9 · Low · Contact of Valdara Industries is the order desk
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- Why: In this document Valdara Industries is the tenderer declaring its qualification. Its contact is the `Order desk` with a `Customer service officer` and the mailbox `order@…`: the function that takes purchase orders for delivery (it is the right contact in the order documents 26–28 of the flow). Questions on a tender, a qualification or a guarantee go to whoever prepares bids, not to the order desk (checklist: the contact fits the role).
- Condition: The contact of Valdara Industries in the tendering documents is a function that handles tenders, or the contact is left out where the document needs none.
- Options: Give Valdara a tender or bid contact for the tendering documents (preferred); or leave the contact out here.
- Needs decision: no

### tender/13#F10 · Low · Contact of the subcontractor: a bids office in a procurement department
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: The contact is named `Bids office` (mailbox `bids@…`), a function that sells, while its job title is `Procurement officer` and its department `Procurement`, a function that buys. Name, job title and department do not agree with each other; the same job title and department are used for the contracting department's contact.
- Condition: Name, job title and department of the contact describe the same function, one that fits the party's role in this document.
- Options: Give the contact a job title and department of its own function (e.g. registrar / registry; bid manager / sales) (preferred).
- Needs decision: no

### tender/13#F11 · Low · Party tax exemption reason worded as a transaction
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/cbc:ExemptionReason` as "A reason for the party's exemption from tax, expressed as text": the party's own status. The text starts with "Sale to a public body", which describes a transaction (a sale by someone else to the department); the code `PUBLIC` comes from a list whose other entries are reasons of a transaction or of goods (`EXP` export, `WATER`, `FOOD`, `RESALE`). What the party itself is, is a public body that buys free of the state sales tax.
- Condition: The exemption reason of the party states the party's status (a public body exempt from the state sales tax), not a kind of sale.
- Options: Reword the text to the party's status, e.g. "Public body: buys free of the state sales tax" (preferred; the code can stay, its definition "A body of the federation, a state or a city buys free of sales tax" fits); or keep the transaction wording only on tax categories of invoices.
- Needs decision: no

### tender/13#F12 · Low · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The legal entity of Lumeport Public Works Department is described like a company: `CompanyLiquidationStatusCode` ("A code signifying the party's liquidation status") `ACTIVE` ("Active, not in liquidation"), registered in a scheme of type `COMMERCIAL` (code list: "Commercial register: A register of businesses"). The department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`), and the information service and the review board are public bodies as well (ISIC 8411 and 8423, public administration). A city department or a public board is not a business in a commercial register and cannot be in liquidation, so the status and the register type say something that has no meaning for these parties.
- Condition: A public body carries no liquidation status, and the register it is identified in is not typed as a commercial register (or the description says in what capacity a public body is entered there).
- Options: Leave out `CompanyLiquidationStatusCode` for public bodies and type their registration scheme differently (preferred; a register type for public bodies would need a code), or leave out the `CorporateRegistrationScheme` details and keep only the identifier.
- Needs decision: no

## Checked and consistent
- Parties and roles: Lumeport Public Works Department as ContractingParty; Valdara Industries as MainQualifyingParty, SignatoryParty; Saltmere Engineering as AdditionalQualifyingParty. Each is the party the role's definition asks for (apart from the findings).
- Every party is identified by the same register number wherever it is named in this example, and the full descriptions (identifiers, address, tax scheme, legal entity, contact, electronic address) are identical, element by element, to those of the same party in all other examples of the tender flow that carry it (compared by script over the 36 `*.xml` of the flow and over the other flows), apart from what the findings and the refuted candidates below say.
- `check_ids.py`: ISIN XU0001042501: check digit correct.
- ISIC Rev. 4 classes fit the parties (own knowledge of ISIC): 3100 manufacture of furniture, 4290 other civil engineering, 8411 general public administration.
- Telephone numbers use the country code +999, which is not assigned to a country (own knowledge of ITU-T E.164); all web and mail addresses are in `.example`.
- Participation shares: 80 % (Valdara) + 20 % (Saltmere) = 100 %.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: suspected that `-1` is not a valid form of a time zone offset — refuted because the definition ("as an offset from Universal Coordinated Time (UTC)") prescribes no format and the value reads unambiguously as UTC−1; it is the same for all addresses of the flow.
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: suspected that `Room 2.14` belongs in `cbc:Room` — refuted because `InhouseMail` is "The specific identifable location within a building where mail is delivered", and a room where the procurement office takes its mail is such a location; `Room` would also be defensible.
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: suspected that a contact named after an office (`Procurement office`) with a job title is inconsistent, and that the address department `Procurement office` differs from the contact department `Procurement` — refuted because UBL recommends a functional name for `Contact/cbc:Name`, and the two department wordings name the same unit.
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: suspected that `STATE` contradicts the party type "local authority" — refuted because `TaxLevelCode` is the level of the tax within the scheme (the state sales tax), not the level of government of the party.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: suspected (1) that `Via delle Officine` and `Ferrano` are not English although tagged `en-XB`/`en-XU`, and (2) that the same address and legal form are rendered differently across the flow (tag `en-XB` and legal form in "English" only in documents issued in Bayvarra: 03, 12, 14, 16, 20–24, 26, 27, 31, 34, 36; tag `en-XU` plus the Urvanian legal form in documents issued by Valdara: 13, 15, 25, 28–30, 32, 33, 35) — refuted because these are the invented world's English-language names of Urvanian places and legal forms (accepted as given), the texts themselves are identical in all examples, and the tag follows the locale of the document's issuer consistently.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount`: suspected a mismatch with the definition "The number of shares in the capital stock of a corporation" (the value is an amount in a currency) — refuted because the element is of an amount type and can only hold the capital stock as money; the definition's wording is a matter of the UBL model, not of the example.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: suspected that ICD `0990` is an assigned ISO 6523 code used for a fictional agency — refuted as far as own knowledge goes: the assigned ICDs are far below 0990; the ICD register was not available to check (see the report).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Language/cbc:ID`: suspected that `qau` is a real ISO 639 code — refuted because qaa–qtz is the range ISO 639-2/3 reserves for local use.
- `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyLegalEntity`: suspected an incomplete description (no legal form, size or registration date, unlike the other companies) — refuted because all are optional and nothing in this document depends on them.
