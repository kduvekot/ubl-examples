# LLM review: 19-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/19#F1 · High · The tender names another tenderer's qualification and reference list as its own
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- Why: `TendererQualificationDocumentReference` is "A reference to the tenderer qualification document that has been used to qualify the tenderer", and the tenderer here is Brackenmere Furniture (`/Tender/cac:TendererParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`). `VI-DOC-26-0199` is the TendererQualification of Valdara Industries (`13-TendererQualification.xml:/TendererQualification/cbc:ID` = `VI-DOC-26-0199`, signed by `13-TendererQualification.xml:/TendererQualification/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`), the competing tenderer. The evidence document `VI-REF-2025` carries Valdara's prefix as well and is the same evidence Valdara's own tender names (`15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`). Brackenmere's own qualification in the flow is `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`. A tender cannot be qualified by, or supported with, a competitor's documents.
- Condition: The qualification reference and the evidence reference of this tender name documents of Brackenmere Furniture (or are absent), and no identifier of a Valdara document occurs in the tender.
- Options: (a) preferred: refer to Brackenmere's qualification application response `BF-DOC-26-0193` and to an evidence document of Brackenmere's own, because the flow already has the first; (b) remove both references if Brackenmere has nothing of the kind. The same two values occur in the withdrawn tender `17-Tender.xml`.
- Needs decision: no

### tender/19#F2 · High · The warranty of the tender line and the warranty answered to the award criterion differ
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:WarrantyInformation` = `Five years on the frame.`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Description` = `Six years on the frame and the slats.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `6`
- Why: The line says the bench has a warranty of five years on the frame, valid for five years; the response to criterion AC-2 ("Warranty and coating.") offers six years on the frame and the slats. Both speak of the frame of the same bench in the same tender, so the tender offers two different warranties and the contracting party cannot tell which one is scored and which one binds. (Valdara's tender does not have this problem: its line gives five years on the frame and its criterion response ten years on the coating, two different subjects.)
- Condition: The warranty period and scope stated on the tender line and those stated in the response to AC-2 are the same, or clearly concern different parts of the bench.
- Options: (a) preferred: make the line say six years on frame and slats (WarrantyInformation and WarrantyValidityPeriod), since the criterion response is what the tenderer competes with; (b) make the criterion response five years, the minimum the call for tenders accepts (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`).
- Needs decision: no

### tender/19#F3 · High · The note calls the earlier tender withdrawn, but this tender was issued before the withdrawal
- XPath: `/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.`
- XPath: `/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `/Tender/cbc:IssueTime` = `12:10:00`
- Why: The note speaks of "the withdrawn tender", but the withdrawal was issued almost six hours later (`18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`, `18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:IssueTime` = `17:56:00`), and it announces this tender as still to come (`18-TenderWithdrawal.xml:/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`). At 12:10 the first tender was not withdrawn, and Brackenmere would have had two tenders in the procedure, which the call for tenders forbids (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`).
- Condition: The issue date and time of this tender are later than those of the withdrawal `BF-DOC-26-0204`, and still before the submission deadline (2026-02-26 12:00).
- Options: (a) preferred: issue this tender after the withdrawal (and before the deadline); (b) issue the withdrawal before this tender. Either way the wording of both notes then holds.
- Needs decision: no

### tender/19#F4 · Medium · The total price is given as the amount tendered for the quality criterion
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `119040.00`
- Why: `Amount` "Specifies the monetary amount tendered for this awarding criterion". The criterion answered is AC-2, the quality criterion (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:Name` = `Quality`), measured in years (minimum 5, maximum 10), for which the tender correctly gives a quantity of 6 years. The amount is the total price of the tender (`/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`), which answers the price criterion AC-1 (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:Name` = `Price`), not the warranty. The tender has no response to AC-1.
- Condition: The response to AC-2 carries no price; if the price is given as a criterion response at all, it is in a response whose `AwardingCriterionID` is AC-1.
- Options: (a) preferred: move the amount into a second AwardingCriterionResponse for AC-1; (b) drop the amount, the price being in LegalMonetaryTotal already. The same pattern is in `15-Tender.xml` and `17-Tender.xml`.
- Needs decision: no

