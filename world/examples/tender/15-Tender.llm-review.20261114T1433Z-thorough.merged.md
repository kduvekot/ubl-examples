# LLM review: 15-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/15-Tender.xml`, Git blob `a052a0ed15639e25ddae372a37b1960f7b6a9857` (committed)
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

### tender/15#F1 · High · Call for tenders referenced under an ID that no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTenderDocumentReference` is "A reference to the call for tender document of which this tender result of". The call for tenders of the procedure, addressed to this tenderer, is 03-CallForTenders.xml with the ID `LPWD-DOC-26-0189`; no example of the flow has the document ID `PWD-2026-PARKS-CFT`, and Valdara itself cites the call by `LPWD-DOC-26-0189` in its catalogue (25). The line reference `1` exists in 03, but hangs on a document ID that does not resolve. Re-checked in the merge: `PWD-2026-PARKS-CFT` occurs in 8 files of the flow (`grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`: 01, 02, 03, 06, 15, 17, 19, 24); the folder ID `PWD-2026-PARKS` does not make it a document ID.
- Condition: Every reference to the call for tenders carries the document ID of 03-CallForTenders.xml (or 03 carries the ID the references use), one ID in the whole flow.
- Options: (a) `LPWD-DOC-26-0189` here and in the other examples (preferred: 03 and 25 already agree on it); (b) give 03 the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no
- From: broad, logistics, context

### tender/15#F2 · Medium · Province in Region
- XPath: `/Tender/cac:TendererParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/cbc:Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `cbc:CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province is a country subentity; the Bayvarran addresses of the flow put their state in `cbc:CountrySubentity`. The same value occurs 219 times in 104 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'`, parties' count; 22 of the 36 tender examples, broad).
- Condition: The province is in `cbc:CountrySubentity` (with a code if Urvania has a list); `cbc:Region` is absent or holds a region in the sense of its definition.
- Options: (a) move the value to `cbc:CountrySubentity` (preferred); a province code is optional.
- Needs decision: no
- From: broad, parties

### tender/15#F3 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:SubcontractorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with `listID="ISO 639"` repeats the language code of the sibling `cbc:ID`; it names no locale (a locale says in which territory or variant the language is used, as the `en-XB`/`en-XU` tags on texts of this flow do). The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales named in `listID`.
- Options: (a) remove `cbc:LocaleCode` (preferred: `cbc:ID` states the language and nothing uses a locale); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad, parties, logistics, context

### tender/15#F4 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The legal entity of the Lumeport Public Works Department is described like a company: `CompanyLiquidationStatusCode` ("A code signifying the party's liquidation status") `ACTIVE` ("Active, not in liquidation"), in a registration scheme of type `COMMERCIAL` ("Commercial register: A register of businesses"). The department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411 here). A city department is not a business and cannot go into liquidation, so both values carry a meaning that does not fit the party. The same description is used in all 36 examples of the flow (broad, by hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the description says in what capacity it is entered there).
- Options: (a) drop `CompanyLiquidationStatusCode` and the `COMMERCIAL` type for public bodies, keeping register name and ID (preferred); (b) a register type for public bodies (needs a code); (c) say in the world's rules that public bodies are entered in the federal business register.
- Needs decision: no
- From: broad, parties

### tender/15#F5 · Medium · The tendered price is given in the response to the quality criterion; the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription` = `Warranty and coating.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `10`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `124080.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- Why: `Amount` in an awarding criterion response "Specifies the monetary amount tendered for this awarding criterion", `Quantity` "Specifies the quantity tendered for this awarding criterion". The response refers to `AC-2`, the quality criterion of the call for tenders (type `QUALITY`, scored in years from 5 to 10); the 10 years answer it. The 124080.00 lume are the tender's total price, which is what the price criterion `AC-1` scores ("The lowest total of unit prices.", with unit-price limits of 350 to 600 lume); the tender has no response to `AC-1` at all. An evaluator finds an amount under quality and nothing under price.
- Condition: Each awarding criterion response carries only what was tendered for the criterion it names: the price (in the terms AC-1 evaluates) under AC-1, the years under AC-2.
- Options: (a) a response to `AC-1` with the amount or the unit prices, and the response to `AC-2` with the years only (preferred); (b) drop the amount, the price being in the lines and the monetary total.
- Needs decision: no
- From: broad, money, logistics, context

