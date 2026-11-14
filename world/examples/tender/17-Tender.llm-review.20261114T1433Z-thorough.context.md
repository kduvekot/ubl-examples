# LLM review: 17-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/17-Tender.xml`, Git blob `ea8d3a233b928425f6a062a240c2497a8e4da8a4` (committed)
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

### tender/17#F1 · High · Reference to a call for tenders under an ID that no example carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The call for tenders this document answers is cited as `PWD-2026-PARKS-CFT`. No example has that document ID: the call for tenders of the procedure is `03-CallForTenders.xml` with the ID `LPWD-DOC-26-0189`, and the catalogue (25) refers to it by that ID. The tender cites it twice, at document level and on line 1. The unresolved ID is used in 8 examples of the flow (`grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`).
- Condition: Every reference to the call for tenders resolves to the document ID of `03-CallForTenders.xml`.
- Options: (a) Preferred: `LPWD-DOC-26-0189` here and in the other examples. (b) Give 03 the ID `PWD-2026-PARKS-CFT` and change the catalogue. Either way one ID in the whole flow.
- Needs decision: no

### tender/17#F2 · High · The tender of Brackenmere cites the qualification and the reference of its competitor Valdara
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- XPath: `/Tender/cac:TendererParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `13-TendererQualification.xml:/TendererQualification/cbc:ID` = `VI-DOC-26-0199`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`
- XPath: `13-TendererQualification.xml:/TendererQualification/cbc:IssueDate` = `2026-02-25`
- XPath: `/Tender/cbc:IssueDate` = `2026-02-23`
- Why: `TendererQualificationDocumentReference` is "a reference to the tenderer qualification document that has been used to qualify the tenderer". `VI-DOC-26-0199` is the qualification of Valdara Industries (13), a different tenderer and the competitor; it is also dated 2026-02-25, two days after this tender, so it did not exist when the tender was issued. Brackenmere's own qualification document in the flow is its qualification application response (07, `BF-DOC-26-0193`). The evidence reference `VI-REF-2025` carries Valdara's prefix as well and is the same ID as in Valdara's tender (15). Both values are Valdara's, copied into Brackenmere's tender. The same occurs in 19.
- Condition: The tender refers to a qualification document and to evidence of the tenderer itself, issued before the tender.
- Options: (a) Preferred: `BF-DOC-26-0193` as qualification reference and an evidence document of Brackenmere's own. (b) Add a tenderer qualification of Brackenmere to the flow and refer to it.
- Needs decision: no

