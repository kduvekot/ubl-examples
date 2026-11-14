# LLM review: 16-TenderReceipt.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/16-TenderReceipt.xml`, Git blob `358439bdf09247da5f2bd664dc2d3fc8e35e72b0` (committed)
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

### tender/16#F1 · Medium · Language code in LocaleCode
- XPath: `/TenderReceipt/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with `listID="ISO 639"` repeats the language code of the sibling `cbc:ID`; it names no locale. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales named in `listID`.
- Options: (a) remove `cbc:LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad, parties, logistics, context

### tender/16#F2 · Medium · Province in Region
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country" that `cbc:CountrySubentity` holds. The Bayvarran addresses of the flow use `CountrySubentity` for their state. 219 occurrences in 104 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: The province is in `cbc:CountrySubentity`; `cbc:Region` is absent or holds a region in the sense of its definition.
- Options: (a) move the value to `cbc:CountrySubentity` (preferred).
- Needs decision: no
- From: broad, parties

### tender/16#F3 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The Lumeport Public Works Department, a department of the city (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411), is described with a liquidation status `ACTIVE` ("Active, not in liquidation") and a registration scheme of type `COMMERCIAL` ("Commercial register: A register of businesses"). A city department is not a business and cannot be in liquidation. The same description is used in all 36 examples of the flow.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop `CompanyLiquidationStatusCode` and the `COMMERCIAL` type for public bodies, keeping register name and ID (preferred); (b) a register type for public bodies (needs a code); (c) state in the world's rules that public bodies are entered in the federal business register.
- Needs decision: no
- From: broad, parties

### tender/16#F4 · Low · Master data the receipt does not use
- XPath: `/TenderReceipt/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Section 4.8: data copied from master data into a document that does nothing with it. A tender receipt acknowledges that a tender arrived. The customs trader numbers identify the parties towards customs (used in 30, 31); Castrano Logistics, Valdara's warehousing and despatch provider with its key account desk, acts only in 29; share capital and stock exchange listing play no part in an acknowledgement.
- Condition: Each party carries only what identifies it or what the receipt uses.
- Options: (a) remove these here (preferred); (b) keep them only in documents where they matter (customs, despatch, business information).
- Needs decision: no
- From: broad, parties, context

### tender/16#F5 · Low · Large enterprise with 180 employees
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: `LARGE` is "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL or 5,000,000,000 XUF). Valdara declares 180 employees and a financial capability of 9 200 000.00 lume (13); its production capability is 4 800 000.00 lume (12). Nothing in the flow supports a turnover above the limit, but none is stated as such, so the contradiction is not strict.
- Condition: The size class of Valdara agrees with the employees and financial figures stated for it in the flow.
- Options: (a) 250 or more employees in 13 if Valdara is meant to be a large listed company; (b) `MEDIUM` wherever Valdara is described.
- Needs decision: yes
- From: broad (High), parties (Low)

### tender/16#F6 · Low · The receipt is "created" at 11:42 and issued at 17:47; the time of receipt of the tender is not stated as such
- XPath: `/TenderReceipt/cbc:RegisteredDate` = `2026-02-25`
- XPath: `/TenderReceipt/cbc:RegisteredTime` = `11:42:00`
- XPath: `/TenderReceipt/cbc:IssueTime` = `17:47:00`
- XPath: `15-Tender.xml:/Tender/cbc:IssueTime` = `09:13:00`
- Why: `RegisteredTime` is "The time, assigned by the sender, at which the Tender Receipt was created"; `IssueTime` the time the document was issued. By the definitions the receipt was created at 11:42 and issued six hours later. 11:42 reads as the time the tender (issued 09:13) was registered on the platform, which is what a tenderer wants confirmed, but that is not what the element says, and the document does not state the time of receipt. Counter-argument (logistics, refuted): creation before issue is consistent, and both are after the tender and before the deadline, so nothing contradicts. The merge keeps it as Low: for an acknowledgement meant to prove timely receipt, which time is the receipt is not clear.
- Condition: Registered and issue time agree with their definitions, and the time at which the tender was received is stated unambiguously.
- Options: (a) registered and issue time a few moments apart (an automatic receipt), and the time of receipt in the note (preferred); (b) keep 11:42 as the time of receipt and say so in the note, recording the reading as a difference from the definition.
- Needs decision: no
- From: broad, context (logistics refuted it)

### tender/16#F7 · Low · Valdara's contact is the order desk
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- Why: The receiver is the tenderer whose tender is acknowledged; its contact is the order desk (`order@…`) with a customer service officer, the function that takes purchase orders (right in 26–28), not the one that submitted the tender. Counter-argument (broad, refuted): a receipt only needs to arrive, and the unfitting contact is a finding of 03, where the call is addressed to it. The merge keeps it, as earlier flows did for every document: the contact the receipt names is the one who answers for the tender.
- Condition: Valdara's contact in the tendering documents is a function that handles tenders, or is left out.
- Options: (a) a bid or tender contact for Valdara (preferred); (b) leave the contact out here.
- Needs decision: no
- From: parties (broad refuted it)

### tender/16#F8 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax, expressed as text": the party's own status. "Sale to a public body" describes a transaction. The code `PUBLIC` fits (its list description "A body of the federation, a state or a city buys free of sales tax" is a buyer status); broad would prefer a separate party-status code.
- Condition: The party's exemption reason states the party's status, not a kind of sale.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a party-status code.
- Needs decision: no
- From: broad, parties

### tender/16#F9 · Low · Italian street name tagged English, and en-XB here against en-XU in Valdara's own documents
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `15-Tender.xml:/Tender/cac:TendererParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The rendering is Italian but tagged `en-XB` here, `en-XU` in the documents Valdara issues (15). Parties refuted both: the world's English names of Urvanian places are accepted as given, and the tag follows the issuer's locale consistently. No such convention is stated; the earlier flows kept the question as Low with a decision (analysis/review-merge-decisions.md), and the merge aligns.
- Condition: One recorded rule for these renderings and their tags.
- Options: (a) record the convention (English exonyms as given; tag by issuer) in the story (preferred); (b) the party's own variety (`en-XU`) everywhere.
- Needs decision: yes
- From: merge (parties considered and refuted it)