### tender/15#F6 · Low · Master data the tender does not use: customs trader numbers and the tenderer's logistics service provider
- XPath: `/Tender/cac:TendererParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: Section 4.8: data copied from a party's master data into a document that does nothing with it. The customs trader numbers identify the parties towards customs; a tender declares nothing to customs (the numbers are used in 30 and 31). `ServiceProviderParty` ("A party providing a service to this party") names Castrano Logistics as Valdara's provider of warehousing and despatch, with its key account desk; the tender offers benches and their installation, names Saltmere as its only subcontractor, and nothing in it concerns warehousing or despatch (Castrano acts in 29-DespatchAdvice.xml).
- Condition: Each party carries only the identifiers and related parties the tender uses.
- Options: (a) leave the customs trader numbers and the service provider out of the tendering documents (preferred); (b) keep them only where the document says what they are for (e.g. as a subcontractor or in delivery terms).
- Needs decision: no
- From: broad, parties, context

### tender/15#F7 · Low · Large enterprise with 180 employees
- XPath: `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- Why: `LARGE` is defined in the world's list as "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL or 5,000,000,000 XUF). Valdara declares 180 employees in its qualification (13), a financial capability of 9 200 000.00 lume, and its production capability is valued at 4 800 000.00 lume (12). Nothing in the flow supports a turnover above the limit, so by the figures given Valdara is medium-sized. The contradiction is not strict, because the definition is an "or" and no turnover is stated as such; a listed company with a share capital of 250 million ferra may have other business. Hence Low, but what Valdara is needs to be decided once.
- Condition: The size class of Valdara Industries agrees with the number of employees and the financial figures stated for it in the flow.
- Options: (a) 250 or more employees in 13, if Valdara is meant to be a large listed company (preferred by broad and parties); (b) `MEDIUM` wherever Valdara is described.
- Needs decision: yes
- From: broad (High), parties (Low)

