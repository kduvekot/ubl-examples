# LLM review: 04-ExpressionOfInterestRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/04-ExpressionOfInterestRequest.xml`, Git blob `1ca94275bd6d396987ad7aa46080a104842bb2c3` (committed)
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

### tender/04#F1 · High · A small enterprise with 85 employees
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: EntitySizeCode `SMALL` means, in the world's list (`world/codelists/lists.json`, EntitySizeCode), "Fewer than 50 persons and a turnover of at most 10,000,000.00 XBL". The same document states that the sawmill employs 85 people ("The number of people employed by this qualifying party"). With 85 persons it is a medium-sized enterprise.
- Condition: The size class and the number of employees of the same party agree.
- Options: (a) fewer than 50 employees (preferred if the sawmill is meant to be small; the same size code is in 05, 10 and 11); (b) size `MEDIUM` in all four examples.
- Needs decision: no

### tender/04#F2 · Medium · Language code in a locale code
- XPath: `/ExpressionOfInterestRequest/cbc:PreferredLanguageLocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: PreferredLanguageLocaleCode is "A code signifying the locale in which the language in the required documents is preferred", LocaleCode "A code signifying the locale in which this language is used." `en` with listID `ISO 639` is a language, not a locale; in the parties it only repeats `cbc:ID`.
- Condition: A locale element carries a locale from a list of locales, or is absent.
- Options: (a) a locale code such as `en-XB` with a suitable list for the preferred language of the documents, and no LocaleCode in the parties (preferred); (b) remove all three.
- Needs decision: no

### tender/04#F3 · Low · Interest expressed after the period for requests to participate has ended
- XPath: `/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- XPath: `/ExpressionOfInterestRequest/cac:DocumentReference/cbc:ID` = `LPWD-DOC-26-0188`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: The contract notice this expression of interest answers says that requests for participation must be delivered by 2026-02-11 (the day the notice was issued); the sawmill writes on 2026-02-14. If the expression of interest is the request to participate, it is late; if the procedure is open, as the notice also says, no expression of interest is needed to tender and the document only serves to "follow the procedure" (its note). Which of the two is meant cannot be settled from the examples; the stale periods are a finding of 02.
- Condition: The expression of interest lies within the period the notice gives for it, or the notice gives no such period.
- Options: (a) correct the periods of the notice (see the review of 02) (preferred); (b) date the expression of interest within the period.
- Needs decision: yes

### tender/04#F4 · Low · 22 years in operation, registered 30 years ago
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:OperatingYearsQuantity` = `22`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: OperatingYearsQuantity is "The number of years that this qualifying party has been in operation." The company was registered on 1996-01-01, 30 years before this document (2026-02-14). 22 years would mean it started operating in 2004, eight years after registration; nothing says so.
- Condition: Years in operation and registration date agree, or the difference is explained.
- Options: (a) 30 years (preferred); (b) a registration date in 2003/2004.
- Needs decision: no

### tender/04#F5 · Low · A consortium lead with a 60 % share that only supplies the slats, with no partner named
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:ParticipationPercent` = `60`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Supplies the slats; a bench maker would build the benches.`
- XPath: `/ExpressionOfInterestRequest/cbc:Note` = `The sawmill considers a tender for lot 1 with a bench maker and asks to follow the procedure.`
- Why: ParticipationPercent is "The extent to which this party is expected to participate in the tendering process, expressed as a percentage." The sawmill supplies five hardwood slats per bench; the steel frame, coating and assembly are the bench maker's. A 60 % share for the slats of a steel bench estimated at 499 lume is implausible, and the consortium is hypothetical: the partner is not named and the remaining 40 % belong to nobody. Stating a precise share and a lead role for a consortium that does not exist yet has no business reason.
- Condition: The share and role are stated only for a consortium whose members are named, and the share fits what the party contributes.
- Options: (a) drop ParticipationPercent and say in the role description that a consortium is considered (preferred); (b) name the bench maker as a second qualifying party with shares that fit.
- Needs decision: no

### tender/04#F6 · Low · Signature ID with another prefix than the party's documents
- XPath: `/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`
- XPath: `/ExpressionOfInterestRequest/cbc:ID` = `MS-DOC-26-0190`
- Why: Every other signature of the flow starts with the abbreviation its party uses in its document numbers (PWD-SIG-…, BF-SIG-…, VI-SIG-…). Marrowdale Sawmill numbers its documents `MS-…` but signs `HS-SIG-EOI` (and `HS-SIG-UNS` in 10).
- Condition: The signature ID uses the party's own prefix.
- Options: (a) `MS-SIG-EOI` (preferred); (b) none other seen.
- Needs decision: no

### tender/04#F7 · Low · A public body described as a company in a commercial register
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/04#F8 · Low · The department's tax exemption reason describes a sale
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: nothing reported as wrong.
- DocumentReference `LPWD-DOC-26-0188` is the ID of 02-ContractNotice.xml, the notice this expression of interest answers; ContractFolderID `PWD-2026-PARKS` and ContractName equal the project ID and name of the notice.
- Validity until 2026-02-26 is the tender deadline of the notice. Lot reference `LOT-1` is the bench lot, type SUPPLIES, name "Park benches" as in 02.
- ISIC 1610 (sawmilling and planing of wood) fits the party; signatory, qualifying party and economic operator carry the same register number 20412329.
- The economic operator is described identically in 04, 05, 10 and 11 (hash of leaf values).

## Considered and refuted
- `/ExpressionOfInterestRequest/cac:DocumentReference`: the reference has an ID only and does not say it is the contract notice — refuted because the ID resolves to the contract notice and an expression of interest can only answer a notice.
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle`: a sales office with a customer service officer as contact for a tender procedure — refuted because for a small sawmill the sales office is where a public buyer's messages arrive.
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cac:Party`: the economic operator names itself as the party qualifying it — refuted because the qualifying data (years, employees, role) are the operator's own.

## Outside this review
- Whether an expression of interest belongs in an open procedure at all is a question of the flow's story; see the review of 02.
