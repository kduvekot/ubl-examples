# LLM review: 14-BusinessInformation.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/14-BusinessInformation.xml`, Git blob `ea59d9c8ec70285678a63c9762adc18d4f21b15e` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
- Checkout: branch `claude/keen-feynman-45qjti`, commit 70e2a4d 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### contest/14#F1 · Medium · LocaleCode carries a language code
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines Language/LocaleCode as "A code signifying the locale in which this language is used", and Language/ID as "An identifier for this language". Every party here gives `en` with listID `ISO 639` in both: the locale element repeats the language code instead of naming a locale (a language in a region, such as en-XB). A language code is a valid code, but not the one the definition names. The same pattern (`<cbc:LocaleCode listID="ISO 639">`) occurs in 213 example files, 362 times (counted with `grep -c` over `world/examples/*/*.xml`).
- Condition: Every LocaleCode either names a locale (language and country/region) from a locale scheme, or is absent.
- Options: Preferred: drop LocaleCode where the party has no locale to state beyond its language (Language/ID already says English). Alternative: a locale code such as `en-XB` with a locale listID (e.g. BCP 47).
- Needs decision: no

### contest/14#F2 · Low · Production capability given as an amount without saying what the amount measures
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00`
- XPath: `13-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6410000.00`
- Why: Capability/ValueAmount: "A monetary amount as a measure of this capability"; CapabilityTypeCode is meant for codes like "Turnover" or "Qualified Engineers". The capability is `PRODUCTION` with the text "Furniture of wood and steel, designed and made in its own workshop", and an amount of several million lume. Whether that is a yearly production value, a turnover or a capacity, and for which period, is not said, so the buyer checking the register cannot use it for the selection. Version 2, four days later, changes the amount from 6,410,000 to 6,830,000 lume and nothing else, without saying what the figure measures or why it changed (a new year's accounts, a correction).
- Condition: The amount says what it measures (and for which period), or the capability carries no amount.
- Options: Preferred: state the measure in the Description (e.g. "value of production in 2025") and keep the amount. Alternative: drop the amount; the register extract is about registration and exclusion grounds.
- Needs decision: yes

### contest/14#F3 · Low · Tax and customs identity copied into a document that does nothing with them
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: BusinessInformation carries no amount that is taxed, no tax total and no customs procedure, yet the parties bring their tax registration (PartyTaxScheme) and, where they have one, their customs trader number (AdditionalPartyIdentification, scheme `customs-trader`). Section 4.8 of the review rules: data copied from a party's master data into a document that does not use it. For the contracting authority the tax scheme also states ExemptionReasonCode `PUBLIC`, whose meaning in the list is "Sale to a public body"; PartyTaxScheme/ExemptionReasonCode is "A reason for the party's exemption from tax", so even where the scheme is kept, the reason should be the party's own status, not a kind of sale.
- Condition: The parties of this document carry no tax scheme and no customs trader number, unless something in the document uses them; where a PartyTaxScheme of a public body is kept, its exemption reason names the party's status.
- Options: Preferred: leave PartyTaxScheme and the customs trader identifier out of the notices and qualification documents, as the Bayvarra Information Service is described throughout the flow. Alternative: keep them only where a tax or customs check is part of the step, and say so in the document.
- Needs decision: no

### contest/14#F4 · Low · Public bodies described as companies in the commercial register, with a liquidation status
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The public bodies of this document (ISIC 84xx: Bayvarra Information Service, Lumeport Public Works Department, "a department of the city of Lumeport") are registered in a CorporateRegistrationScheme of type `COMMERCIAL` ("Commercial register") and carry CompanyLiquidationStatusCode `ACTIVE` ("Active, not in liquidation"). A city department or a state authority is not a company in a commercial register and cannot be liquidated, so "the party's liquidation status" has no meaning for it (review checklist, party legal entity).
- Condition: No public body in this document has a liquidation status, and its registration scheme, if stated, is not a commercial register.
- Options: Preferred: no CompanyLiquidationStatusCode for public bodies, and a registration scheme of a type for public bodies (or none). Alternative: keep the federal register but with a type code that says it registers public bodies.
- Needs decision: no

## Checked and consistent
- BriefDescription ("registered, no exclusion grounds recorded"), NoticeTypeCode `BUSREG` and NoticeSubType `EXTRACT` agree with each other and with the Note ("Extract from the register of economic operators").
- The register keeper sends the extract (SenderParty Bayvarra Information Service) to the buyer that checks the participant (ReceiverParty Lumeport Public Works Department) about the business party Brackenmere Furniture.
- The business party's legal entity and tax registration belong in a register extract and are not copied data here.

## Considered and refuted
- `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:Name` = `Trade sales`: the sales desk as contact — not a finding here: the register publishes the contact it holds for the business, not a contest contact.
