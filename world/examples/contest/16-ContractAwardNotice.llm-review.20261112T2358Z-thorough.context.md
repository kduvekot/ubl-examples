# LLM review: 16-ContractAwardNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/16-ContractAwardNotice.xml`, Git blob `22f99199125c95d2a66f61bed50f597234a75af6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 70e2a4d 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### contest/16#F1 · Medium · NoticeTypeCode `CAN` is the standard-procedure type, not a design-contest notice
- XPath: `/ContractAwardNotice/cbc:NoticeTypeCode` = `CAN`
- Why: The procedure is a design contest (ProcedureCode `DESIGNCONTEST`). In the world's NoticeTypeCode list `CAN` is described as "Contract award notice … Announces the result (eForms can-standard)"; the list has no notice type for a design contest, while the eForms list it cites distinguishes them (can-standard for a standard procedure, can-desg for the results of a design contest). The UBL definition of ContractAwardNotice/NoticeTypeCode itself names the distinction: "The type of notice (CAN general, CAN social, Design)". So the code exists but is not the one this situation calls for.
- Condition: The notice type code of this notice identifies a design-contest notice.
- Options: Preferred: add design-contest notice types to the NoticeTypeCode list (as eForms cn-desg / can-desg) and use them here. Alternative: keep `CN`/`CAN` but change the list's description so that it covers design contests.
- Needs decision: yes

### contest/16#F2 · Medium · LocaleCode carries a language code
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines Language/LocaleCode as "A code signifying the locale in which this language is used", and Language/ID as "An identifier for this language". Every party here gives `en` with listID `ISO 639` in both: the locale element repeats the language code instead of naming a locale (a language in a region, such as en-XB). A language code is a valid code, but not the one the definition names. The same pattern (`<cbc:LocaleCode listID="ISO 639">`) occurs in 213 example files, 362 times (counted with `grep -c` over `world/examples/*/*.xml`).
- Condition: Every LocaleCode either names a locale (language and country/region) from a locale scheme, or is absent.
- Options: Preferred: drop LocaleCode where the party has no locale to state beyond its language (Language/ID already says English). Alternative: a locale code such as `en-XB` with a locale listID (e.g. BCP 47).
- Needs decision: no

