# LLM review: 13-TendererQualification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/13#F1 · Medium · A classification code where an evidence identifier is asked
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessClassificationEvidenceID` = `ISIC-3100`
- Why: the element is "an identifier for an item of evidence to support the classification of this qualifying party". `ISIC-3100` is the classification itself (the same document gives it in `BusinessClassificationScheme`: scheme `ISIC4`, code value `3100`), not an item of evidence; nothing with this ID exists in the document or the flow (the string occurs only here; `grep -l` over `tender/*.xml`). The sibling `BusinessIdentityEvidenceID` shows the intended use: it holds the register number, with its scheme, i.e. the register entry that proves the identity.
- Condition: the element identifies an item of evidence (e.g. the register extract that shows the registered activity), or is absent.
- Options: (a) point to the register entry (`XU-R-104274` with the register's scheme) or to an `Evidence` defined in the document (preferred); (b) remove it, the classification scheme block already gives the class.
- Needs decision: no

### tender/13#F2 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/13#F3 · Low · Evidence and document references that lead nowhere
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Declaration/cac:SuppliedEvidence/cbc:ID` = `EV-DEC-1`
- XPath: `/TendererQualification/cac:AdditionalDocumentReference/cbc:ID` = `VI-ESPD-26`
- Why: the completed task's evidence `EV-FER-PARKS` is described at document level (`/TendererQualification/cac:Evidence/cbc:ID` = `EV-FER-PARKS`, "Ferrano reference"), but the declaration's evidence `EV-DEC-1` has no such entry and carries only an ID, so the document does not say what supports the integrity declaration. `AdditionalDocumentReference` (a generic "reference to an additional document") carries only the ID `VI-ESPD-26`; no document of the flow has it (it occurs only here), and it has no type or description. By its name it is a self-declaration, which is what this qualification document itself is (its ID is `/TendererQualification/cbc:ID` = `VI-DOC-26-0199`).
- Condition: every evidence ID used in the document is described (in `Evidence`, or by a name where it is used), and every generic document reference states the kind of document.
- Options: (a) add an `Evidence` entry or a name for `EV-DEC-1` and a document type for `VI-ESPD-26` (preferred); (b) remove the two references.
- Needs decision: no

### tender/13#F4 · Low · "Consortium lead" for a single tenderer with a subcontractor
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:TendererRoleCode` = `SUBCONTRACTOR`
- Why: both codes mean "Consortium lead" in their lists. The document's note says what the set-up is: `/TendererQualification/cbc:Note[2]` = `The manufacturer with Saltmere as subcontractor for the installation.` A tenderer with a subcontractor is not a consortium: the subcontractor is not a tenderer, and the tender (15) names Valdara alone as tenderer and Saltmere as `SubcontractorParty`. The code does not fit the situation it is used in. (The other party is, consistently, coded as subcontractor.)
- Condition: the main qualifying party's role code means a sole tenderer or main contractor, or the tender is made by a consortium.
- Options: (a) use a code for a sole tenderer or main contractor, if the lists have one (preferred); (b) leave the role codes out for the main party.
- Needs decision: no

### tender/13#F5 · Low · One reference where the procedure asks for three
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Benches for Ferrano's parks.`
- Why: the technical criterion of the procedure is `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`, with a threshold quantity of 3. The qualification lists one completed task (Ferrano, 2023 to 2025). Read as one supply, it does not meet the criterion the document is meant to show; if the three years of deliveries count as three supplies, the document does not say so. Valdara is nevertheless qualified and awarded.
- Condition: the completed tasks listed meet the criterion's threshold, or the description shows how the one task counts as three supplies.
- Options: (a) list three completed tasks (preferred); (b) describe the Ferrano task as three yearly supply contracts.
- Needs decision: no

### tender/13#F6 · Low · The subcontractor's share of 20 % does not match the tender made the same morning
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `80`
- Why: `ParticipationPercent` is "the extent to which this party is expected to participate in the tendering process, expressed as a percentage". Saltmere does the installation (note 2). In the tender issued 21 minutes later, the installation is `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00` of a total of 124080.00 XBL, i.e. 3.5 %, and the tendering terms also put the subcontracted task at 4320.00 XBL. By value Saltmere's share is 3.5 %, not 20 %. The definition does not say the percentage is by value, so this is a plausibility remark, but no other basis for 20 % is visible in the flow.
- Condition: the participation percentages can be derived from the tender (by value: about 96.5 % and 3.5 %), or the basis of the split is stated.
- Options: (a) use the shares by value (preferred); (b) keep 80/20 and say in the role description what it measures.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.
- Issued 2026-02-25 08:52, 21 minutes before the tender that refers to it (15, 2026-02-25 09:13, `TendererQualificationDocumentReference` `VI-DOC-26-0199`) and before the deadline; `VI-DOC-26-0199` precedes Valdara's `VI-DOC-26-0201` in number and time.
- `ContractFolderID` `PWD-2026-PARKS`; interested lots `LOT-1` and `LOT-2` are the two lots of the procedure.
- Requirements of 01 to 03 are met by the figures: 41 years in operation (3 required), 180 employees (10 required), ISIC 3100 (required class), financial capability 9,200,000.00 XBL (turnover above 250,000.00 required).
- Participation 80 % + 20 % = 100 %; 20 % is within the 30 % the tendering terms allow for subcontracting (but see F6).
- Completed task: 2023-01-01 to 2025-12-31 is three years, within "five years" before the issue date; 540000.00 / 3 = 180000.00 = `AnnualAverageAmount`.
- Saltmere Engineering (register 20410685) is the subcontractor named in the tender 15.
- Unit codes ANN, IE, EA; world-list codes resolve.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID`: the register number as an "evidence identifier" — refuted because the register entry is the evidence of the business identity, and the scheme says which register.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity`: 4000 benches a year against 6000 EA in the register extract 12 — not a finding of this example: this document states its measure ("a year"); the unexplained figure is in 12 and reported there.
- `/TendererQualification/cbc:Note[2]`: `languageID` "en-XU" on an English note — refuted, a regional subtag is a valid language tag and Valdara is an Urvanian company.
