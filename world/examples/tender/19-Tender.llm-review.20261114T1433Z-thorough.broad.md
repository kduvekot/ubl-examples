# LLM review: 19-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/19-Tender.xml`, Git blob `21feca31f7c744f8e198c18ed5445abb1d1142ee` (committed)
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

### tender/19#F1 · High · The tender refers to another tenderer's qualification document
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- Why: the element is "A reference to the tenderer qualification document that has been used to qualify the tenderer". The tenderer is Brackenmere Furniture, but `VI-DOC-26-0199` is the TendererQualification of Valdara Industries (`13-TendererQualification.xml:/TendererQualification/cbc:ID` = `VI-DOC-26-0199`, `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`). Brackenmere qualified through its own qualification application response (`07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`). The same wrong reference is in the withdrawn tender 17-Tender.xml.
- Condition: the reference names a document by which Brackenmere Furniture itself was qualified, or is absent.
- Options: (a) refer to `BF-DOC-26-0193` (preferred: it exists in the flow and is Brackenmere's own; it is a qualification application response rather than a TendererQualification, which the reference can say in a DocumentType); (b) leave the reference out.
- Needs decision: no

### tender/19#F2 · High · The evidence document is the competitor's reference list
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- Why: "A reference to a non-structured evidentiary document supporting this tendered project." The identifier carries Valdara Industries' prefix and is the very evidence Valdara's tender cites (`15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`). A competitor's evidence cannot support Brackenmere's tender; Brackenmere's own documents carry the prefix BF (`/Tender/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`).
- Condition: the evidence reference identifies a document of Brackenmere Furniture, or is absent.
- Options: (a) an own evidence document of Brackenmere (e.g. its reference supplies; preferred, the call asks for "Three similar supplies in five years"); (b) remove it.
- Needs decision: no

### tender/19#F3 · High · Warranty of five years on the line, six years in the criterion response
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: the tender line gives a warranty of five years on the frame; the response to awarding criterion AC-2 ("Specifies the quantity tendered for this awarding criterion") tenders six years on the frame and the slats. Both statements are about the frame of the same bench, so one tender offers two different warranty periods, and the higher one is the one that is scored.
- Condition: the warranty period for the frame is the same in the tender line (text and period) and in the awarding criterion response.
- Options: (a) make the line say six years on frame and slats, period 6 ANN (preferred: the criterion response is what the evaluation uses); (b) lower the response to five years.
- Needs decision: no

### tender/19#F4 · High · The corrected tender was issued before the withdrawal that announces it
- XPath: `/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `/Tender/cbc:IssueTime` = `12:10:00`
- XPath: `/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.`
- Why: the note speaks of "the withdrawn tender", but the withdrawal of BF-DOC-26-0203 was issued almost six hours later (`18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`, `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueTime` = `17:56:00`) and itself says `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.` When this tender was issued the first tender was still in force, so Brackenmere had two tenders in at once, which the call forbids (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`).
- Condition: this tender is issued after the withdrawal 18-TenderWithdrawal.xml (and before the deadline 2026-02-26 12:00), so that "withdrawn" and "follows" are both true.
- Options: (a) issue this tender after 2026-02-24 17:56 (preferred); (b) issue the withdrawal before 12:10 and reword its note.
- Needs decision: no

### tender/19#F5 · Medium · The total price is tendered under the quality criterion
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `119040.00`
- Why: Amount "Specifies the monetary amount tendered for this awarding criterion". AC-2 is the quality criterion of the call (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:AwardingCriterionTypeCode` = `QUALITY`), measured in years (5 to 10); the price criterion is AC-1. 119040.00 is the tender's total price, which is not an amount tendered for warranty and coating. There is no response to AC-1.
- Condition: an amount in an awarding criterion response belongs to a criterion that is scored on an amount; the response to AC-2 carries only what AC-2 scores.
- Options: (a) remove Amount from the AC-2 response and add a response to AC-1 with the price (preferred); (b) remove Amount only, the price being in LegalMonetaryTotal.
- Needs decision: no

### tender/19#F6 · Medium · A spare slat as "replacement" for the bench
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:Quantity` = `1`
- Why: ReplacementRelatedItem is "A catalogue item that may be a replacement for the item described in this tender line". The line's item is the bench PB-2; by its identifier BF-SLAT-PB2 is a slat of that bench, i.e. a spare part, which cannot replace the bench. (UBL's Catalogue Line has ComponentRelatedItem and AccessoryRelatedItem for parts; TenderLine has only ReplacementRelatedItem.) The reference also has no name or description, so the reader has to guess from the ID.
- Condition: an item under ReplacementRelatedItem can stand in for the whole bench of the line; a spare part is not given there.
- Options: (a) remove it and mention spare slats in the line's Note (preferred); (b) name a real substitute bench.
- Needs decision: no

### tender/19#F7 · Medium · The call for tenders is cited by an identifier that no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: both elements refer to "the call for tender document". The call for tenders of this procedure is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`; no example of the flow has the document ID PWD-2026-PARKS-CFT (searched `<cbc:ID>PWD-2026-PARKS-CFT</cbc:ID>` over world/examples/*/*.xml: it occurs only inside reference elements). The catalogue of the same flow cites the call by its real ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`). The line reference `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersLineReference/cbc:LineID` = `1` does match line 1 of 03.
- Condition: every reference to the call for tenders resolves to the ID of 03-CallForTenders.xml, the same way in all examples of the flow.
- Options: (a) use LPWD-DOC-26-0189 (preferred); (b) if PWD-2026-PARKS-CFT is meant as the authority's file reference of the call, give it in the call itself so the two can be linked.
- Needs decision: no

