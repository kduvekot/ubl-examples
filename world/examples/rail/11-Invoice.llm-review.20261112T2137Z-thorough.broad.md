# LLM review: 11-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/11-Invoice.xml`, Git blob `ee9c00c2aed8b2e82ac3390db74cfce890bdf1a1` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### rail/11#F1 · High · Emission value does not equal factor × base
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", applied to ValueBaseMeasure; 0.82 × 1 bench = 0.82 kg, not 96 kg. The same triple occurs in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82' world/examples`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a) preferred: drop factor and base (a product footprint per bench); (b) a factor and base that give 96 kg.
- Needs decision: no

### rail/11#F2 · Medium · A system boundary code in FullnessIndicationCode
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty ... used as a parameter when calculating the environmental emission"; cradle to gate (world EmissionBoundaryCode, EN 15804 A1–A3) is a life-cycle boundary, not a load state. 39 examples.
- Condition: The element is absent or holds a load-state code used in the calculation.
- Options: (a) preferred: drop it; (b) note the missing boundary element for the TC write-up.
- Needs decision: no

### rail/11#F3 · Medium · LifecycleStageCode covers less than the stage it describes
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: MANUFACTURING is "Making the product (EN 15804 module A3)" in the world list; the description and value include raw material supply and its transport (SOURCING, A1–A2).
- Condition: The stage code(s) cover what the description and value cover.
- Options: (a) split into SOURCING and MANUFACTURING; (b) preferred: omit the code, keep the text.
- Needs decision: no

### rail/11#F4 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity), as for the customer's "Upland State" in the same invoice. 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as non-administrative.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/11#F5 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` is a language, not a locale.
- Condition: LocaleCode absent or a locale such as `en-XB`.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/11#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address": a gate is not a street, and the invoice address is not a delivery point.
- Condition: AdditionalStreetName holds a street name or is absent.
- Options: (a) preferred: drop it.
- Needs decision: no

### rail/11#F7 · Low · Export exemption without the evidence or the delivery it rests on
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cbc:Note[2]` = `Delivered at place: the price includes the carriage to the siding.`
- Why: In the world's XU list, EXP means "Goods sent to a buyer outside Urvania; the export is evidenced by the customs declaration". The invoice names neither the customs declaration (VI-TD-26-0331, 06) nor the transport document (FRC-WB-26-0334, 08), and has no Delivery with the date and place of delivery (15 April, Lumeway's siding), so the exemption and the DAP note stand without the facts they rest on.
- Condition: The invoice refers to the declaration that evidences the export (and/or the transport document), and states the delivery (date, place), or the world's rules say the order reference suffices.
- Options: (a) preferred: AdditionalDocumentReference to VI-TD-26-0331 (and DespatchDocumentReference or another reference to the waybill), and a Delivery with ActualDeliveryDate 2026-04-15 and the siding; (b) leave it if the world requires no evidence on the invoice.
- Needs decision: no

### rail/11#F8 · Low · Data the invoice does nothing with
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The invoice line carries the full catalogue item (warranty, keywords, properties, dimensions, emissions, circularity profile), and the supplier its warehousing provider. An invoice uses the item's identification, classification and tax category; the rest is copied master data (the order already carries it).
- Condition: The invoiced item carries what the invoice uses; ServiceProviderParty is absent.
- Options: (a) preferred: reduce the item to name, identifiers, classification and tax category; drop ServiceProviderParty; (b) keep sustainability data only if a world rule requires it on invoices.
- Needs decision: no

### rail/11#F9 · Low · Contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact answers billing questions (accounts receivable), the accounting customer's deals with the invoice (accounts payable); both are sales desks here, and Lumeway's is the one serving its own customers.
- Condition: Accounts contacts for both accounting parties, or none.
- Options: (a) preferred: accounts receivable / payable contacts; (b) drop Contact.
- Needs decision: no

## Checked and consistent
- Arithmetic: 192 × 49 900 = 9 580 800 XUF = line, LineExtension, TaxExclusive, TaxInclusive and Payable (tax 0 under G/EXP); settlement discount 2 % = 191 616; settlement period 10 days.
- Reference: `LD-PO-26-0325` resolves to the order (01); order line 1, quantity 192, price 49 900 XUF, item VI-B180 and its classifications agree; buyer and seller are the order's parties; AccountingCost "Stock purchases" (4410) is the buyer's code from the order.
- The quantity invoiced equals the quantity transported and declared (02, 03, 06, 08), and the note on DAP agrees with the order's delivery terms.
- Tax: G with EXP (export of goods outside Urvania) fits goods sent to Bayvarra; the customer's state sales tax registration in Upland State is described as in the other examples.
- Payment: RF20VIINV260337 and the account XU79 0351 0416 0000 0000 2094 58 pass their checks (check_ids.py); branch 03510-41600 matches the account; ChargeBearer SHAR fits a cross-border payment; payment currency XUF = document currency.
- Parties described as in the other rail examples.

## Considered and refuted
- `/Invoice/cbc:IssueTime` = `11:14:00`: suspected an invoice issued before delivery is complete — refuted because delivery took place on 15 April (03, 08) and the invoice is dated 17 April.
- `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`: suspected terms not agreed in the order — refuted because the order states no payment terms, so the seller's standard terms XU-STD apply.
