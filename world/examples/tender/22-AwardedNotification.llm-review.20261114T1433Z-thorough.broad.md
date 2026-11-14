# LLM review: 22-AwardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/22#F1 · Medium · Language code in LocaleCode
- XPath: `/AwardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code and names no locale. Same pattern in 213 of the 250 examples (`grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`).
- Condition: LocaleCode, where present, identifies a locale and differs in kind from Language/ID.
- Options: (a) a locale (country or language-region tag; preferred); (b) leave it out.
- Needs decision: no

### tender/22#F2 · Medium · A province in Region
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division of a country, which is CountrySubentity. A province in Region occurs in 104 examples (`grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: the province is in CountrySubentity; Region is absent or holds a geographic or economic region.
- Options: (a) move it to CountrySubentity (preferred).
- Needs decision: no

### tender/22#F3 · Low · A performance guarantee that the tendering terms never announced
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:GuaranteeTypeCode` = `PERFORMANCE`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`
- Why: the notification asks the winner for a bank guarantee of 5 % of the contract by 19 March. The contract notice and the call for tenders list one required guarantee only, the tender guarantee (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`, 2400.00), and the contract (24-TenderContract.xml) repeats that tender guarantee and does not mention a performance guarantee. A condition the tenderers could not price is first heard of after the award, and no later document shows it constituted.
- Condition: a guarantee demanded at the award is one the tendering terms announced, and the contract reflects it.
- Options: (a) announce the performance guarantee in 02 and 03 and carry it in 24 instead of the tender guarantee (preferred); (b) drop it from this notification.
- Needs decision: yes (whether the procedure has a performance guarantee)

### tender/22#F4 · Low · Master data of the receiver that the notification does not use
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- Why: the authority tells Valdara that it has won. The receiver's logistics provider, stock listing, share capital and the order desk's mobile number have no function in that message; the contact is the sales order desk ("Customer service officer"), which is the contact Valdara gave in its tender (15) but not an office that concludes a framework contract.
- Condition: the receiver is identified and addressed with what the notification needs; service providers, securities and capital appear only in documents that use them.
- Options: (a) reduce the receiver's data (preferred); (b) keep if full party data in every document is the world's rule.
- Needs decision: no

### tender/22#F5 · Low · The public works department described as a company in a commercial register
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the sender is a municipal department (ISIC 8411); it is not a company in a commercial register and has no liquidation status.
- Condition: the department's legal entity carries no liquidation status and no commercial-register type.
- Options: (a) drop the liquidation status and type the scheme as a register of public bodies (preferred); (b) drop CorporateRegistrationScheme for public bodies.
- Needs decision: no

## Checked and consistent
- The award data agree with the award notice (21): AwardID PWD-2026-PARKS-AWARD-1, award 2026-03-09 09:30, contract PWD-2026-PARKS (framework, from 2026-03-23, 24 months), both lots, 124080.00, formalization 2026-03-19 to 2026-03-22, subcontracting 3.5 % / 4320.00 = 240 × 18.00.
- 124080.00 is the total of Valdara's tender (15); "ten years of warranty on the coating" is its criterion response.
- Guarantee arithmetic: 5 % × 124080.00 = 6204.00.
- Issue time 2026-03-09 13:37 follows the award time 09:30; the contract (24) is issued 2026-03-19, inside the formalization period and ten days after the award ("after the standstill period").
- The minutes PWD-MIN-AWARD-26 are the same as in 21 and 23.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/AwardedNotification/cac:TenderResult/cbc:Description`: speaks of Valdara in the third person in a message to Valdara — refuted because it is the award decision's text, the same as in the award notice.
- `/AwardedNotification/cac:TenderResult/cac:Contract/cbc:ID`: PWD-2026-PARKS equals the folder ID — refuted here; the contract is not yet formalized, and the identifier is used consistently in 21, 23 and 26.
- `/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID`: only an ID — refuted because the identifier itself says evaluation report.
- `/AwardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: transaction-like reason on the party — refuted, the text states the party's status.

## Outside this review
- The appeal period given in 20 (2026-03-09 to 2026-03-19) ends on the day the contract is issued (24, 2026-03-19 17:24); whether the standstill had fully run is a timeline question.
- The tender guarantee in 02/03 is 2400.00 at a rate of 2 %, which is 2 % of 120000, not of the estimate 124080.00.
