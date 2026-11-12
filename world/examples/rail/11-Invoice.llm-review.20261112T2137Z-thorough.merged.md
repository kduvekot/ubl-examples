# LLM review: 11-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/11-Invoice.xml`, Git blob `ee9c00c2aed8b2e82ac3390db74cfce890bdf1a1` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit abfa39e 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### rail/11#F1 · High · Emission value is not factor × base
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", ValueBaseMeasure "the base quantity to which the value factor applies". 0.82 × 1 EA = 0.82 kg CO2e, not 96 kg. Refutation tried in the merge: 96 / 0.82 = 117.1, which matches neither the bench's gross weight (41.5 kg, 06) nor its material consumption (56.5 kg), so no reading of the base makes the triple consistent. Same triple as in the order (01) and the transit declaration (06); 39 examples over `*.xml`.
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a) preferred: drop factor and base; (b) a factor and base that give 96 kg.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### rail/11#F2 · Medium · A system boundary code in FullnessIndicationCode
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full, partially full, or empty ... used as a parameter when calculating the environmental emission"; cradle to gate (world list EmissionBoundaryCode, EN 15804 A1–A3) is a life-cycle boundary, not a load state. 39 examples.
- Condition: The element is absent or holds a load state of transport equipment used in the calculation.
- Options: (a) preferred: drop it and record the missing boundary element for the TC write-up; (b) keep it only as a recorded gap.
- Needs decision: no (context said yes; aligned with 06 and rail 01)
- From: broad (F2), context (F2)

### rail/11#F3 · Medium · LifecycleStageCode covers less than the stage it describes
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: MANUFACTURING is "Making the product (EN 15804 module A3)" in the world list; the description and value include raw-material supply and its transport (SOURCING, A1–A2).
- Condition: The stage code(s) cover what the description and the value cover.
- Options: (a) preferred: omit the code and keep the text (broad), or (b) two entries SOURCING and MANUFACTURING (context); (c) narrow the description.
- Needs decision: no
- From: broad (F3), context (F3)

### rail/11#F4 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (CountrySubentity), as the customer's address in the same invoice uses (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 example files.
- Condition: No Urvanian address in this example carries the province in Region; where given, it is in CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it.
- Needs decision: no (broad, context yes; aligned with rail 01–05, wood, plastics)
- From: broad (F4), parties (F1), context (F5)

