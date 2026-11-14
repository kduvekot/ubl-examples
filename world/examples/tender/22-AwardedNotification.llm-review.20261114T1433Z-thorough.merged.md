# LLM review: 22-AwardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/22-AwardedNotification.xml`, Git blob `06273957bdbccc6b43bc0afefe91af957c32f85c` (committed)
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

### tender/22#F1 · Medium · Language code in LocaleCode
- XPath: `/AwardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID` and names no locale. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred by parties and context); (b) a locale such as `en-XB` from a locale list (preferred by broad).
- Needs decision: no
- From: broad, parties, context

### tender/22#F2 · Medium · Province in Region
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the administrative division `CountrySubentity` holds, as the Bayvarran addresses do. 219 occurrences in 104 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: The province is in `CountrySubentity`; `Region` is absent or holds a region in its sense.
- Options: (a) move it to `CountrySubentity` (preferred).
- Needs decision: no
- From: broad, parties, context

### tender/22#F3 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The sender is a city department (ISIC 8411). A liquidation status has no meaning for it and a scheme of type `COMMERCIAL` ("A register of businesses") does not fit; the register number itself is not questioned.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type (preferred); (b) reduce the legal entity to registration name and identifier.
- Needs decision: no
- From: broad, parties, context

### tender/22#F4 · Low · A performance guarantee that neither the call for tenders nor the contract knows
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:GuaranteeTypeCode` = `PERFORMANCE`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:AmountRate` = `5`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`
- Why: `FinalFinancialGuarantee` is "A bond guarantee by the submitter of a tender or bid, required of the tender winner". The notification asks for a performance guarantee of 5 % (recalculated: 0.05 × 124 080.00 = 6 204.00) by 2026-03-19. The tendering terms announce only the tender guarantee (2400.00), so a cost the tenderers could not price appears after the tenders were binding; and nothing later takes it up: the contract signed on the due date (24) carries the tender guarantee (`GuaranteeTypeCode` TENDER) and no performance guarantee, and the only certificate (14) is the tender guarantee (`PERFORMANCE` occurs only in this example). Not High: no document says there is no performance guarantee; it is unsupported, not contradicted.
- Condition: A guarantee required of the winner is announced in the tendering terms and reflected in the contract, or it is not required.
- Options: (a) announce the 5 % performance guarantee in the notices and the call and let the contract carry it instead of the tender guarantee (preferred by all parts); (b) remove it from the notification.
- Needs decision: yes
- From: broad, money, context; logistics listed it under "Outside this review"

### tender/22#F5 · Low · The contract may be formalised on the last day of the appeal period, although it "follows after the standstill period"
- XPath: `/AwardedNotification/cbc:Note` = `Your tender has won both lots. The contract follows after the standstill period.`
- XPath: `/AwardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- XPath: `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `24-TenderContract.xml:/TenderContract/cbc:IssueDate` = `2026-03-19`
- Why: The only standstill the flow states is the appeal period of the unsuccessful tenderer, which runs to and including 2026-03-19. The formalisation period starts that same day, the performance guarantee is due then, and the contract is in fact issued on it (24), while an appeal could still be presented. The notification itself does not say when the standstill ends.
- Condition: The formalisation period starts after the last day on which an appeal can be presented, and the notification's dates make "after the standstill period" checkable.
- Options: (a) formalisation (and the contract) from 2026-03-20 (preferred); (b) end the appeal period on 2026-03-18 in the documents that state it.
- Needs decision: no
- From: logistics (needs decision yes), context; broad listed it under "Outside this review"

### tender/22#F6 · Low · The department's document numbers do not follow the issue times
- XPath: `/AwardedNotification/cbc:ID` = `LPWD-DOC-26-0208`
- XPath: `/AwardedNotification/cbc:IssueTime` = `13:37:00`
- XPath: `23-UnawardedNotification.xml:/UnawardedNotification/cbc:ID` = `LPWD-DOC-26-0209`
- XPath: `23-UnawardedNotification.xml:/UnawardedNotification/cbc:IssueTime` = `10:15:00`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cbc:ID` = `LPWD-DOC-26-0207`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cbc:IssueDate` = `2026-03-13`
- Why: The department's documents carry one running number. This notification (…0208, 2026-03-09 13:37) is issued after …0209 (23, the same day at 10:15) and four days before …0207 (21). A number assigned at issue rises with the issue time; and the loser learning the result before the winner is odd in itself. The same is part of 21#F12.
- Condition: Within the department's series, a higher number is not issued before a lower one.
- Options: (a) winner's notification first, then the loser's, then the award notice, numbered in that order (preferred); (b) state that numbers are reserved per procedure step.
- Needs decision: no
- From: logistics

### tender/22#F7 · Low · The "precise percentage" subcontracted is rounded and does not give the amount
- XPath: `/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted". Recalculated: 4 320.00 / 124 080.00 = 3.4816 %; 3.5 % of 124 080.00 is 4 342.80. The amount is right (240 × 18, line 2 of 15). Same as 21#F15, where broad and context refuted it as rounding and a legitimate reading in a result.
- Condition: `Rate` × awarded amount / 100 equals `Amount`, or the rate is absent.
- Options: (a) drop `Rate` (preferred); (b) more decimals.
- Needs decision: no
- From: money