### tender/19#F5 · Medium · A language code as locale
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (which country or region variant) the language is used. The value repeats the language code of `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used), from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no

### tender/19#F6 · Medium · A spare slat as "replacement" of the bench
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:ID` = `BF-SLAT-PB2`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:ReplacementRelatedItem/cbc:Quantity` = `1`
- Why: `ReplacementRelatedItem` is "A catalogue item that may be a replacement for the item described in this tender line": an item that can be supplied instead of the bench PB-2. The identifier reads as a slat of the PB-2, a spare part of the bench, which cannot replace a bench; nothing else in the element (no description) says what it is, and the identifier occurs nowhere else (searched `world/examples/*/*.xml`: only `17-Tender.xml` and this example). My reading of the identifier is an inference; if it is in fact an alternative bench the finding falls.
- Condition: The item under `ReplacementRelatedItem` is one that can be supplied in place of the tendered bench, and the element says what it is (a description), or the element is absent.
- Options: (a) preferred: name a real substitute bench with a description; (b) remove the element if Brackenmere offers no substitute (spare parts have no element on a tender line).
- Needs decision: yes (what the item is must be settled first)

### tender/19#F7 · Low · Fees of the procedure stated as part of the offer
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeTypeCode` = `COURIER`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: `FeeAmount` is "The fee amount for tendered projects" and `AdditionalFee` "An additional fee for this tendered project": fees that belong to what is tendered. The 50 lume is the contracting party's charge for a paper copy of the procurement documents (`03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`): a cost the tenderer had (if it asked for paper at all; the tender is electronic), not something it offers. The courier fee is likewise the tenderer's own cost of taking part, and it refers to a guarantee of which the flow has none for Brackenmere (the only guarantee certificate, `14-GuaranteeCertificate.xml`, is for Valdara Industries). Neither amount enters the total (115200 + 3840 = 119040). The document does nothing with them, and both values are identical to those in Valdara's tender `15-Tender.xml`.
- Condition: The tendered project carries only fees that are part of what the tenderer offers to the contracting party, or none; a fee that refers to a guarantee has a guarantee of this tenderer behind it.
- Options: (a) preferred: remove both fees from the tender; (b) keep them only if the world has a rule that tenderers declare their participation costs, and then give Brackenmere its own values and guarantee.
- Needs decision: yes (whether a tender declares such fees at all)

### tender/19#F8 · Low · One tendered project and one total for two lots
- XPath: `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[1]/cbc:ID` = `LOT-1`
- XPath: `/Tender/cac:TenderedProject/cac:ProcurementProjectLot[2]/cbc:ID` = `LOT-2`
- XPath: `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cac:Item/cbc:Name` = `Installation of a park bench`
- Why: A `TenderedProject` is "A project with which this Tender is associated. A single Tender can be used to bid for one project, multiple projects, or the global project", and the call for tenders has two lots (LOT-1 park benches, LOT-2 installation) and asks for "Unit prices per lot." (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cac:DocumentTenderRequirement/cbc:Description`). The tender puts both lots into one tendered project with one total, one warranty and one set of criterion responses; which line belongs to which lot can only be guessed from the item names (line 2 has no reference to a line of the call for tenders), and no amount per lot is stated although the lots could be awarded separately.
- Condition: The amount tendered for each lot can be read from the tender without interpreting item names: either one tendered project per lot, or the lot stated for each line.
- Options: (a) preferred: one `TenderedProject` per lot, each with its lot, lines and total; (b) keep one project if the procedure only allows a tender for both lots together, and say so in the call for tenders.
- Needs decision: yes (whether lots can be tendered and awarded separately)

### tender/19#F9 · Low · The contracting party repeated as originator and as beneficiary
- XPath: `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `OriginatorCustomerParty` is "The party originating the Tender" and `BeneficiaryParty` "A Party for whom the associated transaction is ultimately intended or who derives benefit from it". Both hold the same party as `ContractingParty` (`/Tender/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`). The two roles add information only when another body originated the need or benefits from the supply; here they repeat the contracting party, and the tender (a document of the tenderer) does nothing with them. Under the rule "no fillers" they have no business reason.
- Condition: `OriginatorCustomerParty` and `BeneficiaryParty` are present only when they are a party other than the contracting party (e.g. the parks service for which the department buys), or are absent.
- Options: (a) preferred: remove both; (b) name the body that actually uses the benches, if the world has one. The same holds for `15-Tender.xml` and `17-Tender.xml`.
- Needs decision: no

### tender/19#F10 · Low · A public department described as a company in a commercial register, with a liquidation status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The contracting party is a department of a city (industry classification 8411, general public administration). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public department cannot be in liquidation, so the statement "active, not in liquidation" has no meaning for it, and a registration scheme of type "Commercial register" does not fit a public body. In a tender, a document of the tenderer about its offer, this master data of the addressee is also not used.
- Condition: The legal entity of the public department carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the contracting party in tenders to identification and name.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN 9523710900008 has a correct check digit.
- The note "It corrects the price per bench" against the withdrawn tender: line 1 there is 112800.00 for 240 benches (470 each), here 115200.00 (480 each); the only other differences between the two tenders are ID, UUID, issue date and time, signature ID, note and the totals that follow from the price.
- Totals: 115200.00 + 3840.00 = 119040.00 = LineExtensionAmount = PayableAmount; tax 0.00 against a tax-exempt public body.
- `VariantID` = `V0`: the call for tenders allows one variant (a bench of recycled plastic slats), so naming the base offer is meaningful.
- `TenderTypeCode` and `TenderEnvelopeTypeCode` = `COMBINED`, envelope `ENV-1`: as the call for tenders asks (one combined envelope ENV-1).
- Criterion response quantity 6 years lies within the 5–10 years of AC-2; AC-2.1 (durability of the coating) is answered with a description of the finish.
- Lead time 7 days against the 10 days required; warranty 5 years on the line meets the 5 years required; sub-line 1.1 (240 ground anchor sets) mirrors sub-line 1.1 of the call for tenders.
- Validity of 90 days; signature by the tenderer.

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MaximumOrderQuantity`: 96 is less than the 240 benches tendered — refuted because the contract is a framework whose benches are called off in releases over two years; a maximum per order below the total is consistent with that (minimum 20, increment 4 and pallet of 4 agree with each other: 20 and 96 are multiples of 4).
- `/Tender/cac:TenderedProject/cbc:VariantID`: a variant identifier on a tender that is not a variant — refuted, see "Checked and consistent".
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyParty`: the tenderer itself as warranty party looked redundant — refuted because the bench is of Brackenmere's own make and the element's definition asks who is responsible for the warranty described on the line.
- `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount`: a tax total of 0.00 without subtotal — refuted for this lens: the buyer is a public body exempt from the state sales tax and the amount states the consequence; whether a subtotal with category is needed is for the money part.
- `/Tender/cac:Signature`: a signature with only an identifier and the signatory — refuted because the definition asks no more, and a tender is a signed document.

## Outside this review
- `/Tender/cac:CallForTenderDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT` (also on line 1) is not the document ID of the call for tenders in the flow (`LPWD-DOC-26-0189`), while `25-Catalogue.xml` refers to the call for tenders as `LPWD-DOC-26-0189`; reference kinds and targets are the logistics part's lens.
- The tax exemption reason of the contracting party ("Sale to a public body…") describes a transaction rather than the party's status; party tax data is the parties part's lens.
