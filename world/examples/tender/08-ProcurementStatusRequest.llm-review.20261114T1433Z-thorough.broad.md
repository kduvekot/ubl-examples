# LLM review: 08-ProcurementStatusRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/08-ProcurementStatusRequest.xml`, Git blob `8b0ed73feb4728e9ed11f9a24ad476449b06b7f2` (committed)
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

### tender/08#F1 · Medium · Language code in LocaleCode
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/08#F2 · Low · The project has another name here than in the notices
- XPath: `/ProcurementStatusRequest/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatusRequest/cbc:ContractName` = `Park benches for the parks renewal programme`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`
- Why: ProcurementProject/Name is "A name of this procurement project". The project of this procedure is named "Park benches for the parks renewal programme" in 01, 02 and 03, and this document itself uses that name as ContractName; its ProcurementProject is named "Park benches for the city parks" (so in 08, 09 and 24; grep over the `*.xml` of all flows).
- Condition: The procurement project has one name in all documents of the procedure.
- Options: (a) use the name of the notices (preferred); (b) none other seen.
- Needs decision: no

### tender/08#F3 · Low · A public body described as a company in a commercial register
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/08#F4 · Low · The department's tax exemption reason describes a sale
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit.
- TenderingProcess ID `PWD-2026-PARKS-P` is the process ID of 02 and 03; folder `PWD-2026-PARKS`; lots `LOT-1` and `LOT-2` exist in the notice.
- The question ("Does the deadline stand after the answers to the questions?") is asked on 2026-02-20, the day after the period for questions ended (2026-02-19 in 02) and before the deadline (2026-02-26); 09 answers it and refers to this document by its ID.
- Signatory and economic operator are the same party (register number 20412466).

## Considered and refuted
- `/ProcurementStatusRequest/cac:ProcurementProjectLot[2]/cbc:ID`: Brackenmere asks about lot 2 although its qualification (06, 07) and tender (17, 19) concern lot 1 — refuted because the deadline it asks about is the same for both lots, and an operator may ask about the whole procedure.
- `/ProcurementStatusRequest/cac:ProcurementProject/cbc:ProcurementTypeCode`: SUPPLIES although lot 2 is a service — refuted because the project as a whole is classified as supplies in the notices.
