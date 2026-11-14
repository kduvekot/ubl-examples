# LLM review: 17-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/17-Tender.xml`, Git blob `ea8d3a233b928425f6a062a240c2497a8e4da8a4` (committed)
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

### tender/17#F1 · High · Call for tenders referenced under an ID that no document carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTenderDocumentReference` is "A reference to the call for tender document of which this tender result of". The call for tenders is 03-CallForTenders.xml, ID `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`, and the catalogue (25) cites the call by `LPWD-DOC-26-0189`. The ID occurs in 8 files of the flow (01, 02, 03, 06, 15, 17, 19, 24; `grep -l` over `tender/*.xml`, re-checked).
- Condition: Every reference to the call for tenders carries the document ID of 03, one ID in the whole flow.
- Options: (a) `LPWD-DOC-26-0189` (preferred); (b) give 03 the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no
- From: broad, logistics, context

### tender/17#F2 · High · Brackenmere's tender cites Valdara's qualification, issued two days later, and Valdara's reference evidence
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `/Tender/cac:TendererParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/Tender/cbc:IssueDate` = `2026-02-23`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `13-TendererQualification.xml:/TendererQualification/cbc:IssueDate` = `2026-02-25`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`
- Why: `TendererQualificationDocumentReference` is "A reference to the tenderer qualification document that has been used to qualify the tenderer". `VI-DOC-26-0199` is 13, the qualification of the competitor Valdara Industries, issued on 2026-02-25, two days after this tender: Brackenmere could neither have been qualified by it nor known its number. The evidence `VI-REF-2025` (`EvidenceDocumentReference`, "A reference to a non-structured evidentiary document supporting this tendered project") carries Valdara's prefix and is the same ID as in Valdara's tender 15, while every other number in this tender is Brackenmere's (`BF-DS-PARK`, `BF-SLAT-PB2`); that it is Valdara's document rests on the prefix and on 15, so this part alone would be Medium (logistics). Brackenmere's own qualification in the flow is 07 (`BF-DOC-26-0193`, 2026-02-19). The same two values are in 19.
- Condition: The qualification and evidence the tender refers to are the tenderer's own and exist before the tender.
- Options: (a) refer to `BF-DOC-26-0193` and to an evidence document of Brackenmere (preferred; 07 is a qualification application response rather than a TendererQualification, which the fixing session should weigh); (b) remove the references Brackenmere has no document for; (c) add a TendererQualification of Brackenmere to the flow.
- Needs decision: no
- From: broad, parties, logistics (qualification: High, needs decision yes; evidence: separate Medium), context

### tender/17#F3 · High · Five years of warranty on the frame in the line, six years on the frame in the criterion response
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: The tender line offers five years on the frame (text and `WarrantyValidityPeriod` 5 ANN); the response to the quality criterion, which is scored in years, offers six years "on the frame and the slats". Both are about the frame of the same bench, so the tender contradicts itself and the department cannot tell which warranty it scores. In Valdara's tender (15) the same line text does not collide, because its response concerns the coating; the line text looks carried over.
- Condition: The warranty on the tender line and the warranty offered in the criterion response agree for the same component.
- Options: (a) six years on the line (text and period) (preferred: the response is what is evaluated); (b) five years in the response, which lowers the score.
- Needs decision: no
- From: broad, logistics, context

### tender/17#F4 · Medium · Language code in LocaleCode
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID` and names no locale. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad, parties, logistics, context

### tender/17#F5 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The Lumeport Public Works Department (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411) carries a liquidation status `ACTIVE` and a registration scheme of type `COMMERCIAL` ("A register of businesses"). A city department is not a business and cannot be in liquidation. Same in all 36 examples of the flow.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies (preferred); (b) a register type for public bodies; (c) state in the world's rules that public bodies are entered in the federal business register.
- Needs decision: no
- From: broad, parties

### tender/17#F6 · Medium · The tendered price is given in the response to the quality criterion; the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `116640.00`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- Why: `Amount` "Specifies the monetary amount tendered for this awarding criterion". The response is to `AC-2`, the quality criterion (years, 5 to 10); 116 640.00 lume is the total price, which the price criterion `AC-1` ("The lowest total of unit prices.") scores, and `AC-1` has no response. Under AC-1 the answer would be unit prices (470.00 and 16.00).
- Condition: Each response carries only what was tendered for its criterion: the price under AC-1, the years under AC-2.
- Options: (a) a response to `AC-1` with the amount or the unit prices, `AC-2` with the years only (preferred); (b) drop the amount.
- Needs decision: no
- From: broad, money, logistics (Low), context