### tender/19#F8 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; a locale is a place or regional variant (e.g. the country), not the language again. The value repeats the language code of `cbc:ID` with the list "ISO 639". The same pattern is in 213 of the 250 examples (`grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`).
- Condition: LocaleCode, where present, identifies a locale (where the language is used), from a list of locales, and differs in kind from Language/ID.
- Options: (a) a locale such as the country or a language-region tag (preferred); (b) leave LocaleCode out.
- Needs decision: no

### tender/19#F9 · Low · Fees of the contracting authority stated in the tenderer's offer
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: the 50 lume are the authority's charge for a paper copy of the procurement documents (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`; its project says electronic documents are free). The tender is exchanged electronically, nothing shows that Brackenmere took paper copies, and the offer does nothing with either fee: they are not in the tender's totals (119040.00 = lines only). The courier fee concerns "the guarantee's original", but the only guarantee in the flow is Valdara's (14-GuaranteeCertificate.xml, interested party Valdara Industries); Brackenmere's tender has no guarantee reference. The identical values are in Valdara's tender (15) and the withdrawn tender (17), which suggests copied data.
- Condition: a fee in this tender is one that Brackenmere actually paid or charges in this procedure, and the document says which; otherwise it is absent.
- Options: (a) remove both fees (preferred); (b) keep them only with a guarantee and a paper-copy request of Brackenmere in the story.
- Needs decision: yes (whether Brackenmere provided a tender guarantee at all, as the call requires, is a story question)

### tender/19#F10 · Low · The public works department described as a company in a commercial register
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the contracting authority is a municipal department (industry 8411, general public administration). A department is not entered in a commercial register and cannot be in or out of liquidation; "Active, not in liquidation" is a statement about a company. The same description of the department is in every example of the flow that gives its legal entity.
- Condition: the legal entity of the department carries only what applies to a public body (name, its registration number and the register that really holds public bodies), without a liquidation status.
- Options: (a) drop the liquidation status and type the registration scheme as a register of public bodies (preferred); (b) drop CorporateRegistrationScheme for public bodies.
- Needs decision: no

## Checked and consistent
- Arithmetic: 240 × 480.00 = 115200.00 (line 1), 240 × 16.00 = 3840.00 (line 2), sum 119040.00 = LegalMonetaryTotal LineExtensionAmount = PayableAmount; tax 0.00 agrees with the authority's exemption. Against the withdrawn tender (17: 112800.00 = 240 × 470.00) only the bench price changed, as the note says.
- Unit prices 480.00 and 16.00: the bench price lies inside the call's range 350.00–600.00 (03, AC-1 and line 1).
- Tender line 1 against line 1 of 03: quantity 240 EA, sub-line 1.1 ground anchor sets 240 SET, lead time 7 days ≤ the required 10 days, warranty ≥ the required 5 years.
- Lots LOT-1 and LOT-2 exist in 03 (benches; installation) and match lines 1 and 2; envelope ENV-1 / COMBINED matches the call.
- Issue time 2026-02-24 12:10 is before the submission deadline 2026-02-26 12:00.
- Pallet of 4, increment 4, minimum 20 (5 pallets), maximum 96 (24 pallets): all multiples of 4.
- check_ids.py: GLN 9523710900008 has a correct check digit.
- Brackenmere Furniture is described as in 07 and 17 (register number 20412466, Joiners Row 14, Marrowdale).

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity`: 96 is less than the 240 benches tendered — refuted because the contract is a framework with releases over two years; the maximum is per order, and 240 is the total.
- `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: "Sale to a public body" reads like a transaction, not the party's status — refuted because the text gives the party's own status ("public bodies are exempt from the state sales tax"), which is what the element asks for.
- `/Tender/cac:TendererParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` is not written as an ISO 8601 offset — refuted because the element is free text for an offset and the fictional world's zone is accepted as given.
- `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the authority as "party originating the Tender" — refuted because in procurement documents this role is the customer for whom the procedure is run; the authority is its own originator and beneficiary.
- `/Tender/cac:TendererParty/cac:Contact/cbc:JobTitle`: a customer service officer of "Trade sales" as contact for a public tender — refuted because a small furniture maker's sales desk plausibly handles tenders.
- `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription`: "Warranty and coating." differs from the call's name "Quality" for AC-2 — refuted because it describes what AC-2 measures (years, and the coating sub-criterion AC-2.1).
- `/Tender/cac:DocumentReference/cbc:ID`: only an ID, no type — refuted as a finding of its own because the ID repeats on line 1 next to the item, where it reads as the bench's data sheet.

## Outside this review
- The same wrong references (F1, F2), the warranty contradiction (F3) and the fee data (F9) are in 17-Tender.xml, which belongs to that example's review.
- 03-CallForTenders.xml estimates the contract at exactly the amounts of Valdara's tender (124080.00 = 119760.00 + 4320.00), a matter for the reviews of 03 and 15.
