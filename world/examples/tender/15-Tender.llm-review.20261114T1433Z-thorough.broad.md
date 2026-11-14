# LLM review: 15-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/15-Tender.xml`, Git blob `a052a0ed15639e25ddae372a37b1960f7b6a9857` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 1ae0e51 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/15#F1 · High · Call for tenders referenced under an ID no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The tender points to the call for tenders of the procedure as `PWD-2026-PARKS-CFT`. The call for tenders is 03-CallForTenders.xml with the ID `LPWD-DOC-26-0189`; no document of the flow has the ID `PWD-2026-PARKS-CFT`. That ID is used in 8 examples (grep over the flow's XML files: 01, 02, 03, 06, 15, 17, 19, 24), while 25-Catalogue.xml uses `LPWD-DOC-26-0189`, so the flow has two IDs for one document.
- Condition: The reference carries the ID of 03-CallForTenders.xml (or 03 carries the ID the references use).
- Options: (a) use `LPWD-DOC-26-0189` (preferred); (b) keep one procedure-level ID for the call for tenders and carry it in 03 as well.
- Needs decision: no

### tender/15#F2 · High · Valdara Industries is a large enterprise, but declares 180 employees
- XPath: `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- Why: EntitySizeCode `LARGE` means "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (50,000,000.00 XBL) in the world's list (`world/codelists/lists.json`, EntitySizeCode). In its tenderer qualification (13) Valdara declares 180 employees ("The number of people employed by this qualifying party") and a financial capability of 9 200 000.00 lume; 12 gives a production value of 4 800 000.00 lume. No figure in the flow supports a turnover above 50 million lume, so by the figures it gives the company is medium-sized.
- Condition: Size class, number of employees and the financial figures of Valdara Industries agree.
- Options: (a) at least 250 employees in 13 (preferred: a listed company with a share capital of 250 million ferra and its own foundry is plausibly large); (b) size `MEDIUM` wherever the party is described.
- Needs decision: no

### tender/15#F3 · Medium · The tender price is given as the response to the quality criterion; the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `124080.00`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `10`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- Why: Amount in an AwardingCriterionResponse "Specifies the monetary amount tendered for this awarding criterion". The response is to `AC-2`, the quality criterion of the call for tenders (scored on 5 to 10 years); the quantity of 10 years answers it. The amount 124 080.00 is the tender price, which is what the price criterion `AC-1` (weight 60) scores; there is no response to `AC-1`.
- Condition: Each response carries what its criterion scores: the price under AC-1, the years under AC-2.
- Options: (a) a response to `AC-1` with the amount, and no amount under `AC-2` (preferred); (b) drop the amount (the price is in the monetary total).
- Needs decision: no

### tender/15#F4 · Medium · A province in Region
- XPath: `/Tender/cac:TendererParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, for which CountrySubentity exists ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the flow do use CountrySubentity for their state. The same value is in 22 of the 36 examples of the flow (grep for `Province of Ferrano` over the `*.xml` of the flow, files counted).
- Condition: The province is in CountrySubentity (with its code where the country has one); Region is used only for a region that is not an administrative division.
- Options: (a) move the province to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/15#F5 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:SubcontractorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/15#F6 · Low · The tender equals the buyer's estimate to the cent
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- Why: The buyer's estimate, published a month before, is 119 760.00 for the benches (499 a bench) and 4 320.00 for the installation (18 a bench). Valdara tenders exactly these amounts on both lines. In a competition with a price criterion (and an auction to follow) a tender that hits the estimate on both lots to the cent is not plausible; it reads as if the estimate had been taken from the tender.
- Condition: Estimate and tender are independent figures (the estimate rounded, the tender within the allowed 350 to 600 a bench).
- Options: (a) a rounded estimate in 01 to 03 (e.g. 125 000) (preferred: later documents build on the tender price); (b) another tender price.
- Needs decision: yes

### tender/15#F7 · Low · The tenderer's own costs as fees of the tendered project
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: FeeAmount is "The fee amount for tendered projects", AdditionalFee "An additional fee for this tendered project": fees that are part of what is tendered. The 50 lume are what the tenderer paid the department for a paper copy of the documents (in a procedure whose documents are free electronically and whose tenders are electronic), and the 12 lume its courier cost for the guarantee. Neither is offered to or charged to the buyer; they are not in the monetary total. They tell the contracting authority nothing it acts on.
- Condition: The tendered project carries fees only if they are part of the offer.
- Options: (a) remove both (preferred); (b) if the documentation fee is to be evidenced, refer to its receipt.
- Needs decision: no

