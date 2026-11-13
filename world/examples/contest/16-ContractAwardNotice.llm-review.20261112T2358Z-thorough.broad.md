# LLM review: 16-ContractAwardNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/16-ContractAwardNotice.xml`, Git blob `22f99199125c95d2a66f61bed50f597234a75af6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### contest/16#F1 · Medium · Language code in LocaleCode
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is a language code, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples`, and `grep -rl` for the file count).
- Condition: no `cbc:LocaleCode` holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since none of these documents needs a locale beyond the language; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID.
- Needs decision: no

### contest/16#F2 · Medium · Province in Region
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address. Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is "the political or administrative division of a country", which UBL puts in `CountrySubentity`. The same value occurs 219 times in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>[^<]*'` and `grep -rl --include='*.xml' 'Province of Ferrano'` over `world/examples`).
- Condition: Valdara's province is in `CountrySubentity` (with `CountrySubentityCode` if Urvania has one), and `Region` is absent or holds a region in UBL's sense.
- Options: (preferred) move the value to `CountrySubentity`, in each language rendering the address uses; or remove it if the Urvanian address format has no province line.
- Needs decision: no

### contest/16#F3 · Low · Public bodies described as companies in a commercial register
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the public bodies of this example (Lumeport Public Works Department, Bayvarra Information Service) are registered in the `Federal business register of Bayvarra` with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"). UBL defines `Corporate Registration Scheme` as "The corporate registration scheme used to register the party" and the liquidation status as "the party's liquidation status". A department of the city, a national information service and a review board are not companies in a commercial register and cannot go into liquidation (the contracting party describes itself as "a department of the city of Lumeport" in `cac:ContractingPartyType/cbc:PartyType` where present). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for a register of public bodies, so the value is forced.
- Condition: no public body carries `CorporateRegistrationTypeCode` `COMMERCIAL` or a `CompanyLiquidationStatusCode`; if a registration scheme is given for a public body, its type says what kind of register it is.
- Options: (preferred) leave the registration type and the liquidation status out for public bodies and keep only the identifier of the register they are in; or add a public-sector register type to the list. The choice is about how the world registers public bodies, which is why it needs a decision.
- Needs decision: yes

### contest/16#F4 · Low · Customs and tax data of the contracting authority that the document does not use
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: this document belongs to a design contest; it declares no goods to customs and states no tax. The contracting authority's customs-trader number and its `PartyTaxScheme` look copied from its master data. In addition, `ExemptionReason` is defined as "A reason for the party's exemption from tax"; the code chosen means "Sale to a public body", which describes a transaction, not the status of the party, and this document records no sale.
- Condition: the contracting authority carries a customs-trader identifier and a `PartyTaxScheme` only where the document uses them; where a tax exemption of the party is stated, it is the party's own status.
- Options: (preferred) leave both out of the tendering documents; or, if the tax data stays, word the exemption reason as the party's status (a public body exempt from the state sales tax).
- Needs decision: no

### contest/16#F5 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: a contact is "The primary contact for this party" in its role in this document. Here Brackenmere Furniture takes part in a design contest through its trade-sales desk (`Customer service officer`, department `Sales`), while its partner Saltmere Engineering, where present, uses a bids office; Valdara Industries, a prize winner, is reached at its order desk (`Customer service officer`, `Sales`). The contacts look taken from the parties' trading master data.
- Condition: each contact named in this example is one that handles the party's role in the contest (tenders and competitions for a participant, appeals for the review board).
- Options: (preferred) give each party a contact for its role (e.g. a tenders or design office for the participants, a registry clerk or case officer for the review board); or leave the contact out where the role needs none.
- Needs decision: no

### contest/16#F6 · Low · Master data of the second-prize winner that the award notice does nothing with
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the award notice announces that Valdara Industries won the second prize of a design contest. Its customs-trader number, share capital, stock-exchange listing, the mobile number of its order desk and its logistics provider Castrano Logistics ("Warehousing and despatch") play no part in a prize for a design; they look copied from Valdara's master data (Castrano appears in 75 examples, `grep -rl --include='*.xml' 'Castrano Logistics'`).
- Condition: the winner is described with what the award notice needs to identify it (name, identifier, address, legal entity as needed); no logistics provider, listing or customs data unless the notice uses them.
- Options: (preferred) leave these elements out of the award notice; or give each a role in the story of the contest (hard to see for a logistics provider).
- Needs decision: no

