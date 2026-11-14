# LLM review: 15-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/15-Tender.xml`, Git blob `a052a0ed15639e25ddae372a37b1960f7b6a9857` (committed)
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

### tender/15#F1 · High · Reference to a call for tenders under an ID that no example carries
- XPath: `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: The call for tenders this document answers is cited as `PWD-2026-PARKS-CFT`. No example has that document ID: the call for tenders of the procedure is `03-CallForTenders.xml` with the ID `LPWD-DOC-26-0189`, and the catalogue (25) refers to it by that ID. The tender cites it twice, at document level ("the call for tender document of which this tender result of") and on line 1, whose line reference `1` does exist in 03. The unresolved ID is used in 8 examples of the flow (`grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`).
- Condition: Every reference to the call for tenders resolves to the document ID of `03-CallForTenders.xml`.
- Options: (a) Preferred: `LPWD-DOC-26-0189` here and in the other examples. (b) Give 03 the ID `PWD-2026-PARKS-CFT` and change the catalogue. Either way one ID in the whole flow.
- Needs decision: no

### tender/15#F2 · Medium · The tendered price is given in the response to the quality criterion, and the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription` = `Warranty and coating.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `124080.00`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `10`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Ten years on the coating.`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`
- Why: `AwardingCriterionResponse/Amount` "specifies the monetary amount tendered for this awarding criterion". The response refers to `AC-2`, which the call for tenders defines as "Quality" (measured in years, 5 to 10); the tender answers it with 10 years, and with 124080.00 lume, the total price of the tender. The price belongs to criterion `AC-1` ("Price", 60 %), for which the tender has no response at all. An evaluator reading the responses finds an amount under quality and nothing under price.
- Condition: Each awarding criterion of the call for tenders that the tender addresses has its own response, with the amount under the price criterion and the quantity under the quality criterion.
- Options: (a) Preferred: a response to `AC-1` with the amount (or the unit prices), and the response to `AC-2` with the years only. (b) Remove the amount; the monetary total already states the price.
- Needs decision: no

### tender/15#F3 · Medium · A language code in `LocaleCode`
- XPath: `/Tender/cac:SubcontractorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/15#F4 · Low · The tender prices both lots exactly at the buyer's estimate
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `119760.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: The tender's amounts are, to the cent, the estimates the department published: 119760.00 for lot 1 (240 × 499.00), 4320.00 for lot 2 (240 × 18.00), 124080.00 in total. A tenderer in a price competition with an auction to follow does not arrive at exactly the buyer's estimate on both lots by its own calculation; the reader takes one value to be derived from the other.
- Condition: The tendered amounts are the tenderer's own prices and differ from the published estimate, or the document explains why they are equal.
- Options: (a) Preferred: set the estimate of the notices a little apart from the tendered price (an estimate is made before tenders). (b) Change the tender prices; that moves every later amount of the flow.
- Needs decision: yes

### tender/15#F5 · Low · Costs of the tenderer (paper copies, courier) listed as fees of the tendered project
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeTypeCode` = `COURIER`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `TenderedProject/FeeAmount` is "the fee amount for tendered projects" and `AdditionalFee` "an additional fee for this tendered project". The values are what the tenderer spent to take part: 50.00 lume for a paper copy of the documents (of an electronic procedure) and 12.00 for sending the original of its guarantee. They are not part of the offer (the total of 124080.00 does not include them) and the buyer, who set the documentation fee, has no use for them; a tender does not report the tenderer's expenses. If instead they are fees the tenderer charges, they are missing from the total.
- Condition: The tendered project carries a fee only if it is part of what is offered or owed under the tender, and then the document makes clear who pays it and whether the total includes it.
- Options: (a) Preferred: remove the fee and the additional fee. (b) Keep the documentation fee as proof of payment where the procedure requires it, and say so.
- Needs decision: no

