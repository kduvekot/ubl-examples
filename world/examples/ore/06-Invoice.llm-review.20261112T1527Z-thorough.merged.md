# LLM review: 06-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/06-Invoice.xml`, Git blob `b3fee4995e687ca616a88364c0b3bc9ec2261466` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
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

### ore/06#F1 · High · Payment terms and due date contradict the transport plan the invoice refers to
- XPath: `/Invoice/cbc:DueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `41291`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-11`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `05-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-03-10`
- Why: the invoice refers to the plan (`/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` =
  `FRC-TEP-26-0307`) and to the consignment note
  (`/Invoice/cac:AdditionalDocumentReference[2]/cbc:ID` = `FRC-WB-26-0310`). The plan agrees freight
  payment at 30 days net from the consignment note, issued on 10 March: due on 9 April 2026. The
  invoice instead uses the identifier of standard terms (`XU-STD`), counts 30 days from its own date
  (12 March → 11 April, recomputed in the merge) and offers a 2 % settlement discount for payment
  within 10 days (settlement period 12–22 March, 41 291 XUF) that the plan does not grant. The
  identical note, rate and penalty interest in `07-Invoice.xml` (another seller) suggest that standard
  terms were used instead of the contract terms of this service. Two documents of the flow state
  different terms for the same freight.
- Condition: the invoice's due dates, payment terms and any discount agree with the payment terms of
  the plan it refers to, or the plan's terms say what the invoice applies.
- Options: (a, preferred) due date 2026-04-09 in DueDate, PaymentMeans and PaymentTerms, note (and
  ID) referring to the agreed terms of the framework agreement `VI-FRC-FW-2026`, no settlement
  discount unless the agreement grants one (then also in the plan); (b) change the plan's terms to
  the carrier's standard terms (a story change).
- Needs decision: no
- From: broad (F1), money (F1), context (F1)

### ore/06#F2 · High · Bulk-wagon freight billed under a plan for a container train
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- Why: the invoice bills rail freight for ore in bulk wagons and refers to the transport execution
  plan, whose main service is `RAILCONT` ("Container train" in the world's TransportServiceCode list;
  the same in `02-TransportExecutionPlanRequest.xml`). The invoice and the plan it refers to describe
  two different services; a contradiction with a referenced document is a finding of this review
  (section 4). The invoice's description fits the rest of the flow (loose ore, 30 wagons), and the
  world list also has `RAILWAGON`, so the wrong value is most likely the plan's.
- Condition: the service billed and the main transportation service of the referenced plan describe
  the same kind of carriage.
- Options: (a, preferred) correct the plan and the request to the wagon-load service, leaving this
  invoice as it is; no other sensible direction, as the ore is not in containers.
- Needs decision: no
- From: logistics (F1); broad listed it under "Considered and refuted" as a finding of 02/03 (see
  "Changed in the merge")

### ore/06#F3 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located" and Address/CountrySubentity as "The territorial
  division of a country, such as a county or state, expressed as text". A province is a territorial
  division of Urvania; Bayvarran addresses put their states in CountrySubentity.
  `<cbc:Region>Province of` occurs 219 times in 104 XML examples (`grep -rl --include='*.xml'` and
  `grep -rh … | wc -l` over `world/examples`, recounted in the merge).
- Condition: the province of every Urvanian address in this example is in `cbc:CountrySubentity`
  and not in `cbc:Region`, or the world states why Region is used on purpose.
- Options: (a, preferred) move the province to CountrySubentity for all Urvanian addresses, as for
  Bayvarra; (b) keep Region and record in the world why.
- Needs decision: yes (it changes the Urvanian address format in every flow and may be deliberate)
- From: broad (F2), parties (F1), context (F2)

