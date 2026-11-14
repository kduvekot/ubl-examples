# LLM review: 12-BusinessInformation.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/12-BusinessInformation.xml`, Git blob `0bf87195abba0708389105425a425c36428e3dc5` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/12#F1 · Medium · Language code in LocaleCode
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F3), context (F5), logistics (F2), parties (F1)

### tender/12#F2 · Medium · Two public bodies, sender and receiver, described as companies in a commercial register with a liquidation status
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". The Bayvarra Information Service, which keeps the register of economic operators, and the Lumeport Public Works Department (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`) are public bodies (both ISIC 8411); neither is a business, neither can be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F6), parties (F3)

### tender/12#F3 · Medium · A province in Region
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran addresses of the flow put their state in `CountrySubentity`. Recounted: 219 occurrences in 104 of the 250 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`, `-l` for files).
- Condition: The province of an Urvanian address is in `CountrySubentity` (with a code if Urvania has a list); `Region` is absent or holds a region in the sense of the definition.
- Options: (a) move the value to `CountrySubentity` (preferred); a code is optional.
- Needs decision: no
- From: broad (F4), parties (F2)

### tender/12#F4 · Medium · Two competing tenderers presented as a group of business parties
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupTypeCode` = `SAMEACTIVITY`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupType` = `Tenderers in this procedure registered for ISIC 3100`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[1]/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[2]/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/BusinessInformation/cbc:BriefDescription` = `Valdara Industries: registered, no exclusion grounds recorded.`
- Why: `BusinessPartyGroup` is "A group of Business Parties", typed by "A code to specify the type of grouping (e.g. EEIG)": a grouping the business belongs to (an economic interest grouping, a corporate group, a consortium). The document is information about one business, Valdara Industries. The "group" here is Valdara and its competitor Brackenmere, i.e. a list of who tendered; that is no grouping either belongs to, it is not registration data of Valdara, a register of economic operators would not know it (tenders are confidential until award), and it discloses a competitor in Valdara's extract. Parties refuted it for its lens (both are tenderers with ISIC 3100, as the group type says; logistics confirmed the member IDs); that confirms the values, not that the element fits.
- Condition: `BusinessPartyGroup` is present only for a grouping the business party is a member of.
- Options: (a) remove the group (preferred); (b) if the service is to report on all tenderers, one extract per tenderer; (c) if Valdara belongs to a real grouping, state that one.
- Needs decision: yes
- From: broad (F2), context (F3); refuted by parties for its lens (carried)

### tender/12#F5 · Medium · OperationType holds the company's line of business, not the operation the document performs
- XPath: `/BusinessInformation/cac:OperationType/cbc:Code` = `MANUFACTURE`
- XPath: `/BusinessInformation/cac:OperationType/cbc:Description` = `Manufacture of furniture for public spaces.`
- XPath: `/BusinessInformation/cac:BusinessParty/cbc:IndustryClassificationCode` = `3100`
- Why: `OperationType` is "The type of operation for which this document is created", its code "A code to specify the type of operation (e.g. deletion)": the operation on the business registration information (registration, update, deletion, extract). "Manufacture" is what Valdara does, which the party's ISIC 3100 and the business capability already say; what the document is created for is in `NoticeSubType` (`EXTRACT`, "Register extract").
- Condition: `OperationType` states an operation on the registration information, from a list of such operations, or is absent.
- Options: (a) remove it, since `NoticeSubType` `EXTRACT` says what the document is (preferred); (b) an operation code meaning "extract" or "consultation".
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1)

### tender/12#F6 · Low · A requested publication date on an extract sent to one authority
- XPath: `/BusinessInformation/cbc:RequestedPublicationDate` = `2026-02-27`
- XPath: `/BusinessInformation/cbc:Note` = `Extract from the register of economic operators for the evaluation.`
- XPath: `/BusinessInformation/cac:NoticeSubType/cbc:SubTypeDescription` = `Extract asked for by a contracting authority.`
- Why: `RequestedPublicationDate` is "The requested publication date for this Business Registration Information Notice." This is an extract "asked for by a contracting authority" and sent to it "for the evaluation"; nothing is to be published, and the date equals the issue date. The merge keeps Low (broad): the value has no business reason (section 4.8), but it does not contradict another value; context rated it Medium.
- Condition: A publication date is present only when the information is to be published.
- Options: (a) remove it (preferred); none other seen.
- Needs decision: no
- From: broad (F5), context (F2)

