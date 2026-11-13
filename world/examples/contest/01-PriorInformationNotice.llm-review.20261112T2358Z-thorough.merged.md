# LLM review: 01-PriorInformationNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/01-PriorInformationNotice.xml`, Git blob `eabac2882841f25d8b6985b6d92b45b2d3caf81b` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 374ad95 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
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

### contest/01#F1 · Medium · Language code in LocaleCode
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language as used in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is the ISO 639 language code itself, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale (section 6 names a language code in `LocaleCode` as Medium). Verified in the XML at every place listed. The same value occurs 362 times in 213 examples (recounted in the merge with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l` and `grep -rl` for the file count; a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also matches other `…LocaleCode` elements).
- Condition: No `cbc:LocaleCode` in the example holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since nothing in the document needs a locale beyond the language that `Language/cbc:ID` already gives; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID. Same as every earlier flow.
- Needs decision: no
- From: broad F1, parties F2, context F1

### contest/01#F2 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PriorInformationNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: The public bodies of this example (Lumeport Public Works Department, Bayvarra Information Service) are entered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). A city department (and, where present, a federal information service or a review board) is not a business in a register of businesses and is not wound up by liquidation; the contracting party describes itself as "a department of the city of Lumeport" (`ContractingPartyType/PartyType`), and its ISIC class is 8411 (public administration). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no type for a register of public bodies, so the value is forced. Verified in the XML. The values carry a meaning that does not fit the party (Medium, as the customs authority described as a company in the earlier flows). Parties added that a city department is not a legal person at all; the legal entity behind it is the City of Lumeport.
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; a registration scheme given for a public body says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep only the register name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list; or give the City of Lumeport as the department's legal entity (this last option changes who the party is and would need a decision).
- Needs decision: no
- From: broad F2, parties F1, context F3

### contest/01#F3 · Low · Customs master data the procurement document does nothing with
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "One or more additional identifiers for this Party". The customs trader number (scheme `urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works Department towards customs and is used in its customs declarations (e.g. `tender/31-ImportCustomsDeclaration.xml`); this PriorInformationNotice is a procurement document of a design contest for a service: nothing is imported, declared or transported, and nobody in the document uses the number. It is copied from the party's master data (section 4.8; the value is in 55 examples, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted in the merge).
- Condition: The contracting authority carries no customs trader identifier in this procurement document.
- Options: (preferred) leave these values out of the procurement documents and keep them where documents use them (customs declarations, invoices); or keep one only where the story gives this document a reason, and say so.
- Needs decision: no
- From: broad F3 (part), parties F4, logistics F1, context F2 (part)

### contest/01#F4 · Low · Tax scheme of the contracting authority in a document that may not use it
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". The contracting authority brings its state sales tax registration and exemption into a procurement document. This document states amounts (prizes, participation payments, an estimated contract value, a production limit of 900 lume a bench) but no tax on them. Broad and context (and money from 05 on) read it as master data copied into a document that does not use it (section 4.8). Money (01-04, 08) refuted that: the buyer's exemption tells candidates that the amounts of the contest and of the follow-up contract are net of the state sales tax. Both readings are possible; the merge could not settle which the world intends.
- Condition: Either the authority's `PartyTaxScheme` is absent from this document, or the world states that procurement documents carry it to show that amounts are net of sales tax (and it is then carried consistently).
- Options: (preferred) leave it out of documents without amounts and decide for the notices whether the exemption is meant as information to candidates (then keep it and say so where amounts are given); or keep it everywhere as the buyer's tax status.
- Needs decision: yes
- From: broad F3 (part), context F2 (part); refuted by money

### contest/01#F5 · Low · Exemption reason of the contracting authority worded as a sale
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", i.e. the party's own status. The text begins "Sale to a public body", the name of the code in the Bayvarran exemption list (whose other codes are reasons for exempt supplies), and so describes a transaction; this document records no sale. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Money refuted the code itself, rightly: the list describes `PUBLIC` as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (verified in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`). What remains is the wording of the text. The same text is in 55 examples (`grep -rl --include='*.xml' 'Sale to a public body: public bodies' world/examples | wc -l`).
- Condition: Where the authority's exemption reason is stated, the text states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status ("Public body: exempt from the state sales tax") and keep the code; or add a status code for public bodies to the list.
- Needs decision: no
- From: broad F3 (part), parties F3, context F2 (part)

### contest/01#F6 · Low · What the estimated contract amount of 54,000 lume covers is not stated
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: `RequestedTenderTotal` holds "Budget monetary amounts for the project as whole" and `EstimatedOverallContractAmount` is "The estimated overall monetary amount of a contract". The procurement is a design contest for services (`ProcurementTypeCode` `SERVICES`, UN CPC 83912): prizes, payments of 1,000 lume to each of at most five participants and a follow-up service contract. Nothing says what the 54,000 lume cover. The figure is exactly 60 × the production limit of 900 lume a bench in the project description (recalculated), which suggests the production cost of the benches, a contract this procurement does not award. Read instead as prizes, payments and follow-up contract (the usual way of valuing a design contest, money's own knowledge of Directive 2014/24/EU Art. 78), it should have changed when the first prize rose from 6,000 to 8,000 lume between the two versions of the prior information notice (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`, `02-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), while the estimate stayed at 54,000 in every notice. Counter-argument (broad, which refuted it): without a breakdown no arithmetic contradiction can be shown (prizes 14,000 or 16,000 and payments up to 5,000 leave room for a follow-up contract of about 35,000). The merge cannot settle what the figure is meant to be, hence Low with a decision.
- Condition: The estimated overall contract amount is the estimated value of what this procurement buys (prizes, payments and/or the follow-up service contract), agrees with the prize amounts of the same version, and what it covers can be read from the notice.
- Options: (a, preferred) keep an estimate of prizes, payments and follow-up contract, say what it covers and adjust it with the prize change; (b) if 54,000 is the production budget, remove it from `RequestedTenderTotal` and keep the per-bench limit in the description.
- Needs decision: yes
- From: money F1; refuted by broad

## Checked and consistent
- Merge: every finding above was re-checked against the XML (values, positions, counts) and against the referenced examples; the definitions quoted were looked up in UBL-Entities-2.5.gc and the code meanings in `world/codelists/gc/`. The counts were redone over `*.xml` only.
- Prizes 6,000 + 4,000 + 2,000 lume agree with `PrizeDescription` ("Three prizes; the first is 6,000 lume"); the third prize's condition ("if the jury finds it of prize standard") fits `PrizeIndicator` `true`. (from broad)
- `PlannedDate` 2026-03-04 is after the issue date 2026-02-02; version 2 (`02-PriorInformationNotice.xml`) moves it to 2026-03-19, the day the contract notice `03-ContractNotice.xml` is issued. (from broad)
- Short list 3 to 5 agrees with the contract notice; procedure, project name, description, CPC 83912 (industrial design services) and the services nature agree with each other and with the later notices. (from broad)
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). (from broad)
- Prizes: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`, second 4,000, third 2,000 lume; `PrizeDescription` ("Three prizes; the first is 6,000 lume.") agrees with the three `Prize` aggregates and their ranks. (from money)
- Currency: every amount is in `XBL` (Lume), the currency of the contracting authority's tax scheme (`TaxScheme/CurrencyCode` `XBL`). (from money)
- Payments to participants: 1,000 lume to each selected participant that submits a conforming design; with at most five participants (`EconomicOperatorShortList/MaximumQuantity` 5) the outlay is at most 5,000 lume, and prizes plus payments total at most 17,000 lume (calculated). (from money)
- The change of the first prize to 8,000 lume in version 2 (02) is a legitimate change of a notice in a new version (`VersionID` 2, `PreviousVersionID` 1); the later notices follow it. (from money)
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data). (from parties)
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address. (from parties)
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606). (from parties)
- `/PriorInformationNotice/cbc:PlannedDate` = `2026-03-04` (planned publication of the contract notice) lies after the issue date 2026-02-02; it is moved to 2026-03-19 by version 2 (`02-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-03-19`), on which the contract notice is indeed issued (`03-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-03-19`). (from logistics)
- Document identity: `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0633` with `/PriorInformationNotice/cbc:VersionID` = `1`; version 2 (02) keeps the ID and carries PreviousVersionID 1; ContractFolderID `PWD-2026-PROM-DC` and ProfileExecutionID `CONTEST-2026-01` are the same in all 16 examples of the flow. (from logistics)
- Codes against their lists and elements: NoticeTypeCode PIN, ProcedureCode DESIGNCONTEST, ProcurementTypeCode SERVICES, PrizeRankCode FIRST/SECOND/THIRD, ISIC 8411 for public administration, UN CPC 83912 (industrial design services) for a bench design contest, EDED 5153 STT, ISO 4217-style XBL (fictional, not in ISO 4217). (from logistics)
- Party identifiers: register numbers 20410548 (Public Works Department) and 20410959 (Bayvarra Information Service) equal their PartyLegalEntity CompanyID and their endpoint IDs XB:20410548 / XB:20410959, and are the same in every example of the flow; address IDs LUM-ADR-000417 / LUM-ADR-634627 likewise. (from logistics)
- Short list: MinimumQuantity 3 and MaximumQuantity 5, consistent with the contract notice (three to five selected participants). (from logistics)
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against. (from logistics)
- The prize amounts agree with the prize text: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeDescription` = `Three prizes; the first is 6,000 lume.` and Prize[1] = `6000.00` (prizes 1–3 are announced, Prize[3] is conditional on prize standard). (from context)
- The short list (3 to 5, selected on references) fits a restricted contest, and the PIN announces it as one. (from context)
- `/PriorInformationNotice/cbc:PlannedDate` is the planned publication date of the contract notice, as defined; version 2 (`02-PriorInformationNotice.xml`) moves it to the date the contract notice was in fact published. (from context)
- ProcurementTypeCode `SERVICES` and CPC 83912 (industrial design services) fit a design contest for street furniture (own knowledge of UN CPC 2.1, class 8391 specialty design services). (from context)

## Considered and refuted
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`: suspected that the estimate should have risen with the first prize (6,000 to 8,000 lume between the two versions of the prior information notice) — refuted because the flow does not say what the 54,000 lume consist of (prizes 14,000 + participation payments up to 5,000 leave about 35,000 for the follow-up contract); without a breakdown no arithmetic contradiction can be shown. (from broad) Not followed in the merge: kept as F6, with this argument recorded there as counter-argument.
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department` = `Procurement office`: suspected a conflict with the contact's department `Procurement` — refuted because the address names the office to which mail goes and the contact the department the officer works in; both describe the same unit. (from broad)
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction ("Sale to a public body") rather than the party's own status — refuted because the list defines the code as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer, and `ExemptionReason` says so ("public bodies are exempt from the state sales tax"). (from money) Accepted in the merge for the code; the wording of the text remains finding F5.
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: suspected as master data copied into a notice without tax content — refuted because the notice sets a production limit of 900 lume a bench and announces a follow-up service contract; the buyer's exemption tells candidates that these amounts are net of the state sales tax. (from money) Not followed in the merge: kept as F4, with this argument recorded there as counter-argument.
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[3]/cbc:Description`: suspected that a third prize awarded only "if the jury finds it of prize standard" contradicts "Three prizes" and `PrizeIndicator` true — refuted because a conditional third prize is an ordinary contest term and the first two prizes are unconditional. (from money)
- `XBL` as currency: checked that it is not a code assigned in ISO 4217 (own knowledge: the assigned X-codes near it are XBA–XBD, bond-market units); it is the world's fictional Lume. (from money)
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better. (from parties)
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department. (from parties)
- `/PriorInformationNotice/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone`: two postal zones (38517, 38520) for buildings on the same square (Civic Square) — refuted: postal codes for individual large addressees on one square are usual, and both are in the same city subdivision and state. (from parties)
- `/PriorInformationNotice/cac:ProcurementProject/cac:RealizedLocation/cbc:Name` = `Harbour promenade, Lumeport`: suspected a missing location identifier, since Lumeport has the UN/LOCODE XBLMP in other flows — refuted: the location is a promenade, a part of the town, which the city's LOCODE does not identify; no other example identifies the promenade itself. (from logistics)
- `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0633`: suspected that document numbers running consecutively across three senders (LPWD-DOC-26-0633 … BF-DOC-26-0637, BF-DOC-26-0638, BIS-DOC-26-0639, LPWD-DOC-26-0640) imply one shared counter — refuted: each number carries its sender's prefix, is unique over `*.xml` (`grep -rl --include='*.xml'` finds each only in this flow) and nothing in UBL requires gaps; the same numbering style runs through the whole world (e.g. `tender/*.xml`). (from logistics)
- Telephone numbers with country code +999: suspected a real ITU code — refuted: +999 is not assigned to any country (ITU reserves it), so it cannot be mistaken for a real number. (from logistics)
- `/PriorInformationNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: suspected that an aggregate defined as "The type of represention empowering the party to act on behalf of a third party" does not belong to a party acting for itself — refuted because the world's list offers `OWN` and `BEHALF` as the two answers, and stating `OWN` explicitly avoids implying it by absence (IND6). (from context)
- `/PriorInformationNotice/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`: suspected a wrong receiver for a notice of a city department — refuted because a notice goes to the publication office, and the Information Service is that office (its contact is "Publications and register"). (from context)
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `true` and `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`: checked whether the indicators agree with their text — they do: the first prize says its author "is invited to negotiate the follow-up service contract", and nothing in the text makes the jury's ranking advisory. (from context)
- `/PriorInformationNotice/cac:TenderingTerms/cac:EconomicOperatorShortList/cbc:MaximumQuantity` = `5`: whether a short list belongs in a prior information notice — refuted: a PIN of a restricted contest may announce the limitation, and the contract notice repeats it unchanged. (from context)

## Changed in the merge
- broad F2 + parties F1 + context F3 → F2: severity Medium (broad and context gave Low) and Needs decision no (broad and parties said yes), as the customs authority in the earlier flows and as merger B for 09-16: the fix is an encoding of the party, not a change of who it is; the "City of Lumeport as legal entity" option keeps the note that it would need a decision.
- broad F3 and context F2 split into three findings (customs identifier; authority tax scheme; wording of the exemption reason), because the three have different conditions and decisions; parties F3 and F4 and logistics F1 merged into them.
- broad F3 / context F2 (tax scheme copied, Low, no) → authority tax-scheme finding Low, Needs decision yes, because money refuted it with a reason the merge cannot dismiss.
- parties F3 (wording) keeps Low/no; money's refutation of the code is accepted for the code and recorded in the finding.
- Every finding merged from several parts keeps the clearest wording and all evidence; findings are numbered by severity and then by position in the document.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews. (from parties)