### tender/15#F6 · Low · A replacement item that nothing describes
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:Quantity` = `1`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `/Tender/cac:TenderedProject/cbc:VariantID` = `V0`
- Why: `ReplacementRelatedItem` is "a catalogue item that may be a replacement for the item described in this tender line". The tender offers the Serra 180 "as specified" and names `VI-C180-2026` as a possible replacement, with an ID only. The ID occurs in no other example (`grep -l VI-C180-2026 world/examples/tender/*.xml` lists only this file); the catalogue (25) has the bench as `VI-B180` and no such item. The buyer cannot tell what would be delivered instead, or when; and a substitute the buyer has not evaluated sits oddly in a tender that is scored on the offered product. If it is meant as the allowed variant (recycled plastic slats), it belongs in a tendered project with its own `VariantID`.
- Condition: A replacement item is described (name or description, and the condition under which it replaces the item), exists in the tenderer's catalogue, or is absent.
- Options: (a) Preferred: remove it. (b) Offer it as a variant project. (c) Describe it and add it to the catalogue (25).
- Needs decision: no

### tender/15#F7 · Low · The tender does not cite its guarantee
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- XPath: `/Tender/cac:DocumentReference/cbc:ID` = `VI-DS-B180`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:ID` = `BL-DOC-26-0200`
- XPath: `14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`
- Why: The notices require a tender guarantee of 2400.00 lume, constituted by 2026-02-26; the bank certified it the day before this tender (14). The tender mentions the guarantee only as the object of a courier fee. Its document references are the product data sheet, the qualification and a reference letter; neither the certificate (`BL-DOC-26-0200`) nor the guarantee number (`BLUM-G-26-0221`) is cited, so the department must match guarantee and tender by the party alone.
- Condition: The tender refers to the guarantee it relies on (certificate or guarantee number, with a document type).
- Options: (a) Preferred: a `DocumentReference` to the guarantee certificate with a document type. (b) None other seen.
- Needs decision: no

### tender/15#F8 · Low · Originator and beneficiary repeat the contracting party
- XPath: `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The tender names the department three times: as contracting party, as `OriginatorCustomerParty` ("the party originating the Tender") and as `BeneficiaryParty` ("a Party for whom the associated transaction is ultimately intended or who derives benefit from it"). The two extra roles exist for the case that another body asked for or will use the purchase; here they add nothing to `ContractingParty`, and a tenderer has no knowledge of its own about who originated the procedure.
- Condition: Originator and beneficiary are present only where they are a party other than the contracting party.
- Options: (a) Preferred: remove both. (b) Name the parks service as beneficiary, if it is a body of its own in the world.
- Needs decision: no

### tender/15#F9 · Low · The logistics provider of Valdara Industries, with contract number and key account desk, in a tender
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Tender/cac:TendererParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: `ServiceProviderParty` is "a party providing a service to this party": Castrano Logistics, which warehouses and despatches for Valdara Industries, with the number of their arrangement and its key account desk. The tender names Saltmere Engineering as its subcontractor; Castrano Logistics is not offered as a party to the contract, and its key account desk is of no use to the department. It looks copied from the party's master data into a document that does not use it.
- Condition: The party carries a service provider only in documents in which that provider acts or must be known (despatch, transport, customs).
- Options: (a) Preferred: remove the service provider here. (b) If the provider matters to the buyer, declare it where the document has a place for it (as a subcontractor or in the delivery terms).
- Needs decision: no

### tender/15#F10 · Low · Customs trader numbers of the parties in a tender
- XPath: `/Tender/cac:TendererParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. A tender is not declared to customs; the numbers are used when the benches are exported and imported (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- Arithmetic: line 1 119760.00 + line 2 4320.00 = 124080.00 = `LineExtensionAmount` = `PayableAmount`; tax 0.00 fits the exemption of the buyer stated in the notices; unit price 499.00 lies within the bounds 350–600 of the price criterion.
- Tender validity 90 days, envelope `ENV-1` / `COMBINED`, tender type `COMBINED` and lots 1 and 2 agree with the tendering terms of 03; the tender is dated 2026-02-25, before the deadline of 2026-02-26 12:00, and 16 acknowledges it the same day.
- Line 1: quantity 240, sub-line `1.1` with 240 anchor sets and the line reference `1` match the request-for-tender line of 03; lead time 7 days is within the required 10; warranty 5 years equals the required warranty; 10 years on the coating is the maximum of the quality range.
- Order quantities: pallet of 4, increment 4, minimum 20, maximum 96; the first order (26) is for 40 benches, a multiple of 4 within the range.
- `TendererQualificationDocumentReference` `VI-DOC-26-0199` is 13, issued 21 minutes earlier by the same party; the subcontractor Saltmere Engineering is the party 13 names with a share of 20 %.
- ISIN XU0001042501 of the tenderer's listing: check digit correct (`check_ids.py`).

## Considered and refuted
- `/Tender/cac:TenderedProject/cbc:VariantID` = `V0` on the only tendered project: suspected to call the base tender a variant — refuted, an identifier for the base offer is harmless and leaves room for the one variant the terms allow.
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyParty` = the tenderer itself: suspected repetition — refuted, the element says who gives the warranty, and for a manufacturer selling through its own tender that is real information.
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` ("Five years on the frame.") against "Ten years on the coating." in the criterion response: suspected contradiction — refuted, two warranties on two things.
- `/Tender/cac:TenderedProject/cac:TenderLine[2]`: no reference to a line of the call for tenders — refuted as a finding here, 03 has no request-for-tender line for the installation (noted in 02 and 03).
- `/Tender/cac:SubcontractorParty`: "the Subcontractor or other Tenderer who participates in the same Tender" — checked against 13, where the same party is wrongly placed as consortium party; here it is in the right element.

## Outside this review
- The tendering terms tie the envelope `ENV-1` to lot 1 only, while this tender uses it for both lots; the inconsistency lies in 01–03.
- Whether an electronic auction took place after this tender, as 02 and 03 announce, cannot be seen from any example of the flow up to 18; a question of the flow.
