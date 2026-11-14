# LLM review: 19-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/19-Tender.xml`, Git blob `21feca31f7c744f8e198c18ed5445abb1d1142ee` (committed)
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

### tender/19#F1 · High · The corrected tender was issued before the withdrawal that announces it
- XPath: `/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `/Tender/cbc:IssueTime` = `12:10:00`
- XPath: `/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.`
- XPath: `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`
- XPath: `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueTime` = `17:56:00`
- XPath: `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`
- Why: The note calls 17 "the withdrawn tender", but the withdrawal (18, `BF-DOC-26-0204`) was issued 5 h 46 min later and announces this tender as still to come. Each document places the other in its future; the numbering (0203 tender, 0204 withdrawal, 0205 this tender) follows the withdrawal's order, not the issue times. At 12:10 Brackenmere had two live tenders, which the terms exclude. The same contradiction is a finding of 18 (18#F1).
- Condition: This tender is issued after the withdrawal and before the deadline (2026-02-26 12:00), so that both notes and the numbering hold.
- Options: (a) issue this tender after 2026-02-24 17:56 (preferred by broad and logistics); (b) issue the withdrawal before 12:10 (preferred in 18's review by broad, logistics and context). Either way one change; the fixing session picks one for both examples.
- Needs decision: no
- From: broad, logistics, context

### tender/19#F2 · High · Brackenmere's tender cites Valdara's qualification, issued a day later, and Valdara's reference evidence
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `/Tender/cac:TendererParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `13-TendererQualification.xml:/TendererQualification/cbc:IssueDate` = `2026-02-25`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`
- Why: `TendererQualificationDocumentReference` is "A reference to the tenderer qualification document that has been used to qualify the tenderer". `VI-DOC-26-0199` is Valdara's TendererQualification (13), signed by Valdara, issued on 2026-02-25, a day after this tender. The evidence `VI-REF-2025` carries Valdara's prefix and is the evidence Valdara's tender (15) cites, while Brackenmere's own numbers are `BF-…`; that it is Valdara's rests on the prefix and on 15 (logistics rated this part Medium). Brackenmere's own qualification in the flow is 07 (`BF-DOC-26-0193`, 2026-02-19). Same as in 17 (17#F2).
- Condition: The qualification and evidence references name documents of Brackenmere that exist at the tender's issue time, or are absent.
- Options: (a) `BF-DOC-26-0193` (a qualification application response, which a DocumentType can say) and an evidence document of Brackenmere (preferred); (b) remove the references; (c) add a TendererQualification of Brackenmere.
- Needs decision: no
- From: broad (two findings, F1 and F2), parties, logistics (qualification High with needs decision yes; evidence Medium), context

### tender/19#F3 · High · Five years of warranty on the frame in the line, six years on the frame in the criterion response
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: The line grants five years on the frame; the response to AC-2, which is scored in years (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`, maximum 10), offers six years on frame and slats. Both concern the frame of the same bench: the tender is scored on a warranty its own line does not grant. Same as in 17.
- Condition: The line's warranty and the warranty offered for AC-2 agree for the same component.
- Options: (a) six years on the line (text and period) (preferred); (b) five years in the response.
- Needs decision: no
- From: broad, logistics, context

### tender/19#F4 · High · Call for tenders referenced under an ID that no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The call for tenders of the flow is 03 (`LPWD-DOC-26-0189`); `PWD-2026-PARKS-CFT` occurs only inside reference elements, including in 03 itself (logistics), never as a document ID, while 25 cites the call by its document ID. The line reference `1` can only be resolved against `LPWD-DOC-26-0189`. 8 files of the flow carry the ID.
- Condition: Every reference to the call for tenders uses one identifier, the call's own.
- Options: (a) `LPWD-DOC-26-0189` (preferred); (b) make `PWD-2026-PARKS-CFT` the call's declared identifier and use it in the catalogue too.
- Needs decision: no
- From: broad (Medium), logistics (Medium); context listed it under "Outside this review"

### tender/19#F5 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID` and names no locale; the Urvanian parties carry none. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred by parties and context); (b) a locale such as `en-XB` from a locale list (preferred by broad).
- Needs decision: no
- From: broad, parties, context

### tender/19#F6 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The contracting party is a city department (ISIC 8411) with a liquidation status `ACTIVE` and a registration scheme of type `COMMERCIAL`. A department cannot be in liquidation, and a commercial register is not what a public body is in; a general register may list it, so the number itself is not questioned (parties).
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type (preferred); (b) drop `CorporateRegistrationScheme` for public bodies; (c) reduce the contracting party in tenders to identification and name (context).
- Needs decision: no
- From: broad, parties, context

