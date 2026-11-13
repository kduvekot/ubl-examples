# LLM review: 02-PriorInformationNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/02-PriorInformationNotice.xml`, Git blob `a3f76e84106ee3bfd01686b7e8ab9a1352366cec` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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

### contest/02#F1 · Medium · Language code in LocaleCode
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is a language code, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples`, and `grep -rl` for the file count).
- Condition: no `cbc:LocaleCode` holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since none of these documents needs a locale beyond the language; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID.
- Needs decision: no

### contest/02#F2 · Low · Public bodies described as companies in a commercial register
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the public bodies of this example (Lumeport Public Works Department, Bayvarra Information Service) are registered in the `Federal business register of Bayvarra` with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"). UBL defines `Corporate Registration Scheme` as "The corporate registration scheme used to register the party" and the liquidation status as "the party's liquidation status". A department of the city, a national information service and a review board are not companies in a commercial register and cannot go into liquidation (the contracting party describes itself as "a department of the city of Lumeport" in `cac:ContractingPartyType/cbc:PartyType` where present). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for a register of public bodies, so the value is forced.
- Condition: no public body carries `CorporateRegistrationTypeCode` `COMMERCIAL` or a `CompanyLiquidationStatusCode`; if a registration scheme is given for a public body, its type says what kind of register it is.
- Options: (preferred) leave the registration type and the liquidation status out for public bodies and keep only the identifier of the register they are in; or add a public-sector register type to the list. The choice is about how the world registers public bodies, which is why it needs a decision.
- Needs decision: yes

### contest/02#F3 · Low · Customs and tax data of the contracting authority that the document does not use
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: this document belongs to a design contest; it declares no goods to customs and states no tax. The contracting authority's customs-trader number and its `PartyTaxScheme` look copied from its master data. In addition, `ExemptionReason` is defined as "A reason for the party's exemption from tax"; the code chosen means "Sale to a public body", which describes a transaction, not the status of the party, and this document records no sale.
- Condition: the contracting authority carries a customs-trader identifier and a `PartyTaxScheme` only where the document uses them; where a tax exemption of the party is stated, it is the party's own status.
- Options: (preferred) leave both out of the tendering documents; or, if the tax data stays, word the exemption reason as the party's status (a public body exempt from the state sales tax).
- Needs decision: no

### contest/02#F4 · Low · New version does not say what it changes
- XPath: `/PriorInformationNotice/cbc:VersionID` = `2`
- XPath: `/PriorInformationNotice/cbc:PreviousVersionID` = `1`
- XPath: `/PriorInformationNotice/cbc:Note` = `Advance notice of the design contest for the harbour promenade bench.`
- Why: this is version 2 of a published notice with the same `cbc:ID` as version 1; it raises the first prize from 6,000 to 8,000 lume and moves the planned publication of the contract notice from 2026-03-04 to 2026-03-19 (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-03-04`). The only `Note` is the one of version 1, so a reader of the published notice cannot see that, or what, it changes (UBL has no dedicated element for this, which leaves the free-text `Note`, defined as "information that is not contained explicitly in other structures").
- Condition: the new version states which values it changes and, where it corrects an error, that it is a correction.
- Options: (preferred) add a `Note` naming the changes (and the reason); or another means the world's notices use for corrections.
- Needs decision: no

## Checked and consistent
- `PlannedDate` 2026-03-19 matches the issue date of the contract notice (`03-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-03-19`).
- Prizes 8,000 + 4,000 + 2,000 lume and the text "Three prizes; the first is 8,000 lume" agree; the participation payment (1,000 lume) and the jury (five members) are the same in all notices and calls.
- `VersionID` 2 with `PreviousVersionID` 1 and the same `cbc:ID` and `ContractFolderID` as version 1.
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files).

## Considered and refuted
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`: suspected that the estimate should have risen with the first prize (6,000 to 8,000 lume between the two versions of the prior information notice) — refuted because the flow does not say what the 54,000 lume consist of (prizes 14,000 + participation payments up to 5,000 leave about 35,000 for the follow-up contract); without a breakdown no arithmetic contradiction can be shown.
