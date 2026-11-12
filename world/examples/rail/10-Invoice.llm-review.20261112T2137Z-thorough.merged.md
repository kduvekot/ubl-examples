# LLM review: 10-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/10-Invoice.xml`, Git blob `13c4e7c68f3fa88f617d5f615a40ea35e815c2cd` (committed)
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

### rail/10#F1 · High · Due date and discount differ from the payment terms agreed in the transport plan
- XPath: `/Invoice/cbc:DueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-17`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `2621`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `08-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-14`
- Why: The invoice bills the rail freight agreed in the plan 03 (it references the waybill FRC-WB-26-0334 of that transport). The plan's terms are "30 days net from the consignment note"; the consignment note is the waybill of 14 April, so payment falls due on 14 May (14 April + 30 days, recalculated in the merge), with no discount. The invoice counts 30 days from its own date (17 April → 17 May) and offers a 2 % settlement discount that "net" excludes. Refutation tried: the invoice's terms ID XU-STD (the carrier's standard terms) could override, but the plan is the specific agreement for this transport and states different terms; nothing in the flow says the standard terms prevail. Two documents of the flow state different payment terms for the same freight.
- Condition: Due dates and any settlement discount in this invoice follow the terms agreed in 03, or 03 states the terms this invoice applies.
- Options: (a) preferred: the invoice follows the agreement: all three due dates 2026-05-14, no settlement discount (broad; the agreement precedes the invoice); (b) align the plan's terms with the carrier's standard terms used here (30 days from the invoice, 2 % within 10 days), which the same carrier also applies in ore/06 (money's preference).
- Needs decision: no
- From: broad (F1), money (F1)

### rail/10#F2 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (CountrySubentity), as the flow's Bayvarran addresses use (`11-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 example files.
- Condition: No address in this example carries the province in Region; where given, it is in CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it.
- Needs decision: no (broad, context yes; aligned with rail 01–05, wood, plastics)
- From: broad (F2), parties (F1), context (F1)

### rail/10#F3 · Low · Late-payment penalty may differ from the penalty agreed in the plan
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:TimeBasisCode` = `ANN`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- XPath: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- Why: The plan encodes its penalty in PenaltySurchargePercent ("the penalty for payment after the settlement period, expressed as a percentage of the payment"), i.e. as a late-payment penalty of 5 % per day, capped at 25 %; this invoice charges late payment with 8 % a year, simple interest. If the plan's penalty is for late payment, the two contradict each other; if it is for late delivery (the likelier reading of "5 % of the freight per day late"), the plan uses the wrong element (a finding of 03, Medium with a decision in the other merger's decisions) and this invoice is right. Lowered from money's Medium to Low with a decision, because the merge cannot settle which reading is meant.
- Condition: The late-payment penalty in this invoice and any late-payment penalty stated in 03 agree.
- Options: (a) preferred: treat the plan's penalty as a late-delivery penalty and fix its encoding in 03 (this invoice stays as it is); (b) if the plan means late payment, the same penalty in both documents.
- Needs decision: yes (which penalty the agreement means)
- From: money (F2)

### rail/10#F4 · Low · Outbound freight booked as "Raw materials and parts"
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `One container slot on the container train to the distributor's siding.`
- Why: AccountingCostCode/AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". Valdara pays the carriage of its finished benches to its customer under DAP, an outbound distribution cost, not a purchase of raw materials or parts. The code fits Valdara's inbound freight (ore/06 bills ore to the factory with the same code); freight has its own account elsewhere in the world (`plastics/07-Invoice.xml:/Invoice/cbc:AccountingCost` = `Freight`). The code 3100 also equals Valdara's ISIC class, perhaps a coincidence.
- Condition: The buyer's accounting code and text name a cost account that fits outbound freight on sales.
- Options: (a) preferred: a freight-out / distribution cost account of Valdara; (b) drop both if Valdara's chart of accounts is not part of the story.
- Needs decision: no
- From: broad (F3), money (F3), context (F2)

### rail/10#F5 · Low · Contacts do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Freight desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: On an invoice the accounting supplier's contact answers billing questions (accounts receivable) and the accounting customer's contact deals with the invoice and its payment (accounts payable, or transport purchasing as buyer of the freight). Here the carrier's operations planners (used for Ferrano Rail Cargo in every role of the flow) and Valdara's sales order desk are given.
- Condition: The accounting parties' contacts are billing/accounts (or purchasing) functions, or absent.
- Options: (a) preferred: accounts-receivable / accounts-payable contacts; (b) drop Contact.
- Needs decision: no
- From: broad (F4), parties (F3, F4)

### rail/10#F6 · Low · Customer master data the freight invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: A freight invoice from the carrier does nothing with the customer's stock-exchange listing, share capital or warehousing provider (section 4.8).
- Condition: Every legal-entity and service-provider element of the customer has a purpose in the invoice.
- Options: (a) preferred: drop them here; (b) keep share capital only where the world's invoicing rules require it, and then for the supplier, not the customer.
- Needs decision: no
- From: broad (F5), parties (F5), context (F3)

### rail/10#F7 · Low · Reference to the waybill with only an ID
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`
- Why: The reference resolves to the waybill 08, the transport document of the service billed, but carries no DocumentTypeCode or DocumentType; an invoice's AdditionalDocumentReference can be any document. Broad refuted it ("the WB number prefix and the context make the waybill obvious"); the merge disagrees: a number prefix is the issuer's convention, not a statement of the document's type, and the checklist asks a reference with only an ID to say what it refers to where that is not obvious (aligned with plastics and air, "references with ID only": Low).
- Condition: The reference says what kind of document it is (type code or text).
- Options: (a) preferred: add DocumentTypeCode (the world's code for a consignment note) or DocumentType; (b) reference the waybill through DespatchDocumentReference, if the owner reads a consignment note as such.
- Needs decision: no
- From: logistics (F1); broad listed it under "Considered and refuted"

### rail/10#F8 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5); these are tagged `en-XU` but are Italian (own knowledge). A world convention for street names cannot be ruled out; the legal forms are the stronger case. 217 such renderings in 102 example files.
- Condition: Every rendering tagged as English is English, or the world records the Italianate English usage.
- Options: (a) record the convention (preferred if intended); (b) translate; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F2)

### rail/10#F9 · Low · Supplier's registration date 1996-01-01
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Not raised by any part of this run; added by the merge for consistency with rail 01–05 and earlier flows (271 occurrences in 181 example files): the date reads as a default, unless a 1996 (re-)registration is part of the story.
- Condition: Each company's registration date is its own, or the world records a general 1996 registration.
- Options: (a) preferred: own date per company; (b) record a 1996 re-registration in the story.
- Needs decision: yes
- From: merge

## Checked and consistent
- Arithmetic (recalculated in the merge): 2 × 54 600 = 109 200 XUF = line, LineExtension, TaxExclusive and Taxable amounts; 20 % × 109 200 = 21 840; 109 200 + 21 840 = 131 040 = TaxInclusive = Payable. Settlement discount 2 % × 131 040 = 2620.8, stated 2621 (rounded; computed on the tax-inclusive amount as in ore/06 and plastics/07); settlement period 17 to 27 April = 10 days; due date 30 days after issue.
- Price 54 600 XUF per container slot = the waybill's rail freight per container (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`); 2 service units (E48) = the two containers FRXU1044175 and FRXU1044180; the item text agrees with the waybill's delivery location and the plan's slot contract.
- Reference `FRC-WB-26-0334` resolves to the waybill 08. Valdara as accounting customer and buyer agrees with BillToParty in 02 and 03, the consignor that prepays under DAP (01, 03, 08). Issue 17 April is after the planned delivery (15 April) and within the plan's validity.
- Tax: S 20 % with SupplyTypeCode SERVICES on the line and in the subtotal; both parties registered for national VAT in Urvania.
- Payment: RF13FRCINV260336 and the account XU92 0351 0417 0000 0000 5236 45 pass their checks (check_ids.py, from the parts); branch 03510-41700 matches the account; account name `Ferrano Rail Cargo SRU` = supplier's registration name; BIC-like `CREVXUFR` carries the user-assigned country XU; PaymentMeansID 1 points to PaymentMeans 1; ANN = year (UNECE Rec. 20).

## Considered and refuted
- `/Invoice/cbc:TaxPointDate` = `2026-04-17`: tax point should be the completion of the service (15 April) — refuted because the world's tax point rules are not stated as completion-based, the flow carries no actual delivery date, and the invoice date is a legitimate tax point in many VAT systems. (from broad, money)
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S`: standard-rated VAT on freight linked to an export, which many real systems exempt (e.g. EU VAT Directive Art. 146(1)(e)) — refuted because the customer is established in Urvania, the XU exemption list has no such exemption (only EXP for goods and SVCABROAD for customers abroad), and the world consistently charges Urvanian VAT on freight for Urvanian customers (plastics/07). (from money, broad)
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a domestic payment — refuted: a legitimate choice; nothing contradicts it. (from money)
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: redundant next to the accounting customer — refuted: UBL defines the buyer as a role of its own. (from context)
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2`: unit E48 (service unit) for container slots — checked, fits. (from context)
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `One container slot on the container train to the distributor's siding.`: only the rail slots are billed although the carrier also hauls the boxes to the hub — refuted within the logistics lens (whether the haulage is priced into the slot is not contradicted by any value); the merge agrees, no example prices the haulage separately. (from logistics)
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`: the referenced waybill is typed CMR although rail is billed — refuted as a finding of this example: the problem lies in the waybill (08, F1 of its merged review). (from logistics)
- Broad's refutation of the ID-only reference is carried into F7, where the logistics finding stands. (from broad)

## Changed in the merge
- broad/F1, money/F1 → F1: combined; both options kept, preference (a) (invoice follows the agreement) because the plan is the specific agreement; refutation via XU-STD added.
- money/F2 (Medium, yes) → F3: lowered to Low, because the contradiction depends on which reading of the plan's penalty is meant and cannot be settled (skill: uncertain findings stay Low with a decision); aligned with the 01–05 merge, which treats the plan's element as misused in either reading.
- broad/F2, parties/F1, context/F1 → F2: needs decision no (broad, context yes).
- broad/F3, money/F3, context/F2 → F4; broad/F4, parties/F3, F4 → F5; broad/F5, parties/F5, context/F3 → F6: combined.
- logistics/F1 → F7: kept against broad's refutation, with the counter-argument.
- parties/F2 → F8: count replaced by 217 in 102 files.
- F9 added by the merge (registration date 1996-01-01).

## Outside this review
- The waybill's freight charge of 54 600 XUF is given on the first container only, while this invoice bills two slots: a finding of the waybill (08, F17 of its merged review). (from logistics)