### tender/15#F8 · Low · Contacts that do not fit the tenderer's and the subcontractor's role
- XPath: `/Tender/cac:TendererParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Tender/cac:TendererParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Tender/cac:TendererParty/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- XPath: `/Tender/cac:SubcontractorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Tender/cac:SubcontractorParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/Tender/cac:SubcontractorParty/cac:Contact/cbc:Department` = `Procurement`
- Why: Valdara is the tenderer here, but its contact is the order desk with a customer service officer and the mailbox `order@…`, the function that takes purchase orders (the right one in 26–28); questions on a tender go to whoever prepares bids. Saltmere's contact is named `Bids office` (`bids@…`), a selling function, while its job title and department are those of a buyer (`Procurement officer`, `Procurement`), the same as the contracting department's contact; name, job title and department do not agree.
- Condition: Name, job title and department of each contact describe the same function, one that handles tenders for the party.
- Options: (a) a bid or tender contact for Valdara in the tendering documents, and a bid manager / sales department for Saltmere (preferred); (b) drop job title and department, or the contact where the document needs none.
- Needs decision: no
- From: broad, parties

### tender/15#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax, expressed as text": the party's own status. The text begins "Sale to a public body", a property of a transaction (someone else's sale to the department). The code `PUBLIC` itself fits: its list description is "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (parties); broad would prefer a separate party-status code.
- Condition: The party's exemption reason states the party's status (a public body that buys free of the state sales tax), not a kind of sale.
- Options: (a) reword the text to the status, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred, as in the contest flow); (b) a separate party-status code for PartyTaxScheme.
- Needs decision: no
- From: broad, parties

### tender/15#F10 · Low · Originator and beneficiary repeat the contracting party
- XPath: `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The tender names the department three times, as `ContractingParty`, as `OriginatorCustomerParty` ("The party originating the Tender") and as `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it"), the two extra roles by register number and name only. They exist for the case that another body originated or will use the purchase; here they say nothing `ContractingParty` does not (no fillers). Counter-argument (broad, under "Considered and refuted"): a customer party as originator is the customer for whom the tendering was started, as in the notices. The merge keeps the finding: even read that way, the value repeats the contracting party.
- Condition: Originator and beneficiary are present only where they name a party, office or contact that differs from the contracting party.
- Options: (a) remove both (preferred); (b) name the parks service as beneficiary if it is a body of its own in the world.
- Needs decision: no
- From: parties, context

### tender/15#F11 · Low · Fees of the tendered project that are the tenderer's own costs (paper copy, courier)
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeTypeCode` = `COURIER`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `TenderedProject/FeeAmount` is "The fee amount for tendered projects", `AdditionalFee` "An additional fee for this tendered project": fees that are part of what is tendered. The 50 lume are the department's price for a paper copy (`03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`) in an electronic procedure, the 12 lume the tenderer's courier for its guarantee. Neither is offered or charged to the buyer, and the total (sum of the lines) does not include them; if they were charged, they would be missing from it. The same two fees, to the cent, are in all three tenders of the flow (15, 17, 19; `grep -c "Courier of the guarantee"` over the flow's XML). Money adds that a tenderer submitting electronically from Urvania needs a reason to buy the paper copy, and that the guarantee was issued in Lumeport for a beneficiary in Lumeport (14), so the courier's route is not evident.
- Condition: The tendered project carries a fee only if it is part of what is offered or owed under the tender, and then says who pays it and whether the total includes it.
- Options: (a) remove both fees from the tenders (preferred); (b) keep the documentation fee only in the tender of a tenderer the story says bought the paper copy, as a record that it was paid.
- Needs decision: no
- From: broad, money (needs decision yes), context

### tender/15#F12 · Low · The tender does not refer to its tender guarantee
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `/Tender/cac:DocumentReference/cbc:ID` = `VI-DS-B180`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:ID` = `BL-DOC-26-0200`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`
- Why: The terms require a tender guarantee of 2400.00 lume, constituted by the deadline (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`); the bank certified it the day before this tender (14). The tender mentions it only as the object of a courier fee; its references name the data sheet, the qualification, a reference list and the call, not the certificate or the guarantee number (both occur only in 14). The department has to match tender and guarantee by party and folder. Counter-argument (broad, refuted): the bank sends the certificate to the beneficiary itself and the Tender has no dedicated guarantee reference; the merge keeps the finding, because the generic `DocumentReference` the tender already uses can carry it.
- Condition: The tender refers to the guarantee that covers it (certificate or guarantee number, with a document type).
- Options: (a) a `DocumentReference` to `BL-DOC-26-0200` with a document type (preferred); (b) leave the link to the certificate, which names tenderer and procedure, and say so.
- Needs decision: no
- From: money, logistics, context

### tender/15#F13 · Low · Evidence reference with an ID only, not the ID of the reference evidence in the qualification
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:Evidence/cbc:ID` = `EV-FER-PARKS`
- Why: `EvidenceDocumentReference` is "A reference to a non-structured evidentiary document supporting this tendered project". It has only the ID `VI-REF-2025`, which occurs in no other kind of document (only in the three tenders 15, 17, 19), while the qualification this tender relies on calls its reference evidence `EV-FER-PARKS` ("Ferrano reference"). Whether they are the same document is not visible.
- Condition: The evidence reference says what the evidence is (document type or description), and uses the ID of the evidence in 13 if it is the same.
- Options: (a) add a document type or description, and align the ID with 13 if it is the same evidence (preferred); (b) drop it if the qualification's evidence suffices.
- Needs decision: no
- From: logistics

### tender/15#F14 · Low · A tax total of zero that names no tax
- XPath: `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TotalTaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `119760.00`
- Why: `TaxTotal/TaxAmount` is "The total tax amount for a particular taxation scheme, e.g., VAT; the sum of the tax subtotals for each tax category within the taxation scheme." This tax total has no subtotal, so neither the scheme nor the reason for zero is stated. The terms speak of Bayvarra's state sales tax with an exemption for public bodies; the later invoice shows Urvanian VAT at zero as an export and a withholding tax on the installation (`32-Invoice.xml:/Invoice/cac:WithholdingTaxTotal/cbc:TaxAmount` = `72.00`). Line 1 repeats the zero and a tax-inclusive amount; line 2 has neither.
- Condition: The tax total states the scheme, category and exemption reason that make it zero, consistently with the terms, and both lines treat tax alike; or the tender carries no tax total.
- Options: (a) one tax subtotal with category and exemption reason for the taxable amount 124080.00 (preferred); (b) drop the zero amounts.
- Needs decision: no
- From: money

### tender/15#F15 · Low · The tender equals the buyer's estimate to the cent on both lots
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `119760.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: The department's published estimates are 119 760.00 for lot 1 (240 × 499.00), 4 320.00 for lot 2 (240 × 18.00) and 124 080.00 in all; Valdara tenders exactly these amounts. In a price competition with an auction to follow, a tender that hits the estimate to the cent on both lots is not plausible; the reader takes one figure to be derived from the other. (Money placed this under "Outside this review" as a matter of the notices; it is a statement of this tender compared with 03, so it stays here.)
- Condition: Estimate and tender are independent figures, or the document explains why they are equal.
- Options: (a) a rounded estimate in 01–03 (e.g. 125 000) (preferred: later documents build on the tender price); (b) another tender price, which moves every later amount of the flow.
- Needs decision: yes
- From: broad, context

### tender/15#F16 · Low · No unit prices, although the procedure evaluates and auctions unit prices
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:Quantity` = `240`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:PriceEvaluationCode` = `UNITPRICE`
- Why: The terms evaluate unit prices, ask for a price schedule with `Unit prices per lot.`, and announce an auction on the unit prices; framework releases are ordered at the framework prices. The tender gives line totals only (unit prices 499.00 and 18.00 must be worked out by dividing by 240), although the line already carries `OfferedItemLocationQuantity` ("A set of location-specific properties (e.g., price, quantity, lead time)"), used for the lead time alone.
- Condition: Each tender line states the unit price it offers, and quantity × unit price equals the line amount.
- Options: (a) a price in `OfferedItemLocationQuantity` of both lines (preferred); (b) keep the totals and reference the price schedule as a document.
- Needs decision: no
- From: money

### tender/15#F17 · Low · A replacement item that nothing describes
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:Quantity` = `1`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `/Tender/cac:TenderedProject/cbc:VariantID` = `V0`
- Why: `ReplacementRelatedItem` is "A catalogue item that may be a replacement for the item described in this tender line." The tender offers the Serra 180 "as specified" and names `VI-C180-2026` with an ID only. The ID occurs in no other tender example (elsewhere only in retail/02-Catalogue.xml, again with ID and quantity only; `grep -rl --include='*.xml' VI-C180-2026`), and Valdara's framework catalogue (25) lists the bench as `VI-B180` and no such item. The buyer cannot tell what would replace the bench, nor whether it is the one variant the terms allow (recycled plastic slats), which would belong in a tendered project with its own `VariantID`.
- Condition: A replacement item is described (name or description and when it replaces the item), exists in the tenderer's catalogue, or is absent.
- Options: (a) remove it (preferred by context); (b) describe it and add it to the catalogue (preferred by broad and logistics); (c) offer it as a variant project. The merge prefers (a): nothing in the flow uses a replacement.
- Needs decision: no
- From: broad, logistics, context

### tender/15#F18 · Low · The subcontractor has 20 % in the qualification and 3.5 % of the tender
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- Why: The tender names Saltmere Engineering as subcontractor; by 13 it does the installation. The installation line is 4 320.00 of 124 080.00 lume, 3.48 % (recalculated), while the qualification this tender refers to gives Saltmere a participation of 20 %. Participation could be measured otherwise (work share rather than value), but the flow gives no other measure. It stays within the terms' maximum of 30 % either way (money).
- Condition: The share declared in the qualification agrees with the split of the tender, or the measure of the share is stated.
- Options: (a) about 3.5 % in 13 (preferred); (b) show in the tender what else Saltmere does.
- Needs decision: no
- From: broad

### tender/15#F19 · Low · Italian street name and legal form tagged as English
- XPath: `/Tender/cac:TendererParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The renderings are tagged `en-XU` but are Italian. Parties refuted this as the invented world's English-language names of Urvanian places and legal forms (accepted as given), and noted that the tag follows the issuer's locale consistently (`en-XU` in Valdara's documents, `en-XB` in Bayvarran ones). The merge carries the question as a finding to align with the earlier flows (analysis/review-merge-decisions.md: Low, needs decision), because the legal form "Società urvaniana per azioni" is not a proper name, and no convention is stated.
- Condition: A rule for these renderings is recorded (exonyms and legal forms as given in the world's English), or the English renderings are English.
- Options: (a) record the convention in the story (preferred); (b) English renderings, at least for the legal form.
- Needs decision: yes
- From: merge (parties considered and refuted it)

### tender/15#F20 · Low · Signature identifier carries the example's file number
- XPath: `/Tender/cac:Signature/cbc:ID` = `VI-SIG-TENDER-15`
- Why: `Signature/ID` is "An identifier for this signature", assigned by the signer; the suffix is the example's position in the flow's file numbering, not a number of Valdara's. Added by the merge to match 19#F18 (logistics raised it there).
- Condition: The signature ID does not depend on the example's file number.
- Options: (a) derive it from the document number, e.g. `VI-SIG-0201` (preferred).
- Needs decision: no
- From: merge (raised by logistics in 19)

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- Arithmetic, recalculated: 119 760.00 / 240 = 499.00 a bench, within 350.00–600.00; 4 320.00 / 240 = 18.00; 119 760.00 + 4 320.00 = 124 080.00 = `LineExtensionAmount` = `PayableAmount`; tax 0.00, tax-inclusive line amount = line amount.
- Ordering data: pallet of 4, increment 4, minimum 20 and maximum 96 are multiples of 4; the average release of 40 (240 / 6) and the first order (26, 40 EA) fit. Pallet of four benches of 1800 × 620 × 780 mm (25): two side by side (1240 mm) in two layers (1560 mm) on 1800 × 1240 mm is plausible (logistics).
- Against the call for tenders: quantity 240 EA and 240 anchor sets (line 1, sub-line 1.1), line reference 1, envelope `ENV-1` / `COMBINED`, tender type `COMBINED`, validity 90 days, warranty 5 years (required 5), lead time 7 days (at most 10), quality response 10 years (range 5–10), sub-response to `AC-2.1`.
- `TendererQualificationDocumentReference` `VI-DOC-26-0199` is 13 by the same tenderer, issued 21 minutes earlier, with the same subcontractor (Saltmere Engineering, 20410685) and lots. The tender (2026-02-25 09:13) is before the deadline 2026-02-26 12:00 and after the guarantee (14, 2026-02-24); 16 acknowledges it by its ID.
- `DocumentReference` `VI-DS-B180` is the item specification of 25, 26, 29–33.
- Amounts against the award: 22 has the same payable amount 124080.00; the first release is invoiced at 499 + 18 (40 × 517 = 20 680.00). Price score 60 × 119040 / 124080 = 57.6 vs 60 for the other tender, quality 10 vs 6 years: the award to this tender is consistent (money).
- Parties: identical, element by element, to the same parties in the other examples of the flow apart from the findings (parties, by script); telephone country code +999 is unassigned; web and mail in `.example`; ISIC 3100, 4290, 8411 fit.

## Considered and refuted
- `/Tender/cac:OriginatorCustomerParty`: "The party originating the Tender" given as the department, not the tenderer — refuted because the customer party in this role is the customer for whom the tendering was started, as in the notices (from broad; the merge keeps the repetition of the contracting party as F10).
- `/Tender/cac:DocumentReference`: the tender does not refer to the guarantee certificate — refuted because the bank sends the certificate to the beneficiary itself and the tender model has no dedicated reference (from broad; the merge disagrees, see F12).
- `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]`: one tendered project for both lots — refuted because the definition allows "one project, multiple projects, or the global project", and the lines keep the lots apart (from broad).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation`: "Five years on the frame." against "Ten years on the coating." — refuted, warranties on different parts (from broad, context).
- `/Tender/cbc:Note[1]`: the Urvanian note cannot be checked against the English one — refuted as a finding, the language being invented (from broad).
- `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: should be reduced by the withholding tax the invoice later deducts — refuted, the tender states the price; withholding is settlement (from money).
- `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount`: subcontracted share above what the terms allow — refuted: 4320 / 124080 = 3.5 %, under the maximum of 30 % (from money).
- `/Tender/cac:TendererParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` not a valid form — refuted, the definition prescribes no format and the value reads as UTC−1 (from parties).
- `/Tender/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: `Room 2.14` belongs in `cbc:Room` — refuted, a room where mail is delivered fits InhouseMail (from parties).
- `/Tender/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: functional contact name with a job title, and `Procurement office` vs `Procurement` — refuted, functional names are recommended and both name the same unit (from parties).
- `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: `STATE` against a local authority — refuted, the code is the level of the tax, not of the party (from parties).
- `/Tender/cac:TendererParty/cac:PostalAddress/cbc:StreetName[2]`: Italian text tagged English and en-XB/en-XU depending on the issuer — refuted as the world's English-language names and a consistent issuer-locale rule (from parties; the merge carries the Italian-as-English half as F19, to align with earlier flows; the issuer-dependent tag is accepted here, the tag being consistent within this document).
- `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: amount against "The number of shares" — refuted as a matter of the UBL model (from parties; the earlier flows note it for the TC write-up).
- `/Tender/cac:TendererParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` an assigned ISO 6523 code — refuted as far as own knowledge goes; the register was not available (from parties).
- `/Tender/cac:TendererParty/cac:Language/cbc:ID`: `qau` a real ISO 639 code — refuted, qaa–qtz is reserved for local use (from parties).
- `/Tender/cac:SubcontractorParty/cac:PartyLegalEntity`: incomplete description — refuted, all optional and unused here (from parties).
- `/Tender/cac:DocumentReference/cbc:ID`: generic reference with only an ID — refuted, the same ID is the item specification in 25, 26, 29–33 (from logistics).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure`: 7 days here, 5 in the catalogue — refuted, the catalogue after the award may offer a shorter time (from logistics).
- `/Tender/cbc:IssueTime`: 21 minutes after the qualification — refuted, prepared together (from logistics).
- `/Tender/cac:TenderedProject/cbc:VariantID`: `V0` although one variant is allowed — refuted, an identifier for the base tender is legitimate (from logistics, context).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyParty`: repeats the tenderer — refuted, it says who gives the warranty (from context).
- `/Tender/cac:TenderedProject/cac:TenderLine[2]`: no reference to a line of the call — refuted here, 03 has no line for the installation (from context).
- `/Tender/cac:SubcontractorParty`: checked against 13, where the same party is a consortium party — refuted here, the element fits (from context).

## Changed in the merge
- broad/F12, parties/F8 → F4: raised from Low to Medium, to align with analysis/review-merge-decisions.md (public bodies as companies: Medium/no) and the contest and furniture merges; the values carry a meaning that does not fit the party.
- broad/F2 (High/no), parties/F4 (Low/yes) → F7: Low/yes. The LARGE definition is an "or"; 180 persons alone do not contradict it, and no turnover is stated, so there is no strict contradiction (not High).
- logistics/F5 (Low) → F5: Medium, as broad, money and context: the amount carries a meaning other than its definition.
- money/F4 (needs decision yes) → F11: no; removing the fees changes no story; money's option kept as (b).
- logistics/F3 split into F17 (replacement item, combined with broad/F8 and context/F6) and F13 (evidence reference): two different elements and problems.
- broad/F10 and parties/F5, F6 → F8: one contacts finding per example.
- broad/F11, parties/F3, context/F9, F10 → F6: one copied-master-data finding.
- F19 added by the merge from a candidate parties refuted, to align with the earlier flows' decision on Italian text tagged as English.
- F15: kept here, although money placed it under "Outside this review".
- F20 added by the merge (appended, no renumbering) to match what logistics raised in 19.

## Outside this review
- The tendering terms tie envelope `ENV-1` to lot 1 only, while this tender uses it for both lots; the inconsistency lies in 01–03 (from context).
- Whether the electronic auction announced in 02 and 03 took place leaves no trace in the flow (from money, context).
