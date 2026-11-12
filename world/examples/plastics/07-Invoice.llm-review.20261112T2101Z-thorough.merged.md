# LLM review: 07-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/07-Invoice.xml`, Git blob `a1e9b7e2c326a01d31d3b741f419d375d10a04e9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/07#F1 · High · Due date contradicts the payment term agreed in the transport plan
- XPath: `/Invoice/cbc:DueDate` = `2026-05-22`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-05-22`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-22`
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- Why: The contract for this freight agrees `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.` The consignment note is the waybill this invoice refers to (`/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`), issued `06-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-19`; 30 days from it is 2026-05-19 (recalculated in the merge: 11 days left in April + 19 = 30). The invoice counts 30 days from its own issue date (`/Invoice/cbc:IssueDate` = `2026-04-22`) and applies generic terms `XU-STD` (the same ID as Rinova's goods invoice, `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`), so it falls due three days later than agreed.
- Condition: the invoice's due dates follow the payment term agreed in the plan, or the plan's term is the one the invoice applies.
- Options: (a) due 2026-05-19, terms text from the plan (preferred by broad and the merge: the plan is the contract the invoice executes); (b) change the plan's term to the carrier's standard terms (30 days from invoice) if those were agreed (preferred by money).
- Needs decision: no
- From: broad (F2, with the discount), money (F1)

### plastics/07#F2 · High · Freight invoiced as bulk cargo, while the goods travelled in jumbo bags
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Bulk cargo down the river to the coast of Bayvarra, per tonne.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `River freight, bulk`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FB-BULK`
- Why: The invoiced service is bulk river freight. The consignment is not bulk: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:BulkCargoIndicator` = `false`, and the waybill the invoice refers to declares jumbo bags, `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`. Bulk and bagged cargo are different services (handling, rates); the Urvanian renderings say the same. The invoice contradicts the transport documents of the carriage it bills.
- Condition: the invoice line describes the service actually performed (river freight of goods in jumbo bags, per tonne), consistent with 03 and 06, in both languages.
- Options: (a) a freight item for bagged or general cargo with a matching seller's item ID (preferred: the transport documents agree among themselves); (b) if the carrier's tariff has only a "bulk" rate, say "bulk rate applied to bagged cargo".
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### plastics/07#F3 · Medium · Province of Ferrano in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "The political or administrative division of a country …, such as the name of its county, province, or state". The Bayvarran addresses of the flow use CountrySubentity (`Coastal State`). The parts counted 219 occurrences in 104 example files.
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; it is in `cbc:CountrySubentity` (with a code if Urvania has a list).
- Options: (a) move it to CountrySubentity (preferred); (b) keep in Region only if the world defines it as an economic region.
- Needs decision: no
- From: broad (F3), parties (F1), context (F2)

### plastics/07#F4 · Low · Settlement discount offered although the contract says "net"
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- XPath: `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `4306`
- Why: "30 days net" in the plan means payment without deduction; the invoice grants a 2 % settlement discount. A carrier may grant more than agreed, so this is not a contradiction in itself, but the two documents describe the payment terms of the same contract differently. (Broad included it in its High finding on the terms; the merge keeps the due date, which contradicts, apart from the discount, which only differs.)
- Condition: the payment terms in the plan and in the invoice describe the same arrangement (with or without settlement discount).
- Options: (a) drop the discount from the invoice, consistent with F1 option (a) (preferred by the merge); (b) state the discount in the plan as well (preferred by money, together with F1 option (b)).
- Needs decision: no
- From: money (F2), broad (F2, discount part)

### plastics/07#F5 · Low · Standard VAT on the international carriage of exported goods
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `20`
- Why: The service is the carriage of goods exported from Urvania to Bayvarra (05), and the goods themselves are invoiced as a VAT-free export (`10-Invoice.xml`, category `G`). In most VAT systems the transport of goods directly linked to their export is zero-rated or exempt (own knowledge: EU VAT Directive art. 146(1)(e)) (broad). Money refuted this for the world: the customer Rinova is established in Urvania, and the Urvanian exemption reason list has no reason for transport of exported goods (`EXP` covers goods, `SVCABROAD` services to customers established abroad), so the standard rate is consistent with the world's codes. The merge cannot settle it: a code list records the exemption reasons that exist, but whether the world's VAT law exempts such carriage is a tax-treatment judgment the story has to make.
- Condition: the tax category and rate of the freight follow the world's recorded rule for international carriage of exported goods.
- Options: (a) record in the world's tax rules that such carriage is taxable in Urvania and keep 20 % (the merge's preference: consistent with the existing list); (b) zero-rate or exempt it with a new exemption reason (broad's preference: common VAT practice).
- Needs decision: yes
- From: broad (F4); money considered and refuted it

### plastics/07#F6 · Low · Waybill referenced with an ID only; the plan whose terms are billed is not referenced
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`
- Why: AdditionalDocumentReference is "A reference to an additional document associated with this document". It does not say that it is the consignment note, which matters because the plan's term runs "from the consignment note". The plan `FB-TEP-26-0886` (04) and the contract `RR-FB-FW-2026` whose terms the invoice applies are not referenced.
- Condition: the waybill reference says what it refers to (document type), and the invoice references the document that sets its terms.
- Options: (a) add `DocumentTypeCode` to the waybill reference and a reference to the plan or contract (preferred); (b) at least the type.
- Needs decision: no
- From: broad (F5), logistics (F2), context (F3)

### plastics/07#F7 · Low · Rinova's waste-recovery permit in a freight invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: PartyAuthorization is "An authorization issued to this party"; the permit to recover plastic waste plays no part in billing the freight for a product (HS 390110). Context counted it in 14 example files, all 11 of this flow: master data copied into every document (IND5).
- Condition: no permit in the invoice unless the invoice acts on it.
- Options: remove it (preferred).
- Needs decision: no (parties said yes; removal changes no story, aligned with context and with 06)
- From: broad (F7), parties (F3), context (F4)

### plastics/07#F8 · Low · Contacts are operations and sales, not accounts
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Chartering desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact answers questions on the invoice (accounts receivable), the accounting customer's contact receives and pays it (accounts payable); here they are the carrier's chartering desk and Rinova's sales customer service. The parties carry one generic contact in every document of the flow.
- Condition: the accounting parties' contacts handle billing and payables, or are absent.
- Options: (a) role-specific contacts per party (preferred); (b) drop contacts the document does not need.
- Needs decision: no
- From: broad (F6), parties (F2), context (F5)

### plastics/07#F9 · Low · Both companies registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Both companies are registered on New Year's Day 1996; the parts counted 271 occurrences in 181 example files. It reads as a default value (IND5).
- Condition: each company's RegistrationDate belongs to its own history, or the shared date is explained in the story, or the element is absent.
- Options: (a) individual dates (preferred); (b) record a 1996 (re-)registration in the story; (c) drop it.
- Needs decision: yes (parties said no; aligned with broad, context and the wood merges)
- From: broad (F8), parties (F4), context (F6)

### plastics/07#F10 · Low · Italian text tagged as English
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: Renderings tagged `en-XU` are Italian street names ("Via del Riciclo", "Banchina del Fiume", "Piazza della Banca"), and the English legal form is Italian with a gloss. If Italianate exonyms are a world convention, it is not visible in the documents; the legal form is not a proper name. Parties counted the pattern in 101 of 250 examples.
- Condition: every rendering tagged `en-…` is English or a proper name used as such, and the convention is recorded.
- Options: (a) record the convention and render the legal form in English (preferred, aligned with 06 and the wood flow); (b) translate; (c) drop the second rendering.
- Needs decision: yes
- From: parties (F5)

## Checked and consistent
- Arithmetic (recalculated in the merge): 120 t × 1 495 XUF (base quantity 1 t) = 179 400 = line, line extension and tax-exclusive totals, equal to `06-Waybill.xml` freight; 20 % of 179 400 = 35 880; 179 400 + 35 880 = 215 280 = tax-inclusive = payable; 2 % of 215 280 = 4 305.6 → 4 306; settlement period 2026-04-22 to 2026-05-02 = 10 days (broad, money, logistics, context).
- Invoiced quantity 120 t equals the waybill's chargeable weight (logistics).
- Tax point 2026-04-22 = planned discharge day in 04/06 (service completed); issue 14:20 after discharge 08:00 (broad, money, logistics).
- Parties: Fiumella bills Rinova, the seller under CPT and the bill-to party of 03/04 (all parts).
- Payment means: credit transfer to Fiumella's own XUF account; RF reference `RF45FBINV260891` and the account pass `check_ids.py`; RTGS between two Urvanian parties is a legitimate channel; 8 % simple penalty interest, as Rinova's (broad, money, parties).
- Parties identical across the flow apart from the language renderings (parties).

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat the accounting parties, the seller of the goods as buyer — refuted because Rinova buys the freight service from Fiumella; the same companies (from broad, parties, context).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for 215 280 XUF — refuted: a legitimate choice of channel (from broad).
- `/Invoice/cbc:TaxPointDate` = `2026-04-22`: filler equal to the issue date — refuted because the service ends with the discharge on 2026-04-22 (from money).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BIC-shaped `CREVXUFR` could be real — refuted: positions 5–6 carry a fictional country's user-assigned code (from parties).
- `/Invoice/cbc:DefaultLanguageCode` = `en` with texts tagged `en-XU` — refuted because the untagged texts are English (from context).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `S` on carriage of exported goods — money refuted it with the world's exemption list; the merge could not settle it and keeps it as F5 (from money).

## Changed in the merge
- broad/F2, money/F1, money/F2 → F1 and F4: broad's finding on the terms split into the due date (High, contradicts the plan) and the discount (Low, only differs), combined with money's two findings; options of both parts kept, the merge preferring the plan as contract basis.
- broad/F1, logistics/F1, context/F1 → F2: combined, no change.
- broad/F4 → F5: kept as Low, Needs decision yes, against money's refutation, with both arguments; preferred option changed to recording the rule (consistent with the existing list).
- broad/F7, parties/F3, context/F4 → F7: Needs decision changed from yes (parties) to no.
- broad/F8, parties/F4, context/F6 → F9: Needs decision yes (parties said no), aligned with the wood merges.
- parties/F5 → F10: preferred option aligned with the wood flow.
- broad/F3, parties/F1, context/F2 → F3; broad/F5, logistics/F2, context/F3 → F6; broad/F6, parties/F2, context/F5 → F8: combined, no change of severity.
