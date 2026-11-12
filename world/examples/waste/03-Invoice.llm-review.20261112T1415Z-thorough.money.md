# LLM review: 03-Invoice.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/03-Invoice.xml`, Git blob `802363ed10113ef3a82c854031713a677b74609e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### waste/03#F1 · Low · Buyer's accounting cost "Raw materials and parts" for a waste collection and recovery service
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: `AccountingCost` is "the buyer's accounting code, applied to the Invoice as a whole, expressed as text" (`AccountingCostCode` the same as a code). The invoice bills a service, "Collection at the factory and recovery of sorted production waste, per tonne collected" (`/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste…`, `SupplyTypeCode` `SERVICES`): for the buyer Valdara Industries this is a waste disposal / service cost, not a purchase of raw materials or parts. The code `3100` is moreover the same value as the buyer's own industry classification (`/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`, ISIC 3100 furniture manufacture), which suggests a default copied from the buyer's master data rather than a cost account chosen for this supply. The same pair `3100` / `Raw materials and parts` occurs in 12 examples (`grep -rl --include='*.xml' 'Raw materials and parts' world/examples`), all of them with Valdara Industries as a party; in at least `rail/10-Invoice.xml` (a container slot on a train) and `utilities/02-Invoice.xml` (electricity supply) the supply is not raw materials either.
- Condition: `AccountingCost` (and `AccountingCostCode`, if kept) names a cost type of the buyer that fits a waste collection and recovery service, or both are absent.
- Options: (a) preferred: give the buyer a cost account for waste disposal / environmental services (e.g. a different code with text "Waste disposal") in this invoice, because the buyer's booking reference is the purpose of the element; (b) remove both elements if the buyer has not asked for a cost reference.
- Needs decision: no

### waste/03#F2 · Low · The invoice does not say when the service was performed
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-04-04`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-04`
- Why: the invoice bills collection and recovery of 38.2 t of waste, but carries neither `cac:InvoicePeriod` nor `cac:Delivery` (actual delivery / service date). The only date of the service is indirect: the referenced movement document was issued on `02-WasteMovement.xml:/WasteMovement/cbc:IssueDate` = `2026-04-02`, after the waste had been received. `TaxPointDate` is defined as "the date of the Invoice, used to indicate the point at which tax becomes applicable", so the issue date there is a legitimate reading; but an invoice that charges VAT normally states the date of the supply when it differs from the invoice date (own knowledge of VAT invoicing practice, e.g. EU VAT Directive art. 226(7)), and without it the tax point cannot be checked against the supply.
- Condition: the invoice states when the service was performed (a service date or period on or before 2026-04-02), consistent with `02-WasteMovement.xml`.
- Options: (a) preferred: add `cac:InvoicePeriod` (or `cac:Delivery/cbc:ActualDeliveryDate`) with the collection/recovery date, because it states the supply directly; (b) reference the movement with a `DocumentTypeCode`/`IssueDate` in `AdditionalDocumentReference` so the service date can be derived.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2` t × `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `12350` per `/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1` t = 471,770 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `471770`. Units of quantity and base quantity agree (TNE).
- Totals: `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `471770` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `471770` (no allowances or charges); tax 20 % × 471,770 = 94,354 = `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount` = `94354` = `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `94354`; 471,770 + 94,354 = 566,124 = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `566124` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `566124` (no prepayment, no rounding).
- Tax: the line's `ClassifiedTaxCategory` (S, 20 %, SERVICES) matches the subtotal's category (S, 20 %); 20 % is the standard rate used for XU in every other XUF invoice of the examples (rail/10, utilities/02, energy/02 and 03, plastics/07, ore/06 and 07); seller and buyer are both VAT-registered in XU, so a domestic standard-rated supply fits.
- Currency: XUF (Ferra, 0 fractional digits in `world/codelists/CurrencyCode-2.4-world.gc`); all amounts are whole numbers; the account currency and the tax scheme currency are XUF.
- Payment terms: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.` agrees with `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-04` (30 days after 2026-04-04), `/Invoice/cbc:DueDate` = `2026-05-04`, `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-05-04`, the settlement period 2026-04-04 to `/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-14` (10 days) and `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`. `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `11322` = 2 % × 566,124 = 11,322.48, rounded to 0 decimals; `PaymentTerms/cbc:PaymentMeansID` `1` resolves to `/Invoice/cac:PaymentMeans/cbc:ID` = `1`.
- Penalty interest 8 % per year (`ANN`, UN/ECE Rec. 20 "year"), simple interest: coherent.
- Payment means: credit transfer (`30`) to the supplier's own account: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Rinova Recovery SRU` = the supplier's registration name; the account number `XU700351041620000000418916` contains the branch ID `03510-41620` of `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` = `03510-41620`; `check_ids.py`: the IBAN-like check digits are correct, and the creditor reference `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF84RRINV260208` (ISO 11649) is valid and repeated in the instruction note.
- Reference: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207` resolves to `02-WasteMovement.xml`, whose gross weight 38,200 kg equals the invoiced 38.2 t, whose recovery facility is the supplier and whose producer/notifier is the customer, with the same VAT registrations (`XU007318479`, `XU007299291`).

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `11322`: suspected wrong base (2 % of the net amount would be 9,435) — refuted because the note says "2 % discount when paid within 10 days" of the invoice, which is ordinarily read on the amount paid (566,124); the figure is correct for that base.
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste…`: the supplier bills the collection while `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage` is the carrier — refuted because a recovery facility subcontracting the haulage and billing the collection to the producer is ordinary, and no document of the flow says who contracted the carrier or that the carrier bills the producer.
- `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `S`: suspected a domestic reverse charge as some real jurisdictions apply to waste and scrap — refuted because the examples show no such rule for XU and the item is a recovery service, not a supply of scrap.
- `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `12350`: suspected that sorted polyethylene production waste has a positive value, so that the recovery facility would pay the producer — refuted because a gate fee for collection and recovery is a legitimate arrangement and the item says what is charged for.
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`: billed "per tonne collected" on the shipment's gross weight, which includes the big bags — refuted because 12 big bags weigh about 30 kg together (own knowledge), below the invoice's 0.1 t precision; the movement cites a weight statement as basis.
- `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF84RRINV260208`: suspected misuse of "an identifier for a payment made using this means of payment" for a creditor reference — refuted because the RF reference is exactly the identifier the payer is to quote for this payment.
- No `cac:ContractDocumentReference` to the waste contract `01-WasteNotification.xml:/WasteNotification/cac:DocumentReference/cbc:ID` = `VI-WASTE-CONTRACT-26`, on which the price per tonne presumably rests — refuted as a finding because the invoice's purpose does not depend on it (section 4.3); the price is stated in full.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: the buyer's share capital in an invoice (legal invoicing rules usually concern the seller's) — not a transaction amount; left to the parties/context lenses.
