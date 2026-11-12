# LLM review: 02-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/02-Invoice.xml`, Git blob `b2993194ed77fe144060459952d69428ed29f5bc` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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


### utilities/02#F1 · High · Excise per-unit amounts do not produce the excise amounts, and both tiers show the same rate
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TierRange` = `The first 50,000 kWh of the month`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TierRange` = `Above 50,000 kWh: the industrial rate`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`
- Why: PerUnitAmount is "Where a tax is applied at a certain rate per unit, the rate per unit applied", here per BaseUnitMeasure 1 kWh. At 1 XUF/kWh the first tier ("the first 50,000 kWh of the month") yields at most 50000, not 60000, and the second tier, called "the industrial rate", has the same rate as the first. Redone by the merge: the amounts work out only for the electricity of lines 1 and 2, 412800 + 18600 = 431400 kWh, with 50000 × 1.2 = 60000 and (431400 − 50000) = 381400 × 0.6 = 228840. At 1 XUF/kWh the tiers would together tax 288840 kWh, which matches no quantity of the invoice (431400 kWh electricity, 492600 kWh with the gas). Including the gas, (492600 − 50000) gives 228840 / 442600 ≈ 0.517, no plausible rate; tiers per meter (factory 277680 + warehouse 22320 = 300000) do not give 288840 either. The subtotals also do not say that the excise applies to electricity only, while the tier text speaks of all kWh of the month.
- Condition: For each excise tier, PerUnitAmount (in subtotal and category) × the tier's taxed quantity = the tier's TaxAmount, the tiers' quantities add up to the quantity the excise applies to, the rates differ where TierRange says they do, and the tiers name the supply they apply to.
- Options: (a, preferred) PerUnitAmount 1.2 and 0.6 in subtotal and category, keeping the amounts, and a TierRange or category name that says electricity and the taxed quantity (e.g. "50,000 kWh of 431,400 kWh of electricity"); (b) if 1 XUF/kWh is meant, recompute both tiers and the totals, which changes VAT, payable amount, the settlement discount, remittance 04 and statement 01's energy tax report.
- Needs decision: no
- From: broad (F1), money (F1), logistics (F1), context (F2)

### utilities/02#F2 · High · Due date contradicts "30 days net"
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- XPath: `/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-12`
- Why: Redone by the merge: 2026-04-02 + 30 days = 2026-05-02; the three due dates are 2026-04-23, 21 days after issue (23 days after the end of the invoice period). The settlement period does follow the note's 10 days, so the note is the stated term and the due dates contradict its net term. Refutation attempted: "30 days net" could count from the end of the invoice period (2026-03-31 + 30 = 2026-04-30) or from receipt; neither gives 2026-04-23. The same 2026-04-23 occurs in 06 ("30 days net") and in 13 ("45 days net").
- Condition: The due dates and the net term in the note give the same date.
- Options: (a, preferred) due dates 2026-05-02: the terms ID `XU-STD` means "30 days net; 2 % discount when paid within 10 days" with the due date 30 days after issue in every other example that carries it (checked by the merge over `world/examples/*/*.xml`: 12 invoices in the energy, ore, plastics, rail, road, tender and waste flows, e.g. `energy/02-Invoice.xml`), so the note is the world's standard term and the due dates are the outlier; remittance 04 stays within both terms; (b) note "21 days net" with a terms ID of its own, if utility bills are meant to have shorter terms (money's and context's preference, which keeps the flow's 2026-04-23).
- Needs decision: no
- From: broad (F2), money (F2), context (F1)

### utilities/02#F3 · Medium · Excise TaxableAmount holds the tax, not the taxable base
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `228840`
- Why: TaxableAmount is "The net amount to which the tax percent (rate) is applied to calculate the tax amount." In both excise subtotals it equals the TaxAmount, as if a 100 % tax had been applied. The excise is per kWh; the net amount of the electricity taxed in the two tiers would be 50000 × 27.3 = 1365000 and 381400 × 27.3 = 10412220 (together the 11777220 of lines 1 and 2).
- Condition: Each excise subtotal either has no TaxableAmount or carries the net amount of the supply taxed in its tier.
- Options: (a, preferred) leave TaxableAmount out (0..1), since BaseUnitMeasure, PerUnitAmount and TierRange describe a per-unit tax; (b) the net amounts of the tiers.
- Needs decision: no
- From: money (F3), context (F3), broad (F1, part), logistics (F1, part)

### utilities/02#F4 · Medium · Electricity and gas classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture." The world's own SupplyTypeCode list (`world/codelists/gc/SupplyTypeCode.gc`, verified by the merge) defines GOODS as "A supply of goods, including energy and water delivered through a network." and SERVICES as "A supply of services." Electricity (lines 1, 2) and natural gas (line 3) are GOODS by the list's own definition, as in VAT practice modelled on the EU VAT Directive (Art. 15(1), own knowledge; context). The broad part refuted it because the world's VAT law is fictional, and context left the treatment to the story; the world's list settles the question, so the merge keeps Medium (a code whose meaning does not fit the value).
- Condition: The supply type of the electricity and gas lines is GOODS.
- Options: (a, preferred) GOODS on all three lines; (b) SERVICES only if the world's list and tax story are changed to treat network energy as a service.
- Needs decision: no
- From: money (F4), context (F8, Low, yes); broad refuted it

### utilities/02#F5 · Medium · OriginatorParty used for the warehouse occupant, not for the party who originated an order
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:PurchaseReference/cbc:ID` = `FE-C-0047120`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: InvoiceLine/OriginatorParty is "The Party who originates the Order to which the Invoice is related." There is no order in this flow; the supply runs under Valdara's supply contract, and `03-UtilityStatement.xml` says it is "under the customer's contract" with Valdara as UtilityCustomerParty. Castrano Logistics is the party at whose warehouse the electricity is consumed; nothing says it ordered anything.
- Condition: Castrano Logistics appears on line 2 only in an element whose definition fits its role (the party the supply is delivered to), or the story says Castrano originated the order for this connection.
- Options: (a, preferred) Delivery/DeliveryParty on line 2, next to the delivery location; (b) leave the party out and let PurchaseReference and AccountingCost name the warehouse; (c) story: Castrano requested the warehouse connection under Valdara's contract.
- Needs decision: no
- From: broad (F3), parties (F2), context (F4)

### utilities/02#F6 · Medium · Province in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division, for which UBL has CountrySubentity. The Bayvarran addresses of the world use CountrySubentity. Recounted: 219 occurrences in 104 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: Urvanian provinces are given in CountrySubentity (with a code where the world has a list), not in Region.
- Options: (a, preferred) move to CountrySubentity; (b) keep Region only if the story makes the province an economic or geographic region.
- Needs decision: no
- From: broad (F4), parties (F1)

### utilities/02#F7 · Low · Billing reference to line 2 of an earlier invoice with no stated purpose
- XPath: `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0211`
- XPath: `/Invoice/cac:BillingReference/cac:BillingReferenceLine/cbc:ID` = `2`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `February's estimate of 17,200 kWh was 750 kWh too high, as the actual reading shows.`
- Why: BillingReference is "A reference to a billing document associated with this document." This ordinary commercial invoice (380) for March refers to line 2 of the February invoice FE-INV-26-0211 (not an example of the flow, acceptable in itself) without saying why. The only link in the flow is statement 03, which corrects February's estimate for the warehouse meter (this invoice's line 2). But nothing in this invoice applies a correction: line 2 bills 18600 kWh × 27.3 = 507780, the metered March quantity, with no allowance, charge or credit for 750 kWh (utilities/03#F1). The reference is either a filler or a story element that is not told.
- Condition: Either the invoice shows what it does with FE-INV-26-0211 line 2 (e.g. a correction amount or a note), and it agrees with statement 03, or the reference is absent.
- Options: (a) remove the reference (preferred if the March reading already settles February, see utilities/03#F1); (b) keep it with a correction on line 2 (e.g. an allowance of 750 × 27.3 = 20475) or a note that uses it.
- Needs decision: yes
- From: broad (F5), logistics (F2), context (F5)

### utilities/02#F8 · Low · Electricity and gas booked as "Raw materials and parts"
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`
- Why: AccountingCost is the buyer's accounting code applied to the invoice as a whole. Electricity and gas are energy costs, not raw materials and parts; the same text occurs in 12 files (`grep -rl --include='*.xml' 'Raw materials and parts'`, recounted), mostly Valdara's purchases of goods, and 3100 equals Valdara's ISIC class. Line 2 shows that Valdara uses separate cost centres. Copied master data.
- Condition: The invoice-level accounting cost is Valdara's energy cost account (as in 01 and 03), or is absent.
- Options: (a, preferred) an energy or factory-overhead cost account; (b) leave it out at document level and give cost centres per line.
- Needs decision: no
- From: broad (F6), money (F5), context (F6)

### utilities/02#F9 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: A domestic energy invoice uses neither the customer's customs trader number nor its stock-exchange listing; the block is identical in all 75 examples with Valdara's full data (parties part). Copied master data (section 4.8). The context part also listed the ServiceProviderParty (Castrano Logistics); broad and parties showed that it has a reason here (line 2 bills the warehouse Castrano runs for Valdara), so the merge leaves it out of this finding.
- Condition: Every identifier and listing in the customer party has a use in this invoice, or is absent.
- Options: (a, preferred) drop the customs trader ID and the security listing; (b) keep them only with a stated reason.
- Needs decision: no
- From: broad (F7, part), parties (F3), context (F7, part)

### utilities/02#F10 · Low · Customer's contact is its sales order desk, not someone who handles supplier invoices
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact receives and settles the invoice (accounts payable or utilities purchasing). Valdara's contact is its own sales order desk with a customer service officer, the contact it gives its own customers, whatever role it has.
- Condition: The accounting customer's contact deals with incoming invoices or utilities purchasing, and name, job title and department agree.
- Options: (a, preferred) an accounts payable contact for Valdara in the billing documents of this flow; (b) drop the contact.
- Needs decision: no
- From: broad (F7, part), parties (F4), context (F7, part)

### utilities/02#F11 · Low · Delivery location of line 2 is a company name in free text, not the identified consumption point
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Castrano Logistics warehouse, Ferrano`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID` = `FE-CP-4160-07`
- Why: A location names the place, not the company, and identifies it where the same place is identified elsewhere. Statement 03 identifies the same point as FE-CP-4160-07 with its address (Via del Magazzino 24, 4130 Ferrano); the line only describes it by the company's name, so it can be linked to the statement only through the meter number. Line 1 (the factory) has no delivery location at all.
- Condition: The delivery location of line 2 is absent or identifies the warehouse consumption point (ID and/or address) as statement 03 does.
- Options: (a, preferred) give the location the consumption point's ID FE-CP-4160-07 (and address); (b) remove the Delivery aggregate, as the meter reference already identifies the point.
- Needs decision: no
- From: parties (F5), logistics (F3)

### utilities/02#F12 · Low · Italian text tagged as English (street and legal form)
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Added by the merge for alignment with the wood, plastics and rail merges and with utilities/01#F16 (where the parties part refuted it as proper names). The renderings are tagged en-XU but are Italian. For: proper names may keep their form, and the world uses Italianate English names consistently. Against: the legal form is a description, and no convention is recorded. Cannot be settled; 217 such street renderings in 102 files and 112 tagged legal forms (recount over `*.xml`).
- Condition: Either the convention is recorded in the world's story, or the en-XU renderings are English.
- Options: (a, preferred) record the convention for proper names and render the legal form in English; (b) English renderings throughout.
- Needs decision: yes
- From: merge

## Checked and consistent
- Lines: 412800 × 27.3 = 11269440; 18600 × 27.3 = 507780; 61200 × 8.4 = 514080; sum 12291300 = LineExtensionAmount = TaxExclusiveAmount; LineCountNumeric 3.
- Tax: excise 60000 + 228840 = 288840; VAT base 12291300 + 288840 = 12580140; 20 % = 2516028; TaxInclusiveAmount = PayableAmount = 12291300 + 288840 + 2516028 = 15096168; CalculationSequenceNumeric 1 (excise) before 2 (VAT) agrees with VAT on the excise.
- Settlement discount: 2 % × 15096168 = 301923.36 → 301923; settlement period 2026-04-02 to 2026-04-12 = 10 days; remittance 04 pays on 2026-04-10 with exactly this discount.
- Lines 1 and 2 agree with `01-UtilityStatement.xml` and `03-UtilityStatement.xml` (quantities, prices, amounts, meters FE-M-881204 and FE-M-881377, ParentDocumentLineReferenceID 1 and 2); the statements are issued after this invoice.
- Gas line 3: 1350 m³ at 4 bar converted to 61200 kWh agrees with the grid operator's statement `energy/01-UtilityStatement.xml` (meter FG-G-20417, 1350 m³ × 4.9477 = 6679 m³ at standard conditions × 9.163 kWh/m³ = 61200 kWh; logistics part). The factor fits 4 bar gauge; 9.16 kWh/m³ is within the range of low-calorific natural gas (own knowledge). The broad and context parts' estimates (absolute pressure, 11–12 kWh/Nm³) also land in a plausible range.
- Payee account XU080351041600000004084431 (IBAN-like check OK), named Ferrano Energy SUA, branch code 03510-41600 matching the account's digits; the same account and RF58FEINV260313 (ISO 11649 OK) are used in `04-RemittanceAdvice.xml`. ISIN XU0001042501 OK. CREVXUFR cannot be a real BIC (country part XU).
- Penalty interest 8 % per annum, simple. Purpose codes ELEC (lines 1, 2) and GASB (line 3) are ISO 20022 ExternalPurpose1Code values for electricity and gas bills.
- Ferrano Energy and Valdara Industries are described identically in 01–04 and elsewhere; Castrano's register number XU-R-104411 on line 2 matches statement 03; BuyerCustomerParty and SellerSupplierParty have no "if different" condition.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: electricity and gas as services — refuted by broad because the world's VAT law is fictional. The merge disagrees: the world's own SupplyTypeCode list defines GOODS to include network energy; made F4 (from broad).
- `/Invoice/cac:SellerSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID`, `/Invoice/cac:BuyerCustomerParty`: repeat the accounting parties — refuted, the definitions ("The seller.", "The buyer.") have no "if different" condition (from broad, context, parties).
- `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:ID`: category S for an excise — refuted, UNCL 5305 S is a standard rate not limited to VAT (from broad, context).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a routine utility payment — refuted, plausible for about 15 million XUF from a large company (from broad).
- `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate`: previous invoice issued on a Sunday — refuted, automatic issue on any day (from broad).
- `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount`: omits the excise — refuted, net of all taxes by definition; TaxInclusiveAmount includes it (from money).
- `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:Name`: "Energy tax" as a category name — refuted as minor, it identifies the category within EXC (from money).
- `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID`: money effect of the reference — none; its presence is F7 (from money).
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: computed on the tax-inclusive amount — refuted, the note's "2 % discount when paid" reads on the payable amount; whether a discount reduces the VAT is a tax question (from money; logistics had put it under "Outside").
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID`: copied master data — refuted, it explains why Valdara pays for the warehouse on line 2 (from parties; context's contrary view corrected in F9).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department`: billing contact in Sales — refuted, customer service in sales is a usual contact for invoice questions (from parties).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a real BIC — refuted, the country part XU is not an ISO 3166 code (from parties).
- `/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:ID`: a meter number in a purchase reference — refuted, UBL 2.5 names "meter" as an object of PurchaseReference (from logistics).
- `/Invoice/cac:PurchaseReference/cbc:ID`: a supply contract in PurchaseReference — refuted, "a subscription number" is a named example (from context).
- `/Invoice/cac:InvoiceLine[3]/cbc:Note`: "4 bar" gauge or absolute — refuted, the energy flow's factor 4.9477 shows gauge and the arithmetic holds (from logistics); the conversion in a note — refuted, no structured element holds volume and pressure (from context).

## Changed in the merge
- broad/F1 → F1 and F3: TaxableAmount = TaxAmount split off into its own Medium finding, as money and context had it (different element, different condition).
- context/F8 (Low, yes) → F4 Medium, no: the world's SupplyTypeCode list settles the meaning; money's Medium kept.
- context/F7 → F9 and F10: master data and contact split; the ServiceProviderParty XPath dropped from F9 because broad and parties show its use on line 2.
- broad/F7 → F9 and F10: same split.
- parties/F5 and logistics/F3 → F11: combined (same element), options from both.
- F2: preference set to the due dates 2026-05-02, following broad's condition: XU-STD means 30 days in all 12 other invoices that carry it; money's and context's "21 days net" kept as option (b). Aligned with merger B's reasoning for 13 (XL-STD).
- F12 added for alignment with earlier flows' merges.

## Outside this review
- `01-UtilityStatement.xml` reports this invoice's whole excise (288840) as the energy tax of one consumption point: utilities/01#F1.