### tender/17#F3 · High · Five years of warranty on the frame in the line, six years on the frame in the criterion response
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: The tender line says "Five years on the frame." with a warranty validity of 5 years. The response to the quality criterion, which is scored on years, offers "Six years on the frame and the slats." with a quantity of 6 years. The same tender gives two different warranty periods for the frame; the department cannot tell which one is offered and scored. (In Valdara's tender the line text is the same, but the criterion response is about another thing, the coating.)
- Condition: The warranty stated in the tender line and the one offered in the criterion response are the same for the same component.
- Options: (a) Preferred: six years in the line (information and validity period). (b) Five years in the response, which lowers the quality score.
- Needs decision: no

### tender/17#F4 · Medium · The tendered price is given in the response to the quality criterion, and the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `116640.00`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`
- Why: `AwardingCriterionResponse/Amount` "specifies the monetary amount tendered for this awarding criterion". The response refers to `AC-2`, defined in the call for tenders as "Quality" (in years); it carries the years and also 116640.00 lume, the total price of the tender. The price belongs to criterion `AC-1` ("Price"), for which there is no response.
- Condition: The amount is in a response to the price criterion; the response to the quality criterion carries the years only.
- Options: (a) Preferred: a response to `AC-1` with the amount, and `AC-2` with the years. (b) Remove the amount; the monetary total states the price.
- Needs decision: no

### tender/17#F5 · Medium · A language code in `LocaleCode`
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/17#F6 · Low · A courier fee for "the guarantee's original" in the tender of a tenderer without a guarantee, and the paper-copy fee
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:InterestedParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: As in 15, the tendered project lists what the tenderer spent to take part (50.00 for paper copies, 12.00 for a courier); `FeeAmount` is "the fee amount for tendered projects", not the tenderer's expenses, and the total of 116640.00 does not include them. Here the courier fee is also for a guarantee that the flow does not contain: the only guarantee certificate (14) is Valdara's. The two fees and their texts are identical to those of Valdara's tender.
- Condition: The tendered project carries a fee only if it is part of what is offered or owed; a fee that refers to a guarantee presupposes one.
- Options: (a) Preferred: remove both fees. (b) Add a guarantee certificate for Brackenmere to the flow and cite it in the tender.
- Needs decision: no

### tender/17#F7 · Low · Commercial terms identical to the competitor's tender, and a replacement item that nothing describes
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:OrderableUnit` = `Pallet of 4`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity` = `96`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity` = `96`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`
- Why: Brackenmere offers "a bench of its own make", from another plant in another country than Valdara's. Its pallet size (4), order increment, minimum (20) and maximum (96) order quantity, pack level, lead time (7 days) and warranty text are nevertheless the same as in Valdara's tender (15), value for value; only prices, names and the criterion response differ. Two independent makers do not share all logistics parameters. The replacement item `BF-SLAT-PB2` has an ID only; by its name it is a slat, which cannot replace a bench, and the ID occurs only in 17 and 19.
- Condition: The commercial terms are Brackenmere's own (they may coincide in single values, not in all), and a replacement item is described or absent.
- Options: (a) Preferred: own values for packing, order quantities and lead time; remove the replacement item. (b) Keep the values and say that the call for tenders prescribes them (it does not, in 03).
- Needs decision: no

### tender/17#F8 · Low · A tender for both lots from an operator whose qualification exchange covers lot 1 only
- XPath: `/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make.`
- XPath: `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]/cbc:ID` = `LOT-2`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- Why: The tender is "for both lots". The qualification application the department sent to Brackenmere (06) and its response (07) name lot 1 only, and their criterion applies to lot 1 and to the classification of seats. For lot 2 (installation) the operator has stated no qualification, and it names no subcontractor for it.
- Condition: The lots tendered for are the lots the tenderer has qualified for.
- Options: (a) Preferred: extend 06 and 07 to both lots. (b) Tender for lot 1 only.
- Needs decision: no

### tender/17#F9 · Low · Originator and beneficiary repeat the contracting party
- XPath: `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The tender names the department three times: as contracting party, as `OriginatorCustomerParty` ("the party originating the Tender") and as `BeneficiaryParty` ("a Party for whom the associated transaction is ultimately intended or who derives benefit from it"). The two extra roles exist for the case that another body asked for or will use the purchase; here they add nothing to `ContractingParty`, and a tenderer has no knowledge of its own about who originated the procedure.
- Condition: Originator and beneficiary are present only where they are a party other than the contracting party.
- Options: (a) Preferred: remove both. (b) Name the parks service as beneficiary, if it is a body of its own in the world.
- Needs decision: no

### tender/17#F10 · Low · Customs trader numbers of the parties in a tender
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. A tender is not declared to customs. They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- Arithmetic: 112800.00 (240 × 470.00) + 3840.00 (240 × 16.00) = 116640.00 = `PayableAmount`; unit price within the bounds 350–600 of the price criterion.
- The withdrawal (18) refers to this tender by its ID and gives the reason (price per bench entered wrongly); the tender 19 has the corrected line amount 115200.00 (240 × 480.00) and says it corrects the withdrawn tender.
- Validity 90 days, envelope `ENV-1`/`COMBINED` and the line reference `1` agree with 03; issued 2026-02-23, before the deadline.
- GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/Tender/cac:TenderedProject/cbc:VariantID` = `V0`: suspected to call the base tender a variant — refuted as in 15.
- `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription` = "Warranty and coating." for a response that offers no coating warranty: suspected mismatch — refuted, it describes the criterion, not the response, and the sub-response describes the finish.
- A price below Valdara's (116640.00 against 124080.00) from the tenderer that later loses: suspected contradiction with the award — refuted here, this tender is withdrawn and the award depends on quality scores and an auction; it is a question for 21–23.

## Outside this review
- No tender receipt for this tender exists in the flow, though 18 cites one; no guarantee certificate of Brackenmere exists. Gaps of the flow.
- The same wrong qualification and evidence references are in 19.