### contest/16#F3 · Low · Winner given as the lead member only, while the result names the team
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:Description` = `First prize to the Brackenmere and Saltmere design team, second to Valdara Indus…`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: The result text gives the first prize to "the Brackenmere and Saltmere design team", the group that qualified (tenderer qualification: Brackenmere lead, Saltmere member). The WinningParty of rank 1 is Brackenmere Furniture alone, and Saltmere Engineering does not appear, so the structured winner is narrower than the text.
- Condition: The structured winner of rank 1 and the result text name the same winner.
- Options: Preferred: add Saltmere Engineering as a second party of the winning team (or name the group in the party). Alternative: change the text to name Brackenmere as the winner, leading the team.
- Needs decision: no

### contest/16#F4 · Low · PublishAwardIndicator used outside its definition
- XPath: `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`
- Why: ContractAwardNotice/PublishAwardIndicator: "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)." This is a design contest with prizes, published like every notice of the flow; nothing in the world names service categories for which publication is optional (the case the indicator was made for: Annex II B services in the old EU forms, own knowledge). The value `true` has no business reason the document shows (IND5).
- Condition: Either the indicator is absent, or the world has a rule on service categories that it answers.
- Options: Preferred: leave it out. Alternative: state the world rule that makes publication of contest results optional and keep `true`.
- Needs decision: yes

### contest/16#F5 · Low · Logistics service provider of the second-prize winner in a contest result
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara Industries is described with its warehousing and despatch provider, Castrano Logistics. A design contest result awards prizes for designs; nothing is warehoused or despatched under it. Data copied from the party's master data into a document that does not use it (section 4.8).
- Condition: The winning parties of this notice carry no service provider, unless the notice uses it.
- Options: Preferred: drop the ServiceProviderParty here. Alternative: none seen.
- Needs decision: no

### contest/16#F6 · Low · Economic operator contact is a sales desk, not the contest contact
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The contact of a participant in a design contest is the person or office that handles the request to participate, the design and the questions of the jury. The contact given is a sales or order desk (`Customer service officer` in `Sales`), which fits a trading partner taking orders, not a team entering a contest. Elsewhere in the flow the consortium member Saltmere Engineering is given a "Bids office" contact, which shows the kind of contact meant.
- Condition: The economic operator's contact in this document is the office or person that handles the contest.
- Options: Preferred: a bids or design office contact for the lead member. Alternative: no contact, where the electronic address is the channel.
- Needs decision: no

### contest/16#F7 · Low · Tax and customs identity copied into a document that does nothing with them
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `VAT`
- Why: ContractAwardNotice carries no amount that is taxed, no tax total and no customs procedure, yet the parties bring their tax registration (PartyTaxScheme) and, where they have one, their customs trader number (AdditionalPartyIdentification, scheme `customs-trader`). Section 4.8 of the review rules: data copied from a party's master data into a document that does not use it. For the contracting authority the tax scheme also states ExemptionReasonCode `PUBLIC`, whose meaning in the list is "Sale to a public body"; PartyTaxScheme/ExemptionReasonCode is "A reason for the party's exemption from tax", so even where the scheme is kept, the reason should be the party's own status, not a kind of sale.
- Condition: The parties of this document carry no tax scheme and no customs trader number, unless something in the document uses them; where a PartyTaxScheme of a public body is kept, its exemption reason names the party's status.
- Options: Preferred: leave PartyTaxScheme and the customs trader identifier out of the notices and qualification documents, as the Bayvarra Information Service is described throughout the flow. Alternative: keep them only where a tax or customs check is part of the step, and say so in the document.
- Needs decision: no

### contest/16#F8 · Low · Public bodies described as companies in the commercial register, with a liquidation status
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The public bodies of this document (ISIC 84xx: Lumeport Public Works Department, "a department of the city of Lumeport", Bayvarra Information Service) are registered in a CorporateRegistrationScheme of type `COMMERCIAL` ("Commercial register") and carry CompanyLiquidationStatusCode `ACTIVE` ("Active, not in liquidation"). A city department or a state authority is not a company in a commercial register and cannot be liquidated, so "the party's liquidation status" has no meaning for it (review checklist, party legal entity).
- Condition: No public body in this document has a liquidation status, and its registration scheme, if stated, is not a commercial register.
- Options: Preferred: no CompanyLiquidationStatusCode for public bodies, and a registration scheme of a type for public bodies (or none). Alternative: keep the federal register but with a type code that says it registers public bodies.
- Needs decision: no

## Checked and consistent
- The result agrees with the terms: three prizes announced, the third "if the jury finds it of prize standard"; the notice awards two and says the jury withheld the third.
- ReceivedTenderQuantity 4 lies within the short list of 3 to 5; ReceivedForeignTenderQuantity 1 agrees with one prize winner from Urvania (Valdara Industries, scheme `XU:register`).
- AwardDate 2026-06-28 lies after the design deadline (2026-06-12) and before the issue date.
- TenderResultCode `AWARDED` ("A winner was chosen") fits a contest whose first prize was given.
- Prize[1] = `8000.00`, as announced in the contract notice; version 2 corrects the 6,000 of version 1 (`15-ContractAwardNotice.xml`).

## Considered and refuted
- `/ContractAwardNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: suspected that an aggregate defined as "The type of represention empowering the party to act on behalf of a third party" does not belong to a party acting for itself — refuted because the world's list offers `OWN` and `BEHALF` as the two answers, and stating `OWN` explicitly avoids implying it by absence (IND6).
- `/ContractAwardNotice/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`: suspected a wrong receiver for a notice of a city department — refuted because a notice goes to the publication office, and the Information Service is that office (its contact is "Publications and register").
- `/ContractAwardNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cac:PreSelectedParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: a short list in an award notice — refuted: it announces the negotiated procedure without a new call for the follow-up contract, and PreSelectedParty is "preselected to submit a Tender in a negotiated procedure", which is exactly that.
- `/ContractAwardNotice/cac:TenderingProcess/cbc:NegotiationDescription` = `The service contract for the detailed design…`: suspected that it describes a later procedure rather than "the negotiation to be followed during the tendering process" — refuted: the follow-up negotiation is part of the contest's announced process (FollowupContractIndicator), and the award notice is where it is announced.
