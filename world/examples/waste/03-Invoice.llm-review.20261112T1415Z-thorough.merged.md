# LLM review: 03-Invoice.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/03-Invoice.xml`, Git blob `802363ed10113ef3a82c854031713a677b74609e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit e6f29b5 2026-11-12 Reviews of the waste flow, run 20261112T1415Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

This merged file combines the parts broad, money, parties, logistics and context of run
`20261112T1415Z-thorough`; all five parts reviewed the same Git blob as this file.

## Findings

### waste/03#F1 · High · Tonnes billed "per tonne collected" are the movement's gross weight, including packaging and transport equipment
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`
- XPath: `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: the line bills the waste collected, per tonne. The referenced movement (`/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`) states 38 200 kg only as `GrossWeightMeasure`, "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". Billing 38.2 t therefore bills the big bags and the transport equipment as waste; or the movement's 38 200 kg is in fact a net figure in the wrong element, and then 38.2 t of waste plus a tractor and trailer of about 14–15 t (own knowledge) exceeds the 40 t road limit (F7 of 02's review). Either way the two documents contradict each other on the quantity of waste. The weight statement the movement cites (`02-WasteMovement.xml:/WasteMovement/cac:WeightStatementDocumentReference/cbc:ID` = `RR-WB-26-0412`) does not exist, so it cannot settle the question. Money's refutation (bag tare below the 0.1 t precision) does not hold, because the gross weight also includes the transport equipment (see "Considered and refuted").
- Condition: the invoiced quantity equals the net weight of waste stated in the referenced movement (or a referenced weight statement), that net weight is below the movement's gross weight by packaging and transport equipment, and the gross weight is within the vehicle's limits; or the invoice states that the price applies per gross tonne.
- Options: (a) preferred: keep 38 200 kg as gross in the movement, add a net weight (about 23–24 t) there or in a weight statement, and bill that net weight, recalculating the line, tax, totals and settlement discount; (b) declare 38.2 t as `NetWeightMeasure` in the movement and split the load over two vehicles; (c) if the price is agreed per gross tonne, say so in the item description.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1, Medium); refuted as a candidate by money

