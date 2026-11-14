# LLM review: 16-TenderReceipt.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/16-TenderReceipt.xml`, Git blob `358439bdf09247da5f2bd664dc2d3fc8e35e72b0` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit e0e5001 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/16#F1 · High · Valdara Industries is a large enterprise, but declares 180 employees
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- Why: EntitySizeCode `LARGE` means "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (50,000,000.00 XBL) in the world's list (`world/codelists/lists.json`, EntitySizeCode). In its tenderer qualification (13) Valdara declares 180 employees ("The number of people employed by this qualifying party") and a financial capability of 9 200 000.00 lume; 12 gives a production value of 4 800 000.00 lume. No figure in the flow supports a turnover above 50 million lume, so by the figures it gives the company is medium-sized.
- Condition: Size class, number of employees and the financial figures of Valdara Industries agree.
- Options: (a) at least 250 employees in 13 (preferred: a listed company with a share capital of 250 million ferra and its own foundry is plausibly large); (b) size `MEDIUM` wherever the party is described.
- Needs decision: no

### tender/16#F2 · Medium · A province in Region
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, for which CountrySubentity exists ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the flow do use CountrySubentity for their state. The same value is in 22 of the 36 examples of the flow (grep for `Province of Ferrano` over the `*.xml` of the flow, files counted).
- Condition: The province is in CountrySubentity (with its code where the country has one); Region is used only for a region that is not an administrative division.
- Options: (a) move the province to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/16#F3 · Medium · Language code in LocaleCode
- XPath: `/TenderReceipt/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/16#F4 · Low · The receipt was created at 11:42 and issued at 17:47
- XPath: `/TenderReceipt/cbc:RegisteredTime` = `11:42:00`
- XPath: `/TenderReceipt/cbc:RegisteredDate` = `2026-02-25`
- XPath: `/TenderReceipt/cbc:IssueTime` = `17:47:00`
- XPath: `15-Tender.xml:/Tender/cbc:IssueTime` = `09:13:00`
- Why: RegisteredTime is "The time, assigned by the sender, at which the Tender Receipt was created", IssueTime the time the document was issued. A platform that registers a tender creates and issues its receipt at once; here six hours lie between the two. If 11:42 is meant as the time the tender was registered (it was issued at 09:13), that is not what the element's definition says, and then two and a half hours pass between submission and registration of an electronic tender.
- Condition: Registered time and issue time of the receipt agree, or the note says what each time is.
- Options: (a) issue the receipt at the registered time, shortly after the tender (preferred); (b) keep both and explain in the note.
- Needs decision: no

### tender/16#F5 · Low · Master data of Valdara Industries that this document does nothing with
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- Why: The receiver of the receipt is described with its logistics service provider (Castrano Logistics, warehousing and despatch, with a key account desk), its share capital and its stock exchange listing. A tender receipt acknowledges that a tender was received. Nothing in it concerns warehousing, despatch or listed shares; the data looks copied from the party's master data (section 4.8 of the review rules: data copied into a document that does not use it).
- Condition: The party carries only what this document uses or what identifies it.
- Options: (a) remove the service provider, the security listing and the stock amount here (preferred); (b) keep them only in the documents where they matter (despatch, business information).
- Needs decision: no

### tender/16#F6 · Low · A public body described as a company in a commercial register
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/16#F7 · Low · The department's tax exemption reason describes a sale
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TenderReceipt/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- TenderDocumentReference `VI-DOC-26-0201` is the ID of 15-Tender.xml, issued 2026-02-25 09:13; the receipt is of the same day, before the deadline 2026-02-26 12:00, in line with "Received on time".
- "encrypted, unopened until the opening" agrees with the encryption data of the tendering terms and the opening event of 2026-02-26 14:00 in 02 and 03.
- Sender is the department (the tender recipient party of the notices), receiver the tenderer; folder and contract name are the procedure's.

## Considered and refuted
- `/TenderReceipt/cac:ReceiverParty/cac:Contact/cbc:Name`: the receipt goes to Valdara's order desk — refuted here because a receipt only needs to arrive; the unfitting contact is a finding of 03, where the call for tenders is addressed to it.

## Outside this review
- No tender receipt exists for the tenders of Brackenmere Furniture (17, 19), although 18 refers to one (`PWD-RCPT-BF-1`); see the review of 18.