### tender/22#F8 · Low · Master data of the receiver that the notification does not use, and its order desk as contact
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/AwardedNotification/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The department tells Valdara it has won. Its logistics provider (with a key account desk without any means of contact), share capital, listing, the order desk's mobile and the customs trader numbers have no function in that message (section 4.8); the subcontractor that matters is named in the subcontract terms. The contact is the sales order desk, the contact Valdara gave in its tender (15) but not an office that concludes a framework contract. Counter-arguments (parties, refuted): share capital and listing describe the party as a legal entity; the order desk is the contact Valdara gave. Kept, as in 16, 20 and 21.
- Condition: The receiver carries what the notification needs; service providers, securities, capital and customs numbers appear only in documents that use them.
- Options: (a) reduce the receiver's data and give Valdara a tender contact (preferred); (b) keep the full data everywhere and record that as a world rule.
- Needs decision: no
- From: broad, parties (service provider only), context; customs trader numbers added by the merge

### tender/22#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax": the party's status; the text begins with a transaction. Counter-argument (broad, refuted): the text states the status. Kept as in 15–21; the code fits (list description: a public body "buys free of sales tax"). A notification without tax content also does not need the tax scheme.
- Condition: The party's exemption reason states its status only.
- Options: (a) reword the text, keeping the code (preferred); (b) a party-status code; (c) leave the tax scheme out here.
- Needs decision: no
- From: parties (broad refuted it; context listed it under "Outside this review")

### tender/22#F10 · Low · Italian text tagged English, and en-XB here against en-XU in Valdara's own documents
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same text is tagged `en-XB` here and `en-XU` in Valdara's documents (13); the tag follows the issuer's country, not the text, and the text is Italian. No convention is stated (parties could not settle it); aligned with the earlier flows (Low, decision).
- Condition: One recorded rule for these renderings and their tags, applied in every example.
- Options: (a) tag by what the text is (`en-XU`) everywhere (preferred by parties); (b) keep the issuer-dependent tag and record the rule.
- Needs decision: yes
- From: parties

