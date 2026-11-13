# LLM review: 16-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/16-Invoice.xml`, Git blob `50bd624d3511a103ce29142147e25386c48bed58` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/16#F1 · High · "45 days net", but every due date is 30 days after issue
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-02`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XL-STD`
- Why: recalculated: 2026-03-02 + 45 days = 2026-04-16 (29 days to 31 March, 16 into April); 2026-04-01 is 30 days after issue. The terms text and all three due dates contradict each other. The same terms ID XL-STD with the note "45 days net." in the self-billed invoice 04 give exactly 45 days (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:DueDate` = `2026-03-24`, issued 2026-02-07: 21 days to 28 February + 24 = 45). The remittance on 2026-03-29 (18) fits either date.
- Condition: the payment terms text and every due date give the same period from the issue date, and terms with the same ID mean the same period in 04 and 16.
- Options: (a, preferred) all three due dates 2026-04-16, as the ginnery's standard terms say (all four parts that raised it); (b) if the mill was granted 30 days, give these terms their own ID and note ("30 days net."). Aligned with utilities b, which preferred the due dates where the same terms ID means 45 days elsewhere.
- Needs decision: no
- From: broad (F1), money (F1), logistics (F1), context (F1)

### cotton/16#F2 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: `O` of UN/EDIFACT 5305 means "Services outside scope of tax"; the line is a sale of cotton lint (supply type GOODS) from Lisavu, which has no general sales tax. The code's meaning names services, so the value does not fit what is invoiced. EN 16931 uses O for any supply outside the scope of VAT, goods included; under the agreed rule of semantic conformance that practice does not lower the severity, and it is a finding for the TC write-up. Money listed the treatment as consistent with the order 08 (same code there). 17 example files use `O` (`grep -rl --include='*.xml' 'schemeID="UN/EDIFACT EDED 5305">O<'`), 5 of them with GOODS (merger A's count).
- Condition: the tax category of the lint is a code whose meaning covers goods outside the scope of tax, or the deviation is recorded as a decision for the world.
- Options: (a, preferred) decide once world-wide how goods outside any sales tax are coded, and apply it to 01, 04, 05, 08, 16 and sea/29; (b) keep O and record the EN 16931 reading as a known deviation.
- Needs decision: yes
- From: broad (F2); money (checked as consistent with 08)

### cotton/16#F3 · Medium · Language code in `LocaleCode`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F3), parties (F1)

### cotton/16#F4 · Low · Tax scheme without identifier, named after a tax that does not exist
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `TaxScheme` is the taxation scheme within which the category is defined; here it has no `ID` and its name says that there is no such tax. A tax total of 0.000 in a scheme that does not exist states nothing a reader can identify. The same name is in 9 example files (`grep -rl --include='*.xml' '>No general sales tax<'`). Merger A carries context's IND6 counter-argument (an explicit zero tax total instead of an implied absence) for the same problem in 01.
- Condition: the zero tax total names a real scheme of the world (with an ID), or the treatment of Lisavu's sales without sales tax is decided once.
- Options: (a, preferred) one decision for the nine examples: a named Lisavan scheme with ID, or no tax total where no tax exists.
- Needs decision: yes
- From: broad (F4)

### cotton/16#F5 · Low · Category O with a rate of 0 %
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: `Percent` is "The tax rate for this category, expressed as a percentage." A category outside the scope of tax has no rate; 0 % states a rate that does not exist (and reads like a zero-rated supply). No part raised it; added by the merge for alignment with merger A and the earlier flows (utilities, road).
- Condition: no rate is given for a category outside the scope of tax.
- Options: (a, preferred) drop `Percent` in both places.
- Needs decision: no
- From: merge

### cotton/16#F6 · Low · Export invoice without delivery terms, delivery or transport document
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198`
- XPath: `08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: the invoice bills lint shipped from Lisavu to Bayvarra on 2026-03-02 (13), issued the same day after the bill of lading. The order agreed FOB Port of Selanu, which defines what the price includes (no freight: the forwarder bills it separately in 17) and is the basis of the customs values in 11 and 15. The invoice carries no delivery terms, no delivery (date shipped, place) and no reference to the bill of lading TOL-BL-26-0206, so it does not show what its price covers or which shipment it bills; an export commercial invoice normally states them (own knowledge). A completeness remark.
- Condition: the invoice states the delivery terms and the delivery (or refers to the bill of lading or shipment) of the goods it bills.
- Options: (a, preferred) `DeliveryTerms` FOB Port of Selanu, a `Delivery` with the actual delivery date 2026-03-02 at the Port of Selanu, and a document reference to TOL-BL-26-0206.
- Needs decision: no
- From: broad (F5), logistics (F3), context (F3)

### cotton/16#F7 · Low · `PackQuantity` 1 / `PackSizeNumeric` 227: the nominal bale weight as a pack size
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:PackQuantity` = `1`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "The number of items in a pack of this item", a count; 227 is the nominal bale weight in kilograms ("compressed bales of about 227 kg"). Logistics and context read it as a weight in a count element (Medium). Counter-argument (merge): the item is invoiced per kilogram (`InvoicedQuantity` 6129 KGM, price per 1 KGM), so "227 one-kilogram units per pack" is a possible reading of the definition, though bales are only "about" 227 kg. Cannot be settled from the definition alone. Same in 02, 07, 08, 10, 11 and 15.
- Condition: the pack elements, where present, state a count whose unit is clear; otherwise the bale weight is carried where a weight belongs.
- Options: (a, preferred) drop `PackQuantity`/`PackSizeNumeric`, with the nominal bale weight as an item property (and, if wanted, the 27 bales in the description); (b) keep them and record the reading as a convention.
- Needs decision: yes
- From: logistics (F2), context (F2), broad (F10)

### cotton/16#F8 · Low · The accounting customer's contact: Purchasing, Customer service officer, Sales
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: for the accounting customer of an invoice an accounts-payable (or at least a purchasing) contact fits; name (buying) and job title and department (selling) also contradict each other. The combination is in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: name, job title and department agree with each other and with the accounting-customer role.
- Options: (a, preferred) an accounts-payable contact; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad (F7), parties (F2)

### cotton/16#F9 · Low · Classing results carried as the applicant's remarks
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Certificate/Remarks` is "Remarks by the applicant for the certificate"; the text is the classer's result, and grade and staple are already item properties of the same item.
- Condition: the classing result is not carried as an applicant's remark.
- Options: (a, preferred) drop the remark (micronaire, if needed, as an item property).
- Needs decision: no
- From: broad (F8)

### cotton/16#F10 · Low · Origin area in `Region` here, in `District` in the farm's address
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: the same area is a `District` in the farm's address and a `Region` here; a consistency remark.
- Condition: the north coast is in the same address element wherever it occurs in the flow.
- Options: (a, preferred) `District` in the origin address.
- Needs decision: no
- From: broad (F9), context (F4)

### cotton/16#F11 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Ginnery and mill, in two registers, share 1 January 1996, which occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F3)

## Checked and consistent
- 6129 kg × 0.988 XLC per 1 kg = 6055.452 XLC = line extension = tax-exclusive = tax-inclusive = payable amount (no allowances, charges or prepayment); tax 0.000 on a taxable 6055.452.
- `OrderReference` LTM-PO-26-0198 and order line 1 resolve to 08: same item, quantity, price and buyer's accounting cost 2200 "Raw cotton" ("The buyer's accounting code"); the invoice is in the requested currency XLC.
- `check_ids.py`: RF reference RF46SCGINV260210 and the ginnery's account XL31BSEL0020004922263 pass; the account is the one the ginnery pays from in 06 and into which 18 pays.
- The remittance advice 18 refers to this invoice with its issue date 2026-03-02 and pays the full 6055.452 XLC on 2026-03-29, quoting the RF reference.
- Penalty interest 6 % a year, simple, the same as under XL-STD in 04; RTNS over the Trade Accord rail with shared charges fits a cross-border payment.
- Supplier and seller (ginnery), customer and buyer (mill) agree with 08 and 18; the ginnery's description, with en-XL tags and both renderings of its legal form, is identical to 01, the mill's to 08 and 18 (parties).
- The classing certificate (signed 2026-02-20) predates the invoice; item SCG-LINT, HS 520100 and quantity agree with 08, 10, 11 and 15.

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode`: the buyer's cost code on the seller's invoice — refuted: "The buyer's accounting code", which the seller quotes from the order (08 gives the same code) (from broad).
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR`: shared charges making the ginnery receive less than invoiced — refuted because 18 reports the full amount remitted and a zero balance; sharing bank charges is the usual cross-border arrangement (from money).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`: customs-trader numbers as master data the invoice does not use — refuted: the commercial invoice of an export sale accompanies the export and import declarations, where the trader numbers are used (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`: the seller's sales desk on its sales invoice — fits the role (from parties).
- `/Invoice/cac:InvoiceLine/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`: a certificate in an invoice line — refuted because the grade it certifies determines the price invoiced (from context).
- `/Invoice/cbc:PaymentCurrencyCode` = `XLC`: payment currency equal to the document currency as a filler — refuted by money and context (see "Refuted in the merge" for broad's finding).

## Refuted in the merge
### broad/F6 · Low · Payment currency equal to the document currency
- XPath: `/Invoice/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/Invoice/cbc:DocumentCurrencyCode` = `XLC`
- Why (broad): a payment currency equal to the document currency adds nothing (filler); the mill pays from a Lume account (18), but in coral, the invoice currency.
- Condition (broad): the payment currency is absent or differs from the document currency. Options: drop it; or keep it with a note that the mill must pay in coral although its account is in Lume.
- Refuted because: the buyer is in Bayvarra and pays from a Lume account (18); stating that payment is expected in coral is information the buyer needs (money, context), and leaving it out would make the payment currency something implied by absence, which the agreed rules (IND6) avoid. No exchange rate is added, so nothing is redundant.

## Changed in the merge
- F5 added by the merge (no part raised it), for alignment with merger A (cotton 01–09) and earlier flows.
- logistics/F2, context/F2 (Medium) + broad/F10 (Low) → F7: Low with "Needs decision: yes" (the item is invoiced per kilogram; same as cotton/10#F7).
- broad/F2 → F2 and broad/F4 → F4: written out in full (broad referred to cotton/01) and aligned with merger A's rows (O for goods Medium/yes; scheme without ID Low/yes).
- broad/F6 moved to "Refuted in the merge".
