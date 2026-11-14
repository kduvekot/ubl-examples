# LLM review: 17-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/17-Tender.xml`, Git blob `ea8d3a233b928425f6a062a240c2497a8e4da8a4` (committed)
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

### tender/17#F1 · High · Brackenmere's tender refers to Valdara's qualification and Valdara's reference
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `/Tender/cac:TendererParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`
- Why: TendererQualificationDocumentReference is "A reference to the tenderer qualification document that has been used to qualify the tenderer." `VI-DOC-26-0199` is 13-TendererQualification.xml, the qualification of the competitor Valdara Industries, issued on 2026-02-25, two days after this tender. The evidence `VI-REF-2025` likewise carries Valdara's prefix and is the evidence of Valdara's tender 15. Brackenmere's own qualification document in the flow is its qualification application response 07 (`BF-DOC-26-0193`).
- Condition: The tender refers to the tenderer's own qualification and its own evidence, both existing at the time of the tender.
- Options: (a) `BF-DOC-26-0193` as qualification reference and an evidence document of Brackenmere (preferred); (b) drop the two references.
- Needs decision: no

### tender/17#F2 · High · Call for tenders referenced under an ID no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The tender points to the call for tenders of the procedure as `PWD-2026-PARKS-CFT`. The call for tenders is 03-CallForTenders.xml with the ID `LPWD-DOC-26-0189`; no document of the flow has the ID `PWD-2026-PARKS-CFT`. That ID is used in 8 examples (grep over the flow's XML files: 01, 02, 03, 06, 15, 17, 19, 24), while 25-Catalogue.xml uses `LPWD-DOC-26-0189`, so the flow has two IDs for one document.
- Condition: The reference carries the ID of 03-CallForTenders.xml (or 03 carries the ID the references use).
- Options: (a) use `LPWD-DOC-26-0189` (preferred); (b) keep one procedure-level ID for the call for tenders and carry it in 03 as well.
- Needs decision: no

### tender/17#F3 · High · Five years on the frame in the line, six years on the frame in the criterion response
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: The tender line states a warranty of five years on the frame (text and period); the response to the quality criterion, which is scored on the years offered, says six years on the frame and the slats. The same tender offers two different warranties on the frame.
- Condition: The warranty in the tender line and the years offered for the quality criterion agree (or cover clearly different things).
- Options: (a) six years in the line as well (preferred: the score rests on it); (b) five in the response.
- Needs decision: no

### tender/17#F4 · Medium · The tender price is given as the response to the quality criterion; the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `116640.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`
- Why: Amount in an AwardingCriterionResponse "Specifies the monetary amount tendered for this awarding criterion". The response is to `AC-2`, the quality criterion; the amount 116 640.00 is the tender price, which the price criterion `AC-1` scores, and `AC-1` has no response.
- Condition: Each response carries what its criterion scores.
- Options: (a) a response to `AC-1` with the amount, none under `AC-2` (preferred); (b) drop the amount.
- Needs decision: no

### tender/17#F5 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/17#F6 · Low · Fees copied from the other tender, including the courier of a guarantee that does not exist in the flow
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: FeeAmount is "The fee amount for tendered projects", AdditionalFee "An additional fee for this tendered project". As in 15, the two amounts are the tenderer's own costs, not part of the offer or of the monetary total. They are identical to Valdara's (50.00 and 12.00); for Brackenmere no guarantee certificate exists in the flow (14 is Valdara's), although the call for tenders requires a tender guarantee of 2 400 lume.
- Condition: The tendered project carries fees only if they are part of the offer; what it says about a guarantee agrees with the documents of the flow.
- Options: (a) remove both (preferred); (b) add Brackenmere's guarantee to the flow.
- Needs decision: no

### tender/17#F7 · Low · A slat as the replacement for a bench
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:Item/cbc:Name` = `Park bench Brackenmere PB-2`
- Why: ReplacementRelatedItem is "A catalogue item that may be a replacement for the item described in this tender line", i.e. an item that can be supplied instead of the bench. `BF-SLAT-PB2` reads as a slat for the PB-2, a spare part (a component or accessory), not a replacement of the bench; it has no description.
- Condition: A replacement item is one that can take the place of the tendered item, and is described.
- Options: (a) remove it or use the relation for parts/accessories (preferred); (b) name a real alternative bench.
- Needs decision: no

### tender/17#F8 · Low · A public body described as a company in a commercial register
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/17#F9 · Low · The department's tax exemption reason describes a sale
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit.
- Arithmetic: 112 800.00 / 240 = 470.00 a bench (within 350.00 to 600.00); 3 840.00 / 240 = 16.00; 112 800.00 + 3 840.00 = 116 640.00 = LineExtensionAmount = PayableAmount; tax 0.00.
- Against the call for tenders: 240 EA and 240 anchor sets, line reference 1, envelope `ENV-1`, validity 90 days, warranty period 5 years, lead time 7 days (at most 10 required), response of 6 years within the 5 to 10 scored.
- The tender (2026-02-23 16:37) is before the deadline; 18 withdraws it by its ID `BF-DOC-26-0203`; 19 repeats it with 480.00 a bench instead of 470.00, all else equal (compared leaf by leaf).
- Brackenmere's declared turnover of 410 000.00 (07) is above the required 250 000.00.

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:OrderableUnit`: pallet of 4, minimum 20, maximum 96 and lead time 7 days are identical to Valdara's tender — refuted as a finding because the same ordering terms for a bench of the same size are possible; noted as a sign of copying.
- `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]`: Brackenmere tenders for lot 2 although its qualification request concerned lot 1 only — refuted because the notice lets a tenderer submit for one or more lots.
- `/Tender/cac:OriginatorCustomerParty`: the department as "party originating the Tender" — refuted as in 15.

## Outside this review
- Brackenmere's tender is lower than Valdara's (116 640.00 against 124 080.00), and after its correction still lower (119 040.00); how the award to Valdara follows from price and quality scores belongs to the reviews of 21 to 23.
- No tender receipt for this tender exists in the flow; see the review of 18.