### tender/22#F11 · Low · Valdara's legal form in one untagged rendering
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`
- Why: The legal form occurs once without `languageID`, while the address is in both languages, tagged, and Valdara's documents give the legal form twice (13). Split from parties/F5.
- Condition: The legal form is rendered like the address (both renderings, tagged).
- Options: (a) both renderings, tagged (preferred); (b) at least tag the single rendering.
- Needs decision: no
- From: parties

### tender/22#F12 · Low · Additional document reference with only an ID
- XPath: `/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID` = `PWD-EVAL-REPORT-26`
- Why: "A reference to an additional document associated with this document." Nothing says what the document is (no type, description or date), and it is not in the flow (only this example). Counter-arguments: the identifier itself says evaluation report (broad); a non-UBL annex, as the element allows (context, which addressed only that it is not an example). Kept as the earlier flows' decision on ID-only references.
- Condition: The reference states what it refers to.
- Options: (a) add `cbc:DocumentType` "Evaluation report" (preferred).
- Needs decision: no
- From: logistics (broad refuted it)

## Checked and consistent
- The award data agree with 21: award `PWD-2026-PARKS-AWARD-1` of 2026-03-09 09:30, both lots, 124 080.00 = total of 15, contract `PWD-2026-PARKS` (framework, from 2026-03-23, 24 months, to 2028-03-22), formalisation 2026-03-19 to 2026-03-22, subcontract 4 320.00 = 240 × 18.00; minutes `PWD-MIN-AWARD-26` as in 21 and 23; "ten years of warranty on the coating" is 15's criterion response.
- Issue 2026-03-09 13:37 after the award; the qualification (20) precedes it; the tender (2026-02-25, valid 90 days) is still valid; the first order (26) falls on the first day of the contract.
- Sender is the contracting department (signs), receiver and winning party Valdara, rank 1; codes AWARDED, FRAMEWORK, PERFORMANCE are in their lists.
- Parties identical to the other examples of the flow apart from tags and legal-form renderings (parties, by script); ISIN `XU0001042501` check digit correct.

## Considered and refuted
- `/AwardedNotification/cac:TenderResult/cbc:Description`: speaks of Valdara in the third person in a message to Valdara — refuted, the award decision's text (from broad).
- `/AwardedNotification/cac:TenderResult/cac:Contract/cbc:ID`: equals the folder ID — refuted, numbering the contract like the file is allowed and used consistently (from broad, logistics; `PWD-CONTRACT-2026-PARKS` in 24 is a finding there).
- `/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID`: only an ID — refuted, the identifier says evaluation report (from broad; and as a non-UBL annex, from context; the merge keeps F12).
- `/AwardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: transaction-like — refuted, the text states the status (from broad; the merge keeps F9).
- `/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: a framework guarantees no fixed total — refuted, it is the awarded tender's total for the stated 240 benches (from money).
- `/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate`: due ten days after the award — refuted, short but possible and before the contract's start (from money).
- `/AwardedNotification/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` malformed — refuted (from parties).
- `/AwardedNotification/cac:SenderParty/cac:Contact/cbc:Telephone`: +999 real — refuted, unassigned (from parties).
- `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: master data not used — refuted for the parties lens (from parties; the merge keeps it in F8).
- `/AwardedNotification/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD 0990 real — refuted from knowledge of the ICD list (from parties).
- `/AwardedNotification/cac:ReceiverParty/cac:Contact/cbc:Name`: unsuitable contact — refuted, the contact Valdara gave (from parties; the merge keeps it in F8).
- `/AwardedNotification`: no reference to the winning tender — refuted, the document type has no element for it (from logistics).
- `/AwardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:EndDate`: a day before the contract starts — refuted, consistent (from logistics).
- `/AwardedNotification/cac:TenderResult/cac:SubcontractTerms`: told to the party that offered them — refuted, the award is made on them (from context).
- `/AwardedNotification/cac:TenderResult/cac:WinningParty`: repeats the receiver — refuted, the core of a self-contained tender result (from context).
- `/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cbc:VariantID`: `V0` — refuted, says which offer won (from context).

## Changed in the merge
- broad/F5, parties/F4, context/F5 → F3: raised to Medium, as analysis/review-merge-decisions.md and the other tender merges.
- logistics/F2 (needs decision yes), context/F4 (no) → F5: no; moving a date by a day is encoding.
- broad/F4, parties/F6, context/F6 → F8: one master-data finding with the contact; customs trader numbers added by the merge.
- parties/F5 split into F10 (tags, Low/yes) and F11 (untagged legal form, Low/no).

## Outside this review
- The tender guarantee in 02/03 is 2400.00 at a rate of 2 %, which matches no stated base (from broad; a finding of 02/03).
- The auction announced in the call leaves no trace; see 21#F13 (from logistics).