### waste/03#F2 · Medium · The lifecycle stage of the waste given as the item's, with an "environmental impact" text that describes no impact
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:LifecycleStageCode` = `ENDOFLIFE`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:LifecycleStageDescription[2]` = `The service handles the production waste at the end of its life, before it is recycled.`
- Why: `Item/LifecycleStageCode` is "A code indicating the product's lifecycle stage (e.g., sourcing, manufacturing, distribution, usage, end-of-life)", and `LifecycleStageDescription` "A text describing the specific environmental impact associated with this product's lifecycle stage". The item invoiced is a service (collection and recovery, `SupplyTypeCode` SERVICES); "end of life" is the stage of the waste it handles, not of the item. The description explains what the service does, not an environmental impact (no emissions, recycling rate, avoided virgin material). `LifecycleStageCode` occurs in 40 examples (re-counted in the merge, `grep -rl --include='*.xml' '<cbc:LifecycleStageCode'`), so the pattern may recur.
- Condition: either the lifecycle elements are absent from this service line, or the description states an environmental impact of the item at the stage the code names.
- Options: (a) preferred: drop both from this line (the waste's end-of-life status is clear from the flow); (b) keep the code and replace the text by a real impact statement (e.g. recycling rate, avoided virgin PE), if the world has a reason to report it on the invoice.
- Needs decision: no
- From: context (F2)

### waste/03#F3 · Medium · Province in `Region` instead of `CountrySubentity`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country and belongs in `CountrySubentity`, which the world uses for Bayvarra's states (799 occurrences over `*.xml`, parties part). `<cbc:Region>Province of` occurs 219 times in 104 examples (re-counted in the merge).
- Condition: no address in this example carries a province in `Region`; a province, where given, is in `CountrySubentity`.
- Options: move the province to `CountrySubentity` for all Urvanian addresses (preferred); or drop it where the postal zone suffices.
- Needs decision: no
- From: broad (F2), parties (F1), context (F3)

### waste/03#F4 · Low · Buyer's cost account for a waste service is "Raw materials and parts", coded as the buyer's ISIC class
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole, expressed as text" (`AccountingCostCode` the same as a code). Valdara buys a waste collection and recovery service (`SupplyTypeCode` SERVICES), not raw materials or parts. The code `3100` equals Valdara's ISIC class (`/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`, Manufacture of furniture), which suggests a value taken from there rather than from a chart of accounts. The pair occurs in 12 examples (re-counted in the merge, `grep -rl --include='*.xml' 'Raw materials and parts'`), all with Valdara as buyer or customer; at least in `rail/10-Invoice.xml` (a container slot on a train) and `utilities/02-Invoice.xml` (electricity) the supply is not raw materials either (money part).
- Condition: the buyer's accounting cost (and code, if kept) names a cost account that fits a waste collection and recovery service, and the code is a cost-account code, not the ISIC code; or both are absent.
- Options: (a) preferred: a waste disposal / environmental services cost account of Valdara with its own code; (b) omit both, since nothing in the flow uses them.
- Needs decision: no
- From: broad (F3), money (F1), context (F4)

### waste/03#F5 · Low · The invoice does not say when the service was performed
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-04`
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-04-04`
- Why: the invoice bills collection and recovery of 38.2 t but carries neither `cac:InvoicePeriod` nor `cac:Delivery` (actual delivery / service date). The referenced movement states no transport date either (only its issue date `02-WasteMovement.xml:/WasteMovement/cbc:IssueDate` = `2026-04-02`; F2 of 02's review), so no document of the flow says on which day the waste was collected. `TaxPointDate`, "The date of the Invoice, used to indicate the point at which tax becomes applicable", at the issue date is a legitimate reading; but a VAT invoice normally states the date of supply where it differs from the invoice date (own knowledge, e.g. EU VAT Directive art. 226(7)), and without it the tax point cannot be checked against the supply.
- Condition: the invoice (or the referenced movement) states when the service was performed, a date or period no later than 2026-04-02, consistent with `02-WasteMovement.xml`.
- Options: (a) preferred: add `cac:Delivery/cbc:ActualDeliveryDate` with the facility as `DeliveryLocation`, or `cac:InvoicePeriod`, matching the date added to `02-WasteMovement.xml`; (b) reference the movement with its type and `IssueDate` so the service date can be derived (F6).
- Needs decision: no
- From: money (F2), logistics (F2)

### waste/03#F6 · Low · The reference to the waste movement gives only its ID
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`
- Why: the reference resolves to `02-WasteMovement.xml` (a Waste Movement), but the invoice does not say what kind of document it is: no `DocumentTypeCode`/`DocumentType` and no issue date; the prefix `RR-DOC` does not tell the buyer that it is the movement document of the collected load. The weighed quantity the invoice bills comes from the weight statement `RR-WB-26-0412` the movement cites, which the invoice does not mention (context). A `*DocumentReference` whose only child is `cbc:ID` occurs 555 times in 177 of 250 examples (logistics part, counted with lxml).
- Condition: the reference states that it is the waste movement document (code or text), preferably with its issue date 2026-04-02, and the basis of the invoiced quantity can be traced from the invoice.
- Options: (preferred) add `cbc:DocumentTypeCode` (world UBL document type list, `WasteMovement`) or `cbc:DocumentType`, plus `cbc:IssueDate`; optionally a second reference to the weight statement, once it exists (F1 of 02's review).
- Needs decision: no
- From: broad (F4), logistics (F3), context (F6)

### waste/03#F7 · Low · Customer's contact is its own sales order desk
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the accounting customer's contact is whom the supplier contacts about the invoice (accounts payable) or the purchase (purchasing, the plant that hands over the waste). Valdara's contact is its sales order desk, which takes orders from Valdara's own customers. Valdara carries this contact in all its 75 examples whatever its role (`grep -rl --include='*.xml' -F 'order@valdara.example'`, re-counted in the merge; "Order desk" in 87).
- Condition: the customer's contact deals with this purchase or with paying invoices.
- Options: (preferred) an accounts-payable or purchasing contact for Valdara as buyer; or omit the contact.
- Needs decision: no
- From: broad (F5), parties (F4), context (F5)

### waste/03#F8 · Low · Customs and capital-market master data of the parties copied into a domestic service invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XU-TR-104548`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the invoice bills Rinova's collection and recovery service to Valdara, both in Ferrano, Urvania, with Urvanian VAT at the standard rate; no customs procedure is involved, so the customs-trader identifiers of both parties have no use. The customer's share capital, listing and its warehousing-and-despatch provider play no part in billing this service (share capital on an invoice is sometimes a legal requirement for the seller; here it is the buyer's). The Valdara blocks occur in 75 examples each (section 4.8). Context judged the customs-trader ID harmless (see "Considered and refuted"); the merge keeps it with the other copied data, as Low.
- Condition: every party detail present has a use in this invoice.
- Options: (preferred) leave these elements out of the invoice's parties; or give the reason in the example where one exists.
- Needs decision: no
- From: parties (F2), broad (F5), context (F5)

### waste/03#F9 · Low · The supplier's waste operating permit on the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- Why: context: the seller's waste operating permit is relevant to the movement documents, but the invoice does nothing with it; it occurs in 14 examples (re-counted in the merge). Counter-argument (broad, parties): the invoice bills the recovery of the waste, which may only be performed under such a permit, so stating it on the invoice for that service has a reason. The merge cannot settle whether the world wants waste-service invoices to show the operator's permit.
- Condition: the permit is on the invoice only if the world's invoicing of waste services gives it a reason (stated, e.g., in the item or a note), or it is absent.
- Options: (a) drop `PartyAuthorization` from the invoice's supplier; (b) keep it and state why in the item description or a note. No preference; a decision on the world's rules.
- Needs decision: yes
- From: context (F5); refuted as a candidate by broad and parties

### waste/03#F10 · Low · Supplier registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". The same New Year's Day date is given to 25 different legal entities (parties part; 181 files carry the date, re-counted in the merge), while others have individual dates (the customer `1962-04-12`); it looks like a default (rule "no fillers").
- Condition: Rinova's `RegistrationDate` is its own registration date in the world, or is absent.
- Options: (preferred) an individual plausible date; or remove the element. If the world has all registers re-founded on 1996-01-01, record that and dismiss.
- Needs decision: yes
- From: parties (F3)

## Checked and consistent
- Arithmetic (redone in the merge): 38.2 t × 12 350 per 1 t (`BaseQuantity` 1 TNE, same unit as the quantity) = 471 770 = line and `LegalMonetaryTotal/LineExtensionAmount` = `TaxExclusiveAmount` = `TaxableAmount` (no allowances or charges); 20 % × 471 770 = 94 354 = `TaxSubtotal/TaxAmount` = `TaxTotal/TaxAmount`; 471 770 + 94 354 = 566 124 = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `566124` = `PayableAmount` (no prepayment, no rounding).
- Payment terms: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.` agrees with the due date 2026-05-04 (30 days after 2026-04-04) in `DueDate`, `PaymentTerms` and `PaymentMeans`, the settlement period 2026-04-04 to 2026-04-14 (10 days) and `SettlementDiscountPercent` 2; `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `11322` = 2 % × 566 124 = 11 322.48, rounded; `PaymentMeansID` 1 resolves to `PaymentMeans/ID` 1. Penalty interest 8 % per year (`ANN`), simple: coherent.
- Tax: line category S, 20 %, SERVICES matches the subtotal; 20 % is the standard rate for XU in every other XUF invoice of the examples (rail/10, utilities/02, energy/02 and 03, plastics/07, ore/06 and 07; money part); both parties VAT-registered in XU: a domestic standard-rated service.
- Currency XUF (Ferra, 0 decimals): all amounts are whole numbers; account and tax-scheme currency XUF.
- Payment means: credit transfer to the supplier's own account (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Rinova Recovery SRU`); the account number contains the branch ID `03510-41620`; `check_ids.py`: account `XU700351041620000000418916`, RF reference `RF84RRINV260208` and ISIN check digits correct. BIC-like `CREVXUFR` uses the user-assigned country code XU, so it is no real BIC (parties).
- `AdditionalDocumentReference` `RR-DOC-26-0207` resolves to `02-WasteMovement.xml`, issued 2026-04-02 12:34, before this invoice (2026-04-04 12:44); the supplier is the recovery facility and the customer the producer/notifier there, described identically in 01, 02 and 03 (parties part, c14n comparison), with the same VAT registrations.
- `InvoiceTypeCode` 380 fits a request for payment for a service supplied; `ProfileExecutionID` `WASTE-2026-01` agrees with 01 and 02.
- The supplier's permit `XU-ENV-2024-0311` (valid to 2029-12-31) is the same as in 01 and 02 (whether it belongs here is F9).
- Legal forms and sizes fit the parties (SRU small recovery company; SUA large listed manufacturer).

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`: Rinova bills collection while the carrier in `02-WasteMovement.xml` is Trasvia Haulage — refuted because a recovery facility can sell collection as part of its service and subcontract the haulage; no document of the flow says who contracted the carrier (from broad, money, logistics, context).
- `/Invoice/cbc:TaxPointDate` = `2026-04-04`: equal to the issue date, with no service date — refuted as a finding about the tax point (a tax point at issue date is a legitimate rule) (from broad); the missing service date is F5.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3` and `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`: the supplier's permit copied into an invoice — refuted by broad and parties because the recovery service may only be performed under it. Context made it a finding; the merge keeps it as F9 with both arguments.
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `11322`: discount on the tax-inclusive rather than the net amount (2 % of net would be 9 435) — refuted because the note "2 % discount when paid within 10 days" is ordinarily read on the amount paid (from broad, money).
- `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `S`: a domestic reverse charge as some real jurisdictions apply to waste and scrap — refuted because the examples show no such rule for XU and the item is a recovery service, not a supply of scrap (from money).
- `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `12350`: sorted PE waste has a positive value, so the facility would pay the producer — refuted because a gate fee for collection and recovery is a legitimate arrangement (from money).
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`: billed on a gross weight that includes the big bags — refuted by money because 12 big bags weigh about 30 kg, below 0.1 t precision. The merge does not share the refutation: no document states 12 bags (12 is the number of notified shipments; a full load would be about 60 bags, about 150 kg), and by definition the gross weight also includes transport equipment (at least the trailer). The candidate is part of F1.
- `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF84RRINV260208`: misuse of "An identifier for a payment made using this means of payment" for a creditor reference — refuted because the RF reference is the identifier the payer quotes for this payment (from money).
- No `ContractDocumentReference` to `01-WasteNotification.xml:/WasteNotification/cac:DocumentReference/cbc:ID` = `VI-WASTE-CONTRACT-26`, on which the price presumably rests — refuted because the invoice's purpose does not depend on it; the price is stated in full (from money).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: the buyer's share capital — not a transaction amount; it is part of F8 (from money).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: an unfit supplier contact — refuted because the seller's customer service is the right contact for the buyer's questions about the invoice (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`: a furniture maker buying a waste service — refuted, a furniture maker produces plastic production waste (from parties).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: a real BIC — refuted because `XU` is a user-assigned ISO 3166 code (from parties).
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`: a unit conversion error between KGM and TNE — refuted: 38 200 kg = 38.2 t (from logistics).
- Missing reference to the notification `VI-DOC-26-0204` — refuted because the movement the invoice cites refers to it, and the invoice bills one movement (from logistics).
- `/Invoice/cbc:DefaultLanguageCode` = `en` while texts are tagged `en-XU` — refuted because the default applies only to texts without `languageID`, and `en` is the language of `en-XU` (from context).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XU-TR-104548`: a customs trader ID in a domestic invoice — refuted by context as a separate finding (a plain, harmless identifier). Parties made it part of its master-data finding; the merge keeps it in F8, because data the document does not use is a Low finding (section 4.8).

## Changed in the merge
- broad/F1 + logistics/F1 (High) + context/F1 (Medium) → F1: High, because the invoice and the movement contradict each other on the quantity of waste (section 6); options of all three combined; money's refuted candidate answered.
- broad/F2 + parties/F1 + context/F3 → F3: grouped.
- broad/F3 + money/F1 + context/F4 → F4: grouped; money's evidence from other flows kept.
- money/F2 + logistics/F2 → F5: grouped; broad's refutation of the tax-point candidate kept under "Considered and refuted" (it concerns the tax point, not the service date).
- broad/F4 + logistics/F3 + context/F6 → F6: grouped; context's point about the weight statement added to the condition.
- broad/F5 + parties/F2 + parties/F4 + context/F5 → F7 (contact) and F8 (master data): broad/F5 and context/F5 combined both; split so each finding has one condition; the supplier's permit from context/F5 made a finding of its own (F9), because broad and parties refuted it and its condition differs.
- context/F5 (permit part) → F9: separate Low with "Needs decision: yes", because the parts disagree and the merge cannot settle it.

## Outside this review
- Context left settlement discount, tax and totals arithmetic and the missing supply date to the money part; they are under "Checked and consistent" and F5.
- The physics of 38.2 t for one road load is F7 of 02's review.
