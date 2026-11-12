# LLM review: 06-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/06-Invoice.xml`, Git blob `b3fee4995e687ca616a88364c0b3bc9ec2261466` (committed)
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

### ore/06#F1 · High · Payment terms and due date contradict the agreed transport plan
- XPath: `/Invoice/cbc:DueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- Why: the invoice refers to the plan (`/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` =
  `FRC-TEP-26-0307`), whose payment terms are 30 days net from the consignment note. The consignment
  note is dated 10 March (`05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`), so payment is due
  on 9 April. The invoice counts from its own date (12 March → 11 April) and adds a 2 % settlement
  discount for payment within 10 days (settlement period 12–22 March, discount 41 291 XUF) that the
  plan does not grant. Two documents of the flow state different terms for the same freight.
- Condition: due date, payment terms and any discount of the invoice agree with the terms of the
  plan it refers to.
- Options: (a, preferred) due date 9 April, terms "30 days net from the consignment note" and no
  settlement discount, as agreed in the plan; (b) change the plan's terms to the invoice's standard
  terms.
- Needs decision: no

### ore/06#F2 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province
  belongs in `CountrySubentity`. 104 `*.xml` files do the same
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/06#F3 · Low · Bonus, penalty and waiting time of the plan cannot be checked from the invoice
- XPath: `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `1720441`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note` = `2 % of the freight when the train is delivered on the first day of the window, so that the factory can start the blend a day early.`
- Why: the plan agrees a 2 % bonus for delivery on the first day of the window, a 5 % penalty per
  day late, and a waiting-time charge. The invoice bills plain freight (1 788.4 t × 962) without a
  delivery date (no `cac:Delivery/cbc:ActualDeliveryDate`, no `cac:InvoicePeriod`) and without a
  bonus charge or a statement that none is due. The train was despatched on the first day, 10 March
  (`04-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-03-10`), so whether the bonus applies
  depends on the arrival day, which no document of the flow states.
- Condition: the invoice states when the service was performed (delivery date), and the bonus is
  either charged or its absence follows from that date.
- Options: (a, preferred) add the actual delivery date; if it is 10 March, a 2 % charge
  (34 409 XUF on 1 720 441) with reason; (b) add only the delivery date showing a later arrival.
- Needs decision: yes (when the train arrived is part of the story)

### ore/06#F4 · Low · Plan, waybill and framework contract referenced only as untyped additional documents
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- XPath: `/Invoice/cac:AdditionalDocumentReference[2]/cbc:ID` = `FRC-WB-26-0310`
- Why: both references resolve (`03-TransportExecutionPlan.xml`, `05-Waybill.xml`) but carry no
  `DocumentTypeCode`, so the receiver cannot tell which is the plan and which the consignment note
  without knowing the numbering. The framework contract on which the freight rests
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportContract/cbc:ID` =
  `VI-FRC-FW-2026`) is not referenced, although Invoice has `cac:ContractDocumentReference` for it.
- Condition: each reference says what kind of document it is; the contract the invoice is based on
  is referenced if it governs the price.
- Options: (a, preferred) add the document type codes and a `ContractDocumentReference` to
  `VI-FRC-FW-2026`; (b) type codes only.
- Needs decision: no

### ore/06#F5 · Low · Contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the accounting supplier's contact answers questions about the invoice (billing, accounts
  receivable), not an operations planner of the freight desk; the accounting customer's contact is
  accounts payable, not a sales customer-service officer.
- Condition: both contacts belong to the accounting functions of the parties.
- Options: (a, preferred) billing / accounts-payable contacts; (b) drop job title and department.
- Needs decision: no

### ore/06#F6 · Low · Buyer's logistics service provider copied into the invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics has nothing to do with this freight invoice. Master data without use;
  75 `*.xml` files carry it (`grep -rl --include='*.xml' 'VI-SP-2026-01'`).
- Condition: no service provider without a role in the invoice.
- Options: (a, preferred) leave it out; (b) give it a role.
- Needs decision: no

## Checked and consistent
- Arithmetic: 1 788.4 t × 962 XUF = 1 720 440.8 → 1 720 441 (line, LineExtension, TaxExclusive,
  TaxableAmount); 20 % VAT = 344 088.2 → 344 088; 1 720 441 + 344 088 = 2 064 529 = TaxInclusive =
  Payable; settlement discount 2 % of 2 064 529 = 41 290.58 → 41 291.
- Quantity 1 788.4 t equals the despatched quantity (`04-DespatchAdvice.xml`) and the waybill weight.
- Bill-to party of the plan and request (Valdara) is the accounting customer; the seller is the
  carrier; standard-rated VAT on a domestic transport service, supply type `SERVICES`.
- `check_ids.py`: RF reference `RF09FRCINV260311` and account `XU920351041700000000523645` OK; the
  account's bank and branch code (03510, 41700) agree with the branch ID `03510-41700` (Serravona).
- Party descriptions identical to the other examples of the flow.

## Considered and refuted
- `/Invoice/cbc:TaxPointDate` = `2026-03-12`: suspected a tax point before completion of the service
  — refuted because the train left on 10 March for a short domestic run and the invoice date is a
  usual tax point for services.
- `/Invoice/cbc:AccountingCost` = `Raw materials and parts`: suspected wrong cost centre for freight
  — refuted because inbound freight is commonly booked to the cost of the raw material it brings.
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`: this is
  consistent with the goods; the contradiction with the container-train service code lies in
  `02-TransportExecutionPlanRequest.xml` and `03-TransportExecutionPlan.xml` and is a finding there.

## Outside this review
- The flow contains no remittance of this freight invoice; `08-RemittanceAdvice.xml` pays only the
  ore invoice `SM-INV-26-0312`. Whether the freight payment belongs in the flow is a question of the
  flow's composition.
