# LLM review: 09-ProcurementStatus.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/09-ProcurementStatus.xml`, Git blob `e9ed8a2b58652c74ad8a9d6547388d6e5e2746db` (committed)
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

### tender/09#F1 · Medium · Language code in LocaleCode
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en`, with `listID="ISO 639"`, is the language code already given in `cbc:ID` of the same `cac:Language`; it names no locale (a locale says where or in which variant the language is used, as the `en-XB` and `en-XU` tags on texts in this flow do). The same value occurs 362 times in 213 of the 250 examples (`grep -r --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'` over `world/examples`, lines and files counted).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is either absent or holds a locale, with a `listID` that names a list of locales.
- Options: Remove `cbc:LocaleCode` (preferred: `cbc:ID` already states the language and nothing in the document uses a locale); or give the locale (`en-XB`) with a matching list.
- Needs decision: no

### tender/09#F2 · Low · Master data the document does not use (customs trader number)
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Section 4.8 of the review rules: data copied from a party's master data into a document that does nothing with it. The customs trader numbers identify the parties towards customs; this ProcurementStatus is a tendering document and declares nothing to customs (such numbers matter in customs declarations, as in examples 30 and 31 of the flow).
- Condition: The document carries, for each party, only the identifiers and related parties that its purpose uses.
- Options: Leave these out of the tendering documents (preferred); or keep them only where the document says what they are for.
- Needs decision: no

### tender/09#F3 · Low · Party tax exemption reason worded as a transaction
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/cbc:ExemptionReason` as "A reason for the party's exemption from tax, expressed as text": the party's own status. The text starts with "Sale to a public body", which describes a transaction (a sale by someone else to the department); the code `PUBLIC` comes from a list whose other entries are reasons of a transaction or of goods (`EXP` export, `WATER`, `FOOD`, `RESALE`). What the party itself is, is a public body that buys free of the state sales tax.
- Condition: The exemption reason of the party states the party's status (a public body exempt from the state sales tax), not a kind of sale.
- Options: Reword the text to the party's status, e.g. "Public body: buys free of the state sales tax" (preferred; the code can stay, its definition "A body of the federation, a state or a city buys free of sales tax" fits); or keep the transaction wording only on tax categories of invoices.
- Needs decision: no

### tender/09#F4 · Low · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The legal entity of Lumeport Public Works Department is described like a company: `CompanyLiquidationStatusCode` ("A code signifying the party's liquidation status") `ACTIVE` ("Active, not in liquidation"), registered in a scheme of type `COMMERCIAL` (code list: "Commercial register: A register of businesses"). The department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`), and the information service and the review board are public bodies as well (ISIC 8411 and 8423, public administration). A city department or a public board is not a business in a commercial register and cannot be in liquidation, so the status and the register type say something that has no meaning for these parties.
- Condition: A public body carries no liquidation status, and the register it is identified in is not typed as a commercial register (or the description says in what capacity a public body is entered there).
- Options: Leave out `CompanyLiquidationStatusCode` for public bodies and type their registration scheme differently (preferred; a register type for public bodies would need a code), or leave out the `CorporateRegistrationScheme` details and keep only the identifier.
- Needs decision: no

### tender/09#F5 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". The date 1996-01-01 is given for 25 different parties in three countries (among them Marrowdale Sawmill, Brackenmere Furniture, Castrano Logistics, Bayforth Forwarding, Port of Lumeport, Selanu Telecom), 271 times in 181 of the 250 examples (`grep -r --include='*.xml' 'RegistrationDate>1996-01-01'` over `world/examples`; party names collected from the `PartyName` next to each `PartyLegalEntity`). One register entry date, on New Year's Day, for 25 unrelated companies is a default value, not a fact of each company (rule "no fillers").
- Condition: Each party's registration date is its own (parties do not share one default date), or the date is absent where the world has none.
- Options: Give each party a registration date of its own (preferred, since the date is used against `OperatingYearsQuantity` in this flow); or leave `RegistrationDate` out for parties without a history.
- Needs decision: no

### tender/09#F6 · Low · Roles filled with the contracting party itself, adding nothing
- XPath: `/ProcurementStatus/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ProcurementStatus/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: Each of these roles names the Lumeport Public Works Department, by register number and name only: the same party that is the `ContractingParty` of this document, with no contact, address or other detail that differs per role. The roles exist for the case that another party (or another office) originates the need, benefits, hands out the documents, receives or evaluates the tenders. Filled with the contracting party itself they say nothing the document does not already say (rule "no fillers, and nothing implied by absence").
- Condition: Each of these roles is present only where it names a party, office or contact that differs from the contracting party, or adds details (a contact, an address) specific to the role.
- Options: Leave out the roles that only repeat the contracting party (preferred); or give each kept role what distinguishes it (e.g. the contact that receives tenders).
- Needs decision: no

## Checked and consistent
- Parties and roles: Lumeport Public Works Department as ContractingParty, DocumentProviderParty, SignatoryParty, TenderRecipientParty; Brackenmere Furniture as EconomicOperatorParty. Each is the party the role's definition asks for (apart from the findings).
- Every party is identified by the same register number wherever it is named in this example, and the full descriptions (identifiers, address, tax scheme, legal entity, contact, electronic address) are identical, element by element, to those of the same party in all other examples of the tender flow that carry it (compared by script over the 36 `*.xml` of the flow and over the other flows), apart from what the findings and the refuted candidates below say.
- `check_ids.py`: GLN 9523710900008 (GS1 prefix 952, reserved for examples): check digit correct.
- ISIC Rev. 4 classes fit the parties (own knowledge of ISIC): 3100 manufacture of furniture, 8411 general public administration.
- Telephone numbers use the country code +999, which is not assigned to a country (own knowledge of ITU-T E.164); all web and mail addresses are in `.example`.

## Considered and refuted
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: suspected that `-1` is not a valid form of a time zone offset — refuted because the definition ("as an offset from Universal Coordinated Time (UTC)") prescribes no format and the value reads unambiguously as UTC−1; it is the same for all addresses of the flow.
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: suspected that `Room 2.14` belongs in `cbc:Room` — refuted because `InhouseMail` is "The specific identifable location within a building where mail is delivered", and a room where the procurement office takes its mail is such a location; `Room` would also be defensible.
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: suspected that a contact named after an office (`Procurement office`) with a job title is inconsistent, and that the address department `Procurement office` differs from the contact department `Procurement` — refuted because UBL recommends a functional name for `Contact/cbc:Name`, and the two department wordings name the same unit.
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: suspected that `STATE` contradicts the party type "local authority" — refuted because `TaxLevelCode` is the level of the tax within the scheme (the state sales tax), not the level of government of the party.
- `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:Contact`: suspected that a sales contact (`Trade sales`) does not fit an economic operator in a procurement procedure — refuted because for a small manufacturer the sales office is the function that answers tenders; name, job title and department agree.
