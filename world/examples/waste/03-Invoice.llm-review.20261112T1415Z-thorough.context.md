# LLM review: 03-Invoice.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: context

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

### waste/03#F1 · Medium · Tonnes of waste collected are invoiced from a gross weight that includes packaging and transport equipment
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`
- XPath: `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: The line charges "per tonne collected" of waste. The only weight in the flow is the movement's `Shipment/GrossWeightMeasure`, defined as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 38.2 t is exactly that gross figure, so the invoice bills the big bags and the transport equipment as waste — or, if 38.2 t is in fact the net waste weight, the movement uses `GrossWeightMeasure` for a net weight. Either way the two documents cannot both be right about what 38.2 t is.
- Condition: The invoiced quantity is the weight of waste collected, and that weight appears in the movement (or weight statement) as a net weight of the goods; or the invoice states that it bills gross weight.
- Options: (a) preferred: give the movement's goods item a `NetWeightMeasure` (waste only) next to the gross weight, and invoice that net figure. (b) If the price is agreed per gross tonne, say so in the item description (and keep the gross figure).
- Needs decision: no

### waste/03#F2 · Medium · The lifecycle stage of the waste is given as the lifecycle stage of the invoiced service, and its "environmental impact" text describes no impact
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:LifecycleStageCode` = `ENDOFLIFE`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:LifecycleStageDescription[2]` = `The service handles the production waste at the end of its life, before it is recycled.`
- Why: `Item/LifecycleStageCode` is "A code indicating the product's lifecycle stage (e.g., sourcing, manufacturing, distribution, usage, end-of-life)", and `LifecycleStageDescription` "A text describing the specific environmental impact associated with this product's lifecycle stage". The item invoiced is a service (collection and recovery, `SupplyTypeCode` SERVICES); "end of life" is the stage of the waste it handles, not of the item. The description explains what the service does, not an environmental impact (no emissions, recycling rate, avoided material or the like). `LifecycleStageCode` occurs in 40 examples (40 elements) and `LifecycleStageDescription` in 40 (41 elements) (`grep -r --include='*.xml' -o -F '<cbc:LifecycleStageCode'` and `'<cbc:LifecycleStageDescription'` over `world/examples`), so the pattern may recur.
- Condition: Either the lifecycle elements are absent from this service line, or the description states an environmental impact of the item at the stage the code names.
- Options: (a) preferred: drop both from this line (the waste's end-of-life status is already clear from the flow). (b) Keep the code and replace the text by a real impact statement (e.g. the recycling rate or avoided virgin PE), if the world has a reason to report it on the invoice.
- Needs decision: no

### waste/03#F3 · Medium · A province in `Region`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country and belongs in `CountrySubentity`. The same value is in `Region` in 104 examples (219 occurrences; `grep -r --include='*.xml' -o '<cbc:Region>Province of'` over `world/examples`).
- Condition: No `Address/Region` holds a province; the province, where needed, is in `CountrySubentity`.
- Options: (a) preferred: move the value to `CountrySubentity`. (b) Drop it.
- Needs decision: no

### waste/03#F4 · Low · The buyer's accounting code books a waste recovery service as raw materials
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole, expressed as text". Valdara Industries buys the collection and recovery of its production waste, a service, not raw materials or parts. The code `3100` is also the buyer's ISIC code (`/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`, "Manufacture of furniture"), which suggests the buyer's cost account was taken from its industry classification. The same pair occurs in 12 examples (`grep -rl --include='*.xml' -F '>Raw materials and parts<'` and `-F 'AccountingCostCode>3100<'`, 12 files each, among them orders and invoices of the rail, packaging, utilities, ore and wood flows) — plausible where Valdara buys materials, not here.
- Condition: The buyer's accounting cost names a cost account for waste disposal/recovery services (or is absent), and the code is a cost-account code rather than the ISIC code.
- Options: (a) preferred: use an account like "Waste disposal and recovery" with its own code. (b) Drop both, since nothing in the flow needs them.
- Needs decision: no

### waste/03#F5 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The buyer's warehousing provider (Castrano Logistics) plays no part in a recovery invoice, and the buyer's stock listing and share capital are not used by it. The buyer's contact is its sales order desk, which neither ordered the waste service nor handles payables. The seller's waste-operating permit is relevant to the movement documents but the invoice does nothing with it. Same service provider and listing in 75 examples each, "Order desk" in 87, the permit `XU-ENV-2024-0311` in 14 (`grep -rl --include='*.xml' -F` over `world/examples`).
- Condition: Every element under the invoice parties has a reason in the invoice; the buyer's contact is one who bought the service or handles the invoice.
- Options: (a) preferred: drop `ServiceProviderParty`, `SecurityListing`, `CorporateStockAmount`, `FullyPaidSharesIndicator` and `PartyAuthorization` here; give the buyer a purchasing or accounts-payable contact. (b) Keep the permit if the world wants invoices for waste services to show the operator's permit (then state why in the item or a note).
- Needs decision: no

### waste/03#F6 · Low · The reference to the movement document does not say what it is
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`
- Why: The ID resolves to `02-WasteMovement.xml` (a WasteMovement), but the reference carries no `DocumentTypeCode` or description, and an ID ending in "DOC" says nothing about its kind. The weighed quantity that the invoice bills comes from the weight statement `RR-WB-26-0412` that the movement references, which the invoice does not mention.
- Condition: The reference states the kind of document (code or description); the basis of the invoiced quantity can be traced from the invoice.
- Options: (a) preferred: add `DocumentTypeCode` (or `DocumentType`) "Waste movement document" and, optionally, a second reference to the weight statement.
- Needs decision: no

## Checked and consistent
- `AdditionalDocumentReference` `RR-DOC-26-0207` resolves to `02-WasteMovement.xml`, issued 2026-04-02, before this invoice (2026-04-04); seller (XU-R-104548) is the recovery facility and buyer (XU-R-104274) the producer/notifier of the flow.
- `InvoiceTypeCode` 380 (commercial invoice) fits a request for payment for a service supplied.
- `ClassifiedTaxCategory/SupplyTypeCode` SERVICES fits "Collection … and recovery".
- `InvoicedQuantity` and `BaseQuantity` both in TNE, fitting "per tonne collected".
- `PayeeFinancialAccount` belongs to the seller (name Rinova Recovery SRU, holder country XU), the party that receives the payment.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`: Rinova bills collection although Trasvia Haulage is the carrier in the movement — refuted because Rinova can buy the haulage from Trasvia and sell collection as part of its service.
- `/Invoice/cbc:DefaultLanguageCode` = `en`: texts are tagged `en-XU` — refuted because the default applies only to texts without `languageID`, and `en` is the language of `en-XU`.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XU-TR-104548`: a customs trader ID in a domestic invoice — refuted as a separate finding; it is a plain party identifier and harmless, and the domestic-vs-transboundary question is in 01's and 02's reviews.

## Outside this review
- Settlement discount, tax and totals arithmetic, and the missing supply date/period of the service are for the money part.
