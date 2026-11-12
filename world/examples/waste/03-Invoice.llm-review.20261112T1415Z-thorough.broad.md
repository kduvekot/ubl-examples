# LLM review: 03-Invoice.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: broad

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

### waste/03#F1 · High · Tonnes billed equal the shipment's gross weight including the vehicle
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`
- XPath: `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: the line bills "per tonne collected" 38.2 t, which is exactly the gross weight of the referenced movement; `GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The invoice therefore bills the weight of the truck and big bags as waste. Read the other way round (38.2 t is the waste), the movement's gross weight would be the net weight, and 38.2 t of waste plus a tractor and trailer of about 14–15 t (own knowledge) would exceed the 40 t road limit by far. Either way one of the two values is wrong. The weight statement the movement refers to does not exist (`02-WasteMovement.xml:/WasteMovement/cac:WeightStatementDocumentReference/cbc:ID` = `RR-WB-26-0412`), so it cannot settle the question.
- Condition: the invoiced quantity is the net weight of waste collected, and that net weight is stated in (or derivable from) the movement or its weight statement; the movement's gross weight is larger by packaging and transport equipment and within the vehicle's limits.
- Options: (a) keep 38200 kg as gross in the movement, add a net weight (e.g. about 23.8 t) there or in a weight statement, and bill that net weight (preferred: keeps the movement physically plausible); (b) declare 38.2 t as `NetNetWeightMeasure`/`NetWeightMeasure` in the movement and split the load over two vehicles. Either changes the amounts, taxes and settlement discount here.
- Needs decision: no

### waste/03#F2 · Medium · Province in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity` ("The political or administrative division of a country … such as the name of its county, province, or state"). 219 occurrences in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of this example carries a province in `Region`.
- Options: move to `CountrySubentity` (preferred); or drop.
- Needs decision: no

### waste/03#F3 · Low · Buyer's cost account for a waste service is raw materials, coded as the buyer's ISIC class
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole, expressed as text". Valdara buys a waste collection and recovery service, which it would not book on raw materials and parts; the code `3100` is identical to Valdara's ISIC class (`/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`), which suggests a value taken from there rather than from a chart of accounts. The text `Raw materials and parts` occurs in 12 examples (`grep -rl --include='*.xml' 'Raw materials and parts'`), all of them documents where Valdara is the buyer or customer.
- Condition: the buyer's accounting code and text fit a waste disposal/recovery service and are not the party's industry code.
- Options: a waste management / environmental services cost account of Valdara (preferred); or omit both, since nothing in the flow uses them.
- Needs decision: no

### waste/03#F4 · Low · Reference to the movement does not say what it is
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`
- Why: the reference resolves to `02-WasteMovement.xml`, but it carries only the ID; an invoice reader cannot see that it is the waste movement document that proves the collection.
- Condition: the reference states its document type (e.g. `DocumentTypeCode` or `DocumentType`).
- Options: add `DocumentTypeCode` from the world's UBL document type list (`WasteMovement`) or `DocumentType` (preferred); alternatively a `DespatchDocumentReference`-like dedicated reference if one fits.
- Needs decision: no

### waste/03#F5 · Low · Customer's contact is its sales order desk; master data the invoice does not use
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the accounting customer's contact receives and settles the invoice (accounts payable), not Valdara's sales order desk. Valdara's listed shares and its warehousing provider Castrano have no role in this invoice. Same values in 87 (`Order desk`), 75 (`XU0001042501`) and 75 (`VI-SP-2026-01`) examples (`grep -rl --include='*.xml'`).
- Condition: the customer's contact is one that handles invoices; the customer carries no data the invoice does not use.
- Options: accounts payable contact and removal of the copied master data (preferred).
- Needs decision: no

## Checked and consistent
- Arithmetic: 38.2 × 12350 = 471770 (line and `LineExtensionAmount`, `TaxExclusiveAmount`, `TaxableAmount`); 20 % of 471770 = 94354; 471770 + 94354 = 566124 = `TaxInclusiveAmount` = `PayableAmount`.
- Payment terms: due date 2026-05-04 is 30 days after 2026-04-04; settlement period 2026-04-04 to 2026-04-14 is 10 days; `SettlementDiscountAmount` 11322 = 2 % of 566124 (11322.48, rounded), consistent with the note "2 % discount when paid within 10 days".
- `check_ids.py`: RF reference `RF84RRINV260208` and account `XU700351041620000000418916` check digits correct; ISIN correct.
- Tax: standard rate, services, both parties VAT-registered in Urvania; a domestic service.
- `AdditionalDocumentReference` `RR-DOC-26-0207` resolves to `02-WasteMovement.xml`, issued 2026-04-02, before this invoice; the supplier is the recovery facility and the customer the notifier/producer, as in the movement.
- Payee account named after Rinova Recovery SRU, the supplier.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]`: the line bills "collection at the factory" although the carrier in `02-WasteMovement.xml` is Trasvia Haulage — refuted because Rinova can sell collection as part of its service and subcontract the haulage to Trasvia.
- `/Invoice/cbc:TaxPointDate`: equal to the issue date, with no date of the service — refuted as a finding because the tax point at issue date is a legitimate rule and UBL does not require a service date; that the referenced movement itself states no date of collection is a finding of the review of `02-WasteMovement.xml`.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode`: the supplier's waste permit in an invoice — refuted because a recovery service may only be performed under such a permit, so showing it on the invoice for that service has a reason.
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: discount computed on the tax-inclusive amount rather than the net amount — refuted because the terms do not say on which base, and a discount on the amount payable is common practice.