### rail/11#F5 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is a language and repeats `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`. 364 occurrences in 213 example files.
- Condition: LocaleCode is absent or names a locale from a list of locales.
- Options: (a) preferred: drop it; (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad (F5), parties (F2), context (F4)

### rail/11#F6 · Medium · A gate in AdditionalStreetName of the customer's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street, and on an invoice the address identifies the customer, not a delivery point.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) preferred: remove it; (b) where a transport document needs a gate, state it at a delivery location.
- Needs decision: no
- From: broad (F6), parties (F3)

### rail/11#F7 · Low · Export exemption without the evidence or the delivery it rests on
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cbc:Note[2]` = `Delivered at place: the price includes the carriage to the siding.`
- Why: In the world's XU list, EXP means "Goods sent to a buyer outside Urvania; the export is evidenced by the customs declaration". The invoice names neither the customs declaration (VI-TD-26-0331, 06) nor the transport document (FRC-WB-26-0334, 08), and has no Delivery with date and place, so the exemption and the DAP note stand without the facts they rest on. Logistics refuted the missing Delivery within its lens (the invoice's purpose does not depend on it; the delivery is documented in the waybill); the money part found the tax treatment itself consistent. The finding is about the evidence the world's own exemption text names, which the merge keeps as Low.
- Condition: The invoice refers to the declaration that evidences the export (and/or the transport document) and states the delivery, or the world's rules say the order reference suffices.
- Options: (a) preferred: AdditionalDocumentReference to VI-TD-26-0331 (and a reference to the waybill), and a Delivery with the delivery date and the siding; (b) leave it if the world requires no evidence on the invoice.
- Needs decision: no
- From: broad (F7)

### rail/11#F8 · Low · Catalogue and product-passport data on the invoice line
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- Why: An invoice requests payment for the benches; it uses the item's identification, classification and tax category. Warranty, keywords, properties, load-capacity test, dimensions, the footprint and the circularity profile are product documentation (referenced as VI-DS-B180 and VI-RM-B180) that the invoice does nothing with (section 4.8); the order already carries them.
- Condition: The invoice line carries what identifies, classifies and taxes the item (plus what a stated world rule requires).
- Options: (a) preferred: reduce the item to name, identifiers, classification and tax category, leaving product documentation to the referenced documents; (b) keep sustainability data only if a world rule requires it on invoices.
- Needs decision: no
- From: broad (F8, item part), context (F6)

### rail/11#F9 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The invoice does nothing with the supplier's stock-exchange listing or its warehousing provider, nor with the customer's share capital (section 4.8). The supplier's own share capital is not included: parties and context refuted it (company law in several jurisdictions requires it on a company's invoices).
- Condition: Every legal-entity and service-provider element present has a purpose in the invoice.
- Options: (a) preferred: drop them here; (b) keep the supplier's own share capital where the world's invoicing rules require it.
- Needs decision: no
- From: parties (F6), context (F7), broad (F8, party part)

### rail/11#F10 · Low · Customer's contact on the invoice is its sales customer service
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact handles the invoice and its payment (accounts payable) or, as buyer, purchasing; Lumeway's sales customer service serves Lumeway's own customers. The same contact is used for Lumeway as buyer in 01 and as consignee in the transport documents.
- Condition: The accounting customer's contact is Lumeway's accounts-payable or purchasing function.
- Options: (a) preferred: an accounts-payable contact; (b) role-specific contacts in Lumeway's master data.
- Needs decision: no
- From: parties (F5), broad (F9, customer part)

### rail/11#F11 · Low · "English" renderings of the addresses and legal form are Italian
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5); these are tagged `en-XU` but are Italian (own knowledge). A world convention for street names cannot be ruled out; the legal form is the stronger case. 217 such renderings in 102 example files.
- Condition: Every rendering tagged as English is English, or the world records the Italianate English usage.
- Options: (a) record the convention (preferred if intended); (b) translate; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F4)

## Checked and consistent
- Arithmetic (recalculated in the merge): 192 × 49 900 = 9 580 800 XUF = line, LineExtension, TaxExclusive, Taxable, TaxInclusive and Payable amounts (tax 0 under G/EXP); settlement discount 2 % × 9 580 800 = 191 616; settlement period 17 to 27 April = 10 days; due 17 May in DueDate, PaymentMeans and PaymentTerms; penalty 8 % a year.
- Reference `LD-PO-26-0325` resolves to the order 01; order line 1, quantity 192, price 49 900 XUF, item VI-B180 (GRY, 771020000027) and classifications agree with 01 and 06; 192 benches = the consignment of 02, 03, 06, 08; buyer and seller are the order's parties; the buyer's accounting code 4410 "Stock purchases" is the one from the order and fits a wholesaler.
- Tax: G ("Free export item, tax not charged") with EXP and SupplyTypeCode GOODS fits goods sent to Bayvarra under the transit of 06; the customer's state sales tax registration in Upland State as in the other examples.
- Payment: RF20VIINV260337 and the account XU79 0351 0416 0000 0000 2094 58 pass their checks (check_ids.py, from the parts); it is Valdara's account at the Ferrano branch 03510-41600, as in road/15 and tender/32; account name `Valdara Industries SUA` = registration name; RTNS on the Trade Accord rail with SHAR fits a cross-border payment.
- Issue 17 April after the planned delivery 15 April (03, 07); the DAP note agrees with the order and with the freight billed to Valdara (10).
- Parties: Valdara and Lumeway as in 01 (apart from the en-XB/en-XU tagging difference raised in 01's review); GLN 9520610900008 and ISIN XU0001042501 correct; Codana Identification Agency (`XU-R-105644`) as in 01.

## Considered and refuted
- `/Invoice/cbc:IssueTime` = `11:14:00`: invoice issued before delivery — refuted: delivery on 15 April, invoice 17 April. (from broad)
- `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`: terms not agreed in the order — refuted: the order states no payment terms, so the seller's standard terms XU-STD apply. (from broad)
- `/Invoice/cbc:TaxPointDate`: tax point on the invoice date while the train left on 14 April — refuted: no actual export or delivery date is stated in the flow, and a tax point on an invoice issued within days is a common rule. (from money)
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: basis of the discount (gross or net) — refuted: tax is 0, both give 191 616. (from money)
- `/Invoice/cbc:DocumentCurrencyCode`: invoice in XUF to a customer whose tax currency is XBL — refuted: the order was placed in XUF. (from money)
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: redundant with the document currency — refuted: the buyer is in Bayvarra, so stating payment in XUF has a reason. (from context)
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: share capital copied into the invoice — refuted: company law in several jurisdictions requires it on a company's invoices (own knowledge). (from parties, context)
- `/Invoice/cac:InvoiceLine/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`: does not resolve to an example — refuted as a broken reference: the data sheet is a document the flow does not model; likewise VI-LCA-2025 and VI-RM-B180. (from logistics)
- `/Invoice/cac:InvoiceLine/cac:Item`: an export invoice without Delivery or a transport-document reference — refuted within the logistics lens; carried into F7, where broad's finding on the export evidence stands. (from logistics)

## Refuted in the merge
### broad/F9 (part) · Low · Supplier's contact on the invoice is the sales order desk
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Broad: the accounting supplier's contact answers billing questions (accounts receivable); a sales desk is given; condition: accounts contacts for both accounting parties, or none.
- Refuted because: the parties part's argument holds: for a goods invoice that follows the buyer's order, the seller's order desk is a legitimate contact for the buyer's questions about the invoice (quantities, prices, the order); nothing in the role contradicts it. The customer part of broad/F9 stands as F10.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; 96 / 0.82 checked.
- broad/F2, context/F2 → F2: needs decision no (context yes).
- broad/F3, context/F3 → F3; broad/F5, parties/F2, context/F4 → F5; broad/F6, parties/F3 → F6: combined.
- broad/F4, parties/F1, context/F5 → F4: needs decision no (broad, context yes).
- broad/F8 split: item part → F8 (with context/F6), party part → F9 (with parties/F6, context/F7), as in 06.
- broad/F9 split: customer part → F10 (with parties/F5); supplier part → "Refuted in the merge".
- parties/F4 → F11: count replaced by 217 in 102 files.