### ore/06#F4 · Low · Bonus and penalty of the plan neither applied nor excluded
- XPath: `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `1720441`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note` = `2 % of the freight when the train is delivered on the first day of the window, so that the factory can start the blend a day early.`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-03-10`
- Why: the plan agrees a 2 % bonus for delivery on the first day of the window and a 5 % penalty per
  day late. The invoice bills plain freight (1 788.4 t × 962 = 1 720 441) with no allowance or
  charge, no delivery date (no `cac:Delivery/cbc:ActualDeliveryDate`, no `cac:InvoicePeriod`) and no
  statement that none is due. The train was despatched on 10 March, the first day of the service
  window (`04-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-03-10`) for a short domestic
  run, and no example of the flow states when it arrived. So the reader cannot tell whether the bonus
  (2 % of 1 720 441 = 34 409 XUF) was earned and omitted. It is also open which window is meant: the
  plan's service window (from 10 March) or the buyer's requested delivery period
  (`01-Order.xml:/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-09`),
  whose first day the train cannot meet.
- Condition: the invoice states when the service was performed, and either carries the bonus (or
  penalty) as a charge or allowance with its reason, or its amount is consistent with the bonus not
  being earned on that date.
- Options: (a, preferred) the actual delivery date on the invoice and, if it is 10 March, a 2 %
  charge with its reason; (b) if the story says the train arrived later, the delivery date alone
  explains the absence of a bonus.
- Needs decision: yes (when the train arrived, and so whether the bonus was earned, is part of the story)
- From: broad (F3), money (F2); logistics noted it under "Outside this review"

### ore/06#F5 · Low · Plan and waybill referenced only by ID; framework contract not referenced
- XPath: `/Invoice/cac:AdditionalDocumentReference[1]/cbc:ID` = `FRC-TEP-26-0307`
- XPath: `/Invoice/cac:AdditionalDocumentReference[2]/cbc:ID` = `FRC-WB-26-0310`
- Why: AdditionalDocumentReference is "A reference to an additional document associated with this
  document". Both references resolve (`03-TransportExecutionPlan.xml`, `05-Waybill.xml`) but carry no
  `DocumentTypeCode` or `DocumentType`, so the receiver can tell only from the number prefixes which
  is the contract basis and which the proof of performance. The framework contract on which the
  freight rests (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportContract/cbc:ID`
  = `VI-FRC-FW-2026`) is not referenced, although Invoice has `cac:ContractDocumentReference`. The
  logistics part counted 555 of 595 document references in the examples with only an ID (lxml over
  `*/*.xml`; not recounted in the merge).
- Condition: each reference states the type of the referenced document; the contract that governs
  the price is referenced.
- Options: (a, preferred) `DocumentTypeCode` `TransportExecutionPlan` and `Waybill` from the world's
  UBLDocumentTypeCode list, and a `ContractDocumentReference` to `VI-FRC-FW-2026`; (b) type codes only.
- Needs decision: no
- From: broad (F4), logistics (F2), context (F5)