### tender/12#F7 · Low · Urvanian declared as an additional language of the document, but only an address is in it
- XPath: `/BusinessInformation/cbc:NoticeLanguageCode` = `en`
- XPath: `/BusinessInformation/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- XPath: `/BusinessInformation/cbc:BriefDescription` = `Valdara Industries: registered, no exclusion grounds recorded.`
- Why: For the argument (context): `AdditionalNoticeLanguage` is "An additional official language used in this document"; the texts (note, brief description, capability, group type, operation and sub-type descriptions) are English only; the only Urvanian is the street and city of Valdara's address (3 of the 6 `languageID` attributes, recounted). Against it (broad): the business is Urvanian and its registration data are bilingual, so Urvanian is used in the document. The address renderings do make it "used", but an official language of a notice is the language its text is given in; the merge cannot settle which reading applies, so Low with both arguments.
- Condition: Every language declared for the document is the language of its texts, or the world records that a language used in party data counts.
- Options: (a) remove the additional language (the receiver is a Bayvarran authority) (preferred); (b) add Urvanian renderings of the descriptions.
- Needs decision: yes
- From: context (F6); refuted by broad (carried)

### tender/12#F8 · Low · The department's customs trader number in a register extract
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Copied master data (section 4.8): the receiver's customs trader number identifies the department towards customs; nothing in this extract is declared to customs. Context also listed the business party's customs trader number; the merge takes that line out (see "Refuted in the merge"): what the register holds about its subject is the content of an extract.
- Condition: The receiver carries only the identifiers the document uses or that identify it.
- Options: (a) leave the department's customs trader number to the customs and transport documents (preferred); (b) keep it if the world's rule is that every document carries all identifiers of a party, and state that rule.
- Needs decision: no
- From: context (F9, part), parties (F4)

### tender/12#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F7), parties (F5)

### tender/12#F10 · Low · Valdara's address tagged en-XB here and en-XU in its own documents; Italian names tagged English
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same English rendering of Valdara's address is tagged `en-XB` here and `en-XU` in 13 and 15 (checked in the merge), and the street name, tagged as English, is Italian. Parties refuted it: these are the world's English-language names of Urvanian places (accepted as given), the texts are identical everywhere, and the tag follows the locale of the issuer consistently (03, 12, 14, 16 … against 13, 15 …). analysis/review-merge-decisions.md keeps this as Low with Needs decision yes in every flow ("one rule for the language tag"), because no rule is stated; the merge aligns with it and carries the refutation as the counter-argument.
- Condition: One documented rule decides the tag of a party's English rendering (the party's own variety or the issuer's), and it is applied in every example.
- Options: (a) record the rule (issuer's variety) in the world's conventions (preferred: it is already applied consistently); (b) tag the party's own variety (`en-XU`) everywhere.
- Needs decision: yes
- From: merge (parties' refuted candidate, aligned with the main decisions table)

### tender/12#F11 · Low · Valdara's legal form in a single untagged rendering
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`
- Why: The address of the same party is given in Urvanian and English, each tagged; the legal form has one rendering without `languageID`, while 13 and 15 give it in Urvanian (`qau`) and English (`en-XU`). Parties mentioned it within its refuted candidate on language tags; earlier merges keep it as a separate Low/no finding (render it like the address).
- Condition: The legal form is rendered like the address: in each language the document uses for the party, each tagged.
- Options: (a) both renderings, tagged, as in 13 (preferred); (b) one rendering with its `languageID`.
- Needs decision: no
- From: merge (parties' refuted candidate, aligned with the main decisions table)

### tender/12#F12 · Low · Large enterprise with 180 employees
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: The world's list defines `LARGE` as "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL; checked in `world/codelists/gc/EntitySizeCode.gc`). In its qualification Valdara states 180 employees and a financial capability of 9200000.00 lume; nothing in the flow states a turnover above the limit, so nothing supports `LARGE`. Not a strict contradiction, because the turnover alternative of the definition is not stated as such (unlike Marrowdale's `SMALL` with 85 persons, 10 F1, where both conditions must hold); hence Low, with a decision on what Valdara is.
- Condition: The size class of Valdara agrees with the employees and financial figures stated for it in the flow.
- Options: (a) state a turnover above 50 million lume (or 250+ employees) if Valdara is meant to be a large listed company (preferred: it is listed and has 250 million ferra of capital); (b) `MEDIUM` in every example that describes it.
- Needs decision: yes
- From: parties (F6)

### tender/12#F13 · Low · Castrano Logistics, Valdara's warehouse contractor, in a register extract
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: For the argument (context): `ServiceProviderParty` is "a party providing a service to this party"; an extract on registration and exclusion grounds has no use for the arrangement number and key account desk of the company's warehouse contractor; it looks copied from master data. Against it (parties, broad): the document is "A document used to provide information about a business", which describes the party as such, so its service providers are part of that description. The merge cannot settle whether a register of economic operators holds such data; Low with both arguments.
- Condition: Either the extract carries only what the register holds about the business, or the world records that the register holds service providers.
- Options: (a) remove the service provider here (preferred: the note limits the extract to registration for the evaluation); (b) keep it and record what the register holds.
- Needs decision: yes
- From: context (F8); refuted by parties and broad (carried)