### contest/16#F7 · Low · The winning team is named in the text but only its lead is a winning party
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:Description` = `First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: the result says "First prize to the Brackenmere and Saltmere design team", and the team qualified as a group with Saltmere Engineering as member (`07-TendererQualification.xml`, `12-TendererQualification.xml`). `WinningParty` is "A party that is identified as the awarded by a tender result"; only Brackenmere Furniture is given, so the structured data and the text disagree on who won.
- Condition: the structured result and the description name the same winner: either both members of the group, or the lead as the group's representative, said as such.
- Options: (preferred) add Saltmere Engineering as a further `WinningParty` with `Rank` 1, or say in the description that Brackenmere is the lead of the group; adding the member keeps the result complete.
- Needs decision: no

### contest/16#F8 · Low · Italian street name tagged as English
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: `StreetName` "may be repeated only to provide the same content in multiple natural languages", and each rendering is in the language its `languageID` names. `Via delle Officine` is Italian, not English; an English rendering of the Urvanian name would be an English phrase or the Urvanian name itself. The same value with `en-XB` occurs 31 times (`grep -rho --include='*.xml' '<cbc:StreetName languageID="en-XB">[^<]*'`). If the world's convention is that Bayvarran usage keeps Italian-style exonyms for Urvanian streets, the tag should say which language the text is in.
- Condition: every rendering is in the language its `languageID` names.
- Options: (preferred) decide whether Bayvarran English uses these exonyms; if so, tag them with the language they are in, otherwise give an English rendering. This is a world decision.
- Needs decision: yes

### contest/16#F9 · Low · New version does not say what it changes
- XPath: `/ContractAwardNotice/cbc:VersionID` = `2`
- XPath: `/ContractAwardNotice/cbc:PreviousVersionID` = `1`
- XPath: `/ContractAwardNotice/cbc:Note` = `Results of the design contest for the harbour promenade bench.`
- Why: this is version 2 of a published notice with the same `cbc:ID` as version 1; it changes the first prize from 6,000 to 8,000 lume (`15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`), which corrects version 1 to the value the contract notice announced. The only `Note` is the one of version 1, so a reader of the published notice cannot see that, or what, it changes (UBL has no dedicated element for this, which leaves the free-text `Note`, defined as "information that is not contained explicitly in other structures").
- Condition: the new version states which values it changes and, where it corrects an error, that it is a correction.
- Options: (preferred) add a `Note` naming the changes (and the reason); or another means the world's notices use for corrections.
- Needs decision: no

## Checked and consistent
- First prize 8,000 lume agrees with the contract notice (`08-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`).
- `PreviousDocumentReference` `LPWD-DOC-26-0634` resolves to the contract notice (`03-ContractNotice.xml`, `08-ContractNotice.xml`).
- Two prizes listed and the description "The jury withheld the third prize: no other design reached prize standard" agree with the condition of the third prize in the notices.
- Four designs received (`ReceivedTenderQuantity` 4) lies within the three to five participants of the short list; one foreign tender agrees with Valdara Industries being from Urvania (XU).
- Award date 2026-06-28 is after the tender deadline 2026-06-12 and before the issue date; `NegotiationDescription` and `PreSelectedParty` (Brackenmere) agree with `FollowupContractIndicator` `true` and the first-prize description in the notices.
- GS1 GLN `9523710900008` has a valid check digit (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company.
- ISIN `XU0001042501` has a valid check digit (`check_ids.py`); `XU` is not an ISO 3166 country code, so it cannot be mistaken for a real security.
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). Valdara Industries is described the same way in both award notices.

## Considered and refuted
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cbc:Rank` = `2`: suspected that the second-prize winner is not "awarded" — refuted because in a design contest the result is the award of prizes, and the second prize is awarded to Valdara Industries.
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: suspected a mismatch with the definition "The number of shares in the capital stock" — refuted as a separate finding because the element is of type Amount, so a monetary share capital is the reading the type supports; its presence is covered by the master-data finding.
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: suspected that the ISO 6523 ICD 0990 might be a real assigned code — refuted as far as own knowledge goes: the assigned ICDs run in the 0002–0240 range, 0990 is not among them, and the world's identifiers use it consistently.
- `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`: suspected that the indicator ("published for service contracts within certain service categories") does not fit — refuted because the contest is a services procurement (CPC 83912) and the notice is published.