### tender/17#F7 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 1996-01-01 is given for 25 unrelated parties in three countries, 271 times in 181 examples (`grep -r --include='*.xml' 'RegistrationDate>1996-01-01'`): a default, not a fact of each company. The flow uses registration against operating years.
- Condition: Each party's registration date is its own, or absent where the world has none.
- Options: (a) a registration date per company from its history (preferred); (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties (needs decision no)

### tender/17#F8 · Low · Customs trader number of the department in a tender
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Section 4.8: the customs trader number identifies the department towards customs (used in 30, 31); a tender declares nothing to customs.
- Condition: Each party carries only the identifiers the tender uses.
- Options: (a) leave customs trader numbers to the customs and transport documents (preferred); (b) state a world rule that every document carries all identifiers.
- Needs decision: no
- From: parties, context

### tender/17#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" describes a transaction; the code `PUBLIC` fits (list description: a public body "buys free of sales tax"); broad would prefer a party-status code.
- Condition: The party's exemption reason states its status.
- Options: (a) reword the text, keeping the code (preferred); (b) a party-status code.
- Needs decision: no
- From: broad, parties

### tender/17#F10 · Low · Originator and beneficiary repeat the contracting party
- XPath: `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The two roles name the department by register number and name only, adding nothing to `ContractingParty` (no fillers). Counter-argument (broad, refuted as in 15): the originator customer is the customer for whom the tendering was started; even so, the value repeats the contracting party.
- Condition: Originator and beneficiary are present only where they name another party or add role-specific detail.
- Options: (a) remove both (preferred); (b) name the parks service as beneficiary if it is a body of its own.
- Needs decision: no
- From: parties, context

### tender/17#F11 · Low · The tenderer's own costs (paper copy, courier) as fees of the tendered project, copied from Valdara's tender
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: `FeeAmount` is "The fee amount for tendered projects", `AdditionalFee` "An additional fee for this tendered project". As in 15, the amounts are what the tenderer spent to take part (a paper copy of electronic documents, a courier), not part of the offer or the total (116 640.00 is the sum of the lines). They are identical to Valdara's, and appear again in the corrected tender 19, as if incurred twice (money). The courier fee also concerns a guarantee that the flow does not contain for Brackenmere (F12).
- Condition: The tendered project carries a fee only if it is part of what is offered or owed under the tender.
- Options: (a) remove both fees (preferred); (b) keep the documentation fee only where the story says this tenderer bought the paper copy.
- Needs decision: no
- From: broad, money (needs decision yes), context

### tender/17#F12 · Low · No guarantee of Brackenmere in the flow, and the tender cites none
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:InterestedParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The terms require a tender guarantee of 2400.00 lume constituted by the deadline (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`). The tender mentions a guarantee only in the courier fee; its references name no guarantee, and the only certificate in the flow (14) is Valdara's. A buyer checking admissibility cannot link this tender to a guarantee.
- Condition: The tender references the guarantee that covers it, and that guarantee exists in the flow (or the story says Brackenmere's guarantee is not shown).
- Options: (a) add a guarantee certificate of Brackenmere and cite it (preferred by money and context); (b) drop the courier fee and record in the story that the guarantee is outside the examples.
- Needs decision: yes
- From: money, broad (in its fee finding), context (in its fee finding); logistics listed it under "Outside this review"

### tender/17#F13 · Low · No unit prices, although the procedure evaluates and auctions unit prices
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:Quantity` = `240`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `112800.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `3840.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:PriceEvaluationCode` = `UNITPRICE`
- Why: The terms evaluate and auction unit prices and ask for "Unit prices per lot"; the tender gives line totals only (470.00 and 16.00 must be worked out), although `OfferedItemLocationQuantity` (used for the lead time) can hold a price.
- Condition: Each tender line states its unit price, and quantity × unit price equals the line amount.
- Options: (a) a price in `OfferedItemLocationQuantity` of both lines (preferred); (b) reference the price schedule.
- Needs decision: no
- From: money

### tender/17#F14 · Low · A tax total of zero that names no tax
- XPath: `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TotalTaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `112800.00`
- Why: `TaxAmount` is "the sum of the tax subtotals for each tax category within the taxation scheme"; there is no subtotal, so neither scheme nor reason for zero is stated. For a Bayvarran tenderer the exemption of sales to public bodies from the state sales tax would apply; the tender does not say so. Line 1 carries zero and a tax-inclusive amount, line 2 neither.
- Condition: The tax total states scheme, category and exemption reason, and both lines treat tax alike; or there is no tax total.
- Options: (a) one tax subtotal with category and exemption reason (preferred); (b) drop the zero amounts.
- Needs decision: no
- From: money

### tender/17#F15 · Low · Replacement item that reads as a spare part, identified only by a number
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:Item/cbc:Name` = `Park bench Brackenmere PB-2`
- Why: `ReplacementRelatedItem` is "A catalogue item that may be a replacement for the item described in this tender line", an item supplied instead of the bench. `BF-SLAT-PB2` reads as a slat of the PB-2, a spare part, not a substitute; it has no name or description and occurs only in 17 and 19 (`grep -rl --include='*.xml'`). The reading rests on the identifier alone; if the item is an alternative bench, only the missing description remains (as 19#F15).
- Condition: A replacement item can take the place of the tendered item and is described; a spare part is left out (the TenderLine has no element for parts).
- Options: (a) remove it and mention spare slats in the line note (preferred); (b) name and describe a real alternative bench.
- Needs decision: yes
- From: broad, logistics, context

### tender/17#F16 · Low · Ordering and logistics terms identical to the competitor's tender
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:OrderableUnit` = `Pallet of 4`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity` = `96`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity` = `96`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`
- Why: Brackenmere offers "a bench of the furniture maker's own make" from another plant in another country, yet pallet size, increment, minimum and maximum order quantity, pack level, lead time and warranty text are value for value those of Valdara's tender (15); two independent makers do not share all of them (context). Counter-argument (broad, refuted): the same ordering terms for a bench of the same size are possible. The merge cannot settle a plausibility question of this kind: Low, with a decision.
- Condition: The terms are Brackenmere's own (single values may coincide), or the call prescribes them.
- Options: (a) own values for packing, order quantities and lead time (preferred by context); (b) keep them as a deliberate coincidence.
- Needs decision: yes
- From: context (broad refuted it)

### tender/17#F17 · Low · A tender for both lots from an operator whose qualification exchange covers lot 1 only
- XPath: `/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make.`
- XPath: `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]/cbc:ID` = `LOT-2`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- Why: The qualification application sent to Brackenmere (06) and its response (07) name lot 1 only; for lot 2 (installation) Brackenmere has stated no qualification and names no subcontractor. Counter-argument (broad, refuted): the notice lets a tenderer submit for one or more lots. That answers whether it may tender for both, not whether it qualified for lot 2, so the merge keeps the finding.
- Condition: The lots tendered for are lots the tenderer qualified for.
- Options: (a) extend 06 and 07 to both lots (preferred); (b) tender for lot 1 only.
- Needs decision: no
- From: context (broad refuted it)

### tender/17#F18 · Low · References with only an ID: the data sheet
- XPath: `/Tender/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:DocumentReference/cbc:ID` = `BF-DS-PARK`
- Why: The generic `DocumentReference` ("A reference to another document associated with this document") has only an ID; the reader must guess that it is the PB-2's data sheet, which is not in the flow (only 17 and 19 carry the ID). Counter-argument (logistics here, broad in 19): next to the item on line 1 it reads as the data sheet. Added by the merge to match 19#F17 (logistics raised it there) and the earlier flows' decision on ID-only references.
- Condition: The reference states the kind of document.
- Options: (a) add `cbc:DocumentType` "Data sheet" or a type code (preferred).
- Needs decision: no
- From: merge (logistics considered and refuted it here; logistics found it in 19)

### tender/17#F19 · Low · Signature identifier carries the example's file number
- XPath: `/Tender/cac:Signature/cbc:ID` = `BF-SIG-TENDER-17`
- Why: `Signature/ID` is "An identifier for this signature", assigned by the signer; the suffix is the example's position in the flow's file numbering, not a number of Brackenmere's. Added by the merge to match 19#F18 (logistics).
- Condition: The signature ID does not depend on the example's file number.
- Options: (a) derive it from the document number, e.g. `BF-SIG-0203` (preferred).
- Needs decision: no
- From: merge (raised by logistics in 19)

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit (GS1 prefix 952, for examples).
- Arithmetic, recalculated: 112 800.00 / 240 = 470.00 (within 350.00–600.00); 3 840.00 / 240 = 16.00; 112 800.00 + 3 840.00 = 116 640.00 = `LineExtensionAmount` = `PayableAmount`; tax 0.00.
- Against the call: 240 EA and 240 anchor sets, line reference 1, sub-line 1.1, envelope `ENV-1` / `COMBINED`, validity 90 days, lead time 7 days (≤ 10), quality response 6 years (5–10), `AC-2.1` exists.
- Issued 2026-02-23 16:37, after 07 (2026-02-19) and 08/09, before the deadline 2026-02-26 12:00; `BF-DOC-26-0203` follows `BF-DOC-26-0194`; 18 withdraws it by its ID; 19 repeats it with 480.00 a bench (115 200.00 / 240), all else equal.
- `DocumentReference` `BF-DS-PARK` used consistently at document and line level (and in 19).
- Brackenmere's declared turnover of 410 000.00 (07) is above the required 250 000.00; ISIC 3100 and 8411 fit; +999 unassigned; `.example` addresses.

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:OrderableUnit`: same ordering terms as Valdara — refuted, possible for a bench of the same size (from broad; the merge keeps it as F16, Low/yes).
- `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]`: lot 2 although the qualification request concerned lot 1 — refuted, the notice allows one or more lots (from broad; the merge keeps the qualification side as F17).
- `/Tender/cac:OriginatorCustomerParty`: the department as originator — refuted as in 15 (from broad; see F10).
- `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: abnormally low tender ("30 % below the average are examined") — refuted, 6 % below 124 080.00 (from money).
- `/Tender/cac:TendererParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` invalid — refuted, no format prescribed (from parties).
- `/Tender/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: belongs in `Room` — refuted (from parties).
- `/Tender/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: functional name, two department wordings — refuted (from parties).
- `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: `STATE` vs local authority — refuted, the level of the tax (from parties).
- `/Tender/cac:TendererParty/cac:Contact`: `Trade sales` in a procurement procedure — refuted, for a small maker the sales office answers tenders; name, title and department agree (from parties).
- `/Tender/cac:DocumentReference/cbc:ID`: ID only, resolving nowhere — refuted, next to the item it is the bench's data sheet (from logistics; the merge keeps it as F18, as in 19).
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount`: price "entered wrongly" (18) — refuted, that is the story; corrected in 19 (from logistics).
- `/Tender/cac:TenderedProject/cbc:VariantID`: `V0` — refuted as in 15 (from context).
- `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription`: "Warranty and coating." without a coating warranty — refuted, it describes the criterion (from context).
- `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: lower than Valdara's although Brackenmere loses — refuted here; the tender is withdrawn and the award rests on quality and an auction (from context; see 21–23).

## Changed in the merge
- broad/F1, parties/F1, context/F2 and logistics/F1 + F4 → F2: one finding; logistics' separate Medium for the evidence reference folded in (same problem: Valdara's documents in Brackenmere's tender), its weaker basis stated in Why; logistics' needs decision yes set to no (preferred options are encoding).
- broad/F8, parties/F6 → F5: raised to Medium, as analysis/review-merge-decisions.md and the other tender merges.
- logistics/F7 (Low) → F6: Medium, as the other parts.
- parties/F3 → F7: needs decision yes, as every earlier flow.
- money/F5 and the guarantee parts of broad/F6 and context/F6 → F12 (Low/yes: adding a document changes the flow); the fee parts → F11 (Low/no; money's yes not followed, as in 15).
- context/F7 split into F15 (replacement item, with broad/F7, logistics/F6) and F16 (identical terms, Low/yes because broad refuted it and the merge cannot settle it).
- F15: needs decision yes, because the spare-part reading rests on the identifier alone (aligned with 19#F15).
- F18, F19 added by the merge (appended, no renumbering) to match what logistics raised in 19.

## Outside this review
- Brackenmere's tender is lower than Valdara's (116 640.00, after correction 119 040.00, against 124 080.00); how the award follows belongs to 21–23 (from broad, context).
- No tender receipt for this tender exists, although 18 cites one; see 18 (from broad, context).
- The terms do not allow multiple tenders (`MultipleTendersCode` NOTALLOWED in 01–03); this tender is withdrawn (18, 2026-02-24 17:56) after the second tender (19, 2026-02-24 12:10) was issued; reported with 18 (from logistics).
- Whether the fees of this tender and of 19 are one payment or two is a question across the two documents (from money).