### tender/15#F8 · Low · A replacement item with an ID only
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- Why: ReplacementRelatedItem is "A catalogue item that may be a replacement for the item described in this tender line." The tender names `VI-C180-2026` without a description; the buyer cannot tell what would replace the specified bench, or whether it is the variant the call for tenders allows (recycled plastic slats, one variant at most). The ID occurs elsewhere only in retail/02-Catalogue.xml, again as a replacement item with an ID and a quantity only (grep over `world/examples/*/*.xml`).
- Condition: The replacement item is described, or offered as a variant, or absent.
- Options: (a) add a description (preferred); (b) remove it.
- Needs decision: no

### tender/15#F9 · Low · The subcontractor has 20 % in the qualification and 3.5 % of the tender
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- Why: The tender names Saltmere Engineering as subcontractor; by the qualification 13 it does the installation. The installation line is 4 320.00 of 124 080.00 lume, 3.5 %; the qualification this tender refers to gives Saltmere a participation of 20 %.
- Condition: The shares declared in the qualification agree with the split of the tender.
- Options: (a) about 3.5 % in 13 (preferred); (b) show in the tender what else Saltmere does.
- Needs decision: no

### tender/15#F10 · Low · Bids office of the subcontractor staffed by a procurement officer
- XPath: `/Tender/cac:SubcontractorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Tender/cac:SubcontractorParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/Tender/cac:SubcontractorParty/cac:Contact/cbc:Department` = `Procurement`
- Why: A bids office prepares offers to customers; "Procurement officer" in a department "Procurement" is someone who buys. Name, job title and department of the contact do not agree, and for a subcontractor taking part in a tender the selling side is the one that fits.
- Condition: Name, job title and department of the contact agree and fit the role.
- Options: (a) e.g. "Bid manager", department "Sales" or "Bids" (preferred); (b) drop job title and department.
- Needs decision: no

### tender/15#F11 · Low · The logistics service provider of the tenderer copied into the document
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The tenderer carries its logistics service provider (Castrano Logistics, warehousing and despatch, with a key account desk). The tender offers benches and their installation and names Saltmere as subcontractor; nothing in it concerns warehousing or despatch by a third party. The data looks copied from master data (review rules, section 4.8).
- Condition: The party carries a service provider only where the document relies on it.
- Options: (a) remove the service provider here (preferred); (b) if the document is to rely on Castrano, say for what.
- Needs decision: no

### tender/15#F12 · Low · A public body described as a company in a commercial register
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/15#F13 · Low · The department's tax exemption reason describes a sale
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- Arithmetic: 119 760.00 / 240 = 499.00 a bench, within the allowed 350.00 to 600.00; 4 320.00 / 240 = 18.00; 119 760.00 + 4 320.00 = 124 080.00 = LineExtensionAmount = PayableAmount; tax 0.00 (sale to a public body, exempt), so the tax-inclusive line amount equals the line amount.
- Ordering: pallet of 4, increment 4, minimum 20 and maximum 96 are multiples of 4; an average release of 40 benches (240 / 6) lies between them.
- Against the call for tenders: quantity 240 EA and 240 anchor sets, line reference 1, envelope `ENV-1` of type COMBINED, validity 90 days, warranty 5 years (required 5), lead time 7 days (required at most 10), quality response 10 years within the 5 to 10 scored, sub-response to `AC-2.1`.
- TendererQualificationDocumentReference `VI-DOC-26-0199` is 13-TendererQualification.xml, issued 21 minutes earlier; the subcontractor is the one declared there. The tender (2026-02-25 09:13) is before the deadline 2026-02-26 12:00; 16 acknowledges it by its ID.
- Warranty party is the tenderer itself.

## Considered and refuted
- `/Tender/cac:OriginatorCustomerParty`: "The party originating the Tender" is given as the department, not the tenderer — refuted because Customer Party in this role is the customer for whom the tendering was started, as in the notices.
- `/Tender/cac:DocumentReference`: the tender does not refer to the guarantee certificate `BL-DOC-26-0200` — refuted because the bank sends the certificate to the beneficiary itself and the tender model has no dedicated reference; the data sheet `VI-DS-B180` it does reference is the product documentation used again in 25 to 33.
- `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]`: one tendered project for both lots instead of one per lot — refuted because the definition allows "one project, multiple projects, or the global project", and the lines keep the lots apart.
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation`: "Five years on the frame" against "Ten years on the coating" — refuted because they are warranties on different parts.
- `/Tender/cbc:Note[1]`: the Urvanian note cannot be checked against the English one — refuted as a finding, the language being invented.