### ore/06#F6 · Low · Contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Freight desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party". In an invoice the accounting supplier's
  contact answers questions about the bill (billing, accounts receivable), the accounting customer's
  contact processes it (accounts payable). The carrier's operations freight desk and Valdara's sales
  order desk are given, copied from master data (Valdara's contact is in 75 XML examples, Ferrano Rail
  Cargo's in 15, per the parties part).
- Condition: the accounting supplier's contact belongs to billing or accounts receivable and the
  accounting customer's to accounts payable, or each is left out.
- Options: (a, preferred) a contact per function, using the one that fits; (b) leave the contacts
  (or job title and department) out.
- Needs decision: no
- From: broad (F5), parties (F2), context (F3)

### ore/06#F7 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's share listing and its warehousing provider Castrano Logistics (which appears in the
  ore flow only inside Valdara's party) have no use in a freight invoice. Section 4.8 and IND5. Both
  occur in 75 XML examples (`grep -rl --include='*.xml'` for `Castrano Logistics`, `XU0001042501`
  and `VI-SP-2026-01`, recounted in the merge).
- Condition: every aggregate of the parties has a use in this invoice, or the document says why it
  carries it.
- Options: (a, preferred) leave them out; (b) give them a role in the story and show it in the flow.
- Needs decision: no
- From: broad (F6), parties (F3), context (F4)

## Checked and consistent
- Arithmetic (redone in the merge): 1 788.4 t × 962 XUF = 1 720 440.8 → 1 720 441 (line,
  LineExtension, TaxExclusive, TaxableAmount); 20 % VAT = 344 088.2 → 344 088; 1 720 441 + 344 088 =
  2 064 529 = TaxInclusive = Payable; settlement discount 2 % of 2 064 529 = 41 290.58 → 41 291;
  settlement period 12–22 March is the 10 days of the note.
- Quantity 1 788.4 t equals the despatched quantity (`04-DespatchAdvice.xml`) and the waybill's
  1 788 400 kg; the line description "from the mine siding to the factory siding" fits the plan's
  from and to locations.
- References resolve: `FRC-TEP-26-0307` → `03-TransportExecutionPlan.xml`, `FRC-WB-26-0310` →
  `05-Waybill.xml`; issued 2026-03-12 14:45, after the waybill and within the service window (to
  2026-03-13).
- Roles: Ferrano Rail Cargo is accounting supplier and seller (provider in 03, carrier in 05);
  Valdara is accounting customer and buyer, the bill-to party of 02/03.
- Tax: category S, 20 %, supply type `SERVICES` on a domestic transport service; both parties
  Urvanian VAT-registered.
- Payment: account `XU920351041700000000523645` passes the IBAN-style check, is in XUF, named
  `Ferrano Rail Cargo SRU`, at branch `03510-41700` (Serravona) whose codes are embedded in the
  account; the same account for Ferrano Rail Cargo in `rail/10-Invoice.xml`. RF reference
  `RF09FRCINV260311` passes. RTGS channel with credit transfer (4461 code 30) is coherent; penalty
  interest 8 % per annum, simple.
- Parties described identically in all eight ore examples; registration names, IDs and electronic
  addresses agree; `check_ids.py` reports no wrong check digit.

## Considered and refuted
- `/Invoice/cbc:TaxPointDate` = `2026-03-12`: suspected a tax point before the service was
  completed, or that it should be the date of performance — refuted because the definition is "The
  date of the Invoice, used to indicate the point at which tax becomes applicable", and the invoice
  date is a legitimate tax point for services; the world's tax-point rule is outside what the review
  may consult (from broad, money).
- `/Invoice/cbc:AccountingCost` = `Raw materials and parts` and `/Invoice/cbc:AccountingCostCode` =
  `3100` on a freight invoice — refuted because inbound freight is commonly booked to the cost of the
  raw material it brings; Valdara uses this code in all 12 XML examples that carry it (from broad,
  money, context).
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `41291`: suspected the discount should be
  on the net amount (34 409) — refuted because the definition does not fix the base, a cash discount
  on the amount paid is common, and `07-Invoice.xml` computes it the same way (from money). The
  discount itself is part of F1.
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF09FRCINV260311` repeats the PaymentID —
  refuted: the note tells the payer what to quote, consistent with the structured value (from money).
- English renderings in Italian form (street names, legal forms, `languageID` `en-XU`) — refuted:
  proper names kept in their local form, with an English gloss for the legal form (from parties).
- Telephone numbers `+999` — refuted: E.164 country code 999 is reserved and unassigned (from parties).
- `0990:10427` with schemeID `ISO 6523` — refuted on knowledge of the ICD register (0990 not
  assigned), not checked against the register (from parties).
- Ferrano Rail Cargo `EntitySizeCode` `SMALL` — refuted: nothing in the flow states staff or
  turnover (from parties).
- Bank identifier `CREVXUFR` suspected to collide with a real BIC — refuted: its country part `XU`
  is user-assigned in ISO 3166, so no real BIC has it (from parties).
- `/Invoice/cac:BuyerCustomerParty` and `/Invoice/cac:SellerSupplierParty` repeating the accounting
  parties — refuted: UBL defines the roles separately, and stating both avoids meaning implied by
  absence (from parties, context).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` =
  `250000000`: share capital in an invoice — refuted because several real jurisdictions require the
  share capital on commercial documents (own knowledge) (from context).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS` for an ordinary supplier payment —
  refuted: the world's FERRA-RTGS rail is named and RTGS of this size is plausible (from context).

## Changed in the merge
- broad, "Considered and refuted" on `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` (the
  container-train contradiction "is a finding of 02/03") → F2 High, together with logistics/F1:
  the merge disagrees with the refutation, because section 4 makes a contradiction with a referenced
  document a finding of the referring example too.
- broad/F2, context/F2 (Needs decision: no) + parties/F1 (yes) → F3 Needs decision: yes, because the
  change touches the Urvanian address format in every flow and may be deliberate.
- broad/F4 (types and contract reference), logistics/F2, context/F5 (types only) → F5: grouped; the
  condition now covers both the type codes and the contract reference.
- broad/F3 + money/F2 → F4: combined, with money's open question about which window is meant.
- broad/F1, money/F1, context/F1 → F1: combined; all evidence (terms ID, discount amount, waybill
  date) kept; due dates recomputed (10 March + 30 days = 9 April; 12 March + 30 days = 11 April).

## Outside this review
- The flow contains no remittance of this freight invoice; `08-RemittanceAdvice.xml` pays only the ore
  invoice `SM-INV-26-0312`. Whether the freight payment belongs in the flow is a question of the
  flow's composition (from broad; money notes it is not required).
- The flow records no arrival time of the train (timeline across documents; from logistics, see F4).