### tender/12#F14 · Low · Brochure and ISO 9001 certificate referenced in an extract issued by the register
- XPath: `/BusinessInformation/cac:BrochureDocumentReference/cbc:ID` = `VI-BROCHURE-26`
- XPath: `/BusinessInformation/cac:AdditionalDocumentReference/cbc:ID` = `VI-ISO9001-CERT`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`
- Why: The sender is the public information service and the document an "extract from the register of economic operators for the evaluation". A company brochure ("A reference to a company brochure document") is the business's marketing material; in an extract issued by a register it suggests that the register vouches for it. The certificate fits only if the register records certifications. Context also noted that both references have an ID only; logistics refuted that part (the brochure element and the certificate's ID say what they are), and the merge follows logistics on it.
- Condition: An extract issued by the register refers to what the register holds; material of the business is referenced in documents the business sends.
- Options: (a) remove the brochure; keep the certificate only if the register records certifications, with a document type (preferred); (b) let Valdara send a business profile of its own with these references.
- Needs decision: no
- From: context (F7); the "ID only" part refuted by logistics

### tender/12#F15 · Low · Capability figures that say neither what they measure nor agree with Valdara's own qualification
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:Description` = `Steel frame benches, cast, galvanised and coated in its own plant.`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- XPath: `/BusinessInformation/cac:BusinessCapability/cac:SuppliedEvidence/cbc:Name` = `Annual accounts`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: `ValueAmount` is "A monetary amount as a measure of this capability", `ValueQuantity` "A quantity as a measure of this capability". The production capability carries 4800000.00 lume and 6000 EA without a period or a statement of what they are (yearly output? production value? the evidence "Annual accounts" suggests a sales figure). In its own qualification (13), two days earlier, Valdara declares "4,000 benches a year" and a financial capability of 9200000.00 lume. If the quantities are both yearly bench output, 6000 and 4000 contradict each other; if not, neither document says so, and the evaluator who receives both cannot reconcile them. Arithmetic re-done in the merge: 4800000.00 / 6000 = 800.00 lume a piece; 6000 × 499.00 (the tendered unit price, per money) = 2994000.00, 4000 × 499.00 = 1996000.00; none equals the other figure. The parts disagreed: context Medium/yes, money Low/yes, parties Low/yes, logistics Low/no. The merge keeps Low with a decision: the figures may measure different things, so no contradiction can be shown, and which figures are Valdara's is a story fact.
- Condition: The extract says what its amount and quantity measure and for which period, and figures for the same measure are the same in 12 and 13, or the difference is stated (e.g. all street furniture against benches only, capacity against output).
- Options: (a) one production capacity (benches a year) and one turnover figure for Valdara, each named in its description, the same in 12 and 13 (preferred); (b) describe the difference ("6,000 pieces of street furniture in 2025, of which 4,000 benches; sales 4.8 million lume").
- Needs decision: yes
- From: context (F4), logistics (F3), money (F1), parties (F7)

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.
- Issued 2026-02-27 16:26 (a Friday), the day after the tender opening (2026-02-26 14:00 in 02), which fits "for the evaluation"; `RequestedPublicationDate` equals the issue date; the capability's validity ends 2026-12-31, after the issue date.
- `NoticeTypeCode` BUSREG, sub-type `EXTRACT` and the note agree; `BriefDescription` ("registered, no exclusion grounds recorded") is what such an extract gives.
- Sender is the Bayvarra Information Service (register 20410959), receiver of the notices 01, 02 and 21; receiver is the department; the business party's identifiers (`XU-R-104274`, `0990:10427`, `XU-TR-104274`) and description equal those of Valdara in 03, 13, 14 and 15 apart from F10 and F11. Valdara's registration date 1962-04-12 is its own (not the 1996 default). Brackenmere is identified as in 06–09 (`20412466`).
- Capital 250000000 XUF is 2.5 million lume at the 100 : 1 rate the flow's invoice uses (2088000 XUF for 20880.00 XBL), in proportion with the figures here and in 13 (money).
- Codes: BUSREG, EXTRACT, PRODUCTION, COMPANY, LOGISTICS, SAMEACTIVITY, MANUFACTURE resolve in the world lists; en, qau; EA. Parties described as in the other examples of the flow (parties compared by script); +999 telephone numbers and `.example` addresses.

