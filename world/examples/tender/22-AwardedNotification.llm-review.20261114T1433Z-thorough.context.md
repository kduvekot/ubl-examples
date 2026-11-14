# LLM review: 22-AwardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/22-AwardedNotification.xml`, Git blob `06273957bdbccc6b43bc0afefe91af957c32f85c` (committed)
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

### tender/22#F1 · Medium · A province in `Region`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/22#F2 · Medium · A language code as locale
- XPath: `/AwardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/22#F3 · Low · A performance guarantee that neither the call for tenders nor the contract knows
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:GuaranteeTypeCode` = `PERFORMANCE`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`
- Why: `FinalFinancialGuarantee` is "A bond guarantee by the submitter of a tender or bid, required of the tender winner". The notification asks the winner for a performance guarantee of 5 % (6204.00) by 2026-03-19. The tendering terms of the call for tenders announce only a tender guarantee (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`, 2400.00), and no document after this one mentions the performance guarantee: not the contract (`24-TenderContract.xml` has no element or text with it; searched "PERFORMANCE" in `world/examples/tender/*.xml`: only this example) and no guarantee certificate (`14-GuaranteeCertificate.xml` is the tender guarantee). A condition of the award that tenderers could not know when pricing their tender, and that the contract does not record, has no footing in the flow.
- Condition: A guarantee required of the winner is announced in the tendering terms of the procedure and is reflected where the contract is formalized, or it is not required.
- Options: (a) preferred: announce the performance guarantee in the call for tenders (and the notices that repeat its terms) and refer to it in the contract; (b) remove it from the notification.
- Needs decision: yes (adds a requirement, and possibly a document, to the flow)

### tender/22#F4 · Low · The contract may be formalized on the last day of the appeal period
- XPath: `/AwardedNotification/cbc:Note` = `Your tender has won both lots. The contract follows after the standstill period.`
- XPath: `/AwardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- Why: The note promises the contract after the standstill period. The only period of the flow that can be meant is the period for appeals against this award, which the notification to the unsuccessful tenderer gives as ending on 2026-03-19 (`23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`). The formalization period starts on that same day, and the contract is in fact issued on it (`24-TenderContract.xml:/TenderContract/cbc:IssueDate` = `2026-03-19`), while an appeal could still be presented. The notification itself does not say when the standstill ends.
- Condition: The formalization period starts after the last day on which an appeal can be presented, and the notification's dates make "after the standstill period" checkable.
- Options: (a) preferred: start the formalization (and issue the contract) on 2026-03-20 or later; (b) end the appeal period on 2026-03-18 in the documents that state it.
- Needs decision: no

### tender/22#F5 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/22#F6 · Low · Master data of a party that the document does not use
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The notification tells the receiver that it won; its own share capital, listing and logistics provider play no part in that (the subcontractor that does matter, Saltmere Engineering, is named in the subcontract terms). Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py`: ISIN XU0001042501 has a correct check digit.
- Tender result identical to the award notice (`21-ContractAwardNotice.xml`): award `PWD-2026-PARKS-AWARD-1` of 2026-03-09 09:30, both lots, 124080.00 = total of `15-Tender.xml`; the notification is issued the same day at 13:37, after the award.
- Receiver = winning party (Valdara Industries, rank 1); sender = contracting party; signature by the sender.
- Guarantee arithmetic: 5 % of 124080.00 = 6204.00; its constitution ends when formalization starts.
- Subcontract terms: 240 × 18.00 = 4320.00 = 3.48 % of 124080.00 (rate 3.5), `UnknownPriceIndicator` false with an amount.
- Contract: framework, valid from 2026-03-23 for 24 months, as in the award notice and the contract.

## Considered and refuted
- `/AwardedNotification/cac:TenderResult/cac:SubcontractTerms`: subcontract terms told to the party that offered them — refuted because the award is made on these terms and the contracting party confirms what it accepted.
- `/AwardedNotification/cac:TenderResult/cac:WinningParty`: repeats the receiver — refuted because the tender result is a self-contained statement of the award and the element is its core.
- `/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cbc:VariantID`: `V0` — refuted because the call for tenders allows a variant and the award says which offer won.
- `/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID`: an evaluation report that is no example — refuted for this lens: a non-UBL annex, as the element allows.

## Outside this review
- The receiver's contact (order desk, sales) against the role of a tenderer receiving an award, and the sender's tax exemption reason worded as a transaction: parties part.
