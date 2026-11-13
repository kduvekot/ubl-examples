# LLM review: 15-ContractAwardNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/15-ContractAwardNotice.xml`, Git blob `df753bf00bfa8a999e3e4cf1826906a62184db6d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### contest/15#F1 · High · First prize of 6,000 lume contradicts the 8,000 lume of the contract notice it refers to
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`
- XPath: `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0634`
- XPath: `03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`
- XPath: `08-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`
- XPath: `04-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeDescription` = `Three prizes; the first is 8,000 lume.`
- Why: `Prize/ValueAmount` is "The monetary value amount of a prize". The award notice refers to the contract notice `LPWD-DOC-26-0634`, which in both versions promises 8,000 lume for the first prize, as do version 2 of the prior information notice (`02-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`) and both calls for tenders (`09-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`). 6,000 is only in the superseded first version of the PIN (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`); the second prize (4,000) agrees. Merge's attempt to refute: nothing in this notice says the jury reduced the prize or that a different prize rule applied; the first prize's own description is the one of the notices ("its author is invited to negotiate the follow-up service contract"), and the result text names no reduction. The contradiction stands. A diff of the two `*.xml` shows that the first-prize amount is the only content change between this notice and its version 2 (`16-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), so the story may mean an erroneous publication that version 2 corrects; neither notice says so (both notes are `Results of the design contest for the harbour promenade bench.`).
- Condition: the first prize equals the 8,000 lume of the contract notice; or, if this version is meant to carry an error, version 2 states that it corrects the first-prize amount.
- Options: (a, preferred if the correction is the story) keep 6,000 here and let version 2 say in a note that it corrects the first prize from 6,000 to 8,000 lume (see the review of `16-ContractAwardNotice.xml`, F11); (b) 8,000 here and give version 2 another reason to exist, or drop it. Which story is meant is a decision.
- Needs decision: yes
- From: broad (F1), money (F1), logistics (F1), context (F1)

### contest/15#F2 · Medium · The winning team is reduced to its lead: Saltmere Engineering is not a winning party
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:Description` = `First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cac:PreSelectedParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `12-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: `WinningParty` is "A party that is identified as the awarded by a tender result". The result text gives the first prize to "the Brackenmere and Saltmere design team", and the tenderer qualification names Saltmere as member (30 %, `12-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `30`). The structured result names only Brackenmere, as rank-1 winner and as the party invited to negotiate, and no role says it acts as lead. Who won is what an award notice is for, so the structured data misses information the document's purpose depends on (Medium, as parties). Not High: Brackenmere as lead may represent the group, so text and structure do not strictly contradict each other.
- Condition: the award notice identifies every member of the winning group at rank 1, or states in structured form that Brackenmere acts as lead of a group including Saltmere Engineering.
- Options: (preferred) add Saltmere Engineering as a further `WinningParty` with `Rank` 1 (UBL has no group aggregate in `TenderResult`; eForms likewise lists every member of a winning group, own knowledge of parties), optionally also as pre-selected party; or name Brackenmere in the text as lead of the group.
- Needs decision: no
- From: parties (F3, Medium), broad (F8, Low), context (F4, Low)

### contest/15#F3 · Medium · NoticeTypeCode CAN is the standard-procedure award notice, not a design-contest result
- XPath: `/ContractAwardNotice/cbc:NoticeTypeCode` = `CAN`
- Why: the procedure is a design contest (`DESIGNCONTEST`). The world list describes `CAN` as "Announces the result (eForms can-standard)" and has no type for a design contest, whereas eForms distinguishes the results of a design contest (can-desg) from a standard award (own knowledge of context). UBL's own definition of `ContractAwardNotice/NoticeTypeCode` names the distinction: "The type of notice (CAN general, CAN social, Design)" (checked in the model). The code exists, but it is not the one this situation calls for.
- Condition: the notice type identifies a design-contest result notice.
- Options: (preferred) add design-contest notice types to the world's NoticeTypeCode list (as eForms cn-desg / can-desg) and use the award one here; or widen the description of `CAN` to cover design contests.
- Needs decision: no
- From: context (F2, Medium, yes)

### contest/15#F4 · Medium · Language code in LocaleCode
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code and repeats `Language/cbc:ID` (section 6: Medium). 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`, recounted).
- Condition: every `Language/LocaleCode` is absent or holds a locale from a locale list named in its `listID`.
- Options: (preferred) leave `LocaleCode` out; or a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### contest/15#F5 · Medium · Province in Region
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the administrative division that UBL puts in `CountrySubentity` (section 6 names it as Medium). The Bayvarran addresses of the same notice put their state in `CountrySubentity` with a code. The value occurs 219 times in 104 files (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano<'` and `grep -rl` over `world/examples`, recounted; parties counted 111 files with another pattern).
- Condition: Valdara's province is in `CountrySubentity` (with a code if Urvania has a list), and `Region` is absent or holds a region in UBL's sense.
- Options: (preferred) move the province to `CountrySubentity`, in each rendering; or drop it if the Urvanian format has no province line.
- Needs decision: no
- From: broad (F3), parties (F4)

### contest/15#F6 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: the Public Works Department ("a department of the city of Lumeport", in the same notice) and Bayvarra Information Service are entered as `COMMERCIAL` ("A register of businesses") and have a liquidation status; public bodies are not businesses and are not liquidated, and a city department is not a legal person of its own (section 5; parties). The world list has no register type for public bodies.
- Condition: no public body carries a `CompanyLiquidationStatusCode` or a registration scheme of the type "Commercial register".
- Options: (preferred) drop the liquidation status and the registration type for public bodies; or a public-sector register type; or the City of Lumeport as legal entity of the department (a change of who the entity is).
- Needs decision: no
- From: broad (F4), parties (F1), context (F9)

### contest/15#F7 · Low · Contacts of the prize winners are sales and order desks
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the winners are reached through Brackenmere's trade-sales desk and Valdara's order desk (customer service officers in sales), the contacts for trade customers' orders, not the offices that handled the contest. They are the parties' general master-data contacts.
- Condition: each winner's contact handles its part in the contest.
- Options: (preferred) a bids or design office contact; or no contact where the electronic address is the channel.
- Needs decision: no
- From: broad (F6), parties (F7), context (F7)

### contest/15#F8 · Low · Customs-trader numbers and the winners' tax registrations in a result notice
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- Why: section 4.8. The notice declares nothing to customs and taxes nothing: the department's and Valdara's customs-trader numbers serve customs declarations (the department's is in 55 files, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`), and the winners' sales-tax and VAT registrations serve their invoices; no element refers to them. They are copied from master data.
- Condition: the parties carry only identifiers and registrations the notice uses.
- Options: (preferred) leave them out of the award notice.
- Needs decision: no
- From: broad (F5, part), money (F3), parties (F6, part), logistics (F2, part), context (F8)

### contest/15#F9 · Low · Share capital, stock listing, mobile number and logistics provider of the second-prize winner
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: the notice announces that Valdara Industries won the second prize for a design. Its share capital, stock-exchange listing, the mobile number of its order desk and its warehousing and despatch provider play no part in a prize: nothing is stored or despatched under a design contest. They are the master data Valdara carries as a seller in the goods flows (`VI-SP-2026-01` is in 75 files, `grep -rl --include='*.xml' VI-SP-2026-01 world/examples | wc -l`, recounted; logistics counted 73 outside this flow).
- Condition: the second-prize winner is described with what the notice needs to identify it; no listing, share capital or logistics provider unless the notice uses them.
- Options: (preferred) leave these elements out of the award notice; or give each a role in the contest story (hard to see for a logistics provider).
- Needs decision: no
- From: broad (F7), parties (F6, part), logistics (F2, part), context (F6)

### contest/15#F10 · Low · The contracting authority's tax scheme in a result notice
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: broad and context: the notice states no tax, so the department's tax scheme looks copied (section 4.8). Money refuted it: the buyer's exemption bears on the follow-up service contract the notice announces (its fees are net of the state sales tax). The merge cannot settle it: the follow-up contract is still to be negotiated and the notice states none of its amounts, but its announcement is part of the notice.
- Condition: the contracting authority's tax scheme is in the notice only if the notice relies on it (e.g. a statement that the follow-up fees are net of the state sales tax), or it is absent.
- Options: (preferred) leave it out; or keep it and say what it qualifies.
- Needs decision: yes
- From: broad (F5, part), context (F8, part); refuted by money (counter-argument above)

### contest/15#F11 · Low · The party's tax exemption reason is worded as a sale
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the code's list definition ("A body of the federation, a state or a city buys free of sales tax") is the buyer's status and fits; the text begins "Sale to a public body", a transaction. Applies only if F10 keeps the tax scheme.
- Condition: where stated, the text describes the party's status, not a sale.
- Options: (preferred) "Public body: exempt from the state sales tax"; or a status code.
- Needs decision: no
- From: broad (F5, part), parties (F5), context (F8, part)

### contest/15#F12 · Low · Estimated contract amount of 54,000 lume: what it covers is not stated, and it is unchanged after the first prize rose
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: as in the notices: a services procurement (prizes, participation payments, follow-up design contract) with an estimate equal to 60 × the 900 lume production limit, unchanged in every notice although the first prize rose from 6,000 to 8,000 (money; 8 contest files carry it, all `54000.00`). In an award notice the estimate is moreover past: the result is known (prizes 8,000 + 4,000 announced, payments at most 4 × 1,000), and the follow-up contract is still to be negotiated. No arithmetic contradiction can be shown without a breakdown (broad's argument in 09).
- Condition: what the estimate covers can be read from the notice, and it is consistent with the prizes.
- Options: (a, preferred) state what it covers and adjust it where the prize rose; (b) if it is the production budget, remove it from `RequestedTenderTotal`.
- Needs decision: yes
- From: money (F2)

### contest/15#F13 · Low · PublishAwardIndicator without the situation its definition names
- XPath: `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`
- Why: "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)." Nothing in the world names service categories for which publication is optional (the case the indicator was made for, Annex II B services in the old EU forms, own knowledge of context), so `true` has no business reason the document shows (IND5). Broad refuted it: the contest is a services procurement (CPC 83912) and the notice is published. The merge cannot settle it: the definition speaks of "certain service categories", which the world does not define, and whether CPC 83912 is one of them is not stated anywhere.
- Condition: the indicator is absent, or the world has a rule on service categories that it answers.
- Options: (preferred) leave it out; or record the world rule and keep `true`.
- Needs decision: yes
- From: context (F5); refuted by broad (counter-argument above)

### contest/15#F14 · Low · Italian street name and legal form of the Urvanian winner in English-tagged or untagged renderings
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: `StreetName` "may be repeated only to provide the same content in multiple natural languages", each rendering in the language its `languageID` names. `Via delle Officine` is Italian, tagged `en-XB`; the legal form is Italian with an English gloss in a single untagged rendering. Parties refuted the street name: the examples consistently give Urvanian places Italianate exonyms in English renderings (the city as "Ferrano" beside `qau` "Ruldraz"), as English texts keep foreign street names, and the tag names the Bayvarran variant. The merge cannot settle it (the same as in the earlier flows): for a street name the convention is defensible, for the legal form it is less so. Whether a Bayvarra-issued notice tags an Urvanian address `en-XB` or `en-XU` is the same open convention.
- Condition: every rendering is in the language its `languageID` names, or the world records the convention that English renderings keep Italianate Urvanian names.
- Options: (preferred) record the convention in the story, and give the legal form an English rendering (or tag the Italian); or English renderings throughout.
- Needs decision: yes
- From: broad (F9); refuted by parties (counter-argument above); legal-form line added by the merge

### contest/15#F15 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the same date for 25 companies (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, recounted), a holiday; a filler unless the world has a reason. (Valdara's `1962-04-12` is a date of its own.)
- Condition: Brackenmere's registration date has a reason in the world, or is absent.
- Options: (preferred) its own date; or leave it out; or record the date as a story event.
- Needs decision: yes
- From: parties (F8)

## Checked and consistent
- `PreviousDocumentReference` `LPWD-DOC-26-0634` resolves to the contract notice (`03-ContractNotice.xml`, `08-ContractNotice.xml`) of the same `ContractFolderID` (broad, logistics).
- Two prizes listed; "The jury withheld the third prize" agrees with the conditional third prize of the notices; second prize 4,000 agrees with 03/08 (broad, money, logistics, context).
- `ReceivedTenderQuantity` 4 lies within the short list 3–5 (payments at most 4,000 lume); `ReceivedForeignTenderQuantity` 1 agrees with Valdara of Urvania (broad, money, logistics, context).
- `AwardDate` 2026-06-28 after the design deadline (2026-06-12 12:00) and before the issue date (broad, logistics, context).
- `NegotiationDescription` and `PreSelectedParty` agree with `FollowupContractIndicator` and the first-prize description of the notices; `TenderResultCode` `AWARDED` fits (broad, logistics, context).
- Prizes in `XBL` also for the Urvanian winner: the buyer's commitment in its own currency (money).
- GLN 9523710900008 and ISIN `XU0001042501` have valid check digits (`check_ids.py`); GS1 prefix 952 is reserved, `XU` is not an ISO 3166 code, market code XFER is not in the ISO 10383 MIC source (broad, parties, logistics).
- Valdara's register ID, `CompanyID` and endpoint agree; every party is described as in the other examples of the flow (broad, parties, logistics).
- Diff of `15-ContractAwardNotice.xml` and `16-ContractAwardNotice.xml` (merge): apart from UUID, issue date and time and the version elements, only the first prize differs.
- Physics: nothing to calculate (logistics).

## Considered and refuted
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cbc:Rank` = `2`: the second-prize winner is not "awarded" — refuted: in a design contest the result is the award of prizes (from broad).
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: an amount where the definition says "The number of shares in the capital stock" — refuted as a finding of this example: the element's type is Amount, so the definition itself is inconsistent; its presence is F9 (from broad and parties).
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: ICD 0990 a real assigned code — refuted as far as known (assigned ICDs are in the low 0001–02xx range; not checked against the current register) (from broad and logistics).
- `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`: refuted by broad (services procurement, published); kept as F13 (Low, needs decision).
- `/ContractAwardNotice/cac:TenderingProcess/cbc:NegotiationDescription`: the notice should state the value of the follow-up contract — refuted: it is still to be negotiated (from money). Also suspected to describe a later procedure — refuted: the follow-up negotiation is part of the announced process (from context).
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: copied master data — refuted by money (fees of the follow-up contract are net); the merge could not settle it, so it is F10.
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 too general — refuted (from parties).
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: address vs contact department — refuted: the same unit (from parties).
- `/ContractAwardNotice/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone`: two postal zones on one square — refuted (from parties).
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian text tagged `en-XB` — refuted by parties as the world's exonym convention; kept as F14 (Low, needs decision).
- `/ContractAwardNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cac:PreSelectedParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: `PreSelectedParty` is for a negotiated procedure; a short list in an award notice — refuted: the follow-up contract is negotiated with the first-prize winner without a new call, which is such a procedure (from parties and context).
- `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0634`: ambiguous between the two versions of the contract notice — refuted: versions share one document ID by design and the dates make the current version clear (from logistics).
- `/ContractAwardNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: refuted: the list offers OWN and BEHALF, and stating OWN avoids implying it by absence (from context).
- `/ContractAwardNotice/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`: a wrong receiver — refuted: the notice goes to the publication office (from context).

## Changed in the merge
- broad/F1, money/F1, logistics/F1, context/F1 → F1: combined; the merge's refutation attempt and the diff with 16 added.
- parties/F3 (Medium), broad/F8 (Low), context/F4 (Low) → F2: Medium, as parties, because identifying the winners is the purpose of an award notice; not High (see Why). This differs from the qualification response (11/F4, Low), where the lead may answer for the group.
- context/F2 (Medium, yes) → F3: needs decision no, because the fix is a code-list entry, not a change of the story (aligned with merger A for the contract notices 03/08).
- broad/F4 (Low, yes), parties/F1 (Medium, yes), context/F9 (Low, no) → F6: Medium, needs decision no (aligned with the earlier flows).
- broad/F5, broad/F7, money/F3, parties/F6, logistics/F2, context/F6, context/F8 → split into F8 (customs numbers and the winners' tax registrations), F9 (Valdara's share capital, listing, mobile and logistics provider), F10 (the authority's tax scheme, Low/yes after money's refutation) and F11 (exemption wording, parties/F5).
- broad/F6, parties/F7, context/F7 → F7.
- broad/F9 → F14: legal-form line added (as in the earlier flows); parties' refutation added.
- context/F5 → F13: broad's refutation added; needs decision kept yes.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties; they belong to those examples' reviews (from parties).