## Considered and refuted
- `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount`: 800 lume per bench is above the 350 to 600 lume the procedure allows — refuted, the capability describes Valdara's production in general, not this bench's price (from broad).
- `/BusinessInformation/cac:BusinessCapability/cac:SuppliedEvidence`: annual accounts as evidence for a production capability — refuted, the production value can be read from the accounts (from broad).
- `/BusinessInformation/cac:AdditionalNoticeLanguage`: Urvanian as additional language of a Bayvarran extract — refuted by broad (the business is Urvanian, its data bilingual); the merge keeps context's finding as F7, Low/yes, with this argument.
- `/BusinessInformation/cac:BusinessParty/cac:PartyIdentification/cbc:ID`: an Urvanian company in the Bayvarran register of economic operators — refuted, the notices name a register of economic operators in which operators of the Trade Accord countries can be entered, and the brief description says "registered"; the sender "may be … a third-Party who acts on behalf of the owner" (from broad, context, parties).
- `/BusinessInformation/cac:BusinessCapability/cac:WebSite`: duplicate of the party's `WebsiteURI` — refuted, "A web site where the capability is detailed" can be the company site (from context).
- `/BusinessInformation/cac:BrochureDocumentReference/cbc:ID` and `/BusinessInformation/cac:AdditionalDocumentReference/cbc:ID` with only an ID — refuted, the element names the brochure and the ID names the certificate (from logistics); the presence question stays F14.
- `/BusinessInformation/cbc:ID`: `BIS-DOC-26-0198` lower than numbers issued earlier by others — refuted, other senders' series (from logistics).
- `/BusinessInformation/cbc:IssueDate`: no reference to the procedure (no `ContractFolderID`) — refuted, the document type has no such element and the group type names the procedure (from logistics).
- `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount where the definition says "The number of shares in the capital stock of a corporation" — refuted, the element is of an amount type and the share capital of a subject belongs in a register extract; the definition's wording is a point for the TC write-up (from parties).
- `/BusinessInformation/cac:BusinessParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` assigned in ISO 6523 — refuted as far as own knowledge goes (the assigned ICDs are far below 0990); the ICD register was not available to check (from parties; the merge could not check it either).
- `/BusinessInformation/cac:BusinessParty/cac:Language/cbc:ID`: `qau` a real ISO 639 code — refuted, qaa–qtz is reserved for local use (from parties).
- `/BusinessInformation/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/BusinessInformation/cac:ReceiverParty/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty`: master data without use — refuted by parties and broad (a business information document describes the party as such); the merge keeps context's finding as F13, Low/yes, with this argument.
- `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[2]`: a competitor in information about Valdara — refuted by parties for its lens (both are tenderers with ISIC 3100, as the group type says); the merge keeps the finding of broad and context as F4.
- `/BusinessInformation/cac:BusinessParty/cac:PostalAddress/cbc:StreetName[2]`: Italian text tagged English, and en-XB here against en-XU in Valdara's own documents — refuted by parties (world names; the tag follows the issuer consistently); the merge made it F10 and F11, aligned with the main decisions table, with this argument.

## Refuted in the merge
### context/F9 (part) · Low · The business party's customs trader number in a register extract
- XPath: `/BusinessInformation/cac:BusinessParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- Why (context): nothing in this document is declared to customs; the number looks copied from master data. Condition: no customs trader number in a tendering document.
- Refuted because: the business party is the subject of the extract, and what a register holds about its subject (its identifiers and registrations) is the content of an extract, not copied master data. The contest merge (b) decided the same for its register extracts (13/14: "only the receiver's data"). The receiver's number stays in F8.

## Changed in the merge
- broad/F6, parties/F3 (Low) → F2 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- context/F2 (Medium) → F6 Low, with broad/F5: a value without a business reason, no contradiction.
- context/F6 (Low/no) → F7 Low/yes: broad refuted it; the merge cannot settle it.
- context/F9: the business party's line refuted in the merge (above); the receiver's line combined with parties/F4 as F8.
- F10 and F11 added from parties' refuted candidate, aligned with the main decisions table (language tags Low/yes; untagged legal form Low/no).
- context/F8 (Low/no) → F13 Low/yes: parties and broad refuted it; the merge cannot settle it.
- context/F7: the "ID only" part dropped from F14, following logistics' refutation.
- context/F4 (Medium/yes), logistics/F3 (Low/no), money/F1 (Low/yes), parties/F7 (Low/yes) → F15 Low/yes: combined; no contradiction can be shown while the measures are unnamed.

## Outside this review
- Whether the register service knows on 2026-02-27 who the tenderers are is also a question of the flow's story (from broad).
- The same capability question (6000/4800000 here, 4000/9200000 in 13) is raised in 13 from the other side.