### tender/19#F7 · Medium · The tendered price is given in the response to the quality criterion; the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `119040.00`
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:AwardingCriterionTypeCode` = `QUALITY`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:AwardingCriterionTypeCode` = `PRICE`
- Why: `Amount` "Specifies the monetary amount tendered for this awarding criterion". The response answers AC-2, the quality criterion (years); 119 040.00 is the tender total, which belongs to AC-1 ("The lowest total of unit prices.", range 350.00–600.00, i.e. a unit price), and there is no response to AC-1.
- Condition: The response to AC-2 carries no price; a price given as a criterion response is under AC-1, in the terms AC-1 evaluates.
- Options: (a) a response to AC-1 with the amount it evaluates, AC-2 with the years only (preferred); (b) drop the amount.
- Needs decision: no
- From: broad, money, context; logistics noted it under "Considered and refuted" as outside its lens

### tender/19#F8 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 1996-01-01 is given for 25 unrelated companies, 271 times in 181 examples (`grep -r --include='*.xml' 'RegistrationDate>1996-01-01'`), among them four of this flow: a default, not a fact of each company.
- Condition: Each company's registration date is its own, or absent.
- Options: (a) a date per company from its history (preferred); (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties (needs decision no)

### tender/19#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax": the party's status. The text begins "Sale to a public body", a transaction. Counter-argument (broad, refuted): the second half ("public bodies are exempt from the state sales tax") gives the status. The merge keeps the finding as in 15–18: the text mixes both, and the first half is what the code's name says. The code itself fits (list description: a public body "buys free of sales tax"); parties would prefer a status code.
- Condition: The party-level exemption reason states the party's status only.
- Options: (a) reword the text to the status, keeping the code (preferred, as the contest flow); (b) a party-status code.
- Needs decision: no
- From: parties (broad refuted it; context listed it under "Outside this review")

### tender/19#F10 · Low · Originator and beneficiary repeat the contracting party
- XPath: `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: Both roles hold the contracting party, by number and name only, and the tender does nothing with them (no fillers). Counter-arguments: UBL puts no "if different" condition on either role, and the department is the body that needs and uses the benches (parties); in procurement the originator is the customer for whom the procedure is run (broad). The merge keeps it as in 15 and 17: the values say nothing `ContractingParty` does not.
- Condition: The two roles are present only when they are another party (e.g. a parks service), or absent.
- Options: (a) remove both (preferred); (b) name the body that uses the benches, if the world has one.
- Needs decision: no
- From: context (broad and parties refuted it)

### tender/19#F11 · Low · The tenderer's own costs (paper copy, courier) as fees of the tendered project
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeTypeCode` = `COURIER`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: `FeeAmount` is "The fee amount for tendered projects", `AdditionalFee` "An additional fee for this tendered project". The 50 lume are the department's paper-copy charge in an electronic procedure, the 12 lume the tenderer's courier cost; neither is offered or in the total (115 200.00 + 3 840.00 = 119 040.00). The same values are in 15 and 17, so Brackenmere states them twice.
- Condition: The tendered project carries a fee only if it is part of what is offered or owed under the tender.
- Options: (a) remove both (preferred); (b) keep the documentation fee only where the story says this tenderer bought the paper copy, as proof of payment.
- Needs decision: no
- From: broad (needs decision yes, for the guarantee), money, context (needs decision yes)

### tender/19#F12 · Low · No guarantee of Brackenmere in the flow, and the tender cites none
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:InterestedParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The terms require a tender guarantee of 2400.00 lume by the deadline; this tender mentions one only in the courier fee, cites none, and the only certificate of the flow (14) is Valdara's. Whether Brackenmere provided a guarantee at all is a story question (broad).
- Condition: The tender references the guarantee that covers it, and that guarantee exists in the flow (or the story says it is not shown).
- Options: (a) add a guarantee certificate of Brackenmere and cite it (preferred); (b) drop the courier fee and record that the guarantee is outside the examples.
- Needs decision: yes
- From: broad, money, context (each in its fee finding)

### tender/19#F13 · Low · No unit prices, although the procedure evaluates and auctions unit prices
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `115200.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `3840.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cac:DocumentTenderRequirement/cbc:Description` = `Unit prices per lot.`
- Why: The terms evaluate unit prices (`PriceEvaluationCode` UNITPRICE) and ask for "Unit prices per lot"; the tender gives line totals only. Counter-argument (money in this example, refuted): quantity and line amount give the unit price exactly (480.00). The merge keeps it as money's own finding in 15 and 17 did: a price the procedure evaluates and auctions should be stated, not derived, and `OfferedItemLocationQuantity` can hold it.
- Condition: Each tender line states its unit price, and quantity × unit price equals the line amount.
- Options: (a) a price in `OfferedItemLocationQuantity` of both lines (preferred); (b) reference the price schedule.
- Needs decision: no
- From: merge (money considered and refuted it here; found it in 15 and 17)

### tender/19#F14 · Low · A tax total of zero that names no tax
- XPath: `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TotalTaxAmount` = `0.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`
- Why: `TaxAmount` is "the sum of the tax subtotals for each tax category within the taxation scheme"; the tender states zero twice but names neither scheme nor category. The call gives the basis (state sales tax, category E, reason PUBLIC), and the tenderer is a Bayvarran seller under that tax. Counter-argument (context, refuted for its lens): the amount states the consequence of the exemption.
- Condition: The zero is tied to a scheme and category with its exemption reason (a `TaxSubtotal`), or the tender makes no tax statement.
- Options: (a) a `TaxSubtotal` with taxable amount 119040.00, category E, reason PUBLIC, scheme STT (preferred); (b) drop the tax amounts.
- Needs decision: no
- From: money (context refuted it for its lens)

### tender/19#F15 · Low · Replacement item that reads as a spare part, identified only by a number
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:Quantity` = `1`
- Why: `ReplacementRelatedItem` is "A catalogue item that may be a replacement for the item described in this tender line". By its ID `BF-SLAT-PB2` is a slat of the PB-2, a spare part, which cannot replace a bench (one slat for one bench); it has no name or description and occurs only in 17 and 19. If the reading holds, the element carries another meaning than its definition (Medium, broad and context); but it rests on the identifier alone, and if the item is an alternative bench the finding falls (context). Hence Low with a decision.
- Condition: The item under `ReplacementRelatedItem` can be supplied instead of the bench and is described, or the element is absent.
- Options: (a) remove it and mention spare slats in the line note (preferred); (b) name and describe a real substitute bench.
- Needs decision: yes
- From: broad (Medium), logistics (Low), context (Medium, needs decision yes)

### tender/19#F16 · Low · One tendered project and one total for two lots
- XPath: `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[1]/cbc:ID` = `LOT-1`
- XPath: `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]/cbc:ID` = `LOT-2`
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cac:Item/cbc:Name` = `Installation of a park bench`
- Why: `TenderedProject` is "A project with which this Tender is associated. A single Tender can be used to bid for one project, multiple projects, or the global project". The call has two lots and asks for "Unit prices per lot."; the tender puts both into one project with one total, warranty and criterion response, and which line belongs to which lot follows only from the item names (line 2 has no call-for-tenders line reference). Counter-argument (broad, in 15, refuted): the definition allows one project for several, and the lines keep the lots apart. Whether lots can be tendered and awarded separately is a story question.
- Condition: The amount tendered for each lot can be read without interpreting item names (one tendered project per lot, or the lot stated per line).
- Options: (a) one `TenderedProject` per lot (preferred); (b) keep one project if the procedure only allows a tender for both lots together, and say so in the call.
- Needs decision: yes
- From: context

### tender/19#F17 · Low · References with only an ID: the data sheet
- XPath: `/Tender/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`
- Why: `DocumentReference` is the generic "A reference to another document associated with this document"; with only an ID the reader must guess that this is the data sheet of the PB-2, and the document is not in the flow (only 17 and 19 carry the ID). Counter-argument (broad here, logistics in 17): next to the item on line 1 it reads as the data sheet. The merge keeps it, as the earlier flows' decision on ID-only references (Low/no).
- Condition: The reference states the kind of document.
- Options: (a) add `cbc:DocumentType` "Data sheet" or a type code (preferred).
- Needs decision: no
- From: logistics (broad refuted it)

### tender/19#F18 · Low · Signature identifier carries the example's file number
- XPath: `/Tender/cac:Signature/cbc:ID` = `BF-SIG-TENDER-19`
- XPath: `17-Tender.xml:/Tender/cac:Signature/cbc:ID` = `BF-SIG-TENDER-17`
- Why: `Signature/ID` is "An identifier for this signature", assigned by the signer. The suffix is the example's position in the flow's file numbering; Brackenmere has no reason to number its second tender "19". The other signatures of the flow carry business names (`BF-SIG-WD`, `PWD-SIG-RCPT`).
- Condition: The signature ID does not depend on the example's file number.
- Options: (a) derive it from the document number, e.g. `BF-SIG-0205` (preferred).
- Needs decision: no
- From: logistics

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit (GS1 prefix 952, for examples).
- Arithmetic, recalculated: 240 × 480.00 = 115 200.00; 240 × 16.00 = 3 840.00; sum 119 040.00 = `LineExtensionAmount` = `PayableAmount`; tax 0.00; line 1 tax-inclusive 115 200.00. Against 17 only the bench price changed (470.00 → 480.00), as the note says (diff of the two tenders by money and context).
- 119 040.00 is below the winning 124 080.00 (22), consistent with 23 ("lower in price").
- Against the call: 240 EA and 240 SET (line 1, sub-line 1.1), line reference 1, lots LOT-1/LOT-2, envelope `ENV-1` / `COMBINED`, validity 90 days, lead time 7 days (≤ 10), 6 years within 5–10, `AC-2.1` exists; issued before the deadline and after 03 and 07.
- Ordering: pallet of 4, increment 4, minimum 20, maximum 96; 240 = 60 pallets.
- Brackenmere and the department are described as in the other examples of the flow (register numbers 20412466 and 20410548; parties, by script); `CompanyID` = `PartyIdentification`, electronic address = country prefix + number, tax scheme fits the country; contacts fit their roles (parties).

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity`: 96 less than 240 — refuted, a framework with releases; the maximum is per order (from broad, logistics, context).
- `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: reads as a transaction — refuted because the text gives the status (from broad; the merge disagrees, see F9).
- `/Tender/cac:TendererParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` not ISO 8601 — refuted, free text and the same form everywhere (from broad, parties).
- `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the authority as originator — refuted, the customer for whom the procedure is run (from broad; the merge keeps the repetition as F10).
- `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` and `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: fillers — refuted, no "if different" condition (from parties; see F10).
- `/Tender/cac:TendererParty/cac:Contact/cbc:JobTitle`: a sales desk for a public tender — refuted, plausible for a small maker (from broad).
- `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription`: "Warranty and coating." vs "Quality" — refuted, it describes what AC-2 measures (from broad).
- `/Tender/cac:DocumentReference/cbc:ID`: only an ID — refuted, on line 1 it reads as the data sheet (from broad; the merge keeps it as F17).
- `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount`: no tax-inclusive amount on line 2 — refuted as a finding of its own; covered by F14 (from money).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount`: no unit price — refuted, quantity and amount give it (from money; the merge disagrees, see F13).
- `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: fees not in the payable amount — refuted, they are not part of the price; see F11 (from money).
- `/Tender/cac:TendererParty/cac:Contact/cbc:Telephone`: +999 real — refuted, unassigned (from parties).
- `/Tender/cac:TendererParty/cac:AdditionalPartyIdentification/cbc:ID`: a real GLN — refuted, prefix 952 is for examples (from parties).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyParty/cac:PartyName/cbc:Name`: a small maker as sole warranty party — refuted, it makes the bench (from parties, context).
- `/Tender/cac:TenderedProject/cac:TenderLine[2]`: no call-for-tenders line reference — refuted, 03 has no line for the installation (from logistics).
- `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount`: total under AC-2 — not kept by logistics as outside its lens (from logistics; finding F7).
- `/Tender/cac:TenderedProject/cbc:VariantID`: `V0` — refuted, names the base offer (from logistics, context).
- `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount`: zero without subtotal — refuted for the context lens (from context; finding F14).
- `/Tender/cac:Signature`: only an ID and a signatory — refuted, the definition asks no more (from context).

## Changed in the merge
- broad/F1 + F2, parties/F1, logistics/F2 + F4, context/F1 → F2: one finding (Valdara's documents in Brackenmere's tender), as in 17; logistics' needs decision yes set to no.
- broad/F7 (Medium), logistics/F5 (Medium) → F4: raised to High, as in 15 and 17 and the other tender merges (a reference that resolves to no document).
- broad/F10, parties/F5, context/F10 → F6: raised to Medium, as analysis/review-merge-decisions.md.
- parties/F3 → F8: needs decision yes, as every earlier flow.
- broad/F9, money/F2, context/F7 split into F11 (fees, Low/no) and F12 (missing guarantee, Low/yes), as in 17.
- broad/F6 (Medium), context/F6 (Medium/yes), logistics/F7 (Low) → F15: Low/yes, because it rests on reading the identifier; 17#F15 rated the same way.
- F13 made a finding from money's refutation, to stay consistent with money's own findings in 15 and 17.
- F17 kept as a finding against broad's refutation, as the earlier flows' decision on ID-only references.

## Outside this review
- 18 cites a tender receipt `PWD-RCPT-BF-1` that is not in the flow; there is no receipt for this tender either (from logistics; finding of 18).
- 03 estimates the contract at exactly Valdara's tender amounts; a matter for 03 and 15 (from broad).
