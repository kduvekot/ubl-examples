# LLM review: 05-ExpressionOfInterestResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/05-ExpressionOfInterestResponse.xml`, Git blob `3fc9021a423cb516bf42fbd92205840f2d256f11` (committed)
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

### tender/05#F1 · High · The sawmill is a small enterprise here, but has 85 employees according to its expression of interest
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: EntitySizeCode `SMALL` means "Fewer than 50 persons and a turnover of at most 10,000,000.00 XBL" in the world's list (`world/codelists/lists.json`, EntitySizeCode). In 04 the same party states 85 employees, which makes it a medium-sized enterprise.
- Condition: The size class of Marrowdale Sawmill agrees with the number of employees it states in 04.
- Options: (a) fewer than 50 employees in 04 (preferred if the sawmill is meant to be small); (b) size `MEDIUM` in 04, 05, 10 and 11.
- Needs decision: no

### tender/05#F2 · Medium · Language code in LocaleCode
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/05#F3 · Low · A public body described as a company in a commercial register
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/05#F4 · Low · The department's tax exemption reason describes a sale
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: nothing reported as wrong.
- ExpressionOfInterestDocumentReference `MS-DOC-26-0190` is the ID of 04-ExpressionOfInterestRequest.xml, issued the day before (2026-02-14 14:05; this response 2026-02-15 08:35); economic operator, contracting party, contract name, folder ID, project name and lot `LOT-1` equal those of 04.
- The note ("Registered: …") does what the document is for: "to inform the Economic Operator he has been registered as an interested party."
- The sawmill is described identically in 04, 05, 10 and 11, the department identically in all examples (hash of leaf values).

## Considered and refuted
- `/ExpressionOfInterestResponse/cbc:TenderLanguageLocaleCode`: `en` from ISO 639 in an element named "locale code" — refuted because the definition of this element is "A code signifying the language required for the tender"; a language code is what it asks for (unlike PreferredLanguageLocaleCode in 04).
- `/ExpressionOfInterestResponse/cbc:IssueDate`: 2026-02-15 is a Sunday (own calculation) and the department's contact note says "Weekdays 08:00–17:00" — refuted because a registration confirmation can be issued by the platform automatically; the world's calendar is not stated to follow real weekdays.

## Outside this review
- Whether an expression of interest and its confirmation belong in an open procedure is a question of the flow's story; see the review of 02.
