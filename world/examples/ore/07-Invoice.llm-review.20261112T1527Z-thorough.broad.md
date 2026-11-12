# LLM review: 07-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/07-Invoice.xml`, Git blob `0e28c5a596e22d95a0c87b535ac9b772716f3863` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/07#F1 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province
  belongs in `CountrySubentity`. 104 `*.xml` files do the same
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/07#F2 · Low · The mine's site conditions copied into the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: the accounting supplier's physical location (the mine and its rail siding, its access road and
  coordinates) does nothing in an invoice for goods delivered FCA at the siding by rail; it is copied
  from master data (section 4.8). It also appears in the remittance advice
  (`08-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions`).
- Condition: the invoice carries no party data it does not use.
- Options: (a, preferred) leave the physical location out of the invoice; (b) keep only its
  identifier if the invoice needs the place of supply.
- Needs decision: no

### ore/07#F3 · Low · Contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the accounting supplier's contact answers questions about the invoice (accounts receivable);
  the accounting customer's contact is accounts payable. Both are sales customer-service desks;
  for Valdara, the customer, a sales desk is the wrong side altogether.
- Condition: both contacts belong to the accounting functions of the parties.
- Options: (a, preferred) billing and accounts-payable contacts; (b) drop job title and department.
- Needs decision: no

### ore/07#F4 · Low · Buyer's logistics service provider copied into the invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics has nothing to do with this invoice. Master data without use; 75 `*.xml`
  files carry it (`grep -rl --include='*.xml' 'VI-SP-2026-01'`).
- Condition: no service provider without a role in the invoice.
- Options: (a, preferred) leave it out; (b) give it a role.
- Needs decision: no

### ore/07#F5 · Low · Moisture deduction without a basis in the order or the invoice
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Moisture deduction`
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.015`
- XPath: `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `8060`
- Why: ore is commonly priced per dry tonne and the wet tonnage corrected for the measured moisture
  (own knowledge). Here the order prices 8 060 XUF per tonne with no dry/wet basis and no moisture
  clause, and the invoice deducts 1.5 % without stating the measured moisture or the assay it comes
  from. The only hint is an assay reference in the transport request
  (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID`
  = `SM-ASSAY-26-11`), which the invoice does not reference. The deduction cannot be verified from
  the documents.
- Condition: the basis of the deduction is visible: the moisture figure (as item property or in the
  reason) and/or the assay reference, and the order's price basis allows such a deduction.
- Options: (a, preferred) add the measured moisture (e.g. an item property "Moisture" 1.5 %) and an
  additional document reference to the assay certificate; (b) state the wet/dry basis in the order's
  price or line note.
- Needs decision: no

### ore/07#F6 · Low · World item number has the form of a valid GTIN-12 in the GS1 US range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: 12 digits with a correct GS1 mod-10 check digit; as GTIN-13 `0771010000013`, prefix 077 in the
  GS1 US range (own knowledge). The world scheme `urn:ubl-examples:world:item` (64 `*.xml` files)
  can be mistaken for real GTINs. Whether this GTIN is assigned I could not check.
- Condition: the item number cannot be mistaken for a real GTIN, or its non-assignment is recorded.
- Options: (a, preferred) a format that cannot be a GTIN; (b) record a GS1 check in the sources.
- Needs decision: yes (the scheme is world-wide)

## Checked and consistent
- Arithmetic: 1 788.4 t × 8 060 = 14 414 504 (ItemPriceExtension, BaseAmount); × 0.015 = 216 217.56
  → 216 218; 14 414 504 − 216 218 = 14 198 286 (line, LineExtension, TaxExclusive, Taxable);
  20 % VAT = 2 839 657.2 → 2 839 657; total 17 037 943 = TaxInclusive = Payable =
  TaxInclusiveLineExtension. Price extension incl. tax 14 414 504 × 1.2 = 17 297 404.8 → 17 297 405,
  tax 2 882 901. Settlement discount 2 % of 17 037 943 = 340 758.86 → 340 759.
- Order reference and line resolve to `01-Order.xml`, price 8 060 per tonne as ordered; despatch
  reference resolves to `04-DespatchAdvice.xml`, invoiced quantity 1 788.4 t = despatched quantity.
- Due date 10 April = 30 days after 11 March; settlement period 11–21 March = 10 days, as the note.
- Payee account `XU420351041700000000104729` (Serravona, branch 03510-41700) is the account
  `08-RemittanceAdvice.xml` pays to; RF reference `RF73SMINV260312` is quoted there; 17 037 943 paid on
  9 April, after the discount period, without discount, before the due date.
- `check_ids.py`: ISIN, RF reference and account OK.
- Party descriptions identical to the other examples of the flow.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: suspected a
  code that does not fit a moisture deduction — refuted because UN/EDIFACT 5189 has no moisture or
  quality code, and 64 "Special agreement" fits a contractual deduction (own knowledge of 5189).
- `/Invoice/cac:InvoiceLine/cac:ItemPriceExtension/cac:TaxTotal/cbc:TaxAmount` = `2882901`:
  suspected contradiction with the line's tax 2 839 657 — refuted because the price extension is
  defined as price × quantity, before the line allowance, so its tax is on 14 414 504.
- `/Invoice/cbc:IssueDate` = `2026-03-11`: suspected an invoice before arrival — refuted because a
  goods invoice may follow despatch (FCA: delivery at the mine siding on 10 March).