### tender/16#F10 · Low · Valdara's legal form in one untagged rendering
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `15-Tender.xml:/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`
- Why: Here the legal form has one rendering without `languageID`, while the address next to it is given in Urvanian and English, both tagged, and Valdara's own documents give the legal form in both languages, tagged (15). Parties noted the difference and refuted it as the issuer's convention.
- Condition: The legal form is rendered like the address (both renderings, tagged), or the single rendering carries its language.
- Options: (a) both renderings, tagged (preferred, as the earlier flows); (b) tag the single rendering.
- Needs decision: no
- From: merge (parties considered and refuted it)

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- `TenderDocumentReference` `VI-DOC-26-0201` is 15-Tender.xml, Valdara's tender, issued 2026-02-25 09:13; tender < registration (11:42) < issue (17:47), all before the deadline 2026-02-26 12:00: "Received on time" holds.
- "encrypted, unopened until the opening" agrees with the encryption data and the opening event of 2026-02-26 14:00 in 02 and 03.
- Sender is the department (the tender recipient of the notices), receiver the tenderer, signatory the sender; folder and contract name are the tender's; `LPWD-DOC-26-0202` follows the department's `-0197` (2026-02-23).
- Parties identical, element by element, to the same parties in the other examples, apart from the findings (parties, by script); telephone code +999 unassigned; addresses in `.example`; ISIC 3100 and 8411 fit.

## Considered and refuted
- `/TenderReceipt/cac:ReceiverParty/cac:Contact/cbc:Name`: the receipt goes to Valdara's order desk — refuted because a receipt only needs to arrive (from broad; the merge disagrees, see F7).
- `/TenderReceipt/cbc:RegisteredTime`: created six hours before issue — refuted, creation before issue is consistent (from logistics; the merge keeps it as F6).
- `/TenderReceipt/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` not valid — refuted, no format prescribed (from parties).
- `/TenderReceipt/cac:SenderParty/cac:PostalAddress/cbc:InhouseMail`: `Room 2.14` belongs in `Room` — refuted, a mail location in a building (from parties).
- `/TenderReceipt/cac:ReceiverParty`: one named receiver for a call others answer too — refuted, this is the copy sent to Valdara (from parties).
- `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: Italian text tagged English, en-XB vs en-XU — refuted as world names and an issuer-locale rule (from parties; the merge carries it as F9 and F10 to align with earlier flows).
- `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: amount against "number of shares" — refuted as a matter of the model (from parties; the presence of the value is in F4).
- `/TenderReceipt/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` assigned — refuted as far as own knowledge goes (from parties).
- `/TenderReceipt/cac:ReceiverParty/cac:Language/cbc:ID`: `qau` a real code — refuted, reserved range (from parties).
- `/TenderReceipt/cac:TenderDocumentReference/cbc:ID`: Brackenmere's tenders have no receipt while 18 cites one — not a finding of this example; see 18 (from logistics).
- `/TenderReceipt/cbc:Note`: "unopened until the opening" says more than a receipt can know — refuted, the department's own commitment (from context).

## Changed in the merge
- broad/F6, parties/F5 → F3: raised from Low to Medium (public bodies as companies), as analysis/review-merge-decisions.md and the other tender merges.
- broad/F1 (High/no), parties/F6 (Low/yes) → F5: Low/yes; the LARGE definition is an "or" and no turnover is stated.
- broad/F5, parties/F3, context/F3, F4 → F4: one copied-master-data finding.
- F9, F10 added from a candidate parties refuted, to align with the earlier flows (Italian text tagged English: Low/yes; untagged single legal form: Low/no).

## Outside this review
- No tender receipt exists for Brackenmere's tenders (17, 19), although 18 cites one (`PWD-RCPT-BF-1`); see the review of 18 (from broad, logistics, context).
